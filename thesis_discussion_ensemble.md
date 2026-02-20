# The Ensemble Trust Model: Inertia as the Foundation of Continuous Authentication

## Abstract
This document analyzes the theoretical underpinnings of the Ensemble Trust Model. By hybridizing **Short-Term Spatial Fusion** (Dempster-Shafer) with **Long-Term Temporal Inertia** (Exponential Decay), we establish a system that resolves the fundamental tension in Zero Trust: **Security vs. Usability**.

## 1. The Core Thesis: Trust has Momentum
Traditional Zero Trust Architectures (ZTA) often treat every access request as a discrete, independent event. This leads to the "Jittery Access" problem, where minor, transient fluctuations in network latency or device CPU usage cause authentication failures.

Our Ensemble Model posits that **Trust has Momentum (Inertia)**.
*   **Physics Analogy**: A massive object (High History) requires significant force (Strong Evidence) to change its trajectory.
*   **Security Implication**: A user with a strong history of safe behavior should not be revoked due to a single dropped packet (Noise). Conversely, a user with a history of compromise should not be reinstated due to a single clean packet (Beaconing).

## 2. The Freshness-Inertia Continuum
The model implements a dynamic slider between **Signal** and **Memory**, governed by "Session Freshness" ($W_{fresh}$).

### 2.1 The Fresh Session ($t \rightarrow 0$)
*   **State**: $W_{fresh} \approx 1.0$.
*   **Dynamics**: The model is **Signal-Dominant**.
*   **Logic**: "I don't know you yet (in this session). I need to see your current ID, your current Device Health, and your current Network."
*   **Thesis**: At the start of a session, **Verification must be Absolute**. Inertia should not override a bad login.

### 2.2 The Mature Session ($t \rightarrow 30$)
*   **State**: $W_{fresh} \rightarrow 0$.
*   **Dynamics**: The model is **Inertia-Dominant**.
*   **Logic**: "I have been watching you for 29 minutes. Your behavior has been consistent. I will trust my *accumulated knowledge* of you more than this specific millisecond's reading."
*   **Thesis**: As verification ages, **Consistency becomes Policy**. The system effectively "locks in" the decision, reducing the attack surface for session hijacking (a hijacker would need to mimic the established history perfectly to avoid triggering a massive deviation, but even then, the inertia resists rapid change).

## 3. The Role of Time Sessions

### 3.1 Short-Term Network Session ($T_{short} = 30 \text{ min}$)
*   **Role**: **Verification & Freshness**.
*   **Justification**:
    *   **NIST SP 800-63B (AAL2)**: Requires re-authentication after **30 minutes of inactivity**.
    *   **PCI DSS v4.0**: Mandates **15-minute idle timeouts** for critical data environments. We use 30 minutes as a standard enterprise baseline, with 15 minutes as a "Critical" option.
*   **Calculation**:
    We use an **Exponential Decay** function to weight the "Freshness" of the current signal.
    $$ W_{short}(t) = e^{-3.0 \cdot \frac{t}{30}} $$
    *   At $t=0$, $W_{short} = 1.0$ (Full Signal Weight).
    *   At $t=30$, $W_{short} \approx 0.05$ (Near Zero Signal Weight).
    *   **Why Exponential?**: Linear decay is too slow. We want to prioritize freshness heavily in the first few minutes (the "Handshake" phase) and then rapidly transition to stability.

### 3.2 Long-Term Device Session ($T_{long} = 48 \text{ hours}$)
*   **Role**: **Productivity & Continuity**.
*   **Justification**:
    *   **Microsoft Entra ID**: Default "Keep Me Signed In" (KMSI) behavior often extends for **24+ hours** (rolling window).
    *   **Usability**: A 48-hour window covers the "Weekend Gap" (Friday 5 PM to Monday 9 AM), preventing a forced full re-login on Monday morning for valid devices.
    *   **Strict Compliance Note**: For NIST AAL3 (Gov/Critical), this must be capped at **12 Hours**.
*   **Calculation**:
    The inertia itself decays over this long horizon to ensure that even a good history eventually expires and requires re-proofing.
    $$ D_{long}(\Delta t) = e^{-\lambda \cdot \Delta t} $$
    Where $\lambda$ is calibrated such that $D_{long}(48h) \approx 0.05$.
    *   This means "Trust decays to near-zero after 48 hours of silence."

## 4. Mathematical Validation (The Ensemble Formula)
The Weighted Mixture formula ensures stability by combining these two timeframes:

$$ T_{ensemble} = \underbrace{[T_{instant} \cdot W_{short}(t)]}_{\text{Fresh Signal}} + \underbrace{[(T_{prev} \cdot D_{long}) \cdot (1 - W_{short}(t))]}_{\text{Historical Inertia}} $$

*   **In User Terms**:
    *   **Good Employee**: Starts with Full Access. As time passes ($t \rightarrow 30$), the "Need for Fresh Signals" ($W_{short}$) decreases because they have built up "Momentum". Access persists smoothly.
    *   **Attacker**: Starts with No Access. As time passes, the system "Remembers" they are bad. Even if they mimic a safe signal at minute 29, the Inertia ($1 - W_{short} \approx 0.95$) weighs the history of "Bad" so heavily that access remains denied.

## 5. Conclusion
The Ensemble Model successfully implements **Contextual Durability**. It moves Zero Trust from a stateless "Packet Fighter" to a stateful "Behavior Engine," enabling robust security that respects the continuity of legitimate work.
