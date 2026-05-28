# Aggregated Thesis-Level Literature Critiques

## Dynamic Fusion of Beliefs on Trust Models for Zero-Trust Enforcement in Heterogeneous Networks

*This document presents aggregated, thesis-level critical analyses of 23 peer-reviewed works, synthesized from two independent critique streams and grounded against the contributions of this thesis: an Ensemble Trust Model integrating Dempster-Shafer evidential fusion, dynamic variance-based weighting, and temporal decay for Continuous Adaptive Risk and Trust Assessment (CARTA) in heterogeneous enterprise networks.*

---

### 1. A Survey on Trust Models in Heterogeneous Networks (2022)

**Research Objectives.** This survey retrospectively examines the evolution of trust modeling across heterogeneous networks (HetNets), spanning IoT, 5G, and large-scale HetNet (LS-HetNet) topologies. It defines Quality of Trust (QoT) criteria—subjectivity, dynamicity, context-awareness, privacy, scalability, robustness, overhead, explainability, and user acceptance—and taxonomizes trust models into decision, evaluation, and management categories, while delineating open challenges for trustworthy 6G architectures.

**Thesis-Level Critique.** This survey constitutes the strongest foundational anchor for the present thesis because it explicitly addresses the heterogeneity problem—multi-domain nodes, divergent technologies, and asymmetric trust requirements—that our Ensemble Trust Model is designed to resolve. The QoT taxonomy directly validates our architectural choices: our variance-based dynamic weighting ($W_d = \frac{1}{1 + \alpha \cdot \sigma^2}$) operationalizes the "dynamicity" and "robustness" criteria by continuously recalibrating domain influence based on signal stability, while the explicit modeling of uncertainty ($m(\Theta)$) within Dempster-Shafer fusion directly addresses the "context-awareness" criterion by refusing to commit evidential mass when sensor reliability degrades. The survey's emphasis on behavior-based models over certificate-based approaches aligns precisely with our thesis's central argument that trust must be treated as a continuously depreciating, behaviorally computed asset rather than a static credential.

However, the survey remains limited in several respects critical to our work. It provides no empirical fusion of QoT criteria with real SDN testbed implementations, whereas our thesis validates all six trust models on a Mininet/OVS/Docker topology with configurable $\alpha$ and $\lambda$ parameters. The survey also lacks explicit mapping to Zero Trust Architecture principles—the "never trust, always verify" paradigm is implicit in the behavior-based models it reviews but never formalized into the policy enforcement framework (PDP/PEP) that our architecture implements. Most significantly, the survey overlooks the temporal dimension of trust entirely; while it catalogs spatial evaluation mechanisms comprehensively, it does not address session ephemerality, temporal decay, or the Freshness-Inertia continuum that forms the backbone of our Ensemble model.

**Contribution to This Thesis.** The QoT taxonomy provides a formal evaluation lens against which our Ensemble model can be benchmarked. We extend the survey's foundational work by operationalizing QoT criteria through specific mathematical mechanisms: dynamicity via exponential decay ($D(t) = e^{-\lambda \cdot t/T}$), robustness via variance-based evidence discounting, and explainability via the Pignistic Probability transformation ($BetP$) that converts belief intervals into actionable, threshold-based decisions.

---

### 2. Dynamic Access Control Method for SDP-based Network Environments (2023)

**Research Objectives.** This work proposes a Reward/Penalty (RP) engine using Exponential Moving Averages (EMA) and a Dynamic Task (DT) engine for zero-trust Software-Defined Perimeter enforcement, enabling least-privilege access via historical trust scoring in simulated environments.

**Thesis-Level Critique.** The RP engine's use of EMA to weight recent behavioral events more heavily than historical ones is conceptually parallel to our variance-based dynamic weighting, but operates at a fundamentally different mathematical level. Where the RP engine directly adjusts a scalar trust score through additive rewards and penalties, our architecture computes variance ($\sigma_k^2$) over a sliding window of observations and converts this statistical measure into a Dempster-Shafer mass function that explicitly quantifies *uncertainty*—a capability entirely absent from the RP/EMA approach. The RP engine cannot distinguish between "I believe this entity is safe" and "I lack sufficient evidence to decide," which is precisely the distinction that our $m(\Theta)$ term captures and that prevents both false grants and false denials from incomplete telemetry.

The DT engine's capacity for non-predefined task generation addresses HetNet heterogeneity at the policy level, complementing our algorithmic approach which addresses heterogeneity at the evidential computation level. However, the simulation-only validation with arbitrary coefficients and no sensitivity analysis significantly limits the work's generalizability. Our thesis explicitly addresses this through parameterized sensitivity analysis across nine adversarial scenarios with configurable $\alpha$ values governing variance penalty amplification.

The RP engine's documented weakness—high fluctuations in trust score differences due to heavy weighting of recent events—is a problem our variance-based approach inherently mitigates through the sliding window mechanism. Rather than directly weighting individual events, we compute the statistical stability of the entire observation window, making the system robust against transient spikes while remaining sensitive to sustained behavioral deviation.

**Contribution to This Thesis.** The SDP enforcement context validates our architectural decision to decouple the trust computation engine from the physical enforcement layer (SDP controllers/gateways). The RP engine's EMA-based temporal weighting represents a simpler alternative to our exponential decay, but lacks the mathematical rigor of DS theory's explicit uncertainty representation.

---

### 3. Trust Threshold Policy for Explainable and Adaptive Zero-Trust Defense in Enterprise Networks (2022)

**Research Objectives.** This work formulates zero-trust defense as a Partially Observable Markov Decision Process (POMDP), deriving an explainable trust-threshold policy that balances security enforcement against network usability through probabilistic belief updates on observations.

