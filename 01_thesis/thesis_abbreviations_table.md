# List of Abbreviations and Acronyms

| Abbreviation | Full Term |
| :--- | :--- |
| **AAL** | Authenticator Assurance Level |
| **ABAC** | Attribute-Based Access Control |
| **ACM** | Association for Computing Machinery |
| **AD** | Active Directory |
| **AGI** | Artificial General Intelligence |
| **AI** | Artificial Intelligence |
| **AiTM** | Adversary-in-the-Middle |
| **APT** | Advanced Persistent Threat |
| **BYOD** | Bring Your Own Device |
| **CARTA** | Continuous Adaptive Risk and Trust Assessment |
| **CAT** | Continuous Adaptive Trust |
| **CDE** | Cardholder Data Environment |
| **CIO** | Chief Information Officer |
| **CISA** | Cybersecurity and Infrastructure Security Agency |
| **CLI** | Command Line Interface |
| **CPU** | Central Processing Unit |
| **CRQC** | Cryptanalytically Relevant Quantum Computers |
| **CSA** | Cloud Security Alliance |
| **CVSS** | Common Vulnerability Scoring System |
| **DB** | Database |
| **DCTA** | Dempster-Shafer Theory of Evidence (also Dynamic Context-Aware Trust Architecture) |
| **DLP** | Data Loss Prevention |
| **DoD** | Department of Defense |
| **DS** | Dempster-Shafer |
| **DSS** | Data Security Standard |
| **DTMS** | Decentralized Trust Management Systems |
| **EC** | Elliptic Curve |
| **EDR** | Endpoint Detection and Response |
| **FHE** | Fully Homomorphic Encryption |
| **FIDO** | Fast Identity Online |
| **GB** | Gigabyte |
| **HMAC** | Hash-based Message Authentication Code |
| **HMP** | Hierarchical Multi-domain Policy |
| **HR** | Human Resources |
| **IBM** | International Business Machines |
| **ID** | Identity |
| **IdP** | Identity Provider |
| **IDS** | Intrusion Detection System |
| **IEEE** | Institute of Electrical and Electronics Engineers |
| **IoMT** | Internet of Medical Things |
| **IoT** | Internet of Things |
| **IP** | Internet Protocol |
| **IT** | Information Technology |
| **KEM** | Key Encapsulation Mechanism |
| **KMSI** | Keep Me Signed In |
| **KVM** | Kernel-based Virtual Machine |
| **LAN** | Local Area Network |
| **LTS** | Long-Term Support |
| **LXC** | Linux Containers |
| **MAC** | Media Access Control |
| **MDM** | Mobile Device Management |
| **MFA** | Multi-Factor Authentication |
| **MITM** | Man-In-The-Middle |
| **ML** | Machine Learning |
| **ML-KEM** | Module-Lattice-Based Key-Encapsulation Mechanism |
| **NIH** | National Institutes of Health |
| **NIST** | National Institute of Standards and Technology |
| **ODL** | OpenDaylight |
| **OPA** | Open Policy Agent |
| **OS** | Operating System |
| **OTP** | One-Time Password |
| **OVS** | Open vSwitch |
| **OWASP** | Open Web Application Security Project |
| **PC** | Personal Computer |
| **PCI** | Payment Card Industry |
| **PDP** | Policy Decision Point |
| **PEP** | Policy Enforcement Point |
| **PHY** | Physical Layer |
| **PQC** | Post-Quantum Cryptography |
| **PWC** | PricewaterhouseCoopers |
| **QEMU** | Quick Emulator |
| **RAM** | Random Access Memory |
| **RASP** | Runtime Application Self-Protection |
| **RBAC** | Role-Based Access Control |
| **RCE** | Remote Code Execution |
| **RF** | Random Forest |
| **RSA** | Rivest-Shamir-Adleman |
| **SASE** | Secure Access Service Edge |
| **SDN** | Software-Defined Networking |
| **SDP** | Software-Defined Perimeter |
| **SDPN** | Software-Defined Perimeter Networks |
| **SIEM** | Security Information and Event Management |
| **SMS** | Short Message Service |
| **SOAR** | Security Orchestration, Automation, and Response |
| **SP** | Special Publication (e.g., NIST SP) |
| **SPA** | Single Packet Authorization |
| **SSO** | Single Sign-On |
| **TCP** | Transmission Control Protocol |
| **TEE** | Trusted Execution Environment |
| **TLS** | Transport Layer Security |
| **TTL** | Time-To-Live |
| **UI** | User Interface |
| **UX** | User Experience |
| **VM** | Virtual Machine |
| **VPN** | Virtual Private Network |
| **WFH** | Work From Home |
| **XAI** | Explainable AI |
| **XR** | Extended Reality |
| **ZKP** | Zero-Knowledge Proof |
| **ZTA** | Zero Trust Architecture |
| **ZTNA** | Zero Trust Network Access |
| **ZTO** | Zero Trust Orchestration |

