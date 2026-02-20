# Test Results Analysis: Time-Decayed Dynamic Trust Fusion

## 1. Executive Summary
This document analyzes the simulation results of the Time-Decayed Trust Fusion engine (`weighted_belief_fusion_2.py`). This enhanced model introduces a critical dimension to Zero Trust: **Temporal Validity**. 
Unlike the static-session baseline, this model enforces a linear decay of trust based on "Session Freshness," simulating the degradation of authentication confidence over a 30-minute window.

**Key Outcome**: The system successfully demonstrated that **Trust is Ephemeral**. Regardless of signal quality, all sessions naturally expire (Trust Score $\rightarrow$ 0) as $t \rightarrow 30$, enforcing a hard re-authentication requirement.

## 2. Scenario Analysis (Temporal Dynamics)

The following analysis focuses on the interaction between **Signal Quality** (Spatial) and **Session Decay** (Temporal).

### 2.1 Corporate Office (The "Fading" Happy Path)
*   **Profile**: High trust signals (Network/Device > 0.90) with Low Variance.
*   **Temporal Evolution**:
    *   **Start ($t=0$)**: **Full Access** (Trust Score $\approx$ 0.97). Credentials are fresh.
    *   **Mid-Session ($t=15$)**: **Limited Access**. Decay factor drops to 0.5. Trust Score $\approx$ 0.47.
    *   **End ($t=29$)**: **No Access**. Decay factor $\rightarrow$ 0. Trust Score = 0.00.
*   **Analysis**: This validates the "Session Timeout" policy. Even in a secure environment, the mere passage of time erodes the validity of the initial grant.

### 2.2 Remote VPN
*   **Profile**: Strong Device/App signals, slightly lower Network trust.
*   **Temporal Evolution**:
    *   **Start**: **Full Access** ($\approx$ 0.96).
    *   **Mid-Session**: **Limited Access**. The combination of lower Network trust and temporal decay pushes the score below the 0.75 threshold faster than in the Corporate scenario.
    *   **End**: **No Access**.
*   **Analysis**: Demonstrates that "Good Behavior" cannot prolong a session indefinitely. The breakdown of trust is inevitable.

### 2.3 Public Wi-Fi
*   **Profile**: High Network Variance (Instability).
*   **Temporal Evolution**:
    *   **Start**: **Limited Access** ($\approx$ 0.55). The initial instability prevents Full Access.
    *   **Mid-Session ($t=15$)**: **No Access** ($\approx$ 0.22). The decay factor exacerbates the already low confidence, causing the session to terminate *early* (before $t=30$).
    *   **End**: **No Access**.
*   **Critical Observation**: **Accelerated Revocation**. In high-risk environments, the "Effective Session Length" is shorter. The trust score drops below the 0.45 threshold at step 15, effectively halving the usable session time compared to a secure corporate office.

### 2.4 BYOD (Bring Your Own Device)
*   **Profile**: Low Device Trust, Stable Network.
*   **Temporal Evolution**:
    *   **Start**: **Limited Access** ($\approx$ 0.54).
    *   **Mid-Session**: **No Access** ($\approx$ 0.21).
*   **Analysis**: Similar to Public Wi-Fi, the lower starting trust means the "Buffer" against temporal decay is smaller. A BYOD user must re-authenticate more frequently to maintain access.

### 2.5 The Compromised Host
*   **Profile**: Active attack signals.
*   **Result**: **No Access** throughout ($t=0 \rightarrow 30$).
*   **Analysis**: The temporal decay is redundant here; the spatial fusion (Variance Discounting) already vetoes access ($\approx$ 0.25 initially). However, the decay ensures that even if the attack ceases, the session remains invalid.

### 2.6 Untrusted Device in Geofence
*   **Profile**: Strict Zero Trust enforcement.
*   **Result**: **No Access**.
*   **Analysis**: Consistent denial. The temporal factor merely reinforces the existing "Zero Trust" posture.

## 3. Thesis Discussion: Temporal Decay as a Security Feature
The integration of a linear decay factor ($D_t = 1 - t/T_{max}$) fundamentally alters the decision landscape:

$$ 
\text{Final Trust} = \text{Trust}_{spatial} \times D_t 
$$

This ensures that **Certainty is not static**. A "Full Access" decision is a depreciating asset. This forces the system to re-evaluate the "Cost of Trust" continuously, aligning with the core philosophy of **Continuous Adaptive Risk and Trust Assessment (CARTA)**.

## 4. Conclusion
The Time-Decayed model successfully implements a dynamic "Time-to-Live" (TTL) for trust. It provides a nuanced behavior where:
1.  **Secure Contexts** enjoy the full session duration.
2.  **Risky Contexts** suffer from accelerated timeout (Effective TTL < Nominal TTL).
This adaptive session management significantly reduces the attack surface for session hijacking.