**Thesis-Level Critique.** The POMDP formulation represents the most theoretically sophisticated alternative to our Dempster-Shafer fusion approach among the reviewed works. Both frameworks model trust as a partially observable phenomenon—the POMDP treats the true entity state (adversarial vs. legitimate) as hidden and computes belief distributions over possible states via observation-conditioned updates, while our DS-based architecture models trust as an evidential mass distributed across $\{Safe\}$, $\{Unsafe\}$, and $\{Safe, Unsafe\}$ (uncertainty). The critical architectural divergence is that POMDP requires the specification of transition matrices, observation models, and reward functions *a priori*, making it sensitive to model misspecification. Our variance-based DS approach, by contrast, constructs mass functions directly from observed telemetry variance without requiring explicit probabilistic models of attacker behavior—a significant advantage in open HetNet environments where the attacker model is unknown or evolving.

The trust-threshold policy's finding that "highly vulnerable systems or sophisticated attackers require stricter trust thresholds" directly parallels our tiered decision architecture ($T > 0.75$ for Full Access, $0.45 \le T \le 0.75$ for Limited Access, $T < 0.45$ for No Access), but our thresholds are derived from the Pignistic transformation of fused evidential mass rather than from POMDP value iteration. The POMDP approach's focus on single-account enterprise contexts severely constrains its applicability to the multi-domain, multi-entity HetNet scenarios our thesis addresses. Our Ensemble model evaluates trust across four simultaneous telemetry domains with independent variance tracking, each contributing independently to the fused belief state.

The explainability advantage claimed by the POMDP threshold policy is matched by our architecture's Pignistic transformation, which provides a transparent, deterministic mapping from belief intervals to access decisions.

**Contribution to This Thesis.** The POMDP framework validates the theoretical necessity of probabilistic trust modeling but confirms that DS theory's capacity to explicitly model epistemic uncertainty ($m(\Theta)$) without requiring complete probability distributions represents a more operationally deployable approach for heterogeneous environments. The trust-threshold concept directly supports our tiered access architecture.

---

### 4. Tag-Based Trust Evaluation in Zero Trust Architecture (2022)

**Research Objectives.** This work introduces Tag-Based Trust Evaluation (TBTE), combining score-based and criteria-based approaches through fact, prediction, and model tags derived from user and device data, to create explainable, rule-based trust decisions within ZTA Policy Decision Points.

**Thesis-Level Critique.** The TBTE framework addresses a legitimate gap in our architecture: the interpretability layer between raw evidential computation and policy enforcement. While our Dempster-Shafer fusion engine produces mathematically rigorous trust scores, the TBTE approach of decomposing entity attributes into discrete, labeled tags (fact tags for static properties, prediction tags for behavioral forecasts, model tags for computed risk categories) provides a complementary mechanism for translating continuous trust scores into human-readable policy justifications. This could enhance the explainability of our PDP decisions, particularly for compliance auditing where organizations must demonstrate *why* a specific access decision was made.

However, the TBTE framework suffers from a fundamental limitation relative to our thesis: its rule engine operates on static, predefined conditional logic ("if device_health_tag = compromised AND location_tag = external, THEN deny"). This creates precisely the brittle, binary decision structure that our Dynamic Weighting with Temporal Decay is designed to eliminate. Our architecture's "gray-area routing"—where ambiguous evidence results in *Limited Access* rather than a binary Allow/Deny—cannot be replicated by rule-based tag evaluation without exponentially expanding the rule set to cover every intermediate state.

The validation on only 1,000 simulated users and 10 resources is also insufficient for the enterprise-scale scenarios our testbed addresses. The TBTE approach provides no mechanism for temporal decay; a tag assigned at authentication time persists until explicitly updated, creating the same "implicit trust period" vulnerability that our exponential decay function eliminates.

**Contribution to This Thesis.** The tag taxonomy (fact/prediction/model) could serve as a presentation layer atop our evidential fusion engine, translating mass functions into auditable, human-readable tags for compliance purposes. However, tag-based rules cannot replace the continuous, probabilistic nature of our DS-based evaluation.

---

### 5. TrustS: Probability-based Trust Management System in Smart Cities (2022)

**Research Objectives.** TrustS presents a four-state Markov chain model (DOWN/UP/UP-SAFE/UP-UNSAFE) for computing node trust in smart city peer-to-peer overlays, utilizing stationary probabilities for deterministic behavioral assessment independent of overlay topology.

**Thesis-Level Critique.** The Markov chain formulation offers a computationally efficient alternative to our Dempster-Shafer combination rule for resource-constrained environments. The four-state model captures an additional dimension—node availability (DOWN/UP)—that our binary frame ($\Theta = \{Safe, Unsafe\}$) does not explicitly model. This is operationally relevant because our architecture currently assumes continuous sensor availability; a domain that ceases reporting is handled implicitly through variance computation (absent readings increase variance, collapsing the domain weight toward zero), but TrustS's explicit DOWN state provides a cleaner mathematical treatment of intermittent connectivity scenarios common in mobile HetNets and IoT deployments.

However, the Markov model's reliance on accurate transition probability estimation ($\alpha$, the trust coefficient) is directly analogous to the calibration challenge of our sensitivity parameter ($\alpha$ in $W_d = \frac{1}{1 + \alpha \cdot \sigma^2}$). Both systems are sensitive to their respective parameterizations, but our variance-based approach computes weights empirically from observed signal stability, whereas the Markov model requires predetermined transition probabilities—a disadvantage in unknown or rapidly evolving adversarial environments.

The Markov model computes trust deterministically from stationary distributions, meaning it characterizes the *long-run average behavior* of a node. This fundamentally conflicts with our thesis's core argument that trust must be temporally dynamic: the stationary distribution, by definition, is time-invariant. TrustS cannot capture the session ephemerality or temporal decay that our Ensemble model enforces through the Freshness-Inertia continuum.

**Contribution to This Thesis.** The explicit availability state (DOWN/UP) suggests a potential extension to our binary frame to a ternary frame ($\Theta = \{Safe, Unsafe, Unavailable\}$) for IoT deployments. However, the Markov model's time-invariant stationary analysis is architecturally incompatible with our temporal decay requirements.

