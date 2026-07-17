# Additional Literature and Architectural Justifications for the Reproducible Testbed

> **Companion to:** *A Reproducible, Lightweight Zero Trust Testbed for Validating Dynamic Trust Models Based on Virtualization, Emulation, and Simulation*
> **Date:** 26 June 2026

---

## 1. Introduction

The reproducible testbed paper identifies six limitations (Section VII.E) constraining the generalisability of its results: emulated infrastructure, single-machine scale, a binary frame of discernment, simulated telemetry, adversarial evasion via stable-but-false attacks, and same-data hyperparameter selection. This companion document surveys six bodies of related work that address or contextualise these limitations, positioning the testbed within the broader Zero Trust research landscape and defining a concrete integration roadmap.

---

## 2. NIST SP 1800-35: From Abstract Architecture to Practice Guide

NIST SP 1800-35, *Implementing a Zero Trust Architecture*, was released as a final publication in June 2025 [R1]. Developed by the NCCoE with 24 industry partners, it provides 19 sample ZTA implementations built from commercial off-the-shelf (COTS) technologies, translating the abstract component model of SP 800-207 [R2] into deployable reference builds.

The DCTA testbed and SP 1800-35 share a common objective — instantiating the PDP/PA/PEP decomposition — but differ in scope and audience:

| Dimension | NIST SP 1800-35 | DCTA Testbed |
|:---|:---|:---|
| **Stack** | 19 vendor-specific COTS builds | Open-source (Keycloak, OPA, OVS, OpenDaylight) |
| **Trust computation** | Delegated to vendor-opaque engines | Transparent Ensemble Trust Engine |
| **Reproducibility** | Vendor licences required | Docker Compose on commodity hardware |
| **Scope** | Enterprise deployment guidance | Research algorithm validation |

SP 1800-35 validates the *operational feasibility* of Zero Trust; the DCTA testbed validates the *computational correctness* of the trust engine that sits at its core. The testbed's component mapping (Table I in the paper) can be cross-referenced against SP 1800-35's reference architecture, confirming structural compatibility between the open-source implementation and NIST's production-oriented builds [R1], [R2].

---

## 3. AI/ML-Based Dynamic Trust Evaluation

The Continuous Adaptive Risk and Trust Assessment (CARTA) framework mandates that trust scores be continuously recalculated from multi-domain telemetry rather than evaluated once at session initiation [R3]. AI and ML techniques operationalise CARTA through three mechanisms: (i) behavioural baselining via autoencoders and isolation forests [R4]; (ii) dynamic trust scoring through learned domain weightings, including reinforcement learning for adaptive threshold tuning [R5]; and (iii) predictive threat response via time-series anomaly models trained on historical attack patterns [R6].

The DCTA Ensemble Trust Engine occupies a deliberate position on this spectrum:

| Approach | Explainability | Data Dependency | Deployability |
|:---|:---|:---|:---|
| Static rule-based | Fully transparent | None | Trivial |
| **DCTA Ensemble** | **Fully transparent** | **Sliding window only** | **Single workstation** |
| ML-based (supervised) | Requires explanation layer | Labelled training data | GPU/training infrastructure |
| Deep RL-based | Black-box | Extensive interaction data | Significant compute |

The model's variance-based weighting ($w_d = 1/(1 + \alpha \sigma^2)$) achieves an effect functionally analogous to learned domain weighting — unstable signals are automatically suppressed — through a deterministic mechanism requiring no training data [R4]. This transparency is a deliberate architectural choice: in adversarial environments where training data may itself be poisoned, a formally verifiable decision logic offers a security advantage over opaque classifiers [R5], [R6].

The paper's Section VIII identifies adaptive $\alpha$ tuning via reinforcement learning as a future direction. The Ensemble model provides the provably correct baseline; a future ML layer would learn to adjust $\alpha$ per domain based on observed threat patterns, combining the current architecture's explainability with learned adaptability [R5].

---

## 4. Docker over Kubernetes: Architectural Justification

### 4.1 Rationale

The testbed uses Docker Compose as its orchestration layer. Kubernetes was evaluated and deliberately excluded for three reasons that are orthogonal to its production-scale merits [R7], [R8].

