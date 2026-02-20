import pandas as pd
import matplotlib.pyplot as plt
import os
import math
from ds_utils import MassFunction
from dynamic_trust_weighting_time import TrustSimulator
from ensemble_trust_simulator import EnsembleTrustEngine

SCENARIOS = [
    'corporate_office', 
    'remote_vpn', 
    'public_wifi', 
    'byod', 
    'compromised', 
    'untrusted_device_geofence'
]

OUTPUT_DIR = "test_results_Ensemble"

def get_access_decision(trust_score):
    if trust_score > 0.75:
        return "Full Access"
    elif trust_score >= 0.45:
        return "Limited Access"
    else:
        return "No Access"

def run_simulation(scenario_name, steps=30):
    # Initialize Simulator and Engine
    sim = TrustSimulator(scenario=scenario_name, session_duration=steps)
    engine = EnsembleTrustEngine()
    
    # Initialize Trust State (Previous Trust)
    # Start at 0.5 (Neutral) or 1.0 depending on scenario?
    # Let's assume start at 0.5 to show "Trust Building" via inertia?
    # Or start at 0.0?
    # Actually, continuous authentication usually implies existing trust.
    # Let's start at 0.5 for neutrality.
    current_ensemble_trust = 0.5
    
    results = []
    
    for i in range(steps):
        readings = sim.step()
        
        row = {
            'Step': i,
            'Scenario': scenario_name,
            'Decision': 'No Access'
        }
        
        # 1. Calculate Instant Trust (Spatial Fusion)
        # We need to manually perform the fusion step using the Engine helper
        # Logic is similar to `calculate_instant_trust` which returns a single scalar
        # BUT we need intermediate values for logging.
        
        # Get Normalized Weights from Sim (Time-Decayed already!)
        ctx_weights = sim.get_normalized_domain_weights()
        
        # REVERSE the simulator's decay to get RAW spatial trust
        # We want Instant Trust to represent "Signal Quality" only.
        # The Ensemble Engine handles the "Time Freshness".
        sim_decay = sim.get_temporal_decay_factor()
        if sim_decay > 0.001:
            raw_weights = {d: w / sim_decay for d, w in ctx_weights.items()}
        else:
            # If decay is effectively 0, weights are negligible. 
            # But mathematically, we want normalized weights summing to 1.
            # We can re-normalize manually or fallback to uniform if everything is 0.
            total_w = sum(ctx_weights.values())
            if total_w > 0:
                 raw_weights = {d: w / total_w for d, w in ctx_weights.items()}
            else:
                 raw_weights = {d: 0.25 for d in sim.domains}

        # Calculate Domain Scores
        current_scores = {}
        for d in sim.domains:
            current_scores[d] = sim.calculate_domain_score(d, readings[d])
            row[f'{d}_Score'] = current_scores[d]
            row[f'{d}_Weight'] = raw_weights[d]
            
        # Perform Fusion
        step_fusion = None
        for d in sim.domains:
            # Use RAW WEIGHTS for fusion
            evidence = engine.get_observation_mass(current_scores[d], raw_weights[d])
            if step_fusion is None:
                step_fusion = evidence
            else:
                try:
                    step_fusion = step_fusion.combine(evidence)
                except ValueError:
                    pass
        
        if step_fusion:
            betp = step_fusion.pignistic()
            instant_trust = betp.get('safe', 0.0)
        else:
            instant_trust = 0.5
            
        row['Instant_Trust'] = instant_trust
        
        # 2. Calculate Ensemble Trust (Inertia + Freshness)
        # Using the Weighted Mixture logic (Same as engine.calculate_ensemble_trust)
        
        # Use previous trust from last iteration
        prev_trust = current_ensemble_trust
        
        # Calculate terms
        d_long = engine.get_decay_long_term(delta_t_minutes=1)
        trust_history = prev_trust * d_long
        
        w_short = engine.get_decay_short_term(session_time_minutes=i)
        
        # Mixture Weights
        w_history = 1.0 - w_short
        
        # Components for final sum
        term_instant = instant_trust * w_short
        term_history = trust_history * w_history
        
        # Final Trust
        final_trust = min(1.0, max(0.0, term_instant + term_history))
        
        # Log Logic (For transparency)
        inertia_component = term_history
        freshness_component = term_instant
        
        # Update State for next iteration
        current_ensemble_trust = final_trust
        
        # Log Metrics
        row['Prev_Trust'] = prev_trust
        row['Long_Term_Decay'] = d_long
        row['Short_Term_Weight'] = w_short
        row['Inertia_Component'] = inertia_component
        row['Freshness_Component'] = freshness_component
        row['Ensemble_Trust'] = final_trust
        row['Decision'] = get_access_decision(final_trust)
        
        results.append(row)
        
    return results

def generate_graphs(df, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for scenario in SCENARIOS:
        subset = df[df['Scenario'] == scenario]
        plt.figure(figsize=(10, 6))
        
        # Plot Components
        plt.plot(subset['Step'], subset['Instant_Trust'], label='Instant Trust (Spatial)', color='gray', linestyle=':', alpha=0.6)
        plt.plot(subset['Step'], subset['Inertia_Component'], label='Inertia (History)', color='purple', linestyle='--', alpha=0.7)
        
        # Plot Final Trust
        plt.plot(subset['Step'], subset['Ensemble_Trust'], label='Ensemble Trust', color='blue', linewidth=2.5)
        
        # Add decision zones
        plt.axhline(y=0.75, color='darkgreen', linestyle=':', alpha=0.8, label='Full Access (>0.75)')
        plt.axhline(y=0.45, color='orange', linestyle=':', alpha=0.8, label='Limited Access (>=0.45)')
        
        plt.title(f"Ensemble Trust Evolution: {scenario}")
        plt.xlabel("Time Step (Minutes)")
        plt.ylabel("Trust Score")
        plt.ylim(-0.05, 1.05)
        plt.legend(loc='lower left')
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/{scenario}_ensemble_evolution.png")
        plt.close()

def save_sample_outputs(df, output_dir):
    with open(f"{output_dir}/ensemble_sample_outputs.txt", "w") as f:
        f.write("SAMPLE ENSEMBLE SIMULATION OUTPUTS\n")
        f.write("Model: Inertia (48h Decay) + Fusion (30m Freshness)\n")
        f.write("="*80 + "\n\n")
        
        for scenario in SCENARIOS:
            f.write(f"SCENARIO: {scenario}\n")
            f.write("-" * 40 + "\n")
            # Show Start, Middle, End
            subset = df[df['Scenario'] == scenario].iloc[[0, 15, 29]]
            
            cols = ['Step', 'Instant_Trust', 'Prev_Trust', 'Inertia_Component', 'Freshness_Component', 'Ensemble_Trust', 'Decision']
            f.write(subset[cols].to_string(index=False))
            f.write("\n\n" + "="*80 + "\n\n")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Running Ensemble Trust Scenarios...")
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
    df.to_csv(f"{OUTPUT_DIR}/ensemble_simulation_data.csv", index=False)
    print("Done.")

if __name__ == "__main__":
    main()
