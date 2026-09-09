# PhD Thesis Defense — Full Presentation Content

## Evaluating Zero Trust Models Through Evidential Fusion and Temporal Dynamics in Heterogeneous Enterprise Networks

---

## SLIDE 1 — Title Slide

**Title:** Evaluating Zero Trust Models Through Evidential Fusion and Temporal Dynamics in Heterogeneous Enterprise Networks

**Candidate:** [Your Name]
**Supervisors:** [Supervisor Names]
**Institution:** [University Name]
**Date:** [Defense Date]

> **Speaker Notes:** Good [morning/afternoon], distinguished panel members, colleagues, and guests. My name is [Name], and today I present my doctoral research on developing a mathematically rigorous trust computation framework for Zero Trust Architecture. This work addresses a critical gap at the intersection of evidential reasoning, temporal dynamics, and enterprise network security.

---

## SLIDE 2 — The Cybersecurity Landscape: Why This Matters Now

**Visual:** Timeline/infographic showing perimeter collapse + key statistics

**Content:**
- The traditional network perimeter has dissolved
  - 60%+ of enterprise workloads now operate across hybrid/multi-cloud environments
  - Remote work, BYOD, and ephemeral cloud infrastructure have rendered "castle-and-moat" architectures obsolete
- **The financial imperative:**
  - Organizations with mature Zero Trust architectures reduce breach costs by **>$1 million per incident** (IBM Security, 2024)
- **The regulatory mandate:**
  - NIST SP 800-207 (2020) — the foundational Zero Trust standard
  - CISA Zero Trust Maturity Model v2.1 (2024)
  - DoD Zero Trust Strategy (2022) — mandates ZTA across all federal systems by 2027

> **Speaker Notes:** The cybersecurity landscape has undergone a fundamental transformation. The traditional perimeter — the firewall protecting an internal "trusted" network — has collapsed under the weight of remote work, BYOD policies, and cloud-native infrastructure. This is not a theoretical concern. IBM's 2024 Cost of a Data Breach Report demonstrates that organisations deploying mature Zero Trust architectures reduce breach costs by over one million dollars per incident. Governments have responded: NIST SP 800-207, CISA's Maturity Model, and the U.S. Department of Defense all now mandate Zero Trust adoption. The question is no longer *whether* to deploy Zero Trust, but *how to compute trust rigorously and continuously*.

---

## SLIDE 3 — The Problem: The Implicit Trust Period

**Visual:** Diagram showing authentication event → durable session → attack window

**Content:**
- Current ZTA implementations treat authentication as a **discrete, binary event**
- Once authenticated → session access is **durable and unquestioned**
- This creates the **"Implicit Trust Period"** — an operational runway for:
  - ⚠️ Advanced Persistent Threats (APTs) — lateral movement under valid tokens
  - ⚠️ Session hijacking — adversary inherits unexpired trust
  - ⚠️ Insider exfiltration — "low and slow" data theft under established identity
- **The critical gap in standards:**
  - NIST SP 800-207 specifies input variables (Identity, Device, Behaviour) but **leaves the Trust Algorithm's internal mechanics abstracted**
  - CSA SDP v2.0 provides excellent session initiation but **treats trust as binary post-perimeter**

> **Speaker Notes:** Despite the proliferation of Zero Trust frameworks, current implementations suffer from a critical structural deficiency I term the "Implicit Trust Period." Authentication remains a discrete, binary event. Once a user passes the gate, they receive durable session access — creating an operational runway for sophisticated adversaries. An attacker who steals a valid session token inherits that trust unchallenged. A compromised device continues operating under its pre-breach trust level. Critically, neither NIST SP 800-207 nor the Cloud Security Alliance's SDP v2.0 prescribes *how* to actually compute, decay, or fuse trust signals. They define *what* to evaluate but leave the algorithmic calculus entirely abstracted. This is the gap my thesis addresses.

---

## SLIDE 4 — The Convergent Research Gap

**Visual:** Four-quadrant diagram with the gap at centre

**Content:**
No existing work simultaneously addresses:

