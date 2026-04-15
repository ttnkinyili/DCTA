# Journal Paper Proposals from the DCTA Thesis

> Based on a comprehensive review of all project files — Python simulation engines, test results across 6 scenarios, 15+ thesis-level discussion documents, the ZTA testbed architecture, and the full thesis outline — five top-tier journal papers are identified below. Each leverages a distinct, publishable contribution from the thesis.

---

## Paper 1 — Flagship / Systems Paper

### Title
**An Ensemble Trust Architecture for Continuous Zero Trust Enforcement: Fusing Dempster-Shafer Evidence Theory with Dual-Horizon Temporal Decay**

### Target Journals
| Tier | Journal | IF (2024) | Fit Rationale |
|:---|:---|:---:|:---|
| Q1 | *IEEE Transactions on Information Forensics and Security* | 6.8 | Core venue for trust models, access control, and formal security |
| Q1 | *IEEE Transactions on Dependable and Secure Computing* | 7.0 | Emphasises dependability and continuous verification |
| Q1 | *Computers & Security* | 5.6 | Strong ZTA community; rapid turnaround |

### Core Contribution
The **Ensemble Trust Model** that hybridises short-term data freshness (30-min exponential window) with long-term behavioural inertia (48-hr exponential window) via Dempster-Shafer weighted belief fusion. The claim — *trust has momentum* — is validated through simulation across 6 heterogeneous scenarios and a containerised SDP/SDN testbed.

### Proposed Outline

1. **Introduction** — The "implicit trust period" vulnerability; gap between authentication event and session reality
2. **Related Work** — NIST SP 800-207 trust algorithm, CSA SDP Spec v2.0, static vs. dynamic RBAC, temporal decay in access control
3. **System Architecture**
   - Four-pillar evaluation domains (Identity, Device, Network, Application)
   - Variance-based dynamic weighting → DS mass function construction
   - Dempster's combination rule and Pignistic probability
   - Dual-horizon ensemble formula: $T = W_{short} \cdot T_{instant} + (1 - W_{short}) \cdot T_{history} \cdot D_{long}$
4. **Temporal Dynamics**
   - Linear vs. exponential decay: formal analysis
   - Three-phase lifecycle: Initialisation → Handover → Maturity
   - Trust threshold architecture: full / limited / deny with hysteresis
5. **Testbed Implementation**
   - Docker + LXC + Mininet topology; OpenDaylight SDN, Keycloak IdP, OPA PDP, Envoy PEP
   - SDP join/leave workflows mapped to trust engine
6. **Evaluation**
   - 6 scenarios: Corporate Office, Remote VPN, Public Wi-Fi, BYOD, Untrusted Device + Geofence, Compromised Device
   - Model progression: No Policy → Single-Domain → Hierarchical → Base DS → Linear Decay → Exponential Decay → Ensemble
   - Metrics: detection latency, false-positive rate, session effective TTL, adversarial survival time
7. **Discussion** — Contextual grey-area routing; security–usability trade-off; CARTA alignment
8. **Conclusion & Future Work**