## Operational Definition of Terms

*   **Adaptive Routing (Gray-Area Routing)**: Within Software-Defined Perimeters (SDP), this is the dynamic orchestration of network traffic where connections are not strictly binary (allow/deny). Instead, based on degrading trust continuous assessments, sessions are dynamically rerouted into restricted, highly monitored "gray-area" VLANs or enclaves to contain potential adversarial lateral movement (Oprea et al., 2025).
*   **Algorithmic Suspicion (Trust Continuum)**: The operational philosophy of the Continuous Adaptive Risk and Trust Assessment (CARTA) framework. It discards the binary "trusted/untrusted" state, instead placing all network entities on a fluctuating *Trust Continuum* where mathematically formalized suspicion (uncertainty) is continuously quantified based on real-time metadata (Premier Science, 2024). 
*   **Continuous Adaptive Risk and Trust Assessment (CARTA)**: A strategic cybersecurity framework that mandates the continuous, real-time evaluation of all users, devices, and network behaviors to make contextual, adaptive access decisions, rather than relying on static, one-time authentication (Trio.so, 2025).
*   **Dempster-Shafer Theory of Evidence (DCTA)**: A mathematical theory of belief functions used within this thesis's trust evaluation model to calculate operational uncertainty and fuse disparate, conflicting telemetry signals (e.g., Identity, Device, Network) into a single, cohesive trust metric (Fan & Li, 2024). 
*   **Ensemble Trust Model**: The specific algorithmic architecture proposed in this research, which hybridizes deterministic cryptographic gating with probabilistic behavioral analysis to trap adversaries within a continuous, stateful matrix of historical behavioral inertia (Barchart, 2024).
*   **Evidential Fusion**: The algorithmic process of combining multiple streams of contextual security data (telemetry) to generate a comprehensive, probabilistic assessment of an entity's operational trustworthiness or risk level (Chen et al., 2025).
*   **Historical Inertia (Trust Momentum)**: The conceptual mechanism by which a user or device's long-term history of verified, safe network behavior acts as a stabilizing weight against sudden, anomalous telemetry spikes. High historical inertia prevents a single dropped packet or minor anomaly from causing catastrophic revocation of access, ensuring systemic stability (MDPI, 2024).
*   **Network Metadata / Contextual Signals**: The continuous stream of non-payload data generated by an entity during a session. In this thesis, it is categorized into four specific domains: Identity Context, Device Posture, Network Variance, and Application Sensitivity (IEEE Communications Society, 2024).
*   **Software-Defined Networking (SDN)**: A network architecture approach that decouples the network control and forwarding functions, enabling the network control to become directly programmable and the underlying infrastructure to be abstracted for applications and network services (IEEE Communications Society, 2024).
*   **Software-Defined Perimeter (SDP)**: A security framework, popularized by the Cloud Security Alliance, that establishes dynamic, one-to-one network connections between users and authorized resources, adhering to a "zero trust" model where identities and device posture are verified before access is granted, effectively making applications invisible to unauthorized entities (Cloud Security Alliance, 2025).
*   **Spatial Model**: Within Zero Trust, a formal, multi-tiered structure utilized to monitor the physical and logical location hierarchies of users and devices, integrating with temporal constraints to dictate localized access rights (CSDP, 2025).
*   **Temporal Decay (Data Freshness / Sliding Window)**: The mathematical algorithm utilized to validate the recency (*Data Freshness*) of telemetry. It employs *Sliding Windows* to systematically penalize or reduce a previously established trust score over time, ensuring that idle or unverified authorizations expire according to a parameterized rate (linear or exponential) to minimize adversarial dwell time (Al-Tariq et al., 2025).
*   **Zero Trust Architecture (ZTA)**: An enterprise cybersecurity architecture based on zero trust principles, fundamentally operating under the assumption that no actor, system, network, or service operating outside or within the security perimeter is trusted without continuous verification (National Institute of Standards and Technology, 2025).

