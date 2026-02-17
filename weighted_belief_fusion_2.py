import sys
from ds_utils import MassFunction
from dynamic_trust_weighting_time import TrustSimulator

def get_observation_mass(domain_score, context_weight):
    """
    Constructs a Dempster-Shafer Mass Function from a Domain Score and its Contextual Weight.
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

def get_access_decision(belief_safe):
    if belief_safe > 0.75:
        return "Full Access"
    elif belief_safe >= 0.45:
        return "Limited Access"
    else:
        return "No Access"

def main():
    print("Running Weighted Belief Fusion Simulation with Temporal Decay (30 Step Session)...")
    # Using 'corporate_office' to show how even a high trust scenario decays
    sim = TrustSimulator(scenario='corporate_office', session_duration=30)
    
    # Cumulative Belief (Temporal Fusion)
    cumulative_belief = MassFunction({('safe', 'unsafe'): 1.0})
    
    print(f"{'Step':<5} | {'Domain':<10} | {'Score':<6} | {'Weight':<6} | {'Decay':<6} | {'Trust':<6} | {'Decision'}")
    print("-" * 100)

    # Run for 35 steps to show what happens after session expiry (step 30)
    for i in range(35):
        readings = sim.step()
        step_fusion = None
        
        # 1. Spatial Fusion
        
        current_scores = {}
        for d in sim.domains:
            current_scores[d] = sim.calculate_domain_score(d, readings[d])
            
        # Get normalized, decayed weights
        ctx_weights = sim.get_normalized_domain_weights()
        decay_factor = sim.get_temporal_decay_factor()
        
        for d in sim.domains:
            domain_score = current_scores[d]
            ctx_weight = ctx_weights[d]
            
            # Evidence Construction
            evidence = get_observation_mass(domain_score, ctx_weight)
            
            # Inter-Domain Fusion
            if step_fusion is None:
                step_fusion = evidence
            else:
                try:
                    step_fusion = step_fusion.combine(evidence)
                except ValueError:
                    # Handle conflict if necessary
                    pass
        
        # 2. Temporal Fusion
        if step_fusion:
            try:
                cumulative_belief = cumulative_belief.combine(step_fusion)
            except ValueError:
                cumulative_belief = step_fusion 

        # Output logic
        betp = cumulative_belief.pignistic()
        # Apply Temporal Decay to the Final Trust Score
        # This represents "Session Validity"
        trust_score = betp.get('safe', 0.0) * decay_factor
        decision = get_access_decision(trust_score)
        
        # Pretty print one domain example (Device)
        example_dom = 'Device'
        ex_score = current_scores[example_dom]
        ex_weight = ctx_weights[example_dom]
        
        print(f"{i:<5} | {example_dom:<10} | {ex_score:<6.3f} | {ex_weight:<6.3f} | {decay_factor:<6.3f} | {trust_score:.4f} | {decision}")

if __name__ == "__main__":
    main()