---

### 6. Targeted Context-Based Attacks on Trust Management Systems in IoT (2023)

**Research Objectives.** This work proposes and demonstrates "context-based attacks" where adversaries spoof contextual properties (e.g., location, device type) to target specific device groups in IoT Trust Management Systems, successfully compromising seven existing trust models and subsequently developing a mitigating TMS using distance scaling and timeout mechanisms.

**Thesis-Level Critique.** This paper exposes a vulnerability that is directly relevant to our architecture's variance-based weighting mechanism. If an attacker can manipulate the *context* rather than the *behavior* of a domain—for example, spoofing a device posture reading to appear consistently healthy when the device is compromised—the variance ($\sigma^2$) would remain low (the spoofed signal is stable), and the dynamic weight would remain high, allowing the compromised domain to retain disproportionate influence in the fusion output. This represents a potential attack vector against our Weighted Belief Fusion pipeline that our current architecture does not explicitly address.

However, our multi-domain fusion architecture provides a natural partial defense against context-based attacks that single-domain trust models lack. An attacker who successfully spoofs one domain's context (e.g., Device posture) must simultaneously maintain consistent spoofing across all four independent domains (Identity, Device, Network, Application) to avoid triggering cross-domain conflict in the Dempster's combination rule. The conflict factor ($\kappa = m_1(S) \cdot m_2(U) + m_1(U) \cdot m_2(S)$) explicitly detects inter-domain disagreements, meaning a spoofed Device domain reporting "Safe" while the Network domain detects anomalous traffic would generate elevated $\kappa$, triggering the normalization mechanism that redistributes evidential mass away from the conflicting sources.

The proposed mitigation using distance scaling and behavioral timeouts is conceptually aligned with our temporal decay mechanism—both impose a finite validity window on trust assessments. The timeout mechanism in the mitigation TMS performs the same function as our exponential decay ($D(t) = e^{-\lambda \cdot t/T}$): forcing periodic re-evaluation regardless of apparent behavioral consistency.

**Contribution to This Thesis.** This work validates the necessity of multi-domain fusion (rather than single-domain evaluation) as a defense against context manipulation, and confirms the importance of temporal expiration mechanisms. It also identifies a concrete attack vector (context spoofing with low variance) that represents a limitation of our variance-based weighting approach, explicitly acknowledged in our Limitations section.

---

### 7. A Probabilistic-Based Trust Evaluation Model Using Hidden Markov Models and Bonus Malus Systems (2011)

**Research Objectives.** This foundational work proposes Hidden Markov Models (HMM) combined with Bonus-Malus Systems (BMS) for evaluating hidden trust states from observable network behaviors, using Expectation-Maximization for parameter estimation and demonstrating applicability to packet-drop detection.

**Thesis-Level Critique.** The HMM-BMS framework shares the core philosophical premise of our architecture: trust is a *hidden state* that must be inferred from observable behavioral evidence. The HMM's emission probabilities (mapping hidden trust states to observable behaviors) are functionally analogous to our DS mass functions (mapping domain telemetry to evidential support for $\{Safe\}$, $\{Unsafe\}$, or $\{Safe, Unsafe\}$). However, the HMM requires the specification of state transition probabilities and emission distributions *a priori* via EM training, whereas our DS approach constructs mass functions directly from observed variance without training data—a critical advantage for zero-day scenarios where the behavioral profile of the threat is unknown.

The BMS component (borrowed from actuarial science) provides a simplified transition mechanism (+1 for good behavior, -1 for bad) that is computationally cheaper than our full Dempster's combination rule with normalization. This efficiency advantage makes HMM-BMS more suitable for resource-constrained edge devices, a limitation we acknowledge in our thesis for our DS-based approach. However, the BMS's binary reward/penalty structure lacks the nuanced uncertainty representation that our $m(\Theta)$ term provides; a node in the BMS model is either rewarded or penalized, with no capacity to express "insufficient evidence to decide."

The 2011 publication date means this work predates the ZTA conceptual framework (NIST SP 800-207, 2020) and therefore lacks integration with modern zero-trust primitives (PDP/PEP structures, SDP enforcement, micro-segmentation). Its single-trustee focus also contrasts with our multi-domain, multi-entity architecture.

**Contribution to This Thesis.** The HMM framework validates probabilistic hidden-state modeling as foundational to trust computation. The BMS mechanism suggests a computationally lighter alternative to DS fusion for edge deployments, which we identify as a future research direction (Decentralized Fusion for Edge and IoMT Constraints).

---

### 8. A Continuous Authentication Protocol Without Trust Authority for Zero Trust Architecture (2022)

**Research Objectives.** This work proposes a blockchain-based (PBFT consensus) continuous device-to-device authentication protocol eliminating centralized Trust Authorities, using ECC for initial authentication and lightweight continuous verification with formal eCK security proofs.

**Thesis-Level Critique.** This protocol addresses a critical assumption in our architecture: the integrity of the initial authentication event. Our Ensemble Trust Model treats the "Freshness" component at $t = 0$ as a given—the initial cryptographic proof is assumed to originate from a compliant Identity Provider. This paper's contribution is the decentralization of that initial trust establishment through blockchain consensus, which eliminates the single-point-of-failure vulnerability inherent in centralized IdP architectures.

The continuous D2D authentication aspect directly complements our temporal decay mechanism. Where our exponential decay forces re-verification by mathematically degrading trust over time (creating the temporal pressure for re-authentication), this protocol provides the *mechanism* for that re-authentication at the cryptographic layer. The two approaches operate at different architectural tiers—our Ensemble model computes *whether* re-authentication is needed (based on $BetP(Safe)$ falling below thresholds), while this blockchain protocol provides *how* that re-authentication is performed without central coordination.