| Gap Dimension | What's Missing |
|:---|:---|
| **1. Evidential Uncertainty** | Existing probabilistic models (Bayesian, HMM, POMDP) assume complete priors — operationally untenable. No explicit representation of "I don't know." |
| **2. Temporal Depreciation** | Trust computed at discrete time points. No mathematical mechanism for continuous session decay. |
| **3. Multi-Domain Conflict** | Single-domain evaluations vulnerable to context spoofing. No inter-domain inconsistency detection. |
| **4. Enforcement-Agnostic Computation** | Enforcement mechanisms (SDP, SASE) assume trust scores arrive from an unspecified external source. |

**The convergent gap:** The *architecture* and *standards* of Zero Trust are mature; the *algorithmic calculus* is nascent.

> **Speaker Notes:** My literature review identified four interlocking gap dimensions that no single existing contribution addresses holistically. First, existing probabilistic approaches — Bayesian inference, Hidden Markov Models, POMDPs — all assume complete prior distributions over the trust domain, which is operationally untenable when sensor availability is intermittent and attacker models are unknown. Second, there is a near-universal absence of mathematically rigorous temporal decay — trust is computed at discrete points without enforcing session ephemerality. Third, single-domain trust evaluations remain vulnerable to context spoofing — an attacker compromising one domain presents fabricated metrics that a single-domain model cannot detect. Fourth, enforcement mechanisms like SDP and SASE provide the "last mile" but include no native trust computation engine. These four gaps converge into the precise research problem this thesis resolves.

---

## SLIDE 5 — Research Objectives

**Content:**

### Primary Objective
Develop and empirically evaluate a progression of six computational trust models, advancing from static access control to a novel **Ensemble Trust Model** grounded in Dempster-Shafer theory of evidence.

### Sub-Objectives
1. **Formally model trust** as a continuously depreciating, probabilistically computed quantity across four independent domains (Identity, Device, Network, Application)
2. **Develop dynamic variance-based weighting** that mathematically discounts unreliable or erratic telemetry sources
3. **Integrate temporal dynamics** — both linear and exponential decay — to enforce session ephemerality
4. **Hybridise short-term data freshness with long-term behavioural inertia** in the Ensemble Trust Model
5. **Validate empirically** through a reproducible, containerised testbed across six heterogeneous threat scenarios

> **Speaker Notes:** The primary objective of this research is to develop and empirically evaluate a progression of six computational trust models. These advance systematically from static, perimeter-based access control through multi-domain evidential fusion to a novel Ensemble Trust Model grounded in Dempster-Shafer theory. The sub-objectives decompose this into five measurable targets: formally modelling trust as a probabilistic, continuously depreciating quantity; developing the dynamic variance-based weighting mechanism; integrating temporal decay functions; hybridising freshness with behavioural inertia; and validating everything through a reproducible testbed.

---

## SLIDE 6 — Research Questions

**Content:**

| # | Research Question |
|:---:|:---|
| **RQ1** | Can evidential fusion coupled with temporal decay effectively neutralise lateral movement and session hijacking compared to legacy models? |
| **RQ2** | Does variance-based dynamic weighting reduce false-positive lockouts while maintaining security in heterogeneous environments? |
| **RQ3** | Can the Ensemble Trust Model balance aggressive security with operational continuity — resolving the security–usability tension? |

### Hypothesis
> The Ensemble Trust Model, by hybridising short-term Dempster-Shafer spatial fusion with long-term temporal behavioural inertia, will eliminate the implicit trust period, achieve proportional session degradation, and reduce false-positive lockouts compared to static and single-temporal models.

> **Speaker Notes:** These research questions are testable and the hypothesis is falsifiable. RQ1 asks whether evidential fusion with temporal decay can neutralise the specific attack vectors — lateral movement and session hijacking — that exploit the implicit trust period. RQ2 examines whether variance-based weighting actually reduces the false-positive lockouts that plague real-world deployments without sacrificing security. RQ3 addresses the fundamental tension: can we be both aggressively secure and operationally usable? The hypothesis predicts that the Ensemble Model achieves all three.

---

## SLIDE 7 — Literature Positioning: Trust Computation Landscape

**Visual:** Taxonomy table of existing approaches

**Content:**

