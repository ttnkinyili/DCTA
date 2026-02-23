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

#### Calibrating History vs. Variance with $\alpha$
In integrating long-term temporal inertia with real-time Dempster-Shafer fusion, the baseline variance sensitivity parameter ($\alpha$) located within the dynamic weighting mechanism ($W_d = \frac{1}{1 + \alpha \cdot \sigma^2}$) regulates how effectively historical stability can be overridden by present instability. 
*   A stable, 48-hour history accumulates significant mass, functioning as computational momentum. If a device suddenly broadcasts highly variable health signals (significant variance), a large sensitivity index (e.g., **$\alpha \ge 10$**) immediately collapses the signal weight of the current behavior. Therefore, the architecture relies almost entirely on the long-term inertia until an anomalous behavioral trend is sustained over multiple periods.
*   Following recommendations from reputation degradation architectures (Mui et al., 2002, "A Computational Model of Trust and Reputation"), long-term session evaluation optimally functions with a balanced parameter (**$\alpha = 5.0$**). This configuration prevents the system's historical evaluation from being prematurely disrupted by benign sensor spikes, ensuring the long-term exponential factor ($D_{long}$) primarily governs the context's baseline evaluation.

### 3.3 Constants and Tuning Parameters in the Ensemble Model

The mathematical effectiveness of the Ensemble Trust Model relies on calibrating three primary constants: Euler's number ($e$), the decay velocity ($\lambda$), and the variance sensitivity ($\alpha$). Their tuning must align with Continuous Adaptive Trust (CAT) capabilities specified in modern frameworks (e.g., CISA Zero Trust Maturity Model v2.0, 2023; DoD Zero Trust Strategy, 2022).

#### Euler's Number ($e \approx 2.71828$)
*   **Role**: Serves as the mathematical base for the natural exponential decay function ($e^{-\lambda t}$). 
*   **Justification**: Unlike linear decay which degrades steadily, or polynomial decay which drops abruptly to zero, the natural exponential function $e$ models continuous, proportional decay. It ensures that the "Freshness" of a handshake evaporates rapidly but never truly artificially bottoms out at an absolute mathematical zero before the session boundary. This provides the smooth, asymptotic degradation necessary to transfer weight linearly into Historical Inertia over time, making it the industry standard for modeling risk and reputation depreciation.

#### The Decay Velocity Constant ($\lambda$)
*   **Role**: Dictates the steepness or "velocity" of trust depreciation in the exponential function $W_{short}(t) = e^{-\lambda \cdot \frac{t}{T_{short}}}$.
*   **Best Practices and Authoritative Recommendations (2022+)**: Modern Zero Trust frameworks emphasize that initial authentication must be succeeded by dynamic risk assessment to combat credential theft (DoD ZTO, 2022). Trust is ephemeral and must degrade rapidly to force system re-evaluation.
    *   **High $\lambda$ ($\ge 5.0$)**: Causes trust to plummet precipitously. Suitable only for critical, zero-tolerance environments demanding continuous, frictionless re-authentication (e.g., behavioral biometrics).
    *   **Low $\lambda$ ($\le 1.0$)**: Flattens the decay curve, allowing "Freshness" to retain authority longer. Prioritizes user continuity over rapid state expiration.
    *   **Recommended Baseline ($\lambda = 3.0$)**: For enterprise environments balancing security with UX, $\lambda$ should be calibrated to reach an effectively terminal state (e.g., $e^{-3.0} \approx 0.05$) exactly at the maximum idle boundary ($T_{session}$). This forces a predictable transition of decision-making authority away from the initial spatial snapshot.

#### The Variance Sensitivity Parameter ($\alpha$)
*   **Role**: Located in the dynamic weighting mechanism ($W_d = \frac{1}{1 + \alpha \cdot \sigma^2}$), it governs how aggressively the system penalizes uncertainty and instability.
*   **Recommended Baseline ($\alpha = 5.0$)**: In enterprise Zero Trust architectures, setting $\alpha = 5.0$ provides a logistic-style decay that penalizes sustained oscillation while absorbing negligible micro-jitter. This prevents "jitter-induced lockouts" over unstable public networks while retaining mathematical efficacy. For strictly regulated networks, an aggressive $\alpha \ge 10.0$ forces unstable signals to immediately lose influence on the consensus decision.

