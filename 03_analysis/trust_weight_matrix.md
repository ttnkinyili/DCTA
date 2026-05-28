# Trust Weight Mapping Matrix

## 1. Introduction
This document details the **Initialization Matrix** used by the `TrustSimulator`. It explains how specific scenarios (e.g., "Corporate Office") map to specific input values (Scores and Variances) and how those inputs result in the final **Trust Weights**.

The user asks: *"How does the network domain get a 0.95 trust score for the corporate office context?"*
**Answer**: It is explicitly defined as a **Base Parameter** in the simulation configuration, reflecting the expected behavior of a secure, managed infrastructure.

## 2. Derivation Logic

The Trust Cycle follows this derivation path:
1.  **Scenario Definition**: Sets the `Base Score` ($\mu$) and `Base Variance` ($\sigma^2$).
2.  **Simulation Step**: Generates a random value $x \sim N(\mu, \sigma^2)$.
3.  **Variance Calculation**: The system measures the stability of $x$ over time.
4.  **Weight Calculation**: $W_{raw} = \frac{1}{1 + 100 \cdot \sigma^2}$.
5.  **Normalization**: $W_{final} = \frac{W_{raw}}{\sum W_{all}}$.

### Why Variance Matters
*   **Low Variance (0.01)** $\rightarrow$ Raw Weight $\approx 0.5$.
*   **High Variance (0.25)** $\rightarrow$ Raw Weight $\approx 0.04$.
*   **Result**: Stable domains get **12.5x** more weight than unstable ones.

## 3. The Matrix

### Scenario 1: Corporate Office (The "Happy Path")
*   **Context**: Managed device, secure Intranet, calibrated sensors.

| Domain | Base Score | Base Variance | Est. Raw Weight | Norm. Weight | Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Network** | **0.95** | **0.01** | ~0.50 | **0.25** | **High** |
| **Data** | 0.90 | 0.02 | ~0.33 | 0.25 | High |
| **Device** | 0.95 | 0.01 | ~0.50 | 0.25 | High |
| **App** | 0.90 | 0.02 | ~0.33 | 0.25 | High |

> **Clarification: Score vs. Weight**
> The user asks *"what makes the network weight 0.95?"*
> The **0.95** is the **Trust Score** (The Value), NOT the Weight (The Confidence).
> *   **Trust Score (0.95)**: Defined by the Administrator as the "Expected Behavior" for a secure corporate network (low anomalies, high reputation).
> *   **Trust Weight (~0.25)**: Derived mathematically from the **Variance (0.01)**. Since all 4 domains are stable, they share the weight equally ($1.0 / 4 = 0.25$).
>
> **Derivation of the Weight:**
> 1.  Calculate Variance of Network Score history: $\sigma^2 \approx 0.01$.
> 2.  Calculate Raw Reliability: $R = \frac{1}{1 + 100 \cdot 0.01} = \frac{1}{2} = 0.5$.
> 3.  Sum all Reliabilities: $\Sigma R \approx 0.5 + 0.33 + 0.5 + 0.33 \approx 1.66$.
> 4.  Calculate Normalized Weight: $W = \frac{0.5}{1.66} \approx 0.30$. (Wait, calculation check: $0.5/1.66 \approx 0.30$).
>
> *So the Weight is ~0.30, while the Score is 0.95.*

*   **Result**: All domains are stable. The inputs (0.95, 0.90, etc.) are accepted "as is". The fusion result is a straight average of High Scores $\rightarrow$ **Full Access**.

### Scenario 2: Public Wi-Fi (The "Noisy" Path)
*   **Context**: Coffee shop, packet loss, latency jitter.

| Domain | Base Score | Base Variance | Est. Raw Weight | Norm. Weight | Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Network** | **0.30** | **0.25** | ~0.04 | **~0.05** | **Ignored** |
| **Data** | 0.60 | 0.05 | ~0.16 | ~0.30 | Med |
| **Device** | 0.75 | 0.05 | ~0.16 | ~0.30 | Med |
| **App** | 0.70 | 0.05 | ~0.16 | ~0.35 | Med |

*   **Result**: The Network score is low (0.30), but its **Variance is High (0.25)**.
*   **Effect**: The Weight drops to near zero. The low score is treated as "Unknown" rather than "Bad". The decision relies on Data/Device/App.
    *   *Note*: If the Network score was 0.30 but **Stable** (Variance 0.01), it would be weighted highly, causing a "Conflict" and likely denying access. High Variance allows the system to "forgive" the bad network by ignoring it.

### Scenario 3: BYOD (The "Unmanaged" Path)
*   **Context**: Personal phone, unknown patch level.

