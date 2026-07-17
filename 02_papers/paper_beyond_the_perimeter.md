# Beyond the Perimeter: Why Static RBAC, Software-Defined Perimeters, and AI-Augmented Detection Fail Without Dynamic Trust in Heterogeneous Networks

---

**Abstract.** Contemporary network security architectures — perimeter-based defences, static Role-Based Access Control (RBAC), NIST SP 800-207 Zero Trust Architecture, Cloud Security Alliance Software-Defined Perimeters (CSA SDP Specification v2.0 and Architecture Guide), and AI-augmented Intrusion Detection Systems (IDS) deployed within Software-Defined Networking (SDN) fabrics — are each presented as progressive solutions to the access control problem in heterogeneous enterprise networks. This paper presents a structured critical analysis demonstrating that all five paradigms share a common structural failure: the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions. Each paradigm is evaluated against four diagnostic criteria — temporal trust treatment, contextual awareness, uncertainty representation, and enforcement coupling — and the failures are mapped to a unified diagnostic table identifying the specific missing capability. The paper then specifies the requirements for an architectural resolution and positions the Dynamic Contextual Trust Architecture (DCTA) Ensemble Model, grounded in Dempster-Shafer evidential fusion with variance-based dynamic weighting and exponential temporal decay, as a candidate resolution whose formal properties address the identified gaps. Empirical validation is reported in companion publications.

**Keywords:** Zero Trust Architecture, dynamic trust, RBAC, Software-Defined Perimeter, NIST SP 800-207, AI-IDS, SDN, Dempster-Shafer theory, temporal decay, heterogeneous networks

---

## 1. Introduction: The Persistence of Implicit Trust

The foundational promise of modern cybersecurity — that identity has replaced the network perimeter as the primary security boundary — remains structurally unfulfilled across every dominant access control paradigm. Despite two decades of architectural evolution from castle-and-moat firewalls through role-based access control to software-defined perimeters and AI-augmented detection, a single vulnerability persists: the *implicit trust period* — a temporal window during which an authenticated entity retains access privileges without continuous re-verification of its trustworthiness.

This implicit trust period is not the residue of incomplete implementation. It is a *structural* property of architectures that treat trust as a binary, point-in-time determination rather than as a continuous, temporally depreciating, evidentially grounded quantity. A firewall that grants access to authenticated internal traffic implicitly trusts that traffic for the duration of the session. A static RBAC policy that validates role membership at login implicitly trusts that the authenticated role holder remains legitimate until session expiration. An SDP controller that issues a cryptographic entitlement after a rigorous multi-phase Join workflow implicitly trusts that entitlement until an explicit Leave event occurs. An AI-based IDS that classifies traffic as benign implicitly trusts that classification until the model is retrained. In each case, the security architecture performs rigorous verification at a discrete temporal boundary and then withdraws into passive monitoring or complete inattention for the interval that follows — an interval that adversaries are precisely optimised to exploit [1], [5].

The consequences of this structural gap are empirically documented. The IBM Security (2024) *Cost of a Data Breach Report* identifies that the mean time to identify a data breach reached 194 days in 2024, with lateral movement within implicitly trusted zones accounting for a substantial portion of the containment delay [2]. Smiliotopoulos et al. [30] provide a systematic survey confirming that lateral movement remains one of the most challenging post-compromise activities to detect, precisely because it occurs within the implicitly trusted interior. The Cybersecurity and Infrastructure Security Agency (CISA) reports that exploitation of VPN appliance vulnerabilities and credential compromise constitutes a primary vector for advanced persistent threat campaigns targeting critical infrastructure [3]. These are not implementation failures; they are architectural consequences of systems that grant temporal passports at authentication boundaries and then lack the mathematical apparatus to depreciate, re-evaluate, or revoke those passports in response to post-authentication contextual changes.

This paper presents a unified critical analysis demonstrating that five ostensibly progressive security paradigms — perimeter defence, static RBAC, NIST SP 800-207, CSA SDP, and AI-augmented IDS in SDN — all converge on the same structural failure. The analysis is not merely diagnostic; it is constructive. Each paradigm's failure is mapped to a specific absence in its trust evaluation architecture, and the requirements for an architectural resolution are formally specified.

The contributions of this paper are threefold:

1. **Unified diagnostic analysis**: A structured demonstration that five distinct security paradigms — spanning three decades of architectural evolution — share a single, common structural failure: the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions.
2. **Failure-to-capability mapping**: A systematic mapping of each paradigm's specific vulnerability to the precise missing capability (Table 1), establishing the requirements that any resolution must satisfy.
3. **Requirements specification and candidate architecture**: Specification of the requirements for an architectural resolution and positioning of the DCTA Ensemble Trust Model as a candidate whose formal properties address the identified gaps, with empirical validation reported in companion publications.

The remainder of this paper is organised as follows. Section 2 describes the analytical methodology. Section 3 analyses the dissolution of the network perimeter. Section 4 examines the structural inadequacy of static RBAC. Sections 5 and 6 critique NIST SP 800-207 and CSA SDP respectively. Section 7 exposes the adversarial fragility of AI-augmented IDS in SDN. Section 8 synthesises the common thread across all five paradigms and presents the resolution requirements. Section 9 concludes.

---

## 2. Analytical Methodology

This paper employs a structured critical analysis to evaluate five dominant security paradigms against the Zero Trust principle of continuous verification. The paradigms were selected based on three criteria: (i) architectural significance in the evolution of enterprise access control, (ii) prevalence in production deployments and industry adoption, and (iii) foundational role in the academic cybersecurity literature. This selection approach follows established practice in multivocal literature reviews of Zero Trust Architecture [5], [19].

Each paradigm is evaluated at the specification level — published standards (NIST SP 800-207 [1], CSA SDP v2.0 [27]), peer-reviewed research, and authoritative industry reports — rather than from production deployment data. This approach enables identification of structural limitations inherent in the architectural design, independent of implementation-specific mitigations that vendors or organisations may apply.

The analysis follows a failure-mapping framework in which each paradigm is assessed against four diagnostic criteria:

1. **Temporal trust treatment**: Does the paradigm specify how trust depreciates over time after initial verification?
2. **Contextual awareness**: Does the paradigm incorporate multi-dimensional contextual signals (device posture, network conditions, behavioural patterns) into access decisions?
3. **Uncertainty representation**: Does the paradigm distinguish between "trusted," "untrusted," and "insufficient evidence to determine" — or does it operate on a binary trust model?
4. **Enforcement coupling**: Is the detection/evaluation mechanism tightly coupled with the enforcement mechanism, or do they operate independently?