| Approach | Limitation for ZTA |
|:---|:---|
| Bayesian (PTIT-ELO) | Requires complete prior distributions |
| Hidden Markov (HMM-BMS) | Requires complete prior distributions |
| POMDP belief states | Requires complete prior distributions |
| Markov chain (TrustS) | Requires complete prior distributions |
| **Dempster-Shafer Theory** | ✅ Explicit uncertainty via unprojected mass m(Θ) |

**Why DS Theory?**
- Explicitly represents "I don't have enough evidence to decide" — without forcing uniform priors
- The unprojected mass m(Θ) is a first-class mathematical object representing epistemic uncertainty
- **Gap:** Existing DS applications are limited to single-domain evaluations

**This thesis:** Four-domain DS fusion where Dempster's combination rule detects inter-domain conflict (κ) — transforming network heterogeneity from a liability into a defensive asset.

> **Speaker Notes:** Among the probabilistic approaches surveyed, each imposes a critical assumption: the availability of complete prior distributions. In heterogeneous enterprise networks where sensor availability is intermittent and attacker models are unknown, this is operationally untenable. Dempster-Shafer theory resolves this constraint by providing explicit uncertainty representation through unprojected belief mass — the mathematical capacity to say "I do not have enough evidence to decide." However, existing DS applications in cybersecurity remain limited to single-domain evaluations. This thesis extends DS theory into a four-domain fusion architecture where Dempster's combination rule actively detects inter-domain conflict, turning the network's heterogeneity from a vulnerability into a strength.

---

## SLIDE 8 — Standards vs. Algorithms: The Gap This Thesis Fills

**Visual:** Bridge diagram — Standards on one side, Algorithms on the other, thesis as the bridge

**Content:**
- **NIST SP 800-207:** Specifies *what* to evaluate — Identity Assurance, Device Posture, Behavioural Signals — but **not how to weight, synthesise, or decay them**
- **CSA SDP v2.0:** Excellent session initiation (SPA, multi-stage posture) but **trust becomes binary post-perimeter**
- **Enforcement mechanisms** (SDP, SASE, micro-segmentation): Provide the "last mile" but assume trust scores arrive from an external, unspecified source

### This thesis bridges the gap:
**Architecture** (SDP/NIST) ←→ **Algorithm** (DS fusion + temporal decay + variance weighting)

> **Speaker Notes:** The architecture and standards of Zero Trust are highly mature. What remains nascent is the algorithmic calculus required to manage dynamic trust across time, domains, and enforcement substrates. This thesis serves as the mathematical bridge. It provides the missing trust algorithm that standards like NIST 800-207 mandate but do not prescribe.

---

## SLIDE 9 — Research Methodology

**Visual:** Methodology flowchart

**Content:**
- **Approach:** Design Science Research — iterative development and evaluation of computational artefacts
- **Six progressively sophisticated trust models** evaluated systematically
- **Four independent evidentiary domains:**

| Domain | What It Evaluates | Example Telemetry |
|:---|:---|:---|
| **Identity** | *Who* is requesting access | MFA strength, login behaviour, AD compliance |
| **Device** | *What* is making the request | MDM status, patch level, EDR signals |
| **Network** | *Where* the request originates | IP reputation, geolocation, connection type |
| **Application** | *What* is being accessed | Data sensitivity, app integrity, access patterns |

- **Mathematical pipeline:** Bernoulli random variables → binomial proportions → variance → dynamic weights → DS mass functions → belief fusion → pignistic transform → temporal integration

> **Speaker Notes:** I employed a Design Science Research approach, iteratively developing and evaluating computational artefacts. Trust evaluation spans four independent domains aligned with the NIST SP 800-207 pillars: Identity, Device, Network, and Application. Each domain's binary compliance facets are modelled as Bernoulli observations. These feed into a binomial proportion that generates the domain score, which is then processed through the variance-based dynamic weighting mechanism, converted into Dempster-Shafer mass functions, fused via Dempster's combination rule, and transformed into actionable trust scores via the pignistic transform.

---

## SLIDE 10 — The Mathematical Engine: Core Equations

**Visual:** Three equations with annotations

**Content:**