However, the assumption of blockchain availability is operationally challenging for our envisioned HetNet deployments. PBFT consensus requires a minimum quorum of participating nodes, which may not be achievable in disconnected or partitioned network segments. Additionally, the protocol's focus on D2D authentication does not address the multi-domain telemetry evaluation that our four-domain architecture (Identity, Device, Network, Application) performs.

**Contribution to This Thesis.** This work is architecturally complementary: it provides the decentralized cryptographic substrate that our trust computation engine can consume as its initial Freshness input. The combination of blockchain-based initial auth with our DS-fused temporal evaluation represents a complete zero-trust stack from cryptographic verification through behavioral monitoring.

---

### 9. A Critical Analysis of Zero Trust Architecture (2022)

**Research Objectives.** This meta-analysis evaluates ZTA through the lens of classical security patterns and principles, constructs a preliminary Security Reference Architecture (SRA), and critically examines the practical feasibility, overhead costs, and implementability of zero-trust deployments.

**Thesis-Level Critique.** This paper provides essential intellectual discipline for our thesis by mapping ZTA abstractions back to classical security principles: least privilege, complete mediation, fail-safe defaults, and defense in depth. Our architecture explicitly operationalizes several of these principles: the tiered access policy (Full/Limited/No Access) implements least privilege by restricting permissions proportional to evidential support; the continuous evaluation at every time step $t$ implements complete mediation by never caching access decisions; and the explicit modeling of uncertainty ($m(\Theta)$) implements fail-safe defaults by routing uncertain evidence toward access restriction rather than implicit grant.

The critical analysis's exposure of ZTA "hype" versus classical substance serves as a valuable check against overclaiming in our thesis. The paper's finding that ZTA overhead concerns remain empirically unanswered is directly relevant—our testbed validation provides partial empirical answers through measured latencies (2.1ms per evaluation cycle across 25 nodes), but we acknowledge that scaling to enterprise-grade deployments of 10,000+ nodes remains unvalidated.

The pattern-based approach to ZTA design suggests that our Ensemble model could be formalized as a *trust computation pattern* within the broader ZTA pattern catalog, making it reusable across different enforcement technologies (SDP, SASE, ZTNA) without modification to the core DS fusion algorithm.

**Contribution to This Thesis.** The SRA framework and classical principle mapping provide the theoretical grounding for our architectural claims. The overhead critique directs our future work toward empirical performance benchmarking at enterprise scale.

---

### 10. Zero Trust Architecture — NIST SP 800-207 (2020)

**Research Objectives.** The foundational NIST standard defining core ZTA tenets, abstract component architecture (Policy Engine, Policy Administrator, Policy Enforcement Point), deployment models, and migration guidance for federal agencies.

**Thesis-Level Critique.** NIST SP 800-207 is the bedrock standard against which our entire thesis is architecturally validated. Our PDP/PEP decomposition directly implements the Policy Engine/Administrator/Enforcement Point triad defined in this document. The seven tenets of ZTA—particularly "All data sources and computing services are considered resources," "All communication is secured regardless of network location," and "Access to individual enterprise resources is granted on a per-session basis"—are mathematically enforced by our architecture: per-session access is guaranteed by temporal decay ($D(t) \rightarrow 0$ as $t \rightarrow T$), location-independent verification is achieved through multi-domain fusion across Identity, Device, Network, and Application domains, and continuous monitoring is implemented through the sliding-window variance computation that feeds the dynamic weighting engine.

The standard's enterprise focus and abstract nature represent both a strength and a limitation relative to our work. As a strength, it provides vendor-agnostic architectural principles that justify our thesis's deliberate exclusion of proprietary implementations. As a limitation, it offers no mathematical formalization of trust computation—the "Policy Engine" is described functionally but not algorithmically. Our thesis fills this gap by providing the specific mathematical backbone (DS fusion, variance weighting, temporal decay, Pignistic transformation) that operationalizes the abstract Policy Engine into a deployable trust computation pipeline.

The standard predates many of the AI and probabilistic advances reviewed in this literature critique, yet its architectural principles remain fully compatible with our algorithmic extensions. This demonstrates that the NIST framework was designed with sufficient abstraction to accommodate the class of evidential fusion engines our thesis proposes.

**Contribution to This Thesis.** NIST SP 800-207 provides the normative architectural framework within which our Ensemble Trust Model operates. Every component of our seven-stage WBF pipeline—from domain score computation through Pignistic decision—maps directly to a functional requirement within this standard.

---

### 11. An Artificial Intelligence Approach for Deploying Zero Trust Architecture (2022)

**Research Objectives.** This work explores Machine Learning classification algorithms (specifically Decision Trees at 85% accuracy) as an alternative to manual zero-trust policy configuration, aiming to automate the prediction of allow/deny decisions from static firewall configurations in simulated environments.

**Thesis-Level Critique.** The AI-driven policy engine addresses a scalability challenge that our mathematical architecture does not: the *configuration* of trust parameters. Our architecture requires the manual specification of sensitivity parameters ($\alpha$), temporal decay rates ($\lambda$), observation window lengths ($N$), and access thresholds—all of which we currently treat as empirically calibrated constants. An ML classifier that could learn optimal parameter configurations from operational data would represent a valuable automation layer atop our fusion engine.

However, the Decision Tree approach applied in this work operates at a fundamentally different abstraction level than our DS-based fusion. The ML classifier produces binary allow/deny predictions from static configurations, which recreates the very binary decision structure our tiered access architecture (Full/Limited/No Access) was designed to transcend. A Decision Tree cannot output "Limited Access with 26.2% residual uncertainty ($m(\Theta) = 0.262$)"—it can only output a class label. This loss of granularity eliminates the proportional, uncertainty-aware response that constitutes our architecture's primary innovation.

