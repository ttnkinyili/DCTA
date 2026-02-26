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
