# Understanding the Ensemble Trust Output

This document explains the derivation and role of each component in the Ensemble Trust simulation outputs.
The model calculates trust as a **Weighted Mixture** of **Historical Inertia** and **Current Signal Freshness**.

# 1. Component Definitions

### 1\. Instant_Trust ($T_{instant}$)
*   **Role**: Represents the **Raw Signal Quality** at the current moment ($t$).
*   **Derivation**:
    1.  Collect current sensor readings (Network, Device, Data, App).
    2.  Calculate Domain Scores and Weights (normalized).
    3.  Fuse them using **Dempster-Shafer Theory**.
    4.  Extract the Pignistic Probability of Safety:
        $$ T_{instant} = BetP(\text{Safe}) $$
*   **Significance**: This is what the system *sees* right now. If the network jitters, this score drops immediately.

### 2\. Prev_Trust ($T_{prev}$)
*   **Role**: The **Ensemble Trust Score** from the *previous* time step ($t-1$).
*   **Derivation**:
    *   At $t=0$, this is initialized (e.g., 0.5 or 1.0 depending on scenario).
    *   At $t>0$, $T_{prev}(t) = T_{ensemble}(t-1)$.
*   **Significance**: This is the system's **Memory**. It carries forward the "earned" trust.

### 3\. Freshness_Component ($C_{fresh}$)
*   **Role**: The **Weighted Contribution** of the current instant signal.
*   **Derivation**:
    *   Calculate **Short-Term Weight** based on session age ($t$):
        $$ W_{short} = e^{-\mu_{30m} \cdot t} $$
        (Starts at 1.0, decays to $\approx 0.05$ at 30 mins).
    *   Multiply by Instant Trust:
        $$ C_{fresh} = T_{instant} \times W_{short} $$
*   **Significance**: This component dominates at the **start** of a session. It ensures that initialization is rigorous (verification-heavy). As the session ages, this component shrinks, meaning new signals matter less.

### 4\. Inertia_Component ($C_{inertia}$)
*   **Role**: The **Weighted Contribution** of the historical trust.
*   **Derivation**:
    *   Calculate **Long-Term Decay** (48h refresh cycle):
        $$ D_{long} \approx 1.0 \text{ (over minutes)} $$
    *   Calculate **History Weight** (Inverse of Short-Term):
        $$ W_{history} = 1.0 - W_{short} $$
    *   Combine:
        $$ C_{inertia} = (T_{prev} \times D_{long}) \times W_{history} $$
*   **Significance**: This component dominates at the **end** of a session. It ensures stability (productivity-heavy). It fills the gap left by the shrinking Freshness Component.

### 5\. Ensemble_Trust ($T_{ensemble}$)
*   **Role**: The Final Trust Score used for access decisions.
*   **Derivation**:
    $$ T_{ensemble} = C_{fresh} + C_{inertia} $$
    (Clamped to [0.0, 1.0]).

---

# 2. Sample Walkthrough

### Scenario: Corporate Office (Stable High Trust)

#### Step 0 (Start of Session)
*   **Context**: Fresh login, perfect signal.
*   **Values**:
    *   $T_{instant} \approx 0.79$ (Good Signal).
    *   $W_{short} \approx 1.0$ (High Freshness).
    *   $W_{history} \approx 0.0$ (No History Weight).
*   **Calculation**:
    *   $C_{fresh} = 0.79 \times 1.0 = 0.79$.
    *   $C_{inertia} = 0.5 \times 0.0 = 0.0$.
    *   **$T_{ensemble} = 0.79$**.
*   **Result**: The system trusts the *Signal*.

#### Step 15 (Mid-Session)
*   **Context**: Still perfect signal.
*   **Values**:
    *   $T_{instant} \approx 0.80$.
    *   $W_{short} \approx 0.22$.
    *   $W_{history} \approx 0.78$.
    *   $T_{prev} \approx 0.80$.
*   **Calculation**:
    *   $C_{fresh} = 0.80 \times 0.22 = 0.176$.
    *   $C_{inertia} = 0.80 \times 0.78 = 0.624$.
    *   **$T_{ensemble} = 0.176 + 0.624 = 0.80$**.
*   **Result**: The system trusts the *Mixture*. The score remains high because both Signal and History agree.

---

### Scenario: Compromised Host (Bad Signal)

#### Step 0 (Start)
*   **Values**:
    *   $T_{instant} \approx 0.23$ (Bad Signal).
    *   $W_{short} \approx 1.0$.
*   **Calculation**:
    *   $C_{fresh} = 0.23 \times 1.0 = 0.23$.
    *   **$T_{ensemble} = 0.23$**.
*   **Result**: Immediate Denial.

#### Step 15 (Attacker tries to "wait it out")
*   **Context**: Attacker is still bad, or trying to hide.
*   **Values**:
    *   $T_{instant} \approx 0.35$.
    *   $T_{prev} \approx 0.29$ (From previous bad steps).
    *   $W_{short} \approx 0.22$.
    *   $W_{history} \approx 0.78$.
*   **Calculation**:
    *   $C_{fresh} = 0.35 \times 0.22 = 0.077$.
    *   $C_{inertia} = 0.29 \times 0.78 = 0.226$.
    *   **$T_{ensemble} = 0.077 + 0.226 = 0.30$**.
*   **Result**: **Still Denied**.
*   **Why?**: Even if the attacker spoofs a perfect signal ($1.0$) right now, the Freshness weight is so low ($0.22$) that it can only add $0.22$ to the score. The Inertia ($0.226$) holds the score down near the history of failure. This proves the **Dampening Effect** against rapid spoofing.