### 1. Dynamic Variance-Based Weighting
$$W_d = \frac{1}{1 + \alpha \cdot \sigma_d^2}$$
- High variance (erratic behaviour) → weight drops → domain influence suppressed
- $\alpha$ = variance sensitivity parameter (recommended: 5.0 enterprise, ≥10.0 critical)

### 2. Dempster-Shafer Mass Functions
$$m'_d(\text{Safe}) = W_d \cdot m_d(\text{Safe})$$
$$m'_d(\Theta) = 1 - W_d \quad \text{(Uncertainty)}$$
- Explicit mathematical representation of incomplete evidence

### 3. The Ensemble Trust Formula
$$T_{ensemble} = \underbrace{W_{short}(t) \cdot T_{instant}}_{\text{Freshness}} + \underbrace{(1 - W_{short}(t)) \cdot T_{prev} \cdot D_{long}(\Delta t)}_{\text{Inertia}}$$
- $W_{short}(t) = e^{-3.0 \cdot t/30}$ — 30-minute freshness decay
- $D_{long}(\Delta t) = e^{-\lambda \cdot \Delta t}$ — 48-hour inertia decay

> **Speaker Notes:** The mathematical engine rests on three pillars. First, dynamic variance-based weighting — the domain weight is inversely proportional to its signal variance. A stable sensor carries full authority; an erratic sensor is mathematically discounted. Second, these weights feed Dempster-Shafer mass functions where uncommitted weight becomes explicit Uncertainty — the system can formally say "I don't know" without defaulting to either trust or distrust. Third, the Ensemble formula hybridises short-term spatial freshness with long-term behavioural inertia, governed by tunable exponential decay parameters calibrated against NIST and PCI DSS compliance baselines.

---

## SLIDE 11 — Testbed Architecture

**Visual:** Network topology diagram showing all components

**Content:**

| Component | Role | Technology |
|:---|:---|:---|
| **SDN Controller** | Policy Administrator | OpenDaylight (port 8181) |
| **Identity Provider** | Trust Anchor | Keycloak (OIDC/SAML) |
| **Policy Engine** | Decision Point (PDP) | Open Policy Agent (Rego) |
| **Application Proxy** | Enforcement Point (PEP) | Envoy Proxy (L7) |
| **Network Fabric** | Microsegmentation | Mininet + Open vSwitch |
| **State Store** | Sliding window / history | Redis 7.x |

### Six Canonical Threat Scenarios:
1. Corporate Office (high trust, stable)
2. Remote VPN (moderate jitter)
3. Public Wi-Fi (chaotic network)
4. BYOD (device asymmetry)
5. Untrusted Device + Geofence Violation
6. Compromised Endpoint (systemic failure)

**Scale:** 25 active nodes | **Latency:** 2.1 ms policy evaluation

> **Speaker Notes:** The testbed integrates six open-source components into a containerised stack. OpenDaylight serves as the SDN controller, Keycloak provides identity management, Open Policy Agent evaluates trust policies written in Rego, and Envoy Proxy enforces access decisions at the application layer. The entire network topology is emulated via Mininet with Open vSwitch, allowing precise control of network conditions. Six canonical threat scenarios — ranging from a pristine corporate office to a fully compromised endpoint — provide the evaluation framework. The testbed demonstrated 2.1-millisecond policy evaluation latency across 25 active nodes.

---

## SLIDE 12 — The Six-Model Progression

**Visual:** Horizontal evolution diagram with arrows

**Content:**

```
Model 1          Model 2           Model 3              Model 4
Implicit    →    Single-Domain  →  Static Multi-Domain → Dynamic DS
Trust             Criteria          (Fixed Weights)       Fusion
(No Policy)                                               (Variance)

    Model 5                              Model 6
→   Temporal Decay                  →    ENSEMBLE
    (Linear / Exponential)               (Freshness + Inertia)
    ★ NOVEL CONTRIBUTION                 ★★ FLAGSHIP CONTRIBUTION
```

**The narrative arc:** Each model resolves a deficiency exposed by its predecessor:
- No Policy → vulnerable to everything
- Single-Domain → vulnerable to context spoofing
- Static Multi-Domain → vulnerable to "low and slow" attacks
- Dynamic DS Fusion → resolves noise but blind to time
- Temporal Decay → aggressive security but excessive friction
- **Ensemble → resolves the security–usability paradox**