The reliance on synthetic training data is a significant limitation shared with our testbed validation. However, our mathematical approach is deterministic and analytically verifiable (we demonstrate mass function axiom satisfaction by construction), whereas ML models trained on synthetic data face the additional challenge of domain shift when deployed against real-world distributions.

**Contribution to This Thesis.** ML-based policy automation represents a viable future enhancement layer for our architecture, particularly for the dynamic calibration of $\alpha$ and $\lambda$ parameters using supervised learning from operational feedback. We identify this as a future work direction (Unsupervised Machine Learning for Behavioral Inertia).

---

### 12. Integrating Trusted Computing Mechanisms with Trust Models to Achieve Zero Trust Principles (2022)

**Research Objectives.** This work outlines a theoretical framework integrating hardware-based Trusted Computing Group (TCG) mechanisms—specifically TPM modules and Chains of Trust (CoT)—with enterprise trust models to enforce "Never Trust, Always Verify" through continuous hardware/software property attestation.

**Thesis-Level Critique.** TCG integration addresses a fundamental assumption in our architecture's Device domain: that the reported device posture telemetry is authentic and has not been tampered with at the hardware level. Our variance-based weighting can detect *behavioral inconsistency* in device reporting (high variance triggers weight reduction), but it cannot detect a compromised TPM that consistently reports falsified-but-stable posture data. Hardware attestation via CoT provides the cryptographic root-of-trust that validates the authenticity of the signals our fusion engine consumes.

In our architecture, device posture is one of four telemetry domains feeding the DS fusion pipeline. TCG attestation would strengthen this specific domain by providing hardware-verified ground truth, reducing the epistemic uncertainty ($m(\Theta)$) associated with device signals during mass function construction. A hardware-attested device with verified CoT would justify a lower $m(\Theta)$ (higher confidence) compared to a software-only attested device, directly influencing the fusion output.

However, the assumption of universal TPM availability is problematic for heterogeneous environments. BYOD devices, consumer IoT sensors, and legacy embedded systems rarely include TPM 2.0 modules. Our architecture's strength is its graceful degradation in the absence of hardware attestation—the variance-based weighting mechanism treats unreliable or missing attestation signals the same way it treats any unstable telemetry: by discounting the domain weight and shifting mass to uncertainty, ensuring the system degrades safely rather than catastrophically.

**Contribution to This Thesis.** Hardware attestation enhances the trustworthiness of the Device domain's input to our fusion engine. The CoT concept maps directly to our "Freshness" component, providing cryptographic proof of device integrity at session initiation that our temporal decay subsequently depreciates.

---

### 13. Secure Access Service Edge: A Zero Trust Based Framework for Accessing Data Securely (2022)

**Research Objectives.** This work reviews the SASE framework—converging ZTA with SD-WAN, Secure Web Gateways (SWG), and Cloud Access Security Brokers (CASB)—for securing distributed remote workforces with reduced backhaul latency.

**Thesis-Level Critique.** SASE represents the cloud-native enforcement topology within which our Ensemble Trust Model would be deployed at scale. Our architecture's separation of the trust computation engine (PDP) from the enforcement layer (PEP) aligns architecturally with SASE's distributed Points of Presence (POPs), where our DS fusion engine would execute at the POP level to make local access decisions without requiring round-trip consultation with a centralized policy server. This distributed deployment model directly addresses the latency concerns we acknowledge in our testbed limitations.

The SASE framework's incorporation of SWG and CASB provides the application-layer inspection capabilities that correspond to our Application/Data Sensitivity domain. Our thesis evaluates this domain through abstract trust scores ($S_a$), but SASE provides the concrete enforcement mechanisms (URL filtering, DLP policies, API security) that would generate the raw telemetry our fusion engine consumes.

The paper's identification of legacy system migration and hybrid-cloud interoperability as barriers directly parallels our thesis delimitations—we explicitly assume a baseline level of network modernization and exclude legacy mainframe integration. The financial constraints highlighted by the paper also validate our vendor-agnostic approach: by focusing on mathematical algorithms rather than specific SASE vendors, our contributions remain transferable across commercial implementations.

**Contribution to This Thesis.** SASE provides the deployment topology for operationalizing our Ensemble model in cloud-distributed environments. The POP-based architecture validates our PDP/PEP separation and suggests that our DS fusion engine should be designed for edge-distributed execution.

---

### 14. Towards Zero Trust: The Design and Implementation of a Secure End-Point Device for Remote Working (2021)

**Research Objectives.** This work presents "ProGun," a secure USB dongle implementing FIDO2 multi-factor authentication, Risk-Based Authentication (RBA), GPS-based location verification, and encrypted trusted boundaries for remote zero-trust enforcement at the endpoint.

**Thesis-Level Critique.** ProGun provides tangible hardware instantiation of the "Freshness" component in our Ensemble model. At $t = 0$, our architecture requires a cryptographic proof of identity that we abstract as the initial trust score. ProGun's FIDO2 + GPS attestation mechanism generates exactly this proof with hardware-rooted assurance, producing a high-confidence initial Device domain score ($S_d \approx 0.95$) and Identity domain score ($S_i \approx 0.98$) that our temporal decay subsequently depreciates.

The RBA component—triggering additional authentication challenges based on contextual anomalies (new IP, unusual location)—is functionally equivalent to our architecture's behavior when $BetP(Safe)$ crosses a threshold boundary. When our Ensemble model detects that trust has decayed into the "Limited Access" tier, the operational response should be precisely the RBA-style re-authentication challenge that ProGun implements. This establishes a complete feedback loop: our mathematical engine determines *when* re-authentication is needed; ProGun provides *how* it is performed at the hardware level.

However, the device-specific nature of ProGun limits its scalability. The dongle addresses a single endpoint; our architecture evaluates trust across the entire session continuum across four domains simultaneously. The paper acknowledges that its rule-based RBA heuristics are insufficient against advanced session hijacking—precisely the attack vector that our Ensemble model's behavioral inertia mechanism is designed to counter. A session hijacker who lacks the victim's historical behavioral baseline will trigger our Inertia Component collapse regardless of possessing the victim's ProGun token.