## Scope, Limitations, and Delimitations

### Scope of the Study
This thesis investigates the mathematical transition of Zero Trust Architectures (ZTA) from static, binary access control (Implicit Trust models) to continuous, stateful methodologies. The primary scope encompasses the design, algorithmic modeling, and empirical simulation of an "Ensemble Trust Model," which integrates Dempster-Shafer (DS) evidential fusion with distinct Temporal Decay algorithms (Linear and Exponential) (Al-Tariq et al., 2025; Fan & Li, 2024). The research evaluates the efficacy of this hybridized continuous assessment against simulated adversarial paradigms, including lateral movement, session hijacking, and "noisy" environmental constraints across four logical telemetry domains (Identity, Device, Network Variance, and Application Sensitivity). Validation is confined to a virtualized, multi-node enterprise testbed orchestrating containerized microservices (Docker/LXC) atop Software-Defined Perimeters (SDP) and Software-Defined Networking (SDN) protocols.

### Limitations of the Study
Due to the constraints of the emulated environment and the theoretical nature of the algorithmic models, several inherent limitations apply to this research:
1.  **Computational Overhead in Deep Edge Scenarios**: The Dempster-Shafer evidential fusion engine, while highly accurate, incurs computational costs that may induce latency if deployed linearly on resource-constrained Internet of Things (IoT) or edge devices without cryptographic offloading or Federated Learning optimizations (Xu, 2024). 
2.  **Containerized Emulation vs. Physical Hardware**: The testbed validation relies on containerized microservices and virtual networking (Mininet, OVS). While structurally rigorous for algorithm testing, it does not fully replicate the physical hardware variances, kernel-level bootkit threats, or the massive scale (10,000+ nodes) of a live, corporate-wide Software-Defined Perimeter deployment.
3.  **Algorithmic Determinism vs. Human Unpredictability**: While the "Historical Inertia" protocols accurately baseline uniform operational cadences, the variance models ($\alpha$) may struggle to differentiate between erratic but legitimate human anomalies (e.g., unpredictable mobile workforce switching networks rapidly) and sophisticated evasion tactics without the deeper semantic context provided by true Cognitive architectures.

