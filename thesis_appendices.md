# Appendices: Simulation Data, Core Code, and Graphical Outputs

This appendix compiles the raw data, source code, and graphical outputs generated during the mathematical simulations of the four primary trust models evaluated in this research. The data serves as empirical proof of the efficacy of the proposed Ensemble Trust Model.

---

## Appendix A: Core Simulation Code and Algorithms

### A.1 Dempster-Shafer Combination Engine (`ds_utils.py`)
The foundational logic for evidential fusion relies on Dempster-Shafer Math, normalizing conflicting domains. The custom `combine` method calculates the mathematical intersection of Belief masses ($m$) across Independent sensors. If the sensors report contradicting telemetry, the conflict ($K$) is quantified and the resulting Trust Score ($Belief(Safe)$) is algorithmically dampened.

```python
class MassFunction:
    """
    A class to represent a Dempster-Shafer Mass Function (Basic Probability Assignment).
    """
    def combine(self, other):
        """
        Combine this MassFunction with another using Dempster's Rule of Combination.
        """
        combined = {}
        conflict = 0.0

        for h1, m1 in self.masses.items():
            for h2, m2 in other.masses.items():
                intersection = h1.intersection(h2)
                if not intersection:
                    conflict += m1 * m2
                else:
                    combined[intersection] = combined.get(intersection, 0.0) + (m1 * m2)

        normalization_factor = 1.0 - conflict
        if normalization_factor <= 1e-9:
            raise ValueError("MassFunctions are totally conflicting, cannot combine.")

        for h in combined:
            combined[h] /= normalization_factor

        return MassFunction(combined)
```

### A.2 The Ensemble Decay Algorithm (`ensemble_trust_simulator.py`)
This snippet demonstrates the algorithm responsible for calculating continuous session decay utilizing exponential ($\lambda$) factors. It explicitly hybridizes historical inertia ($w_{history}$) with instant cryptographic freshness ($w_{short}$). As time progresses without re-verification, the engine automatically shifts the burden of trust away from the initial spatial signal and onto the mathematical behavioral variance.

```python
class EnsembleTrustEngine:
    def __init__(self):
        self.LAMBDA_LONG = 3.0 / 2880.0
        self.MU_SHORT = 0.1

    def calculate_ensemble_trust(self, prev_trust, instant_trust, time_step_mins):
        """
        Combines History (Inertia) and Freshness (Instant) using a Weighted Mixture.
        """
        d_long = math.exp(-self.LAMBDA_LONG * 1)
        trust_history = prev_trust * d_long
        w_short = math.exp(-self.MU_SHORT * time_step_mins)
        w_history = 1.0 - w_short
        
        term_instant = instant_trust * w_short
        term_history = trust_history * w_history
        
        total_trust = term_instant + term_history
        
        return min(1.0, max(0.0, total_trust))
```

---

## Appendix B: Standardized Scenario Configurations
To test the simulation universally across models, a standard six-scenario matrix was established mapping theoretical Network, Device, Data, and App variables to realistic operational bounds. This standardization enables direct comparative analysis. By holding the inputs constant, the variances in the ensuing output graphs uniquely isolate the mechanical behavior of the Trust Models being tested.

```text
+-------------------+-----------------------+------------------+------------------+-----------------------+-----------------------+---------------------+
| Scenario Name     | Network Trust         | Device Trust     | Data Sensitivity | App Risk Posture      | Typical Decision      | Description         |
+-------------------+-----------------------+------------------+------------------+-----------------------+-----------------------+---------------------+
| Corporate Office  | High (0.95)           | High (0.95)      | High (0.90)      | Low Risk (0.90)       | Full Access           | Empoyee on-site     |
| VPN / Remote      | Medium-High (0.85)    | High (0.90)      | High (0.85)      | Low Risk (0.90)       | Full Access           | WFH with managed PC |
| Public Wi-Fi      | Low (0.30)            | Med-High (0.75)  | Medium (0.60)    | Med Risk (0.70)       | Limited Access        | Coffee shop usage   |
| BYOD / Guest      | High (0.90)           | Low (0.40)       | Low/Med (0.50)   | Med Risk (0.60)       | Limited Access        | Personal phone      |
| Untrusted         | Low (0.30)            | Low (0.30)       | Low (0.30)       | High Risk (0.30)      | No Access             | Unknown external    |
| Compromised       | Very Low (0.20)       | Very Low (0.20)  | Low (0.20)       | High Risk (0.20)      | No Access             | Detected attack     |
+-------------------+-----------------------+------------------+------------------+-----------------------+-----------------------+---------------------+
```

---

## Appendix C: Phase 1 & 2 - Base Dynamic Weighted Belief Fusion
This initial framework demonstrates the ability to isolate spatial uncertainty using variance weighting, dynamically ignoring chaotic ambient noise (like public Wi-Fi jitter). Note that the raw simulation outputs plateau unconditionally, proving the necessity of temporal constraints.

