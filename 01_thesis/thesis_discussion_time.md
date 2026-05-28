# Dynamic Trust Fusion with Temporal Decay: A Time-Sensitive Analysis

## Abstract
This document expands upon the Weighted Belief Fusion architecture by introducing a temporal decay factor. The core thesis is that **Trust is a Function of Time**. 
In addition to spatial fusion (Network, Device, Data, App), the system now enforces a linear degradation of trust based on "Session Freshness," effectively creating a dynamic Time-to-Live (TTL) that scales with the initial security posture.

## 1. Introduction: Zero Trust is Continuous
Static authentication creates a security vulnerability: the "Implicit Trust Period." Once a user authenticates, they are typically trusted for the duration of a session (e.g., 8-24 hours).
Our implementation challenges this by enforcing a **Continuous Decay Model**. Trust is not a boolean state achieved at login; it is a depreciating asset that must be continuously renewed or allowed to expire.

## 2. The Temporal Decay Mechanism
We implemented a linear decay function:
$$ 
D(t) = \max \left(0, 1 - \frac{t}{T_{session}}\right) 
$$
Where $t$ is the current time step and $T_{session}$ is the maximum session duration (30 minutes).

### 2.1 Impact on Fusion Logic
The Final Trust Score ($T_{final}$) is the product of the Spatial Trust ($T_{spatial}$) and the Decay Factor ($D(t)$):
$$ 
T_{final} = T_{spatial} \times D(t) 
$$
This structure ensures that regardless of how secure the device or network is ($T_{spatial} \approx 1.0$), the system will inevitably revoke access as $D(t) \rightarrow 0$.

## 3. Scenario Analysis: The Effective Session Length
A key finding from our simulation is that the "Effective Session Length" (time until access revocation) is **context-dependent**.

### 3.1 The "Happy Path" (Corporate Office)
*   $T_{spatial} \approx 0.97$
*   Decay Threshold for Limited Access (0.75):
    $$ 0.97 \times D(t) < 0.75 \Rightarrow D(t) < 0.77 \Rightarrow t \approx 7 \text{ mins} $$
*   **Result**: A user in a secure office enjoys **Full Access** for the first ~7 minutes, then degrades to **Limited Access**, finally losing access at 30 minutes.

### 3.2 The "Risky Path" (Public Wi-Fi)
*   $T_{spatial} \approx 0.55$ (Limited Access initially)
*   Decay Threshold for No Access (0.45):
    $$ 0.55 \times D(t) < 0.45 \Rightarrow D(t) < 0.81 \Rightarrow t \approx 5 \text{ mins} $$
*   **Result**: The user starts with **Limited Access**. However, because their initial trust "buffer" is small, the temporal decay pushes them below the minimum threshold much faster (at ~5 minutes). 
*   **Implication**: **Risky contexts receive shorter effective sessions.** This is a highly desirable security property.

#### The Impact of Variance Sensitivity ($\alpha$) on Risky Paths
In volatile scenarios like Public Wi-Fi connections, network signals are inherently prone to jitter and packet loss, producing high variance ($\sigma^2$). Because the architectural trust discount model leverages dynamic weighting ($W_d = \frac{1}{1 + \alpha \cdot \sigma^2}$), the **sensitivity parameter $\alpha$** plays a critical role in shaping the temporal decay trajectory:

*   If an overly aggressive parameter is utilized (e.g., **$\alpha \ge 10$**), standard Wi-Fi instability rapidly collapses the spatial trust ($T_{spatial}$). As a consequence, the effective session length is severely truncated, often to seconds instead of minutes.
*   By calibrating $\alpha$ to a balanced tier (e.g., **$\alpha = 5.0$**), the fusion engine accommodates the baseline ambient noise of a public network while enforcing the intended ~5-minute decay timeline. As validated in subjective logic computations (Jøsang, 2016), setting an appropriate sensitivity factor is essential to prevent "jitter-induced lockouts" while retaining the mathematical efficacy of continuous temporal decay.

## 4. Scenario Analysis & Decision Boundaries

We evaluated the temporal model against six canonical scenarios to observe how linear decay impacts access durations. The access thresholds remain constant:
*   **Full Access**: $> 0.75$
*   **Limited Access**: $\ge 0.45$ and $\le 0.75$
*   **No Access**: $< 0.45$

| Scenario | Characteristics | Temporal Outcome | Discussion |
| :--- | :--- | :--- | :--- |
| **Corporate Office** | High initial spatial trust ($\approx 0.97$). | **Full $\rightarrow$ Limited $\rightarrow$ No Access** | The high trust buffer ensures a long effective session. Users enjoy ~7 minutes of Full Access before degrading to Limited. |
| **Remote / VPN** | Strong signals across Device/App/Data. | **Full $\rightarrow$ Limited $\rightarrow$ No Access** | Similar to Corporate Office, strong spatial trust provides a durable time-to-live before revocation. |
| **Public Wi-Fi** | Network trust fluctuates ($\approx 0.55$). | **Limited $\rightarrow$ No Access** | The session starts at Limited Access and the temporal decay pulls it below the minimum threshold rapidly ($\approx 5$ mins). |
| **Untrusted Device / BYOD** | Device score is persistently low. | **Limited $\rightarrow$ No Access** | Even with good network trust, the low device score reduces the initial trust buffer, resulting in a significantly shorter session. |
| **Compromised** | All domains failing ($BetP(\text{Safe}) < 0.10$). | **No Access** | Denied immediately at $t=0$; temporal decay is irrelevant. |
| **Untrusted Device (Strict)** | Strict policies against unmanaged devices. | **No Access** | Denied immediately at $t=0$. |

## 5. Conclusion
The addition of temporal decay transforms the Trust Fusion engine from a static evaluator into a dynamic lifecycle manager.
1.  **Security**: It mitigates session hijacking risks by enforcing shorter windows of opportunity in risky environments.
2.  **Usability**: It naturally "upgrades" secure contexts with longer effective sessions compared to insecure ones.
This confirms that **Time** is a critical dimension of Zero Trust, equal in importance to Identity and Device Health.
