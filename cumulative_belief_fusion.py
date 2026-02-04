import sys
from ds_utils import MassFunction
from dynamic_trust_weighting import TrustSimulator

def get_observation_mass(domain, raw_trust, weight):
    """
    Convert a weighted trust score into a Mass Function.
    
    Hypotheses:
    - {Safe}
    - {Unsafe}
    - {Safe, Unsafe} (Uncertainty)
    
    Logic:
    - High trust -> Mass({Safe})
    - Low trust -> Mass({Unsafe})
    - Weight determines how much mass goes to Uncertainty ({Safe, Unsafe})
      Lower weight -> Higher Uncertainty.
    """
    
    # Simple model mapping trust [0,1] to Safe/Unsafe
    # 0.5 is neutral. > 0.5 is Safe. < 0.5 is Unsafe.
    
    certainty = weight # The 'reliability' of the source determines max certainty
    
    if raw_trust > 0.5:
        # Tending towards Safe
        # Scale (0.5 to 1.0) -> (0.0 to 1.0)
        lean = (raw_trust - 0.5) * 2
        m_safe = lean * certainty
        m_unsafe = 0.0
    else:
        # Tending towards Unsafe
        # Scale (0.5 to 0.0) -> (0.0 to 1.0)
        lean = (0.5 - raw_trust) * 2
        m_safe = 0.0
        m_unsafe = lean * certainty
        
    m_uncertain = 1.0 - (m_safe + m_unsafe)
    
    # We use tuples to represent the hypotheses so they are converted to frozensets of strings
    # instead of frozensets of characters.
    return MassFunction({('safe',): m_safe, ('unsafe',): m_unsafe, ('safe', 'unsafe'): m_uncertain})

def get_access_decision(belief_safe):
    if belief_safe >= 0.75:
        return "Full Access"
    elif belief_safe >= 0.45:
        return "Limited Access"
    else:
        return "No Access"

def main():
    print("Running Scenario: Remote User, Untrusted Device, Geofenced Network")
    sim = TrustSimulator(scenario='untrusted_device_geofence')
    history = {d: [] for d in sim.domains}
    
    # Cumulative Belief (Temporal Fusion)
    # Start with high uncertainty (vacuous belief)
    cumulative_belief = MassFunction({('safe', 'unsafe'): 1.0})
    
    print(f"{'Step':<5} | {'Domain':<10} | {'Output Mass (Evidence)':<60} | {'Belief Safe':<12} | {'Decision'}")
    print("-" * 130)

    for i in range(15): # Run for 15 steps
        readings = sim.step()
        
        step_fusion = None
        
        # 1. Spatial Fusion (Fuse across domains at this time step)
        for d in sim.domains:
            history[d].append(readings[d])
            recent_history = history[d][-5:]
            weight = sim.get_dynamic_weight(d, recent_history)
            
            # Create evidence (Mass Function)
            evidence = get_observation_mass(d, readings[d], weight)
            
            # Fuse with other domains in this step
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
        # Query belief for the set {'safe'}
        bel_safe = cumulative_belief.belief({'safe'})
        pl_safe = cumulative_belief.plausibility({'safe'})
        
        decision = get_access_decision(bel_safe)
        
        # Pretty print one domain example for the table space
        example_dom = 'Device' # Show Device as it is the interesting one in this scenario
        ex_weight = sim.get_dynamic_weight(example_dom, history[example_dom][-5:])
        ex_mass = get_observation_mass(example_dom, readings[example_dom], ex_weight)
        
        print(f"{i:<5} | {example_dom:<10} | {str(ex_mass):<60} | {bel_safe:.4f}       | {decision}")

if __name__ == "__main__":
    main()
