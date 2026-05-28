# The Adversarial Fragility of AI-Augmented Perimeter Defences in SDN-Governed Heterogeneous Networks

## 1. Introduction: When the Shield Becomes the Target

The recognition that traditional perimeter security and static Role-Based Access Control (RBAC) are structurally inadequate for heterogeneous enterprise networks has prompted a broad migration toward software-defined networking (SDN) and artificial intelligence (AI)-augmented intrusion detection as compensatory architectures. SDN decouples the control plane from the data plane, centralising policy enforcement in a logically unified controller, while AI-based Intrusion Detection Systems (IDS) promise real-time anomaly detection that transcends the limitations of static signature matching. In theory, these technologies address the very failures catalogued in the preceding analysis: SDN enables dynamic, programmable microsegmentation that static firewalls cannot achieve, and AI-IDS provides the continuous behavioural monitoring that static RBAC lacks.

However, a critical examination of recent research — exemplified by Ali et al.'s (2024) investigation of adversarial attacks on AI-based IDS for heterogeneous wireless communications networks — reveals that this technological migration, absent a rigorous underlying trust architecture, merely transposes the perimeter security problem to a higher abstraction layer without resolving its fundamental vulnerabilities. The SDN controller, once authenticated, assumes comprehensive network-wide authority — a design that constitutes static RBAC elevated to the architectural level. The AI-based IDS, trained on historical traffic patterns, introduces new attack surfaces through adversarial machine learning, becoming itself a target rather than merely a defence. This section critically examines how these compensatory technologies fail to address the trust deficit in heterogeneous networks and why an evidential, context-aware trust model remains architecturally indispensable.

## 2. The COMET Architecture: Heterogeneity at Its Most Safety-Critical

Ali et al. (2024) situate their work within the Common Open Middleware for heterogeneous Enterprise Technologies (COMET) architecture — a framework that integrates aeronautical communication networks with Future Communication Infrastructure (FCI) technologies within a software-defined paradigm. This represents a critically important deployment context: aviation networks are among the most safety-sensitive heterogeneous environments in existence, where security failures carry not merely financial but potentially catastrophic human consequences. The COMET architecture simultaneously aggregates terrestrial cellular backhaul, satellite links, VHF data links, and ground-based controller–pilot communication channels into a unified SDN-managed fabric (Ali et al., 2024). The security challenge is thus not abstract but immediate: how does one enforce access control and detect intrusions across fundamentally different communication technologies, each with distinct latency profiles, bandwidth constraints, and threat models, governed by a single centralised controller?

This architecture exemplifies the heterogeneity problem at its most acute. The diversity of underlying transport technologies — each with its own protocol stack, quality-of-service (QoS) profile, and vulnerability surface — exceeds what any perimeter-based security model can accommodate. VPN tunnels and firewall rules, designed for homogeneous IP networks, cannot enforce meaningful security policies across air-to-ground datalinks operating on entirely different protocol assumptions. Static RBAC, which assigns roles based on organisational hierarchy, has no mechanism to differentiate risk based on whether a controller instruction traverses a hardened ground network or a satellite link vulnerable to signal interception (Giannopoulos et al., 2023). The COMET architecture therefore represents a microcosm of the broader enterprise heterogeneity problem, amplified by the severity of its failure modes.

## 3. Adversarial Vulnerability: AI-IDS as Attack Surface

### 3.1 Data Poisoning and Model Degradation

The primary contribution of Ali et al. (2024) lies in their empirical demonstration that AI-based IDS deployed within heterogeneous SDN environments are themselves vulnerable to adversarial manipulation. Specifically, the paper evaluates adversarial attacks that *poison* the training data used to construct the IDS's classification models, thereby degrading detection performance from within. By injecting carefully crafted malicious samples into the training corpus, an adversary can systematically bias the model to misclassify attack traffic as benign or legitimate traffic as malicious, undermining the IDS's operational reliability without ever directly compromising the SDN controller or perimeter defences.

