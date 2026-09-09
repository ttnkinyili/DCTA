# PhD Thesis Defense Presentation Outline

## Title: Evaluating Zero Trust Models Through Evidential Fusion and Temporal Dynamics in Heterogeneous Enterprise Networks

**Total Duration: 25 minutes** (+ Q&A)

---

## Section 1: Opening & Context Setting (2 minutes)

### Slide 1 — Title Slide (30 sec)
- Thesis title, candidate name, supervisors, institution, date
- Key message: *This is a mathematically-grounded contribution to Zero Trust Architecture*

### Slide 2 — The Cybersecurity Landscape (1 min 30 sec)
- The collapse of the traditional perimeter (remote work, BYOD, cloud)
- IBM 2024: breach cost differential ($1M+) between ZTA and legacy architectures
- The Zero Trust mandate: NIST SP 800-207, CISA Maturity Model v2.1, DoD ZT Strategy
- Key message: *The problem is urgent, well-funded, and architecturally unresolved*

---

## Section 2: Problem Statement & Research Gap (3 minutes)

### Slide 3 — The Implicit Trust Period Problem (1 min 30 sec)
- Authentication as a discrete, binary event → durable session access
- The "operational runway" for APTs, session hijacking, insider exfiltration
- Neither NIST SP 800-207 nor CSA SDP v2.0 prescribes *how* to compute, decay, or fuse trust
- Key message: *Zero Trust standards define WHAT to do, but not HOW to compute trust continuously*

### Slide 4 — The Convergent Research Gap (1 min 30 sec)
- Four interlocking gap dimensions:
  1. **Evidential uncertainty quantification** — no explicit representation of incomplete knowledge
  2. **Temporal trust depreciation** — no continuous decay, only binary timeouts
  3. **Multi-domain conflict detection** — no inter-domain inconsistency detection
  4. **Enforcement-agnostic computation** — no decoupled trust engine
- Key message: *No existing work simultaneously addresses all four dimensions*

---

## Section 3: Research Objectives & Questions (2 minutes)

### Slide 5 — Research Objectives (1 min)
- **Primary Objective:** Develop and empirically evaluate a progression of computational trust models, advancing from static access control to a novel Ensemble Trust Model grounded in Dempster-Shafer theory
- **Sub-objectives:**
  1. Formally model trust as a continuously depreciating, probabilistically computed quantity
  2. Demonstrate multi-domain evidential fusion with dynamic variance-based weighting
  3. Integrate temporal dynamics (linear and exponential decay) into the trust equation
  4. Validate through a reproducible, containerised testbed across heterogeneous threat scenarios

### Slide 6 — Research Questions & Hypotheses (1 min)
- RQ1: Can evidential fusion coupled with temporal decay effectively neutralise lateral movement and session hijacking compared to legacy models?
- RQ2: Does variance-based dynamic weighting reduce false-positive lockouts while maintaining security?
- RQ3: Can the Ensemble Model balance security aggressiveness with operational continuity?
- Key message: *The questions are testable, the hypotheses are falsifiable*

---

## Section 4: Literature Positioning (2 minutes)

### Slide 7 — Trust Computation Landscape (1 min)
- Bayesian (PTIT-ELO), HMM (HMM-BMS), POMDP, Markov chain (TrustS)
- All assume complete prior distributions — operationally untenable in heterogeneous networks
- DS theory resolves: explicit uncertainty via unprojected mass m(Θ)
- Gap: Surveyed DS applications limited to single-domain

### Slide 8 — Standards vs. Algorithms (1 min)
- NIST SP 800-207: specifies input variables but leaves Trust Algorithm abstracted
- CSA SDP v2.0: excellent session initiation, but binary trust post-perimeter
- This thesis fills the algorithmic calculus gap between architecture and mathematics
- Key message: *Architecture and standards are mature; the algorithm is what's missing*

---

## Section 5: Methodology & Testbed Design (3 minutes)

### Slide 9 — Research Methodology (1 min)
- Design Science Research approach
- Six progressively sophisticated trust models evaluated
- Four independent domains: Identity, Device, Network, Application/Data
- Bernoulli random variables → binomial proportions → variance-based dynamic weighting → DS mass functions

### Slide 10 — The Mathematical Engine (1 min)
- Core equations:
  - Dynamic weight: $W_d = \frac{1}{1 + \alpha \cdot \sigma^2}$
  - DS combination rule for belief fusion
  - Ensemble formula: $T_{ensemble} = W_{short}(t) \cdot T_{instant} + (1 - W_{short}(t)) \cdot T_{prev} \cdot D_{long}(\Delta t)$
- Three tunable parameters: $e$ (decay base), $\lambda$ (decay velocity), $\alpha$ (variance sensitivity)

### Slide 11 — Testbed Architecture (1 min)
- Containerised stack: OpenDaylight (SDN controller), Keycloak (IdP), OPA (policy engine), Envoy (PEP)
- Mininet-emulated SDN fabric with Open vSwitch
- Six canonical threat scenarios: Corporate Office, Remote VPN, Public Wi-Fi, BYOD, Untrusted Device + Geofence, Compromised Endpoint
- 25 active nodes, 2.1 ms policy evaluation latency

---

## Section 6: The Model Progression & Results (7 minutes) ★ Core Section

