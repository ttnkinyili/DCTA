# Temporal Dynamics & The Role of Variance in Trust Fusion

## Abstract
This document analyzes the temporal evolution of trust within the Dynamic Weighted Belief Fusion engine. Specifically, it examines the critical "Initialization Phase" (Steps 0-9) where the system transitions from a static, variance-agnostic baseline to a mature, historically-weighted decision state. It further details how signal variance manifests in each scenario to drive access control outcomes.

## 1. The Role of Simulation Steps 0-9

The simulation window (Time Steps $t=0$ to $t=9$) is not arbitrary; it represents the **Convergence Interval** of the trust engine. This interval is defined by the sliding window size of the history buffer (10 steps).

### Phase 1: Initialization ($t=0$)
*   **State**: Tabula Rasa. The system has exactly one data point per parameter.
*   **Mathematical Consequence**: Variance calculation requires at least two data points ($N \ge 2$). The standard variance formula is functionally undefined or zero:
    $$
    \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}
    $$
    At $t=0$, we assume $\sigma^2 \rightarrow 0$.
*   **Functional Weighting**: The weighting function defaults to its maximum value (or uniform weights) because the denominator term vanishes:
    $$
    W = \frac{1}{1 + \alpha \sigma^2} \xrightarrow{\sigma^2 \to 0} 1.0
    $$
*   **Significance**: Step 0 represents the **"Naive Trust"** assessment. It reflects the pure sensor readings without the context of stability. A fluctuating sensor that happens to be "high" at $t=0$ will be fully trusted, potentially leading to a Type I error (False Positive) *only* at this specific instant.

### Phase 2: Variance Onset ($t=1 \rightarrow 2$)
*   **State**: The system acquires its second and third data points.
*   **Differentiation**: This is the critical bifurcation point.
    *   **Stable Signals**: $x_1 \approx x_0 \Rightarrow \sigma^2 \approx 0 \Rightarrow W \approx 1.0$. Trust is maintained.
    *   **Volatile Signals**: $x_1 \not\approx x_0 \Rightarrow \sigma^2 \uparrow \Rightarrow W \downarrow$. Trust begins to degrade immediately.
*   **Significance**: The engine begins to distinguish "Quality of Evidence" from "Quantity of Evidence".

### Phase 3: Convergence ($t=3 \rightarrow 9$)
*   **State**: The history buffer accumulates data up to its window size ($N=10$).
*   **Statistical Significance**: The variance $\sigma^2$ stabilizes, becoming a robust metric of the signal's true behavior rather than stochastic noise.
*   **Outcome**: By Step 9, the Trust Score ($Bel(\text{Safe})$) has converged to its steady-state value. The decision made at $t=9$ is the "True" decision of the Weighted Belief model.

---

## 2. Variance Analysis by Scenario

Variance is the primary mechanism for **Evidence Discounting**. The following table details how variance manifests in each scenario to alter the Trust weights.

### 2.1 Corporate Office
*   **Variance Profile**: $\sigma^2_{all} \approx 0.0$ (Near Zero).
*   **Mechanism**: Parameters are modeled with tight Gaussian distributions (e.g., `Device Score = 0.95`, `Variance = 0.01`).
*   **Effect**:
    $$
    W_{Network} \approx 1.0, \quad W_{Device} \approx 1.0
    $$
*   **Result**: All evidence is treated as reliable. High scores translate directly to high Belief.
*   **Outcome**: **Robust Full Access**.

### 2.2 Public Wi-Fi
*   **Variance Profile**:
    *   $\sigma^2_{Device} \approx 0.0$ (Stable, Managed).
    *   $\sigma^2_{Network} \gg 0.2$ (High Instability).
*   **Mechanism**: The Network domain simulates packet loss, latency jitter, and routing changes typical of public hotspots. This continually spikes the variance calculation for parameters like `Anomalies` and `ProtocolScore`.
*   **Effect**:
    $$
    W_{Device} \rightarrow \text{High} \quad (\approx 1.0)
    $$
    $$
    W_{Network} \rightarrow \text{Low} \quad (< 0.2)
    $$
*   **Result**: The Network's potentially conflicting evidence ("I am barely safe") is **discounted**. In Dempster-Shafer theory, this discounted mass moves to **Uncertainty** ($m(\Theta)$) rather than "Unsafe".
*   **Outcome**: **Limited Access** initially (due to Uncertainty). As the Device proves its stability over $t=0 \rightarrow 9$, the accumulated positive mass from the Device eventually outweighs the uncertainty from the Network, potentially upgrading to **Full Access**.

### 2.3 BYOD
*   **Variance Profile**:
    *   $\sigma^2_{Network} \approx 0.0$ (Stable Corporate Network).
    *   $\sigma^2_{Device} \approx 0.2$ (Unmanaged, varied usage).
*   **Mechanism**: The unmanaged device exhibits fluctuating compliance scores (e.g., user installs/removes apps, OS updates lag).
*   **Effect**:
    $$
    W_{Network} \approx 1.0
    $$
    $$
    W_{Device} \rightarrow \text{Penalized}
    $$
*   **Result**: The model trusts the Environment (Network) but doubts the Endpoint (Device).
*   **Outcome**: The stable Network provides a "Safety Net". While the Device is untrusted, the high-confidence signal from the Network prevents a complete lockout, allowing **Limited Access**.

### 2.4 Compromised Host
*   **Variance Profile**: $\sigma^2 \gg 0.3$ across **multiple** domains (Network, Device, App).
*   **Mechanism**: Active attacks generate chaotic signals (e.g., massive spikes in CPU usage, rapid connection resets).
*   **Effect**:
    $$
    W_{all} \rightarrow 0
    $$
*   **Result**: Systemic Discounting. The Fusion Engine effectively says "I cannot trust *anything* I am seeing."
*   **Outcome**: With almost all mass shifted to Global Uncertainty ($m(\Theta) \approx 1.0$) and almost zero belief in Safety ($Bel(\text{Safe}) \approx 0$), the default **Fail-Safe** policy triggers: **No Access**.

## 3. Mathematical Implication
The implementation proves that:
$$
\lim_{t \to 9} \text{Trust}(S) \neq \text{Trust}(S_{t=0})
$$
Trust is not a snapshot; it is an integral over time. Steps 0-9 represent the calculation of this integral.