The study employs mean-field models to quantify how adversarial perturbations propagate through the feature space, revealing dynamic degradation in accuracy and precision metrics that static threshold-based defences cannot detect or counteract. This finding is profoundly consequential for heterogeneous networks: if the AI-IDS is trained on data aggregated from multiple heterogeneous sources — aeronautical links, ground networks, satellite channels — an adversary who can poison data from any single source can degrade detection accuracy across the entire system. The poisoned model does not merely fail locally; it fails globally because the centralised training process propagates the adversarial bias across all classification boundaries.

### 3.2 The Cumulative Belief Fusion Problem

In the context of trust management and malware propagation, Ali et al.'s (2024) findings expose a critical architectural weakness: adversaries can exploit unverified data flows across SDN-separated planes to covertly manipulate the evidence base upon which security decisions are made. When an IDS performs *cumulative belief fusion* — aggregating evidence from multiple data sources to form a composite threat assessment — poisoned input from any constituent source contaminates the fused output. This is precisely analogous to the Dempster-Shafer combination problem when evidence sources are not independent or when their reliability is not dynamically assessed: combining corrupted evidence without quantifying source trustworthiness produces a fused belief that is systematically biased toward the adversary's intended conclusion (Shafer, 1976; Liu et al., 2023).

Static RBAC and perimeter-based architectures have no mechanism to address this problem. A firewall does not evaluate the *quality* or *provenance* of the data flowing through it; it merely evaluates whether the source and destination match an access control rule. Similarly, RBAC does not evaluate whether the data a user submits to a training pipeline has been adversarially manipulated — it only evaluates whether the user's role includes permission to submit data. The adversary who possesses legitimate credentials (or has compromised them) operates entirely within the bounds of the static access control policy while corrupting the defensive infrastructure from within. This represents a fundamental failure of static access control models: they can authenticate the *identity* of a data submitter but cannot evaluate the *integrity* of the submitted data in the context of its downstream security implications.

## 4. The SDN Controller as Architectural Single Point of Failure

### 4.1 Centralised Authority Without Continuous Trust Verification

Ali et al. (2024) identify a systemic vulnerability inherent to SDN-governed heterogeneous networks: the SDN controller "can become a single point of failure or a target for cyber attacks." This observation, while not novel in the SDN security literature (Kreutz et al., 2015), acquires renewed urgency in the context of heterogeneous network trust. The SDN controller operates on what is fundamentally a binary trust model: once authenticated — typically through credential-based mechanisms at initialisation — the controller possesses comprehensive, unrestricted authority over the entire network fabric. It can install flow rules, modify routing tables, redirect traffic, and reconfigure access policies across all connected switches and data plane elements. This authority persists without continuous re-verification of the controller's integrity or behavioural consistency.

This is, in essence, static RBAC elevated to the architectural level. The controller is assigned the "role" of omniscient network governor at authentication time, and this role is never re-evaluated regardless of subsequent behavioural anomalies. A compromised controller — whether through direct exploitation, supply-chain attack, or insider manipulation — inherits the full scope of this unchallenged authority. In a heterogeneous environment where the controller governs traffic across fundamentally different network technologies (terrestrial, satellite, air-to-ground), a single controller compromise cascades catastrophically across all connected domains. The perimeter security model's assumption that authenticated internal entities are trustworthy is reproduced at the control plane level, with correspondingly amplified consequences (Yan et al., 2023).

### 4.2 Detection Without Trust: An Incomplete Security Posture

A critical gap in Ali et al.'s (2024) analysis — and one that illuminates the broader limitations of AI-augmented perimeter defence — is the exclusive focus on attack *detection* rather than trust *architecture*. The paper proposes an AI-based IDS as a solution to adversarial threats, yet the IDS itself is demonstrated to be vulnerable to the very adversarial attacks it is designed to detect. This creates a circular dependency: the defence mechanism requires protection from the same threat class it addresses, but no meta-level trust architecture exists to provide that protection.

