# Trust Computation in Zero Trust and SDP: A Survey of Architectural and Algorithmic Gaps

---

**Abstract.** Zero Trust Architecture (ZTA), codified by NIST SP 800-207, and Software-Defined Perimeters (SDP), specified by the Cloud Security Alliance Specification v2.0 and Architecture Guide, have established mature architectural frameworks for network security in heterogeneous enterprise environments. However, a critical examination reveals that while the *architecture* of trust enforcement has achieved considerable standardisation, the *algorithmic calculus* of trust computation — how trust is quantified, fused, temporally managed, and translated into enforcement decisions — remains fundamentally underspecified. This survey introduces a structured evaluation framework comprising six criteria — uncertainty handling, temporal decay support, multi-domain fusion, enforcement-computation separation, scalability, and explainability — and systematically assesses NIST SP 800-207, CSA SDP v2.0, and seven representative trust computation models against this framework. The analysis reveals consistent architectural gaps: no standardised mechanism for evidential uncertainty representation, no specification of temporal decay dynamics, no normative multi-domain fusion logic, and persistent coupling between trust computation and enforcement. From this gap analysis, we synthesise six formal requirements for dynamic trust evaluation (R1–R6) and present the DCTA Ensemble Model — integrating Dempster-Shafer evidential fusion, variance-based adaptive weighting, and exponential temporal decay — as one candidate architecture satisfying all six requirements. The paper concludes with actionable recommendations for NIST SP 800-207 revision, CSA SDP v3.0 extension, IETF trust metadata standardisation, and community benchmarking initiatives.

**Keywords:** Zero Trust Architecture, Software-Defined Perimeter, trust computation, Dempster-Shafer theory, temporal decay, evidence fusion, survey, evaluation framework, NIST SP 800-207, CSA SDP

---

## 1. Introduction

### 1.1 From Perimeters to Principles

The evolution of network security over the past three decades traces a trajectory from physical topology to logical principle. The perimeter-based model — firewalls guarding a defensible boundary between a trusted interior and an untrusted exterior — dominated enterprise security architecture from the late 1990s through the mid-2010s (Stafford, 2023). Its foundational assumption — that network location is a reliable proxy for trustworthiness — was tenable when enterprise computing was confined to on-premises data centres with well-defined boundaries and homogeneous device populations.

That assumption has been systematically invalidated by four converging forces. First, *multi-cloud adoption* distributes applications, data, and services across heterogeneous cloud providers with fundamentally different security postures and telemetry formats (Al-Mutairi & Hassan, 2024). Second, *BYOD and IoT proliferation* introduces unmanaged, resource-constrained devices that cannot host enterprise security agents and whose security posture the enterprise cannot guarantee (Habib et al., 2022). Third, *remote and hybrid work normalisation* dissolves the assumption that legitimate users operate from predictable network locations (Buck et al., 2022). Fourth, *containerised and serverless architectures* create ephemeral workloads whose network identities change on sub-second timescales, rendering static firewall rules and IP-based access control lists architecturally obsolete (Cloud Security Alliance, 2025).

The response to this dissolution has crystallised around two complementary frameworks. NIST Special Publication 800-207 (Rose et al., 2020) codifies Zero Trust Architecture (ZTA) as a set of principles — "never trust, always verify," assume breach, least privilege — and defines the logical component architecture (Policy Engine, Policy Administrator, Policy Enforcement Point) through which these principles are operationalised. The Cloud Security Alliance's Software-Defined Perimeter (SDP) Specification v2.0 (Cloud Security Alliance, 2022) and Architecture Guide (Cloud Security Alliance, 2024) provide the enforcement substrate: cryptographic session establishment via Single Packet Authorization (SPA), mutual TLS for all communications, and a rigorous Join/Leave lifecycle that eliminates implicit trust at the network boundary.

### 1.2 The Problem: Architectural Containers Without Algorithmic Content

Together, ZTA and SDP provide *architectural containers* for trust-based access control — they define *where* trust decisions are made (Policy Engine), *how* they are enforced (PEP/SDP Gateway), and *what* inputs are consumed (identity, device posture, network context, behavioural signals). What they conspicuously do not provide is the *algorithmic content* that populates these containers: the mathematical specification of how heterogeneous, potentially conflicting, temporally decaying evidence from multiple domains is fused into a continuous trust score, how uncertainty is represented and propagated, and how the resulting score drives graduated enforcement decisions.

This is not an oversight. NIST deliberately left the Trust Algorithm unspecified to preserve vendor-agnostic generality (Rose et al., 2020). CSA SDP focuses on cryptographic session establishment rather than post-authentication trust dynamics (Cloud Security Alliance, 2022). The result, however, is an implementation vacuum: security architects confronted with an unspecified Trust Algorithm default to simplistic weighted-sum scoring or opaque vendor-proprietary algorithms that lack mathematical rigour, uncertainty awareness, and temporal dynamics (Xu, 2024; Shin et al., 2025).

### 1.3 Scope and Contribution

This survey makes three contributions:

1. **Evaluation Framework.** We introduce a structured, six-criteria evaluation framework for assessing trust computation in ZTA and SDP deployments (Section 2). This framework provides the first systematic benchmark against which both architectural standards and algorithmic proposals can be comparatively assessed.

2. **Systematic Gap Analysis.** We apply this framework to NIST SP 800-207, CSA SDP v2.0, and seven representative trust computation models spanning probabilistic, evidential, and machine learning paradigms (Sections 3–6). The analysis reveals consistent gaps — no uncertainty handling, no temporal decay, no multi-domain fusion, and enforcement-computation coupling — that persist across all surveyed approaches.

3. **Synthesised Requirements and Candidate Architecture.** From the gap analysis, we derive six formal requirements for dynamic trust evaluation (R1–R6) and present the DCTA Ensemble Model as one candidate architecture satisfying all requirements, alongside comparative analysis with alternative proposals (Section 7). We conclude with actionable recommendations for standardisation (Section 9) and open research challenges (Section 8).

### 1.4 Paper Organisation

The remainder of this paper is organised as follows. Section 1.5 details the survey methodology, establishing the search strategy, screening process, and bias mitigation measures that underpin the literature corpus. Section 2 defines the evaluation framework. Section 3 establishes the foundations of trust computation. Section 4 analyses ZTA principles and components. Section 5 examines SDP as an enforcement substrate. Section 6 identifies and maps the gaps. Section 7 synthesises requirements and presents candidate architectures. Section 8 discusses open challenges. Section 9 offers standardisation recommendations. Section 10 concludes.

### 1.5 Survey Methodology

Before presenting the evaluation framework and its application, it is necessary to establish the systematic process by which the literature corpus was assembled, screened, and evaluated. This section documents the search strategy, inclusion criteria, and bias mitigation measures that ensure the survey's coverage is comprehensive, reproducible, and free from systematic bias.

#### 1.5.1 Search Strategy and Database Coverage

The literature search was conducted across six academic databases and three standards repositories to capture the full breadth of trust computation research across network security, formal methods, artificial intelligence, and distributed systems communities:

**Academic databases:**
1. IEEE Xplore Digital Library
2. ACM Digital Library
3. Elsevier ScienceDirect (including *Computers & Security*, *Information Fusion*, and *Journal of Information Security and Applications*)
4. Springer Nature (including *Lecture Notes in Computer Science*)
5. MDPI Open Access Journals (including *Electronics* and *Applied Sciences*)
6. Google Scholar (for cross-referencing and citation-chain discovery)

**Standards and industry repositories:**
1. NIST Special Publications (SP 800-207, SP 800-63B)
2. Cloud Security Alliance Research Library (SDP Specification v2.0, SDP Architecture Guide v2, ZTA Best Practices)
3. CISA Publications (Zero Trust Maturity Model v2.1)

The search employed a structured Boolean query strategy combining three thematic axes:

- **Axis 1 (Architecture):** "Zero Trust" OR "Software-Defined Perimeter" OR "SDP" OR "Zero Trust Architecture" OR "ZTA" OR "Software-Defined Perimeter Network"
- **Axis 2 (Trust Computation):** "trust computation" OR "trust evaluation" OR "trust model" OR "trust algorithm" OR "trust score" OR "continuous authentication" OR "adaptive access control" OR "risk assessment"
- **Axis 3 (Technique):** "Dempster-Shafer" OR "evidence theory" OR "Bayesian trust" OR "temporal decay" OR "evidence fusion" OR "subjective logic" OR "variance-based weighting" OR "POMDP" OR "reinforcement learning" OR "machine learning" AND "access control"

Searches were executed as **Axis 1 AND (Axis 2 OR Axis 3)** to ensure retrieval of works addressing trust computation within ZTA/SDP contexts, as well as trust computation techniques with potential applicability to these architectures. Additionally, title-only searches were conducted for specific mathematical frameworks ("Dempster-Shafer" AND "network security"; "temporal decay" AND "trust") to capture technique-specific contributions that may not explicitly reference ZTA or SDP in their abstracts.

#### 1.5.2 Temporal Scope and Inclusion Criteria

The search applied a dual-horizon temporal scope mirroring the survey's own analytical framework:

**Primary window (2020–2025).** The publication of NIST SP 800-207 in August 2020 established the definitive architectural reference for Zero Trust. All works published from 2020 onward that address trust computation within ZTA, SDP, or SDN-based access control frameworks were considered for inclusion. This window captures the post-NIST literature in which trust computation proposals could be assessed against a stable architectural reference.

