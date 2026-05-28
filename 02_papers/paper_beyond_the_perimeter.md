# Beyond the Perimeter: Why Static RBAC, Software-Defined Perimeters, and AI-Augmented Detection Fail Without Dynamic Trust in Heterogeneous Networks

---

**Abstract.** Contemporary network security architectures — perimeter-based defences, static Role-Based Access Control (RBAC), NIST SP 800-207 Zero Trust Architecture, Cloud Security Alliance Software-Defined Perimeters (CSA SDP Specification v2.0 and Architecture Guide), and AI-augmented Intrusion Detection Systems (IDS) deployed within Software-Defined Networking (SDN) fabrics — are each presented as progressive solutions to the access control problem in heterogeneous enterprise networks. This paper demonstrates, through a unified critical analysis, that all five paradigms share a common structural failure: the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions. Perimeter security assumes a defensible boundary that no longer exists. Static RBAC treats authentication as a one-time gate, issuing temporal passports that adversaries exploit for lateral movement. NIST SP 800-207 mandates continuous trust evaluation but leaves the Trust Algorithm mathematically unspecified. CSA SDP excels at session establishment but provides no standardised post-authentication trust management. AI-augmented IDS in SDN environments introduces new adversarial attack surfaces — including data poisoning and cumulative belief fusion corruption — while the SDN controller reproduces static RBAC at the architectural level. The paper maps each failure to a unified diagnostic: the missing *dynamic trust imperative* — and positions the Dynamic Contextual Trust Architecture (DCTA) Ensemble Model, grounded in Dempster-Shafer evidential fusion with variance-based dynamic weighting and exponential temporal decay, as the architectural resolution that bridges the post-authentication trust management gap across all five paradigms.

**Keywords:** Zero Trust Architecture, dynamic trust, RBAC, Software-Defined Perimeter, NIST SP 800-207, AI-IDS, SDN, Dempster-Shafer theory, temporal decay, heterogeneous networks

---

## 1. Introduction: The Persistence of Implicit Trust

The foundational promise of modern cybersecurity — that identity has replaced the network perimeter as the primary security boundary — remains structurally unfulfilled across every dominant access control paradigm. Despite two decades of architectural evolution from castle-and-moat firewalls through role-based access control to software-defined perimeters and AI-augmented detection, a single vulnerability persists: the *implicit trust period* — a temporal window during which an authenticated entity retains access privileges without continuous re-verification of its trustworthiness.

This implicit trust period is not the residue of incomplete implementation. It is a *structural* property of architectures that treat trust as a binary, point-in-time determination rather than as a continuous, temporally depreciating, evidentially grounded quantity. A firewall that grants access to authenticated internal traffic implicitly trusts that traffic for the duration of the session. A static RBAC policy that validates role membership at login implicitly trusts that the authenticated role holder remains legitimate until session expiration. An SDP controller that issues a cryptographic entitlement after a rigorous multi-phase Join workflow implicitly trusts that entitlement until an explicit Leave event occurs. An AI-based IDS that classifies traffic as benign implicitly trusts that classification until the model is retrained. In each case, the security architecture performs rigorous verification at a discrete temporal boundary and then withdraws into passive monitoring or complete inattention for the interval that follows — an interval that adversaries are precisely optimised to exploit (IBM Security, 2024; Rose et al., 2020).

The consequences of this structural gap are empirically documented. The IBM Security (2024) *Cost of a Data Breach Report* identifies that the average time to identify and contain a breach remains 258 days in organisations relying on perimeter-centric and static access control architectures, with lateral movement within implicitly trusted zones accounting for the majority of the containment delay. The Cybersecurity and Infrastructure Security Agency (CISA, 2024) reports that exploitation of VPN appliance vulnerabilities — which inherit the authenticated user's full network visibility — constitutes one of the most frequently exploited initial access vectors in advanced persistent threat campaigns. These are not implementation failures; they are architectural consequences of systems that grant temporal passports at authentication boundaries and then lack the mathematical apparatus to depreciate, re-evaluate, or revoke those passports in response to post-authentication contextual changes.

This paper presents a unified critical analysis demonstrating that five ostensibly progressive security paradigms — perimeter defence, static RBAC, NIST SP 800-207, CSA SDP, and AI-augmented IDS in SDN — all converge on the same structural failure. The analysis is not merely diagnostic; it is constructive. Each paradigm's failure is mapped to a specific absence in its trust evaluation architecture, and the Dynamic Contextual Trust Architecture (DCTA) Ensemble Trust Model (ETM) — integrating Dempster-Shafer evidential fusion, variance-based dynamic weighting, and exponential temporal decay — is positioned as the architectural bridge that transforms point-in-time authentication assurance into continuous, self-calibrating, uncertainty-aware trust evaluation.

The contributions of this paper are threefold:

1. **Unified diagnostic analysis**: A structured demonstration that five distinct security paradigms — spanning three decades of architectural evolution — share a single, common structural failure: the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions.
2. **Failure-to-capability mapping**: A systematic mapping of each paradigm's specific vulnerability to the precise missing capability (Table 1), establishing the requirements that any resolution must satisfy.
3. **Architectural resolution**: Positioning of the DCTA Ensemble Trust Model as the constructive resolution that bridges the identified gaps, with formal property analysis demonstrating its mathematical fitness for purpose.

The remainder of this paper is organised as follows. Section 2 analyses the dissolution of the network perimeter. Section 3 examines the structural inadequacy of static RBAC. Sections 4 and 5 critique NIST SP 800-207 and CSA SDP respectively. Section 6 exposes the adversarial fragility of AI-augmented IDS in SDN. Section 7 synthesises the common thread across all five paradigms and presents the DCTA as the architectural resolution. Section 8 concludes.

---

## 2. The Dissolution of the Perimeter

### 2.1 Topological Obsolescence

The foundational premise of perimeter-based security — that a clearly delineated boundary exists between a trusted internal network and an untrusted external environment — has been rendered architecturally obsolete by the heterogeneity of modern enterprise infrastructures. Contemporary enterprises operate across a continuum of on-premises data centres, multi-cloud platforms (AWS, Azure, GCP), edge computing nodes, and a proliferation of unmanaged endpoints introduced by Bring Your Own Device (BYOD) and Internet of Things (IoT) policies (Stafford, 2023; NIST, 2020). Network traffic no longer flows through a single defensible chokepoint; it traverses hybrid topologies where users, applications, and data reside in distributed trust domains with fundamentally different security postures (Buck et al., 2022).

The heterogeneity is not merely topological but *protocological*. Modern enterprise networks integrate devices operating on disparate communication protocols — Zigbee, BLE, and MQTT for IoT; HTTP/2 and gRPC for cloud-native microservices; legacy SNMP for infrastructure management — and across fundamentally different architectural paradigms, including on-premises virtualisation, containerised cloud workloads, and edge computing nodes. Wang et al. (2022) argue that this heterogeneity of architectures, networking technologies, and protocols makes it "extremely difficult to evaluate, transfer, and maintain trust among different devices, protocols, architectures, and network operators." Perimeter security cannot enforce protocol-level inspection across this diversity, and no firewall rule can meaningfully differentiate risk based on the protocol or architectural context of an access request when that request traverses a satellite link, a 5G cellular backhaul, and a ground-based corporate LAN in sequence.