> **Speaker Notes:** The thesis evaluates six models in a deliberate progression. Each model resolves a specific deficiency exposed by its predecessor, creating a clear narrative of architectural evolution. We begin with implicit trust — essentially no policy — and demonstrate its catastrophic vulnerability. Single-domain criteria improve this but remain fragile to context spoofing. Static multi-domain models collect more evidence but treat it with fixed weights, creating durational passports. My first novel contribution — dynamic variance-based DS fusion — resolves the noisy sensor problem but remains blind to time. Adding temporal decay enforces session ephemerality but creates excessive operational friction. The Ensemble Trust Model — my flagship contribution — resolves this tension by hybridising freshness with behavioural inertia.

---

## SLIDE 13 — Static Models: Why They Fail

**Visual:** Results table + trust trajectory plots showing failures

**Content:**

### Model 1: Implicit Trust (No Policy)
- Unchecked lateral movement after any single compromise
- Flat network topology = ransomware propagation runway

### Model 2: Single-Domain Criteria
- AiTM attack defeats identity-only verification
- Cannot reconcile conflicting signals across domains

### Model 3: Static Multi-Domain (Fixed Weights)
- Chaotic public Wi-Fi weighted equally with stable corporate LAN
- **False-positive rate: 28.4%**
- **Classification accuracy: 71.8%**
- Conflict detection: K = 0.18 (low sensitivity)
- Zero resistance to session hijacking, insider threats, spoofing

> **Speaker Notes:** The static models fail categorically. Implicit trust creates an existential vulnerability — once any single endpoint is compromised, the attacker has unchecked lateral mobility. Single-domain models improve this but are defeated by adversary-in-the-middle attacks since they cannot cross-reference identity evidence against device or network context. Static multi-domain models with fixed weights produce a 28.4% false-positive rate in heterogeneous environments because they treat a chaotic public Wi-Fi signal with the same mathematical authority as a stable corporate LAN. Their 71.8% classification accuracy means nearly one in three access decisions is incorrect. These models have zero resistance to session hijacking because they lack any temporal dimension.

---

## SLIDE 14 — Dynamic Variance-Based DS Fusion: The Breakthrough

**Visual:** Before/after comparison + Contextual Gray-Area Routing diagram

**Content:**

### The Innovation: Stability as a Proxy for Trust
- High signal variance → erratic behaviour/compromise → weight **discounted**
- Low signal variance → stable, predictable → weight **amplified**
- Uncommitted weight becomes DS **Uncertainty** m(Θ) — not false-positive

### Contextual Gray-Area Routing
| Trust Score | Access Tier | Response |
|:---:|:---|:---|
| **> 0.75** | Full Access | All resources |
| **≥ 0.45** | Limited Access | Standard apps only (quarantine) |
| **< 0.45** | No Access | Session terminated |

### Key Results (vs. Static Model 3):
- **False-positive rate: 7.5%** (↓ 73% reduction)
- **Classification accuracy: 94.2%** (↑ 31% improvement)
- **Conflict coefficient K: 0.42** (↑ actionable conflict detection)

> **Speaker Notes:** The dynamic variance-based DS fusion model represents the first major breakthrough. The core insight is that stability is a proxy for trust. If a domain sensor exhibits high variance — indicative of erratic behaviour, a compromised sensor, or an active intrusion — the algorithm mathematically discounts that domain's influence. Crucially, the uncommitted weight becomes Dempster-Shafer Uncertainty — not a false positive. This enables what I call Contextual Gray-Area Routing: instead of binary allow/deny, the system routes ambiguous sessions into proportional access tiers. The results are striking: the false-positive rate drops from 28.4% to 7.5% — a 73% reduction — while classification accuracy rises to 94.2%. The conflict coefficient increases to 0.42, providing actionable inter-domain conflict detection.

---

## SLIDE 15 — Temporal Decay: Trust as an Ephemeral Asset

**Visual:** Side-by-side trust trajectory plots — Linear vs. Exponential decay

**Content:**

