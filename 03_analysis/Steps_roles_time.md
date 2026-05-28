# Temporal Dynamics & The Role of Variance in Trust Fusion (Time-Decayed)

## Abstract
This document analyzes the temporal evolution of trust within the Dynamic Weighted Belief Fusion engine, specifically focusing on the interaction between **Signal Variance** (Stability) and **Session Decay** (Freshness).
It examines how the "Initialization Phase" (Steps 0-9) behaves under the pressure of a linear time-decay model, where the "Value of Trust" depreciates with every time step.

## 1. The Interaction of Convergence and Decay

The simulation window (Time Steps $t=0$ to $t=9$) now represents a race between two opposing forces:
1.  **Convergence (Constructive)**: The system building confidence through accumulated history ($N=10$).
2.  **Decay (Destructive)**: The session freshness effectively "rusting" the trust score.

### Phase 1: Initialization ($t=0$)
*   **State**: Fresh Session ($D(t) = 1.0$).
*   **Trust Mechanics**:
    *   **Variance**: $\sigma^2 \rightarrow 0$ (Naive Trust).
    *   **Freshness**: $1.0$ (Max Value).
*   **Significance**: Step 0 is the "Golden Moment". It is the only point in time where the system can theoretically achieve a Perfect Trust Score (1.0). In our simulations, the Corporate Office scenario achieves $\approx 0.97$ here. This validates the initial authentication exchange.

### Phase 2: The "Honeymoon" Period ($t=1 \rightarrow 5$)
*   **State**: High Freshness ($D(t) \approx 0.9$), Low Variance.
*   **Dynamics**:
    *   **Stable Scenarios**: The variance remains low, so $W_{context} \approx 1.0$. The decay factor $D(t)$ is the *dominant* reducer of trust.
    *   **Unstable Scenarios**: Variance spikes quickly. Here, $W_{context}$ drops *faster* than $D(t)$.
*   **Key Finding**: In high-risk scenarios (Public Wi-Fi), the **Variance Penalty** outpaces the **Time Decay**. The system revokes trust due to *instability* long before the session expires naturally.

### Phase 3: Convergence and Decline ($t=6 \rightarrow 15$)
*   **State**: Moderate Freshness ($D(t) \rightarrow 0.5$).
*   **Dynamics**: By Step 9, the variance calculation has fully stabilized.
*   **The Crossover Point**: Around Step 15 (Mid-Session), the Decay Factor becomes the primary driver for all scenarios.
    *   Even if variance is 0 (perfect stability), $D(15) = 0.5$.
    *   Max Possible Trust Score = $0.5$.
    *   **Result**: This forces a transition from **Full Access** to **Limited Access** (or No Access) regardless of behavior.

---

## 2. Variance Analysis by Scenario (with Time Decay)

The addition of Time Decay ($D(t)$) alters the effective "Trust Horizon" for each scenario.

### 2.1 Corporate Office
*   **Variance**: $\approx 0.0$ (Negligible).
*   **Decay Impact**: Purely linear. The Trust Score tracks the Decay Curve almost perfectly.
    $$ T_{final} \approx 1.0 \times (1 - t/30) $$
*   **Outcome**: The user gets the maximum possible session length, but still faces a hard stop at $t=30$.

### 2.2 Public Wi-Fi
*   **Variance**: High ($\sigma^2 > 0.2$).
*   **Decay Impact**: Compounded.
    $$ T_{final} \approx W_{low} \times (1 - t/30) $$
*   **Outcome**: The low weight ($W_{low} \approx 0.4$) combined with the decay ($D(t)$) means the Trust Score drops below usable levels ($< 0.45$) very quickly.
    *   **Effective Session**: $\approx 15$ steps.
    *   **Security Value**: The system inherently creates a "Short Session" policy for risky networks without explicit configuration.

### 2.3 Compromised Host
*   **Variance**: Extreme.
*   **Decay Impact**: Irrelevant.
    *   $W_{context} \rightarrow 0$.
    *   $T_{final} \approx 0 \times D(t) = 0$.
*   **Outcome**: **Immediate Revocation**. The time decay is a secondary safeguard, ensuring that even if the attack stops, the "stale" session cannot be resurrected.

## 3. Mathematical Implication
The Time-Decayed model introduces a **Universal Dampener**:
$$
\lim_{t \to T_{max}} \text{Trust}(S) = 0
$$
This proves that in a Zero Trust architecture, **Time is a Vulnerability**. The longer a session exists, the less trustworthy it becomes, regardless of the entity's behavior. Steps 0-9 are no longer just about establishing stability; they are about establishing the *initial value* from which the inevitable decline begins.