| Criterion | Docker Compose | Kubernetes |
|:---|:---|:---|
| **Deployment** | Single `docker compose up` | Cluster bootstrap, CNI, ingress controller |
| **Resources** | 8-core, 16 GB (commodity) | Control plane alone: 2–4 GB RAM |
| **Networking** | Docker bridge — transparent, inspectable | CNI overlay — VXLAN encapsulation, NAT |
| **Sidecar injection** | Not required | Service mesh injects per-pod proxies [R9] |
| **Mininet integration** | Direct OVS bridge attachment via veth | CNI conflicts with OVS bridge requirements |
| **Reproducibility** | Deterministic | Non-deterministic (cluster state, CNI version, injection timing) |

### 4.2 The Sidecar Problem

Kubernetes-based Zero Trust deployments enforce mTLS and per-request access control through sidecar proxies injected via mutating admission webhooks [R9]. This introduces: (i) resource overhead of 50–128 MB RAM per pod, consuming resources that should be allocated to trust computation; (ii) injection non-determinism that undermines the testbed's reproducibility guarantee; and (iii) CNI networking conflicts with Mininet's requirement for direct OVS bridge attachment [R8], [R10].

The industry is responding with sidecar-less alternatives — eBPF-based enforcement (Cilium) and ambient mesh architectures (Istio Ambient Mesh) — that eliminate per-pod proxies entirely [R10], [R11]. These approaches are discussed in Section 6.

### 4.3 Upward Compatibility

Docker validates the algorithm; Kubernetes deploys it at scale. The trust engine (Python), policy logic (Rego), and enforcement proxy (Envoy) are all Kubernetes-native components, ensuring the testbed's architecture is upwardly compatible with production orchestration when scaling beyond the single-workstation research environment [R7].

---

## 5. SPIFFE/SPIRE: Workload Identity

### 5.1 Overview

SPIFFE (Secure Production Identity Framework for Everyone) is a CNCF-graduated open standard (graduated August 2022) that defines how workloads are issued cryptographically verifiable identities — SPIFFE Verifiable Identity Documents (SVIDs), typically X.509 certificates or JWTs — without hardcoded secrets [R12], [R13]. SPIRE is the reference implementation, automating identity issuance, rotation, and verification through platform attestation: the SPIRE Agent verifies a workload's identity by inspecting kernel-level properties (PID, container ID, service account) rather than any presented credential [R12].

### 5.2 Relevance to the Testbed

The testbed uses Keycloak for human-centric identity (OIDC/SAML). SPIFFE/SPIRE would complement this by addressing machine identity — authenticating containerised services to each other via automated mTLS [R13]:

| Identity Scenario | Current (Keycloak) | With SPIFFE/SPIRE |
|:---|:---|:---|
| Human-to-service | ✅ OIDC/SAML + JWT | ✅ (unchanged) |
| Service-to-service mTLS | ❌ Manual certificates | ✅ Automated SVID rotation |
| Workload attestation | ❌ Not implemented | ✅ Kernel-level verification |

Integration would involve deploying SPIRE Server as a Docker container, configuring Envoy to obtain certificates via the SPIRE Workload API (SDS integration), and extending the Identity domain ($\mathcal{D}_I$) to incorporate attestation status as an additional trust signal [R12], [R13].

---

## 6. eBPF and Cilium: Kernel-Level Enforcement

### 6.1 Technology

Cilium, a CNCF-graduated project, uses eBPF (extended Berkeley Packet Filter) to enforce network security policies directly within the Linux kernel's data path [R10], [R14]. Unlike userspace proxies or iptables, eBPF programs are JIT-compiled, verified by the kernel, and operate at wire speed with sub-millisecond latency [R10].

In the Zero Trust context, Cilium provides three relevant capabilities: (i) identity-based enforcement using cryptographic workload identities rather than ephemeral IP addresses [R10]; (ii) sidecar-less architecture that eliminates per-pod proxy overhead — addressing the same problems motivating the testbed's Docker-over-Kubernetes decision (Section 4.2); and (iii) Layer 7 protocol inspection via eBPF parsers, enabling granular API-level policies without application-layer proxies [R14].

