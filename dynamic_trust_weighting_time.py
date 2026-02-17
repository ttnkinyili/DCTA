import random
import time
import json
import math

class TrustSimulator:
    def __init__(self, scenario='default', session_duration=30):
        self.domains = ['Network', 'Data', 'Device', 'App']
        self.session_duration = session_duration
        
        # Granular Parameters configuration
        self.parameters = {
            'Data': ['Integrity', 'Freshness', 'Authenticity'],
            'Device': ['Identity', 'Reputation', 'Compliance'],
            'App': ['VulnerabilityScore', 'Consistency', 'AccessCompliance'],
            'Network': ['Anomalies', 'ProtocolScore', 'NodeReputation']
        }
        
        # Parameter Weights (Static for this simulation, but could be dynamic)
        # Sum should be 1.0 per domain for Weighted Sum
        self.param_weights = {
            'Data': {'Integrity': 0.4, 'Freshness': 0.2, 'Authenticity': 0.4},
            'Device': {'Identity': 0.3, 'Reputation': 0.3, 'Compliance': 0.4},
            'App': {'VulnerabilityScore': 0.4, 'Consistency': 0.3, 'AccessCompliance': 0.3},
            'Network': {'Anomalies': 0.4, 'ProtocolScore': 0.3, 'NodeReputation': 0.3}
        }

        # Initialize base scores and variances for parameters
        self.param_scores = {}
        self.param_variance = {}

        # Initialize base scores and variances based on scenario
        if scenario == 'corporate_office':
            # High Trust Everywhere
            self._set_domain_params('Network', 0.95, 0.01) # Stable, Secure
            self._set_domain_params('Data', 0.90, 0.02)
            self._set_domain_params('Device', 0.95, 0.01) # Managed
            self._set_domain_params('App', 0.90, 0.02)
            
        elif scenario == 'remote_vpn':
            # Good Device, Secure Path, but remote
            self._set_domain_params('Network', 0.85, 0.05) # VPN is good, but public, slightly more variance
            self._set_domain_params('Data', 0.90, 0.02)
            self._set_domain_params('Device', 0.95, 0.01) # Managed
            self._set_domain_params('App', 0.90, 0.02)

        elif scenario == 'public_wifi':
            # 3. Public Wi-Fi: Low to Medium Trust (Risky Network)
            self._set_domain_params('Network', 0.30, 0.25) # Low
            self._set_domain_params('Data', 0.60, 0.05)    # Medium
            self._set_domain_params('Device', 0.75, 0.05)  # Med-High (Managed but risky environment)
            self._set_domain_params('App', 0.70, 0.05)     # Medium

        elif scenario == 'byod': 
            # 4. BYOD: Low to Medium Trust (Unmanaged Device)
            self._set_domain_params('Network', 0.90, 0.02) # High (Internal)
            self._set_domain_params('Data', 0.50, 0.05)    # Low/Med
            self._set_domain_params('Device', 0.40, 0.20)  # Low
            self._set_domain_params('App', 0.60, 0.10)     # Medium

        elif scenario == 'compromised':
            # 6. Compromised: LOW TRUST FOR ALL FACETS
            self._set_domain_params('Network', 0.20, 0.30) # Very Low
            self._set_domain_params('Data', 0.20, 0.10)    # Low
            self._set_domain_params('Device', 0.20, 0.30)  # Low
            self._set_domain_params('App', 0.20, 0.20)     # Low

        elif scenario == 'untrusted_device_geofence':
            # 5. Untrusted: LOW TRUST FOR ALL FACETS
            self._set_domain_params('Network', 0.30, 0.10) # Low
            self._set_domain_params('Data', 0.30, 0.05)    # Low
            self._set_domain_params('Device', 0.30, 0.20)  # Low
            self._set_domain_params('App', 0.30, 0.10)     # Low
            
        else:
            # Default / Fallback
            self._set_domain_params('Network', 0.5, 0.1)
            self._set_domain_params('Data', 0.5, 0.1)
            self._set_domain_params('Device', 0.5, 0.1)
            self._set_domain_params('App', 0.5, 0.1)
            
        self.scenario = scenario
        self.time_step = 0
        
        # History tracking for dynamic variance calculation
        # Structure: self.history[domain][param] = [val1, val2, ...]
        self.history = {d: {p: [] for p in self.parameters[d]} for d in self.domains}
        
        # Aggregated Domain Score History (for inter-domain weighting)
        self.domain_score_history = {d: [] for d in self.domains}

    def _set_domain_params(self, domain, base_score, base_variance):
        """Helper to initialize parameters for a domain around a base score"""
        self.param_scores[domain] = {}
        self.param_variance[domain] = {}
        for param in self.parameters[domain]:
            # Add slight random variation to initial parameter scores so they aren't identical
            variation = random.uniform(-0.05, 0.05)
            self.param_scores[domain][param] = max(0.0, min(1.0, base_score + variation))
            self.param_variance[domain][param] = base_variance

    def step(self):
        """Simulate a time step. Parameters fluctuate."""
        self.time_step += 1
        
        # Scenario Logic: Network Attack (only for default scenario for now)
        if self.scenario == 'default' and self.time_step == 5:
            print(">>> EVENT: Network Anomalies Detected")
            self.param_scores['Network']['Anomalies'] = 0.2 # Drastic drop
            self.param_variance['Network']['Anomalies'] = 0.4 # Chaotic

        current_readings = {}
        
        for domain in self.domains:
            current_readings[domain] = {}
            for param in self.parameters[domain]:
                # fluctuation
                var = self.param_variance[domain][param]
                noise = random.gauss(0, var)
                current_val = self.param_scores[domain][param]
                
                # Check bounds
                new_val = max(0.0, min(1.0, current_val + noise))
                
                current_readings[domain][param] = new_val
                
                # Update History
                self.history[domain][param].append(new_val)
                if len(self.history[domain][param]) > 10: # Keep window short
                    self.history[domain][param].pop(0)

        return current_readings

    def _calculate_variance(self, data):
        if len(data) < 2: return 0.0
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)

    def get_dynamic_param_weights(self, domain):
        """
        Calculate intra-domain weights for parameters based on variance.
        Normalize properties so sum(weights) = 1.0
        Low Variance = High Weight.
        """
        variances = {}
        for param in self.parameters[domain]:
            hist = self.history[domain][param]
            variances[param] = self._calculate_variance(hist)
            
        # Raw Weight = 1 / (1 + scaling * Variance)
        raw_weights = {p: 1.0 / (1.0 + v * 100) for p, v in variances.items()}
        
        # Normalize
        total_weight = sum(raw_weights.values())
        if total_weight == 0:
            # Fallback to equal weights
            count = len(self.parameters[domain])
            return {p: 1.0/count for p in self.parameters[domain]}
            
        normalized = {p: w / total_weight for p, w in raw_weights.items()}
        return normalized

    def calculate_domain_score(self, domain, param_readings):
        """
        Stage 1 Fusion: Dynamic Weighted Sum of Parameters (Normalized)
        """
        # Get dynamic normalized weights for this step
        weights = self.get_dynamic_param_weights(domain)
        
        score = 0.0
        for param, value in param_readings.items():
            score += value * weights[param]
            
        # Track for inter-domain calculation
        self.domain_score_history[domain].append(score)
        if len(self.domain_score_history[domain]) > 10:
             self.domain_score_history[domain].pop(0)
             
        return score

    def get_temporal_decay_factor(self):
        """
        Calculates a multiplier (0.0 - 1.0) based on time using Exponential Decay.
        Formula: Decay = e^(-lambda * t)
        
        We calibrate lambda such that at t = session_duration, the value is effectively 0 (e.g., 0.05).
        Let target at duration be 0.05:
            0.05 = e^(-k) => k ~= 3.0
            So, exponent = -3.0 * (t / duration)
        """
        if self.time_step >= self.session_duration:
            return 0.05 # Asymptote but effectively expired
            
        # Exponential Decay
        # t=0 -> 1.0
        # t=15 -> e^-1.5 ~= 0.22
        # t=30 -> e^-3.0 ~= 0.05
        ratio = float(self.time_step) / float(self.session_duration)
        decay = math.exp(-3.0 * ratio)
        return decay

    def get_normalized_domain_weights(self):
        """
        Calculate Inter-domain weights.
        Based on variance of the AGGREGATED domain scores.
        Normalized so sum(weights) = 1.0 (BEFORE decay).
        
        THEN multiplied by the Temporal Decay factor.
        """
        variances = {}
        for domain in self.domains:
            hist = self.domain_score_history[domain]
            variances[domain] = self._calculate_variance(hist)
            
        # Raw Weight
        raw_weights = {d: 1.0 / (1.0 + v * 100) for d, v in variances.items()}
        
        # Normalize
        total = sum(raw_weights.values())
        if total == 0:
             normalized = {d: 0.25 for d in self.domains}
        else:
             normalized = {d: w / total for d, w in raw_weights.items()}
             
        # Apply Temporal Decay
        # NOTE: This effectively reduces the "reliability" of the context
        # In DS terms: W -> 0 means Mass -> Uncertainty
        decay = self.get_temporal_decay_factor()
        
        decayed_weights = {d: w * decay for d, w in normalized.items()}
        return decayed_weights
