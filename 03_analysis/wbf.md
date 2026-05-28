# Discussion on Weighted Belief Fusion (WBF)

Weighted Belief Fusion (WBF) is a critical mathematical framework used to synthesize conflicting, multi-domain telemetry into a singular, actionable decision. It is particularly indispensable in environments like Zero Trust Architectures (ZTA), where naïve approaches (such as purely additive or averaging models) fail in the presence of adversarial manipulation, sensor instability, or asymmetric domain reliability.

WBF resolves these vulnerabilities by integrating two foundational pillars:
1.  **Dynamic Variance-Based Contextual Weighting**: A statistical mechanism that treats signal stability as a proxy for evidential reliability.
2.  **Dempster-Shafer (DS) Theory of Evidence**: A formal framework for combining independent uncertain evidence sources with an explicit representation of ignorance.

Unlike Bayesian inference, which requires exhaustive prior probabilities, Dempster-Shafer theory explicitly mathematically models "I don't know" (total ignorance). This is crucial when sensor readings may be absent, corrupted, or deliberately spoofed.

---

## 1. Theoretical Foundations: Dempster-Shafer Evidence Theory

### 1.1 The Frame of Discernment
Dempster-Shafer theory operates over a Frame of Discernment ($\Theta$)—an exhaustive, mutually exclusive set of possible states. For binary trust evaluation, this is:
$$ \Theta = \{\text{Safe},\ \text{Unsafe}\} $$

The power set $2^\Theta$ contains all possible subsets representing the space over which evidential mass is distributed:
$$ 2^\Theta = \left\{ \emptyset,\ \{\text{Safe}\},\ \{\text{Unsafe}\},\ \{\text{Safe, Unsafe}\} \right\} $$

### 1.2 The Basic Probability Assignment (BPA)
A mass function (or BPA), denoted $m: 2^\Theta \rightarrow [0, 1]$, distributes evidential support across these subsets such that $\sum_{A \subseteq \Theta} m(A) = 1$ and $m(\emptyset) = 0$.

In this context, every evidence source produces three mass values:
*   $m(\{\text{Safe}\})$: Direct belief that the entity is trustworthy.
*   $m(\{\text{Unsafe}\})$: Direct belief that the entity is compromised.
*   $m(\{\text{Safe, Unsafe}\})$ or $m(\Theta)$: Uncertainty (epistemic ignorance).

### 1.3 Belief and Plausibility
From the mass function, two bounding measures define the true probability interval:
*   **Belief** ($Bel$): The minimum guaranteed support ($Bel(\{\text{Safe}\}) = m(\{\text{Safe}\})$).
*   **Plausibility** ($Pl$): The maximum possible support ($Pl(\{\text{Safe}\}) = m(\{\text{Safe}\}) + m(\Theta)$).
The width of the interval $[Bel, Pl]$ represents the degree of residual uncertainty.

---

## 2. Dynamic Variance-Based Contextual Weighting

To account for heterogeneous sensor reliability (e.g., a stable corporate device vs. a volatile compromised endpoint), WBF uses variance as a proxy for reliability. 

The statistical variance ($\sigma_k^2$) of a domain's trust score $S_k$ is computed over a sliding historical window of $N$ observations:
$$ \sigma_k^2 = \frac{1}{N} \sum_{j=1}^{N} \left(S_{k,j} - \bar{S}_k \right)^2 $$

Domains with stable readings are rewarded; those with chaotic signals are penalized using an inverse-variance weighting function:
$$ W_{\text{raw}, k} = \frac{1}{1 + \alpha \cdot \sigma_k^2} $$
where $\alpha$ governs the aggressiveness of the variance penalty (e.g., $\alpha = 5$ for a balanced logistic-style decay).

These raw weights are then normalized across the $K$ active domains to ensure they sum to 1.0, redistributing the proportional share of penalized domains to stable ones:
$$ W_{\text{final}, k} = \frac{W_{\text{raw}, k}}{\sum_{j=1}^{K} W_{\text{raw}, j}} $$

---

## 3. Evidence Construction via Discounting

The normalized weight $W_{\text{final}, k}$ acts as a *discounting factor*. A domain's trust score $S_k$ dictates the proportion of evidence supporting Safety vs. Danger, and the weight $W_{\text{final}, k}$ dictates how much of that evidence is confidently committed versus assigned to uncertainty:

$$ m_k(\{\text{Safe}\}) = S_k \cdot W_{\text{final}, k} $$
$$ m_k(\{\text{Unsafe}\}) = (1 - S_k) \cdot W_{\text{final}, k} $$
$$ m_k(\Theta) = 1 - W_{\text{final}, k} $$

**Boundary Behaviours:**
*   **Perfect Reliability** ($W = 1.0$): Zero residual uncertainty; the mass function precisely equals the domain score.
*   **Complete Unreliability** ($W = 0$): Generates *pure vacuous evidence* ($m(\Theta) = 1.0$). The sensor is mathematically neutralized; it does not explicitly claim "danger," but rather an absence of knowledge, preventing it from sabotaging the consensus.

---

## 4. Fusion and Decision-Making

### 4.1 Inter-Domain Spatial Fusion (Dempster's Rule)
Independent mass functions from active domains are fused using Dempster's Rule of Combination. For two domains $m_1$ and $m_2$, and any subset $A$:
$$ m_{1,2}(A) = \frac{1}{1 - \kappa} \sum_{B \cap C = A} m_1(B) \cdot m_2(C) $$
where $\kappa$ is the degree of conflict between the sources:
$$ \kappa = \sum_{B \cap C = \emptyset} m_1(B) \cdot m_2(C) $$

Spatial Fusion combines all domains iteratively at time step $t$:
$$ m_{\text{spatial}}^{(t)} = m_1^{(t)} \oplus m_2^{(t)} \oplus \cdots \oplus m_K^{(t)} $$

### 4.2 Temporal Fusion
WBF cumulatively combines successive spatial mass functions across time steps to dynamically track trust state changes:
$$ m_{\text{cum}}^{(t)} = m_{\text{cum}}^{(t-1)} \oplus m_{\text{spatial}}^{(t)} $$

### 4.3 Pignistic Probability (Trust Score Transformation)
Access controls require a point-estimate probability rather than interval bounds. The Pignistic Probability transformation distributes the mass of uncertain focal elements equally across their singleton components. The final **Trust Score** is:
$$ BetP(\text{Safe}) = m_{\text{cum}}(\{\text{Safe}\}) + \frac{m_{\text{cum}}(\Theta)}{2} $$

This score directly maps to nuanced access decisions:
*   $\mathbf{> 0.75}$: Full Access
*   $\mathbf{0.45 \text{ to } 0.75}$: Limited Access (Granular Quarantine)
*   $\mathbf{< 0.45}$: No Access

## Conclusion

By grounding access decisions in Dempster-Shafer theory, Weighted Belief Fusion achieves **epistemic humility** (representing missing data as ignorance, not danger) and **dynamic contextualization** (ignoring erratic sensors). It mathematically isolates uncertainty from truth, allowing adaptive decision-making resilient against spoofing and asymmetrical sensor dropouts.