The findings from each paradigm analysis are synthesised into a unified failure mapping (Table 1) that identifies the specific missing capability, establishing the requirements for any architectural resolution.

---

## 3. The Dissolution of the Perimeter

### 3.1 Topological Obsolescence

The foundational premise of perimeter-based security — that a clearly delineated boundary exists between a trusted internal network and an untrusted external environment — has been rendered architecturally obsolete by the heterogeneity of modern enterprise infrastructures. Contemporary enterprises operate across a continuum of on-premises data centres, multi-cloud platforms (AWS, Azure, GCP), edge computing nodes, and a proliferation of unmanaged endpoints introduced by Bring Your Own Device (BYOD) and Internet of Things (IoT) policies [7], [14]. Network traffic no longer flows through a single defensible chokepoint; it traverses hybrid topologies where users, applications, and data reside in distributed trust domains with fundamentally different security postures [5].

The heterogeneity is not merely topological but *protocological*. Modern enterprise networks integrate devices operating on disparate communication protocols — Zigbee, BLE, and MQTT for IoT; HTTP/2 and gRPC for cloud-native microservices; legacy SNMP for infrastructure management. Wang et al. [17] demonstrate in their comprehensive survey that this heterogeneity of architectures, networking technologies, and protocols makes it "extremely difficult to evaluate, transfer, and maintain trust among different devices, protocols, architectures, and network operators." Perimeter security cannot enforce protocol-level inspection across this diversity, and no firewall rule can meaningfully differentiate risk based on the protocol or architectural context of an access request when that request traverses multiple network technologies in sequence.

Furthermore, modern enterprise topologies are not static: containers are spun up and destroyed in seconds, serverless functions execute transiently, and edge devices connect and disconnect unpredictably [7]. The attack surface of heterogeneous networks is exponentially larger than that of homogeneous, perimeter-bounded environments, and perimeter security treats this interior heterogeneity as a trusted monolith — providing no mechanism to distinguish between a fully patched, enterprise-managed workstation and a compromised IoT sensor operating on the same network segment. Wu et al. [20] demonstrate this challenge from the perspective of complex network observability, showing that IoT security fundamentally depends on the ability to observe and evaluate device behaviour across heterogeneous network topologies.

### 3.2 VPN Credential Inheritance and Lateral Movement

Firewalls and Virtual Private Networks (VPNs), the historic cornerstones of perimeter defence, were designed to gate access at a well-defined boundary. However, VPNs extend broad network-level access to authenticated users without continuous verification of their post-authentication behaviour, effectively creating authenticated tunnels of implicit trust [8], [9]. Once a VPN session is established, an adversary who has compromised a single credential or exploited a VPN vulnerability inherits that user's full network visibility, enabling unimpeded lateral movement across enterprise segments. The evolution from traditional VPN to Software-Defined Perimeter and Zero Trust Network Access architectures explicitly acknowledges this fundamental limitation of perimeter-centric models [8].

This is not a theoretical concern. CISA [3] confirms that state-sponsored actors routinely exploit VPN and perimeter appliance vulnerabilities to achieve persistent access to critical infrastructure. IBM Security [2] reports that organisations relying on perimeter-centric architectures experience significantly higher breach containment times precisely because lateral movement occurs within the "trusted" zone where monitoring is sparse and access controls are permissive. Smiliotopoulos et al. [30] provide a systematic analysis confirming that lateral movement detection remains one of the most challenging problems in modern network defence, precisely because existing architectures implicitly trust internal traffic.

The convergence of perimeter dissolution, protocological heterogeneity, and VPN credential inheritance establishes the first dimension of the structural failure: **perimeter security assumes a boundary that no longer exists, and its authentication model grants temporal passports that persist without depreciation**.

---

## 4. Static RBAC: Structural Inadequacy in Heterogeneous Environments

### 4.1 Role Explosion

Static Role-Based Access Control (RBAC), which assigns permissions to predefined organisational roles rather than to individual users, was originally conceived for relatively stable enterprise environments with predictable workforce structures and well-defined application boundaries [10]. While RBAC simplified administrative overhead by abstracting individual permissions into role hierarchies, its static nature introduces critical vulnerabilities in the dynamic, heterogeneous networks that characterise modern enterprises.

The first structural failure is *role explosion* — the combinatorial growth in the number of roles required to represent the fine-grained access patterns of a heterogeneous environment. Das et al. [11] demonstrate that in microservice architectures, the proliferation of service endpoints creates a role assessment challenge that static RBAC cannot manage without constructing centralised perspectives across distributed mesh architectures. In enterprises where users operate across multiple business units, access diverse cloud services, and interact with context-dependent resources, the number of distinct role definitions required to capture every legitimate access pattern grows unmanageably. Iqal et al. [12] provide a comprehensive systematic review confirming that in IoT-integrated enterprise environments, the frequency with which devices are added, reconfigured, or decommissioned renders static access control assignments perpetually stale, creating either over-privileged roles that violate least privilege or under-privileged roles that impede operational workflows.

### 4.2 Context-Blindness: Same Role, Different Risk

Beyond administrative rigidity, static RBAC is inherently *stateless* with respect to context and time. A user assigned the role of "Database Administrator" retains identical permissions whether they are connecting from an enterprise-hardened workstation on the corporate LAN at 10:00 AM or from an unmanaged personal device on a public Wi-Fi network at 02:00 AM. The access control system possesses no mechanism to evaluate the risk differential between these two contexts because static RBAC evaluates *who the user is* — their role — not *what the user is doing, from where, on what device, and at what time* [19]. This contextual blindness constitutes a critical vulnerability: a compromised credential operating under a high-privilege role can exfiltrate data undetected because the RBAC system has no behavioural baseline against which to detect anomalous access patterns.

### 4.3 The Temporal Passport Problem

The most consequential failure of static RBAC is its treatment of authentication as a discrete, one-time gate. Once a user authenticates and their role is validated, access persists for the session duration without re-evaluation. Meng et al. [13] demonstrate that continuous authentication protocols without centralised trust authorities are necessary precisely because static scoring models fail to trigger re-evaluation even when a device's security posture degrades mid-session — effectively granting a "temporal passport" that adversaries exploit for low-and-slow data exfiltration campaigns.

This temporal blindness directly contradicts the Zero Trust principle of "never trust, always verify," which requires continuous authentication and authorisation throughout the lifetime of every session [1]. In heterogeneous environments where device posture, network conditions, and user behaviour are inherently volatile, this "authenticate once, access forever" model creates a window of implicit trust — the very construct that Zero Trust Architecture exists to eliminate [5]. The inability of RBAC to revoke or constrain access dynamically in response to real-time risk signals means that session hijacking, credential theft, and insider threats all benefit from an extended operational runway.