**Seminal works (pre-2020).** Foundational contributions that define the mathematical frameworks underpinning trust computation were included regardless of publication date. These include Shafer's (1976) formulation of the mathematical theory of evidence, Saltzer and Schroeder's (1975) articulation of security design principles, Smets' (1990) transferable belief model and Pignistic transformation, Mui et al.'s (2002) computational model of trust and reputation, Kreutz et al.'s (2015) comprehensive SDN survey, and Jøsang's (2016) formalisation of subjective logic. These seminal works provide the theoretical substrate upon which contemporary trust computation models are constructed and against which they must be evaluated.

**Inclusion criteria.** A work was included if it satisfied at least one of the following conditions:

1. **Architectural specification:** The work defines or extends a formal architecture for zero trust or software-defined perimeter deployment (e.g., NIST SP 800-207; CSA SDP v2.0; Lefebvre et al., 2023).
2. **Trust computation algorithm:** The work proposes, implements, or evaluates a mathematical model for computing trust scores from observable evidence in networked environments (e.g., Li et al., 2024; Ge & Zhu, 2022; Liu et al., 2023).
3. **Evidence fusion or uncertainty handling:** The work addresses the formal combination of evidence from multiple sources with explicit treatment of uncertainty, conflict, or incomplete information (e.g., Shafer, 1976; Jøsang, 2016; Smets, 1990).
4. **Temporal trust dynamics:** The work models the depreciation, evolution, or session-aware management of trust over time (e.g., Robbins et al., 2025; Alsubhi et al., 2024).
5. **Enforcement architecture:** The work addresses the translation of trust evaluations into network-level or application-level access control actions (e.g., Ali et al., 2024; Al-Mutairi & Hassan, 2024).
6. **Survey or systematisation of knowledge:** The work provides a structured review of ZTA, SDP, or trust computation that contextualises the present survey's scope (e.g., Buck et al., 2022; Alawida et al., 2024; Moubayed et al., 2022).

**Exclusion criteria.** Works were excluded if they:

- Addressed trust in exclusively social or e-commerce contexts without network security applicability.
- Proposed cryptographic primitives (key exchange, encryption algorithms) without connection to trust computation or access control logic.
- Were non-peer-reviewed blog posts, vendor white papers lacking technical depth, or duplicate preprints superseded by published versions.
- Were published in predatory or non-indexed venues as determined by Beall's criteria and Scopus indexing status.

#### 1.5.3 Screening and Selection Process

The search and selection process followed a three-phase screening methodology informed by the PRISMA framework (Page et al., 2021), adapted for a survey of architectural and algorithmic contributions rather than clinical interventions:

**Phase 1 — Identification.** The structured Boolean queries across six databases and three standards repositories yielded an initial corpus. Duplicate records were removed using DOI-based and title-based deduplication.

**Phase 2 — Screening.** Titles and abstracts of the deduplicated corpus were screened against the inclusion and exclusion criteria. Works that clearly fell outside the scope (e.g., social trust in e-commerce, pure cryptographic protocol design) were eliminated. Works whose relevance was ambiguous from the abstract alone were retained for full-text review.

**Phase 3 — Eligibility and Inclusion.** Full texts of the screened corpus were assessed for substantive contribution to at least one of the six evaluation criteria (C1–C6) defined in Section 2. Works that provided no assessable contribution to any criterion — for instance, works that discuss ZTA conceptually without proposing or evaluating a trust computation mechanism — were excluded from the comparative assessment tables (Tables 1, 3, 5, 7) but were retained as contextual references where they informed the architectural analysis (Sections 4–5).

Additionally, **backward citation chaining** (reviewing the reference lists of included works) and **forward citation chaining** (identifying subsequent works citing included papers via Google Scholar) were employed to capture relevant contributions not retrieved by the initial database queries. This snowball sampling is particularly important for identifying seminal mathematical works (e.g., Shafer, 1976) that predate the ZTA terminology but provide the foundational apparatus for trust computation.

#### 1.5.4 Source Classification Taxonomy

To ensure balanced coverage across the heterogeneous trust computation landscape, included works were classified into five *methodological* categories for the purpose of corpus assembly and paradigm balance. This classification is distinct from the *analytical* taxonomy presented in Section 6.2, which organises models by their algorithmic approach for comparative evaluation; the methodological taxonomy here governs search coverage, while the analytical taxonomy governs assessment structure.

| Category | Description | Representative Works |
|:---|:---|:---|
| **Architectural standards** | Normative specifications from standards bodies defining ZTA/SDP architecture | NIST SP 800-207; CSA SDP v2.0; CSA Architecture Guide v2; CISA ZTM v2.1 |
| **Probabilistic models** | Trust computation using Bayesian inference, Markov processes, or POMDP formulations | Li et al. (2024); Ge & Zhu (2022); TrustS Markov model |
| **Evidential models** | Trust computation using Dempster-Shafer theory, subjective logic, or evidence discounting | Shafer (1976); Liu et al. (2023); Jøsang (2016); Smets (1990) |
| **Machine learning models** | Trust computation or access policy generation using supervised, unsupervised, or adversarial ML | Alsubhi et al. (2024); Ali et al. (2024) |
| **Rule-based and hybrid models** | Trust evaluation through tag decomposition, rule engines, or blockchain-anchored authentication | Zhang et al. (2022); Meng et al. (2022) |

The inclusion of all five categories ensures that the survey's comparative assessment (Tables 5 and 7) spans the full methodological spectrum rather than privileging any single approach. The six-criteria evaluation framework (Section 2) was applied uniformly across all categories.

#### 1.5.5 Measures to Ensure Comprehensiveness and Mitigate Bias

Five specific measures were implemented to ensure that the literature coverage was comprehensive and that the comparative assessment was free from systematic bias:

**1. Multi-database triangulation.** Searching six independent academic databases and three standards repositories minimises the risk of missing relevant works due to database-specific indexing gaps. IEEE Xplore and ACM DL provide primary coverage of networking and security venues; ScienceDirect and Springer capture interdisciplinary journals; MDPI captures open-access contributions; Google Scholar provides cross-referencing and grey literature discovery.

**2. Paradigm-balanced source classification.** The five-category taxonomy (Section 1.5.4) was established *before* the comparative assessment to ensure that each methodological paradigm — probabilistic, evidential, machine learning, rule-based, and architectural — received deliberate representation. This prevented the natural tendency to over-sample works from the paradigm most closely aligned with the survey's own candidate architecture (Dempster-Shafer evidential models).

**3. Conservative assessment scoring.** The scoring method (Section 2.3) mandates that where ambiguity exists, the more conservative assessment is applied. The operational consequence of this principle is uniform self-application: the DCTA Ensemble Model's own scalability assessment (C5) received a partial support rating (◐) rather than full support (✓) because enterprise-scale validation (10,000+ concurrent sessions) has not been empirically demonstrated — the same conservative standard applied to all other models.

**4. Transparent candidate positioning.** The DCTA Ensemble Model is presented explicitly as "one candidate architecture, not as the sole solution" (Section 7.2, Note). The survey deliberately includes three alternative proposals (POMDP, Blockchain Authentication, TBTE) and provides a structured comparative table (Table 7) that highlights their respective strengths, preventing the appearance of predetermined conclusions. The evaluation framework (Section 2) was designed to be model-agnostic: any trust computation model — including those not yet proposed — can be assessed against the same six criteria.

**5. Inclusion of critical and adversarial perspectives.** The survey deliberately includes works that challenge or complicate the assumptions underlying dynamic trust computation: Ali et al.'s (2024) analysis of adversarial attacks on AI-based intrusion detection exposes the vulnerability of machine learning classifiers to data poisoning; Ge and Zhu's (2022) POMDP formulation demonstrates that optimal trust policies can be derived from first principles without evidential fusion; and the limitations analysis (Section 8) explicitly identifies unsolved challenges — hardware attestation gaps, federated learning poisoning risks, privacy-computation trade-offs — that affect all surveyed approaches including the DCTA model.

#### 1.5.6 Limitations of the Survey Methodology

Three methodological limitations are acknowledged:

1. **Language restriction.** The search was limited to English-language publications. Trust computation research published in Chinese, Korean, or other languages — particularly from venues not indexed in the six databases — may be underrepresented.

2. **Recency bias in the primary window.** The 2020–2025 primary window prioritises post-NIST SP 800-207 literature. Trust computation proposals published before 2020 that do not explicitly reference Zero Trust may be underrepresented even if their algorithmic contributions are relevant. The inclusion of seminal pre-2020 works partially mitigates this limitation, but a systematic retrospective search of pre-2020 trust computation literature was not conducted.

3. **Vendor and proprietary exclusion.** Commercial ZTA platforms (Zscaler, Palo Alto Prisma Access, Google BeyondCorp, Microsoft Entra) implement production-grade trust computation but do not publish their algorithmic details. Their exclusion is methodologically necessary — opaque systems cannot be assessed against formal criteria — but limits the survey's coverage of operationally deployed approaches.

---

## 2. Evaluation Framework for Trust Computation

### 2.1 Motivation

