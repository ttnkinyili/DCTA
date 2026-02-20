# Ensemble Trust Model Analysis: Inertia vs. Freshness

## 1. Executive Summary
The Ensemble Trust Model introduces a **Weighted Mixture** approach to combine:
1.  **Inertia (Contextual Memory)**: Previous trust state derived from 48-hour history.
2.  **Fusion (Instant Signal)**: Real-time evidence derived from 30-minute session freshness.

**Key Finding**: The model successfully smooths out short-term volatility while maintaining strict security boundaries. The "Corporate" scenario maintains high trust throughout the session, whereas the "Compromised" scenario is correctly identified and restricted, despite the inertia.

## 2. Model Logic
$$ T_{ensemble} = \alpha \cdot T_{inertia} + (1 - \alpha) \cdot T_{instant} $$

Where:
*   $T_{instant}$: Pure spatial fusion score (normalized to remove double-decay).
*   $T_{inertia} = T_{prev} \cdot e^{-\lambda_{48h}}$
*   $\alpha = 1 - e^{-\mu_{30m}}$ (Weight of History increases as Data Freshness decreases).

This ensures that at the start of a session ($t=0$), confidence is based on the **Current Signal**. As the session ages ($t \rightarrow 30$), confidence relies increasingly on **Established History**, preventing premature session expiry *valid* contexts, while still allowing *invalid* contexts to fail via the underlying spatial fusion.

## 3. Scenario Analysis

### 3.1 Corporate Office (Stability)
*   **Behavior**:
    *   Start: Full Access (~0.79).
    *   End: Full Access (~0.79).
*   **Analysis**: The inertia component (prev trust ~1.0) perfectly counteracts the slight variance or decay in the instant signal, effectively "locking in" the trust for the duration of the session. This solves the "Jittery Exec" problem where minor fluctuations cause annoying re-auths.

### 3.2 Compromised Host (Security)
*   **Behavior**:
    *   Start: No Access (~0.23).
    *   End: No Access (~0.30).
*   **Analysis**: Despite the inertia trying to carry value forward, the *base* spatial trust is so low that the weighted mixture never crosses the threshold. This confirms that **Inertia does not overwrite Bad Behavior**.

### 3.3 Public Wi-Fi (Smoothing)
*   **Behavior**:
    *   Start: Limited Access (~0.57).
    *   End: Limited Access (~0.60).
*   **Analysis**: The model provides a stable "Limited" state. The initial volatility of the network is smoothed out by the history component, allowing for a consistent user experience without elevating risk.

## 4. Conclusion
The Ensemble Model provides a superior balance of **Usability** (Stability via Inertia) and **Security** (Responsiveness via Freshness Weighting). It effectively implements a "Trust but Verify" approach where verification frequency scales with signal freshness.