A further dimension of this failure concerns computational asymmetry: enterprise networks increasingly incorporate resource-constrained devices — IoT sensors, embedded controllers, and edge gateways — whose limited processing power, memory, and energy budgets cannot sustain the overhead of complex centralised access control lookups. Mohseni-Ejiyeh [15] demonstrates that lightweight access control protocols are essential for mobile cloud-based IoT sensors, confirming that static RBAC designed for server-class infrastructure imposes requirements incompatible with resource-constrained devices.

The convergence of role explosion, context-blindness, and temporal passports establishes the second dimension of the structural failure: **static RBAC assumes a workforce, device population, and application landscape that does not change within the lifetime of a session — an assumption that heterogeneous enterprise networks violate continuously and at scale**.

---

## 5. Critique of NIST SP 800-207: The Unspecified Trust Algorithm

### 5.1 Section 3 — Logical Components: PE/PA/PEP Gaps

NIST Special Publication 800-207 remains the definitive federal framework establishing Zero Trust Architecture. Its tripartite logical architecture — Policy Engine (PE), Policy Administrator (PA), and Policy Enforcement Point (PEP) — is architecturally elegant and has profoundly influenced both academic discourse and commercial implementations [1]. The PE consumes contextual telemetry from identity stores, device posture databases, threat intelligence feeds, and behavioural analytics platforms to produce access determinations. The PA translates these into actionable instructions, and the PEP enforces them at the resource boundary.

However, a critical assessment reveals the most consequential limitation: the *deliberate abstraction of the Trust Algorithm* that operates within the PE. NIST SP 800-207 explicitly acknowledges that the Trust Algorithm processes input variables — identity assurance, device posture compliance, behavioural signals, resource sensitivity, and threat intelligence — to produce access decisions, yet provides no normative guidance on the mathematical form of this algorithm [1]. The framework specifies neither the weighting scheme by which disparate input variables are synthesised, nor the temporal dynamics by which evidence is discounted, nor the decision-theoretic framework by which uncertainty is handled. This architectural agnosticism was intentional — NIST sought to provide a framework, not a prescription — but it creates a critical implementation vacuum. In practice, security architects confronted with this vacuum default to either simplistic linear scoring models that assign fixed weights to each input variable, or to vendor-specific proprietary algorithms whose decision logic is opaque, unverifiable, and non-portable [19], [22].

The second structural concern relates to the *centralisation assumption* implicit in the PE–PA–PEP triad. While distributed deployment is permitted, the logical model describes a single authoritative decision point. In heterogeneous enterprise networks, the centralised PE becomes a performance bottleneck and a single point of failure whose unavailability reduces the enterprise to either a fail-open state (violating Zero Trust) or a fail-closed state (halting operations). The framework's failure to mandate distributed PE architectures with consensus mechanisms represents a significant gap for heterogeneous deployments [19].

Furthermore, none of NIST's four deployment model variations — Device Agent/Gateway, Enclave-Based, Resource Portal, and Device Application Sandboxing — adequately addresses the computational asymmetry that characterises heterogeneous networks. The Device Agent/Gateway model requires endpoint-hosted agents incompatible with BYOD and IoT devices [12]. The Device Application Sandboxing model assumes computational capacity unavailable on constrained devices [15]. The absence of heterogeneity-aware deployment guidance is a structural gap.

### 5.2 Section 4 — Deployment Scenarios: Underspecified Heterogeneous Guidance

Section 4 maps the abstract architecture to concrete scenarios: remote employees, multi-cloud environments, non-employee access, and BYOD devices. Each scenario illustrates PE–PA–PEP configuration for a specific topology, but all share a critical limitation: *temporal stationarity*.

The remote employee scenario assumes a static access pattern — a worker connected to a defined set of resources from a single device and location. It does not address the increasingly prevalent pattern of *mobile, multi-device, multi-network access* — a worker who transitions from corporate laptop on home network, to mobile device on cellular network, to shared workstation at a co-working space. Each transition fundamentally changes device posture, network context, and application context, yet the framework provides no guidance on how the Trust Algorithm should handle mid-session contextual shifts without either terminating the session or implicitly trusting the new context [5].

The multi-cloud scenario underestimates the complexity of trust signal federation across heterogeneous cloud environments, where each provider exposes different identity federation standards, device attestation capabilities, and network telemetry formats [17]. The BYOD scenario raises the most acute trust evaluation challenges. Unmanaged devices lack enterprise agents, may not support device attestation, and cannot be assumed to comply with endpoint security policies [12]. The framework's reliance on device agent telemetry as a trust input is structurally weakened, creating a "trust signal gap" where the PE must make access decisions with incomplete or absent device posture information.

### 5.3 Section 5 — Threats: Acknowledged but Unmitigated Temporal Vulnerabilities

Section 5 catalogues threats uniquely associated with ZTA deployments and represents a commendably honest self-assessment. The most architecturally consequential threat identified is the *subversion of the ZTA decision process* — a compromised PE that silently modifies access policies, rendering the entire apparatus complicit in an attack. NIST warns that "any enterprise administrator who can configure the PE rules can perform or approve changes to policy in an undetected way" [1], but provides no self-monitoring mechanism for the PE itself.

The *denial of service against PE/PA components* threat is particularly acute: because all access decisions flow through the PE–PA pipeline, its unavailability paralyses the entire infrastructure. Wang et al. [22] demonstrate that zero-trust based dynamic access control for cloud computing requires architectures that can function under degraded conditions — a capability NIST's centralised model does not guarantee.

The *stolen credentials and insider exploitation* threat assumes that the Trust Algorithm can distinguish between legitimate and illegitimate use of valid credentials — a capability requiring multi-dimensional behavioural analysis that the framework describes conceptually but does not specify algorithmically. The encrypted traffic inspection gap is amplified in heterogeneous environments with fragmented encryption standards, as documented across UAV, satellite, and ground-based communication networks [25].

In aggregate, NIST SP 800-207 establishes the third dimension of the structural failure: **the framework mandates continuous trust evaluation but leaves the mathematical apparatus — the weighting, temporal dynamics, uncertainty handling, and fusion logic — entirely unspecified, creating an implementation vacuum that defaults to the deterministic, context-blind scoring it was designed to replace**.

---

## 6. Critique of the CSA Software-Defined Perimeter

### 6.1 SDP Specification v2.0: Cryptographic Rigour, Post-Authentication Silence