### The Defining Realisation: Trust is an Ephemeral Asset
A session's mathematical validity **must degrade over time** regardless of behavioural purity.

### Linear Temporal Decay: $D(t) = 1 - t/T_{session}$
- Steady, predictable degradation
- **Proportional TTL:** High-trust context = longer session; risky context = shorter session
- Suitable for standard corporate environments

### Exponential Temporal Decay: $D(t) = e^{-\lambda(t/T)}$
- Precipitous initial drop → "continuous algorithmic suspicion"
- Mathematical **kill-switch** against persistent threats
- Forces constant re-verification
- Suitable for high-security enclaves ($\lambda = 3.0$, 30-min absolute TTL)

### Key Result:
- Both models **eliminate the implicit trust period entirely**
- Exponential decay shatters the attack window for APTs
- But: exponential creates **excessive operational friction** for legitimate users

> **Speaker Notes:** The defining contribution of this thesis is the mathematical integration of time into the Zero Trust equation. Trust is an ephemeral asset — a session's mathematical validity must degrade over time regardless of how stable the user's behaviour appears. Linear decay provides proportional session degradation: a user connecting from a secure corporate environment enjoys a longer session, while a user on risky public Wi-Fi faces rapid expiration. Exponential decay is more aggressive — it transitions the network from "default trust with eventual expiration" to "continuous algorithmic suspicion." Both eliminate the implicit trust period. However, exponential decay creates excessive friction for legitimate users, motivating the Ensemble approach.

---

## SLIDE 16 — ★ The Ensemble Trust Model: Flagship Contribution

**Visual:** Freshness-Inertia continuum diagram + Ensemble formula + trust trajectory comparison

**Content:**

### The Security–Usability Paradox Resolved
$$T_{ensemble} = \underbrace{W_{short}(t) \cdot T_{instant}}_{\text{Fresh Signal (30 min)}} + \underbrace{(1 - W_{short}(t)) \cdot T_{prev} \cdot D_{long}(\Delta t)}_{\text{Historic Inertia (48 hours)}}$$

### Three Session Phases:
| Phase | Time | Dynamics |
|:---|:---|:---|
| **Skeptic Phase** | t → 0 | Signal-dominant. "I don't know you yet." Verification must be absolute. |
| **Calibration Phase** | t > 5 | Handover. Fresh signal fades, inertia grows. Jitter absorbed. |
| **Partner Phase** | t → 30 | Inertia-dominant. "I've been watching you. Consistency is policy." |

### The Attacker's Paradox:
To subvert the Ensemble engine, an adversary must:
1. Intercept a valid identity token **AND**
2. Perfectly replicate the victim's long-term behavioural baseline over an extended duration

→ A **virtually impossible** operational requirement.

### Comprehensive Results:

| Metric | Static (Model 3) | **Ensemble (Model 6)** | Improvement |
|:---|:---:|:---:|:---:|
| Classification Accuracy | 71.8% | **94.2%** | +31% |
| False-Positive Rate | 28.4% | **7.5%** | −73% |
| Conflict Detection (K) | 0.18 | **0.42** | +133% |
| Session Hijacking Resistance | None | **Strong** | — |
| Insider Threat Detection | Weak | **Strong** | — |
| Trust Evaluation Latency | 12.0 ms | **18.5 ms** | +6.5 ms |
| SDN Flow-Rule Impact | — | **None** | Identical |

> **Speaker Notes:** The Ensemble Trust Model is the flagship contribution of this thesis. It resolves the security-usability paradox by hybridising two time horizons. The short-term freshness component, governed by a 30-minute exponential decay, ensures that initial verification is rigorous and immediate. The long-term inertia component, governed by a 48-hour decay, provides behavioural momentum — a user with a strong history of safe behaviour is not revoked due to a single dropped packet. The model moves through three phases: the Skeptic Phase demands absolute verification; the Calibration Phase balances fresh evidence with growing history; the Partner Phase relies primarily on accumulated trust. This creates what I call the Attacker's Paradox: to maintain access, an adversary must simultaneously compromise the short-term cryptographic challenge AND perfectly replicate the victim's long-term behavioural cadence — a virtually impossible requirement. The results speak clearly: 94.2% classification accuracy, 73% false-positive reduction, and strong resistance to both session hijacking and insider threats, all at a cost of just 6.5 additional milliseconds — with zero impact on SDN flow-rule installation.