### Delimitations of the Study
To maintain focus and academic rigor, the following parameters explicitly bound the execution of this research:
1.  **Vendor Agnosticism**: The research deliberately eschews the evaluation or benchmarking of proprietary, commercial "Zero Trust" vendor products (e.g., specific Cisco, Palo Alto, or Zscaler implementations). The focus remains strictly on the underlying mathematical algorithms, SDP/SDN open-source protocols, and structural architectures (Alawida et al., 2024; Smith & Jones, 2025).
2.  **Exclusion of Legacy Protocol Security**: This study assumes a baseline modernization of the simulated enterprise network. It does not address the securing of highly inherited legacy systems (e.g., mainframe architectures or protocols predating TLS 1.3) within the CARTA framework, focusing instead on cloud-native and micro-segmented topologies (Turner & O'Connor, 2024).
3.  **Cryptographic Primaries**: While acknowledging the necessity of secure authentication (e.g., FIDO2), the thesis does not exhaustively design new foundational cryptographic identity verification standards or Post-Quantum Cryptographic key exchanges, assuming such access primitives (Initial 'Freshness') are handled by existing, compliant Identity Providers (IdP) (Grassi et al., 2025; Williams, 2025).

## References
Al-Mutairi, A., & Hassan, R. (2024). Integrating SDN and Zero Trust Architecture for robust cloud environments: A review. *Computers and Security*, 136, 103550.

Al-Tariq, M., Hossain, M. S., & Atiquzzaman, M. (2025). Hybrid trust architectures for securing cyber-physical systems and enterprise networks. *IEEE Communications Surveys & Tutorials, 27*(1), 54-82.

Alawida, M., Oqaily, A., Halboob, W., & Abutair, H. (2024). A comprehensive survey on zero trust architecture (ZTA): Concepts, components, and implementation. *IEEE Access*, 12, 4526-4550.

Appgate. (2024). *The state of Zero Trust and SDP operational deployment*. Appgate Cybersecurity Research.

Barchart. (2024). *Artificial intelligence in cybersecurity: Next-generation threat detection using machine learning baselines*. Barchart Research.

Chen, X., et al. (2025). Trust management schemes for user authentication in IoT based on Dempster-Shafer Evidence Theory. *IEEE Internet of Things Journal, 12*(3), 2134-2148.

Chen, Y., Wang, L., & Zhao, H. (2025). Distributed Zero Trust framework leveraging Software-Defined Perimeter protocols for IoT environments. *Journal of Network and Computer Applications*, 215, 103628.

Cloud Security Alliance. (2024). *Software-Defined Perimeter (SDP) Specification v2.0: Implementation and Best Practices in Modern ZTA*. Cloud Security Alliance.

Cloud Security Alliance. (2025). *Software-Defined Perimeter: Architecture Guide V3*. CSA Research.

CSDP. (2025). *Spatial model of the adaptive security profile against dynamic cyber threats*. Cyber Security and Data Protection Conference.

Davidson, R. (2025). Agentic communication and fail-safe logic in autonomous zero trust frameworks. *Journal of Cybersecurity and Privacy*, 5(1), 112-128.

Fan, Y., & Li, M. (2024). Data-centric trust evaluation based on Dempster-Shafer theory for distributed systems. *IEEE Transactions on Information Forensics and Security, 19*, 45-56.

Grassi, P. A., Garcia, M. E., & Fenton, J. L. (2025). *Digital Identity Guidelines: Authentication and Lifecycle Management* (NIST Special Publication 800-63B-4). National Institute of Standards and Technology.

IEEE Communications Society. (2024). Security challenges and threat mitigation strategies in Software-Defined Networking architectures. *IEEE Communications Surveys & Tutorials, 26*(1), 112-140.

Johnson, M. (2024). *Zero Trust Evolution: Migrating from Legacy VPNs to Dynamic SDP Entitlements*. Information Security Journal, 33(4), 405-420.

Lefebvre, M., Engels, D. W., & Nair, S. (2023). On SDPN: Integrating the Software-Defined Perimeter (SDP) and the Software-Defined Network (SDN) Paradigms. *IEEE Communications Magazine*, 61(2), 55-61.

MDPI. (2024). *Sliding Window-Based Trust Correction in secure computing environments to track client trust fluctuations*. MDPI Research.

National Institute of Standards and Technology. (2025). *Implementing a Zero Trust Architecture* (NIST Special Publication 1800-35). U.S. Department of Commerce.

Oprea, O., et al. (2025). Adaptive routing systems within Zero Trust Network Access environments. *IEEE Security & Privacy*.

Oqaily, A., Alawida, M., & Halboob, W. (2024). Operational metrics and latency analysis of Zero Trust Architecture deployments. *IEEE Security & Privacy*, 22(4), 18-29.

Premier Science. (2024). *The Trust Continuum: Dynamic variable modeling in cybersecurity environments*. Premier Science Publications.

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2024). *Advancing Zero Trust Architecture: Lessons Learned from NIST SP 800-207 Implementations*. NIST Cybersecurity Whitepaper.

Shin, D., Kim, J., & Lee, S. (2025). A generalized framework for optimizing context-aware trust algorithms in Zero Trust Architecture. *Computers & Security*, 148, 104112.

Smith, J. (2024). Overcoming Controller bottlenecks in Gateway-to-Gateway Software-Defined Perimeters. *Journal of Network and Systems Management*, 32(3), 45-62.

Smith, J., & Jones, A. (2025). Zero Trust 2.0: A systematic review of architectural advancements from 2020 to 2025. *Security and Communication Networks*, 2025.

Trio.so. (2025). *CARTA: An Overview of Gartner's Continuous Adaptive Risk and Trust Assessment*. Trio Security.

Turner, L., & O'Connor, P. (2024). Secure by design: Embedding "deny-first" and fail-safe defaults in cloud-native applications. *IEEE Security & Privacy*, 22(3), 34-42.

Williams, T. (2025). Passwordless authentication and NIST compliance: The rise of FIDO2 in enterprise Zero Trust validation. *International Journal of Information Security*, 24(2), 215-230.

Xu, J. (2024). Trust algorithm optimization in Zero Trust architectures utilizing federated learning and SDN. *Journal of Information Security and Applications*, 80, 103681.

---

## Scope, Limitations, and Delimitations – Claude

### 1. Scope of the Study

This study is situated within the broader domain of Zero Trust Architecture (ZTA) and investigates the mathematical viability of transitioning enterprise access control from static, binary authentication paradigms to continuous, stateful trust evaluation. Specifically, the research designs, implements, and empirically validates an Ensemble Trust Model that integrates Dempster-Shafer (DS) evidential fusion with temporal decay algorithms to enforce Continuous Adaptive Risk and Trust Assessment (CARTA) across heterogeneous network environments (National Institute of Standards and Technology, 2025; Trio.so, 2025).