The Cloud Security Alliance's SDP Specification v2.0 represents the most technically prescriptive articulation of Zero Trust Network Access at the protocol level. Where NIST operates at the architectural abstraction layer, SDP descends to the packet level, mandating exact cryptographic handshake sequences and protocol state machines [27].

The centrepiece is the enhanced Single Packet Authorization (SPA) protocol, which implements the "authenticate before connect" paradigm: the SDP Controller maintains all service ports in a default-closed state, rendering protected infrastructure invisible to network scanning, and opens a transient, individualised data path only upon cryptographic validation of a correctly formed SPA packet. The v2.0 enhancements — cryptographic nonces against replay attacks, timestamp validation for temporal freshness, and HMAC for payload integrity — address the most commonly cited vulnerabilities in older SPA implementations [28].

#### 6.1.1 The SPA Replay Window

Despite these enhancements, a rigorous evaluation reveals structural limitations. SPA is, by its architectural nature, a *point-in-time authentication mechanism*. The SPA packet demonstrates that the Initiating Host possessed valid credentials and a compliant device posture at the precise moment the packet was generated. It provides no assurance about the entity's state at any subsequent point. Once the SPA handshake succeeds and the encrypted tunnel is established, the specification provides no protocol-level mechanism for continuous re-evaluation during the active session. This creates precisely the implicit trust period that Zero Trust is designed to eliminate — a window of variable and potentially unbounded duration during which a compromised endpoint operates under the authority of an increasingly stale authentication signal [1]. The specification delegates post-authentication trust management to "continuous monitoring" mechanisms that are referenced but neither specified nor standardised. Lefebvre et al. [4] confirm this architectural limitation in their analysis of the integration between SDP and SDN paradigms, noting that the post-authentication monitoring gap requires explicit architectural remediation.

#### 6.1.2 The mTLS Certificate Lifecycle Problem

The v2.0 mandate of Mutual TLS (mTLS) for all intra-SDP communications elevates cryptographic assurance to bidirectional identity verification. However, the mTLS mandate introduces a *certificate lifecycle management complexity* that the specification acknowledges but does not resolve. In heterogeneous networks with thousands of Initiating Hosts — managed workstations, mobile devices, BYOD endpoints, IoT sensors, ephemeral cloud instances — each device requires a unique X.509 certificate issued by a trusted Certificate Authority, stored securely, and rotated before expiration. Certificate mismanagement — expired certificates, improperly stored private keys, revocation list propagation delays — represents a significant operational risk [22]. The specification's silence on recommended PKI architectures and fallback authentication mechanisms creates an implementation gap identified as a primary barrier to SDP adoption.

#### 6.1.3 IoT Computational Overhead

The v2.0 SPA message requires the Initiating Host to generate cryptographic nonces, compute HMAC digests, and in some configurations perform asymmetric key operations — all within the strict temporal window for timestamp validity. For resource-constrained IoT devices — industrial sensors, medical telemetry devices, smart building actuators — these cryptographic operations may exceed the device's computational budget or introduce authentication latencies conflicting with real-time operational requirements [15]. The specification provides no lightweight SPA variant for constrained devices, no delegation mechanism for gateway-mediated SPA on behalf of downstream devices, and no guidance on maintaining security guarantees when the full SPA handshake is computationally infeasible.

### 6.2 SDP Architecture Guide: Operational Workflows and Structural Limitations

#### 6.2.1 Controller Centralisation