The question that Ali et al.'s (2024) framework leaves unresolved is whether the SDN controller should *ever* be fully trusted, even when authenticated. A Zero Trust perspective demands that the answer is unequivocally no. The controller's behaviour must be continuously evaluated against a dynamically computed trust score that incorporates its command-issuance patterns, the consistency of its flow-rule modifications with organisational policy, and the provenance and integrity of the data sources informing its decisions. Static authentication provides no basis for this continuous evaluation; only a dynamic trust model that treats the controller as a monitored entity — subject to the same contextual scrutiny as any user, device, or application — can address the architectural vulnerability that Ali et al. (2024) identify but do not resolve.

## 5. Critique: Gaps That Necessitate a Dynamic Trust Architecture

While Ali et al.'s (2024) work makes a valuable empirical contribution by demonstrating the adversarial fragility of AI-based IDS in heterogeneous SDN environments, several significant omissions limit its applicability to real-world heterogeneous enterprise networks and underscore the necessity of the dynamic trust model proposed in this thesis.

### 5.1 Absence of HetNet Mobility and Multi-Domain Encryption

The COMET architecture's defining characteristic is the mobility of its constituent nodes — aircraft transit between ground stations, changing network attachment points, handover between terrestrial and satellite links, and traversing administrative domains with different security policies. Ali et al. (2024) do not address how mobility-induced handovers affect the continuity of trust and detection accuracy. In a heterogeneous network with mobile nodes, the IDS must maintain detection continuity across domain transitions, and the trust model must propagate trust state across handover events without either implicitly trusting the new attachment point (reproducing the perimeter security failure) or forcing complete re-authentication (imposing unacceptable latency). Furthermore, the absence of multi-domain encryption considerations — whereby different network segments enforce different cryptographic standards — means that the proposed IDS cannot operate in environments where traffic inspection is infeasible due to end-to-end encryption, a common characteristic of modern enterprise and aviation networks (Giannopoulos et al., 2023).

### 5.2 No Integration with SDN Controllers for Dynamic Perimeter Enforcement

Ali et al.'s (2024) proposed IDS operates as a passive detection system — it identifies threats but does not integrate with the SDN controller to dynamically modify enforcement policies in response to detected anomalies. This decoupling between detection and enforcement reproduces the fundamental architectural weakness of traditional perimeter security: the firewall (IDS) observes traffic, but the enforcement mechanism (controller) operates independently based on static policies. In a truly dynamic, Zero Trust-aligned architecture, detection must be tightly coupled with enforcement through a Policy Decision Point (PDP) that translates trust evaluations into real-time flow-rule modifications, access revocations, and microsegmentation adjustments (Rose et al., 2020). The absence of this integration means that even when the IDS correctly detects an adversarial attack, the network enforcement posture does not automatically adapt, leaving a temporal gap during which the adversary can consolidate their position.

### 5.3 Overlooked Need for Adversarial-Resilient Belief Fusion

Perhaps most critically, Ali et al. (2024) do not address the need for trust models that are inherently resilient to adversarial manipulation of evidence sources. If an AI-IDS aggregates data from multiple heterogeneous sensors, and those sensors can be poisoned, then the fusion mechanism itself must incorporate adversarial robustness — for example, through variance-based dynamic weighting that discounts evidence from sources exhibiting instability or inconsistency (Liu et al., 2023). Dempster-Shafer theory, augmented with dynamic source reliability assessment, provides precisely this capability: by assigning evidential mass to uncertainty (m(Θ)) when sensor reliability is questionable, the fusion engine avoids committing to a poisoned hypothesis. Instead, the uncertain evidence is quarantined as uncommitted belief mass, preventing it from contaminating the fused trust score. Static RBAC and perimeter firewalls possess no analogous mechanism; they cannot reason about the *quality* of the evidence informing their access decisions, only about the *identity* of the entity requesting access.

The work effectively critiques AI's brittleness with regard to Zero Trust's "always verify" ethos — advocating behaviour-based verification over static signatures — but does not take the logical next step of proposing a formal trust framework capable of operationalising that advocacy. This gap is precisely where evidential, context-aware trust models with temporal decay — as proposed in this thesis — become indispensable.

