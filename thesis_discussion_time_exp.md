# Dynamic Trust Fusion with Exponential Temporal Decay

## Abstract
This document explores the theoretical friction between continuous authentication and session longevity by introducing **Exponential Temporal Decay** into the Weighted Belief Fusion architecture. The core thesis expands upon the premise that *Trust is a Function of Time* by evaluating how an aggressive decay curve impacts the "Effective Session Length" in various contextual states.

## 1. Introduction: The Ephemerality of Verification
Static authentication protocols trust a user for the entirety of their session (the "Implicit Trust Period"). While our previous linear temporal decay model addressed this by enforcing a steady erosion of trust, an exponential model challenges the fundamental concept of a "Session."

By applying the decay function $D(t) = e^{-\lambda (t / T_{session})}$, the architecture mathematically asserts that the instant a cryptographic handshake concludes, its value plummets. It effectively establishes a dynamic **"Time-to-Live" (TTL) that is heavily front-loaded.**

## 2. Theoretical Implications of Exponential Depreciation

### 2.1 The Accelerated Decay Threshold
With $\lambda = 3.0$ over a 30-minute session:
*   At $t=0$: $D(t) = 1.0$ (Full Trust)
*   At $t=10$: $D(t) \approx 0.36$ (Severe Depreciation)

In our simulation, the Final Trust Score ($T_{final}$) is the product of the Spatial Trust ($T_{spatial}$) and the Decay Factor ($D(t)$). 
This implies that even if $T_{spatial}$ is a perfect $1.0$ (Corporate Office, managed device), the final trust score will crash through the "Limited Access" threshold ($0.75$) and plummet into "No Access" ($< 0.45$) within the first $5-10$ minutes. 

### 2.2 Security vs. Operational Viability
**The Security Benefit**: Session hijacking becomes practically impossible. Stolen cookies or transient network compromises are suffocated by the rapid expiration of the authentication event's initial weight.

**The Operational Reality**: A pure exponential decay model is unusable in a production environment. Users would be forcefully ejected from their applications every few minutes, causing complete operational paralysis.

## 3. Scenario Analysis: The Collapse of the Effective Session

We evaluated this model against our six canonical scenarios, noting the severe compression of access durations compared to the linear variant.

| Scenario | Characteristics | Exponential Outcome | Comparison to Linear Decay |
| :--- | :--- | :--- | :--- |
| **Corporate Office** | High initial spatial trust ($\approx 0.95$). | **Limited $\rightarrow$ No Access** | The "Full Access" buffer is almost instantly erased; the session terminates in fraction of the linear time. |
| **Remote / VPN** | Strong signals across Device/App/Data. | **Limited $\rightarrow$ No Access** | The high-trust buffer is insufficient to combat the exponential curve. |
| **Public Wi-Fi** | Network trust fluctuates ($\approx 0.55$). | **Immediate No Access** | The combination of low initial trust and rapid depreciation denies access almost immediately. |
| **Untrusted Device / BYOD** | Device score is persistently low. | **Immediate No Access** | Evaluated as too risky to grant even a momentary session. |
| **Compromised** | All domains failing ($BetP(\text{Safe}) < 0.10$). | **No Access** | Irrelevant; spatial trust correctly denies access before time can decay. |

## 4. The Ensemble Model Imperative

The simulation of **Exponential Temporal Decay** perfectly validates the architectural necessity of the **Ensemble Trust Model**. 

If we accept that the value of an initial authentication event *must* decay rapidly for security reasons (Exponential Decay), then the system *must* have a mechanism to replace that lost value for operational reasons. 

The Ensemble Model resolves this paradox. It intentionally utilizes the aggressive exponential decay to kill off the "Fresh Verification" signal ($W_{short}$), but uses that identical temporal function to inversely transfer weight onto the user's **Historical Inertia** ($1 - W_{short}$). 

Therefore, exponential decay proves that sustained Zero Trust access cannot be supported by continuous *verification* (which decays), but must be carried by continuous *behavioral consistency* (which accumulates).