### Key Data Sources
- [ensemble_trust_simulator.py](file:///Users/admin/Desktop/DCTA/ensemble_trust_simulator.py), [run_ensemble_scenarios.py](file:///Users/admin/Desktop/DCTA/run_ensemble_scenarios.py)
- [test_results_Ensemble/](file:///Users/admin/Desktop/DCTA/test_results_Ensemble) (belief evolution plots, CSV data)
- [thesis_evaluation_of_models.md](file:///Users/admin/Desktop/DCTA/thesis_evaluation_of_models.md), [thesis_discussion_ensemble.md](file:///Users/admin/Desktop/DCTA/thesis_discussion_ensemble.md)

---

## Paper 2 — Theoretical Foundations Paper

### Title
**Probabilistic Trust Aggregation in Zero Trust Architectures: A Nested Bernoulli-Binomial Framework with Dempster-Shafer Mass Construction**

### Target Journals
| Tier | Journal | IF (2024) | Fit Rationale |
|:---|:---|:---:|:---|
| Q1 | *Information Fusion* | 18.6 | Premier venue for evidential reasoning and DS theory |
| Q1 | *Information Sciences* | 8.1 | Strong probability theory + CS audience |
| Q1 | *Artificial Intelligence* | 14.4 | Formal uncertainty reasoning |

### Core Contribution
The **hierarchical probabilistic pipeline** from Bernoulli facets → Binomial domain proportions → Nested composite → DS mass functions → Pignistic access decisions. Formally proves the variance cascade (3-stage attenuation), Beta-Binomial regularisation during initialisation, and the closed-form connection between binomial variance and dynamic weight suppression.

### Proposed Outline

1. **Introduction** — Trust as a probabilistic inference problem; limitations of deterministic scoring
2. **Preliminaries** — Bernoulli trials, Binomial/Poisson-Binomial distribution, DS theory basics
3. **Stage 1: Facets as Bernoulli Variables**
   - 16 concrete facets across 4 domains (table from thesis)
   - Weighted facet aggregation ($w_{k,j}$)
4. **Stage 2: Domain Scores as Binomial Proportions**
   - Homogeneous vs. Poisson-Binomial (heterogeneous) case
   - Variance: $\text{Var}(S_k) = p_k(1-p_k)/n_k$
5. **Stage 3: Nested Composite**
   - Weighted sum of independent binomial proportions
   - Double-attenuation variance proof
   - Connection to portfolio diversification (Markowitz, 1952)
6. **Stage 4: DS Mass Construction from Binomial Variance**
   - Variance → weight $W_k = 1/(1 + \alpha\sigma^2_k)$
   - Weight → mass: $m(\{Safe\}) = S_k \cdot W_k$, $m(\Theta) = 1 - W_k$
   - Self-calibrating uncertainty: erratic domains → vacuous mass
7. **Stage 5: Beta-Binomial Regularisation**
   - Conjugate Beta prior for initialisation-phase smoothing
   - Overdispersion property → conservative trust during data scarcity
8. **Numerical Example & Sensitivity Analysis**
   - Worked end-to-end example (Corporate VPN scenario)
   - Per-facet failure sensitivity: $\Delta S = -W_k / n_k$
9. **Conclusion**

### Key Data Sources
- [thesis_bernoulli_binomial_trust.md](file:///Users/admin/Desktop/DCTA/thesis_bernoulli_binomial_trust.md) (29 KB, 421 lines — complete manuscript-ready content)
- [ds_utils.py](file:///Users/admin/Desktop/DCTA/ds_utils.py), [weighted_belief_fusion.py](file:///Users/admin/Desktop/DCTA/weighted_belief_fusion.py)

---

## Paper 3 — Temporal Dynamics / Evidence Discounting Paper

### Title
**Trust Decay as Continuous Verification: Exponential Evidence Discounting, Sliding Windows, and Graduated Thresholds for Zero Trust Sessions**

### Target Journals
| Tier | Journal | IF (2024) | Fit Rationale |
|:---|:---|:---:|:---|
| Q1 | *IEEE Transactions on Network and Service Management* | 4.7 | Session management, policy enforcement |
| Q1 | *Journal of Network and Computer Applications* | 7.7 | Applied networking + security |
| Q1 | *ACM Computing Surveys* | 16.6 | Comprehensive survey + formal treatment (if expanded) |

### Core Contribution
The formal treatment of **trust as a depreciating asset**: exponential decay within the DS discounting framework, dual sliding-window architecture (30-min + 48-hr), forgetting factors, three-phase session lifecycle (Initialisation → Handover → Maturity), and **graduated trust thresholds** (full / constrained / deny) with hysteresis and dynamic calibration.

### Proposed Outline

1. **Introduction** — The "implicit trust period" as the root cause of session hijacking; trust's temporal dimension
2. **Background** — EWMA in signal processing; Bayesian evidence discounting; DS mass redistribution
3. **Linear vs. Exponential Decay**
   - Formal comparison: $D_{lin}(t) = \max(0, 1 - t/T)$ vs. $D_{exp}(t) = e^{-\lambda t}$
   - Residual weight at midpoint: 50% (linear) vs. 22% (exponential at λ = 0.1)
   - Architectural implications for high-security vs. low-risk enclaves
4. **DS Evidence Discounting**
   - Discounted BPA: $m_\alpha(A) = \alpha \cdot m(A)$; $m_\alpha(\Theta) = 1 - \alpha(1 - m(\Theta))$
   - Asymptotic convergence to vacuous mass
5. **Dual Sliding-Window Architecture**
   - Short-term (30 min): captures acute anomalies
   - Long-term (48 hr): captures chronic patterns
   - Forgetting factor $\alpha \in (0,1)$ and weight sequences
6. **Trust Thresholds and Decision Architecture**
   - Three-tier access: $\tau_{full}$, $\tau_{deny}$, constrained zone
   - Hysteresis: $\delta_{up}$, $\delta_{down}$ margins
   - Dynamic calibration via SIEM/threat intelligence
   - Resource-differentiated and temporal threshold modulation
7. **Simulation Results**
   - Comparative session TTL analysis across 6 scenarios
   - Linear vs. exponential effective session lengths
8. **Conclusion**

### Key Data Sources
- [trust_decay_discussion.md](file:///Users/admin/Desktop/DCTA/trust_decay_discussion.md) (33 KB, comprehensive treatment)
- [Linear_Exponential_comparison.md](file:///Users/admin/Desktop/DCTA/Linear_Exponential_comparison.md)
- [test_results_time/](file:///Users/admin/Desktop/DCTA/test_results_time), [test_results_time_exp/](file:///Users/admin/Desktop/DCTA/test_results_time_exp) (comparative data)
- [thesis_discussion_time.md](file:///Users/admin/Desktop/DCTA/thesis_discussion_time.md), [thesis_discussion_time_exp.md](file:///Users/admin/Desktop/DCTA/thesis_discussion_time_exp.md)

---

## Paper 4 — Critical Review / Position Paper

### Title
**Beyond the Perimeter: Why Static RBAC, Software-Defined Perimeters, and AI-Augmented Detection Fail Without Dynamic Trust in Heterogeneous Networks**

### Target Journals
| Tier | Journal | IF (2024) | Fit Rationale |
|:---|:---|:---:|:---|
| Q1 | *IEEE Communications Surveys & Tutorials* | 35.6 | Definitive venue for comprehensive surveys and critiques |
| Q1 | *ACM Computing Surveys* | 16.6 | Broad CS audience; theoretical depth |
| Q1 | *Computer Science Review* | 12.9 | Integrative reviews |

### Core Contribution
A **unified critical analysis** demonstrating that perimeter security, static RBAC, CSA SDP (Spec v2.0 + Architecture Guide), NIST SP 800-207 trust algorithm, and AI-augmented IDS in SDN-governed heterogeneous networks all share a common structural failure: the absence of **continuous, temporally decaying, evidentially grounded trust evaluation**. Positions the DCTA Ensemble Model as the architectural resolution.

### Proposed Outline

1. **Introduction** — The persistence of implicit trust across all contemporary architectures
2. **The Dissolution of the Perimeter**
   - Topology arguments: multi-cloud, BYOD, IoT, edge
   - VPN credential inheritance and lateral movement data (IBM, 2024)
3. **Static RBAC: Structural Inadequacy**
   - Role explosion in heterogeneous environments
   - Context-blindness: same role, different risk contexts
   - Temporal passport problem: authentication as one-time gate
4. **Critique of NIST SP 800-207**
   - §3 Logical Components: PE/PA/PEP gaps
   - §4 Deployment scenarios: underspecified heterogeneous guidance
   - §5 Threats: acknowledged but unmitigated temporal vulnerabilities
5. **Critique of CSA SDP**
   - Spec v2.0: SPA replay window, mTLS certificate lifecycle, IoT computational overhead
   - Architecture Guide: Controller centralisation, binary trust (Join/Leave), thundering herd
   - The post-authentication trust management gap
6. **Adversarial Fragility of AI-IDS in SDN**
   - Data poisoning and cumulative belief fusion corruption (Ali et al., 2024)
   - SDN controller as static-RBAC-at-scale
   - Detection without enforcement: incomplete security posture
7. **The Common Thread: The Dynamic Trust Imperative**
   - Mapping each failure to the missing continuous trust evaluation
   - DCTA as the architectural bridge
8. **Conclusion**

### Key Data Sources
- [perimeter_rbac_failure.md](file:///Users/admin/Desktop/DCTA/perimeter_rbac_failure.md) (23 KB)
- [thesis_lit_review_addition.md](file:///Users/admin/Desktop/DCTA/thesis_lit_review_addition.md) (70 KB — SDP + NIST critiques)
- [ai_ids_sdn_critique.md](file:///Users/admin/Desktop/DCTA/ai_ids_sdn_critique.md) (20 KB)
- [thesis_literature_critiques.md](file:///Users/admin/Desktop/DCTA/thesis_literature_critiques.md) (57 KB)

---

## Paper 5 — Applied / Testbed Paper

### Title
**A Lightweight Zero Trust Testbed for Validating Dynamic Trust Models in Software-Defined Enterprise Networks**

### Target Journals
| Tier | Journal | IF (2024) | Fit Rationale |
|:---|:---|:---:|:---|
| Q1 | *Journal of Systems Architecture* | 5.6 | Systems integration, testbed design |
| Q1 | *Future Generation Computer Systems* | 7.5 | SDN/cloud/edge testbed validation |
| Q2 | *SoftwareX* | 3.4 | Open-source tools and reproducible experiments |

### Core Contribution
The **end-to-end testbed design** that bridges theoretical trust algorithms with operational SDP/SDN enforcement. Demonstrates that identity-aware SDP controllers can synchronise with network-layer SDN fabrics using containerised microservices (Docker + LXC + Mininet), achieving 2.1 ms policy evaluation latency across 25 active nodes.

### Proposed Outline

1. **Introduction** — The gap between ZTA theory and operational validation; need for reproducible testbeds
2. **Design Principles**
   - Resource-constrained philosophy: commodity hardware, open-source stack
   - Decoupling trust engine from enforcement gateways
   - Automated orchestration vs. manual configuration
3. **Architecture**
   - Network layer: Open vSwitch + OpenDaylight (SDN controller, port 6653/8181)
   - Identity layer: Keycloak (IdP, OIDC/SAML, port 8080)
   - Policy layer: Open Policy Agent (Rego, port 8182)
   - Enforcement layer: Envoy Proxy (L7 PEP, port 10000)
   - Emulation layer: Mininet (custom topologies)
4. **Trust Engine Integration**
   - Python-based DS fusion engine feeding OPA policies
   - 4-domain telemetry → trust score → OPA input → Envoy enforcement
   - SDP join/leave lifecycle mapped to trust thresholds
5. **Validation Experiments**
   - Baseline (pre-policy) vs. policy-enforced connectivity
   - Static multi-domain → dynamic DS → temporal decay → ensemble
   - 6 scenarios: corporate, VPN, Wi-Fi, BYOD, geofence, compromised
   - Performance metrics: latency, throughput, policy evaluation time
6. **Reproducibility & Lessons Learned**
   - State synchronisation fragility between SDP and SDN layers
   - Heartbeat/reconciliation thread necessity (30-sec polling)
   - Containerisation overhead and namespace isolation challenges
7. **Conclusion & Open-Source Release**

### Key Data Sources
- [README.md](file:///Users/admin/Desktop/DCTA/README.md) (full setup guide)
- [test_results/](file:///Users/admin/Desktop/DCTA/test_results), [test_results_Ensemble/](file:///Users/admin/Desktop/DCTA/test_results_Ensemble) (all CSV + PNG visualisations)
- [thesis_conclusions.md](file:///Users/admin/Desktop/DCTA/thesis_conclusions.md) (testbed validation summary + performance data)
- All Python engines: [dynamic_trust_weighting.py](file:///Users/admin/Desktop/DCTA/dynamic_trust_weighting.py), [ensemble_trust_simulator.py](file:///Users/admin/Desktop/DCTA/ensemble_trust_simulator.py), [weighted_belief_fusion.py](file:///Users/admin/Desktop/DCTA/weighted_belief_fusion.py)

---

## Summary Matrix

| # | Paper | Core Innovation | Top Target | Readiness |
|:---:|:---|:---|:---|:---:|
| 1 | Ensemble Trust Architecture | Dual-horizon DS fusion + ensemble model | *IEEE TIFS* | ★★★★☆ |
| 2 | Bernoulli-Binomial Trust Pipeline | Nested probabilistic hierarchy → DS mass | *Information Fusion* | ★★★★★ |
| 3 | Trust Decay & Thresholds | Exponential discounting + graduated access | *IEEE TNSM* | ★★★★☆ |
| 4 | Critical Review / Position | Unified critique: RBAC + SDP + NIST + AI-IDS | *IEEE COMST* | ★★★★☆ |
| 5 | Testbed Validation | Reproducible SDP/SDN ZTA testbed | *J. Sys. Arch.* | ★★★☆☆ |

> **Readiness Legend:** ★★★★★ = manuscript-ready content; ★★★★☆ = requires restructuring/reformatting; ★★★☆☆ = additional experiments or data needed.

### Recommended Authorship Strategy
- **Papers 1 & 2** should be submitted first — they carry the thesis's strongest novel contributions
- **Paper 4** can be submitted in parallel as a survey/position paper (different audience)
- **Paper 3** can be extracted after Paper 1 is accepted, to avoid self-overlap
- **Paper 5** is best published after Papers 1–2, so the testbed validates an already-published model
