# Research Gap: From Literature Critique to the Ensemble Trust Model

The works reviewed in the preceding sections collectively illuminate a convergent set of structural deficiencies that no single existing contribution addresses holistically. This section distils the critiqued literature into four interlocking gap dimensions, culminating in the precise research problem that this thesis resolves.

## 1. Evidential Uncertainty and Multi-Domain Fusion

Among the probabilistic approaches surveyed — Bayesian inference (PTIT-ELO), Hidden Markov Models (HMM-BMS), POMDP belief states, and Markov chain stationary distributions (TrustS) — each imposes a critical assumption: the availability of complete prior distributions over the trust domain. In heterogeneous enterprise networks, where sensor availability is intermittent and attacker models are unknown, this assumption is operationally untenable. Dempster-Shafer theory resolves this constraint by providing explicit uncertainty representation through unprojected belief mass (*m*(Θ)) — the capacity to mathematically express "I do not have enough evidence to decide" — without requiring complete priors.

Yet the surveyed DS applications remain limited to single-domain evaluations. The context-based attack literature demonstrates that single-domain trust is inherently vulnerable to context spoofing: an attacker who compromises one domain can present fabricated metrics that a single-domain model cannot detect. This thesis addresses both limitations simultaneously through its four-domain fusion architecture, where Dempster's combination rule detects inter-domain conflict (κ) when spoofed domains disagree with honest ones — transforming the network's heterogeneity from a liability into a defensive asset. As Randhawa et al. (2017) note, robust trust calculation requires both accurate multi-source aggregation and reliable contextual transfer of trust values; this architecture addresses both requirements structurally.

## 2. Temporal Fragility of Continuous Trust

A striking deficiency across the surveyed literature is the near-universal absence of mathematically rigorous temporal decay. The HetNet trust survey, POMDP framework, tag-based evaluation, and Markov models all compute trust at discrete time points without enforcing session ephemerality.

This gap has profound operational consequences. The Cloud Security Alliance's SDP v2.0 provides exemplary session initiation protocols through Single Packet Authorization and multi-stage posture checks, but treats trust as a binary state achieved at the perimeter boundary — it lacks an algorithmic mechanism for continuously degrading trust over a sustained session. NIST SP 800-207 acknowledges the need for continuous verification, mandating that the Policy Engine ingest observability data, yet explicitly leaves the Trust Algorithm's internal mechanics abstracted: it specifies input variables (Identity Assurance, Device Posture, Behavioral Signals) but offers no standardisation on how to weight, synthesise, or decay them over time. As Shin et al. (2025) and Xu (2024) observe, this forces engineers to rely on rigid linear timeouts or aggressive exponential kill-switches — both conflicting with enterprise productivity.

This thesis fills the temporal gap through the Freshness-Inertia continuum, modelling trust decay as configurable linear and exponential functions (governed by λ) that bridge NIST's architectural mandate for continuous verification with the operational reality of session continuity.

## 3. Enforcement-Computation Separation

The SDP, SASE, micro-segmentation, and ProGun works provide enforcement mechanisms — the "last mile" translating trust scores into access decisions — but none includes a native, mathematically principled trust computation engine. They assume trust scores arrive from an external source without specifying how those scores should be generated, weighted, or temporally managed. Conversely, relying strictly on static fail-closed enforcement during minor telemetry fluctuations (e.g., a momentary Wi-Fi drop) creates user friction that undermines security adoption.

This confirms the thesis's architectural decision to separate trust computation (Policy Decision Point) from trust enforcement (Policy Enforcement Point). The Ensemble Trust engine remains enforcement-agnostic — capable of driving SDP gateways, SDN flow rules, or Envoy proxy sidecars — while the enforcement layer remains algorithm-agnostic. This decoupling enables graduated response (full, limited, or denied access based on continuous trust scores) rather than binary fail-open/fail-closed behaviour.

## Convergent Research Gap

The literature demonstrates that while the *architecture* of Zero Trust (SDP, SDPN) and the *standards* of Zero Trust (NIST SP 800-207) are highly mature, the *algorithmic calculus* required to manage dynamic trust across time, domains, and enforcement substrates remains nascent. No existing work simultaneously addresses:

1. **Evidential uncertainty quantification** — representing incomplete knowledge as a first-class mathematical object rather than forcing uniform priors;
2. **Temporal trust depreciation** — enforcing session ephemerality through continuous decay rather than binary timeout thresholds;
3. **Multi-domain conflict detection** — fusing trust from heterogeneous domains while detecting inter-domain inconsistencies indicative of compromise;
4. **Enforcement-agnostic computation** — producing trust scores that drive any PEP technology without algorithm-enforcement coupling.

This convergent gap validates the core contribution of this research: a hybridised Ensemble Trust Model that mathematically augments SDP and NIST's cryptographic boundaries with spatial belief fusion, continuous temporal inertia, variance-based weighting, and multi-domain conflict detection — bridging the gap between absolute security and operational continuity.

## Identified Extensions

The literature suggests three extensions constituting natural future research directions: (1) **hardware-rooted attestation** via TCG/TPM to validate telemetry authenticity at the silicon level; (2) **AI-driven parameter optimisation** for α (variance sensitivity) and λ (decay rate) calibration via reinforcement learning; and (3) **collusion detection mechanisms** to counter coordinated multi-domain compromise. These align with future work directions in Chapter 10.