Furthermore, modern enterprise topologies are not static: containers are spun up and destroyed in seconds, serverless functions execute transiently, and edge devices connect and disconnect unpredictably (Cloud Security Alliance, 2025). A firewall rule configured for a container that existed five minutes ago is meaningless for the replacement container running the same microservice with a different IP address and potentially different security posture. The attack surface of heterogeneous networks is exponentially larger than that of homogeneous, perimeter-bounded environments, and perimeter security treats this interior heterogeneity as a trusted monolith — providing no mechanism to distinguish between a fully patched, enterprise-managed workstation and a compromised IoT sensor operating on the same network segment (Ahmed et al., 2024).

### 2.2 VPN Credential Inheritance and Lateral Movement

Firewalls and Virtual Private Networks (VPNs), the historic cornerstones of perimeter defence, were designed to gate access at a well-defined boundary. However, VPNs extend broad network-level access to authenticated users without continuous verification of their post-authentication behaviour, effectively creating authenticated tunnels of implicit trust (Mehraj & Banday, 2022). Once a VPN session is established, an adversary who has compromised a single credential or exploited a VPN vulnerability inherits that user's full network visibility, enabling unimpeded lateral movement across enterprise segments.

This is not a theoretical concern. Recent high-profile breaches, including the exploitation of zero-day vulnerabilities in VPN appliances documented by CISA (2024), confirm that perimeter-centric architectures routinely fail to contain advanced persistent threats (APTs) that begin at the network edge and propagate inward. IBM Security (2024) reports that organisations relying on perimeter-centric architectures experience significantly higher breach containment times precisely because lateral movement occurs within the "trusted" zone where monitoring is sparse and access controls are permissive. Modern adversaries do not "break in" through the perimeter so much as "log in" using stolen credentials or compromised endpoints, and then move laterally through a flat, implicitly trusted interior.

The convergence of perimeter dissolution, protocological heterogeneity, and VPN credential inheritance establishes the first dimension of the structural failure: **perimeter security assumes a boundary that no longer exists, and its authentication model grants temporal passports that persist without depreciation**.

---

## 3. Static RBAC: Structural Inadequacy in Heterogeneous Environments

### 3.1 Role Explosion

Static Role-Based Access Control (RBAC), which assigns permissions to predefined organisational roles rather than to individual users, was originally conceived for relatively stable enterprise environments with predictable workforce structures and well-defined application boundaries (Sandhu et al., 1996). While RBAC simplified administrative overhead by abstracting individual permissions into role hierarchies, its static nature introduces critical vulnerabilities in the dynamic, heterogeneous networks that characterise modern enterprises.

The first structural failure is *role explosion* — the combinatorial growth in the number of roles required to represent the fine-grained access patterns of a heterogeneous environment (Habib et al., 2022). In enterprises where users operate across multiple business units, access diverse cloud services, and interact with context-dependent resources — for example, a clinician accessing patient records from a hospital workstation versus a personal tablet on public Wi-Fi — the number of distinct role definitions required to capture every legitimate access pattern grows unmanageably. Habib et al. (2022) demonstrate that in IoT-integrated enterprise environments, the frequency with which devices are added, reconfigured, or decommissioned renders static role assignments perpetually stale, creating either over-privileged roles that violate least privilege or under-privileged roles that impede operational workflows.

### 3.2 Context-Blindness: Same Role, Different Risk

Beyond administrative rigidity, static RBAC is inherently *stateless* with respect to context and time. A user assigned the role of "Database Administrator" retains identical permissions whether they are connecting from an enterprise-hardened workstation on the corporate LAN at 10:00 AM or from an unmanaged personal device on a public Wi-Fi network at 02:00 AM. The access control system possesses no mechanism to evaluate the risk differential between these two contexts because static RBAC evaluates *who the user is* — their role — not *what the user is doing, from where, on what device, and at what time* (Al-Sanjary et al., 2023). This contextual blindness constitutes a critical vulnerability: a compromised credential operating under a high-privilege role can exfiltrate data undetected because the RBAC system has no behavioural baseline against which to detect anomalous access patterns.

### 3.3 The Temporal Passport Problem

The most consequential failure of static RBAC is its treatment of authentication as a discrete, one-time gate. Once a user authenticates and their role is validated, access persists for the session duration without re-evaluation. Alsubhi et al. (2024) empirically demonstrate that static scoring models fail to trigger re-evaluation even when a device's security posture degrades mid-session, effectively granting a "temporal passport" that adversaries exploit for low-and-slow data exfiltration campaigns.

This temporal blindness directly contradicts the Zero Trust principle of "never trust, always verify," which requires continuous authentication and authorisation throughout the lifetime of every session (Rose et al., 2020). In heterogeneous environments where device posture, network conditions, and user behaviour are inherently volatile, this "authenticate once, access forever" model creates a window of implicit trust — the very construct that Zero Trust Architecture exists to eliminate (Alder, 2025). The inability of RBAC to revoke or constrain access dynamically in response to real-time risk signals means that session hijacking, credential theft, and insider threats all benefit from an extended operational runway.

A further dimension of this failure concerns computational asymmetry: enterprise networks increasingly incorporate resource-constrained devices — IoT sensors, embedded controllers, and edge gateways — whose limited processing power, memory, and energy budgets cannot sustain the overhead of complex centralised access control lookups (Sharma et al., 2023). Static RBAC, designed for server-class infrastructure, imposes uniform authorisation queries regardless of the requesting device's computational capacity, resulting in either bypassed security checks or operational degradation (Alqassem et al., 2025).

The convergence of role explosion, context-blindness, and temporal passports establishes the second dimension of the structural failure: **static RBAC assumes a workforce, device population, and application landscape that does not change within the lifetime of a session — an assumption that heterogeneous enterprise networks violate continuously and at scale**.

---

## 4. Critique of NIST SP 800-207: The Unspecified Trust Algorithm

### 4.1 Section 3 — Logical Components: PE/PA/PEP Gaps

NIST Special Publication 800-207 remains the definitive federal framework establishing Zero Trust Architecture. Its tripartite logical architecture — Policy Engine (PE), Policy Administrator (PA), and Policy Enforcement Point (PEP) — is architecturally elegant and has profoundly influenced both academic discourse and commercial implementations (Rose et al., 2020). The PE consumes contextual telemetry from identity stores, device posture databases, threat intelligence feeds, and behavioural analytics platforms to produce access determinations. The PA translates these into actionable instructions, and the PEP enforces them at the resource boundary.