### 6.2 Tetragon: Runtime Security

Cilium's companion project, Tetragon, extends eBPF enforcement to process-level runtime security — detecting system call patterns indicative of compromise (file access, privilege escalation, anomalous network connections) with sub-microsecond overhead [R15]. This provides device posture telemetry directly mappable to the DCTA model's Device domain ($\mathcal{D}_D$).

### 6.3 Comparison

| Layer | DCTA Testbed (OVS + Envoy) | eBPF/Cilium |
|:---|:---|:---|
| **L3/L4** | OpenFlow rules on OVS | eBPF at TC/XDP |
| **L7** | Envoy WASM filter | eBPF protocol parsers |
| **Latency** | 2–5 ms (flow rule install) | Sub-millisecond (in-kernel) |
| **Mininet** | ✅ Direct OVS bridge | ⚠️ Requires Kubernetes CNI |

For production deployments, eBPF-based enforcement is the emerging standard [R10], [R14]. For single-workstation research, OVS + Envoy provides equivalent functional fidelity with direct Mininet integration. A future testbed iteration could replace OVS with Cilium while retaining the Ensemble Trust Engine — validating enforcement-agnostic portability.

---

## 7. Network Telemetry: Zeek and Suricata

### 7.1 The Telemetry Gap

The testbed generates simulated domain scores from controlled Gaussian distributions (Limitation 4, Section VII.E). Zeek and Suricata provide the two complementary approaches to real network telemetry collection [R16], [R17].

### 7.2 Complementary Roles

| Capability | Zeek | Suricata |
|:---|:---|:---|
| **Focus** | Visibility — structured protocol metadata | Detection — real-time threat identification |
| **Detection** | Behavioural anomaly via scripting [R16] | Signature matching and protocol anomaly [R17] |
| **Output** | Structured logs (conn, dns, ssl, http, files) | EVE JSON (alerts, flows, protocol data) |
| **Inline blocking** | No (passive observer) | Yes (IDS or IPS mode) |
| **Correlation** | Community ID for cross-tool linking | Community ID for cross-tool linking |

Zeek converts raw packets into high-fidelity session metadata — TLS handshake parameters, certificate chains, DNS queries, file hashes — producing the behavioural baselines required for trust evaluation [R16]. Suricata evaluates traffic against signature rule sets (ET Open, Emerging Threats Pro) for real-time threat identification, providing ground-truth anomaly labels against which the trust engine's classification accuracy can be independently validated [R17].

### 7.3 Integration Architecture

Deploying both tools on a Mininet mirror port (SPAN) would replace simulated telemetry with real network observation:

```
  Mininet (OVS) ──── Mirror/SPAN ──┬──── Zeek (passive) ──┐
                                    │                       │
                                    └── Suricata (IDS) ─────┤
                                                            ▼
                                              Telemetry Aggregator
                                                            │
                                              Ensemble Trust Engine
```

**Telemetry-to-domain mapping:**

| Source | DCTA Domain | Metric |
|:---|:---|:---|
| Zeek `conn.log` — connection patterns | Network ($\mathcal{D}_N$) | Protocol compliance |
| Zeek `ssl.log` — certificate/cipher analysis | Data ($\mathcal{D}_I$) | Encryption compliance |
| Zeek scripts — behavioural anomalies | Network ($\mathcal{D}_N$) | Anomaly detection score |
| Suricata alerts — signature matches | Network ($\mathcal{D}_N$) | Anomaly score (inverse severity) |
| Suricata flows — traffic baselines | Application ($\mathcal{D}_A$) | Behavioural consistency |

This integration directly addresses Limitation 4 and would validate whether variance-based weighting correctly suppresses noisy real-world signals — where consecutive observations exhibit temporal autocorrelation, unlike the simulation's i.i.d. assumption [R16], [R17].

---

## 8. Summary

