import pandas as pd
import matplotlib.pyplot as plt
import os
from ds_utils import MassFunction
from dynamic_trust_weighting_time_exp import TrustSimulator
from weighted_belief_fusion_2 import get_observation_mass, get_access_decision

SCENARIOS = [
    'corporate_office', 
    'remote_vpn', 
    'public_wifi', 
    'byod', 
    'compromised', 
    'untrusted_device_geofence'
]

OUTPUT_DIR = "test_results_time_exp"

def run_simulation(scenario_name, steps=30):
    sim = TrustSimulator(scenario=scenario_name, session_duration=steps)
    domain_history = {d: [] for d in sim.domains}
    cumulative_belief = MassFunction({('safe', 'unsafe'): 1.0})
    
    results = []
    
    for i in range(steps):
        readings = sim.step()
        step_fusion = None
        
        row = {
            'Step': i,
            'Scenario': scenario_name,
            'Decision': 'No Access'
        }
        
        # 1. Spatial Fusion
        
        # Calculate all scores first for history update
        current_scores = {}
        for d in sim.domains:
            # 1a. Intra-Domain Fusion Details
            param_weights = sim.get_dynamic_param_weights(d)
            domain_readings = readings[d]
            
            # Log individual parameter details
            for param, score in domain_readings.items():
                weight = param_weights.get(param, 0.0)
                row[f'{d}_Param_{param}_Score'] = score
                row[f'{d}_Param_{param}_Weight'] = weight
                
            # Calculate and store aggregated domain score
            domain_score = sim.calculate_domain_score(d, readings[d])
            current_scores[d] = domain_score
            row[f'{d}_Score'] = domain_score

        # Get Normalized Weights (and Decay Factor)
        ctx_weights = sim.get_normalized_domain_weights() # This already returns decayed weights? 
        # Wait, in dynamic_trust_weighting_time.py, get_normalized_domain_weights returns decayed weights!
        # Let's verify. Yes, looked at code: "decayed_weights = {d: w * decay ...}"
        # HOWEVER, the user also wants "Session Value represents Data Freshness".
        # In weighted_belief_fusion_2.py, we ALSO decayed the final trust score. 
        # Doubling up decay?
        # dynamic_trust_weighting_time.py:197 -> returns weights * decay.
        # This means the Evidence Mass for "Safe" and "Unsafe" will decrease, and "Uncertainty" will increase.
        # m(Safe) = Score * Weight. If Weight -> 0, m(Safe) -> 0.
        # This inherently reduces Trust Score because BetP(Safe) = m(Safe) + m(Uncertain)/2 (if using classical)
        # BUT our pignistic implementation in ds_utils splits uncertainty.
        # If m(Uncertainty) = 1.0, BetP(Safe) = 0.5.
        # If we want Trust -> 0, we need to explicitly penalize Uncertainty or use the linear decay on final score.
        # In weighted_belief_fusion_2.py, we did `trust_score = betp.get('safe', 0.0) * decay_factor`.
        # This is a strong enforcement of session expiry.
        # I will include this explicit decay on the final score as well for the strict "Session Expiry" visual.
        
        decay_factor = sim.get_temporal_decay_factor()
        row['Decay_Factor'] = decay_factor
        
        for d in sim.domains:
            # Stage 2: Context Weight
            ctx_weight = ctx_weights[d]
            row[f'{d}_Weight'] = ctx_weight
            
            # Stage 3: Evidence Construction
            evidence = get_observation_mass(current_scores[d], ctx_weight)
            
            # Stage 4: Inter-Domain Fusion
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
                
        # Trust Score Calculation (Pignistic Probability)
        betp = cumulative_belief.pignistic()
        
        # Explicitly decay the final trust score to represent "Session Validity"
        # As session value increases (older), influence decreases -> Trust score fades
        trust_score = betp.get('safe', 0.0) * decay_factor
        
        row['Belief_Safe'] = cumulative_belief.belief({'safe'})
        row['Belief_Unsafe'] = cumulative_belief.belief({'unsafe'})
        row['Uncertainty'] = cumulative_belief.plausibility({'safe'}) - cumulative_belief.belief({'safe'})
        
        # DECISION BASED ON TRUST SCORE, NOT RAW BELIEF
        row['Trust_Score'] = trust_score 
        row['Decision'] = get_access_decision(trust_score)
        
        results.append(row)
        
    return results

