# Time-Bounded Zero Trust: The Exponential Decay Model

## 1. Overview
This integration introduces **Temporal Decay** as a dedicated dimension within the Zero Trust Belief Fusion engine. 

While spatial dimensions (Network, Device, Data, App) evaluate *instantaneous context*, the temporal dimension evaluates *session freshness*. In this variant, we use an **Exponential Decay** function. This shifts the architectural paradigm from a static "Time-to-Live" (linear) to a dynamic "State Handover" where verification must occur rapidly at the start of a session, and initial trust swiftly erodes, transferring the security burden linearly onto historical inertia (as seen in the Ensemble model).

## 2. Core Mechanism: Exponential Temporal Decay

### 2.1 The Decay Function ($D_{exp}(t)$)
Instead of a straight line, trust weight drops exponentially based on the session duration.

$$ 
D_{exp}(t) = e^{-\lambda \left(\frac{t}{T_{session}}\right)} 
$$

Where:
*   $t$ is the current time step (e.g., minutes).
*   $T_{session}$ is the maximum session boundary (e.g., 30 steps).
*   $\lambda$ is the decay constant calibrated to ensure the trust reaches near-zero at the boundary (we use $\lambda = 3.0$ so that $e^{-3.0} \approx 0.05$).

### 2.2 Integration Sequence
The script `dynamic_trust_weighting_time_exp.py` modifies the original fusion pipeline:

1.  **Read Context**: Gather Network, Device, Data, App scores.
2.  **Calculate Initial Weights**: Determine the normalized base weight for each domain using variance (as before).
3.  **Apply Exponential Decay**: Multiply the base weights by the temporal decay factor $D_{exp}(t)$.
    *   $W_{effective} = W_{base} \times D_{exp}(t)$
    *   *Result*: As time progresses, the mathematical *Evidence Mass* provided by the initial spatial context shrinks rapidly.
4.  **Dempster-Shafer Fusion**: The shrinking evidence mass translates directly to increased **Uncertainty**.
5.  **Final Trust Scaling**: To represent explicit session validity, the final Trust Score (BetP) is also scaled by the decay factor, forcing a hard drop-off in access decisions.

## 3. Mathematical Implications of Exponential Decay

### 3.1 The "Handshake Priority"
In linear decay, an authentication event from 10 minutes ago retains $\approx 66\%$ of its original authority. In exponential decay (with $\lambda=3.0$), an event from 10 minutes ago drops to $e^{-1.0} \approx 36\%$ of its authority.
This forces the system into a "Handshake Priority" state: the spatial context dictates access almost entirely in the first few minutes, but that authority evaporates rapidly, drastically reducing the window of opportunity for attackers attempting session hijacking.

### 3.2 Accelerated Threshold Crossings
Because trust drops off a cliff rather than gliding down a slope, the "Effective Session Lengths" (the time before a user drops from Full to Limited, or Limited to None) are significantly shorter and more aggressive than in the linear model.

## 4. How to Run the Exponential Temporal Simulation
1.  Run the simulation generator:
    ```bash
    python3 run_scenarios_time_exp.py
    ```
2.  This will output data into the `/test_results_time_exp/` directory:
    *   **Graphs**: Visual representations of the rapid trust evaporation per scenario.
    *  **`sample_outputs.txt`**: A table showing the trust state at the beginning, middle, and end of the session.

## 5. Next Steps
The extreme speed of exponential decay highlights why a pure "Time + Spatial" model is inherently unstable for long-term productivity: users would be constantly booted from their sessions after 5-10 minutes. 

This mathematical reality proves the necessity of the **Ensemble Model**, which catches the user as the fresh signal decays, substituting the rapidly vanishing evidence with the accumulated weight of their consistent behavioral history (Inertia).