### 3.4 Recommended Session Lengths 

Based on NIST SP 800-63B guidelines and standard enterprise continuous authentication deployments (2023), the following boundaries are recommended for the Ensemble Engine:

| Session Type | Purpose | Recommended Window ($T$) | Justification |
| :--- | :--- | :--- | :--- |
| **Short-Term (Freshness)** | **Verification** | **30 Minutes** | NIST AAL2 baseline for inactivity. Ensures the "Initial Handshake" value decays rapidly enough to prevent active session hijacking if a device is left unattended. |
| **Short-Term (Critical)** | **Verification** | **15 Minutes** | PCI DSS v4.0 standard for sensitive data environments. Used when evaluating highly classified Data Domain contexts. |
| **Long-Term (Inertia)** | **Continuity** | **48 Hours** | Limits the lifespan of historical momentum. Ensures "Trust" completely decays over a standard weekend gap, forcing a full, fresh re-authentication on Monday morning. |
| **Long-Term (Critical)** | **Continuity** | **12 Hours** | NIST AAL3 standard. Prevents historical inertia from keeping an adversary authenticated overnight in highest-security enclaves. |

## 4. Mathematical Validation (The Ensemble Formula)
The Weighted Mixture formula ensures stability by combining these two timeframes:

$$ T_{ensemble} = \underbrace{[T_{instant} \cdot W_{short}(t)]}_{\text{Fresh Signal}} + \underbrace{[(T_{prev} \cdot D_{long}) \cdot (1 - W_{short}(t))]}_{\text{Historical Inertia}} $$

*   **In User Terms**:
    *   **Good Employee**: Starts with Full Access. As time passes ($t \rightarrow 30$), the "Need for Fresh Signals" ($W_{short}$) decreases because they have built up "Momentum". Access persists smoothly.
    *   **Attacker**: Starts with No Access. As time passes, the system "Remembers" they are bad. Even if they mimic a safe signal at minute 29, the Inertia ($1 - W_{short} \approx 0.95$) weighs the history of "Bad" so heavily that access remains denied.

## 5. Scenario Analysis & Decision Boundaries

We evaluated the ensemble hybrid model against six canonical scenarios to observe how historical inertia impacts security and usability over time. The access thresholds are defined as:
*   **Full Access**: $> 0.75$
*   **Limited Access**: $\ge 0.45$ and $\le 0.75$
*   **No Access**: $< 0.45$

| Scenario | Characteristics | Ensemble Outcome | Discussion |
| :--- | :--- | :--- | :--- |
| **Corporate Office** | Consistently high signals over time. | **Stable Full Access** | High fresh signal transitions smoothly into high inertia. Trust score is practically locked at $\approx 1.0$. |
| **Remote / VPN** | Minor network jitter during a mature session. | **Stable Full Access** | The system relies on the historical inertia of the device/user. Transient VPN drops are absorbed without access revocation. |
| **Public Wi-Fi** | High variance in the fresh network signal. | **Limited $\rightarrow$ Full Access** | System starts cautiously relying on fresh signals. As evidence of good device health accumulates over time, inertia builds, upgrading access to Full. |
| **Untrusted Device / BYOD** | Device lacks history or has low health. | **Limited Access** | High network trust keeps the user in Limited Access, but the lack of positive device history prevents the ensemble score from reaching Full Access. |
| **Compromised** | Sudden, systemic failure across domains. | **Immediate No Access** | If variance ($\sigma^2$) spikes aggressively due to anomalous behavior, the dynamic weight drops, causing the fusion engine to strip access despite any previous positive history. |
| **Beaconing Attacker** | A known bad user sends a single perfect signal. | **No Access** | The system's memory ($1 - W_{short}$) heavily weights the prior history of malicious behavior. A single "clean" packet cannot overcome the inertia of negative trust. |

## 6. Conclusion
The Ensemble Model successfully implements **Contextual Durability**. It moves Zero Trust from a stateless "Packet Fighter" to a stateful "Behavior Engine," enabling robust security that respects the continuity of legitimate work.