### C.1 Sample Output Data

**Public Wi-Fi Snippet:** The data illustrates how a highly unstable network ($0.13$) initially restricts trust to $0.35$ (Limited Access). However, by Step 5, the model recognizes the stability in the Device and App sensors, algorithmically boosting the Belief ($0.77$) to grant Full Access despite the noisy environment.
```text
SCENARIO: public_wifi
----------------------------------------
 Step  Network_Score  Data_Score  Device_Score  App_Risk_Posture  Belief_Safe       Decision
    0       0.136693    0.597395      0.731363          0.760499     0.357156 Limited Access
    3       0.289882    0.627784      0.748960          0.783207     0.674491 Limited Access
    5       0.353284    0.599599      0.787179          0.703540     0.776159    Full Access
    9       0.027876    0.587662      0.730330          0.733718     0.910126    Full Access
```

**Compromised Host Snippet:** This data logs the system's "Fail-Safe". Because all incoming spatial telemetry is extremely low ($<0.30$) and highly variant, Dempster-Shafer calculates overwhelming Disbelief. The session is immediately terminated with a raw Trust Score plummeting below $0.05$.
```text
SCENARIO: compromised
----------------------------------------
 Step  Network_Score  Data_Score  Device_Score  App_Risk_Posture  Belief_Safe  Decision
    0       0.279667    0.134725      0.061394          0.165068     0.078945 No Access
    3       0.319293    0.101613      0.047309          0.147789     0.028666 No Access
    9       0.206757    0.206560      0.061481          0.208143     0.000903 No Access
```

### C.2 Graphical Outputs
The base model plots immediately demonstrate rapid geometric convergence toward $1.0$. Because time is mathematically ignored throughout this phase, the system builds an impenetrable baseline of trust within 10 operational steps that never degrades.

*   **Corporate Office**: ![Graph](./test_results/corporate_office_belief_evolution.png)
*   **Remote VPN**: ![Graph](./test_results/remote_vpn_belief_evolution.png)
*   **Public Wi-Fi**: ![Graph](./test_results/public_wifi_belief_evolution.png)
*   **BYOD**: ![Graph](./test_results/byod_belief_evolution.png)
*   **Compromised Host**: ![Graph](./test_results/compromised_belief_evolution.png)
*   **Untrusted Domain**: ![Graph](./test_results/untrusted_device_geofence_belief_evolution.png)

---

## Appendix D: Phase 3 (Linear) - Temporal Decay
The introduction of a linear Time-To-Live (TTL) standardizes session durations for corporate compliance, effectively enforcing re-authentication at defined intervals (e.g., NIST AAL2). However, the predictable, gradual downward slope of the trust calculation lacks the urgency required to defeat an active session hijacker operating quickly within the approved window.

### D.1 Graphical Outputs
These models reveal mathematically predictable degradation. Regardless of how pristine the initial spatial authentication was (e.g., Corporate Office), the trust algorithm decays by a rigid, standardized value every time step, ultimately intersecting the $0.45$ termination threshold precisely on schedule.

*   **Corporate Office**: ![Graph](./test_results_time/corporate_office_belief_evolution.png)
*   **Remote VPN**: ![Graph](./test_results_time/remote_vpn_belief_evolution.png)
*   **Public Wi-Fi**: ![Graph](./test_results_time/public_wifi_belief_evolution.png)
*   **BYOD**: ![Graph](./test_results_time/byod_belief_evolution.png)
*   **Compromised Host**: ![Graph](./test_results_time/compromised_belief_evolution.png)
*   **Untrusted Domain**: ![Graph](./test_results_time/untrusted_device_geofence_belief_evolution.png)

---

## Appendix E: Phase 3 (Exponential) - Temporal Decay
Exponential decay introduces an aggressive $\lambda$ parameter that serves as an immediate cryptographic kill-switch against Advanced Persistent Threats (APTs). By forcing the trust score to crash precipitously the moment spatial telemetry verification stops, the system maintains a state of continuous suspicion, mathematically collapsing hijacked sessions before lateral movement can be executed.

### E.1 Graphical Outputs
Unlike the linear models, these exponential plots exhibit a volatile concave curve. The trust score plummets the moment the initial session is granted, forcing the user (or hijacker) into a state of immediate re-verification. While secure, the aggressive mathematics render this model practically unusable for standard high-productivity workflows.

*   **Corporate Office**: ![Graph](./test_results_time_exp/corporate_office_belief_evolution.png)
*   **Remote VPN**: ![Graph](./test_results_time_exp/remote_vpn_belief_evolution.png)
*   **Public Wi-Fi**: ![Graph](./test_results_time_exp/public_wifi_belief_evolution.png)
*   **BYOD**: ![Graph](./test_results_time_exp/byod_belief_evolution.png)
*   **Compromised Host**: ![Graph](./test_results_time_exp/compromised_belief_evolution.png)
*   **Untrusted Domain**: ![Graph](./test_results_time_exp/untrusted_device_geofence_belief_evolution.png)

