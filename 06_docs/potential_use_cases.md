# Potential Use Cases for DCTA Research

## Dynamic Context-Aware Trust Architecture — Applications, Justifications & Benefits

---

## Overview

This document maps the research contributions of the DCTA thesis to concrete, real-world use cases across five sectors. Each use case identifies the specific problem, how the thesis contributions address it, which components are utilised, and the quantifiable benefits.

---

## Sector 1: Enterprise & Corporate Networks

### Use Case 1: Hybrid Workforce Zero Trust Access

**Problem:** Post-pandemic enterprises operate with employees connecting from corporate offices, home networks, co-working spaces, coffee shops, and mobile hotspots — simultaneously. Current VPN-based access models grant uniform, durable access regardless of the connecting environment's risk profile.

**How DCTA Addresses This:**
- The **four-domain fusion** (Identity, Device, Network, Application) continuously evaluates trust across all connection contexts
- **Variance-based dynamic weighting** automatically suppresses the influence of noisy public Wi-Fi without triggering false-positive lockouts
- **Contextual Gray-Area Routing** provides proportional access:
  - Corporate office → Full Access
  - Home VPN → Full Access (strong device health compensates for moderate network)
  - Coffee shop Wi-Fi → Limited Access (email, calendar — but not production databases)

**Key Components Used:** Dynamic weighting, DS belief fusion, Gray-Area Routing

**Quantifiable Benefits:**
| Metric | Legacy VPN | DCTA Ensemble |
|:---|:---:|:---:|
| False-positive lockouts | ~28% | ~7.5% |
| Access granularity | Binary (Allow/Deny) | 3-tier proportional |
| Session hijacking detection | None | Active (Inertia mismatch) |
| User productivity loss from lockouts | High | Reduced by ~73% |

**Standards Alignment:** NIST SP 800-207, CISA Zero Trust Maturity Model v2.1

---

### Use Case 2: Insider Threat Detection & Mitigation

**Problem:** Insider threats are the most financially damaging cybersecurity risk. Malicious insiders possess valid credentials and operate from compliant devices, easily bypassing static access controls. "Low and slow" exfiltration campaigns can persist for months under established identities.

**How DCTA Addresses This:**
- **Behavioural variance tracking** detects deviations from established operational patterns (e.g., sudden spike in database queries, access to unusual data classifications)
- **Temporal decay** ensures that even perfectly stable sessions degrade over time, forcing periodic re-verification that exposes dormant threats
- The **Ensemble Inertia component** collapses when an adversary deviates from the victim's long-term behaviour — even if they hold valid credentials
- **Inter-domain conflict detection** (K coefficient) flags when identity signals are strong but behavioural signals are anomalous

**Key Components Used:** Ensemble Trust Model (Freshness + Inertia), variance-based weighting, conflict coefficient K

**Quantifiable Benefits:**
- Detection of behavioural deviation within **4-8 evaluation cycles** (4-8 minutes)
- Forced session re-authentication every 30 minutes (short-term TTL)
- Conflict coefficient K = 0.42 provides actionable alerts (vs. 0.18 in static models)
- Eliminates the "durational passport" that enables multi-month insider campaigns

**Justification:** IBM's 2024 Cost of a Data Breach Report identifies insider threats as the costliest attack vector. The Ensemble Model's temporal decay function directly addresses the operational runway insiders exploit.

---

### Use Case 3: BYOD Security Management

**Problem:** BYOD (Bring Your Own Device) policies reduce hardware costs but introduce unmanaged devices with unknown security postures. Traditional approaches either block BYOD entirely (sacrificing productivity) or grant full access (creating security gaps).

**How DCTA Addresses This:**
- The **Device domain** captures MDM status, patch levels, EDR presence, and OS integrity
- **Dynamic weighting** automatically increases the influence of Network and Application domains when Device trust is low — compensating for unknown device health with strong context from other domains
- **Gray-Area Routing** provides a graduated response:
  - Unmanaged device + secure network + valid identity → **Limited Access** (non-sensitive resources)
  - Unmanaged device + public network → **No Access**
  - This replaces the binary BYOD allow/deny with mathematically proportional access

**Key Components Used:** Multi-domain fusion, Gray-Area Routing, dynamic weighting

**Quantifiable Benefits:**
- Enables BYOD without full access exposure — **proportional access** based on combined context
- Eliminates the "all-or-nothing" BYOD policy dilemma
- Device domain weight automatically adjusts based on device compliance volatility

---

## Sector 2: Government & Defence

### Use Case 4: DoD / Federal Zero Trust Mandate Compliance

**Problem:** The U.S. Department of Defense (DoD) and federal agencies are mandated to achieve Zero Trust maturity by 2027. NIST SP 800-207 and CISA's Zero Trust Maturity Model v2.1 require continuous verification, but provide no standardised trust computation algorithm. Agencies struggle to implement the *how* of continuous trust assessment.