**Contribution to This Thesis.** ProGun and similar hardware tokens serve as the physical authentication substrate that feeds our trust computation engine. The ProGun-to-Ensemble pipeline represents a complete zero-trust stack: hardware-rooted initial verification → continuous DS-fused behavioral evaluation → temporally decaying trust → proportional access enforcement.

---

### 15. A Zero Trust Model Based Framework for Data Quality Assessment

**Research Objectives.** This work adapts zero-trust security principles to data quality management, introducing a Zero Trust Data Quality Framework (ZTDQF) that employs a continuous data quality processing engine to separate trusted data from data exceptions based on dynamically evolving standards.

**Thesis-Level Critique.** While tangential to our thesis's focus on network access control, this work provides an instructive cross-domain validation of zero-trust principles. The ZTDQF's core insight—that data quality cannot be established through one-time validation but requires continuous, dynamic assessment—directly mirrors our thesis's central argument that trust cannot be established through one-time authentication. Both frameworks reject the "verify once, trust forever" paradigm.

The continuous data quality processing engine's approach of scoring data against dynamically updating quality standards is structurally analogous to our variance-based weighting: both compute a reliability metric that modulates the degree to which a signal (data record or telemetry reading) is trusted in downstream processing. However, the ZTDQF does not employ evidential fusion or explicit uncertainty modeling, operating instead on deterministic quality thresholds. This means it cannot express "I am uncertain about this data's quality," which is precisely the epistemic state our $m(\Theta)$ term captures.

**Contribution to This Thesis.** The ZTDQF validates the cross-domain applicability of continuous, zero-trust evaluation principles beyond network security. It suggests that our DS-based trust computation framework could be generalized to data quality assurance in enterprise data pipelines—a potential spinoff application.

---

### 16. Design of Network Communication Security Scheme Based on Dynamic Trust Estimation

**Research Objectives.** This work constructs a network communication architecture that dynamically evaluates and updates node trust values using graph-based models, formulating strict communication permission rules combined with encryption and intrusion detection for comprehensive protection.

**Thesis-Level Critique.** The dynamic trust estimation approach shares our thesis's core premise of continuous evaluation, but operates at the network topology level (graph-based node trust) rather than our multi-domain evidential level. The graph constraint—currently restricted to undirected networks—is a significant limitation that our domain-independent fusion approach avoids. Our DS combination rule is agnostic to network topology; it fuses evidence from four independent domains regardless of whether the underlying network is directed, undirected, hierarchical, or mesh.

The work's integration of trust values with encryption and intrusion detection mirrors our architectural vision of embedding trust computation within the broader security stack (alongside SDP controllers, IDS/IPS, and SIEM platforms). However, the static initial weight assignment and predefined equilibrium coefficients introduce the same inflexibility our thesis identifies as the "Peril of Inflexible Calibration" (Section 2.4 of our evaluation chapter). Our variance-based dynamic weighting eliminates static weight assignment by computing weights empirically from observed signal stability at every evaluation epoch.

**Contribution to This Thesis.** The graph-based trust propagation model could complement our point-evaluation architecture by incorporating topological awareness—understanding not just *how trustworthy* an entity is, but *how its trust propagates* through the network graph. This is relevant for our lateral movement defense scenarios.

---

### 17. Dynamic Access Control Architecture of Distribution Master Station Based on Extended Trust Evaluation

**Research Objectives.** This work creates a dynamic access control architecture for power distribution master stations, using an improved isolated forest algorithm for anomaly detection and continuous behavioral trust evaluation to transition from static digital certificate verification.

**Thesis-Level Critique.** This paper provides the strongest Industrial IoT (IIoT) validation context for our thesis's generalizability. The power distribution master station represents a critical infrastructure environment where our Ensemble model's aggressive temporal decay would be operationally justified—the consequences of unauthorized access far exceed those in standard enterprise environments, warranting $\alpha \ge 10$ (aggressive variance penalty) and short session ceilings aligned with NIST AAL3 requirements.

The improved isolated forest algorithm for anomaly detection operates as a complementary mechanism to our variance-based approach. Where our $\sigma^2$ computation detects sustained behavioral deviation, the isolated forest detects individual anomalous traffic patterns. The combination of both—using isolated forest for point anomaly detection and variance for trend anomaly detection—would provide a more comprehensive behavioral monitoring capability than either alone.

However, the work's reliance on statically assigned initial weights and a predefined equilibrium coefficient is precisely the architectural limitation our dynamic variance weighting resolves. Our architecture never assigns static weights; every weight is computed at every evaluation epoch from the rolling variance of the preceding $N$ observations.

**Contribution to This Thesis.** The IIoT/critical infrastructure context validates the operational necessity of our most aggressive parameterizations ($\alpha \ge 10$, short session TTLs). The isolated forest approach suggests a potential enhancement to our anomaly detection capabilities beyond pure variance computation.

---

### 18. Dynamic Model of Malware Propagation Based on Community Structure in Heterogeneous Networks

**Research Objectives.** This work investigates how community structures in heterogeneous networks influence malware propagation dynamics using the VUMRV (Vulnerable-Unprotected-Malfunctioned-Recovered-Vulnerable) epidemiological model, demonstrating that community-based segmentation mathematically restricts the basic reproduction number ($R_0$).

**Thesis-Level Critique.** This epidemiological approach to malware propagation provides the most rigorous mathematical justification for our thesis's micro-segmentation advocacy. The finding that community structure properties mathematically restrict $R_0$ directly validates our architectural claim that tiered access (Full/Limited/No Access) creates effective "community boundaries" that impede lateral movement. In our architecture, when an entity's trust score degrades into "Limited Access," it is mathematically isolated from high-sensitivity resources, creating precisely the community boundary that restricts $R_0$ in this malware propagation model.