---

## SLIDE 17 — Summary of Contributions

**Visual:** Five-pillar diagram

**Content:**

### Five-Dimensional Contribution Framework

| Dimension | Contribution |
|:---|:---|
| 🔬 **Theoretical** | Extended Dempster-Shafer Theory into cybersecurity with dynamic weighting and temporal decay formalisation. Established mathematical foundations for trust as a continuously depreciating, probabilistic quantity. |
| 📐 **Methodological** | Rigorous emulation of complex network environments and simulation of adversarial validation scenarios using precisely generated synthetic data. Six-model comparative evaluation framework. |
| 🏗️ **Practical** | Calibrated decay matrices for real-world deployment: 30-min short-term TTL (NIST AAL2), 48-hour long-term inertia baseline, tuneable α and λ parameters. |
| ⚙️ **Technological** | Decoupled trust computation (PDP) from enforcement (PEP). Enforcement-agnostic: drives SDP gateways, SDN flow rules, or proxy sidecars. Demonstrated automated orchestration necessity. |
| 📊 **Empirical** | Testbed validated SDP mechanics using raw SDN/OpenFlow protocols. Successfully demonstrated decoupled control/data planes. 4-domain real-time telemetry integration. 2.1 ms evaluation latency at 25 nodes. |

> **Speaker Notes:** This thesis makes contributions across five dimensions. Theoretically, it extends Dempster-Shafer theory into cybersecurity with formal mechanisms for dynamic weighting and temporal decay. Methodologically, it establishes a rigorous six-model comparative evaluation framework validated across six threat scenarios. Practically, it provides calibrated deployment parameters aligned with NIST and PCI DSS standards that organisations can adopt directly. Technologically, it demonstrates the critical architectural principle of decoupling trust computation from enforcement — the Ensemble engine is enforcement-agnostic. Empirically, the containerised testbed validated SDP structural requirements using raw OpenFlow protocols, proving the viability of fully decoupled control and data planes within a trust-centric architecture.

---

## SLIDE 18 — What This Thesis Proves: Three Key Takeaways

**Visual:** Three bold statements with supporting evidence

**Content:**

### 1. The Fallacy of Static Trust
> "Cybersecurity can no longer treat authorisation as a discrete, binary checkpoint; it must be approached as a continuous, stateful evaluation."
- Static models produce 28.4% false-positive rates and have zero temporal awareness
- Boolean access policies are **structurally deficient** against automated modern threats

### 2. The Efficacy of Multi-Domain Evidential Fusion
> "The integration of Dynamic Variance-Based Weighting into the DS model solves the 'noisy sensor' problem."
- Contextual Gray-Area Routing replaces catastrophic lockouts with proportional access
- Heterogeneity becomes a defensive asset through inter-domain conflict detection

### 3. The Necessity of Temporal Dynamics
> "Trust is an ephemeral asset."
- The Ensemble Model eliminates the implicit trust period
- Freshness–Inertia hybridisation traps adversaries in the Attacker's Paradox
- **A mathematically rigorous blueprint for CARTA**

> **Speaker Notes:** This thesis proves three fundamental propositions. First, static trust is a fallacy — Boolean access policies are structurally deficient and produce unacceptable error rates in heterogeneous environments. Second, multi-domain evidential fusion with dynamic variance-based weighting solves the noisy sensor problem that plagues real deployments, enabling proportional rather than catastrophic access decisions. Third, and most importantly, temporal dynamics are not optional — trust is an ephemeral asset that must continuously depreciate. The Ensemble Trust Model, by hybridising freshness with inertia, provides a mathematically rigorous blueprint for Continuous Adaptive Risk and Trust Assessment — what the industry calls CARTA.

---

## SLIDE 19 — Scope & Limitations

**Content:**