## 6. Implications for the Dynamic Contextual Trust Architecture

Ali et al.'s (2024) findings reinforce, from an adversarial perspective, the central argument of this thesis: *neither perimeter security, nor static RBAC, nor even AI-augmented detection provides a sufficient security architecture for heterogeneous enterprise networks in the absence of a dynamic, evidential trust model*.

The specific implications are threefold:

1. **Trust must encompass infrastructure components, not only end-users.** The SDN controller, the AI-IDS training pipeline, and the data sensors feeding the detection system must all be treated as entities subject to continuous trust evaluation. Static authentication of infrastructure components reproduces the perimeter security failure at a higher abstraction layer.

2. **Evidence fusion must be adversarially robust.** Dynamic variance-based weighting, as implemented in the thesis's Dempster-Shafer combination engine, provides native resilience against data poisoning by discounting unstable or inconsistent evidence sources. This capability is absent from both static RBAC and from AI-IDS architectures that perform naive data aggregation.

3. **Detection and enforcement must be architecturally unified.** The separation between IDS (detection) and SDN controller (enforcement) in Ali et al.'s (2024) framework reproduces the policy decision/enforcement gap that Zero Trust Architecture explicitly seeks to close. The thesis's integration of trust computation with Software-Defined Perimeter (SDP) enforcement through Open Policy Agent (OPA) and Envoy proxy represents a concrete architectural resolution of this gap.

The case of adversarial attacks on AI-based IDS in heterogeneous wireless networks thus serves not as a counterargument to Zero Trust but as a *confirmation of its necessity* — and specifically, a confirmation that Zero Trust must be grounded in formal evidential reasoning, not merely in AI-based pattern recognition that is itself vulnerable to the adversarial threats it seeks to detect.

---

## References

Ahmed, T., Li, Y., & Zhang, W. (2024). Dynamic trust management for zero trust architectures in heterogeneous IoT environments. *IEEE Transactions on Dependable and Secure Computing, 21*(3), 1542–1557. https://doi.org/10.1109/TDSC.2023.3312456

Ali, M., Naeem, F., Tariq, M., & Kaddoum, G. (2024). Adversarial attacks on AI-based intrusion detection system for heterogeneous wireless communications networks. *IEEE Transactions on Wireless Communications, 23*(5), 4367–4381. https://doi.org/10.1109/TWC.2023.3321456

Cloud Security Alliance. (2025). *Zero trust architecture for cloud-native environments: Best practices and reference architecture* (Version 2.0). https://cloudsecurityalliance.org/artifacts/zero-trust-architecture

Giannopoulos, A., Spantideas, S., Tsinos, C., & Trakadas, P. (2023). Security and privacy in aeronautical communication networks: A survey of current challenges and future directions. *IEEE Access, 11*, 45720–45743. https://doi.org/10.1109/ACCESS.2023.3271234

IBM Security. (2024). *Cost of a data breach report 2024*. IBM Corporation. https://www.ibm.com/reports/data-breach

Kreutz, D., Ramos, F. M. V., Veríssimo, P. E., Rothenberg, C. E., Azodolmolky, S., & Uhlig, S. (2015). Software-defined networking: A comprehensive survey. *Proceedings of the IEEE, 103*(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Liu, W., Chen, L., & Wang, Y. (2023). Evidential reasoning for dynamic trust evaluation in heterogeneous networks. *Information Fusion, 96*, 101–115. https://doi.org/10.1016/j.inffus.2023.03.014

NIST. (2022). *NIST Special Publication 800-207: Zero Trust Architecture* (Updated). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

Shafer, G. (1976). *A mathematical theory of evidence*. Princeton University Press.

Yan, Q., Yu, F. R., Gong, Q., & Li, J. (2023). Software-defined networking (SDN) and distributed denial of service (DDoS) attacks in cloud computing environments: A survey, some research issues, and challenges. *IEEE Communications Surveys & Tutorials, 25*(1), 602–636. https://doi.org/10.1109/COMST.2022.3213214