The Architecture Guide treats the Controller as a logically centralised, architecturally singular component [31], [32]. While operational deployments may replicate the Controller for high availability, the logical model describes a single policy authority. This centralisation creates two architectural risks: the Controller becomes a high-value target for adversarial compromise — a compromised Controller can silently issue entitlements to adversary-controlled devices (analogous to NIST SP 800-207's PE subversion threat) — and the Controller becomes a single point of failure whose unavailability paralyses the entire infrastructure [19]. Lefebvre et al. [33] demonstrate through their SDP implementation for network introspection that the centralised controller model introduces inherent scalability constraints that distributed architectures must address.

#### 6.2.2 Binary Trust: The Join/Leave Cliff-Edge

The Architecture Guide's trust model remains fundamentally binary. Upon successful completion of the Join process, the Initiating Host is either fully trusted (receiving the cryptographic entitlement for complete resource access) or fully untrusted (receiving nothing). There is no intermediate state — no mechanism for granting constrained, read-only, or monitored access to entities whose trustworthiness is ambiguous or degraded but not categorically insufficient. This binary model creates a cliff-edge access decision: a device meeting 95% of posture requirements but failing a single check is treated identically to a device failing every check — both receive zero access. In practice, this cliff-edge behaviour drives security administrators to relax posture requirements to avoid excessive denials, inadvertently undermining the security assurance the multi-phase verification was designed to provide [5]. Harshavardini and Bertia [21] confirm that integrating SDP with SDN-based microsegmentation requires moving beyond this binary model to enable graduated trust enforcement.

#### 6.2.3 The Thundering Herd Problem

The Join process's sequential, blocking nature — where each verification phase must complete before the next begins, and any failure terminates the entire process — creates a "thundering herd" problem in high-throughput environments. At the start of a business day, during a failover event, or following a network partition recovery, thousands of simultaneous Join requests exceed the Controller's processing capacity, producing escalating latencies and potential timeouts that deny access to legitimate devices. Pagadala-Sekar [34] identifies this scalability concern in the context of integrating SDP and Zero Trust in platform engineering, noting the need for distributed policy enforcement mechanisms.

### 6.3 The Post-Authentication Trust Management Gap

The preceding critiques of both the Specification and Architecture Guide converge on a single, architecturally fundamental observation: **the SDP framework excels at session establishment but provides no standardised, mathematically specified mechanism for managing trust during an established session**.

A session established through rigorous SPA and mTLS at time $t = 0$ remains fully authorised at $t = 30$ minutes, at $t = 2$ hours, and at $t = 24$ hours, unless an explicit revocation event terminates it. During this period, the initial authentication signal — highly reliable at $t = 0$ — progressively loses its evidentiary weight without any corresponding reduction in the access privileges it underwrites. This temporal blindness creates the implicit trust period that adversaries exploit: a session hijack or device compromise occurring after the SPA handshake but before the next posture check operates with the full authority of the original authentication.

The SDP framework's reactive revocation model — terminating sessions upon detection of posture degradation — partially mitigates this risk but suffers from fundamental detection latency. The interval between a posture degradation event and its detection by the SDP Client or Controller constitutes a "detection gap" during which the compromised session retains full access [2].

The SDP framework thus establishes the fourth dimension of the structural failure: **cryptographic session establishment rigour combined with post-authentication trust management silence creates an architecture that is maximally secure at the moment of authentication and progressively less secure with every passing second**.

---

## 7. Adversarial Fragility of AI-Augmented IDS in SDN-Governed Heterogeneous Networks

### 7.1 The Compensatory Migration and Its False Promise

The recognition that perimeter security and static RBAC are structurally inadequate has prompted a broad migration toward software-defined networking (SDN) and AI-augmented intrusion detection as compensatory architectures. SDN decouples the control plane from the data plane, centralising policy enforcement in a logically unified controller, while AI-based IDS promises real-time anomaly detection transcending static signature matching [35]. In theory, these technologies address the catalogued failures: SDN enables dynamic, programmable microsegmentation that static firewalls cannot achieve, and AI-IDS provides the continuous behavioural monitoring that static RBAC lacks.

However, absent a rigorous underlying trust architecture, this technological migration merely transposes the perimeter security problem to a higher abstraction layer without resolving its fundamental vulnerabilities. Ali et al.'s [35] investigation of adversarial attacks on AI-based IDS for heterogeneous wireless communications networks reveals that the compensatory migration introduces *new* attack surfaces while leaving the original trust deficit unaddressed.

### 7.2 Data Poisoning and Cumulative Belief Fusion Corruption

Ali et al. [35] empirically demonstrate that AI-based IDS deployed within heterogeneous SDN environments are themselves vulnerable to adversarial manipulation through *data poisoning*. By injecting carefully crafted malicious samples into the training corpus, an adversary can systematically bias the classification model to misclassify attack traffic as benign or legitimate traffic as malicious, undermining operational reliability without directly compromising the SDN controller or perimeter defences.

This finding is profoundly consequential for heterogeneous networks: if the AI-IDS is trained on data aggregated from multiple heterogeneous sources, an adversary who can poison data from any single source degrades detection accuracy across the entire system. The poisoned model does not fail locally; it fails *globally* because the centralised training process propagates adversarial bias across all classification boundaries.

In the context of trust management, these findings expose a critical architectural weakness: adversaries can exploit unverified data flows across SDN-separated planes to covertly manipulate the evidence base upon which security decisions are made. When an IDS performs *cumulative belief fusion* — aggregating evidence from multiple sources to form composite threat assessments — poisoned input from any constituent source contaminates the fused output. This is precisely analogous to the Dempster-Shafer combination problem when evidence sources are not independent or when their reliability is not dynamically assessed: combining corrupted evidence without quantifying source trustworthiness produces fused belief that is systematically biased toward the adversary's intended conclusion [38]. Ji et al. [37] demonstrate that weighted fusion of evidence requires explicit unified trust distribution mechanisms to prevent precisely this form of corruption.

Static RBAC and perimeter-based architectures possess no mechanism to address this problem. A firewall does not evaluate the *quality* or *provenance* of data flowing through it — it merely evaluates whether source and destination match an access control rule. RBAC does not evaluate whether data submitted to a training pipeline has been adversarially manipulated — it only evaluates whether the user's role includes permission to submit data. The adversary possessing legitimate credentials operates entirely within the bounds of the static access control policy while corrupting defensive infrastructure from within.

### 7.3 The SDN Controller as Static RBAC at Scale

The SDN controller operates on what is fundamentally a binary trust model: once authenticated through credential-based mechanisms at initialisation, the controller possesses comprehensive, unrestricted authority over the entire network fabric — installing flow rules, modifying routing tables, redirecting traffic, and reconfiguring access policies across all connected switches. This authority persists without continuous re-verification of the controller's integrity or behavioural consistency [39].

This is *static RBAC elevated to the architectural level*. The controller is assigned the "role" of omniscient network governor at authentication time, and this role is never re-evaluated regardless of subsequent behavioural anomalies. A compromised controller inherits the full scope of this unchallenged authority. In a heterogeneous environment where the controller governs traffic across fundamentally different network technologies, a single controller compromise cascades catastrophically across all connected domains. Thirumalairai and Pradeesh [18] propose probabilistic trust inference to address this precise vulnerability, confirming that multi-level trust in SDN cannot rely on static, one-time authentication. The perimeter security model's assumption that authenticated internal entities are trustworthy is reproduced at the control plane level, with correspondingly amplified consequences.

### 7.4 Detection Without Enforcement: The Incomplete Security Posture

A critical gap in the AI-augmented approach — and one that illuminates the broader limitations of AI-augmented perimeter defence — is the exclusive focus on attack *detection* rather than trust *architecture*. The proposed AI-based IDS operates as a passive detection system: it identifies threats but does not integrate with the SDN controller to dynamically modify enforcement policies in response [35]. This decoupling between detection and enforcement reproduces the fundamental weakness of traditional perimeter security: the firewall (IDS) observes traffic, but the enforcement mechanism (controller) operates independently based on static policies.

In a genuinely dynamic architecture, detection must be tightly coupled with enforcement through a Policy Decision Point that translates trust evaluations into real-time flow-rule modifications, access revocations, and microsegmentation adjustments [1]. The absence of this integration means that even when the IDS correctly detects an adversarial attack, the network enforcement posture does not automatically adapt, leaving a temporal gap during which the adversary can consolidate their position.

Furthermore, the AI-IDS itself is demonstrated to be vulnerable to the very adversarial attacks it is designed to detect. This creates a circular dependency: the defence mechanism requires protection from the same threat class it addresses, but no meta-level trust architecture exists to provide that protection. Mekdad et al. [25] document analogous adversarial vulnerabilities across heterogeneous UAV communication networks, confirming that the detection-without-architecture problem generalises beyond terrestrial SDN to airborne and heterogeneous network domains.

The AI-IDS paradigm thus establishes the fifth dimension of the structural failure: **detection without trust-grounded enforcement, combined with adversarial vulnerability of the detection mechanism itself, creates a security architecture that is simultaneously incomplete and self-undermining**.

---

## 8. The Common Thread: The Dynamic Trust Imperative

### 8.1 Mapping Each Failure to the Missing Continuous Trust Evaluation

The five paradigms analysed in Sections 3–7, despite their apparent architectural diversity, converge on a single structural failure. Table 1 maps each paradigm's specific vulnerability to the missing capability.

**Table 1.** Structural failure mapping across five security paradigms.

| Paradigm | Specific Vulnerability | Missing Capability |
|:---|:---|:---|
| **Perimeter Security** | VPN credential inheritance; flat trust interior; lateral movement | Continuous post-authentication verification; trust depreciation |
| **Static RBAC** | Role explosion; context-blindness; temporal passport | Context-aware, temporally dynamic access evaluation |
| **NIST SP 800-207** | Unspecified Trust Algorithm; centralised PE; temporal stationarity in deployment scenarios | Mathematically specified weighting, fusion, and decay logic |
| **CSA SDP** | Point-in-time SPA; binary Join/Leave trust; post-authentication silence; IoT overhead | Graduated, continuous trust scoring; lightweight evaluation |
| **AI-IDS in SDN** | Data poisoning; belief fusion corruption; static-RBAC controller; detection-enforcement gap | Adversarially robust evidence fusion; trust-aware enforcement |

The common thread is unambiguous: **the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions**. Each paradigm performs its respective authentication, verification, or detection function competently at a discrete temporal boundary — perimeter crossing, role validation, SPA handshake, model classification — and then either withdraws entirely or delegates post-boundary trust management to unspecified, ad hoc mechanisms that lack mathematical rigour, uncertainty awareness, or temporal dynamics.

### 8.2 Requirements for an Architectural Resolution

The failure mapping in Table 1 yields five requirements that any architectural resolution must satisfy:

**Requirement 1: Multi-dimensional evidential fusion.** The resolution must fuse evidence from multiple independent telemetry domains (identity, device, network, behaviour) using a framework that explicitly represents epistemic uncertainty — distinguishing "trusted," "untrusted," and "insufficient evidence to determine."

**Requirement 2: Dynamic evidence weighting.** The resolution must automatically adjust the influence of each evidence source based on its observed reliability, discounting volatile or potentially compromised sources without requiring manual configuration.

**Requirement 3: Temporal decay.** The resolution must treat trust as a temporally depreciating asset, continuously reducing the evidentiary weight of authentication and prior observations as time passes, forcing reliance on fresh behavioural evidence.

**Requirement 4: Graduated access decisions.** The resolution must replace binary allow/deny logic with graduated thresholds that route uncertain entities into constrained access tiers proportionate to the residual uncertainty.

**Requirement 5: Detection-enforcement coupling.** The resolution must tightly couple trust evaluation with enforcement, translating continuous trust scores into real-time policy modifications.

### 8.3 The DCTA Ensemble Model as Candidate Resolution

The Dynamic Contextual Trust Architecture (DCTA) Ensemble Model is designed to satisfy these requirements through four interlocking mechanisms:

**Multi-domain evidential fusion via Dempster-Shafer theory.** The DCTA evaluates trust across four independent telemetry domains — Identity, Device, Network, and Application/Data — each producing its own basic probability assignment (BPA) over the binary frame of discernment $\Theta = \{Safe, Unsafe\}$. The Dempster-Shafer combination rule fuses evidence conjunctively, requiring concordant evidence across sources to produce high committed belief [38]. This conjunctive property ensures that no single domain's favourable assessment can override genuine risk signals from another domain — a mathematically enforceable implementation of the separation of privilege principle [41] that operates continuously rather than only at session establishment. Aaqib et al. [6] demonstrate the effectiveness of this approach in IoT systems, confirming that Dempster-Shafer fusion combined with multi-classifier ensemble learning produces robust trust assessments across heterogeneous device populations. The DS framework's explicit representation of epistemic uncertainty through $m(\Theta)$ — mass assigned to the full frame of discernment — provides the mathematical apparatus absent from all five paradigms (Requirement 1).

**Variance-based dynamic weighting.** Each domain's evidential authority is governed by a variance-driven weighting function $W_k = 1/(1 + \alpha \sigma_k^2)$, where $\sigma_k^2$ is the rolling variance of domain $k$'s trust scores and $\alpha > 0$ is the variance penalty amplifier. This mechanism directly addresses the data poisoning vulnerability: an attacker who forces artificially high trust scores simultaneously introduces variance into the historical signal, triggering weight suppression. Ji et al. [37] demonstrate that weighted fusion of evidence using unified trust distribution mechanisms is essential for preventing corruption of fused outputs — the DCTA's variance-based weighting implements precisely this principle. The vacuous identity property of Dempster's Rule ($m \oplus m_{\text{vacuous}} = m$) guarantees that a domain rendered vacuous by high variance is mathematically invisible in the fusion [42] (Requirement 2). Table 2 illustrates this dynamic.

**Table 2.** Domain weight dynamics under varying variance levels ($\alpha = 10$).

| Domain State | $\sigma^2$ | $W_{\text{raw}}$ | Effect on Fusion |
|:---|:---:|:---:|:---|
| Stable, well-instrumented | 0.01 | 0.909 | Near-full evidential commitment |
| Moderate jitter (BYOD) | 0.05 | 0.667 | One-third of evidence uncertain |
| High volatility (IoT sensor) | 0.10 | 0.500 | Half the evidence is uncertain |
| Suspected compromise | 0.25 | 0.286 | Domain nearly vacuous |

**Exponential temporal decay.** Trust is treated as a temporally depreciating asset via $D(t) = e^{-\lambda t/T}$, where $\lambda$ is the decay rate constant and $T$ is the session window duration. Wang et al. [43] establish the theoretical foundation for time decay-based dynamic trust models, demonstrating that exponential decay functions effectively capture the diminishing reliability of authentication signals over time. This mechanism directly resolves the temporal passport problem across all five paradigms (Requirement 3). The companion paper provides full formal treatment including dual sliding-window architecture and session lifecycle management.

**Graduated access via Pignistic transformation.** The continuous trust score maps to tiered access thresholds — Full Access ($BetP > 0.75$), Constrained Access ($0.45 \leq BetP \leq 0.75$), and No Access ($BetP < 0.45$) — replacing binary allow/deny with risk-proportionate access decisions. Jeong and Yang [29] validate this graduated approach through a trust score-based access control model for Zero Trust Architecture, demonstrating through sensitivity analysis and real-world performance evaluation that continuous trust scoring with graduated thresholds outperforms binary access models (Requirement 4).

### 8.4 Architectural Integration

The DCTA does not replace the five paradigms; it *completes* them. Table 3 maps the DCTA's mechanisms to the specific gaps each paradigm leaves open.

**Table 3.** DCTA architectural integration with existing paradigms.

| Paradigm Gap | DCTA Resolution Mechanism |
|:---|:---|
| Perimeter: no post-VPN verification | Temporal decay depreciates VPN authentication; multi-domain fusion detects post-auth compromise |
| RBAC: context-blindness, temporal passport | Four-domain contextual evaluation replaces single-dimension role check; decay eliminates temporal passport |
| NIST PE: unspecified Trust Algorithm | DS fusion + variance weighting + temporal decay = fully specified, mathematically tractable Trust Algorithm |
| SDP: post-authentication silence, binary trust | Continuous trust scoring fills the post-SPA gap; graduated thresholds replace binary Join/Leave |
| AI-IDS: data poisoning, detection-enforcement gap | Variance-based weighting discounts poisoned evidence; trust scores directly drive enforcement via PDP/PEP coupling |

### 8.5 Limitations

The following limitations constrain the scope and generalisability of this analysis:

1. **Analytical scope.** This paper provides a structured critical analysis and requirements specification rather than empirical validation. The DCTA Ensemble Trust Model is presented as a candidate resolution whose formal properties are argued to address the identified gaps. Empirical validation — including experimental evaluation across six canonical scenarios on a Mininet/SDN testbed — is reported in companion publications. The claims regarding breach containment, latency, and classification accuracy are supported by the companion testbed and simulation studies, not by the critical analysis presented here.

2. **Specification-level critique.** The five paradigms are analysed at the specification level (NIST SP 800-207 [1], CSA SDP v2.0 [27], published research papers) rather than from production deployment data. Implementation-specific mitigations — vendor-proprietary continuous monitoring add-ons, custom SIEM integrations, or organisation-specific RBAC extensions — may partially address the identified gaps in specific deployments without resolving the architectural absence at the specification level.

3. **Binary framing.** The DCTA model's frame of discernment is binary ($\Theta = \{Safe, Unsafe\}$). While this is sufficient for the three-tiered access classification presented, more granular risk categorisation (e.g., $\{Safe, Suspicious, Compromised\}$) may be required for advanced threat response workflows. Extension to multi-state frames is architecturally feasible but increases DS combination complexity.

4. **Adversarial adaptation.** The variance-based anti-spoofing mechanism addresses attackers who introduce detectable variance. Sophisticated adversaries capable of maintaining low variance while reporting fabricated — but stable — high trust scores (the "stable-but-false" attack) require complementary hardware attestation (TPM 2.0) for mitigation, which is outside the scope of this analysis.

5. **Paradigm selection.** The five paradigms were selected for their architectural significance and prevalence in the literature. Other relevant approaches — including blockchain-based authentication [16], SASE frameworks, and microsegmentation-only architectures — are acknowledged but not analysed in equivalent depth. Their inclusion would strengthen the comprehensiveness of the diagnostic but is unlikely to alter the central finding.

---

## 9. Conclusion

This paper has demonstrated, through structured critical analysis against four diagnostic criteria, that five ostensibly progressive security paradigms — perimeter defence, static RBAC, NIST SP 800-207, CSA SDP (Specification v2.0 and Architecture Guide), and AI-augmented IDS in SDN-governed heterogeneous networks — all share a common structural failure: the absence of continuous, temporally decaying, evidentially grounded trust evaluation during active sessions. This failure is not a residue of incomplete implementation but a structural property of architectures that treat trust as a binary, point-in-time determination.

Perimeter security assumes a defensible boundary that heterogeneous multi-cloud, BYOD, and IoT topologies have dissolved. Static RBAC assumes a stable workforce and device population that does not change within the lifetime of a session. NIST SP 800-207 mandates continuous trust evaluation but leaves the Trust Algorithm mathematically unspecified, creating an implementation vacuum. CSA SDP achieves rigorous session establishment through SPA and mTLS but provides no post-authentication trust management, creating an implicit trust period that grows with every second after the handshake. AI-augmented IDS in SDN introduces new adversarial attack surfaces — data poisoning, cumulative belief fusion corruption — while the SDN controller reproduces static RBAC's temporal passport at the architectural level.

The Dynamic Contextual Trust Architecture Ensemble Model bridges these gaps through four interlocking mechanisms: multi-domain Dempster-Shafer evidential fusion that explicitly represents epistemic uncertainty [38]; variance-based dynamic weighting that achieves native adversarial resilience through automatic evidence discounting [37]; exponential temporal decay that transforms authentication from a one-time gate into a continuously depreciating asset [43]; and graduated Pignistic-based access decisions that replace binary allow/deny logic with risk-proportionate, threshold-based access tiers [42]. The resulting architecture does not replace any of the five paradigms; it completes them — providing the mathematically specified, temporally dynamic, uncertainty-aware trust evaluation engine that each paradigm implicitly requires but none specifies.

---

## References

[1] Rose S, Borchert O, Mitchell S, Connelly S. NIST Special Publication 800-207 — Zero Trust Architecture. National Institute of Standards and Technology; 2020. https://doi.org/10.6028/NIST.SP.800-207

[2] IBM Security. Cost of a Data Breach Report 2024. IBM Corporation; 2024.

[3] CISA Advisory. PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Cybersecurity and Infrastructure Security Agency; 2024. https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

[4] Lefebvre M, Engels DW, Nair S. On SDPN: Integrating the Software-Defined Perimeter (SDP) and the Software-Defined Network (SDN) Paradigms. In: 2022 IEEE Conference on Communications and Network Security (CNS); 2022. p. 353–8. https://doi.org/10.1109/CNS56114.2022.9947267

[5] Buck C, Olenberger C, Schweizer A, Völter F, Eymann T. Never trust, always verify: A multivocal literature review on current knowledge and research gaps of zero-trust. Computers & Security 2021;110:102436. https://doi.org/10.1016/j.cose.2021.102436

[6] Aaqib M, Ali A, Chen L, Nibouche O. Behaviour-based trust assessment for the Internet of Things systems using multi-classifier ensemble learning and Dempster–Shafer fusion. Neural Computing and Applications 2025;37:22191–214. https://doi.org/10.1007/s00521-025-11273-8

[7] Verma S. Zero Trust Architecture in Cloud-Native Environments: Implementation Strategies & Best Practices. International Journal of Computer Trends and Technology 2025;73:102–7. https://doi.org/10.14445/22312803/IJCTT-V73I4P114

[8] Adorno J. Evolution of Secure Access: From VPN to SDP-Enabled Zero Trust Network Access (ZTNA). Zscaler; 2025. https://www.zscaler.com/blogs/product-insights/evolution-secure-access-vpn-sdp-enabled-zero-trust-network-access-ztna

[9] Lev E, Black J. From VPN to Zero Trust: Why It's Time to Retire Traditional VPNs, Part 2. Akamai; 2025. https://www.akamai.com/blog/security/vpn-zero-trust-time-retire-traditional-vpns-part-2

[10] Sandhu RS, Coyne EJ, Feinstein HL, Youman CE. Role-based access control models. IEEE Computer 1996;29(2):38–47. https://doi.org/10.1109/2.485845

[11] Das D, Walker A, Bushong V, Svacina J, Černý T, Matyas V. On automated RBAC assessment by constructing a centralized perspective for microservice mesh. PeerJ Computer Science 2021;7:e376. https://doi.org/10.7717/peerj-cs.376

[12] Iqal Z, Selamat A, Krejcar O. A comprehensive systematic review of access control in IoT: Requirements, technologies, and evaluation metrics. IEEE Access 2023;11:1–41. https://doi.org/10.1109/ACCESS.2023.3347495

[13] Meng L, Huang D, An J, Zhou X, Lin F. A continuous authentication protocol without trust authority for zero trust architecture. China Communications 2022;19:198–213. https://doi.org/10.23919/JCC.2022.08.015

[14] Nasiruzzaman M, Ali M, Salam I, Miraz D. The Evolution of Zero Trust Architecture (ZTA) from Concept to Implementation. In: Proc. IEEE IT Conference; 2025. p. 1–8. https://doi.org/10.1109/IT64745.2025.10930254

[15] Mohseni-Ejiyeh A. Zero Trust Real-Time Lightweight Access Control Protocol for Mobile Cloud-Based IoT Sensors. arXiv preprint arXiv:2309.01293v2; 2023.

[16] Pule B, Nleya B, Sibiya K. A Zero Trust Driven Federative Learning Algorithm for Privacy Enhancement. Applied Sciences 2026;16. https://doi.org/10.3390/app16083872

[17] Wang J, Yan Z, Wang H, Li T, Pedrycz W. A Survey on Trust Models in Heterogeneous Networks. IEEE Communications Surveys & Tutorials 2022;24:2127–62. https://doi.org/10.1109/COMST.2022.3192978

[18] Thirumalairai A, Pradeesh S. Probabilistic Trust Inference Theory to Optimizing Multi-Level Trust in Software Defined Networks. In: 2024 International Conference on System, Computation, Automation and Networking (ICSCAN); 2024. p. 1–7. https://doi.org/10.1109/ICSCAN62807.2024.10894307

[19] Syed NF, Shah SW, Shaghaghi A, Anwar A, Baig Z, Doss R. Zero Trust Architecture (ZTA): A Comprehensive Survey. IEEE Access 2022;10:57143–79. https://doi.org/10.1109/ACCESS.2022.3174679

[20] Wu X, Jing Z, Wang X. The security of IOT from the perspective of the observability of complex networks. Heliyon 2024;10. https://doi.org/10.1016/j.heliyon.2024.e27104

[21] Harshavardini S, Bertia A. A Software-Defined Zero Trust Framework for Secure Access Control and Microsegmentation using SDN and SDP. In: 2025 Fourth International Conference on Smart Technologies, Communication and Robotics (STCR); 2025. p. 1–7. https://doi.org/10.1109/STCR62650.2025.11020089

[22] Wang R, Li C, Zhang K, Tu B. Zero-trust based dynamic access control for cloud computing. Cybersecurity 2025;8. https://doi.org/10.1186/s42400-024-00320-x

[23] Jafri J, Amin SI, Rahman A, Mohd nor S. A systematic literature review of the role of trust and security on Fintech adoption in banking. Heliyon 2023;10:e22980. https://doi.org/10.1016/j.heliyon.2023.e22980

[25] Mekdad Y, Arış A, Babun L, El Fergougui A, Conti M, Lazzeretti R, et al. A survey on security and privacy issues of UAVs. Computer Networks 2023;224:109626. https://doi.org/10.1016/j.comnet.2023.109626

[27] Cloud Security Alliance. Software-Defined Perimeter (SDP) Specification v2.0; 2022.

[28] Moubayed A, Refaey A, Shami A. Software-Defined Perimeter (SDP): State of the Art Secure Solution for Modern Networks. IEEE Network 2019;33:226–33. https://doi.org/10.1109/MNET.2019.1800324

[29] Jeong E, Yang D. A Trust Score-Based Access Control Model for Zero Trust Architecture: Design, Sensitivity Analysis, and Real-World Performance Evaluation. Applied Sciences 2025;15:9551. https://doi.org/10.3390/app15179551

[30] Smiliotopoulos C, Kambourakis G, Kolias C. Detecting lateral movement: A systematic survey. Heliyon 2024;10. https://doi.org/10.1016/j.heliyon.2024.e26317

[31] Cloud Security Alliance. Software-Defined Perimeter: Architecture Guide V3. CSA Research; 2025.

[32] Cloud Security Alliance. Software-Defined Perimeter Architecture Guide; 2019.

[33] Lefebvre M, Nair S, Engels DW, Horne D. Building a Software Defined Perimeter (SDP) for Network Introspection. In: 2021 IEEE Conference on Network Function Virtualization and Software Defined Networks (NFV-SDN); 2021. p. 91–5. https://doi.org/10.1109/NFV-SDN53031.2021.9665152

[34] Pagadala-Sekar S. Integrating software defined perimeter and zero trust in platform engineering: A security framework for modern infrastructure. World Journal of Advanced Engineering Technology and Sciences 2025;15:357–79. https://doi.org/10.30574/wjaets.2025.15.2.0562

[35] Ali M, Hu Y-F, Luong DK, Oguntala G, Li J-P, Abdo K. Adversarial Attacks on AI based Intrusion Detection System for Heterogeneous Wireless Communications Networks. In: 2020 AIAA/IEEE 39th Digital Avionics Systems Conference (DASC); 2020. p. 1–6. https://doi.org/10.1109/DASC50938.2020.9256597

[37] Ji Z, Tian J, Chen H, Liu S. A new method for weighted fusion of evidence based on the unified trust distribution mechanism and the reward-punishment mechanism. Information Sciences 2023;629:798–815. https://doi.org/10.1016/j.ins.2023.02.010

[38] Shafer G. A Mathematical Theory of Evidence. Princeton University Press; 1976.

[39] Yan Q, Yu R, Gong Q, Li J. Software-Defined Networking (SDN) and Distributed Denial of Service (DDoS) Attacks in Cloud Computing Environments: A Survey, Some Research Issues, and Challenges. IEEE Communications Surveys & Tutorials 2015;18:602–36. https://doi.org/10.1109/COMST.2015.2487361

[41] Saltzer JH, Schroeder MD. The protection of information in computer systems. Proceedings of the IEEE 1975;63:1278–308.

[42] Jøsang A. Subjective Logic — A Formalism for Reasoning Under Uncertainty. Springer; 2016. https://doi.org/10.1007/978-3-319-42337-1

[43] Wang H, Jiang J, Li W. A Dynamic Trust Model Based on Time Decay Factor. In: 2018 IEEE SmartWorld, Ubiquitous Intelligence & Computing; 2018. p. 2048–51. https://doi.org/10.1109/SmartWorld.2018.00343