The VUMRV model's five-state lifecycle provides a richer representation of entity compromise than our binary trust frame ($\Theta = \{Safe, Unsafe\}$). The intermediate states (Vulnerable but not yet exploited, Recovered but potentially re-infectable) map to our "Limited Access" tier, where an entity is not confirmed compromised but exhibits sufficient risk indicators to warrant privilege restriction. This suggests that our tiered access architecture implicitly implements the community-based containment strategy this paper formally describes.

However, the evaluation on synthetic Barabási-Albert networks lacks the operational realism of our SDN/SDP testbed. Real enterprise topologies exhibit more complex community structures than scale-free random graphs, and the malware propagation dynamics would be influenced by the trust-based access restrictions our architecture imposes—creating a feedback loop between trust computation and propagation dynamics that neither work currently models.

**Contribution to This Thesis.** The $R_0$ restriction framework provides a formal epidemiological justification for our tiered access architecture's effectiveness against lateral movement, strengthening the theoretical foundations of our gray-area routing concept.

---

### 19. Probabilistic Trust Inference Theory to Optimizing Multi-Level Trust in Software Defined Networks

**Research Objectives.** This work proposes Probabilistic Trust Inference Theory (PTIT) combined with Enhanced Lion Optimization (ELO) for multi-level trust management in WSN/SDN environments, using Bayesian inference for continuous trust score updates and achieving significant improvements in energy consumption and throughput.

**Thesis-Level Critique.** The PTIT-ELO framework represents the closest Bayesian alternative to our Dempster-Shafer approach, enabling direct comparison of the two evidential reasoning paradigms. The Bayesian inference pipeline continuously updates trust scores through posterior computation, which functions similarly to our temporal fusion ($m_{cum}^{(t)} = m_{cum}^{(t-1)} \oplus m_{spatial}^{(t)}$). However, the critical distinction is that Bayesian inference requires complete prior probability distributions over all hypotheses, whereas our DS approach permits the explicit assignment of mass to $\Theta$ (total ignorance). In SDN environments where sensor readings may be absent or corrupted, the Bayesian model must either impute a prior (potentially introducing bias) or crash; our DS model assigns vacuous mass ($m(\Theta) = 1.0$), mathematically expressing "no information available" without distorting the fusion output.

The ELO-based cluster formation for secure routing is architecturally relevant to our SDP enforcement layer but operates at a different abstraction level. While our architecture determines *whether* an entity should have access, the PTIT-ELO framework determines *how* traffic should be routed through trusted clusters—a complementary function that could be integrated with our SDP controllers.

The simulation assumption of homogeneous sensor nodes with unlimited base station resources directly contradicts the heterogeneous, resource-constrained environments our thesis targets. Our architecture explicitly handles heterogeneity through independent per-domain variance computation and weight normalization.

**Contribution to This Thesis.** The Bayesian vs. DS comparison validates our choice of DS theory for environments with incomplete telemetry. The SDN-native trust routing concept suggests that our trust scores could directly influence SDN flow table entries for trust-aware traffic engineering.

---

### 20. Timely Data Delivery for Heterogeneous IoT Applications

**Research Objectives.** This work derives optimal update generation policies minimizing Age of Information (AoI) across heterogeneous IoT applications, achieving a two-order-of-magnitude reduction in server energy consumption with 19.9% higher fairness compared to state-of-the-art approaches.

**Thesis-Level Critique.** While not directly addressing zero-trust or access control, this paper's Age of Information concept is directly analogous to our "Data Freshness" component in the Ensemble model. AoI measures the staleness of information at a receiver; our Freshness-Inertia continuum ($W_{fresh}(t) = e^{-3.0 \cdot t/30}$) measures the staleness of the initial cryptographic verification. Both frameworks recognize that information value degrades with time and formalize this degradation mathematically.

The optimization framework balancing AoI, fairness, and energy consumption provides a theoretical basis for optimizing our temporal decay parameters. Our current decay rates are calibrated against compliance standards (NIST SP 800-63B for 30-minute short-term, enterprise KMSI for 48-hour long-term), but an AoI-based optimization could adaptively calibrate these rates based on the actual information arrival patterns of each telemetry domain—domains with high update frequency could tolerate longer decay windows, while domains with sparse updates should trigger faster decay.

**Contribution to This Thesis.** The AoI framework provides a theoretical foundation for adaptive decay rate calibration, which is identified in our future work as a potential enhancement to the Ensemble model's currently static temporal parameters.

---

### 21. Trust as a Service: Building and Managing Trust in the Internet of Things

**Research Objectives.** This work conceptualizes "Trust as a Service" (TaaS) by categorizing IoT trust into three dimensions: verifiable belief-driven trust (secured by Blockchain), statistical evidence-based trust (defended by the M2MTrust model against malicious collectives), and complex cognitive trust (mapped using CNNs).

**Thesis-Level Critique.** The three-dimensional trust taxonomy (belief-driven, evidence-based, cognitive) maps instructively to our architecture. Our Dempster-Shafer fusion engine operates primarily in the "evidence-based" dimension, computing trust from statistical telemetry. The "belief-driven" dimension, secured by blockchain in this work, corresponds to our assumed cryptographic authentication layer (the initial Freshness proof). The "cognitive" dimension—representing latent, complex trust patterns requiring deep learning to uncover—maps to our acknowledged limitation: the variance-based weighting operates without semantic understanding and cannot interpret the *cause* of behavioral deviation.

The M2MTrust model's defense against malicious collectives (coordinated groups of compromised nodes manipulating trust evaluations) exposes a threat vector relevant to our multi-domain architecture. If multiple telemetry domains are simultaneously compromised by a coordinated attack (e.g., an APT controlling both the device and the network), the individual domains would independently report consistent, high-trust readings. Our fusion engine would produce a high $BetP(Safe)$ despite the compromise, because the conflict factor $\kappa$ would be low (all domains agree on "Safe"). The M2MTrust framework's collusion detection mechanisms could enhance our architecture's resilience against this coordinated attack vector.

