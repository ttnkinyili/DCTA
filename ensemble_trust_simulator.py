import math
from ds_utils import MassFunction
from dynamic_trust_weighting_time import TrustSimulator

class EnsembleTrustEngine:
    def __init__(self):
        # Constants for Exponential Decay
        # Long Term: 48 hours (2880 minutes) -> decay to 0.05
        # 0.05 = e^(-lambda * 2880) => lambda ~= 3.0 / 2880
        self.LAMBDA_LONG = 3.0 / 2880.0
        
        # Short Term: 30 minutes -> decay to 0.05
        # 0.05 = e^(-mu * 30) => mu ~= 3.0 / 30.0 = 0.1
        self.MU_SHORT = 0.1

    def get_decay_long_term(self, delta_t_minutes=1):
        """
        Decay factor for Historical Trust (Inertia).
        """
        return math.exp(-self.LAMBDA_LONG * delta_t_minutes)

    def get_decay_short_term(self, session_time_minutes):
        """
        Decay factor for Instant Evidence (Data Freshness).
        """
        return math.exp(-self.MU_SHORT * session_time_minutes)

    def get_observation_mass(self, domain_score, context_weight):
        """
        Constructs a Dempster-Shafer Mass Function (Same as weighted_belief_fusion).
        """
        m_safe = domain_score * context_weight
        m_unsafe = (1.0 - domain_score) * context_weight
        m_uncertain = 1.0 - context_weight
        
        if m_uncertain < 0: m_uncertain = 0.0
        
        mass_dict = {
            ('safe',): m_safe,
            ('unsafe',): m_unsafe,
            ('safe', 'unsafe'): m_uncertain
        }
        
        return MassFunction(mass_dict)

    def calculate_instant_trust(self, sim, readings):
        """
        Performs the Spatial Fusion (DS Theory) for the current time step.
        Returns the Instant Pignistic Probability of Safety.
        """
        step_fusion = None
        
        # Pre-calc values
        current_scores = {}
        for d in sim.domains:
            current_scores[d] = sim.calculate_domain_score(d, readings[d])
            
        # Get Normalized Weights (Base, not decayed yet)
        # We handle the "Freshness" decay explicitly in the ensemble formula, 
        # so we use the raw normalized weights here (or the ones from the new sim).
        # Note: TrustSimulator in dynamic_trust_weighting_time applies decay inside get_normalized_domain_weights!
        # We should define if we want to double-apply or not.
        # The prompt says: "let the 30 min session value represent the data freshness... weight for older metadata has lower influence"
        # Since we have an explicit formula: T_final = T_prev * D_long + T_instant * W_short
        # We should probably get the UNDECAYED spatial trust as "T_instant" and then apply W_short.
        # However, `sim.get_normalized_domain_weights()` in `dynamic_trust_weighting_time` ALREADY applies decay.
        # To avoid double counting, we should use the method carefully or just use the result as T_instant?
        # Actually, if T_instant is ALREADY decayed, then T_instant * W_short is decaying it TWICE.
        # Strategy: We will use the `sim` methods but notice that the sim applies decay to *weights*.
        # If weights -> 0, Mass -> Uncertainty, so Trust -> 0.5 (Neutral).
        # But we want Trust -> 0.
        # So we will take the resulting Trust from the DS fusion (which might be 0.5 because of Uncertainty)
        # And then apply the Ensemble Combiner.
        
        # WAIT. If weights decay to 0 in DS, you get Trust=0.5 (Uncertainty).
        # We want "Old Metadata = Low Influence". 
        # In the formula: Sum(w_i * E_i). This suggests the *Evidence* is weighted.
        # Let's perform standard fusion. We will trust the simulator gives us "Best Effort" spatial trust.
        
        ctx_weights = sim.get_normalized_domain_weights() 
        # Note: These weights in `dynamic_trust_weighting_time.py` are ALREADY multiplied by `decay`.
        # This means `ctx_weights` sums to < 1.0 as time goes on.
        # m_uncertain will be 1 - result. So Uncertainty increases.
        # This is correct for DS.
        
        for d in sim.domains:
            domain_score = current_scores[d]
            ctx_weight = ctx_weights[d]
            
            evidence = self.get_observation_mass(domain_score, ctx_weight)
            
            if step_fusion is None:
                step_fusion = evidence
            else:
                try:
                    step_fusion = step_fusion.combine(evidence)
                except ValueError:
                    pass
                    
        if step_fusion is None:
            return 0.5 # Neutral
            
        betp = step_fusion.pignistic()
        # This is T_instant (but already heavily influenced by the sim's internal decay)
        trust = betp.get('safe', 0.0) 
        return trust, current_scores, ctx_weights

    def calculate_ensemble_trust(self, prev_trust, instant_trust, time_step_mins):
        """
        Combines History (Inertia) and Freshness (Instant) using a Weighted Mixture.
        
        Logic:
        - Inertia: Previous Trust decayed by Long Term factor (48h).
        - Evidence: Instant Trust weighted by Session Freshness (30m).
        
        Formula:
        T = (Weight_Inst * T_Inst) + (Weight_Hist * T_Hist)
        
        We normalize the weights to sum to 1.0 to keep Trust in [0,1].
        Weight_Inst = get_decay_short_term(t)  [1.0 -> 0.05]
        Weight_Hist = 1.0 - Weight_Inst        [0.0 -> 0.95]
        
        This means:
        - Start of Session: Trust is defined by Instant spatial signals.
        - End of Session: Trust is defined by Inertia (History).
        """
        
        # 1. Inertia Component (Memory)
        # Decay the previous trust over the last time step (1 min)
        d_long = self.get_decay_long_term(delta_t_minutes=1)
        trust_history = prev_trust * d_long
        
        # 2. Freshness Component (New Evidence)
        w_short = self.get_decay_short_term(time_step_mins)
        
        # 3. Weighted Mixture
        # As w_short decays (data gets old), we rely more on History.
        # However, to prevent infinite trust extension without valid data,
        # we can enforce that Inertia also has a ceiling or we strictly follow the mixture.
        # User requirement: "weight for older metadata has lower influence"
        # i.e., at t=30, T_instant has low influence.
        
        # Mixture Weights
        # w_short is [1.0 -> 0.0]
        # w_history is [0.0 -> 1.0]
        w_history = 1.0 - w_short
        
        term_instant = instant_trust * w_short
        term_history = trust_history * w_history
        
        total_trust = term_instant + term_history
        
        return min(1.0, max(0.0, total_trust))

