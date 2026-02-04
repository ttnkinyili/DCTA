import random
import time
import json

class TrustSimulator:
    def __init__(self, scenario='default'):
        self.domains = ['Network', 'Data', 'Device', 'App']
        
        if scenario == 'untrusted_device_geofence':
            # Scenario: Remote User, Geofenced Network (High), Untrusted Device (Low), Authorized Data (High)
            self.trust_scores = {
                'Network': 0.95, # Geofenced
                'Data': 0.90,    # Authorized
                'Device': 0.30,  # Untrusted
                'App': 0.85      # Standard
            }
            self.variance = {
                'Network': 0.01, # Stable
                'Data': 0.05,
                'Device': 0.20,  # Unstable/Risky
                'App': 0.05
            }
        else:
            # Default Baseline
            self.trust_scores = {
                'Network': 0.9,
                'Data': 0.85,
                'Device': 0.95,
                'App': 0.8
            }
            self.variance = {
                'Network': 0.05,
                'Data': 0.1,
                'Device': 0.02,
                'App': 0.15
            }
            
        self.scenario = scenario
        self.time_step = 0

    def step(self):
        """Simulate a time step. Trust scores fluctuate."""
        self.time_step += 1
        
        # Scenario: Network attack starts at step 5 ONLY for default
        if self.scenario == 'default' and self.time_step == 5:
            print(">>> EVENT: Network Attack Simulation Started")
            self.trust_scores['Network'] = 0.4 # Drops significantly
            self.variance['Network'] = 0.3     # Becomes unstable

        # Update scores with random noise
        current_readings = {}
        for d in self.domains:
            # Random fluctuation
            noise = random.gauss(0, self.variance[d])
            new_score = max(0.0, min(1.0, self.trust_scores[d] + noise))
            current_readings[d] = new_score
            
        return current_readings

    def get_dynamic_weight(self, domain, history):
        """
        Calculate dynamic weight based on stability (variance) of recent history.
        High variance -> Low Weight (Unreliable source)
        Low variance -> High Weight (Reliable source)
        """
        if len(history) < 2:
            return 1.0 # Default weight
        
        # Simple variance calculation
        mean = sum(history) / len(history)
        var = sum((x - mean) ** 2 for x in history) / len(history)
        
        # Weight formula: 1 / (1 + variance_factor)
        # Scaled to be sensitive
        weight = 1.0 / (1.0 + (var * 100)) 
        return weight

def main():
    print("Running Scenario: Remote User, Untrusted Device, Geofenced Network")
    sim = TrustSimulator(scenario='untrusted_device_geofence')
    history = {d: [] for d in sim.domains}
    
    print(f"{'Step':<5} | {'Domain':<10} | {'Raw Trust':<10} | {'Weight':<10} | {'Weighted Trust':<15}")
    print("-" * 65)

    for i in range(15): # Run for 15 steps
        readings = sim.step()
        
        for d in sim.domains:
            history[d].append(readings[d])
            # Keep history short for dynamic responsiveness (e.g., last 5 steps)
            recent_history = history[d][-5:]
            
            weight = sim.get_dynamic_weight(d, recent_history)
            
            # Application of weight: 
            # In direct trust, we might scale the score. 
            # In Dempster-Shafer later, we will use this to 'discount' the mass.
            
            print(f"{i:<5} | {d:<10} | {readings[d]:<10.3f} | {weight:<10.3f} | {readings[d]*weight:<15.3f}")
        
        print("-" * 65)

if __name__ == "__main__":
    main()
