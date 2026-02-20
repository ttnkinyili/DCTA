# Justification of Trust Thresholds for Access Control

## Executive Summary
This document justifies the specific numerical ranges used in the Ensemble Trust Model for access decisions.
These ranges are derived by mapping our **[0.0 - 1.0]** continuous trust score to the discrete **Confidence Levels** and **Trust Tiers** defined in authoritative industry frameworks (NIST, Google BeyondCorp, CVSS).

---

## 1. The Thresholds

| Trust Score ($T$) | Decision | Industry Equivalent |
| :--- | :--- | :--- |
| **$0.75 < T \le 1.00$** | **Full Access** | **High Confidence** (NIST) / **Tier 3** (BeyondCorp) |
| **$0.45 \le T \le 0.75$** | **Limited Access** | **Moderate Confidence** (NIST) / **Tier 2** (BeyondCorp) |
| **$T < 0.45$** | **No Access** | **Low Confidence** (NIST) / **Tier 1** (BeyondCorp) |

---

## 2. Justification & Citations

### 2.1 Full Access ($> 0.75$)
**Definition**: The entity is fully authenticated, compliant, and operating in a secure context.

*   **Google BeyondCorp**: Maps to **"Highly Privileged Access"** (Tier 3).
    *   *Citation*: "Devices in this tier possess the highest level of security hardening... and are granted greater privileges for sensitive internal resources." [Source: Google Cloud / BeyondCorp Research]
    *   *Why 0.75?* This aligns with the upper quartile of trust, requiring effectively perfect scores in at least 3 of 4 domains (Network, Device, Identity) to achieve.

*   **NIST SP 800-63B**: Maps to **IAL3 / AAL3** (Identity/Authenticator Assurance Level 3).
    *   *Citation*: Requires "proof of possession of a key... hard cryptographic authenticator... and verifiable user presence."

### 2.2 Limited Access ($0.45 - 0.75$)
**Definition**: The entity is authenticated, but the context carries elevated risk (e.g., BYOD, Public Wi-Fi).

*   **Google BeyondCorp**: Maps to **"Basic Access"** (Tier 2).
    *   *Citation*: "Allows for more access than untrusted devices, but still has limitations." Used for standard web apps (email, calendar) but restricts sensitive infrastructure.
    *   *Why 0.45-0.75?* This range captures the "Middle Ground" where valid credentials exist (driving the score up from 0) but environmental factors (Network/Device) drag the average down.
    *   *CVSS alignment*: Maps to the inverse of **Medium Severity (4.0 - 6.9)**. If Risk is Medium, Trust is Medium.

*   **NIST SP 800-207**: Maps to **"Moderate Confidence"**.
    *   *Citation*: "Access to a resource is granted if the calculated trust score surpasses a pre-configured threshold... factors such as device status can tailor the access granted."

### 2.3 No Access ($< 0.45$)
**Definition**: The entity is unknown, non-compliant, or behaving anomalously.

*   **Google BeyondCorp**: Maps to **"Untrusted"** (Tier 1).
    *   *Citation*: "Devices in this tier have minimal security hardening and are typically allowed to access only publicly available data."
    *   *Why < 0.45?* A score below 0.50 mathematically implies that **Uncertainty ($m(\Theta)$)** or **Disbelief** outweighs Belief. In Dempster-Shafer theory, you cannot grant access when ignorance dominates knowledge.

*   **CVSS v3.1**: Maps to the inverse of **High/Critical Severity (7.0 - 10.0)**.
    *   *Citation*: A device with a High vulnerability (Risk > 0.7) implies Trust < 0.3.

---

## 3. Mathematical Basis for 0.75 / 0.45

Why these specific numbers?

1.  **The "Majority Rule" (0.75)**:
    In a 4-domain system (User, Device, Network, App), if **1 domain fails completely** (Score 0.0) and 3 are perfect (1.0), the simple average is **0.75**.
    *   *Implication*: To get $>0.75$ (Full Access), you **cannot fail a single domain**. You must be perfect or near-perfect in all.

2.  **The "Coin Toss" (0.50 $\rightarrow$ 0.45)**:
    A score of 0.50 represents "Unknown" or "Random Chance". We lower the threshold slightly to **0.45** to account for **measurement noise** (Variance).
    *   *Implication*: If the system is less than 45% sure you are safe, it is statistically safer to deny you. This provides a 5% "buffer" for benign jitter before revocation.

---

---

## 4. Unified Compliance & Mapping Matrix

The following table provides a **holistic view** of how our Access Decisions map across major industry frameworks.
It demonstrates that a decision of "Full Access" is not arbitrary, but corresponds to specific, standardized criteria in NIST and CVSS.

| Access Decision | Trust Score | NIST SP 800-207 (Confidence) | NIST SP 800-63 (Assurance) | CVSS v3.1 Severity (Allowed Risk) | Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Full Access** | **> 0.75** | **High Confidence** | **IAL3 / AAL3** | **None (0.0)** | **"Gold Standard"**. Requires Hardware-based Auth + Managed Device + Zero Vulnerabilities. Equivalent to Top Secret/Critical system access. |
| **Full / Limited** | **0.60 - 0.75** | **High / Moderate** | **IAL2 / AAL2** | **Low (0.1 - 3.9)** | **"Silver Standard"**. Strong Auth (MFA) + Healthy Device. Minor non-exploitable issues (Low CVSS) are tolerated. |
| **Limited Access** | **0.45 - 0.60** | **Moderate Confidence** | **IAL2 / AAL2** | **Medium (4.0 - 6.9)** | **"Bronze Standard"**. Valid Identity, but Environment is risky (Public Wi-Fi, BYOD) or Device has unpatched moderate issues. Access is restricted to non-sensitive apps. |
| **No Access** | **< 0.45** | **Low Confidence** | **IAL1 / AAL1** | **High / Critical (≥ 7.0)** | **"Untrusted"**. The entity failed authentication or presents an unacceptable risk (e.g., active RCE vulnerability). All access is blocked. |

### Description of Mapping Columns
1.  **Trust Score**: The internal value calculated by our Ensemble Model.
2.  **NIST 800-207**: The "Confidence Level" required by the Policy Engine to grant access to resources of varying sensitivity.
3.  **NIST 800-63 (Identity)**: The rigor of the authentication event.
    *   *AAL3*: Hardware crypto (Smartcard/FIDO).
    *   *AAL2*: Software MFA (Push/OTP).
    *   *AAL1*: Password only (Single Factor).
4.  **CVSS v3.1**: The maximum *allowable* vulnerability severity on the device.
    *   *Logic*: If a device has a **High (CVSS 8.0)** vulnerability, it cannot qualify for "Full" or "Limited" access; it falls to **No Access**.

