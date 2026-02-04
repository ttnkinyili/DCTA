# Dynamic Trust Fusion in Heterogeneous Networks: A Contextual Analysis

## Abstract
This document presents a critical analysis of dynamic trust weighting and belief fusion across four cardinal domains: Network, Data, Device, and Application. By leveraging Dempster-Shafer theory, we demonstrate how contextual instability (variance) can dynamically discount evidence sources, thereby enhancing the robustness of access control decisions in Zero Trust environments.

## 1. Introduction
Traditional access control models (RBAC, ABAC) often rely on static policy evaluation. However, in heterogeneous environments—characterized by BYOD, edge computing, and remote work—trust is ephemeral. A static "trusted" device may become compromised within minutes. This necessitates a **Continuous Adaptive Risk and Trust Assessment (CARTA)** approach.

Our implementation models this through two key mechanisms:
1.  **Dynamic Contextual Weighting**: Using signal stability (variance) as a proxy for reliability.
2.  **Belief Fusion**: Using the Dempster-Shafer (DS) Theory of Evidence to mathematically combine conflicting or uncertain inputs.

## 2. Analysis of Domain Facets
The trust architecture relies on four independent axes of evidence. Independence is crucial for the efficacy of DS fusion.

### 2.1 Network Domain
*   **Context**: Represents the transport layer security (Zero Trust Network Access - ZTNA).
*   **Trust Indicators**: Geo-location, IP reputation, encryption strength, network segregation (geofencing).
*   **Scenario Impact**: A "Corporate Office" implies high network trust (0.95), whereas "Public Wi-Fi" (0.30) introduces high uncertainty.
*   **Dynamic Weighting**: Sudden latency spikes or routing changes (simulated as "Network Attack") increase variance. In our model, this variance drastically reduces the *weight* of the Network domain, effectively removing it from the consensus without policies explicitly failing.

### 2.2 Data Domain
*   **Context**: The sensitivity and classification of the resource being accessed.
*   **Trust Indicators**: DLP tags, classification levels (Confidential, Restricted), integrity checksums.
*   **Role in Fusion**: High data sensitivity (Trust Score ~0.90 for authorized access) demands higher aggregated belief for access. Low sensitivity allows for "Limited Access" even with lower overall trust.

### 2.3 Device Domain
*   **Context**: The health and identity of the endpoint.
*   **Trust Indicators**: MDM status, patch levels, EDR signals, jailbreak detection.
*   **Criticality**: In "BYOD" or "Untrusted Device" scenarios, this score drops (0.20 - 0.40). The fusion engine must decide if a secure Network and App can compensate for an insecure Device. Our simulation shows that with weighted fusion, a single low-trust domain (Device) generates significant *Uncertainty* mass, often preventing a "Full Access" decision unless other signals are overwhelmingly positive.

### 2.4 Application Domain
*   **Context**: The security posture of the requesting application.
*   **Trust Indicators**: App signature, vulnerability status, runtime integrity (RASP).
*   **Behavior**: An application behaving anomalously (high signal variance) would be discounted.

## 3. The Mechanics of Contextual Weighting

### 3.1 Variance as a Trust Discounter
We utilized a statistical approach to dynamic weighting:
$$ W_d = \frac{1}{1 + \alpha \cdot \sigma^2} $$
Where $W_d$ is the weight of domain $d$, and $\sigma^2$ is the variance of the trust signal over a sliding window window.

*   **Stable High Trust**: produces strong evidence ($m(\text{Safe}) \approx 1.0$).
*   **Stable Low Trust**: produces strong negative evidence ($m(\text{Unsafe}) \approx 1.0$).
*   **Unstable Signal**: High variance reduces $W_d \rightarrow 0$. In Dempster-Shafer terms, this converts the mass to **Uncertainty** ($m(\Theta)$).
    *   *Significance*: An oscillating sensor (e.g., a flickering firewall status) is not treated as "Bad" (which would block access via conflict), but as "Irrelevant" (Ignorance). This prevents false positives in denial.

## 4. Scenario Analysis & Decision Boundaries

We evaluated the model against six canonical scenarios. The Fusion Engine output determines the decision based on thresholds: Full Access ($Bel( Safe) \ge 0.75$), Limited ($Bel(Safe) \ge 0.45$), Deny ($< 0.45$).

| Scenario | Characteristics | Fusion Outcome | Discussion |
| :--- | :--- | :--- | :--- |
| **Corporate Office** | High scores across all domains. | **Full Access** | The "Happy Path". Convergence is rapid. |
| **Remote / VPN** | Network trust dips slightly (VPN is secure but over public internet). Device is high. | **Full Access** | Fusion robustness allows the high Device/Data trust to compensate for minor Network variance. |
| **Public Wi-Fi** | Network trust crashes (0.30). | **Limited Access** | The drop in Network trust adds significant *Uncertainty*. Typically results in Limited access unless Data sensitivity is very low. |
| **Untrusted Device / BYOD** | Device score is low (0.30 - 0.40). Network may be high (Geofenced). | **Limited/Full** | *Key Insight*: Our simulation showed that a High Network + High App can sometimes "carry" a low-trust device if the Data is not critical. However, for sensitive Data, the math prevents Full Access. |
| **Compromised** | Multiple domains show low scores or high variance. | **No Access** | The accumulation of evidence for "Unsafe" ($m(\text{Unsafe})$) dominates. |

## 5. Conclusion
The integration of Dynamic Contextual Weighting with Dempster-Shafer belief fusion provides a superior mechanism for Zero Trust Access Control compared to static Boolean logic. By mathematically distinguishing between "Known Bad" (Low Score, High Weight) and "Unknown/Unstable" (High Variance, Low Weight), the system achieves a nuanced "Gray Area" decision capability—essential for modern, heterogeneous network environments.