The scope of the algorithmic investigation spans six progressively complex trust architectures: Implicit Trust (No Policy), Single-Domain Criteria, Hierarchical Multi-Domain Policy, Dynamic Variance-Based Weighted Belief Fusion, Fused Dynamic Weighting with Linear Temporal Decay, Fused Dynamic Weighting with Exponential Temporal Decay, and the culminating Ensemble Trust Model that hybridizes short-term cryptographic freshness with long-term behavioral inertia (Al-Tariq et al., 2025). Each model is evaluated against its capacity to mitigate lateral movement, session hijacking, Advanced Persistent Threats (APTs), and insider data exfiltration across four independent telemetry domains: Identity Context, Device Posture, Network Variance, and Application/Data Sensitivity (Chen et al., 2025; Fan & Li, 2024).

The empirical validation is conducted through a virtualized enterprise testbed orchestrating containerized microservices (Docker and LXC) atop a Software-Defined Networking (SDN) fabric utilizing Open vSwitch (OVS) and Mininet, governed by Software-Defined Perimeter (SDP) controllers that enforce programmatic access decisions via OpenFlow protocols (Lefebvre et al., 2023; Cloud Security Alliance, 2024). The testbed simulates nine distinct adversarial scenarios spanning corporate, remote, public Wi-Fi, BYOD, and fully compromised contexts, with configurable parameters including initial trust scores, observation window lengths, variance sensitivity thresholds ($\alpha$), and temporal decay rates ($\lambda$). Trust calculations employ the Pignistic Probability transformation (BetP) to convert Dempster-Shafer belief intervals into actionable, threshold-based access decisions mapped to three tiers: Full Access ($T > 0.75$), Limited Access ($0.45 \le T \le 0.75$), and No Access ($T < 0.45$) (Shin et al., 2025).

### 2. Limitations of the Study

Several inherent limitations constrain the generalizability and operational applicability of the findings presented in this research.

First, the Dempster-Shafer combination rule, while mathematically rigorous for fusing independent evidence, incurs computational complexity that scales combinatorially with the number of focal elements and active domains. In the binary trust frame ($\Theta = \{\text{Safe}, \text{Unsafe}\}$) employed in this thesis, the three focal elements per domain produce manageable nine-product combinations per pairwise fusion. However, extending this framework to richer multi-state frames—as would be necessary for granular role-based classifications in large-scale enterprise deployments—would significantly increase the computational overhead of each evaluation epoch. This presents a material constraint for resource-limited edge and Internet of Medical Things (IoMT) environments where latency budgets are measured in single-digit milliseconds (Xu, 2024; Chen et al., 2025).

Second, the testbed validation, while structurally rigorous for algorithmic evaluation, relies entirely on containerized virtualization and synthetic telemetry data. The Docker/LXC/Mininet topology successfully maintains 2.1ms latencies across 25 active nodes and faithfully emulates the logical separation of control and data planes via SDN. However, containerized environments do not reproduce the full spectrum of physical hardware vulnerabilities, including kernel-level rootkits, firmware-based bootkits, side-channel attacks on shared CPU caches, or the electromagnetic interference patterns encountered in industrial operational technology (OT) environments. Furthermore, the 25-node testbed does not replicate the concurrency pressures of enterprise-scale deployments governing tens of thousands of simultaneous sessions, where Policy Decision Point (PDP) bottlenecks and state synchronization latencies between distributed SDP controllers become operationally critical (Smith, 2024; Oqaily et al., 2024).

Third, the variance-based dynamic weighting mechanism ($W_d = \frac{1}{1 + \alpha \cdot \sigma^2}$), while effective at discounting erratic or potentially spoofed telemetry, operates on a purely statistical basis without semantic understanding. The sensitivity parameter $\alpha$ governs how aggressively the engine penalizes signal instability, but it cannot intrinsically distinguish between benign human unpredictability—such as a mobile employee rapidly transitioning between cellular, Wi-Fi, and VPN connections during a commute—and the deliberate injection of variance by an adversary probing the system's detection thresholds. The current architecture lacks the cognitive or machine-learning-driven semantic layer that would be required to contextually interpret the *cause* of behavioral deviation, rather than merely its statistical magnitude (Barchart, 2024; Shin et al., 2025).

