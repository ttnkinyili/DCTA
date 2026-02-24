# CHAPTER FOUR: Dynamic Trust Models for Enterprise Networks - Adapting to Change

The limitations of static access mapping—specifically the creation of large implicit trust windows—require the implementation of dynamic, stateful evaluation architectures. These architectures must continuously ingest telemetry signals and intelligently fuse them into a cohesive "Safety" metric that dictates access in real-time. This chapter outlines the mathematical mechanics of evidential fusion and the critical integration of temporal constraints in creating a resilient Zero Trust framework.

## 4.1 Evidential Fusion Frameworks

Operating in a heterogeneous networking environment guarantees that the Policy Decision Point (PDP) will receive conflicting telemetry. For instance, a user may present strong cryptographic identity credentials while simultaneously connecting from a highly volatile public network. The system must synthesize this contradictory evidence mathematically.

### 4.1.1 Cumulative Belief Fusion (The Additive Vulnerability)
In a purely cumulative framework, trust is additive. The engine calculates the total belief in a hypothesis (e.g., Safe) by simply summing the positive evidential masses ($m$) provided by each independent domain sensor (Identity ($i$), Device ($d$), Network ($n$), Data ($a$)). 

Mathematically, a naive cumulative trust score ($T_{cum}$) for a Safe state ($S$) can be represented as:
$$ T_{cum}(S) = \min\left(1.0, \sum_{k \in \{i,d,n,a\}} m_k(S) \right) $$

**The Vulnerability:** An attacker could orchestrate a breach by supplying extremely strong spoofed credentials (e.g., $m_i(S) = 0.99$) while suffering a total failure on the Device posture (e.g., $m_d(S) = 0.00$). If the system utilizes a cumulative threshold—for instance, requiring a total score of $T_{cum} > 0.80$ to grant access—the perfect identity score alone triggers authorization. The additive nature of the math eclipses the catastrophic failure of the device. This mathematical structure fails to implement the "weakest link" principles essential to modern cybersecurity and provides no mechanism for conflict resolution.

### 4.1.2 Average Belief Fusion (The Normalization Flaw)
A step forward from cumulative models, average systems normalize the total belief by the number of active sensors ($N$). This approach attempts to treat all domains equally and prevents a single perfect score from overwhelming the calculation.

Mathematically, the average trust score ($T_{avg}$) is represented as:
$$ T_{avg}(S) = \frac{1}{N} \sum_{k=1}^{N} m_k(S) $$

**The Vulnerability:** While mitigating the immediate additive vulnerability, averaging is equally dangerous in heterogeneous networks because it implies equal sensor validity. Consider a scenario where an employee logs in from a pristine corporate device ($m_d=0.95$) over a highly unstable and potentially hostile public Wi-Fi network ($m_n=0.30$). The simple mathematical average ($T_{avg} \approx 0.62$) might still grant them "Limited" or even full access depending on policy thresholds. Because the mathematical median acts as a smoothing function, simple averaging allows strong, pristine vectors to camouflage highly compromised attack vectors, pulling dangerous signals up into acceptable ranges.

### 4.1.3 Weighted Belief Fusion (Dynamic Contextualization)
To resolve the mathematical vulnerabilities inherent in both additive and averaging systems, a robust Zero Trust engine must employ **Dynamic Contextual Weighting** integrated alongside Dempster-Shafer (DS) Evidence Theory. In this framework, evidence is not simply combined; it is scaled algorithmically based on the *historical reliability* of the sensor providing it.

The core contribution of this model is the realization that *stability is a proxy for trust*. The engine assesses the historical variance ($\sigma^2$) of the incoming telemetry across each domain before calculating the final trust score. 

The raw weight ($W_{raw}$) for any domain $k$ is calculated inversely proportional to its variance, multiplied by a sensitivity parameter $\alpha$:
$$ W_{raw, k} = \frac{1}{1 + \alpha \cdot \sigma_k^2} $$

These raw weights are then normalized to ensure the total influence sums to 1.0 ($100\%$):
$$ W_{final, k} = \frac{W_{raw, k}}{\sum W_{raw}} $$