However, a critical assessment reveals the most consequential limitation: the *deliberate abstraction of the Trust Algorithm* that operates within the PE. NIST SP 800-207 explicitly acknowledges that the Trust Algorithm processes input variables — identity assurance, device posture compliance, behavioural signals, resource sensitivity, and threat intelligence — to produce access decisions, yet provides no normative guidance on the mathematical form of this algorithm (Rose et al., 2020). The framework specifies neither the weighting scheme by which disparate input variables are synthesised, nor the temporal dynamics by which evidence is discounted, nor the decision-theoretic framework by which uncertainty is handled. This architectural agnosticism was intentional — NIST sought to provide a framework, not a prescription — but it creates a critical implementation vacuum. In practice, security architects confronted with this vacuum default to either simplistic linear scoring models that assign fixed weights to each input variable, or to vendor-specific proprietary algorithms whose decision logic is opaque, unverifiable, and non-portable (Xu, 2024; Shin et al., 2025).

The second structural concern relates to the *centralisation assumption* implicit in the PE–PA–PEP triad. While distributed deployment is permitted, the logical model describes a single authoritative decision point. In heterogeneous enterprise networks, the centralised PE becomes a performance bottleneck — empirical evaluations demonstrate latencies of 50–200 milliseconds per decision cycle in large-scale deployments (Oqaily et al., 2024) — and a single point of failure whose unavailability reduces the enterprise to either a fail-open state (violating Zero Trust) or a fail-closed state (halting operations). The framework's failure to mandate distributed PE architectures with consensus mechanisms represents a significant gap for heterogeneous deployments.

Furthermore, none of NIST's four deployment model variations — Device Agent/Gateway, Enclave-Based, Resource Portal, and Device Application Sandboxing — adequately addresses the computational asymmetry that characterises heterogeneous networks. The Device Agent/Gateway model requires endpoint-hosted agents incompatible with BYOD and IoT devices (Alawida et al., 2024). The Device Application Sandboxing model assumes computational capacity unavailable on constrained devices (Sharma et al., 2023). The absence of heterogeneity-aware deployment guidance is a structural gap.

### 4.2 Section 4 — Deployment Scenarios: Underspecified Heterogeneous Guidance

Section 4 maps the abstract architecture to concrete scenarios: remote employees, multi-cloud environments, non-employee access, and BYOD devices. Each scenario illustrates PE–PA–PEP configuration for a specific topology, but all share a critical limitation: *temporal stationarity*.

The remote employee scenario assumes a static access pattern — a worker connected to a defined set of resources from a single device and location. It does not address the increasingly prevalent pattern of *mobile, multi-device, multi-network access* — a worker who transitions from corporate laptop on home network, to mobile device on cellular network, to shared workstation at a co-working space. Each transition fundamentally changes device posture, network context, and application context, yet the framework provides no guidance on how the Trust Algorithm should handle mid-session contextual shifts without either terminating the session or implicitly trusting the new context (Buck et al., 2022).

The multi-cloud scenario underestimates the complexity of trust signal federation across heterogeneous cloud environments, where each provider exposes different identity federation standards, device attestation capabilities, and network telemetry formats. The framework provides no normative guidance on normalising, correlating, and weighting trust signals from fundamentally different observability infrastructures (Al-Mutairi & Hassan, 2024).

The BYOD scenario raises the most acute trust evaluation challenges. Unmanaged devices lack enterprise agents, may not support device attestation, and cannot be assumed to comply with endpoint security policies (Habib et al., 2022). The framework's reliance on device agent telemetry as a trust input is structurally weakened, creating a "trust signal gap" where the PE must make access decisions with incomplete or absent device posture information.

### 4.3 Section 5 — Threats: Acknowledged but Unmitigated Temporal Vulnerabilities

Section 5 catalogues threats uniquely associated with ZTA deployments and represents a commendably honest self-assessment. The most architecturally consequential threat identified is the *subversion of the ZTA decision process* — a compromised PE that silently modifies access policies, rendering the entire apparatus complicit in an attack. NIST warns that "any enterprise administrator who can configure the PE rules can perform or approve changes to policy in an undetected way" (Rose et al., 2020, p. 30), but provides no self-monitoring mechanism for the PE itself.

The *denial of service against PE/PA components* threat is particularly acute: because all access decisions flow through the PE–PA pipeline, its unavailability paralyses the entire infrastructure. NIST recommends "properly secured" or "replicated" deployment but falls short of an architectural mandate for graceful degradation.

The *stolen credentials and insider exploitation* threat assumes that the Trust Algorithm can distinguish between legitimate and illegitimate use of valid credentials — a capability requiring multi-dimensional behavioural analysis that the framework describes conceptually but does not specify algorithmically (Chen & Wang, 2025). The *network visibility* threat acknowledges that encrypted traffic creates inspection gaps that are amplified in heterogeneous environments with fragmented encryption standards (Giannopoulos et al., 2023).

In aggregate, NIST SP 800-207 establishes the third dimension of the structural failure: **the framework mandates continuous trust evaluation but leaves the mathematical apparatus — the weighting, temporal dynamics, uncertainty handling, and fusion logic — entirely unspecified, creating an implementation vacuum that defaults to the deterministic, context-blind scoring it was designed to replace**.

---

## 5. Critique of the CSA Software-Defined Perimeter

### 5.1 SDP Specification v2.0: Cryptographic Rigour, Post-Authentication Silence

The Cloud Security Alliance's SDP Specification v2.0 represents the most technically prescriptive articulation of Zero Trust Network Access at the protocol level. Where NIST operates at the architectural abstraction layer, SDP descends to the packet level, mandating exact cryptographic handshake sequences and protocol state machines (Cloud Security Alliance, 2022).

The centrepiece is the enhanced Single Packet Authorization (SPA) protocol, which implements the "authenticate before connect" paradigm: the SDP Controller maintains all service ports in a default-closed state, rendering protected infrastructure invisible to network scanning, and opens a transient, individualised data path only upon cryptographic validation of a correctly formed SPA packet. The v2.0 enhancements — cryptographic nonces against replay attacks, timestamp validation for temporal freshness, and HMAC for payload integrity — address the most commonly cited vulnerabilities in older SPA implementations (Moubayed et al., 2022).

#### 5.1.1 The SPA Replay Window

Despite these enhancements, a rigorous evaluation reveals structural limitations. SPA is, by its architectural nature, a *point-in-time authentication mechanism*. The SPA packet demonstrates that the Initiating Host possessed valid credentials and a compliant device posture at the precise moment the packet was generated. It provides no assurance about the entity's state at any subsequent point. Once the SPA handshake succeeds and the encrypted tunnel is established, the specification provides no protocol-level mechanism for continuous re-evaluation during the active session. This creates precisely the implicit trust period that Zero Trust is designed to eliminate — a window of variable and potentially unbounded duration during which a compromised endpoint operates under the authority of an increasingly stale authentication signal (Rose et al., 2020). The specification delegates post-authentication trust management to "continuous monitoring" mechanisms that are referenced but neither specified nor standardised.

#### 5.1.2 The mTLS Certificate Lifecycle Problem

The v2.0 mandate of Mutual TLS (mTLS) for all intra-SDP communications elevates cryptographic assurance to bidirectional identity verification. However, the mTLS mandate introduces a *certificate lifecycle management complexity* that the specification acknowledges but does not resolve. In heterogeneous networks with thousands of Initiating Hosts — managed workstations, mobile devices, BYOD endpoints, IoT sensors, ephemeral cloud instances — each device requires a unique X.509 certificate issued by a trusted Certificate Authority, stored securely, and rotated before expiration. Certificate mismanagement — expired certificates, improperly stored private keys, revocation list propagation delays — represents a significant operational risk (Zanasi et al., 2023). The specification's silence on recommended PKI architectures and fallback authentication mechanisms creates an implementation gap identified as a primary barrier to SDP adoption (Kumar & Patel, 2023).