**How DCTA Addresses This:**
- The Ensemble Trust Model provides the **missing algorithmic calculus** that NIST SP 800-207 mandates but does not prescribe
- **Enforcement-agnostic design** allows integration with any existing federal infrastructure (FedRAMP, ICAM, CDM)
- **Auditable trust computation** — every access decision produces a traceable path through the DS fusion pipeline, meeting accountability requirements
- **Configurable temporal parameters** align with NIST AAL levels:
  - AAL2: 30-minute short-term window
  - AAL3: 12-hour maximum inertia window for classified enclaves

**Key Components Used:** Complete Ensemble framework, configurable decay parameters, enforcement-agnostic PDP

**Quantifiable Benefits:**
| Capability | DoD ZT Requirement | DCTA Provision |
|:---|:---|:---|
| Continuous verification | Mandatory by 2027 | ✅ Every evaluation cycle |
| Multi-domain assessment | Identity + Device + Network + Data | ✅ Four-domain fusion |
| Automated response | Dynamic policy enforcement | ✅ Trust → OPA → SDN flow rules |
| Auditability | Complete decision trail | ✅ DS mass functions logged per step |
| Temporal enforcement | Session ephemerality | ✅ Dual-horizon exponential decay |

**Justification:** The federal mandate creates a guaranteed demand for transparent, standardised trust algorithms. The DCTA framework provides a reference implementation that agencies can adapt without vendor lock-in.

---

### Use Case 5: Classified Network Access Control

**Problem:** Classified environments (TS/SCI, NATO SECRET) require the most aggressive access controls. Current approaches rely on physical isolation (air gaps) and rigid RBAC, which cannot adapt to dynamic risk during active sessions.

**How DCTA Addresses This:**
- **Exponential temporal decay** with aggressive parameters (λ ≥ 5.0, T_short = 15 min) creates "continuous algorithmic suspicion" — the mathematical kill-switch
- Sessions in classified enclaves degrade within **15 minutes**, forcing constant re-verification
- **Long-term inertia capped at 12 hours** (NIST AAL3) prevents overnight persistence
- **Multi-domain fusion** ensures that a valid identity cannot override a compromised device or anomalous network signature

**Key Components Used:** Aggressive exponential decay, multi-domain DS fusion, conflict detection

**Quantifiable Benefits:**
- Eliminates the implicit trust period in classified systems
- Reduces the maximum undetected session hijacking window from **hours** to **minutes**
- Compliant with NIST AAL3 and PCI DSS v4.0 session requirements

---

## Sector 3: Healthcare

### Use Case 6: Hospital Network Trust Management (IoMT Security)

**Problem:** Hospitals deploy thousands of Internet of Medical Things (IoMT) devices — infusion pumps, patient monitors, imaging systems — alongside clinician workstations, guest Wi-Fi, and administrative systems. These devices often run legacy firmware, cannot support endpoint agents, and coexist on the same network infrastructure. A compromised infusion pump could serve as a lateral movement vector to reach patient records.