Finally, the dynamic weights are applied to the initial belief masses, significantly dampening the influence of erratic sensors:
$$ m'_{k}(\text{Safe}) = W_{final, k} \cdot m_{k}(\text{Safe}) $$

Under real-world conditions (such as a remote worker navigating cellular dead zones), minor telemetry fluctuations are inevitable. The engine mathematically measures this instability. If a domain returns chaotic, highly variant telemetry (e.g., $\sigma^2 = 0.25$), its normalized weight ($W_{final}$) is dynamically slashed to near-zero. 

The resulting normalized weights guarantee that the final DS fusion calculation relies heavily on stable, predictable inputs, decisively ignoring hostile or erratic data points. This creates **Behavioral Inertia**—a historical mathematical memory of the user's operational cadence. Instead of a single bad packet crashing the session, or a single average score hiding malware, Weighted Belief Fusion scientifically isolates uncertainty from truth.

## 4.2 The Integration of Temporal Dynamics

While spatial evidential fusion elegantly handles environmental noise, it cannot defeat an adversary who perfectly spoofs an established, trusted baseline. If an endpoint is completely compromised, it will broadcast a perfect "safe" signal indefinitely. Therefore, the architecture requires the integration of time.

*Trust is an ephemeral asset.* This research establishes the necessity of explicitly decaying the mathematical value of an authentication event the longer it persists without active re-verification.

### The Temporal Evolution of the Session
A standard Zero Trust session governed by temporal dynamics moves through distinct evolutionary phases:

1.  **Phase 1: Initialization ("The Skeptic Phase"):** At session conception ($t=0$), the system rejects historical inertia. The mathematical decay weight function ($W_{fresh}$) is at its absolute peak ($1.0$). The engine demands unassailable, immediate proof of identity and spatial posture; any anomaly results in immediate denial.
2.  **Phase 2: The Handover ("The Calibration Phase"):** As the session persists ($t > 5$), the reliance on raw immediate "freshness" begins to recede while the reliance on the user's established behavioral "inertia" grows. This equilibrium dampens oscillations; transient network jitter will not trigger a catastrophic lockout because the established history absorbs the impact.
3.  **Phase 3: Maturity & Lock-In ("The Partner Phase"):** Deep into the session window, trust is predominantly determined by accumulated history. As long as the entity does not exhibit a radical operational deviation (which would instantly spike variance and kill the session), productivity is seamlessly maintained. 

### Parameterizing Decay: Linear vs. Exponential
To operationally configure this decay, the engine provides two distinct mathematical frameworks tailored to specific enterprise risk profiles:

*   **Linear Temporal Decay:** This model linearly degrades the validity of the trust signal over a predetermined Time-To-Live (TTL). Parameterized for standard corporate environments (e.g., HR portals), the user is granted a mathematically predictable session length (e.g., aligned with a standard 8-hour shift or the NIST AAL2 30-minute inactivity threshold) before a hard re-authentication is mandated.
*   **Exponential Temporal Decay:** Employed for highly sensitive enclaves (e.g., production databases or classified systems), this model utilizes an aggressive decay parameter ($\lambda$). Trust values crash exponentially, forcing the evaluation engine into a state of continuous, paranoid suspicion. This mechanism serves as a mathematical kill-switch against persistent threats attempting to leverage established sessions; the attacker has virtually no temporal runway.

## 4.3 The Ensemble Trust Model

The culmination of these frameworks is the **Ensemble Trust Assessment Model**. This architecture hybridizes the instant, cryptographic verification of Spatial Fusion ("Freshness") with the mathematical momentum of historical tracking ("Inertia"), bound by a continuous temporal decay function.

By simultaneously evaluating the raw evidential data state alongside the speed of its degradation, the Ensemble model efficiently isolates complex threats. It mathematically proves that to subvert a fully parameterized Zero Trust Architecture, an adversary must not only intercept a valid identity token at the precise moment of inception but also perfectly replicate the victim's complex, historical behavioral baseline over an extended duration. This forces the adversary into a virtually impossible operational paradox.