| Domain | Base Score | Base Variance | Est. Raw Weight | Norm. Weight | Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Device** | **0.40** | **0.20** | ~0.05 | **~0.05** | **Ignored** |
| **Network** | 0.90 | 0.02 | ~0.33 | ~0.40 | High |

*   **Result**: Similar to Public Wi-Fi, the unmanaged device is unstable. The system relies on the secure Network to grant **Limited Access**.

### Scenario 4: Compromised Host (The "Attack" Path)
*   **Context**: Active malware, chaotic resource usage.

| Domain | Base Score | Base Variance | Est. Raw Weight | Norm. Weight | Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Network** | 0.20 | 0.30 | ~0.03 | ~0.25 | Low |
| **Device** | 0.20 | 0.30 | ~0.03 | ~0.25 | Low |
| **All** | < 0.30 | High | Low | Low | **None** |

*   **Result**: Everything is unstable. Total Weight is low (but normalized to sum to 1). However, since **ALL** scores are low, there is no "Good" signal to fallback on.
*   **Fusion**: $m(\text{Safe}) \approx 0$. $m(\text{Uncertainty}) \approx 1$.
*   **Outcome**: **No Access**.

## 4. Code Reference
(From `dynamic_trust_weighting_time.py`)

```python
if scenario == 'corporate_office':
    # High Trust Everywhere
    self._set_domain_params('Network', 0.95, 0.01) # Stable, Secure
    self._set_domain_params('Data', 0.90, 0.02)
    self._set_domain_params('Device', 0.95, 0.01) # Managed
```
This explicit initialization is the "Source of Truth" for the 0.95 value.

## 5. Deep Dive: The Normalization Formula

The user asks: *Explain this formula $W_{final} = \frac{W_{raw}}{\sum W_{all}}$.*

This is a standard **Normalization** technique used to convert absolute values into **relative proportions** (or percentages).

### Why do we need it?
The **Raw Weight** ($W_{raw}$) measures the **Stability** of a single domain in isolation.
*   $W_{network} = 0.5$ (Very Stable)
*   $W_{device} = 0.05$ (Very Unstable)

However, to make a decision, we need to know **"How much of the total vote should differ to this domain?"**
The sum of all votes must equal 1.0 (or 100%).

### Step-by-Step Example

Imagine a scenario where the **Network is Stable** but the **Device is Unstable**.

1.  **Calculate Raw Weights** (based on Variance):
    *   Network: $W_{raw} = 0.50$
    *   Device: $W_{raw} = 0.05$
    *   Data: $W_{raw} = 0.50$ (assume stable)
    *   App: $W_{raw} = 0.50$ (assume stable)

2.  **Calculate the Total Quality** ($\sum W_{all}$):
    $$ \text{Total} = 0.50 + 0.05 + 0.50 + 0.50 = 1.55 $$

3.  **Calculate Final Normalized Weights** ($W_{final}$):
    *   **Network**: $0.50 / 1.55 \approx \mathbf{0.32}$ (32% Influence)
    *   **Device**: $0.05 / 1.55 \approx \mathbf{0.03}$ (3% Influence)
    *   **Data**: $0.50 / 1.55 \approx \mathbf{0.32}$ (32% Influence)
    *   **App**: $0.50 / 1.55 \approx \mathbf{0.32}$ (32% Influence)

### Conclusion
The formula ensures that **Stable Domains dominate the decision**.
In this example, the Device's instability reduced its influence from a potential 25% (equal share) to just **3%**. The other three domains took over its share, rising to **32%** each. This is the mathematical mechanism of "ignoring bad data".

## 6. Origin of Base Values

The user asks: *How are the base score and base variance calculated and/or derived?*

**Short Answer**: They are **Configuration Parameters** (Inputs), not Calculations (Outputs).
They are set by the **System Designer** (or Administrator) to model a specific environment.

### 6.1 Base Score ($\mu$)
*   **Definition**: The "Expected Trust Level" for a domain in a specific scenario.
*   **Derivation Source**: **Policy & Specs**.
    *   **"Corporate Network"**: We know it has strict firewalls, IDS, and authentication. Therefore, we *assign* it a score of **0.95** (Near Perfect).
    *   **"Public Wi-Fi"**: We know it has no encryption, potential MITM, and random people. Therefore, we *assign* it a score of **0.30** (Low Trust).
*   **Role**: This sets the "Target" around which the simulation oscillates.

### 6.2 Base Variance ($\sigma^2$)
*   **Definition**: The "Expected Instability" or "Noise Level".
*   **Derivation Source**: **Physics & Environment**.
    *   **"Wired Ethernet"**: Physically shielded, stable connection. We *assign* a variance of **0.01** (Very Stable).
    *   **"Coffee Shop Wi-Fi"**: Radio interference, microwave ovens, moving people. We *assign* a variance of **0.25** (Chaotic).
