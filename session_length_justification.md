# Justification of Session Lengths in Heterogeneous Enterprise Networks

## Executive Summary
This document analyzes the chosen session lengths (**30 Minutes** for Short-Term Network Trust, **48 Hours** for Long-Term Device Trust) against authoritative industry standards (NIST, PCI DSS, OWASP, Microsoft).

**Verdict**:
*   **30 Minutes (Short Term)**: **Justifiable** for Standard High Security. (Aligns with NIST AAL2 Inactivity).
    *   *Correction for Critical Data*: Should be **15 Minutes** (PCI DSS compliance).
*   **48 Hours (Long Term)**: **Justifiable** for Device Trust Reuse (Microsoft "Keep me signed in").
    *   *Correction for Strict Compliance*: NIST AAL2/3 mandates periodic re-authentication every **12 Hours**.

---

## 1. Short-Term Network Session (30 Minutes)

**Role**: Defines the window of "Freshness" for network/behavioral signals before re-verification is prioritized.

### Justification
1.  **NIST SP 800-63B (Identity Guidelines)**
    *   **Citation**: *Section 5.2.2 (AAL2)*: "Reauthentication... is required following any period of inactivity lasting **30 minutes** or longer."
    *   **Analysis**: 30 minutes is the standard industry benchmark for "Moderate Assurance" inactivity. It balances security (limiting hijacking window) with usability (preventing frustration during reading/thinking tasks).

2.  **OWASP Session Management Cheat Sheet**
    *   **Citation**: "Common idle timeout ranges are **2-5 minutes** for high-value applications... and **15-30 minutes** for standard enterprise applications."
    *   **Analysis**: For a heterogeneous network, 30 minutes is an appropriate baseline.

3.  **PCI DSS v4.0 (Critical Data Context)**
    *   **Citation**: *Requirement 8.1.8*: "User sessions must automatically terminate after **15 minutes** of inactivity."
    *   **Recommendation**: If the environment handles Credit Card Data (CDE), the 30-minute parameter **MUST** be lowered to **15 minutes**.

---

## 2. Long-Term Device Session (48 Hours)

**Role**: Defines the window of "Inertia" where a known, healthy device retains some trust even without fresh signals.

### Justification
1.  **Microsoft Entra ID (Azure AD)**
    *   **Citation**: *Token Lifetimes*: "Refresh tokens for Single Page Apps (SPA) have a default lifetime of **24 hours**." Standard Refresh Tokens can last up to **90 days** (rolling).
    *   **Analysis**: 48 Hours falls well within the standard "Refresh Token" window. It represents a "Rolling Session" where the device is trusted to request new access tokens without a full login, provided it isn't revoked.

2.  **NIST SP 800-63B (Strict Compliance)**
    *   **Citation**: *Section 5.2.2 (AAL2)*: "Periodic reauthentication of the subscriber... shall be performed at least once every **12 hours**."
    *   **Analysis**: For strict FedRAMP/Gov compliance, **48 hours is too long**. The hard limit for a session (without re-proofing) should be 12 hours.

3.  **Usability vs. Risk (The "Keep Me Signed In" Factor)**
    *   **Context**: In a modern Zero Trust environment (e.g., Zscaler, CrowdStrike), "Device Trust" is often evaluated continuously. If the specific *session* is 48 hours, it implies the **Device Certificate** is treated as valid proof of identity for 2 days.
    *   **Justification**: This aligns with a "Weekend Gap" (Friday 5 PM to Monday 9 AM is >48h). A 48h window covers a standard work-from-home gap without forcing a full re-login on Monday morning, optimizing productivity.

---

## 3. Recommended Configuration Matrix

Based on the research, we recommend defining three "Time Profiles" for the simulator:

| Profile | Short-Term (Freshness) | Long-Term (Inertia) | Justification |
| :--- | :--- | :--- | :--- |
| **Strict / PCI / AAL3** | **15 Minutes** | **12 Hours** | PCI DSS v4.0 (Idle) + NIST AAL3 (Periodic). Max security. |
| **Standard / Corp / AAL2** | **30 Minutes** | **24 Hours** | NIST AAL2 (Idle). 24h allows daily login cycle. |
| **Flexible / BYOD** | **60 Minutes** | **48 Hours** | Microsoft Default (approx). Optimizes for usability. |

*   **Current Simulator Default**: **Standard/Flexible Hybrid** (30m / 48h). This is a defensible "balanced" posture for a general enterprise.