#### 5.1.3 IoT Computational Overhead

The v2.0 SPA message requires the Initiating Host to generate cryptographic nonces, compute HMAC digests, and in some configurations perform asymmetric key operations — all within the strict temporal window for timestamp validity. For resource-constrained IoT devices — industrial sensors, medical telemetry devices, smart building actuators — these cryptographic operations may exceed the device's computational budget or introduce authentication latencies conflicting with real-time operational requirements (Sharma et al., 2023). The specification provides no lightweight SPA variant for constrained devices, no delegation mechanism for gateway-mediated SPA on behalf of downstream devices, and no guidance on maintaining security guarantees when the full SPA handshake is computationally infeasible.

### 5.2 SDP Architecture Guide: Operational Workflows and Structural Limitations

#### 5.2.1 Controller Centralisation

The Architecture Guide treats the Controller as a logically centralised, architecturally singular component (Cloud Security Alliance, 2024). While operational deployments may replicate the Controller for high availability, the logical model describes a single policy authority. This centralisation creates two architectural risks: the Controller becomes a high-value target for adversarial compromise — a compromised Controller can silently issue entitlements to adversary-controlled devices (analogous to NIST SP 800-207's PE subversion threat) — and the Controller becomes a single point of failure whose unavailability paralyses the entire infrastructure (Alawida et al., 2024). The Architecture Guide recommends geographically distributed replicas but specifies no consensus protocol for distributed Controller coordination — a gap particularly acute for globally distributed operations.

#### 5.2.2 Binary Trust: The Join/Leave Cliff-Edge

The Architecture Guide's trust model remains fundamentally binary. Upon successful completion of the Join process, the Initiating Host is either fully trusted (receiving the cryptographic entitlement for complete resource access) or fully untrusted (receiving nothing). There is no intermediate state — no mechanism for granting constrained, read-only, or monitored access to entities whose trustworthiness is ambiguous or degraded but not categorically insufficient. This binary model creates a cliff-edge access decision: a device meeting 95% of posture requirements but failing a single check is treated identically to a device failing every check — both receive zero access. In practice, this cliff-edge behaviour drives security administrators to relax posture requirements to avoid excessive denials, inadvertently undermining the security assurance the multi-phase verification was designed to provide (Buck et al., 2022).

#### 5.2.3 The Thundering Herd Problem

The Join process's sequential, blocking nature — where each verification phase must complete before the next begins, and any failure terminates the entire process — creates a "thundering herd" problem in high-throughput environments. At the start of a business day, during a failover event, or following a network partition recovery, thousands of simultaneous Join requests exceed the Controller's processing capacity, producing escalating latencies and potential timeouts that deny access to legitimate devices (Smith, 2024). The Architecture Guide acknowledges this scalability concern but provides no formal specification of load-balancing, request-routing, or priority-queuing mechanisms.

### 5.3 The Post-Authentication Trust Management Gap

The preceding critiques of both the Specification and Architecture Guide converge on a single, architecturally fundamental observation: **the SDP framework excels at session establishment but provides no standardised, mathematically specified mechanism for managing trust during an established session**.

A session established through rigorous SPA and mTLS at time $t = 0$ remains fully authorised at $t = 30$ minutes, at $t = 2$ hours, and at $t = 24$ hours, unless an explicit revocation event terminates it. During this period, the initial authentication signal — highly reliable at $t = 0$ — progressively loses its evidentiary weight without any corresponding reduction in the access privileges it underwrites. This temporal blindness creates the implicit trust period that adversaries exploit: a session hijack or device compromise occurring after the SPA handshake but before the next posture check operates with the full authority of the original authentication (Chen et al., 2025).

The SDP framework's reactive revocation model — terminating sessions upon detection of posture degradation — partially mitigates this risk but suffers from fundamental detection latency. The interval between a posture degradation event and its detection by the SDP Client or Controller constitutes a "detection gap" during which the compromised session retains full access. Empirical studies suggest that the mean time to detect a sophisticated compromised session ranges from 7 minutes for well-instrumented networks to several hours for environments with limited observability (IBM Security, 2024).

The SDP framework thus establishes the fourth dimension of the structural failure: **cryptographic session establishment rigour combined with post-authentication trust management silence creates an architecture that is maximally secure at the moment of authentication and progressively less secure with every passing second**.

---

## 6. Adversarial Fragility of AI-Augmented IDS in SDN-Governed Heterogeneous Networks

### 6.1 The Compensatory Migration and Its False Promise

The recognition that perimeter security and static RBAC are structurally inadequate has prompted a broad migration toward software-defined networking (SDN) and AI-augmented intrusion detection as compensatory architectures. SDN decouples the control plane from the data plane, centralising policy enforcement in a logically unified controller, while AI-based IDS promises real-time anomaly detection transcending static signature matching (Ali et al., 2024). In theory, these technologies address the catalogued failures: SDN enables dynamic, programmable microsegmentation that static firewalls cannot achieve, and AI-IDS provides the continuous behavioural monitoring that static RBAC lacks.

However, absent a rigorous underlying trust architecture, this technological migration merely transposes the perimeter security problem to a higher abstraction layer without resolving its fundamental vulnerabilities. Ali et al.'s (2024) investigation of adversarial attacks on AI-based IDS for heterogeneous wireless communications networks — situated within the COMET (Common Open Middleware for heterogeneous Enterprise Technologies) architecture integrating aeronautical communication with Future Communication Infrastructure technologies — reveals that the compensatory migration introduces *new* attack surfaces while leaving the original trust deficit unaddressed.

### 6.2 Data Poisoning and Cumulative Belief Fusion Corruption

Ali et al. (2024) empirically demonstrate that AI-based IDS deployed within heterogeneous SDN environments are themselves vulnerable to adversarial manipulation through *data poisoning*. By injecting carefully crafted malicious samples into the training corpus, an adversary can systematically bias the classification model to misclassify attack traffic as benign or legitimate traffic as malicious, undermining operational reliability without directly compromising the SDN controller or perimeter defences.

The study employs mean-field models to quantify how adversarial perturbations propagate through the feature space, revealing dynamic degradation in accuracy and precision that static threshold-based defences cannot detect or counteract. This finding is profoundly consequential for heterogeneous networks: if the AI-IDS is trained on data aggregated from multiple heterogeneous sources, an adversary who can poison data from any single source degrades detection accuracy across the entire system. The poisoned model does not fail locally; it fails *globally* because the centralised training process propagates adversarial bias across all classification boundaries.

In the context of trust management, these findings expose a critical architectural weakness: adversaries can exploit unverified data flows across SDN-separated planes to covertly manipulate the evidence base upon which security decisions are made. When an IDS performs *cumulative belief fusion* — aggregating evidence from multiple sources to form composite threat assessments — poisoned input from any constituent source contaminates the fused output. This is precisely analogous to the Dempster-Shafer combination problem when evidence sources are not independent or when their reliability is not dynamically assessed: combining corrupted evidence without quantifying source trustworthiness produces fused belief that is systematically biased toward the adversary's intended conclusion (Shafer, 1976; Liu et al., 2023).

Static RBAC and perimeter-based architectures possess no mechanism to address this problem. A firewall does not evaluate the *quality* or *provenance* of data flowing through it — it merely evaluates whether source and destination match an access control rule. RBAC does not evaluate whether data submitted to a training pipeline has been adversarially manipulated — it only evaluates whether the user's role includes permission to submit data. The adversary possessing legitimate credentials operates entirely within the bounds of the static access control policy while corrupting defensive infrastructure from within.

### 6.3 The SDN Controller as Static RBAC at Scale

Ali et al. (2024) identify a systemic vulnerability: the SDN controller "can become a single point of failure or a target for cyber attacks." The SDN controller operates on what is fundamentally a binary trust model: once authenticated through credential-based mechanisms at initialisation, the controller possesses comprehensive, unrestricted authority over the entire network fabric — installing flow rules, modifying routing tables, redirecting traffic, and reconfiguring access policies across all connected switches. This authority persists without continuous re-verification of the controller's integrity or behavioural consistency (Yan et al., 2023).

This is *static RBAC elevated to the architectural level*. The controller is assigned the "role" of omniscient network governor at authentication time, and this role is never re-evaluated regardless of subsequent behavioural anomalies. A compromised controller inherits the full scope of this unchallenged authority. In a heterogeneous environment where the controller governs traffic across fundamentally different network technologies (terrestrial, satellite, air-to-ground in the COMET architecture), a single controller compromise cascades catastrophically across all connected domains. The perimeter security model's assumption that authenticated internal entities are trustworthy is reproduced at the control plane level, with correspondingly amplified consequences (Kreutz et al., 2015).

### 6.4 Detection Without Enforcement: The Incomplete Security Posture

A critical gap in Ali et al.'s (2024) analysis — and one that illuminates the broader limitations of AI-augmented perimeter defence — is the exclusive focus on attack *detection* rather than trust *architecture*. The proposed AI-based IDS operates as a passive detection system: it identifies threats but does not integrate with the SDN controller to dynamically modify enforcement policies in response. This decoupling between detection and enforcement reproduces the fundamental weakness of traditional perimeter security: the firewall (IDS) observes traffic, but the enforcement mechanism (controller) operates independently based on static policies.

In a genuinely dynamic architecture, detection must be tightly coupled with enforcement through a Policy Decision Point that translates trust evaluations into real-time flow-rule modifications, access revocations, and microsegmentation adjustments (Rose et al., 2020). The absence of this integration means that even when the IDS correctly detects an adversarial attack, the network enforcement posture does not automatically adapt, leaving a temporal gap during which the adversary can consolidate their position.

Furthermore, the AI-IDS itself is demonstrated to be vulnerable to the very adversarial attacks it is designed to detect. This creates a circular dependency: the defence mechanism requires protection from the same threat class it addresses, but no meta-level trust architecture exists to provide that protection. The question that the framework leaves unresolved is whether the SDN controller should *ever* be fully trusted, even when authenticated. A Zero Trust perspective demands that the answer is unequivocally no.

The AI-IDS paradigm thus establishes the fifth dimension of the structural failure: **detection without trust-grounded enforcement, combined with adversarial vulnerability of the detection mechanism itself, creates a security architecture that is simultaneously incomplete and self-undermining**.

---

## 7. The Common Thread: The Dynamic Trust Imperative

### 7.1 Mapping Each Failure to the Missing Continuous Trust Evaluation

The five paradigms analysed in Sections 2–6, despite their apparent architectural diversity, converge on a single structural failure. Table 1 maps each paradigm's specific vulnerability to the missing capability.

**Table 1.** Structural failure mapping across five security paradigms.

| Paradigm | Specific Vulnerability | Missing Capability |
|:---|:---|:---|
| **Perimeter Security** | VPN credential inheritance; flat trust interior; lateral movement | Continuous post-authentication verification; trust depreciation |
| **Static RBAC** | Role explosion; context-blindness; temporal passport | Context-aware, temporally dynamic access evaluation |
| **NIST SP 800-207** | Unspecified Trust Algorithm; centralised PE; temporal stationarity in deployment scenarios | Mathematically specified weighting, fusion, and decay logic |
| **CSA SDP** | Point-in-time SPA; binary Join/Leave trust; post-authentication silence; IoT overhead | Graduated, continuous trust scoring; lightweight evaluation |
| **AI-IDS in SDN** | Data poisoning; belief fusion corruption; static-RBAC controller; detection-enforcement gap | Adversarially robust evidence fusion; trust-aware enforcement |

The common thread is unambiguous: **the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions**. Each paradigm performs its respective authentication, verification, or detection function competently at a discrete temporal boundary — perimeter crossing, role validation, SPA handshake, model classification — and then either withdraws entirely or delegates post-boundary trust management to unspecified, ad hoc mechanisms that lack mathematical rigour, uncertainty awareness, or temporal dynamics.

### 7.2 The DCTA Ensemble Model as Architectural Bridge

The Dynamic Contextual Trust Architecture (DCTA) Ensemble Model is designed to bridge precisely this structural gap. Its architecture addresses each dimension of the failure through four interlocking mechanisms:

#### 7.2.1 Multi-Domain Evidential Fusion via Dempster-Shafer Theory

The DCTA evaluates trust across four independent telemetry domains — Identity, Device, Network, and Application/Data — each producing its own basic probability assignment (BPA) over the binary frame of discernment $\Theta = \{Safe, Unsafe\}$. The Dempster-Shafer combination rule fuses evidence conjunctively, requiring concordant evidence across sources to produce high committed belief:

$$
m_{1,2}(A) = \frac{1}{1-\kappa} \sum_{\substack{B \cap C = A \\ B, C \subseteq \Theta}} m_1(B) \cdot m_2(C), \quad A \neq \emptyset
$$

where $\kappa = \sum_{B \cap C = \emptyset} m_1(B) \cdot m_2(C)$ is the inter-source conflict. This conjunctive property ensures that no single domain's favourable assessment can override genuine risk signals from another domain — a mathematically enforceable implementation of the separation of privilege principle (Saltzer & Schroeder, 1975) that operates continuously rather than only at session establishment.

Critically, the DS framework's explicit representation of epistemic uncertainty through $m(\Theta)$ — mass assigned to the full frame of discernment — provides the mathematical apparatus absent from all five paradigms. When evidence is insufficient to commit belief to either the Safe or Unsafe hypothesis, the framework does not default to a binary grant or denial but instead expresses "insufficient evidence to decide" — routing the entity into a constrained access tier proportionate to the degree of uncertainty. This addresses:

- **RBAC's context-blindness**: by evaluating multi-dimensional context rather than static role membership.
- **NIST's unspecified Trust Algorithm**: by providing the mathematically specified fusion logic.
- **SDP's binary trust**: by replacing cliff-edge Join/Leave with graduated trust thresholds.
- **AI-IDS's belief fusion corruption**: by incorporating source reliability assessment through variance-based weighting.

#### 7.2.2 Variance-Based Dynamic Weighting

The DCTA computes each domain's evidential authority through a variance-driven weighting function:

$$
W_{\text{raw},k} = \frac{1}{1 + \alpha \cdot \sigma_k^2}
$$

where $\sigma_k^2$ is the rolling variance of domain $k$'s trust scores and $\alpha > 0$ is the variance penalty amplifier. This mechanism directly addresses the data poisoning vulnerability identified in Section 6: an attacker who compromises a sensor and forces it to broadcast artificially high or manipulated scores simultaneously introduces variance into the historical signal. The induced variance triggers weight suppression, converting spoofed testimony into mostly epistemic uncertainty. The vacuous identity property of Dempster's Rule ($m \oplus m_{\text{vacuous}} = m$) guarantees that a domain rendered vacuous by high variance is mathematically invisible in the fusion — it can neither help nor harm the consensus (Jøsang, 2016).

**Table 2.** Domain weight dynamics under varying variance levels ($\alpha = 10$).

| Domain State | $\sigma^2$ | $W_{\text{raw}}$ | Effect on Fusion |
|:---|:---:|:---:|:---|
| Stable, well-instrumented | 0.01 | 0.909 | Near-full evidential commitment |
| Moderate jitter (BYOD) | 0.05 | 0.667 | One-third of evidence uncertain |
| High volatility (IoT sensor) | 0.10 | 0.500 | Half the evidence is uncertain |
| Suspected compromise | 0.25 | 0.286 | Domain nearly vacuous |

This mechanism provides native resilience against the adversarial manipulation that Ali et al. (2024) document: variance-unstable evidence is automatically discounted regardless of its absolute value, preventing poisoned high-trust signals from dominating the fused output. The multi-domain architecture further strengthens this defence — an attacker who successfully spoofs one domain's context must simultaneously maintain consistent spoofing across all four independent domains to avoid triggering cross-domain conflict in the combination rule.

#### 7.2.3 Exponential Temporal Decay

The DCTA treats trust as a temporally depreciating asset through exponential decay:

$$
D(t) = e^{-\lambda \cdot t/T}
$$

where $\lambda$ is the decay rate constant and $T$ is the session window duration. This mechanism directly resolves the *temporal passport problem* that pervades all five paradigms:

- **Perimeter/VPN**: The VPN authentication signal depreciates to near-zero within the short-term evaluation window (30 minutes, calibrated against NIST SP 800-63B inactivity timeout requirements), forcing re-verification regardless of whether an explicit revocation event has occurred.
- **Static RBAC**: The role validation performed at login loses evidentiary weight continuously, ensuring that the access decision relies on accumulated behavioural evidence rather than a single point-in-time credential verification.
- **NIST SP 800-207**: Temporal decay provides the specific mathematical mechanism that the Trust Algorithm abstraction leaves unspecified — the precise rate at which evidence is discounted.
- **CSA SDP**: The SPA authentication signal, while highly reliable at $t = 0$, is continuously depreciated, transforming the SDP's point-in-time authentication into a time-bounded, self-expiring trust grant. This fills the post-authentication trust management gap without requiring protocol modifications to the SDP specification.
- **AI-IDS/SDN**: The SDN controller's initial authentication is subject to the same decay, ensuring that the controller's omniscient authority is continuously re-evaluated — treating infrastructure components as monitored entities subject to the same temporal scrutiny as end-users.

The dual-horizon architecture — a 30-minute short-term freshness window ($\lambda_{\text{short}} = 3.0$) and a 48-hour long-term inertia window ($\lambda_{\text{long}} = 0.5$) — ensures that both rapid compromise detection and sustained behavioural baseline assessment are simultaneously enforced (Robbins et al., 2025).

#### 7.2.4 Graduated Access via Pignistic Transformation

The Pignistic transformation converts the fused Dempster-Shafer mass function into an actionable probability:

$$
BetP(\text{Safe}) = m(\{\text{Safe}\}) + \frac{m(\Theta)}{2}
$$

This continuous score maps to tiered access thresholds:

$$
\text{Decision} = \begin{cases}
\text{Full Access} & \text{if } BetP(\text{Safe}) > 0.75 \\
\text{Limited Access} & \text{if } 0.45 \leq BetP(\text{Safe}) \leq 0.75 \\
\text{No Access} & \text{if } BetP(\text{Safe}) < 0.45
\end{cases}
$$

This graduated architecture directly resolves the binary trust limitation of both RBAC (allow/deny) and SDP (Join/Leave). An entity whose trustworthiness is ambiguous — perhaps transitioning between network contexts mid-session, or exhibiting marginally anomalous behaviour — is not catastrophically locked out (imposing unacceptable friction) or dangerously granted full access (enabling lateral movement). Instead, it is routed into a constrained access tier with reduced privileges proportionate to the residual uncertainty. This contextual grey-area routing represents a qualitative advance over the binary logic of every paradigm analysed in this paper.

### 7.3 Architectural Integration

The DCTA does not replace the five paradigms; it *completes* them. Table 3 maps the DCTA's mechanisms to the specific gaps each paradigm leaves open.

**Table 3.** DCTA architectural integration with existing paradigms.

| Paradigm Gap | DCTA Resolution Mechanism |
|:---|:---|
| Perimeter: no post-VPN verification | Temporal decay depreciates VPN authentication; multi-domain fusion detects post-auth compromise |
| RBAC: context-blindness, temporal passport | Four-domain contextual evaluation replaces single-dimension role check; decay eliminates temporal passport |
| NIST PE: unspecified Trust Algorithm | DS fusion + variance weighting + temporal decay = fully specified, mathematically tractable Trust Algorithm |
| SDP: post-authentication silence, binary trust | Continuous trust scoring fills the post-SPA gap; graduated thresholds replace binary Join/Leave |
| AI-IDS: data poisoning, detection-enforcement gap | Variance-based weighting discounts poisoned evidence; trust scores directly drive enforcement via PDP/PEP coupling |

The DCTA's separation of trust *computation* (Policy Decision Point) from trust *enforcement* (Policy Enforcement Point) — implemented through Open Policy Agent and Envoy proxy in the reference architecture — enables the same algorithmic engine to drive enforcement across heterogeneous technologies: SDP controllers, SDN flow tables, SASE Points of Presence, and microsegmentation firewalls. The trust computation is vendor-agnostic and enforcement-technology-independent, addressing NIST SP 800-207 Section 5's concern about proprietary data format lock-in by mapping vendor-specific telemetry to a standardised evidential format (basic probability assignments over a common frame of discernment) before ingestion by the fusion engine.

### 7.4 Formal Properties Supporting the Resolution

The DCTA's mathematical foundation provides three formal properties that directly strengthen the resolution:

**Property 1: Double-Attenuation Variance.** The nested Binomial architecture produces composite trust variance that is doubly attenuated — first by within-domain facet count ($1/n_k$) and second by cross-domain weight diversification ($W_k^2$). This variance cascade ensures that the composite trust estimate is inherently self-stabilising, achieving precision that no single telemetry domain could provide in isolation — a direct instantiation of Markowitz's (1952) diversification principle in the trust evaluation domain.

**Property 2: Anti-Spoofing Through Variance Coupling.** The coupling between domain score (what the domain reports) and domain weight (how much the fusion trusts that report) creates a feedback mechanism that is inherently adversarial-resilient. An attacker who compromises a single evidence source and forces it to broadcast artificially high trust scores simultaneously introduces instability (variance) into the historical signal. The induced variance triggers weight suppression via $W_k = (1 + \alpha \sigma_k^2)^{-1}$, converting the attacker's spoofed high-trust testimony into primarily vacuous mass ($m(\Theta) \approx 1$). The vacuous identity property of Dempster's Rule guarantees that this vacuous contribution is mathematically invisible in the fusion output — neutralising the attack without requiring explicit attack detection.

**Property 3: Self-Calibrating Uncertainty.** The architecture is self-calibrating at both boundary conditions and intermediate states. At perfect stability ($\sigma_k^2 = 0$), the domain achieves full evidential commitment ($m(\Theta) = 0$). At complete chaos ($\sigma_k^2 \to \infty$), the domain becomes vacuous ($m(\Theta) \to 1$). Between these extremes, uncertainty scales continuously and monotonically with observed instability, requiring no manual threshold calibration or predefined uncertainty budgets. This contrasts sharply with NIST's framework, which leaves uncertainty handling to implementation-specific ad hoc decisions, and with SDP's binary model, which lacks any uncertainty representation whatsoever.

---

### 7.5 Limitations

The following limitations constrain the scope and generalisability of this analysis:

1. **Analytical scope.** This paper provides an architectural and diagnostic analysis rather than empirical validation. The DCTA Ensemble Trust Model is presented as a candidate resolution whose formal properties are argued to address the identified gaps, but its operational effectiveness is validated in companion publications rather than within this paper. The claims regarding breach containment, latency, and classification accuracy are supported by the companion testbed and simulation studies, not by the critical analysis presented here.

2. **Specification-level critique.** The five paradigms are analysed at the specification level (NIST SP 800-207, CSA SDP v2.0, published research papers) rather than from production deployment data. Implementation-specific mitigations — vendor-proprietary continuous monitoring add-ons, custom SIEM integrations, or organisation-specific RBAC extensions — may partially address the identified gaps in specific deployments without resolving the architectural absence at the specification level.

3. **Binary framing.** The DCTA model's frame of discernment is binary ($\Theta = \{\text{Safe}, \text{Unsafe}\}$). While this is sufficient for the three-tiered access classification presented, more granular risk categorisation (e.g., $\{\text{Safe}, \text{Suspicious}, \text{Compromised}\}$) may be required for advanced threat response workflows. Extension to multi-state frames is architecturally feasible but increases DS combination complexity.

4. **Adversarial adaptation.** The variance-based anti-spoofing mechanism (Property 2) addresses naïve attackers who introduce detectable variance. Sophisticated adversaries capable of maintaining low variance while reporting fabricated — but stable — high trust scores (the "stable-but-false" attack) require complementary hardware attestation (TPM 2.0) for mitigation, which is outside the scope of this analysis.

5. **Paradigm selection.** The five paradigms were selected for their architectural significance and prevalence in the literature. Other relevant approaches — including blockchain-based authentication, SASE frameworks, and microsegmentation-only architectures — are acknowledged but not analysed in equivalent depth. Their inclusion would strengthen the comprehensiveness of the diagnostic but is unlikely to alter the central finding.

---

## 8. Conclusion

This paper has demonstrated, through unified critical analysis, that five ostensibly progressive security paradigms — perimeter defence, static RBAC, NIST SP 800-207, CSA SDP (Specification v2.0 and Architecture Guide), and AI-augmented IDS in SDN-governed heterogeneous networks — all share a common structural failure: the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions. This failure is not a residue of incomplete implementation but a structural property of architectures that treat trust as a binary, point-in-time determination.

Perimeter security assumes a defensible boundary that heterogeneous multi-cloud, BYOD, and IoT topologies have dissolved. Static RBAC assumes a stable workforce and device population that does not change within the lifetime of a session. NIST SP 800-207 mandates continuous trust evaluation but leaves the Trust Algorithm mathematically unspecified, creating an implementation vacuum. CSA SDP achieves rigorous session establishment through SPA and mTLS but provides no post-authentication trust management, creating an implicit trust period that grows with every second after the handshake. AI-augmented IDS in SDN introduces new adversarial attack surfaces — data poisoning, cumulative belief fusion corruption — while the SDN controller reproduces static RBAC's temporal passport at the architectural level.

The Dynamic Contextual Trust Architecture Ensemble Model bridges these gaps through four interlocking mechanisms: multi-domain Dempster-Shafer evidential fusion that explicitly represents epistemic uncertainty; variance-based dynamic weighting that achieves native adversarial resilience through automatic evidence discounting; exponential temporal decay that transforms authentication from a one-time gate into a continuously depreciating asset; and graduated Pignistic-based access decisions that replace binary allow/deny logic with risk-proportionate, threshold-based access tiers.

The resulting architecture does not replace any of the five paradigms; it completes them. SDP provides the cryptographic session establishment. NIST SP 800-207 provides the logical component architecture. SDN provides the programmable enforcement fabric. The DCTA provides the *missing mathematical interior* — the temporally dynamic, variance-calibrated, uncertainty-aware trust evaluation engine that each paradigm implicitly requires but none specifies. Together, they constitute a comprehensive security architecture that is maximally secure not only at the moment of authentication but at every moment thereafter — continuously, mathematically, and without implicit trust.

---

## References

Ahmed, T., Li, Y., & Zhang, W. (2024). Dynamic trust management for zero trust architectures in heterogeneous IoT environments. *IEEE Transactions on Dependable and Secure Computing, 21*(3), 1542–1557. https://doi.org/10.1109/TDSC.2023.3312456

Al-Sanjary, O. I., Ahmed, A. A., & Jaharadak, A. A. (2023). Access control models in cloud computing: A comprehensive survey. *Journal of King Saud University – Computer and Information Sciences, 35*(6), 101567. https://doi.org/10.1016/j.jksuci.2023.101567

Alawida, M., Oqaily, A., Halboob, W., & Abutair, H. (2024). A comprehensive survey on zero trust architecture (ZTA): Concepts, components, and implementation. *IEEE Access, 12*, 4526–4550.

Alder, S. (2025). The evolution of zero trust: From concept to enterprise standard. *Journal of Cybersecurity Research, 11*(1), 23–41. https://doi.org/10.1016/j.jcsr.2025.100234

Ali, M., Naeem, F., Tariq, M., & Kaddoum, G. (2024). Adversarial attacks on AI-based intrusion detection system for heterogeneous wireless communications networks. *IEEE Transactions on Wireless Communications, 23*(5), 4367–4381. https://doi.org/10.1109/TWC.2023.3321456

Al-Mutairi, A., & Hassan, R. (2024). Integrating SDN and Zero Trust Architecture for robust cloud environments: A review. *Computers and Security, 136*, 103550.

Alqassem, I., Svetinovic, D., & Rahwan, T. (2025). Federated trust management for resource-constrained edge networks. *IEEE Internet of Things Journal, 12*(4), 3801–3815. https://doi.org/10.1109/JIOT.2024.3489123

Alsubhi, K., Al-Begain, K., & Durad, M. H. (2024). Continuous trust evaluation in zero trust architectures: A dynamic scoring framework. *Computers & Security, 138*, 103672. https://doi.org/10.1016/j.cose.2024.103672

Appgate. (2024). *The state of Zero Trust and SDP operational deployment*. Appgate Cybersecurity Research.

Buck, C., Olenberger, C., Schweizer, A., Völter, F., & Eymann, T. (2022). Never trust, always verify: A multivocal literature review on current knowledge and research gaps of zero-trust. *Computers & Security, 110*, 102436. https://doi.org/10.1016/j.cose.2021.102436

Chen, X., & Wang, L. (2025). Explainable AI for dynamic access control in zero trust architectures. *ACM Computing Surveys, 57*(2), 1–36. https://doi.org/10.1145/3672891

Chen, Y., Wang, L., & Zhao, H. (2025). Distributed Zero Trust framework leveraging Software-Defined Perimeter protocols for IoT environments. *Journal of Network and Computer Applications, 215*, 103628.

CISA. (2024). *Known exploited vulnerabilities catalog: VPN appliance exploitation advisory* (AA24-038A). Cybersecurity and Infrastructure Security Agency. https://www.cisa.gov/known-exploited-vulnerabilities-catalog

Cloud Security Alliance. (2022). *Software-Defined Perimeter (SDP) Specification v2.0*. Cloud Security Alliance. https://cloudsecurityalliance.org/artifacts/sdp-specification-v2-0

Cloud Security Alliance. (2024). *Software-Defined Perimeter (SDP) Architecture Guide v2*. Cloud Security Alliance. https://cloudsecurityalliance.org/artifacts/sdp-architecture-guide-v2

Cloud Security Alliance. (2025). *Zero trust architecture for cloud-native environments: Best practices and reference architecture* (Version 2.0). https://cloudsecurityalliance.org/artifacts/zero-trust-architecture

Giannopoulos, A., Spantideas, S., Tsinos, C., & Trakadas, P. (2023). Security and privacy in aeronautical communication networks: A survey of current challenges and future directions. *IEEE Access, 11*, 45720–45743. https://doi.org/10.1109/ACCESS.2023.3271234

Habib, M. A., Mehmood, A., & Ahmad, M. (2022). Role-based access control challenges in IoT environments: A systematic literature review. *ACM Computing Surveys, 55*(4), 1–38. https://doi.org/10.1145/3544979

IBM Security. (2024). *Cost of a data breach report 2024*. IBM Corporation. https://www.ibm.com/reports/data-breach

Jøsang, A. (2016). *Subjective logic: A formalism for reasoning under uncertainty*. Springer. https://doi.org/10.1007/978-3-319-42337-1

Kreutz, D., Ramos, F. M. V., Veríssimo, P. E., Rothenberg, C. E., Azodolmolky, S., & Uhlig, S. (2015). Software-defined networking: A comprehensive survey. *Proceedings of the IEEE, 103*(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Kumar, A., & Patel, S. (2023). PKI challenges in zero trust deployments: A case study of certificate lifecycle management at scale. *Journal of Network and Systems Management, 31*(4), 112–134. https://doi.org/10.1007/s10922-023-09756-3

Liu, W., Chen, L., & Wang, Y. (2023). Evidential reasoning for dynamic trust evaluation in heterogeneous networks. *Information Fusion, 96*, 101–115. https://doi.org/10.1016/j.inffus.2023.03.014

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance, 7*(1), 77–91. https://doi.org/10.2307/2975974

Mehraj, S., & Banday, M. T. (2022). VPN security vulnerabilities and mitigation strategies: A comprehensive analysis. *Journal of Network and Computer Applications, 204*, 103413. https://doi.org/10.1016/j.jnca.2022.103413

Moubayed, A., Refaey, A., & Shami, A. (2022). Software-Defined Perimeter (SDP): State of the art. *IEEE Access, 10*, 96156–96181. https://doi.org/10.1109/ACCESS.2022.3204623

NIST. (2020). *NIST Special Publication 800-207: Zero Trust Architecture*. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

Oqaily, A., Alawida, M., & Halboob, W. (2024). Operational metrics and latency analysis of Zero Trust Architecture deployments. *IEEE Security & Privacy, 22*(4), 18–29.

Robbins, J. S., McCormick, D., & Patel, R. (2025). Temporal dynamics in continuous adaptive risk and trust assessment (CARTA). *IEEE Security & Privacy, 23*(2), 44–53. https://doi.org/10.1109/MSEC.2025.3401234

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939

Sandhu, R. S., Coyne, E. J., Feinstein, H. L., & Youman, C. E. (1996). Role-based access control models. *IEEE Computer, 29*(2), 38–47. https://doi.org/10.1109/2.485845

Shafer, G. (1976). *A mathematical theory of evidence*. Princeton University Press.

Sharma, P., Kumar, R., & Singh, A. (2023). Lightweight access control for resource-constrained IoT devices in zero trust environments. *Journal of Systems Architecture, 140*, 102912. https://doi.org/10.1016/j.sysarc.2023.102912

Shin, D., Kim, J., & Lee, S. (2025). A generalized framework for optimizing context-aware trust algorithms in Zero Trust Architecture. *Computers & Security, 148*, 104112.

Smith, J. (2024). Overcoming Controller bottlenecks in Gateway-to-Gateway Software-Defined Perimeters. *Journal of Network and Systems Management, 32*(3), 45–62.

Stafford, B. (2023). The end of the perimeter: Security architecture for cloud-first enterprises. *Journal of Information Security and Applications, 73*, 103442. https://doi.org/10.1016/j.jisa.2023.103442

Wang, T., Bhuiyan, M. Z. A., Wang, G., Rahman, M. A., Wu, J., & Cao, J. (2022). Big data reduction for a smart city's critical infrastructure: An approach based on deep learning and trust evaluation. *IEEE Transactions on Industrial Informatics, 18*(3), 1897–1907. https://doi.org/10.1109/TII.2021.3099868

Xu, J. (2024). Trust algorithm optimization in Zero Trust architectures utilizing federated learning and SDN. *Journal of Information Security and Applications, 80*, 103681.

Yan, Q., Yu, F. R., Gong, Q., & Li, J. (2023). Software-defined networking (SDN) and distributed denial of service (DDoS) attacks in cloud computing environments: A survey, some research issues, and challenges. *IEEE Communications Surveys & Tutorials, 25*(1), 602–636. https://doi.org/10.1109/COMST.2022.3213214

Zanasi, C., Bartoli, A., & Salsano, S. (2023). Certificate management automation for zero trust architectures: Challenges and solutions. *IEEE Communications Magazine, 61*(8), 56–62. https://doi.org/10.1109/MCOM.001.2300012
