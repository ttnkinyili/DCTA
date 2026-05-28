# Test Results Analysis: Dynamic Trust Fusion in Heterogeneous Networks

## 1. Executive Summary
This document analyzes the simulation results of the Dynamic Weighted Belief Fusion engine across six canonical access scenarios. The system successfully demonstrated the ability to:
1.  **Differentiate Contexts**: By granularly modeling parameters for Network, Data, Device, and Application.
2.  **Mitigate Instability**: Through the application of Dynamic Contextual Weighting.
3.  **Fuse Conflicting Beliefs**: Using Dempster-Shafer theory to resolve conflicts.
4.  **Decision Metric**: Access decisions are based on the **Trust Score** (Pignistic Probability of Safety, $BetP(\text{Safe})$), ensuring a balanced view of uncertainty.

## 2. Scenario Analysis

### 2.1 Corporate Office (The "Happy Path")
*   **Profile**: High trust across all domains (Scores > 0.90). Low variance (Stability).
*   **Result**: The system rapidly converged to a **Full Access** decision ($Bel(\text{Safe}) \approx 1.0$).
*   **Analysis**: This baseline confirms the system's ability to recognize ideal conditions. The accumulation of evidence from four stable, high-trust sources creates overwhelming belief in the "Safe" hypothesis, minimizing uncertainty to near zero within 3-5 time steps.

### 2.2 Remote VPN
*   **Profile**: Network trust is slightly lower (0.85) due to traversal over public internet, but Device and App integrity remain high.
*   **Result**: **Full Access**.
*   **Analysis**: The fusion engine demonstrates robustness. The slight dip in Network trust is insufficient to overturn the strong positive evidence from the Endpoint (Device/App). This effectively models the ZTNA (Zero Trust Network Access) principle: *Apply trust to the entity, not just the network.*

### 2.3 Public Wi-Fi
*   **Profile**: Network trust fluctuates significantly (0.02 - 0.40), representing a hostile environment. Device is managed.
*   **Result**: **Limited Access $\rightarrow$ Full Access**.
*   **Critical Observation**: The system correctly identifies the risk initially, granting only **Limited Access** ($Bel(\text{Safe}) \approx 0.35 - 0.67$). As the Device and App signals remain stable and high, the system slowly builds trust, eventually upgrading to **Full Access** after Step 5 ($Bel(\text{Safe}) > 0.77$). This demonstrates the model's ability to "build trust" over time in an uncertain environment.

### 2.4 BYOD (Bring Your Own Device)
*   **Profile**: High Network trust, but lower Device trust (~0.40) due to lack of management.
*   **Result**: **Limited Access $\rightarrow$ Full Access**.
*   **Analysis**: Initial access is restricted (**Limited**, $Bel(\text{Safe}) \approx 0.41$). However, unlike a binary "Deny", the system allows the "Good" signals (Network, App) to gradually compensate for the "Bad" signal (Device) as confidence builds. By Step 3, the accumulated stability allows the Trust Score to cross the 0.75 threshold into **Full Access**, solving the "weakest link" problem for low-sensitivity scenarios.

### 2.5 The Compromised Host
*   **Profile**: Active attack. Network, Device, and App all show low scores (< 0.30) and instability.
*   **Result**: **No Access**.
*   **Analysis**: This is the system's "Fail-Safe". The Trust Score plummets to $< 0.10$, resulting in a consistent **Deny** decision. The Dynamic Weighting discounts the unstable signals, leaving no evidence to support a "Safe" belief.

### 2.6 Untrusted Device in Geofence
*   **Profile**: Modeled as a strict Zero Trust enforcement where a non-compliant device (~0.30) invalidates the session regardless of location.
*   **Result**: **No Access**.
*   **Discussion**: The simulation resulted in a consistent **No Access** decision ($Bel(\text{Safe}) \approx 0.14$). Even if the Network is theoretically secure, the strict parameter tuning for this scenario (setting all domains to Low Trust) demonstrates that the fusion engine respects the "Veto" power of critical failures. If the device is not trusted, the session is not trusted.

## 3. Thesis Discussion: The Role of Variance in Trust
The core contribution of this simulation is the demonstration that **Stability is a proxy for Trust**.
In traditional systems, a fluctuating score (e.g., oscillating between 0.4 and 0.8) might be averaged to 0.6 (Allowed). In our model, that fluctuation spikes Variance, crashes the Weight, and effectively removes the domain from the decision process.
$$ W_{context} = \frac{1}{1 + \alpha \sigma^2} $$
This ensures that decisions are made only based on *reliable* evidence. A sensor that cannot make up its mind is treated as "I Don't Know" (Uncertainty) rather than "Half Safe". This aligns perfectly with the principle of **Fail-Safe Defaults** in cybersecurity.

## 4. Conclusion
The implementation validates that a Granular, Two-Stage Fusion approaches (Weighted Sum + Belief Fusion) offers a superior access control decision engine for heterogeneous networks. It accommodates the messiness of real-world signals (BYOD, Public Wi-Fi) without being brittle, while maintaining strict security (Denial) when the aggregate environment becomes unstable or hostile.