| Technology | Testbed Layer | Current State | Extension |
|:---|:---|:---|:---|
| **NIST SP 1800-35** [R1] | Standards | SP 800-207 mapping | Cross-reference with 1800-35 builds |
| **AI/ML scoring** [R4]–[R6] | Trust Engine | Deterministic variance weighting | Adaptive $\alpha$ via RL |
| **Docker** [R7], [R8] | Orchestration | Docker Compose | K8s for production scale |
| **SPIFFE/SPIRE** [R12], [R13] | Identity | Keycloak (human IdP) | Machine identity + mTLS |
| **eBPF/Cilium** [R10], [R14] | Enforcement | OVS + Envoy | Kernel-level, sub-ms |
| **Zeek + Suricata** [R16], [R17] | Telemetry | Simulated Gaussian | Real network metadata + IDS |

Each technology addresses a specific limitation identified in the paper while preserving the testbed's design principles: open-source, reproducible, and lightweight.

---

## References

[R1] National Institute of Standards and Technology, "Implementing a Zero Trust Architecture," NIST SP 1800-35, June 2025. doi: 10.6028/NIST.SP.1800-35.

[R2] S. Rose, O. Borchert, S. Mitchell, and S. Connelly, "Zero Trust Architecture," NIST SP 800-207, Aug. 2020. doi: 10.6028/NIST.SP.800-207.

[R3] Gartner, "Market Guide for Zero Trust Network Access (ZTNA)," Gartner Research, 2024.

[R4] K. Alsubhi, A. S. Aljohani, and A. Aljuhani, "Machine learning-based approach for evaluating zero trust security architecture," *Applied Sciences*, vol. 14, no. 2, p. 642, Jan. 2024.

[R5] W. Zhang, J. Li, and P. Zhao, "AI-driven multi-domain trust fusion for mitigating insider threats in hybrid cloud environments," *Comput. Security*, vol. 142, 103856, 2025.

[R6] X. Li and Y. Wang, "AI-driven behavioral analysis and dynamic session aging for zero trust architectures," *J. Inf. Security Applications*, vol. 77, 103554, 2025.

[R7] E. Gilman, D. Barth, R. Rais, and C. Morillo, *Zero Trust Networks: Building Secure Systems in Untrusted Networks*, 2nd ed. Sebastopol, CA: O'Reilly Media, Apr. 2024.

[R8] S. Prabhakaran, V. Rajagopal, and M. Kumar, "Mininet-based SDN testbeds for zero trust evaluation: A survey," in *Proc. IEEE Int. Conf. Network Softwarization*, pp. 112–119, 2024.

[R9] R. Goyal, S. Sharma, and P. Kaur, "Software-defined networking for micro-segmentation in zero trust environments," *IEEE Access*, vol. 12, pp. 34521–34536, 2024.

[R10] Isovalent/Cilium Project, "Cilium: eBPF-based Networking, Observability, and Security," Cloud Native Computing Foundation, 2025. [Online]. Available: https://cilium.io

[R11] Istio Project, "Introducing Ambient Mesh," 2024. [Online]. Available: https://istio.io/latest/blog/2024/ambient-reaches-ga/

[R12] SPIFFE Project, "SPIFFE: Secure Production Identity Framework for Everyone," Cloud Native Computing Foundation, 2022. [Online]. Available: https://spiffe.io

[R13] E. Gilman, D. Barth, R. Rais, and C. Morillo, *Zero Trust Networks*, 2nd ed. O'Reilly, 2024, ch. 6 ("Trusting Compute").

[R14] M. Vieira and L. Deri, "eBPF-based network security monitoring: Opportunities and challenges," in *Proc. IEEE Symp. Computers and Communications (ISCC)*, 2023, pp. 1–6.

[R15] Isovalent, "Tetragon: eBPF-based Security Observability and Runtime Enforcement," 2025. [Online]. Available: https://tetragon.io

[R16] Zeek Project, "The Zeek Network Security Monitor," 2025. [Online]. Available: https://zeek.org

[R17] Open Information Security Foundation, "Suricata: Open Source IDS/IPS/NSM Engine," 2025. [Online]. Available: https://suricata.io

[R18] Cybersecurity and Infrastructure Security Agency, "Zero Trust Maturity Model Version 2.1," Department of Homeland Security, 2024.
