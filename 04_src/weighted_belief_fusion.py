import sys
from ds_utils import MassFunction
from dynamic_trust_weighting import TrustSimulator

def get_observation_mass(domain_score, context_weight):
    """
    Constructs a Dempster-Shafer Mass Function from a Domain Score and its Contextual Weight.
    
    Logic (Refined):
    1. Belief (Safe) = Score * Weight
    2. Disbelief (Unsafe) = (1 - Score) * Weight
    3. Uncertainty (Absence of Metadata) = 1 - Weight
       - "Neutral base value of 0.5" is implicit: if Weight=0, mass is pure Uncertainty, 
         BetP(Safe) becomes 0.5.
    """
    
    m_safe = domain_score * context_weight
    m_unsafe = (1.0 - domain_score) * context_weight
    m_uncertain = 1.0 - context_weight
    
    # Handle floating point precisions or weight > 1 (shouldn't happen with normalization)
    if m_uncertain < 0: m_uncertain = 0.0
    
    mass_dict = {
        ('safe',): m_safe,
        ('unsafe',): m_unsafe,
        ('safe', 'unsafe'): m_uncertain
    }
    
    return MassFunction(mass_dict)

def get_access_decision(belief_safe):
    if belief_safe > 0.75:
        return "Full Access"
    elif belief_safe >= 0.45:
        return "Limited Access"
    else:
        return "No Access"

def main():
    print("Running Weighted Belief Fusion Simulation (Granular Parameters)...")
    sim = TrustSimulator(scenario='untrusted_device_geofence')
    domain_history = {d: [] for d in sim.domains}
    
    # Cumulative Belief (Temporal Fusion)
    cumulative_belief = MassFunction({('safe', 'unsafe'): 1.0})
    
    print(f"{'Step':<5} | {'Domain':<10} | {'Agg Score':<10} | {'Ctx Weight':<10} | {'Belief Safe':<12} | {'Decision'}")
    print("-" * 130)

    for i in range(15):
        readings = sim.step()
        
        step_fusion = None
        
        # 1. Spatial Fusion (Fuse across domains at this time step)
        # 1. Spatial Fusion (Fuse across domains at this time step)
        
        # Pre-calculate domain scores to update history in simulator
        current_scores = {}
        for d in sim.domains:
            current_scores[d] = sim.calculate_domain_score(d, readings[d])
            
        # Get normalized context weights for all domains
        # These now sum to 1.0 across domains
        ctx_weights = sim.get_normalized_domain_weights()
        
        for d in sim.domains:
            # Stage 1: Domain Score (Already calculated)
            domain_score = current_scores[d]
            
            # Stage 2: Contextual Weight
            ctx_weight = ctx_weights[d]
            
            # Stage 3: Evidence Construction (Discounting)
            evidence = get_observation_mass(domain_score, ctx_weight)
            
            # Stage 4: Inter-Domain Fusion (Dempster's Rule)
            if step_fusion is None:
                step_fusion = evidence
            else:
                try:
                    step_fusion = step_fusion.combine(evidence)
                except ValueError:
                    pass
        
        # 2. Temporal Fusion
        if step_fusion:
            try:
                cumulative_belief = cumulative_belief.combine(step_fusion)
            except ValueError:
                cumulative_belief = step_fusion 

        # Output logic
        # Use Pignistic Probability as the "Eventual Trust Score"
        betp = cumulative_belief.pignistic()
        trust_score = betp.get('safe', 0.0)
        
        decision = get_access_decision(trust_score)
        
        # Pretty print one domain example for table (Device is the interesting one)
        example_dom = 'Device'
        ex_score = current_scores[example_dom]
        ex_weight = ctx_weights[example_dom]
        
        print(f"{i:<5} | {example_dom:<10} | {ex_score:<10.3f} | {ex_weight:<10.3f} | {trust_score:.4f}       | {decision}")

if __name__ == "__main__":
    main()