**How DCTA Addresses This:**
- **Network domain** monitoring detects anomalous communication patterns from IoMT devices
- **Dynamic weighting** suppresses erratic IoMT sensor readings (inherently noisy) without false-positive lockouts that could disrupt clinical workflows
- **Gray-Area Routing** quarantines suspicious IoMT devices to a limited network segment without disrupting patient care
- The **tiered trust architecture** (from the thesis's future work) enables:
  - Tier 1 (IoMT device): Binary compliance check only
  - Tier 2 (Ward gateway): Simplified DS fusion
  - Tier 3 (Hospital data centre): Full Ensemble evaluation

**Key Components Used:** Variance-based weighting (handles IoMT noise), Gray-Area Routing, tiered architecture

**Quantifiable Benefits:**
- Reduces IoMT-related false-positive network isolation events (critical for patient safety)
- Enables microsegmentation of clinical devices without operational disruption
- Proportional access: diagnostic devices access imaging servers but not patient billing systems

**Justification:** Healthcare breaches are the costliest across all industries (IBM, 2024). IoMT devices are the most vulnerable entry points. The DCTA's ability to handle inherently noisy signals without catastrophic lockouts is uniquely suited to clinical environments where false negatives *and* false positives both endanger patients.

---

### Use Case 7: Remote Telehealth Security

**Problem:** Telehealth consultations involve clinicians accessing patient records from home networks, personal devices, and mobile connections. HIPAA requires strict access controls, but aggressive security creates friction that disrupts patient care.

**How DCTA Addresses This:**
- **Contextual Gray-Area Routing** allows clinicians to access patient records from home with Limited Access (view-only) while reserving full write access for hospital-secured connections
- **Ensemble Inertia** prevents session disruption during clinician consultations — a momentary Wi-Fi drop doesn't terminate a telehealth session mid-diagnosis
- **Temporal decay** ensures session expiration aligns with consultation durations (30-60 min typical appointment windows)

**Key Components Used:** Ensemble (Freshness + Inertia), Gray-Area Routing

**Quantifiable Benefits:**
- Zero session drops during active consultations (inertia absorbs transient network instability)
- HIPAA-aligned temporal controls
- Proportional access prevents over-privileged remote access to sensitive records

---

## Sector 4: Financial Services

### Use Case 8: Real-Time Transaction Trust Scoring

**Problem:** Financial institutions process millions of transactions daily. Fraudulent transactions must be detected in milliseconds without blocking legitimate activity. Current rule-based systems produce high false-positive rates that frustrate customers and increase operational costs.

**How DCTA Addresses This:**
- **DS evidential fusion** across transaction domains: Identity (cardholder authentication), Device (terminal/browser fingerprint), Network (geo-location, IP reputation), Application (transaction pattern, amount deviation)
- **Variance-based weighting** dynamically adjusts the influence of each domain based on stability — a customer who always transacts from the same device has a high-weight Device signal; a new device introduction triggers elevated Uncertainty
- **Conflict detection** (K coefficient) flags transactions where identity is strong but location or device is anomalous

**Key Components Used:** Four-domain DS fusion, variance weighting, conflict coefficient

**Quantifiable Benefits:**
| Metric | Rule-Based | DCTA Fusion |
|:---|:---:|:---:|
| False-positive rate | ~15-30% | ~7.5% |
| Detection latency | ~50-200 ms | ~18.5 ms (computation only) |
| Contextual granularity | Binary (approve/decline) | 3-tier (approve, step-up auth, decline) |

**Justification:** The 73% false-positive reduction demonstrated in the thesis directly translates to fewer blocked legitimate transactions, reduced customer friction, and lower manual review costs.

---

### Use Case 9: High-Frequency Trading Infrastructure Security

**Problem:** High-frequency trading (HFT) environments demand microsecond-level latency and cannot tolerate security-induced delays. However, a compromised trading terminal could execute unauthorized trades for extended periods before detection.

**How DCTA Addresses This:**
- **Exponential temporal decay** (λ ≥ 5.0) forces continuous re-verification of trading terminal sessions
- The additional **6.5 ms latency** of the Ensemble model is negligible relative to HFT execution windows (typically 10-100 ms end-to-end)
- **Conflict detection** immediately flags if a terminal's network behaviour deviates from its identity profile (e.g., trades originating from an unexpected geographic location)
- **Enforcement-agnostic architecture** integrates with existing trading infrastructure without replacing exchange connectivity

**Key Components Used:** Aggressive exponential decay, conflict detection, enforcement-agnostic PDP

**Quantifiable Benefits:**
- Sub-23.5 ms trust evaluation — compatible with HFT latency requirements
- Eliminates multi-hour implicit trust windows on trading terminals
- Automated trust-based circuit breakers for anomalous trading patterns

---

## Sector 5: Critical Infrastructure & IoT

### Use Case 10: Industrial Control System (ICS/SCADA) Protection

**Problem:** Critical infrastructure — power grids, water treatment, oil pipelines — runs on legacy ICS/SCADA systems designed for reliability, not security. These systems often lack modern authentication, run proprietary protocols, and operate in environments where availability is paramount (a false-positive lockout could disrupt power distribution).

**How DCTA Addresses This:**
- **Variance-based dynamic weighting** is ideal for SCADA environments where sensor readings are inherently noisy — minor fluctuations don't trigger lockouts
- **Gray-Area Routing** enables proportional response: a suspicious SCADA command routes to a monitoring queue rather than being blocked outright, preserving operational continuity
- **Temporal decay** ensures that even authenticated engineering workstations cannot maintain indefinite access to SCADA controllers
- The **Gateway-to-Gateway deployment model** (acknowledged in the thesis) can bridge legacy OT systems with the trust engine at the network boundary

**Key Components Used:** Variance weighting (noise tolerance), Gray-Area Routing, temporal decay, gateway model

**Quantifiable Benefits:**
- Reduces false-positive operational disruptions in critical infrastructure (the #1 concern)
- Enforces session ephemerality for engineering workstations accessing SCADA controllers
- Proportional response preserves availability while flagging anomalies for investigation

**Justification:** The Colonial Pipeline (2021) and Oldsmar water treatment (2021) incidents demonstrate that ICS/SCADA systems are actively targeted. The DCTA framework's noise tolerance and proportional access model are uniquely suited to environments where availability requirements override traditional binary security.

---

### Use Case 11: Smart City / Edge Computing Trust Management

**Problem:** Smart city deployments involve thousands of edge devices — traffic sensors, environmental monitors, surveillance cameras — each generating continuous telemetry. These devices are physically exposed, computationally constrained, and connect over unreliable wireless networks.

**How DCTA Addresses This:**
- The **tiered architecture** from the thesis's future work section directly applies:
  - Edge devices perform binary compliance checks (Tier 1)
  - Neighbourhood gateways perform simplified DS fusion (Tier 2)
  - City data centre runs full Ensemble evaluation (Tier 3)
- **Welford's online algorithm** (proposed for resource-constrained environments) reduces per-device memory from 320 bytes to 48 bytes
- **Event-driven evaluation** (proposed) reduces computation by 80%, extending battery life
- **Federated lightweight trust** distributes computation across device mesh networks

**Key Components Used:** Tiered architecture, lightweight mathematical approximations, event-driven evaluation

**Quantifiable Benefits:**
- 80% energy reduction through event-driven evaluation
- 48-byte per-device memory footprint (compatible with MCU constraints)
- Proportional trust across physically exposed, computationally constrained devices

---

### Use Case 12: Multi-Cloud / Cloud-Native Application Security

**Problem:** Modern enterprises operate across multiple cloud providers (AWS, Azure, GCP) with ephemeral containerised workloads (Kubernetes). Trust between services, pods, and APIs must be continuously evaluated as workloads scale up, migrate, and terminate dynamically.

**How DCTA Addresses This:**
- **Enforcement-agnostic PDP** integrates with service mesh proxies (Envoy — already validated in the testbed) as sidecars
- **Temporal decay** aligns with container lifecycle — ephemeral pods receive aggressive short-term decay; long-running services build inertia
- **Variance-based weighting** handles the inherent instability of containerised networking (pod restarts, rolling updates, network policy changes)
- **OPA integration** (validated in the testbed) provides Kubernetes-native policy enforcement via Rego

**Key Components Used:** Enforcement-agnostic PDP, Envoy proxy integration, OPA, temporal decay

**Quantifiable Benefits:**
- Native Kubernetes/service mesh integration (demonstrated with Envoy + OPA)
- Trust computation that adapts to container lifecycle dynamics
- Microsegmentation at the pod level driven by continuous trust scores
- Zero-trust service-to-service communication with proportional access tiers

---

## Prioritisation Matrix

| # | Use Case | Sector | Implementation Readiness | Impact | Thesis Alignment |
|:---:|:---|:---|:---:|:---:|:---:|
| 1 | Hybrid Workforce Access | Enterprise | ★★★★★ | ★★★★★ | ★★★★★ |
| 2 | Insider Threat Detection | Enterprise | ★★★★☆ | ★★★★★ | ★★★★★ |
| 4 | Federal ZT Compliance | Government | ★★★★★ | ★★★★★ | ★★★★★ |
| 8 | Transaction Trust Scoring | Financial | ★★★★☆ | ★★★★★ | ★★★★☆ |
| 12 | Multi-Cloud Security | Enterprise | ★★★★★ | ★★★★☆ | ★★★★★ |
| 3 | BYOD Management | Enterprise | ★★★★☆ | ★★★★☆ | ★★★★☆ |
| 6 | Hospital IoMT | Healthcare | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| 7 | Telehealth Security | Healthcare | ★★★★☆ | ★★★★☆ | ★★★★☆ |
| 5 | Classified Networks | Defence | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| 9 | HFT Security | Financial | ★★★☆☆ | ★★★★☆ | ★★★☆☆ |
| 10 | ICS/SCADA | Critical Infra | ★★☆☆☆ | ★★★★★ | ★★★☆☆ |
| 11 | Smart City / Edge | IoT | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ |

### Top 3 Priority Use Cases:
1. **Hybrid Workforce Access** — Highest readiness, immediate demand, directly validated by testbed
2. **Federal ZT Compliance** — Guaranteed demand from DoD mandate, framework provides missing algorithm
3. **Insider Threat Detection** — Highest financial impact, Ensemble Model uniquely positioned

---

## Summary: Why Each Contribution Matters

| Thesis Contribution | Primary Use Cases Enabled |
|:---|:---|
| **Dynamic Variance-Based Weighting** | IoMT, SCADA, BYOD — any environment with noisy/unreliable sensors |
| **Dempster-Shafer Multi-Domain Fusion** | All use cases — the foundation of proportional, context-aware access |
| **Contextual Gray-Area Routing** | Healthcare, critical infrastructure — where false positives endanger operations |
| **Temporal Decay (Linear/Exponential)** | Classified networks, HFT, insider threats — aggressive session management |
| **Ensemble Trust Model** | Enterprise hybrid workforce, federal compliance — balancing security with usability |
| **Enforcement-Agnostic PDP** | Multi-cloud, Kubernetes, service mesh — deployment flexibility |
| **Reproducible Testbed** | Academic research, federal R&D — open-source reference implementation |