---

## Appendix F: Phase 4 - The Ensemble Trust Model
The Ensemble model resolves the operational turbulence of strict exponential decay by hybridizing instant cryptographic "Freshness" with a rolling window of behavioral "Inertia". This sophisticated architecture successfully absorbs minor environmental jitters (maintaining the session) while ensuring that a fundamental shift in user behavior still results in a rapid algorithmic denial.

### F.1 Sample Output Data

**Remote VPN Snippet (The Hybridization):** Here we see the transition in real-time. At $T=0$, the session relies entirely on cryptographic Freshness ($0.787$). By $T=29$, Freshness has decayed exponentially ($0.043$), but the user's Behavioral Inertia has successfully scaled ($0.739$) to maintain a stable, highly-trusted session ($0.782$).
```text
SCENARIO: remote_vpn
----------------------------------------
 Step  Instant_Trust  Prev_Trust  Inertia_Component  Freshness_Component  Ensemble_Trust    Decision
    0       0.787406    0.500000           0.000000             0.787406        0.787406 Full Access
   15       0.791865    0.786103           0.610064             0.176689        0.786753 Full Access
   29       0.788218    0.783121           0.739261             0.043370        0.782631 Full Access
```

**Compromised Snippet:** The model proves its lethality. Because the initial Instant Trust was terrible ($0.226$), it failed to build any significant Inertia weight ($0.279$). The final Ensemble score stabilizes far below the access threshold ($0.298$), locking the attacker out permanently.
```text
SCENARIO: compromised
----------------------------------------
 Step  Instant_Trust  Prev_Trust  Inertia_Component  Freshness_Component  Ensemble_Trust  Decision
    0       0.226935    0.500000           0.000000             0.226935        0.226935 No Access
   15       0.349937    0.288259           0.223706             0.078081        0.301788 No Access
   29       0.351770    0.296184           0.279596             0.019356        0.298951 No Access
```

### F.2 Graphical Outputs
These final output graphs represent the optimal Zero Trust state. The chaotic oscillations seen in the Exponential model are dampened, resulting in clean, reliable trust thresholds that maximize operational continuity while inherently blocking access vectors that lack established historical inertia.

*   **Corporate Office**: ![Graph](./test_results_Ensemble/corporate_office_ensemble_evolution.png)
*   **Remote VPN**: ![Graph](./test_results_Ensemble/remote_vpn_ensemble_evolution.png)
*   **Public Wi-Fi**: ![Graph](./test_results_Ensemble/public_wifi_ensemble_evolution.png)
*   **BYOD**: ![Graph](./test_results_Ensemble/byod_ensemble_evolution.png)
*   **Compromised Host**: ![Graph](./test_results_Ensemble/compromised_ensemble_evolution.png)
*   **Untrusted Domain**: ![Graph](./test_results_Ensemble/untrusted_device_geofence_ensemble_evolution.png)

---

## Appendix G: Trust Domain Metrics

The following table formalizes the mathematical equations utilized by the Dempster-Shafer combination engine to calculate the individual domain trust values ($T_{D_i}$) from their underlying aggregated metrics ($M_{i,j}$).

| Domain | Metrics ($M_{i,j}$) | Domain Trust ($T_{D_i}$) |
| :--- | :--- | :--- |
| **Data Trust**<br>($T_D$) | $M_{D,1}$ (Integrity),<br>$M_{D,2}$ (Freshness),<br>$M_{D,3}$ (Authenticity) | $T_D = \sum_{j=1}^{3} \lambda_{D,j} \cdot M_{D,j}$ |
| **Device Trust**<br>($T_{Dev}$) | $M_{Dev,1}$ (Identity),<br>$M_{Dev,2}$ (Reputation),<br>$M_{Dev,3}$ (Compliance) | $T_{Dev} = \sum_{j=1}^{3} \lambda_{Dev,j} \cdot M_{Dev,j}$ |
| **Network Trust**<br>($T_N$) | $M_{N,1}$ (Anomaly Detection),<br>$M_{N,2}$ (Protocol Score),<br>$M_{N,3}$ (Node Reputation) | $T_N = \sum_{j=1}^{3} \lambda_{N,j} \cdot M_{N,j}$ |
| **Application Trust**<br>($T_{App}$) | $M_{App,1}$ (Behavior Consistency),<br>$M_{App,2}$ (Vulnerability Score),<br>$M_{App,3}$ (Access Compliance) | $T_{App} = \sum_{j=1}^{3} \lambda_{App,j} \cdot M_{App,j}$ |
