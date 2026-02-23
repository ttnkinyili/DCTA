# Linear vs. Exponential Temporal Decay in Zero Trust Fusion

## 1. The Core Difference

### Linear Temporal Decay
*   **Mechanism**: Trust decreases at a constant, steady rate over a set period. 
*   **Formula**: $D(t) = \max(0, 1 - \frac{t}{T_{session}})$
*   **Behavior**: If the session is 30 minutes, the trust score drops by the exact same mathematical weight during minute 1 as it does during minute 29. 
*   **Use Case**: Best for simple, predictable Time-to-Live (TTL) mechanisms where the architecture requires a hard cutoff that approaches zero evenly. 

### Exponential Temporal Decay
*   **Mechanism**: Trust decreases rapidly at the very beginning of the session, and the *rate* of decay slows down as time progresses, creating an asymptotic, curved degradation path.
*   **Formula**: $W(t) = e^{-\lambda \cdot t}$ (where $\lambda$ dictates the velocity of the initial drop).
*   **Behavior**: Trust plummets heavily in the first few minutes, rapidly shifting the system's reliance away from the "current precise moment" and forcing it to look elsewhere for validation. 
*   **Use Case**: Best for modeling "Freshness" and smoothly handing off decision-making power from a real-time signal to historical inertia.

## 2. Decaying Short-Term Memory: Exponential vs. Linear

In advanced continuous authentication architectures (like the Ensemble Model), **short-term memory (Freshness) should be decayed exponentially.**

This is considered the structural best practice for session weighting for the following key reasons:

### 2.1 The Danger of "Slow" Linear Decay
If linear decay is utilized for a standard 30-minute enterprise session, at minute 15, the "freshness" weight produced by the original authentication handshake still retains 50% of its authority. 
In modern, volatile network environments, a session endpoint can be hijacked, or a device computationally compromised, in a matter of seconds. Relying heavily on an authentication signal that is 15 minutes old creates a significant security vulnerability (a prolonged "Implicit Trust Period").

### 2.2 The "Handshake" Handoff
Exponential decay allows the system to prioritize absolute freshness exclusively during the critical first few minutes (the "Handshake" or "Boot-up" phase of the connection). By minute 5, an exponential decay curve drastically de-prioritizes the value of that initial connection state, essentially treating the original login as "stale."

### 2.3 Forcing the Transition to Inertia
By rapidly killing the mathematical weight of the "Fresh Signal" via exponential decay, the formula forces the fusion engine to shift its reliance onto **Historical Inertia** ($T_{prev}$). 

The computational logic becomes: *"That initial handshake is no longer fresh. The engine will no longer trust the spatial data the device provided 10 minutes ago; instead, the engine will heavily trust the consistent behavioral history the user has built up over the last 10 minutes."*

## 3. Conclusion
**Linear decay** turns trust into a simple, naive ticking timer. 
**Exponential decay**, conversely, treats trust like a highly volatile element that must be instantly verified and then immediately handed off to behavioral momentum. This creates a far more secure, lifecycle-driven shift from the "Fresh Session" state into the "Mature Session" state.