Fourth, the temporal decay parameters—specifically the 30-minute short-term session ($T_{short}$) aligned with NIST SP 800-63B AAL2 inactivity thresholds and the 48-hour long-term session ($T_{long}$) modeled on enterprise KMSI patterns—are calibrated against general corporate risk profiles. These parameterizations may require significant recalibration for sector-specific deployments. Financial institutions governed by PCI DSS v4.0 may require 15-minute absolute TTLs, while critical infrastructure environments under NIST AAL3 mandates may require 12-hour maximum session ceilings, fundamentally altering the Freshness-Inertia equilibrium of the Ensemble model (Grassi et al., 2025; Williams, 2025).

Finally, while the Dempster-Shafer framework explicitly models epistemic uncertainty through the mass assigned to the frame of discernment ($m(\Theta)$), the research does not incorporate mechanisms for detecting or mitigating deliberate adversarial manipulation of the uncertainty channel itself. A sophisticated attacker who understands the variance-discounting architecture could theoretically inject precisely calibrated noise to force specific domains into vacuous states ($W_k \approx 0$), thereby removing those domains from the fusion consensus and reducing the system to a fewer-domain evaluation that may be easier to subvert (Davidson, 2025).

### 3. Delimitations of the Study

The following boundaries were deliberately imposed to maintain methodological coherence and academic focus.

This research is explicitly vendor-agnostic. It does not evaluate, benchmark, or compare proprietary commercial Zero Trust platforms such as those offered by Cisco, Palo Alto Networks, Zscaler, or Microsoft Entra ID. The investigation focuses exclusively on the underlying mathematical algorithms governing trust computation—specifically Dempster-Shafer evidential fusion, variance-based dynamic weighting, and temporal decay functions—and their interoperability with open-source SDP and SDN protocols. This decision ensures that the findings are architecturally transferable and not constrained by the implementation-specific limitations or licensing boundaries of any single vendor ecosystem (Alawida et al., 2024; Smith & Jones, 2025).

The study deliberately excludes the design of novel cryptographic primitives. While the Ensemble Trust Model relies on the integrity of the initial authentication event (the "Freshness" component at $t=0$), the research assumes that foundational identity verification—including multi-factor authentication, FIDO2 hardware token validation, and certificate-based device attestation—is performed by compliant, standards-conformant Identity Providers (IdP) external to the trust evaluation engine. Similarly, while the thesis acknowledges the emerging necessity of Post-Quantum Cryptography (PQC) and module-lattice-based key encapsulation mechanisms (ML-KEM) for preserving the cryptographic integrity of SDP tunnels, the design and analysis of these cryptographic schemes falls outside the scope of the trust computation research (Grassi et al., 2025; Williams, 2025).

The simulated enterprise environment assumes a baseline level of network modernization. The testbed does not model the integration of the Ensemble Trust Model with legacy mainframe systems, pre-TLS 1.3 protocols, or flat network topologies that lack fundamental micro-segmentation capabilities. The research presupposes that the target deployment environment supports SDN-capable switching infrastructure, containerized or virtualized workloads, and programmatic policy enforcement via SDP controllers—characteristics consistent with cloud-native or hybrid-cloud enterprise architectures (Turner & O'Connor, 2024; Johnson, 2024).

The adversarial threat models evaluated in this research are confined to six canonical scenarios: Corporate Office, Remote/VPN, Public Wi-Fi, BYOD/Untrusted Device, Compromised Endpoint, and Advanced Persistent Threat with session hijacking. While these scenarios comprehensively cover the most prevalent attack vectors in heterogeneous enterprise environments, the study does not extend to the evaluation of supply-chain attacks, hardware implant vectors, or state-sponsored quantum-enabled cryptanalysis. These exclusions reflect the temporal and methodological boundaries of the current research phase and are identified as future research directions (Cloud Security Alliance, 2025; Rose et al., 2024).

Finally, the study confines its evaluation to mathematical simulation and algorithmic emulation. It does not include a live pilot deployment within an operational enterprise network, nor does it incorporate user experience (UX) studies measuring the friction imposed by continuous re-authentication challenges on workforce productivity. The operational usability of the Ensemble model's aggressive temporal decay in real-world conditions—particularly the balance between security enforcement and employee satisfaction—remains an empirical question requiring dedicated field trials beyond the scope of this thesis (Appgate, 2024; Oqaily et al., 2024).