| Limitation | Implication | Mitigation |
|:---|:---|:---|
| **Synthetic telemetry** | Abstracts production traffic stochasticity | Carefully parameterised against documented threat actor behaviours |
| **25-node testbed** | Does not expose enterprise-scale bottlenecks | Demonstrated architectural feasibility; latency is a lower-bound estimate |
| **Static parameters** (α, λ) | No adaptive tuning to changing threat conditions | Calibrated against NIST/PCI DSS baselines; RL optimisation deferred to future work |
| **No hardware trust anchors** | Vulnerable to sensor spoofing with stable fabricated telemetry | TPM/TEE integration identified as critical future direction |
| **Classical DS rule only** | Counterintuitive results under extreme conflict | Variance-based suppression mitigates; alternative rules (Yager, PCR5/6) not compared |
| **Independence assumption** | Correlated domain failures may produce underestimated variance | Operationally reasonable for selected facets; acknowledged as constraint |

> **Speaker Notes:** I want to be transparent about the boundaries of this research. The validation uses synthetic telemetry, which, though carefully parameterised, inevitably abstracts the full stochastic complexity of production traffic. The testbed operates at 25 nodes — orders of magnitude smaller than enterprise deployments. Parameters are fixed rather than adaptively tuned. No hardware trust anchors are integrated, leaving a theoretical vulnerability to sophisticated sensor spoofing. These are acknowledged boundaries that define natural future research directions rather than invalidating the core contributions.

---

## SLIDE 20 — Future Research Directions

**Visual:** Three-horizon timeline

**Content:**

### Short-Term (1–2 Years)
- 🔗 **Federated Edge Intelligence:** Collaborative trust learning without transmitting raw security logs
- 🔐 **Post-Quantum Cryptography:** ML-KEM integration into the authentication layer
- 🔍 **Explainable AI:** Human-readable rationale for every automated access decision

### Medium-Term (3–5 Years)
- 🤖 **AI-Driven Parameter Optimisation:** Reinforcement learning for adaptive α and λ calibration
- 🔄 **Autonomous Orchestration:** Cross-layer trust propagation (application → hardware isolation)
- 🔒 **Privacy-Preserving Telemetry:** Zero-Knowledge Proofs / Fully Homomorphic Encryption

### Long-Term (5+ Years)
- 🧠 **Cognitive Trust Systems:** AGI paradigms for semantic intent evaluation
- ⚛️ **Quantum Trust Computation:** Native quantum algorithms for evidential fusion
- 🏗️ **Self-Healing Network Topologies:** Autonomous restructuring upon trust degradation

> **Speaker Notes:** The research opens several compelling future directions. In the short term, extending the model into federated edge environments and integrating post-quantum cryptography are immediate priorities. Explainable AI integration is critical for operational viability. In the medium term, replacing static parameters with reinforcement learning-driven adaptive calibration and exploring privacy-preserving telemetry through zero-knowledge proofs are natural extensions. In the long term, the vision extends to cognitive trust systems that contextualise human intent and quantum-native fusion algorithms that could process virtually infinite telemetry variables concurrently.

---

## SLIDE 21 — Closing Statement

**Visual:** Clean, impactful closing slide

**Content:**

### From "Trust But Verify" → "Continuous Algorithmic Suspicion"

This thesis transitions the theoretical discourse on Zero Trust Architecture into a **mathematically actionable framework**.

By disproving the viability of static, Boolean access policies and demonstrating the superior resilience of **multi-domain evidential fusion bound by strict temporal decay**, this research provides a definitive mathematical blueprint for **Continuous Adaptive Risk and Trust Assessment (CARTA)** in heterogeneous enterprise networks.

---

*Thank you. I welcome your questions.*

> **Speaker Notes:** To close: this thesis transitions Zero Trust Architecture from a conceptual security philosophy into a mathematically actionable framework. It disproves the viability of static, Boolean access policies. It demonstrates the superior resilience of multi-domain evidential fusion with dynamic weighting. And it proves that trust is an ephemeral asset that must continuously depreciate. The Ensemble Trust Model — hybridising short-term cryptographic freshness with long-term behavioural inertia — provides the definitive blueprint for continuous adaptive risk and trust assessment. We move from the flawed standard of "trust but verify" to a mathematically sound state of continuous algorithmic suspicion. Thank you. I welcome your questions.