**Contribution to This Thesis.** The TaaS taxonomy validates our architecture as an evidence-based trust computation engine and identifies the cognitive trust dimension as a future extension requiring ML integration. The collusion detection concept addresses a specific multi-domain attack scenario our current architecture does not explicitly counter.

---

### 22. Zero Trust Security Architecture

**Research Objectives.** This work surveys the paradigm shift from perimeter-based security to Zero Trust Security Architecture (ZTSA) across sectors including Department of Defense, healthcare, and Industrial IoT, highlighting implementations such as quantum fingerprinting, Streebog cryptographic substitution, and the MEDRAF hybrid safety/security risk assessment.

**Thesis-Level Critique.** The cross-sector deployment survey validates our thesis's claim that zero-trust principles are sector-agnostic, but the documented adoption barriers—implementation complexity, financial constraints, and cultural resistance—highlight operational challenges that our mathematical architecture does not address. Our thesis deliberately confines itself to the algorithmic layer, assuming that organizational adoption challenges are external to the trust computation problem. However, the healthcare constraints noted in this survey (financial limitations, legacy medical device integration) directly align with our thesis delimitations regarding the exclusion of legacy protocol security.

The quantum fingerprinting techniques surveyed here provide potential future-proofing for our authentication substrate. As post-quantum cryptographic standards mature, the initial "Freshness" proof consumed by our Ensemble model should transition from classical cryptographic attestation to quantum-resistant mechanisms (ML-KEM), which we identify in our future works section.

**Contribution to This Thesis.** The cross-sector survey confirms the broad applicability of our architectural approach and validates our future work directions regarding quantum-safe authentication and AI-driven anomaly detection.

---

### 23. Zero Trust Using Network Micro Segmentation

**Research Objectives.** This work demonstrates a ZTA network security model utilizing micro-segmentation via traffic whitelisting in a three-tier Azure application, successfully preventing lateral movement by inspecting port and protocol information.

**Thesis-Level Critique.** Micro-segmentation via traffic whitelisting represents the enforcement-layer mechanism that our trust computation engine's decisions control. When our Ensemble model assigns "Limited Access" ($0.45 \le BetP(Safe) \le 0.75$), the *enforcement* of that limitation occurs through precisely the kind of micro-segment boundary this work implements—restricting the entity to specific whitelisted ports and protocols while blocking access to high-sensitivity segments. Our architecture computes the *what* (access tier); micro-segmentation implements the *how* (port/protocol-level enforcement).

The critical limitation identified by both our critique streams—that static whitelisting does not scale to highly dynamic, ephemeral containerized workloads—is directly relevant to our testbed design. Our Docker/LXC-based testbed uses containerized microservices with dynamic IP assignments, which would require the whitelisting rules to be dynamically updated as containers scale. This dynamic policy enforcement is precisely the function of the SDP controllers in our architecture, which consume the trust computation output and translate access tier decisions into flow rules in real-time.

The manual whitelisting approach contrasts with our automated, algorithmic trust computation. Where this work requires administrators to manually define allowed traffic patterns, our architecture *mathematically derives* the appropriate access restrictions from the fused evidential state, eliminating manual configuration and enabling real-time adaptation to changing threat contexts.

**Contribution to This Thesis.** Micro-segmentation provides the network-level enforcement mechanism for our trust computation outputs. The Azure three-tier deployment validates the applicability of our architecture to cloud-native environments. The scaling limitation of static whitelisting confirms the necessity of our dynamic, algorithmic approach.

---

## Cumulative Synthesis: Positioning the Ensemble Trust Model

The 23 works reviewed above collectively illuminate the landscape within which this thesis's Ensemble Trust Model is positioned. Several key synthesis observations emerge:

**Evidential Reasoning Paradigm.** Among the probabilistic approaches surveyed—Bayesian inference (PTIT-ELO), Hidden Markov Models (HMM-BMS), POMDP belief states, and Markov chain stationary distributions (TrustS)—Dempster-Shafer theory uniquely provides explicit uncertainty representation ($m(\Theta)$) without requiring complete prior distributions. This capacity to mathematically express "I don't know" is the decisive advantage in heterogeneous environments where sensor availability is intermittent and attacker models are unknown.

**Temporal Dimension Gap.** A striking deficiency across the surveyed literature is the near-universal absence of temporal decay mechanisms. The survey on HetNet trust models, the POMDP framework, the tag-based evaluation, and the Markov models all compute trust at discrete time points without mathematically enforcing session ephemerality. Our thesis fills this gap through the Freshness-Inertia continuum, which treats trust as a time-dependent, depreciating asset.

**Multi-Domain Fusion vs. Single-Domain Evaluation.** The context-based attack paper demonstrates that single-domain trust evaluation is inherently vulnerable to context spoofing. Our four-domain fusion architecture provides structural resilience through Dempster's combination rule, which detects inter-domain conflict ($\kappa$) when spoofed domains disagree with honest ones. This multi-domain approach is architecturally superior to every single-domain trust model reviewed.

**Enforcement Layer Complementarity.** The SDP, SASE, micro-segmentation, and ProGun works provide the enforcement mechanisms that our trust computation engine's outputs control. This confirms our thesis's architectural decision to separate trust *computation* (PDP) from trust *enforcement* (PEP), enabling the same algorithmic engine to drive heterogeneous enforcement technologies.

**Identified Extensions.** The literature collectively suggests three primary extensions to our architecture: (1) hardware-rooted attestation via TCG/TPM to validate telemetry authenticity, (2) AI-driven parameter optimization for $\alpha$ and $\lambda$ calibration, and (3) collusion detection mechanisms to counter coordinated multi-domain compromise. These align with the future work directions identified in our thesis conclusions.