def generate_graphs(df, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # 1. Belief Evolution per Scenario
    for scenario in SCENARIOS:
        subset = df[df['Scenario'] == scenario]
        plt.figure(figsize=(10, 6))
        
        # Plot Beliefs (Evidence)
        plt.fill_between(subset['Step'], subset['Belief_Safe'], color='green', alpha=0.1)
        plt.plot(subset['Step'], subset['Belief_Safe'], label='Belief(Safe)', color='green', linestyle='--', linewidth=1)
        # Plot Trust Score (Decision Metric)
        plt.plot(subset['Step'], subset['Trust_Score'], label='Trust Score (Decayed)', color='blue', linewidth=2.5)
        
        # Plot Decay Factor for reference
        plt.plot(subset['Step'], subset['Decay_Factor'], label='Session Validty', color='gray', linestyle=':', linewidth=1)
        
        # Add decision zones
        plt.axhline(y=0.75, color='darkgreen', linestyle=':', alpha=0.8, label='Full Access (>0.75)')
        plt.axhline(y=0.45, color='orange', linestyle=':', alpha=0.8, label='Limited Access (>=0.45)')
        
        plt.title(f"Trust Score Evolution (Time Decayed): {scenario}")
        plt.xlabel("Time Step (Session Duration)")
        plt.ylabel("Probability / Score")
        plt.ylim(-0.05, 1.05)
        plt.legend(loc='lower left')
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/{scenario}_belief_evolution.png")
        plt.close()

    # 2. Domain Scores per Scenario
    for scenario in SCENARIOS:
        subset = df[df['Scenario'] == scenario]
        plt.figure(figsize=(10, 6))
        for d in ['Network', 'Device', 'Data', 'App']:
            label = d
            if d == 'App':
                label = 'App Risk Posture'
            plt.plot(subset['Step'], subset[f'{d}_Score'], label=f'{label} Score')
            
        plt.title(f"Domain Scores: {scenario}")
        plt.xlabel("Time Step")
        plt.ylabel("Trust Score")
        plt.ylim(-0.05, 1.05)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/{scenario}_domain_scores.png")
        plt.close()

def save_sample_outputs(df, output_dir):
    with open(f"{output_dir}/sample_outputs.txt", "w") as f:
        f.write("SAMPLE SIMULATION OUTPUTS (TIME DECAYED)\n")
        f.write("="*80 + "\n\n")
        
        for scenario in SCENARIOS:
            f.write(f"SCENARIO: {scenario}\n")
            f.write("-" * 40 + "\n")
            # Show Start, Middle, End of session
            # Steps 0, 15, 29
            subset = df[df['Scenario'] == scenario].iloc[[0, 15, 29]]
            
            cols = ['Step', 'Network_Score', 'Data_Score', 'Device_Score', 'App_Score', 'Decay_Factor', 'Trust_Score', 'Decision']
            display_df = subset[cols].rename(columns={'App_Score': 'App_Risk_Posture'})
            f.write(display_df.to_string(index=False))
            f.write("\n\n" + "="*80 + "\n\n")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Running all scenarios with Exponential Time Decay...")
    all_results = []
    
    for scenario in SCENARIOS:
        print(f"Executing: {scenario}")
        scenario_data = run_simulation(scenario, steps=30)
        all_results.extend(scenario_data)
        
    df = pd.DataFrame(all_results)
    
    print(f"Generating artifacts in {OUTPUT_DIR}...")
    generate_graphs(df, OUTPUT_DIR)
    save_sample_outputs(df, OUTPUT_DIR)
    
    # Save raw data
    df.to_csv(f"{OUTPUT_DIR}/simulation_data_time_exp.csv", index=False)
    print("Done.")

if __name__ == "__main__":
    main()