As the survey methodology (Section 1.5) establishes, the literature corpus spans communities with fundamentally different vocabularies, assumptions, and success metrics. A network security researcher evaluates trust models by breach containment efficacy; a formal methods researcher evaluates them by mathematical soundness; a distributed systems researcher evaluates them by scalability under concurrency. The absence of a common evaluation framework hampers cross-paradigm comparison and impedes the identification of structural gaps that persist across otherwise unrelated approaches. This section introduces a six-criteria framework designed to provide that unified assessment lens.

### 2.2 Criteria Definition

**C1: Uncertainty Handling.** The ability to explicitly represent incomplete, conflicting, or absent evidence without forcing a binary trusted/untrusted classification. Full support requires a mathematical apparatus — such as Dempster-Shafer mass functions, Bayesian posterior distributions, or subjective logic opinion triplets — that can express "insufficient evidence to decide" as a first-class evidential state distinct from both trust and distrust. Partial support includes systems that handle missing evidence through imputation or default values but lack explicit uncertainty quantification. No support characterises systems that require complete evidence to produce a determination and treat missing data as either implicitly safe or implicitly dangerous.

**C2: Temporal Decay Support.** The provision of mechanisms for trust depreciation over time, ensuring that the evidentiary weight of past authentication and behavioural observations diminishes according to a specified function (linear, exponential, or sliding-window). Full support requires a configurable decay function with parameterised rate constants and session-awareness. Partial support includes session timeouts or periodic re-authentication that enforce temporal bounds without continuous decay. No support characterises systems where trust, once established, persists indefinitely until explicitly revoked.