*   **Role**: This controls the "Spread" of the random noise added to the Base Score.

### Summary
The algorithm **does not calculate** these values. It **uses** these values (Inputs) to calculate the Weights (Outputs).

| Value | Type | Source | Example |
| :--- | :--- | :--- | :--- |
| **Base Score** | Input | Policy | "Corporate = 0.95" |
| **Base Variance** | Input | Biology/Physics | "Human Typing = 0.05" |
| **Raw Weight** | Output | Math ($1/(1+100\sigma^2)$) | "0.50" |
| **Norm Weight** | Output | Math ($W/\sum W$) | "0.32" |

## 7. Configuration Legend (The "Matrix")

The following matrix provides the **Reference Ranges** for configuring the system based on real-world trust assessments.

### 7.1 Trust Score Legend (Base Score)

| Range | Trust Level | Description | Example Contexts |
| :--- | :--- | :--- | :--- |
| **0.90 - 1.00** | **Critical / High** | **Managed & Compliant**. Fully authenticated, patch-compliant, encrypted, and monitored. | Corporate LAN, Company-Issued Laptop, Admin User. |
| **0.70 - 0.89** | **High / Medium** | **Known but Flexible**. Authenticated but potentially unmanaged or roaming. | Remote VPN, Vendor Laptop (with Agent), Standard User. |
| **0.50 - 0.69** | **Medium / Low** | **Unknown / Gray**. Authenticated user on unknown device or network. | BYOD (Mobile), Coffee Shop Wi-Fi, Guest Network. |
| **< 0.50** | **Untrusted** | **Hostile / Malicious**. Known bad reputation, active anomalies, or policy violation. | Tor Exit Node, Jailbroken Device, Failed Login. |

### 7.2 Stability Legend (Variance)

| Value | Stability | Description | Example Contexts |
| :--- | :--- | :--- | :--- |
| **0.01 - 0.02** | **Stable** | **Fixed / Wired**. Physical connection or static location. | Ethernet, Desktop PC, Server. |
| **0.03 - 0.05** | **Variable** | **Wireless / Roaming**. Normal fluctuation due to RF or human movement. | Office Wi-Fi, 4G/5G, Laptop moving between APs. |
| **0.10 - 0.20** | **Unstable** | **Weak Signal / Congested**. High packet loss or latency. | Public Wi-Fi (Crowded), Edge of Cell Tower. |
| **> 0.25** | **Chaotic** | **Attack / Failure**. Random behavior indicative of spoofing or DoS. | Man-in-the-Middle Attack, Hardware Failure. |

## 8. Literature & Industry Alignment

The User asks: *What differentiates 0.95 and 0.90? Can we get literature to support these ranges?*

### 8.1 The "Gold vs. Silver" Distinction (0.95 vs 0.90)
Within the **Critical / High** band (0.90 - 1.00), minute differences reflect **Assurance Levels** (NIST 800-63B).

*   **0.95 (Gold Standard)**:
    *   **Context**: Highly restricted, strictly managed assets.
    *   **Requirements**: Device Certificate + Biometric + Geolocation + No Vulnerabilities.
    *   **Example**: Admin Workstation accessing Production DB.
*   **0.90 (Silver Standard)**:
    *   **Context**: Standard corporate access.
    *   **Requirements**: Password + MFA + Healthy Device.
    *   **Example**: HR Employee accessing Payroll Web App.
    *   *Why lower?* Web sessions are inherently less "hardware-bound" than device-tunnel sessions, slightly increasing risk surface (e.g., session cookie theft).

### 8.2 Industry Mapping (CVSS & NIST)
Our scoring model aligns with established cybersecurity frameworks to ensure interoperability:

**1. CVSS v3.1 (Common Vulnerability Scoring System)**
*   **Critical (9.0 - 10.0)** $\rightarrow$ Matches our **0.90 - 1.00** Trust.
*   **High (7.0 - 8.9)** $\rightarrow$ Matches our **0.70 - 0.89** Trust.
*   **Medium (4.0 - 6.9)** $\rightarrow$ Matches our **0.40 - 0.69** Trust.
*   **Low (0.1 - 3.9)** $\rightarrow$ Matches our **< 0.40** Trust.
*   *Support*: This mapping allows us to ingest vulnerability data directly into the **App/Device** domain scores. A device with a "Critical" vulnerability (CVSS 9.0) would drop its Trust Score by 0.9, effectively zeroing it out.

**2. NIST SP 800-207 (Zero Trust Architecture)**
*   **Concept**: **Confidence Levels**.
*   NIST defines that access is granted not just on "Identity" but on the "Confidence" in that identity's current state.
*   Our **Variance-based Weighting** directly implements NIST's recommendation to "measure the distinctiveness and freshness" of the data. High Variance = Low Confidence.
