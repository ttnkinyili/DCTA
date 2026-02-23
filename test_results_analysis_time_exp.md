# Test Results Analysis: Exponential Time Decay Model

## 1. Overview
This document analyzes the simulation results from the `dynamic_trust_weighting_time_exp.py` model, generated in the `/test_results_time_exp/` directory.

The key distinction in this model is the application of **Exponential Temporal Decay** ($D_{exp}(t) = e^{-3.0(t/30)}$) to the Pignistic probability (Trust Score) instead of a linear degradation. 

## 2. Global Observations on Exponential Decay
The most striking feature of the exponential data is the extreme velocity at which trust evaporates.
1.  **Step 0**: The Decay Factor is $\approx 0.90$ (due to calculating at the end of the first time slice step). The spatial trust ($T_{spatial}$) heavily dictates the score.
2.  **Step 15 (Mid-Session)**: The Decay Factor plummets to $0.20$.
3.  **Step 29 (End-Session)**: The Decay Factor bottoms out at $0.05$.

Unlike linear decay, where half the time means half the trust, exponential decay means half the time leaves only $\approx 20\%$ of the original trust weight.

### 2.3 The Role of Lambda ($\lambda$)
In the exponential temporal decay function $D_{exp}(t) = e^{-\lambda (t / T_{session})}$, the constant **$\lambda$ (lambda)** dictates the steepness or "velocity" of the initial drop in trust. 
*   **High $\lambda$ (e.g., $\lambda \ge 5.0$)**: Causes trust to plummet precipitously the moment the session begins. This creates an extremely narrow verification window, virtually demanding continuous re-authentication. It is suitable only for the most critical, zero-tolerance operations.
*   **Low $\lambda$ (e.g., $\lambda \le 1.0$)**: Flattens the curve, making the initial depreciation much more gradual (resembling a linear decay in the early stages). This allows the initial "Freshness" to retain its authority longer, prioritizing user continuity over strict temporal security.
*   **Calculated Balance ($\lambda = 3.0$)**: In our simulation, $\lambda$ is calibrated to 3.0 specifically so that at the end of the session timeframe ($t = T_{session}$), the decay factor reaches effectively zero ($e^{-3.0} \approx 0.05$). This structural choice ensures a rapid transition of decision-making power from the initial snapshot to historical inertia, without instantly dropping the session in the very first step.

## 3. Scenario Analysis

### 3.1 The "Happy Paths" (Corporate Office & VPN)
*   **Result**: Start at $\approx 0.70$ (Limited Access) and immediately crash well below the 0.45 (No Access) threshold by step 15 ($\approx 0.20$).
*   **Analysis**: In a linear model, these users enjoyed 7-8 minutes of Full Access. Here, despite near-perfect spatial indicators ($0.95+$ across the board), the exponential pressure strips access almost instantly. 
*   **Conclusion**: An exponential model cannot be deployed in isolation for an enterprise environment. It enforces a "Handshake Only" paradigm where users would require continuous re-authentication every $\approx 3-5$ minutes.

### 3.2 The "Risky Paths" (Public Wi-Fi & BYOD)
*   **Result**: Start lower ($\approx 0.54$) and drop even faster. By step 15, they are under $0.18$.
*   **Analysis**: The exponential decay acts as an incredibly aggressive session terminator for risky contexts. 

### 3.3 The "Denied Paths" (Compromised & Untrusted Geofence)
*   **Result**: Start below the threshold ($\approx 0.23 - 0.30$) and are denied immediately at step 0.
*   **Analysis**: The temporal factor is irrelevant here; spatial fusion correctly identifies the threat and blocks access before time even has a chance to pass.

## 4. The "Handshake Priority" vs Operational Reality
The empirical data from `sample_outputs.txt` confirms the theoretical thesis: **Exponential Temporal Decay is a session killer.**

Because $e^{-\lambda t}$ creates an aggressive curve, the system essentially screams: *"I only trust the verification you gave me EXACTLY when you logged in. Every moment that passes since then makes me exponentially more suspicious."*

While mathematically fascinating, this proves that Zero Trust architectures **must** employ a counter-balance to time decay. If a session ages out exponentially, the system *must* be capable of transferring that lost verification weight onto something else (like behavioral consistency, which is the foundation of the **Ensemble Model**).