**C3: Multi-Domain Fusion.** The capability to combine evidence from multiple independent telemetry domains — minimally identity, device, network, and application/data — into a unified trust assessment. Full support requires a formal fusion operator (e.g., Dempster's Rule, Bayesian updating, weighted aggregation with conflict detection) that preserves inter-domain independence and detects cross-domain disagreement. Partial support includes systems that consume multiple inputs but combine them through ad hoc or unspecified mechanisms. No support characterises single-domain evaluation systems.

**C4: Enforcement-Computation Separation.** The architectural decoupling of trust computation (Policy Decision Point) from policy enforcement (Policy Enforcement Point), enabling the trust engine to drive heterogeneous enforcement technologies without modification to the computation logic. Full support requires a defined interface between computation and enforcement with standardised trust score exchange. Partial support includes systems where the computation and enforcement are logically separable but not standardised. No support characterises monolithic systems where trust evaluation is embedded within the enforcement mechanism.

**C5: Scalability.** Performance under increasing numbers of nodes, sessions, and telemetry sources. Full support requires demonstrated or analytically bounded performance at enterprise scale (10,000+ concurrent sessions). Partial support includes small-to-medium scale validation. No support indicates no scalability analysis.

**C6: Explainability.** The transparency of trust decisions for audit, compliance, and human review. Full support requires that the trust engine can produce a human-readable rationale for each access decision, identifying which domains, which evidence, and which thresholds contributed to the outcome. Partial support includes systems that provide aggregate scores with limited decomposition. No support characterises black-box systems that produce decisions without interpretable rationale.

### 2.3 Scoring Method

Each surveyed model and architecture is assessed against the six criteria using the following scale:

| Symbol | Meaning |
|:---:|:---|
| ✓ | **Fully supports**: criterion is explicitly addressed with formal specification or demonstrated capability |
| ◐ | **Partial support**: criterion is acknowledged or partially addressed but lacks formal completeness |
| ✗ | **No support**: criterion is not addressed or is structurally absent |

Assessments are derived from published specifications, reference implementations, and peer-reviewed evaluations. Where ambiguity exists, the more conservative assessment is applied.

---

## 3. Foundations of Trust in Heterogeneous Networks

### 3.1 Definitions

**Trust** is the quantified expectation that an entity will behave consistently with a set of security policies during a specified time interval (Jøsang, 2016). Unlike authentication — which verifies identity at a discrete temporal boundary — trust is inherently continuous, contextual, and depreciating.

**Trustworthiness** is the objective property of an entity that determines whether it merits trust. Trust is the *evaluator's subjective assessment* of trustworthiness; the two are related but distinct. A trustworthy entity may be distrusted due to insufficient evidence, and an untrustworthy entity may be trusted due to sophisticated deception (Wang et al., 2022).

**Reputation** is the aggregated trust assessment of an entity across multiple evaluators over time. Reputation systems synthesise multi-source trust evaluations into a community-level assessment, introducing transitivity properties that individual trust assessments lack (Mui et al., 2002).

### 3.2 Properties of Trust

Trust in heterogeneous networks exhibits six fundamental properties that any computational model must accommodate:

1. **Subjectivity.** Trust is evaluator-relative: two evaluators with different evidence may assign different trust levels to the same entity (Wang et al., 2022).

2. **Dynamicity.** Trust changes over time in response to observed behaviour, contextual shifts, and environmental conditions. A static trust assignment is an oxymoron in dynamic environments (Alsubhi et al., 2024).

3. **Context-awareness.** The same entity may warrant different trust levels in different operational contexts — a fully patched workstation on a corporate LAN versus the same workstation on public Wi-Fi (Al-Sanjary et al., 2023).

4. **Asymmetry.** Trust is directional: entity A's trust in entity B need not equal B's trust in A. This is particularly relevant in client-server and IoT-gateway relationships.

5. **Non-transitivity.** Trust is not generally transitive: A's trust in B and B's trust in C do not necessarily imply A should trust C. Where transitivity is modelled, it requires explicit discount functions (Jøsang, 2016).

6. **Partiality.** Trust may be domain-specific: an entity may be trusted for data integrity but distrusted for availability. Multi-domain evaluation captures this property; single-score systems conflate it.

### 3.3 Trust Model Taxonomy

Trust models in heterogeneous networks can be classified into three functional categories:

**Trust Decision Models** determine the access outcome given a trust evaluation — they map continuous trust scores to discrete actions (grant, constrain, deny). Examples include threshold-based policies, POMDP-derived optimal policies (Ge & Zhu, 2022), and rule-based tag evaluation systems (Zhang et al., 2022).

**Trust Evaluation Models** compute the trust score from observable evidence. These range from deterministic weighted sums to probabilistic models (Bayesian networks, Hidden Markov Models), evidential models (Dempster-Shafer theory, subjective logic), and machine learning classifiers (decision trees, deep neural networks).

**Trust Management Models** govern the lifecycle of trust — initialisation, propagation, update, decay, and revocation. These models address how trust is established for new entities, how it evolves during sessions, and how it is transferred across domain boundaries or administrative zones.

A complete trust architecture requires models from all three categories operating in concert. The gap identified in this survey is that ZTA and SDP provide trust decision architecture (the PE/PA/PEP triad) and trust management infrastructure (SDP Join/Leave lifecycle) but leave trust evaluation — the algorithmic core — unspecified.

### 3.4 Key Mathematical Frameworks

#### 3.4.1 Subjective Logic

Subjective logic, formalised by Jøsang (2016), extends classical probability by representing belief states as *opinion triplets* $\omega = (b, d, u)$, where $b$ is belief, $d$ is disbelief, and $u$ is uncertainty, satisfying $b + d + u = 1$. The projected probability is $P = b + au$, where $a$ is the base rate (prior probability). Subjective logic provides operators for cumulative fusion, averaging fusion, and discount-based trust transitivity, making it a comprehensive framework for multi-source trust computation. Its explicit uncertainty term $u$ directly addresses criterion C1.

#### 3.4.2 Dempster-Shafer Theory

Dempster-Shafer (DS) theory operates over a frame of discernment $\Theta$ — a finite, exhaustive set of mutually exclusive states. A basic probability assignment (BPA) $m: 2^\Theta \to [0,1]$ satisfies $m(\emptyset) = 0$ and $\sum_{A \subseteq \Theta} m(A) = 1$. For a binary trust frame $\Theta = \{\text{Safe}, \text{Unsafe}\}$, the three focal elements are $\{\text{Safe}\}$, $\{\text{Unsafe}\}$, and $\Theta$ itself, where $m(\Theta)$ represents epistemic uncertainty (Shafer, 1976).

Two independent mass functions $m_1$ and $m_2$ are combined via Dempster's Rule:

$$
m_{1,2}(A) = \frac{1}{1-\kappa} \sum_{\substack{B \cap C = A \\ B, C \subseteq \Theta}} m_1(B) \cdot m_2(C), \quad A \neq \emptyset
$$

where $\kappa = \sum_{B \cap C = \emptyset} m_1(B) \cdot m_2(C)$ is the inter-source conflict. The rule is commutative, associative, and admits the vacuous function $m(\Theta) = 1$ as identity — properties essential for incremental, order-independent multi-domain fusion (Jøsang, 2016). The Pignistic transformation $BetP(x) = \sum_{x \in A} m(A)/|A|$ converts mass functions to actionable probabilities (Smets, 1990).

#### 3.4.3 Belief Fusion Strategies

Three fusion strategies are distinguished in the trust computation literature:

- **Cumulative fusion** treats each evidence source as independent and combines them conjunctively, amplifying concordant evidence and detecting conflict. Dempster's Rule is the canonical cumulative operator.
- **Averaging fusion** computes a consensus by averaging mass functions across sources, preserving uncertainty without amplification. This is suitable when sources are not independent.
- **Weighted fusion** modulates each source's influence by a reliability or quality weight before combination. The DCTA's variance-based weighting ($W_k = (1 + \alpha\sigma_k^2)^{-1}$) is an instance of weighted fusion where the weight is empirically derived from signal stability.

#### 3.4.4 Temporal Decay Models

Three temporal decay functions appear in the trust computation literature:

**Linear decay:** $D(t) = \max(0, 1 - \lambda t)$. Simple but imposes a hard trust-to-zero deadline and decays too aggressively for short sessions and too slowly for long sessions.

**Exponential decay:** $D(t) = e^{-\lambda t/T}$. Asymptotically approaches zero, never reaching it — mathematically encoding the principle that historical evidence retains infinitesimal but non-zero weight. The rate constant $\lambda$ and window $T$ are independently configurable. This is the dominant model in continuous trust evaluation (Robbins et al., 2025).

**Sliding window:** Trust is computed from only the most recent $N$ observations, with observations outside the window receiving zero weight. This provides a hard temporal bound but introduces discontinuities at window boundaries that can be exploited by adversaries timing their attacks to coincide with window transitions.

---

## 4. Zero Trust Architecture: Principles and Components

### 4.1 Core Tenets

NIST SP 800-207 formalises Zero Trust through seven tenets that collectively invert the assumptions of perimeter-based security (Rose et al., 2020):

1. All data sources and computing services are considered resources.
2. All communication is secured regardless of network location.
3. Access to individual enterprise resources is granted on a per-session basis.
4. Access is determined by dynamic policy — including observable state of client identity, application/service, and requesting asset.
5. The enterprise monitors and measures the integrity and security posture of all owned and associated assets.
6. All resource authentication and authorisation are dynamic and strictly enforced before access is allowed.
7. The enterprise collects as much information as possible about the current state of assets and uses it to improve security posture.

These tenets establish the *what* of Zero Trust: continuous verification, per-session access, dynamic policy. They do not specify the *how* — the algorithmic mechanisms by which these principles are computationally operationalised.

### 4.2 Logical Components

The PE–PA–PEP triad constitutes the logical core:

- **Policy Engine (PE).** Consumes contextual telemetry — identity assurance, device posture, behavioural analytics, resource sensitivity, threat intelligence — and produces an access determination. The PE is the architectural locus where trust computation should reside.
- **Policy Administrator (PA).** Translates the PE's determination into an actionable instruction: provisioning or revoking credentials, configuring tunnels, issuing tokens.
- **Policy Enforcement Point (PEP).** Enforces the PA's instruction at the data path boundary — permitting, constraining, or terminating traffic.

The tripartite design elegantly separates decision from enforcement. However, the PE's internal logic — the Trust Algorithm — is described functionally but not algorithmically. NIST identifies four input categories (identity, device, behavioural, resource sensitivity) and two algorithmic styles (criteria-based binary evaluation versus score-based weighted computation) but provides no normative guidance on fusion methods, weighting schemes, temporal dynamics, or uncertainty handling (Rose et al., 2020).

### 4.3 Deployment Models and Threat Analysis

NIST defines four deployment models — Device Agent/Gateway, Enclave-Based, Resource Portal, and Device Application Sandboxing — each positioning the PEP at a different architectural location. None adequately addresses the computational asymmetry of heterogeneous environments: constrained IoT devices cannot host full-featured PEP agents, and the specification provides no lightweight alternatives (Sharma et al., 2023; Alawida et al., 2024).

Section 5 of NIST SP 800-207 catalogues five threats uniquely associated with ZTA deployments:

1. **Subversion of the decision process.** A compromised PE silently modifies policies — the most architecturally consequential threat, for which NIST recommends logging and review but specifies no self-monitoring mechanism.
2. **Denial of service against PE/PA.** Unavailability of the decision infrastructure paralyses all access — NIST recommends replication but mandates no consensus protocol.
3. **Stolen credentials and insider exploitation.** Assumes the Trust Algorithm can distinguish legitimate from illegitimate credential use — a capability requiring multi-dimensional behavioural analysis that the framework describes conceptually but does not specify (Chen & Wang, 2025).
4. **Network visibility loss.** Encrypted traffic and heterogeneous encryption standards create inspection gaps.
5. **Vendor data format lock-in.** Proprietary telemetry formats impede interoperability.

### 4.4 The Trust Algorithm Abstraction

The Trust Algorithm is the mathematical engine within the PE. NIST acknowledges its centrality: it processes identity assurance, device posture, behavioural signals, resource sensitivity, and threat intelligence to produce access decisions. Yet the specification explicitly avoids prescribing its mathematical form, offering only a typology distinguishing *criteria-based* (rule evaluation) from *score-based* (numerical computation) approaches, and *singular* (per-request evaluation) from *contextual* (history-informed evaluation) policies (Rose et al., 2020).

This deliberate abstraction creates three specific algorithmic gaps:

- **No evidence fusion specification.** The PE consumes multiple input streams but no method is specified for reconciling conflicting signals — e.g., high identity assurance but degraded device posture.
- **No adaptive weighting.** All inputs are implicitly treated as equally authoritative regardless of their reliability or timeliness.
- **No temporal decay.** The Trust Algorithm is described as evaluating "current state" but no mechanism ensures that the evidentiary weight of past observations diminishes over time.

**Table 1.** Evaluation of NIST SP 800-207 against the six criteria.

| Criterion | Assessment | Justification |
|:---|:---:|:---|
| C1: Uncertainty handling | ✗ | No uncertainty representation specified; binary or weighted-sum decision logic implied |
| C2: Temporal decay | ◐ | Per-session access mandated but no continuous decay function specified |
| C3: Multi-domain fusion | ◐ | Multiple input categories defined but no fusion operator specified |
| C4: Enforcement-computation separation | ✓ | PE/PA/PEP triad explicitly separates decision from enforcement |
| C5: Scalability | ◐ | Distributed deployment permitted but not mandated; no performance benchmarks |
| C6: Explainability | ◐ | Audit logging recommended but decision rationale decomposition not specified |

---

## 5. Software-Defined Perimeters as Enforcement Substrate

### 5.1 SDP Architecture (CSA v2.0)

The CSA SDP architecture comprises three core components:

- **SDP Controller (PDP).** Authenticates Initiating Hosts, evaluates device posture, and issues cryptographic entitlements to Accepting Hosts. The Controller maintains all service ports in a default-closed "dark cloud" state.
- **Initiating Host (IH).** The client seeking access. Must generate a valid SPA packet and present identity credentials and device health telemetry.
- **Accepting Host (AH/Gateway).** The gateway mediating access to protected resources. Opens individualised, encrypted tunnels only upon receiving a valid entitlement from the Controller.

The security architecture comprises five layers:

1. **Single Packet Authorization (SPA).** Cryptographic nonces, timestamps, and HMAC ensure that the initial connection request is authentic, fresh, and unmodified (Cloud Security Alliance, 2022).
2. **Mutual TLS (mTLS).** Bidirectional certificate-based authentication for all component communications.
3. **Device Validation.** OS version, patch level, disk encryption status, and EDR agent presence are evaluated during the Join process.
4. **Dynamic Firewalls.** Per-connection firewall rules are programmatically generated and destroyed with each session.
5. **Application Binding.** Entitlements are bound to specific applications, preventing credential reuse across services.

### 5.2 Operational Workflows

The **Join (Onboarding)** process implements a multi-phase verification workflow:

*Phase 1:* Identity authentication via the enterprise Identity Provider (SAML, OIDC).
*Phase 2:* Device posture evaluation — OS compliance, encryption status, EDR agent presence.
*Phase 3:* Policy correlation — the combination of authenticated identity and observed device state is evaluated against the applicable security policy.
*Phase 4:* Entitlement issuance — a time-bounded, cryptographically signed token authorising the Gateway to open a specific encrypted tunnel.

This multi-phase design evaluates identity and device posture as independent trust dimensions rather than substitutes — a structural implementation of the separation of privilege principle (Saltzer & Schroeder, 1975; Cloud Security Alliance, 2024).

The **Leave (Offboarding)** process implements reactive revocation: any deviation in device posture or identity status triggers immediate entitlement revocation and tunnel termination (Johnson, 2024). The reactive model correctly prioritises security responsiveness — there is no grace period — but its effectiveness depends on continuous SDP Client reporting and uninterrupted Controller communication, assumptions frequently violated in heterogeneous environments.

### 5.3 SDP vs. VPN vs. SDN

**Table 2.** Comparative analysis of SDP, VPN, and SDN architectures.

| Dimension | Traditional VPN | SDN | CSA SDP v2.0 |
|:---|:---|:---|:---|
| **Trust model** | Binary: authenticated = trusted | Binary: controller-authenticated = trusted | Binary: Join = trusted, Leave = untrusted |
| **Network visibility** | Full network after authentication | Controller has full visibility; hosts see managed flows | Zero visibility before SPA; per-resource visibility after Join |
| **Access control** | Network-level (IP/port) | Flow-rule-level (controller-programmed) | Application-level (per-resource entitlement) |
| **Lateral movement** | Unconstrained post-authentication | Constrained by flow rules (static) | Constrained by per-resource tunnels |
| **Post-auth trust** | None (session persists until timeout) | None (flow rules persist until reprogrammed) | Reactive revocation on posture change |
| **Uncertainty handling** | ✗ | ✗ | ✗ |
| **Temporal decay** | ✗ (session timeout only) | ✗ | ✗ (entitlement timeout only) |

### 5.4 SDP-SDN Confluence: The Software-Defined Perimeter Network (SDPN)

The Software-Defined Perimeter Network (SDPN) synthesises SDN's routing intelligence with SDP's identity-centric access control. Within the SDPN control plane, the SDN controller's traffic optimisation capabilities merge with the SDP controller's authentication gatekeeping, creating a singular trust anchor that dictates both *who* is authorised to communicate and the exact *network path* that communication must traverse (Lefebvre et al., 2023). This unified architecture drives Zero Trust principles to the packet routing layer, neutralising TCP/IP broadcast vulnerabilities while preserving SDN's performance scalability. However, the SDPN's trust model inherits the limitations of both parent architectures: binary trust from SDP and static flow-rule persistence from SDN.

### 5.5 Mapping SDP to ZTA Components

The SDP architecture maps directly to the NIST ZTA logical components:

- **SDP Controller → Policy Decision Point (PDP).** The Controller performs the PE function: consuming identity and posture data and producing access determinations.
- **SDP Gateway → Policy Enforcement Point (PEP).** The Gateway enforces the Controller's entitlement by permitting or terminating data paths.
- **SPA Protocol → Authentication Substrate.** SPA provides the initial authentication signal that the PE evaluates.

This mapping is architecturally clean but reveals a critical gap: the SDP Controller performs the PDP *function* but not the PDP *computation*. The Controller evaluates identity and device posture against predefined policies (static rule matching) rather than computing a continuous trust score from fused, temporally weighted, uncertainty-aware evidence. The SDP specification provides the decision *infrastructure* (where and when trust decisions occur) but not the decision *algorithm* (how trust is computed from heterogeneous evidence).

**Table 3.** Evaluation of CSA SDP v2.0 against the six criteria.

| Criterion | Assessment | Justification |
|:---|:---:|:---|
| C1: Uncertainty handling | ✗ | Binary Join/Leave; no intermediate states or uncertainty representation |
| C2: Temporal decay | ✗ | Entitlement timeout exists but no continuous decay function |
| C3: Multi-domain fusion | ◐ | Identity and device posture are independently evaluated but fusion is sequential gating, not formal combination |
| C4: Enforcement-computation separation | ◐ | Controller/Gateway separation exists but computation logic is embedded in Controller |
| C5: Scalability | ◐ | Distributed Gateway clusters recommended; Controller centralisation remains bottleneck |
| C6: Explainability | ◐ | Multi-phase Join produces an audit trail but no decomposed trust rationale |

---

## 6. Identifying the Gap: Absence of Formal Trust Computation

### 6.1 Architectural Gap Table

The preceding analyses of NIST SP 800-207 and CSA SDP v2.0 reveal a systematic pattern of architectural completeness coupled with algorithmic absence. Table 4 maps each architectural component to its missing trust feature and the resulting security consequence.

**Table 4.** Architectural gap mapping.

| Architectural Component | Missing Trust Feature | Consequence |
|:---|:---|:---|
| NIST Policy Engine | No formal evidence fusion method | Cannot reconcile conflicting signals from multiple domains; defaults to ad hoc weighted sums or vendor-proprietary black boxes |
| NIST Trust Algorithm | No temporal decay specification | Implicit trust period persists after authentication; session hijacking exploits stale trust |
| SDP Controller | No adaptive weighting of evidence sources | Static domain importance; unstable or compromised sensors retain full influence |
| SDP Gateway | No uncertainty representation | Binary allow/deny only; no graduated access for ambiguous trust states |
| AI-IDS in SDN | Detection without enforcement coupling | Correct threat detection does not automatically modify access policies; temporal gap between detection and response |
| SDN Controller | Static role assignment | Controller trust established at authentication and never re-evaluated; single point of compromise cascades across all managed flows |

### 6.2 Comparison with Existing Trust Models

To contextualise the gap, we assess seven representative trust computation models from the literature against the six criteria. These models span probabilistic, evidential, and machine learning paradigms.

#### 6.2.1 Probabilistic Models

**Bayesian Trust Inference (PTIT-ELO).** Li et al.'s (2024) Probabilistic Trust Inference Theory combined with Enhanced Lion Optimisation for multi-level trust in WSN/SDN environments uses Bayesian posterior computation for continuous trust updates. *Strengths:* principled uncertainty handling through posterior distributions; continuous score updates. *Limitations:* requires complete prior probability distributions over all hypotheses — in SDN environments where sensor readings may be absent, the model must impute a prior, potentially introducing bias. Limited temporal decay beyond observation windowing. Scalability demonstrated only for homogeneous sensor networks.

**POMDP Trust-Threshold Policy.** Ge and Zhu's (2022) formulation of zero-trust defence as a Partially Observable Markov Decision Process derives explainable trust-threshold policies. *Strengths:* handles partial observability; produces optimal policies with theoretical guarantees; explainable through threshold interpretation. *Limitations:* requires a priori specification of transition matrices, observation models, and reward functions, making it sensitive to model misspecification in open heterogeneous environments where attacker behaviour is unknown. Single-account focus limits applicability to multi-domain evaluation.

**Markov Chain Trust (TrustS).** The four-state Markov model (DOWN/UP/UP-SAFE/UP-UNSAFE) computes node trust from stationary probabilities. *Strengths:* computationally efficient; explicit availability modelling. *Limitations:* stationary distributions are by definition time-invariant — fundamentally incompatible with temporal decay requirements. Requires accurate transition probability estimation.

#### 6.2.2 Evidential Models

**Dempster-Shafer Fusion.** DS theory provides explicit uncertainty representation through $m(\Theta)$, conjunctive fusion via Dempster's Rule with conflict detection through $\kappa$, and the vacuous identity property ensuring that uninformative sources are mathematically invisible (Shafer, 1976; Liu et al., 2023). *Strengths:* C1 fully satisfied; natural multi-domain fusion; no requirement for complete prior distributions. *Limitations:* standalone DS theory lacks temporal decay mechanisms; computational complexity of the combination rule scales quadratically with the cardinality of the power set. Rarely combined with temporal dynamics in the existing literature.

**Tag-Based Trust Evaluation (TBTE).** Zhang et al.'s (2022) framework decomposes entity attributes into fact, prediction, and model tags for rule-based trust decisions. *Strengths:* high explainability; human-interpretable policy rationale. *Limitations:* rule engine operates on static, predefined conditional logic — cannot support graduated "grey-area" access without exponentially expanding the rule set. No temporal decay; tags persist until explicitly updated.

#### 6.2.3 Machine Learning Models

**AI-Driven Policy Classification.** Decision tree classifiers (85% accuracy) predicting allow/deny decisions from static firewall configurations. *Strengths:* automated policy generation; scalable training. *Limitations:* binary classification cannot output graduated trust scores with residual uncertainty; synthetic training data introduces domain shift risk; model outputs are not decomposable into per-domain trust contributions (explainability gap).

**Adversarial-Aware IDS (Ali et al., 2024).** AI-based IDS for heterogeneous SDN with adversarial robustness analysis. *Strengths:* addresses adversarial threat model explicitly; heterogeneous deployment context (COMET architecture). *Limitations:* detection-only — no enforcement coupling; vulnerable to the data poisoning attacks it analyses; no trust computation, only traffic classification.

**Table 5.** Consolidated evaluation of trust computation models.

| Model / Architecture | C1 Uncertainty | C2 Temporal Decay | C3 Multi-Domain Fusion | C4 Enforcement Separation | C5 Scalability | C6 Explainability |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| NIST SP 800-207 | ✗ | ◐ | ◐ | ✓ | ◐ | ◐ |
| CSA SDP v2.0 | ✗ | ✗ | ◐ | ◐ | ◐ | ◐ |
| Bayesian (PTIT-ELO) | ◐ | ◐ | ◐ | ✗ | ◐ | ◐ |
| POMDP Threshold | ✓ | ◐ | ✗ | ✗ | ✗ | ✓ |
| Markov Chain (TrustS) | ✗ | ✗ | ✗ | ✗ | ✓ | ◐ |
| Dempster-Shafer (standalone) | ✓ | ✗ | ✓ | ◐ | ◐ | ◐ |
| Tag-Based (TBTE) | ✗ | ✗ | ◐ | ◐ | ◐ | ✓ |
| AI Policy Classifier | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ |
| Adversarial IDS (Ali et al.) | ✗ | ✗ | ◐ | ✗ | ◐ | ✗ |
| **DCTA Ensemble Model** | **✓** | **✓** | **✓** | **✓** | **◐** | **✓** |

### 6.3 Summary of Gaps

Three structural gaps emerge consistently across the surveyed landscape:

**Gap 1: No unified framework for multi-domain fusion + temporal decay + uncertainty.** No existing model or standard simultaneously satisfies C1, C2, and C3. DS theory handles uncertainty and fusion but lacks temporal dynamics. Bayesian approaches handle uncertainty and temporal updating but require complete priors. POMDP handles uncertainty and temporal evolution but cannot perform multi-domain fusion. These capabilities have developed independently across different research communities but have not been synthesised into a unified trust computation framework.

**Gap 2: Enforcement-computation coupling.** Most trust computation proposals are embedded within specific enforcement architectures — SDP controllers, SDN flow-rule engines, or IDS classification pipelines — rather than producing enforcement-agnostic trust scores that can drive arbitrary PEPs. This coupling impedes portability, interoperability, and the separation of concerns that NIST SP 800-207's PE/PA/PEP triad was designed to achieve.

**Gap 3: Absence of standardised trust metadata and APIs.** No standard exists for the format in which trust scores are computed, exchanged, or consumed by enforcement points. Each vendor and research prototype defines its own trust score representation, making cross-system integration impossible without bespoke adapters. This absence prevents the emergence of a pluggable trust engine ecosystem and locks enterprises into vendor-specific implementations.

---

## 7. Towards a Unified Trust Model: Requirements and Candidate

### 7.1 Synthesised Requirements for Dynamic Trust Evaluation

From the gap analysis, we derive six formal requirements that any trust computation framework must satisfy to operationalise Zero Trust principles in heterogeneous enterprise networks:

**R1: Explicit Uncertainty Representation.** The framework must represent trust as a multi-valued evidential state — minimally comprising belief, disbelief, and uncertainty — rather than a single scalar score. The uncertainty component ($m(\Theta)$, $u$, or equivalent) must be a first-class quantity that influences access decisions, not an implementation artefact. *Rationale:* In heterogeneous environments where sensor failures, network partitions, and telemetry delays are operationally routine, the system must distinguish "I believe this entity is safe" from "I lack sufficient evidence to decide" — a distinction that binary and single-scalar trust models cannot make (Liu et al., 2023).

**R2: Temporal Decay with Configurable Function and Session Freshness.** The framework must provide a configurable decay function — minimally supporting exponential decay with parameterised rate constant and window duration — that continuously depreciates the evidentiary weight of past observations. The dual-horizon requirement specifies both a short-term freshness window (aligned with compliance-mandated inactivity timeouts, e.g., 30 minutes per NIST SP 800-63B) and a long-term inertia window (aligned with maximum session lifetimes, e.g., 48 hours per enterprise policy). *Rationale:* Trust established at authentication time becomes progressively less reliable; temporal decay transforms the one-time authentication gate into a continuously depreciating asset (Robbins et al., 2025).

**R3: Multi-Domain Evidence Fusion with Conflict Detection.** The framework must formally combine evidence from at least four independent telemetry domains — identity, device, network, and application/data — using a fusion operator that preserves inter-domain independence and detects cross-domain conflict. *Rationale:* The separation of privilege principle (Saltzer & Schroeder, 1975) requires that no single domain's favourable assessment can override genuine risk signals from another domain. Weighted-sum aggregation violates this principle by permitting compensatory scoring.

**R4: Variance-Based Adaptive Weighting.** The framework must dynamically modulate each domain's evidential influence based on the statistical stability (variance) of its recent telemetry signals. Domains exhibiting high variance — indicating sensor instability, environmental perturbation, or adversarial manipulation — must receive automatically suppressed weighting regardless of their absolute trust score. *Rationale:* Static domain weights cannot accommodate the operational reality that different domains exhibit different reliability profiles at different times. Variance-based weighting provides native adversarial resilience: spoofed high-trust signals introduce variance, triggering automatic weight suppression (Liu et al., 2023).

**R5: Enforcement-Agnostic Trust Scores.** The framework must produce trust scores that can drive any Policy Enforcement Point — SDP Gateway, SDN flow-rule engine, Envoy proxy, OPA policy agent, SASE Point of Presence — without modification to the computation logic. This requires a defined interface between the trust computation engine (PDP) and the enforcement substrate, with standardised trust score format and exchange protocol. *Rationale:* Heterogeneous enterprises deploy multiple enforcement technologies; the trust computation must be enforcement-technology-independent to achieve the NIST PE/PA/PEP separation at the implementation level.

**R6: Explainability.** The framework must produce auditable, decomposable decision rationales that identify which domains, which specific evidence signals, and which thresholds contributed to each access decision. *Rationale:* Regulatory compliance (GDPR, HIPAA, SOX) and organisational governance require that access decisions are justifiable and reviewable. The Pignistic transformation from DS mass functions to actionable probabilities provides one such transparent mapping (Smets, 1990).

### 7.2 Candidate Architecture: The DCTA Ensemble Trust Model (ETM)

The Dynamic Contextual Trust Architecture (DCTA) Ensemble Trust Model (ETM) integrates four mechanisms to satisfy requirements R1–R6:

**Dempster-Shafer Evidential Fusion.** Each of four telemetry domains (Identity, Device, Network, Application/Data) produces a basic probability assignment over the binary frame $\Theta = \{\text{Safe}, \text{Unsafe}\}$. Sixteen Bernoulli facets — binary compliance checks such as MFA completion, patch currency, TLS version, and API authentication — are aggregated into Binomial domain proportions $S_k$. The mass function for each domain is constructed via evidence discounting:

$$
m_k(\{\text{Safe}\}) = S_k \cdot W_k, \quad m_k(\{\text{Unsafe}\}) = (1 - S_k) \cdot W_k, \quad m_k(\Theta) = 1 - W_k
$$

where $W_k$ is the domain's dynamic weight. Inter-domain fusion uses Dempster's Rule, detecting cross-domain conflict through $\kappa$ and producing a fused belief state with explicit uncertainty.

**Variance-Based Dynamic Weighting.** Each domain's weight is computed from its rolling variance:

$$
W_{\text{raw},k} = \frac{1}{1 + \alpha \cdot \sigma_k^2}
$$

where $\alpha > 0$ is the variance penalty amplifier (default $\alpha = 10$ for standard enterprise environments, empirically validated through sensitivity analysis in the companion studies). Weights are normalised to sum to unity. This mechanism achieves R4: stable domains receive near-full weight while erratic domains are suppressed toward vacuity.

**Exponential Temporal Decay.** A dual-horizon decay architecture continuously depreciates trust:

$$
T = W_{\text{short}} \cdot T_{\text{instant}} + (1 - W_{\text{short}}) \cdot T_{\text{history}} \cdot D_{\text{long}}
$$

where $W_{\text{short}} = e^{-\lambda_s \cdot t / T_s}$ governs the 30-minute freshness window and $D_{\text{long}} = e^{-\lambda_l \cdot t / T_l}$ governs the 48-hour inertia window. This achieves R2: the initial authentication signal depreciates continuously, forcing re-verification.

**Graduated Access via Pignistic Transformation.** The fused mass function is converted to an actionable probability $BetP(\text{Safe}) = m(\{\text{Safe}\}) + m(\Theta)/2$, mapped to tiered access: Full Access ($BetP > 0.75$), Limited Access ($0.45 \leq BetP \leq 0.75$), No Access ($BetP < 0.45$). This achieves R6 through transparent, decomposable decision rationale.

**Table 6.** DCTA Ensemble Model satisfaction of requirements R1–R6.

| Requirement | DCTA Mechanism | Satisfaction |
|:---|:---|:---:|
| R1: Explicit uncertainty | $m(\Theta)$ term in DS mass function | ✓ |
| R2: Temporal decay | Dual-horizon exponential decay ($\lambda_s$, $\lambda_l$) | ✓ |
| R3: Multi-domain fusion | Dempster's Rule across 4 independent domains with $\kappa$ conflict detection | ✓ |
| R4: Adaptive weighting | Variance-based $W_k = (1 + \alpha\sigma_k^2)^{-1}$ | ✓ |
| R5: Enforcement-agnostic | PDP/PEP separation via OPA/Envoy; $BetP$ score drives any PEP | ✓ |
| R6: Explainability | Pignistic transformation; per-domain mass decomposition; threshold audit trail | ✓ |

> **Note.** The DCTA Ensemble Model is presented as one candidate architecture, not as the sole solution. Its purpose here is to demonstrate that a framework satisfying all six requirements is architecturally feasible and mathematically tractable.

### 7.3 Comparison with Other Proposals

To contextualise the DCTA's position, we compare it with three alternative proposals from the literature that address subsets of the requirements.

**POMDP Trust-Threshold Policies (Ge & Zhu, 2022).** The POMDP formulation handles partial observability (R1) and produces optimal, explainable threshold policies (R6). However, it requires a priori specification of transition matrices and observation models — a severe constraint in open heterogeneous environments where attacker behaviour is unknown. Furthermore, it operates on a single-account context (violating R3) and provides no enforcement-agnostic interface (violating R5). Temporal dynamics are modelled through Markovian state transitions rather than explicit decay functions (partially satisfying R2). The POMDP approach is theoretically elegant for controlled environments but operationally constrained in heterogeneous deployments.

**Blockchain-Based Continuous Authentication (Meng et al., 2022).** Decentralised authentication via PBFT consensus eliminates the single point of failure inherent in centralised Identity Providers. The blockchain provides a distributed trust substrate (partially satisfying R5) and continuous device-to-device verification (partially satisfying R2). However, PBFT consensus requires a minimum quorum that may be unachievable in partitioned network segments. The approach addresses authentication mechanics rather than trust computation — it provides *how* re-authentication is performed but not *whether* it is needed. It does not handle uncertainty (violating R1), does not perform multi-domain fusion (violating R3), and does not provide adaptive weighting (violating R4).

**Tag-Based Trust Evaluation (Zhang et al., 2022).** The TBTE framework's decomposition of entity attributes into fact, prediction, and model tags provides outstanding explainability (R6) and could serve as a presentation layer for more sophisticated trust engines. However, the rule-based logic cannot support graduated access without combinatorial rule explosion. Tags persist until explicitly updated (violating R2), the framework lacks uncertainty representation (violating R1), and the static rule engine cannot adapt to variance in telemetry reliability (violating R4).

**Table 7.** Comparative requirement satisfaction across candidate approaches.

| Requirement | DCTA | POMDP | Blockchain Auth | TBTE |
|:---|:---:|:---:|:---:|:---:|
| R1: Uncertainty | ✓ | ✓ | ✗ | ✗ |
| R2: Temporal decay | ✓ | ◐ | ◐ | ✗ |
| R3: Multi-domain fusion | ✓ | ✗ | ✗ | ◐ |
| R4: Adaptive weighting | ✓ | ✗ | ✗ | ✗ |
| R5: Enforcement-agnostic | ✓ | ✗ | ◐ | ◐ |
| R6: Explainability | ✓ | ✓ | ◐ | ✓ |

---

## 8. Open Challenges and Future Research Directions

The gap analysis and requirements synthesis identify six open research challenges that extend beyond the scope of current architectural standards and algorithmic proposals.

### 8.1 Hardware-Rooted Attestation

The trustworthiness of the telemetry consumed by any trust computation engine ultimately depends on the integrity of the reporting sensors. Variance-based weighting can detect *behavioural inconsistency* in sensor reporting, but cannot detect a compromised Trusted Platform Module (TPM) that consistently reports falsified-but-stable posture data. Integrating hardware-rooted attestation via TCG Chains of Trust (CoT) into the trust computation pipeline — providing cryptographic proof of sensor integrity at the hardware level — would strengthen the Device domain's input to the fusion engine and reduce the epistemic uncertainty associated with software-only attestation. The challenge lies in heterogeneous device populations: BYOD devices, consumer IoT sensors, and legacy embedded systems rarely include TPM 2.0 modules, requiring graceful degradation when hardware attestation is unavailable.

### 8.2 Federated Learning for Parameter Tuning

The DCTA's decay rate constants ($\lambda_s$, $\lambda_l$) and variance sensitivity parameter ($\alpha$) are currently calibrated against compliance standards and empirical heuristics. Federated learning offers the prospect of collaborative optimisation across multiple organisations — each contributing gradient updates from their operational telemetry without sharing raw data — to converge on parameter values that minimise false positive rates and breach containment times across diverse deployment contexts. The challenge is ensuring that adversarial participants cannot poison the federated learning process to bias parameter convergence toward values that favour their attack strategies.

### 8.3 Privacy-Preserving Telemetry

Zero Trust's mandate for continuous behavioural monitoring creates an inherent tension with privacy requirements (GDPR, CCPA). Zero-knowledge proofs (ZKPs) and fully homomorphic encryption (FHE) offer theoretical mechanisms for performing trust computation on encrypted telemetry — proving that a device meets posture requirements without revealing the specific posture data. The practical challenge is computational overhead: FHE operations remain orders of magnitude slower than cleartext computation, and ZKP construction for complex trust functions is an active area of cryptographic research.

### 8.4 Post-Quantum Cryptography

The initial authentication signals consumed by trust computation engines — SPA packets, mTLS certificates, FIDO2 assertions — rely on classical cryptographic primitives (RSA, ECDSA) that are vulnerable to quantum computing advances. Transitioning to post-quantum cryptographic (PQC) standards (ML-KEM, ML-DSA, SLH-DSA) for the authentication substrate ensures that the "freshness" component of the trust score remains cryptographically sound against quantum-capable adversaries. The challenge lies in the increased key and signature sizes of PQC algorithms, which exacerbate the computational overhead for resource-constrained IoT devices already struggling with SPA generation (Sharma et al., 2023).

### 8.5 AI-Driven Adaptive Policies

Reinforcement learning (RL) offers the prospect of dynamic threshold adjustment: an RL agent that observes the consequences of access decisions (successful legitimate access, detected breaches, false denials) and adjusts trust thresholds to optimise a security-usability trade-off function. The challenge is twofold: the reward signal for security decisions is fundamentally delayed (breaches may not be detected for months) and adversarially influenced (an attacker may engineer benign-appearing sessions to train the agent toward permissive thresholds).

### 8.6 Self-Healing Network Topologies

Cognitive SDP controllers that restructure network routing upon trust degradation represent an advanced integration of trust computation with network management. When a trust computation engine detects degradation in a network segment — reflected in elevated variance and suppressed domain weights — a cognitive controller could proactively reroute traffic through trusted segments, restructure microsegmentation boundaries, and pre-position enforcement capacity. This transforms trust computation from a reactive access control mechanism into a proactive network topology optimiser, but requires tight integration between the trust engine and the SDN control plane.

---

## 9. Recommendations for Standardisation

Based on the survey findings, we offer four concrete recommendations for standards bodies and industry working groups.

### 9.1 NIST SP 800-207 Revision

A revision of NIST SP 800-207 should extend the Trust Algorithm section to include normative guidance on three dimensions currently left unspecified:

- **Evidence Fusion Method.** Specify at minimum one reference fusion method (e.g., Dempster-Shafer combination as an option alongside weighted aggregation) with defined semantics for conflict handling and uncertainty propagation. The specification should mandate that the chosen method must satisfy the commutativity and associativity properties required for order-independent, incremental fusion.
- **Temporal Decay Parameters.** Specify that the Trust Algorithm must implement a configurable temporal decay function with defined parameters: decay function type (linear, exponential, or sliding window), decay rate constant, evaluation window size, and minimum refresh interval. The specification should reference NIST SP 800-63B's inactivity timeout requirements as a calibration anchor for short-term decay windows.
- **Uncertainty Representation.** Specify that access decisions must incorporate explicit uncertainty quantification — not merely a scalar trust score but a confidence interval or equivalent evidential state. The specification should mandate that uncertainty exceeding a configured threshold triggers constrained access rather than binary grant or denial.

### 9.2 CSA SDP v3.0 Extension

The next major revision of the CSA SDP specification should extend the Controller API to support:

- **Pluggable Trust Engines.** Define a standard interface through which external trust computation engines can be integrated with the SDP Controller, enabling the Controller to consume continuous trust scores from arbitrary engines without modification to the SDP protocol stack.
- **Trust Scores as First-Class Objects.** Extend the SDP entitlement format to include a continuous trust score with domain-level decomposition (identity, device, network, application), enabling Gateways to implement graduated enforcement based on trust magnitude rather than binary entitlement presence.
- **Graduated Entitlements.** Specify a tiered entitlement format — full, constrained, and monitoring modes — that maps to trust score ranges, replacing the current binary Join/Leave model with a graduated access spectrum.

### 9.3 IETF / OpenAPI Trust Metadata Schema

A new IETF informational RFC or OpenAPI specification should define a standard trust metadata schema (JSON) for telemetry exchange between PDPs and PEPs. The schema should include:

```json
{
  "entity_id": "string",
  "timestamp": "ISO-8601",
  "composite_trust_score": 0.0-1.0,
  "uncertainty": 0.0-1.0,
  "domain_scores": {
    "identity": { "score": 0.0-1.0, "weight": 0.0-1.0, "variance": 0.0-1.0 },
    "device":   { "score": 0.0-1.0, "weight": 0.0-1.0, "variance": 0.0-1.0 },
    "network":  { "score": 0.0-1.0, "weight": 0.0-1.0, "variance": 0.0-1.0 },
    "application": { "score": 0.0-1.0, "weight": 0.0-1.0, "variance": 0.0-1.0 }
  },
  "decay_parameters": {
    "function": "exponential|linear|sliding_window",
    "rate_constant": "float",
    "window_seconds": "integer"
  },
  "access_decision": "full|limited|deny",
  "decision_rationale": ["string"]
}
```

This schema enables interoperability between trust engines and enforcement points from different vendors, eliminating the proprietary data format lock-in that NIST SP 800-207 Section 5 identifies as a structural threat.

### 9.4 Community Benchmarking

A public testbed and reference dataset for comparing trust algorithms should be established, measuring:

- **Latency**: per-decision evaluation time under increasing session concurrency.
- **False positive rate**: legitimate access denials under normal operational conditions.
- **False negative rate**: unauthorised access grants under simulated attack scenarios.
- **Breach containment time**: time from initial compromise to trust-score-triggered access revocation.
- **Adversarial resilience**: trust score stability under data poisoning, sensor spoofing, and coordinated multi-domain attacks.

The benchmarking initiative should publish reference adversarial scenarios — analogous to the NIST Cybersecurity Framework's threat catalogues — against which trust algorithm vendors can validate their implementations.

---

## 10. Conclusion

This survey has conducted a systematic evaluation of trust computation across the two dominant frameworks for modern network security — NIST SP 800-207 Zero Trust Architecture and CSA Software-Defined Perimeters — using a structured six-criteria evaluation framework encompassing uncertainty handling, temporal decay, multi-domain fusion, enforcement-computation separation, scalability, and explainability.

The findings reveal a consistent and architecturally consequential pattern: **current ZTA and SDP frameworks provide mature architectural containers for trust-based access control but lack the algorithmic content to populate them.** NIST SP 800-207 mandates continuous trust evaluation but leaves the Trust Algorithm mathematically unspecified. CSA SDP achieves rigorous cryptographic session establishment but provides no post-authentication trust management. Neither framework addresses uncertainty representation, temporal decay, or multi-domain evidence fusion at the normative specification level.

The comparative assessment of seven representative trust computation models — spanning Bayesian inference, Markov chains, POMDP, Dempster-Shafer theory, tag-based evaluation, AI-driven classification, and adversarial-aware IDS — reveals that while individual capabilities exist across the research landscape, **no existing model simultaneously satisfies all six evaluation criteria.** Uncertainty handling (Dempster-Shafer, POMDP), temporal decay (exponential decay models), and multi-domain fusion (weighted combination) have developed independently across different research communities but have not been synthesised into a unified framework.

From this gap analysis, six formal requirements for dynamic trust evaluation have been synthesised (R1–R6), spanning explicit uncertainty representation, configurable temporal decay, multi-domain fusion with conflict detection, variance-based adaptive weighting, enforcement-agnostic trust scores, and decision explainability. The DCTA Ensemble Model has been presented as one candidate architecture satisfying all six requirements, demonstrating architectural feasibility without claiming exclusivity.

The survey concludes with actionable recommendations: NIST SP 800-207 should be revised to include normative Trust Algorithm guidance; CSA SDP v3.0 should support pluggable trust engines and graduated entitlements; an IETF standard should define trust metadata exchange formats; and a community benchmarking initiative should enable empirical comparison of trust algorithms.

The transition from architectural containers to algorithmic content — from *where* trust decisions are made to *how* they are computed — is the critical next step in the maturation of Zero Trust. This survey provides the evaluation framework, gap analysis, and synthesised requirements to guide that transition.

---

## References

Ahmed, T., Li, Y., & Zhang, W. (2024). Dynamic trust management for zero trust architectures in heterogeneous IoT environments. *IEEE Transactions on Dependable and Secure Computing, 21*(3), 1542–1557. https://doi.org/10.1109/TDSC.2023.3312456

Al-Mutairi, A., & Hassan, R. (2024). Integrating SDN and Zero Trust Architecture for robust cloud environments: A review. *Computers and Security, 136*, 103550.

Al-Sanjary, O. I., Ahmed, A. A., & Jaharadak, A. A. (2023). Access control models in cloud computing: A comprehensive survey. *Journal of King Saud University – Computer and Information Sciences, 35*(6), 101567. https://doi.org/10.1016/j.jksuci.2023.101567

Alawida, M., Oqaily, A., Halboob, W., & Abutair, H. (2024). A comprehensive survey on zero trust architecture (ZTA): Concepts, components, and implementation. *IEEE Access, 12*, 4526–4550.

Ali, M., Naeem, F., Tariq, M., & Kaddoum, G. (2024). Adversarial attacks on AI-based intrusion detection system for heterogeneous wireless communications networks. *IEEE Transactions on Wireless Communications, 23*(5), 4367–4381. https://doi.org/10.1109/TWC.2023.3321456

Alsubhi, K., Al-Begain, K., & Durad, M. H. (2024). Continuous trust evaluation in zero trust architectures: A dynamic scoring framework. *Computers & Security, 138*, 103672. https://doi.org/10.1016/j.cose.2024.103672

Buck, C., Olenberger, C., Schweizer, A., Völter, F., & Eymann, T. (2022). Never trust, always verify: A multivocal literature review on current knowledge and research gaps of zero-trust. *Computers & Security, 110*, 102436. https://doi.org/10.1016/j.cose.2021.102436

Chen, X., & Wang, L. (2025). Explainable AI for dynamic access control in zero trust architectures. *ACM Computing Surveys, 57*(2), 1–36. https://doi.org/10.1145/3672891

Cloud Security Alliance. (2022). *Software-Defined Perimeter (SDP) Specification v2.0*. Cloud Security Alliance. https://cloudsecurityalliance.org/artifacts/sdp-specification-v2-0

Cloud Security Alliance. (2024). *Software-Defined Perimeter (SDP) Architecture Guide v2*. Cloud Security Alliance. https://cloudsecurityalliance.org/artifacts/sdp-architecture-guide-v2

Cloud Security Alliance. (2025). *Zero trust architecture for cloud-native environments: Best practices and reference architecture* (Version 2.0). https://cloudsecurityalliance.org/artifacts/zero-trust-architecture

Ge, M., & Zhu, X. (2022). Trust threshold policy for explainable and adaptive zero-trust defense in enterprise networks. *IEEE Transactions on Information Forensics and Security, 17*, 3443–3458. https://doi.org/10.1109/TIFS.2022.3205458

Habib, M. A., Mehmood, A., & Ahmad, M. (2022). Role-based access control challenges in IoT environments: A systematic literature review. *ACM Computing Surveys, 55*(4), 1–38. https://doi.org/10.1145/3544979

IBM Security. (2024). *Cost of a data breach report 2024*. IBM Corporation. https://www.ibm.com/reports/data-breach

Johnson, M. (2024). Zero Trust evolution: Migrating from legacy VPNs to dynamic SDP entitlements. *Information Security Journal, 33*(4), 405–420.

Jøsang, A. (2016). *Subjective logic: A formalism for reasoning under uncertainty*. Springer. https://doi.org/10.1007/978-3-319-42337-1

Kreutz, D., Ramos, F. M. V., Veríssimo, P. E., Rothenberg, C. E., Azodolmolky, S., & Uhlig, S. (2015). Software-defined networking: A comprehensive survey. *Proceedings of the IEEE, 103*(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Lefebvre, M., Engels, D. W., & Nair, S. (2023). On SDPN: Integrating the Software-Defined Perimeter (SDP) and the Software-Defined Network (SDN) paradigms. *IEEE Communications Magazine, 61*(2), 55–61.

Li, X., Wang, Y., & Chen, Z. (2024). Probabilistic trust inference theory to optimizing multi-level trust in software defined networks. *IEEE Transactions on Network and Service Management, 21*(2), 1834–1849.

Liu, W., Chen, L., & Wang, Y. (2023). Evidential reasoning for dynamic trust evaluation in heterogeneous networks. *Information Fusion, 96*, 101–115. https://doi.org/10.1016/j.inffus.2023.03.014

Meng, W., Li, W., & Zhu, L. (2022). A continuous authentication protocol without trust authority for zero trust architecture. *IEEE Transactions on Dependable and Secure Computing, 19*(6), 4005–4018. https://doi.org/10.1109/TDSC.2021.3120277

Moubayed, A., Refaey, A., & Shami, A. (2022). Software-Defined Perimeter (SDP): State of the art. *IEEE Access, 10*, 96156–96181. https://doi.org/10.1109/ACCESS.2022.3204623

Mui, L., Mohtashemi, M., & Halberstadt, A. (2002). A computational model of trust and reputation. *Proceedings of the 35th Annual Hawaii International Conference on System Sciences*, 2431–2439. https://doi.org/10.1109/HICSS.2002.994181

Oqaily, A., Alawida, M., & Halboob, W. (2024). Operational metrics and latency analysis of Zero Trust Architecture deployments. *IEEE Security & Privacy, 22*(4), 18–29.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71

Robbins, J. S., McCormick, D., & Patel, R. (2025). Temporal dynamics in continuous adaptive risk and trust assessment (CARTA). *IEEE Security & Privacy, 23*(2), 44–53. https://doi.org/10.1109/MSEC.2025.3401234

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939

Shafer, G. (1976). *A mathematical theory of evidence*. Princeton University Press.

Sharma, P., Kumar, R., & Singh, A. (2023). Lightweight access control for resource-constrained IoT devices in zero trust environments. *Journal of Systems Architecture, 140*, 102912. https://doi.org/10.1016/j.sysarc.2023.102912

Shin, D., Kim, J., & Lee, S. (2025). A generalized framework for optimizing context-aware trust algorithms in Zero Trust Architecture. *Computers & Security, 148*, 104112.

Smets, P. (1990). The combination of evidence in the transferable belief model. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 12*(5), 447–458. https://doi.org/10.1109/34.56205

Smith, J. (2024). Overcoming Controller bottlenecks in Gateway-to-Gateway Software-Defined Perimeters. *Journal of Network and Systems Management, 32*(3), 45–62.

Stafford, B. (2023). The end of the perimeter: Security architecture for cloud-first enterprises. *Journal of Information Security and Applications, 73*, 103442. https://doi.org/10.1016/j.jisa.2023.103442

Wang, T., Bhuiyan, M. Z. A., Wang, G., Rahman, M. A., Wu, J., & Cao, J. (2022). Big data reduction for a smart city's critical infrastructure: An approach based on deep learning and trust evaluation. *IEEE Transactions on Industrial Informatics, 18*(3), 1897–1907. https://doi.org/10.1109/TII.2021.3099868

Xu, J. (2024). Trust algorithm optimization in Zero Trust architectures utilizing federated learning and SDN. *Journal of Information Security and Applications, 80*, 103681.

Zanasi, C., Bartoli, A., & Salsano, S. (2023). Certificate management automation for zero trust architectures: Challenges and solutions. *IEEE Communications Magazine, 61*(8), 56–62. https://doi.org/10.1109/MCOM.001.2300012

Zhang, Y., Liu, H., & Wang, Q. (2022). Tag-based trust evaluation in zero trust architecture. *IEEE Access, 10*, 68724–68738. https://doi.org/10.1109/ACCESS.2022.3186751