### Slide 12 — The Six-Model Progression Overview (1 min)
- Visual diagram: Model 1 → Model 6 (evolution arrow)
  1. Implicit Trust (No Policy)
  2. Single-Domain Criteria
  3. Static Multi-Domain with DS Fusion
  4. Dynamic Weighting with Variance-Based DS Fusion
  5. Dynamic Weighting + Temporal Decay (Linear / Exponential)
  6. **Ensemble Trust Model** (Freshness + Inertia hybridisation)

### Slide 13 — Static Models: Why They Fail (1 min)
- Implicit Trust → unchecked lateral movement
- Single-Domain → context spoofing defeats single axis
- Static Multi-Domain → "inflexible calibration" creates durational passport
- Key result: Static models = 28.4% false-positive rate, 71.8% classification accuracy

### Slide 14 — Dynamic Variance-Based DS Fusion (1 min 30 sec)
- Stability as a proxy for trust: high variance → weight discounted → mass becomes Uncertainty
- **Contextual Gray-Area Routing**: Full > 0.75, Limited ≥ 0.45, No Access < 0.45
- Solves the "noisy sensor" problem — oscillating signals treated as "Irrelevant" not "Bad"
- Key result: False-positive rate drops to 7.5%, accuracy rises to 94.2%

### Slide 15 — Temporal Decay Integration (1 min 30 sec)
- Linear decay: proportional TTL — riskier contexts → shorter sessions
- Exponential decay: "continuous algorithmic suspicion" — mathematical kill-switch
- Trust as an ephemeral asset — sessions degrade regardless of behavioral purity
- Key result: Eliminates the implicit trust period entirely

### Slide 16 — The Ensemble Trust Model (2 min) ★ Flagship Result
- Freshness–Inertia continuum diagram
- Short-term (30-min exponential): verification & data freshness
- Long-term (48-hour exponential): behavioral momentum & continuity
- The "Attacker's Paradox": must intercept token AND replicate behavioral baseline
- Key results:
  - 94.2% classification accuracy (vs. 71.8% static)
  - 73% false-positive reduction
  - Conflict detection: K = 0.42 (vs. 0.18 static)
  - 6.5 ms additional latency (negligible, no SDN impact)

---

## Section 7: Contributions (3 minutes) ★ Emphasis Section

### Slide 17 — Summary of Contributions (2 min)
Present as five pillars:

| Dimension | Contribution |
|:---|:---|
| **Theoretical** | Extended DS theory into cybersecurity with dynamic weighting + temporal decay formalisation |
| **Methodological** | Rigorous validation via synthetic data across 6 threat scenarios with statistical testing |
| **Practical** | Calibrated decay matrices for enterprise deployment (30-min short-term, 48-hour long-term) |
| **Technological** | Decoupled trust computation engine from enforcement — enforcement-agnostic architecture |
| **Empirical** | Testbed validated SDP mechanics using raw SDN/OpenFlow with decoupled control/data planes |

### Slide 18 — What This Thesis Proves (1 min)
- Three key takeaways:
  1. **The Fallacy of Static Trust**: Boolean access policies are structurally deficient
  2. **The Efficacy of DS Fusion**: Multi-domain evidential fusion + dynamic weighting resolves the noisy sensor problem
  3. **The Necessity of Temporal Dynamics**: Trust is an ephemeral asset; time must be part of the equation
- Key message: *This thesis transitions Zero Trust from conceptual framework to mathematically actionable blueprint*

---

## Section 8: Limitations & Future Work (2 minutes)

### Slide 19 — Scope & Limitations (1 min)
- Synthetic telemetry (not production traffic)
- 25-node testbed (not enterprise scale)
- Static parameter calibration (α, λ fixed throughout)
- No hardware trust anchors (TPM/TEE absent)
- Classical DS rule only (Yager, PCR5/6 not compared)
- Independence assumption across domain facets

### Slide 20 — Future Research Directions (1 min)
- **Short-term (1–2 years):** Federated edge intelligence, post-quantum cryptography integration, Explainable AI
- **Medium-term (3–5 years):** ML-driven adaptive parameters, autonomous orchestration, privacy-preserving telemetry (ZKPs/FHE)
- **Long-term (5+ years):** Cognitive trust systems, quantum trust computation

---

## Section 9: Closing (1 minute)

### Slide 21 — Closing Statement (1 min)
- Restate the core contribution: "A mathematically rigorous blueprint for Continuous Adaptive Risk and Trust Assessment"
- From "trust but verify" → "continuous algorithmic suspicion"
- Acknowledgements
- *"Thank you. I welcome your questions."*

---

## Timing Summary

| Section | Duration | Slides |
|:---|:---:|:---:|
| Opening & Context | 2 min | 1–2 |
| Problem & Gap | 3 min | 3–4 |
| Objectives & Questions | 2 min | 5–6 |
| Literature Positioning | 2 min | 7–8 |
| Methodology & Testbed | 3 min | 9–11 |
| Model Progression & Results | 7 min | 12–16 |
| Contributions | 3 min | 17–18 |
| Limitations & Future Work | 2 min | 19–20 |
| Closing | 1 min | 21 |
| **Total** | **25 min** | **21 slides** |

---

## Presentation Design Notes

- Use dark theme with gradient accents (cybersecurity aesthetic)
- All equations should be rendered cleanly (LaTeX or high-res images)
- Trust trajectory plots from simulation results as key visuals
- Architecture diagrams: testbed topology, model progression, Freshness-Inertia continuum
- Keep text minimal on slides — speak to the content, don't read it
- Practice transitions between sections — the "model progression" section is the narrative arc
