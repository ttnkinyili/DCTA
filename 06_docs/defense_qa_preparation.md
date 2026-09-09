# PhD Defense Preparation: Focus Areas, Anticipated Questions & Answer Strategies

---

## PART 1: Key Focus Areas for the Defense

### Area 1: The Problem and Its Significance
**Why this matters to examiners:** They want to know you understand *why* this research is needed, not just *what* you built.

- The implicit trust period as a structural vulnerability (not just a theoretical concern)
- The disconnect between ZTA standards (NIST, CSA SDP) and algorithmic implementation
- The financial imperative: $1M+ breach cost reduction with mature ZTA (IBM, 2024)
- The regulatory momentum: DoD mandate, CISA Maturity Model

### Area 2: Mathematical Rigour of the Trust Engine
**Why this matters:** Examiners will probe whether your mathematical framework is sound, novel, and well-justified.

- Bernoulli → binomial → variance pipeline (why this specific probabilistic model?)
- The dynamic weighting equation: $W_d = 1/(1 + \alpha \cdot \sigma^2)$ — derivation and behaviour
- DS combination rule: when does it work well? When does it break down? (Zadeh's paradox)
- Pignistic transform: why BetP and not plausibility/belief directly?
- Ensemble formula: why weighted mixture vs. other fusion strategies?

### Area 3: The Ensemble Model as Flagship Contribution
**Why this matters:** This is your primary original contribution — expect the deepest questioning here.

- Freshness–Inertia continuum: theoretical justification
- Three session phases (Skeptic, Calibration, Partner): why these boundaries?
- Parameter calibration: why λ=3.0, α=5.0, T_short=30min, T_long=48hr?
- The Attacker's Paradox: how realistic is this claim under sophisticated adversaries?

### Area 4: Experimental Design and Validation
**Why this matters:** Examiners will assess whether your evaluation supports your claims.

- Why these six scenarios? How representative are they?
- Synthetic vs. real telemetry: what are the validity implications?
- Statistical significance: what tests were used? Effect sizes?
- The 25-node testbed: does it validate at scale?
- Testbed component choices: why OpenDaylight, Keycloak, OPA, Envoy specifically?

### Area 5: Contributions and Novelty
**Why this matters:** This determines whether the thesis meets the doctoral standard.

- What specifically is novel vs. what is integration of existing techniques?
- How does this advance the state of the art beyond existing DS-based trust models?
- The five-dimensional contribution framework: which is the strongest?
- Publications arising from this work

### Area 6: Limitations and Honesty
**Why this matters:** Examiners respect candidates who clearly understand boundaries.

- The independence assumption: how realistic is this?
- Static parameters: how sensitive are results to α and λ choices?
- No formal adversarial robustness analysis
- No hardware trust anchors
- No real user telemetry or UX measurement

---

## PART 2: Anticipated Questions and Answer Strategies

### Category 1: Motivation & Problem Statement

---

**Q1: Why focus on the trust algorithm specifically, rather than improving enforcement mechanisms like SDP or SASE?**

**Strategy:** Frame your answer around the separation of concerns principle.

> "Enforcement mechanisms like SDP and SASE are mature at the *last mile* — translating trust decisions into access actions. However, they all assume trust scores arrive from an external, unspecified source. No enforcement mechanism can compensate for a poorly computed trust score. My thesis addresses the *computation layer* — the missing algorithmic calculus — which is deliberately enforcement-agnostic. This decoupling is itself a contribution: the Ensemble engine can drive SDP gateways, SDN flow rules, or proxy sidecars without modification."

---

**Q2: How is the 'implicit trust period' different from a standard session timeout problem?**

**Strategy:** Distinguish between timeout (a blunt instrument) and continuous evaluation (a mathematical process).

> "A session timeout is a binary mechanism — access persists unchanged for N minutes, then terminates. The implicit trust period is the *entire duration* during which the system does not re-evaluate trust. Even with a 30-minute timeout, a device compromised at minute 1 operates with full trust until minute 30. My approach replaces the binary timeout with continuous mathematical depreciation — trust degrades continuously, and contextual changes are detected in real-time. The Ensemble Model creates *proportional* session degradation, not cliff-edge expiration."

---

**Q3: Is this problem already solved by continuous authentication products in the market?**

**Strategy:** Acknowledge commercial products but highlight the algorithmic gap.

> "Commercial continuous authentication products exist — Microsoft Entra, Google BeyondCorp, Zscaler. However, these are proprietary implementations whose trust algorithms are opaque. My contribution is the *mathematical framework* — a transparent, auditable, reproducible algorithm. No published work demonstrates how these products compute, weight, fuse, and decay trust across multiple domains. This thesis provides that missing mathematical blueprint, which can be implemented within or alongside any enforcement platform."

---

### Category 2: Methodology

---

**Q4: Why synthetic telemetry rather than real network traces? Doesn't this limit your findings?**

**Strategy:** Own the limitation, but explain the methodological justification.

> "I acknowledge this as a limitation. However, real-world telemetry is subject to privacy constraints, regulatory barriers, and an inability to reproduce specific threat scenarios deterministically. Synthetic telemetry allows precise control of variables — I can systematically introduce credential theft, lateral movement, and insider exfiltration at exact time steps. The telemetry parameters were calibrated against documented threat actor behaviours from IBM, Elastic Security Labs, and CISA incident reports. That said, validation with operational datasets is the critical next step I identify in my future work."

---

**Q5: How did you validate the statistical significance of your results?**

**Strategy:** Reference the specific tests and effect sizes.

> "Statistical validation employed the Wilcoxon signed-rank test across 50 independent simulation runs, yielding p < 0.01 for the comparison between static and Ensemble models. Effect sizes were quantified using Cliff's delta, which indicated a *large* effect (|δ| ≥ 0.474) for classification accuracy improvement and false-positive reduction. Per-scenario accuracy was computed as the fraction of time steps where predicted tier matched ground truth, aggregated as mean ± standard deviation across runs."

---

**Q6: Why six scenarios? How do you know they are representative of real enterprise environments?**

**Strategy:** Map each scenario to documented real-world conditions.

> "The six scenarios were designed to span the operational spectrum described in NIST SP 800-207 and the CISA Zero Trust Maturity Model. Corporate Office represents the baseline pristine environment. Remote VPN captures the dominant post-pandemic workforce model. Public Wi-Fi and BYOD represent the highest-risk conditions organisations face today. Compromised Endpoint simulates the specific attack vectors identified in IBM's Threat Intelligence Index — credential relay, lateral movement, and session hijacking. The Untrusted Device with Geofence Violation combines multiple risk factors simultaneously. Together, they cover the axes of network quality, device trustworthiness, and active compromise."

---

**Q7: Why did you choose this specific testbed stack (OpenDaylight, Keycloak, OPA, Envoy)?**

**Strategy:** Justify each component architecturally.

> "Each component was selected to map directly to a NIST SP 800-207 logical component. OpenDaylight serves as the Policy Administrator — a mature, open-source SDN controller supporting OpenFlow. Keycloak provides the Identity and Trust Anchor via industry-standard OIDC/SAML protocols. Open Policy Agent serves as the Policy Decision Point using Rego, a declarative policy language that enables auditable, version-controlled trust logic. Envoy Proxy provides the application-layer Policy Enforcement Point. Crucially, all are open-source, enabling full reproducibility — a contribution in itself."

---

### Category 3: Mathematical Foundations

---

**Q8: Why Dempster-Shafer theory specifically? Why not Bayesian inference or fuzzy logic?**

**Strategy:** Highlight the unique advantage of DS theory — explicit uncertainty representation.

> "The decisive advantage of Dempster-Shafer over Bayesian inference is its native capacity for *epistemic uncertainty* — the explicit representation of 'I don't know.' Bayesian inference requires complete prior distributions; in heterogeneous networks where sensor availability is intermittent and attacker models are unknown, uniform priors introduce unjustified assumptions. DS theory allows uncommitted belief mass m(Θ) — the system can formally quantify its ignorance. This is operationally critical: when a sensor is erratic, I want the system to say 'Uncertain,' not to force a guess between 'Safe' and 'Unsafe.' Fuzzy logic could model gradual membership but lacks DS theory's formal conflict detection via the normalisation constant K — which I leverage to detect multi-domain compromise."

---

**Q9: How do you handle Zadeh's paradox — the known weakness of Dempster's combination rule under high conflict?**

**Strategy:** Show awareness of the critique and explain your mitigation.

> "Zadeh's paradox arises when combining highly conflicting evidence — the normalisation in Dempster's rule amplifies residual mass and can produce counterintuitive results. I mitigate this structurally through the variance-based weight suppression mechanism. When a domain exhibits high conflict with others, it also exhibits high variance. The dynamic weighting equation $W_d = 1/(1 + α·σ²)$ drives the weight toward zero, converting that domain's committed mass into Uncertainty rather than conflicting Belief. Effectively, high-conflict domains are mathematically silenced before they enter the combination. I acknowledge that I did not empirically compare Dempster's rule against alternatives like Yager's rule or PCR5/6 — this is a stated limitation — but the variance suppression provides a pragmatic and effective mitigation."

---

**Q10: Why use the pignistic transform rather than reporting belief/plausibility intervals?**

**Strategy:** Justify BetP as the decision-theoretic choice.

> "The pignistic transform BetP is the decision-theoretically optimal point estimate for making access decisions. Belief and plausibility intervals provide bounds — useful for analysis but not for a binary or tiered access decision. When the system must route a session to Full, Limited, or No Access, it needs a single actionable value. BetP distributes uncommitted mass proportionally among focal elements, providing a probability that is compatible with betting ratios — hence 'pignistic.' This is the standard approach in operational DS applications where point decisions are required."

---

**Q11: Why model individual facets as Bernoulli random variables? What justifies this simplification?**

**Strategy:** Explain the principled chain from facet to domain score.

> "Each binary compliance facet — MFA completed or not, patch current or not, TLS 1.3 or not — is inherently a binary observation, making the Bernoulli model a natural fit. The binomial aggregation across facets within a domain produces the domain score as a proportion. This proportion then feeds the variance computation over a sliding window of N=10 observations. The simplification is justified because the alternative — continuous-valued sensor readings — would require parametric distribution assumptions that are harder to validate. The Bernoulli model is parsimonious, interpretable, and aligns with how real endpoint telemetry is typically reported: pass/fail compliance checks."

---

### Category 4: Dempster-Shafer Specifics

---

**Q12: How does the conflict coefficient K contribute to your security model?**

**Strategy:** Explain K as a signal of multi-domain compromise.

> "The conflict coefficient K measures the degree to which evidence sources disagree. In my architecture, a high K value signals that one or more domains are reporting evidence that contradicts the others — a strong indicator of compromise. For example, if Identity reports 'Safe' (valid token) but Network reports 'Unsafe' (anomalous routing), the conflict surfaces as elevated K. In the Ensemble Model, K reaches 0.42 compared to 0.18 in the static model, meaning the dynamic weighting amplifies conflict to actionable levels. This is a feature, not a bug — the system transforms the network's heterogeneity into a detection mechanism."

---

**Q13: You mention four domains. Why four? Why not more or fewer?**

**Strategy:** Align with NIST pillars while acknowledging extensibility.

> "The four domains — Identity, Device, Network, Application/Data — align directly with the core pillars specified in NIST SP 800-207. Additional domains like physical access or biometrics are acknowledged but excluded from the current evaluation to maintain scope. Crucially, the DS combination rule accommodates an arbitrary number of evidence sources — the framework is mathematically extensible without structural modification. Adding a fifth domain would require only an additional mass function and one more pairwise combination. The four-domain configuration represents the minimum set required for comprehensive ZTA evaluation."

---

### Category 5: Temporal Dynamics

---

**Q14: Why exponential decay rather than some other function? What about logistic or hyperbolic decay?**

**Strategy:** Justify exponential and acknowledge alternatives.

> "Exponential decay was selected because it models continuous, proportional depreciation — the rate of trust loss is proportional to the current trust level. This is the standard in risk modelling and reputation systems. Unlike linear decay, which degrades at a constant rate regardless of current value, exponential decay inflicts rapid initial depreciation and smooth asymptotic convergence — matching the security intuition that a fresh session is far more trustworthy than a stale one. Logistic and hyperbolic decay profiles are acknowledged as alternatives in my limitations — they may offer advantages in specific deployment contexts and are identified as future research."

---

**Q15: How sensitive are your results to the choice of λ=3.0 and α=5.0?**

**Strategy:** Acknowledge this as a limitation while explaining the calibration rationale.

> "The parameters were calibrated against compliance baselines: λ=3.0 ensures that $e^{-3.0} ≈ 0.05$, meaning trust reaches a terminal state at exactly the NIST AAL2 30-minute idle boundary. α=5.0 provides a balanced logistic-style decay that penalises sustained oscillation while absorbing micro-jitter, following recommendations from Jøsang's Subjective Logic framework. I acknowledge that a full parameter sensitivity analysis across the entire (α, λ) space was not conducted — the conditions under which specific parameterisations produce oscillatory behaviour or excessive false positives remain uncharacterised. Reinforcement learning and Bayesian optimisation for adaptive calibration are identified as priority future work."

---

**Q16: Isn't 30 minutes too short for a standard enterprise session? And 48 hours too long?**

**Strategy:** Cite the standards that justify these choices.

> "The 30-minute short-term window aligns with NIST SP 800-63B AAL2, which mandates re-authentication after 30 minutes of inactivity. PCI DSS v4.0 specifies an even more aggressive 15-minute timeout for sensitive data environments. The 48-hour long-term window covers the operational 'weekend gap' — Friday evening to Monday morning — preventing a forced full re-login for devices with established behavioural history. For high-security enclaves, I specify that the long-term window must be capped at 12 hours per NIST AAL3. These are configurable parameters, not fixed constants — the architecture supports enterprise-specific calibration."

---

### Category 6: The Ensemble Model

---

**Q17: What evidence do you have that the 'Attacker's Paradox' actually holds against a sophisticated adversary?**

**Strategy:** Bound your claim carefully.

> "The Attacker's Paradox holds under the assumption that the adversary cannot simultaneously reproduce the victim's long-term behavioural baseline while conducting their attack objectives. Our simulations validate this across six scenarios. However, I want to be precise: a highly sophisticated adversary with full knowledge of the algorithm, extended observation of the victim's behaviour, and the ability to control all four domains simultaneously could theoretically evade the model. This coordinated multi-domain manipulation attack is identified as a limitation. The practical barrier is the *duration* requirement — maintaining perfect behavioural mimicry across four independent domains over an extended period while simultaneously exfiltrating data is operationally extremely difficult, even for advanced APTs."

---

**Q18: How does the Ensemble Model handle cold-start — a completely new user or device with no history?**

**Strategy:** Explain the default variance strategy.

> "At cold start, the system has no historical baseline. The sliding window is empty, so variance defaults to σ²=0.25 — the maximum variance for a Bernoulli distribution (p=0.5). This produces conservative dynamic weights, routing the new entity into Limited Access until sufficient observations accumulate. The system requires 4–8 evaluation steps to build meaningful variance history. This is a one-time initialisation cost — approximately 5–8 minutes at standard 1-minute evaluation intervals. This conservative approach aligns with Zero Trust philosophy: new entities are granted minimal access until they prove themselves."

---

**Q19: The Ensemble formula is a weighted linear combination. Have you considered non-linear fusion approaches?**

**Strategy:** Justify linearity and acknowledge the extension.

> "The weighted linear combination was chosen for interpretability, computational efficiency, and auditability — the contribution of freshness versus inertia is transparent at every time step. Non-linear fusion — neural networks, deep learning-based aggregation — could potentially capture more complex temporal patterns but would sacrifice explainability. Given the operational requirement for transparent, auditable trust decisions (highlighted by Chen & Wang, 2025, in the Explainable AI context), linearity is a deliberate design choice. That said, exploring non-linear fusion with Explainable AI wrappers is a natural medium-term research direction."

---

### Category 7: Testbed & Validation

---

**Q20: Your testbed has 25 nodes. How do you know this scales to enterprise environments with thousands of endpoints?**

**Strategy:** Acknowledge the gap but explain architectural reasoning.

> "I cannot claim production-scale validation from a 25-node testbed. However, the architecture provides strong evidence for scalability. Per-session computation is independent — there are no cross-session dependencies — enabling trivial horizontal scaling through load-balanced Ensemble Trust Engine instances. The 18.5 ms per-evaluation latency is bounded by fixed-size operations: variance over 10 values, DS fusion over 4 domains, and two exponential calculations. These do not grow with the number of nodes. The Redis state store requires 320 bytes per session — at 10,000 concurrent sessions, that's 3.2 MB, well within single-node Redis capacity. The architectural bottleneck would be the SDN controller, not the trust engine. I identify scaling validation as a priority for operational deployment."

---

**Q21: You report 2.1 ms policy evaluation latency. Under what conditions? Is this realistic?**

**Strategy:** Be precise about measurement conditions.

> "The 2.1 ms measurement represents the trust computation plus OPA policy evaluation on the containerised testbed under nominal load conditions — no concurrent session stress, Mininet-emulated links with zero packet loss. This is a lower-bound estimate. In production, with WAN latency, concurrent sessions, and controller load, I would expect 20–50 ms end-to-end. The critical point is that even the full Ensemble pipeline at 18.5 ms plus 5 ms for OpenFlow rule installation totals approximately 23.5 ms — well within the sub-100 ms threshold that SDN literature considers acceptable for flow-rule installation."

---

**Q22: Did you compare your results against any existing trust computation system?**

**Strategy:** Explain the comparative approach within the thesis.

> "My comparative evaluation is *internal* — the six-model progression provides the baseline comparison. Each model is evaluated under identical conditions across the same six scenarios, allowing direct comparison of classification accuracy, false-positive rates, and conflict detection. I did not benchmark against an external trust computation system because (a) no open-source, algorithmically transparent system exists that performs multi-domain DS fusion with temporal decay, and (b) commercial systems are proprietary black boxes. The closest academic comparisons are discussed in the literature review — Bayesian, HMM, and POMDP approaches — which I compare theoretically rather than experimentally due to the absence of common benchmarks."

---

### Category 8: Contributions & Novelty

---

**Q23: What is the single most important original contribution of this thesis?**

**Strategy:** Lead with the Ensemble Model but frame it within the broader contribution.

> "The single most important contribution is the formal integration of *temporal dynamics* into the multi-domain Dempster-Shafer trust fusion framework — specifically, the Ensemble Trust Model's Freshness-Inertia hybridisation. While individual elements exist in isolation — DS fusion in other domains, temporal decay in session management — no prior work combines variance-based dynamic weighting, four-domain DS evidential fusion, dual-horizon exponential temporal decay, and the Freshness-Inertia continuum into a unified, enforcement-agnostic trust computation engine. The synthesis is the contribution."

---

**Q24: How does this advance the state of the art beyond existing DS-based trust models?**

**Strategy:** Be specific about three advances.

> "Three specific advances. First, existing DS applications in cybersecurity are limited to single-domain evaluations — my model extends to four independent domains with inter-domain conflict detection. Second, no prior DS-based trust model integrates temporal decay — they compute trust at discrete snapshots without enforcing session ephemerality. Third, the variance-based dynamic weighting mechanism resolves Zadeh's paradox pragmatically by suppressing conflicting evidence sources before combination, rather than relying on alternative combination rules."

---

**Q25: Have any papers been published from this work?**

**Strategy:** List publications and submissions.

> [Cite your actual publications. If papers are under review, state that clearly: "Two papers are under review at [journals/conferences]."]

---

### Category 9: Limitations & Robustness

---

**Q26: You assume independence between domain facets. What happens if this assumption is violated?**

**Strategy:** Explain the practical risk and mitigation.

> "If domain facets are correlated — for example, a system compromise simultaneously disabling endpoint protection and subverting hardware attestation — the model would underestimate domain-level variance. The correlated failure would appear as a single-domain event rather than a systemic compromise. The Dempster-Shafer combination rule itself assumes source independence. In practice, the four *domains* (Identity, Device, Network, Application) are architecturally independent — they are measured by separate systems. The *facets within* a single domain may exhibit correlation. The practical risk is bounded because correlated failures typically produce extreme scores (near zero) that trigger denial regardless of variance estimation accuracy."

---

**Q27: What if an adversary knows your algorithm and crafts inputs to evade detection?**

**Strategy:** Acknowledge this as a stated limitation and explain the structural barriers.

> "This is a stated limitation — I did not conduct a formal adversarial robustness analysis. An adversary with full algorithm knowledge could theoretically craft stable, fabricated telemetry that passes the variance check. However, the structural defence is the *multi-domain independence*. To evade the Ensemble engine, the adversary would need to simultaneously control four independent telemetry pipelines, maintain stable variance across all four, AND accomplish their attack objectives — a significantly more challenging requirement than defeating any single-domain system. This is the essence of the Attacker's Paradox, though I acknowledge it has not been formally proven against an optimal adversary."

---

**Q28: You mention no hardware trust anchors (TPM/TEE). Doesn't this fundamentally undermine your security claims?**

**Strategy:** Contextualise the contribution layer.

> "My contribution operates at the *algorithmic* layer — how to compute and fuse trust once telemetry is received. Hardware trust anchors operate at the *telemetry integrity* layer — ensuring the data fed to the algorithm is authentic. These are complementary, not competing, concerns. The Ensemble engine would only become *more* robust with TPM-attested telemetry. Without it, the model is vulnerable to a specific attack class: stable fabricated signals from a compromised endpoint. I identify TPM/TEE integration as a critical short-term future direction. The algorithmic contribution remains valid regardless of the telemetry source — it's the computation over whatever data is available."

---

**Q29: What is the false-negative rate? You report false-positive reduction but not missed attacks.**

**Strategy:** Frame the answer around classification accuracy.

> "The 94.2% classification accuracy captures both false positives (legitimate users denied) and false negatives (attackers granted access). Across the Compromised Endpoint and Untrusted Device scenarios, the Ensemble Model correctly classified these as 'No Access' in 100% of evaluation steps after the initial convergence period of 4–8 steps. The false-negative risk is highest during the cold-start convergence period and in the 'low and slow' attack scenario where the attacker maintains perfect behavioural mimicry. The temporal decay component specifically addresses the latter — even perfect mimicry cannot prevent session expiration."

---

### Category 10: Future Work & Broader Impact

---

**Q30: If you had one more year, what would you do?**

**Strategy:** Prioritise the single highest-impact extension.

> "I would conduct a comprehensive parameter sensitivity analysis using Bayesian optimisation to map the (α, λ) parameter space, identify optimal configurations for different risk profiles, and characterise the conditions under which the model produces oscillatory or unstable behaviour. This directly addresses the most significant limitation and would transform the static parameterisation into an adaptive, self-tuning engine."

---

**Q31: How would you deploy this in a real enterprise?**

**Strategy:** Describe the architectural path.

> "The deployment architecture follows the tiered model I describe. The Ensemble Trust Engine runs as a containerised microservice, decoupled from the enforcement layer. It ingests telemetry via streaming architecture — ideally Apache Kafka for real-time event processing — and outputs trust scores to the existing policy enforcement infrastructure. The engine integrates with SIEM/SOAR platforms for telemetry aggregation. The critical operational requirement is automated SDP orchestration — linking trust score changes to flow-rule updates without manual intervention. The testbed demonstrates this path using OPA and OpenDaylight."

---

**Q32: What about algorithmic fairness? Could your model discriminate against certain user groups?**

**Strategy:** Show awareness and cite the specific concern.

> "This is an important concern I identify in the limitations. Variance-based dynamic weighting treats all facets as neutral technical signals, yet certain behavioural facets — keystroke dynamics, access pattern normality — may exhibit differential baseline distributions across user populations. A user with a disability affecting keystroke dynamics, or a user in a non-standard time zone, could receive systematically suppressed trust scores. I identify Explainable AI integration and empirical bias auditing across demographic and operational subgroups as critical requirements for production deployment, but I did not conduct this auditing within the thesis scope."

---

**Q33: Is this work applicable outside enterprise networks — IoT, healthcare, critical infrastructure?**

**Strategy:** Identify the extension path.

> "Absolutely, and this is where the enforcement-agnostic design is most valuable. For IoT environments, I outline a tiered trust architecture — lightweight binary checks at the device, simplified DS fusion at the gateway, full Ensemble at the cloud. For healthcare (IoMT), the strict temporal decay parameters would align with HIPAA requirements. For critical infrastructure, the exponential decay with λ≥5.0 provides the mathematical kill-switch needed. The DS framework accepts arbitrary evidence sources, so industrial sensors, medical telemetry, or SCADA readings can be incorporated as additional domains."

---

## PART 3: General Answer Strategies

### The "I Don't Know" Protocol
If asked a question you genuinely cannot answer:
> "That is an excellent question that extends beyond the current scope of this research. What I can say is [relevant adjacent knowledge]. I would approach this by [methodology]. This is precisely the type of investigation I identify as future work in Chapter 8."

### The Hostile Question Protocol
If an examiner challenges a core assumption:
1. **Acknowledge:** "You raise an important point."
2. **Contextualise:** "Within the scope of this research, I bounded this as follows..."
3. **Evidence:** "The results demonstrate that under these conditions..."
4. **Concede gracefully if appropriate:** "This is a stated limitation, and I agree that [extension] would strengthen the contribution."

### Numbers to Have Memorised
| Metric | Value |
|:---|:---|
| Classification accuracy (Static → Ensemble) | 71.8% → 94.2% |
| False-positive reduction | 73% (28.4% → 7.5%) |
| Conflict detection improvement | K: 0.18 → 0.42 |
| Ensemble latency overhead | +6.5 ms |
| Total end-to-end latency | ~23.5 ms |
| Testbed nodes | 25 |
| Policy evaluation latency | 2.1 ms |
| Sliding window size | N = 10 |
| Memory per session | 320 bytes |
| Short-term decay | 30 min, λ=3.0 |
| Long-term inertia | 48 hours |
| Recommended α | 5.0 (enterprise), ≥10.0 (critical) |
| Breach cost reduction | >$1M (IBM, 2024) |

### Key Phrases to Use
- "Trust is an ephemeral asset"
- "Continuous algorithmic suspicion"
- "Contextual Gray-Area Routing"
- "The Attacker's Paradox"
- "Stability as a proxy for trust"
- "Enforcement-agnostic computation"
- "The Freshness-Inertia continuum"
- "From 'trust but verify' to 'continuous adaptive risk and trust assessment'"
