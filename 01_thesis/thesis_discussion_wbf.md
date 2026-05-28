# Weighted Belief Fusion: A Thesis-Level Discussion

## 1. Introduction

The enforcement of Zero Trust Architecture (ZTA) in heterogeneous enterprise networks demands a mathematically rigorous mechanism for synthesizing conflicting, multi-domain telemetry into a singular, actionable access decision. Naïve approaches—whether purely additive (cumulative) or normalizing (averaging)—fail catastrophically in the presence of adversarial manipulation, sensor instability, or asymmetric domain reliability (Jøsang, 2016; Chen et al., 2024). **Weighted Belief Fusion (WBF)** resolves these structural vulnerabilities by integrating two foundational pillars:

1.  **Dynamic Variance-Based Contextual Weighting**: A statistical mechanism that treats signal stability as a proxy for evidential reliability.
2.  **Dempster-Shafer (DS) Theory of Evidence**: A formal mathematical framework for combining independent, uncertain evidence sources with an explicit representation of ignorance.

Unlike Bayesian inference, which mandates exhaustive prior probability distributions across every hypothesis, Dempster-Shafer theory permits the explicit assignment of mass to *sets* of hypotheses—including the complete frame of discernment ($\Theta$), which represents total ignorance. This capacity to explicitly mathematically model "I don't know" is indispensable in operational Zero Trust environments where sensor readings may be absent, corrupted, or deliberately spoofed (Shafer, 1976; Smets & Kennes, 1994). In a Bayesian framework, if a device sensor ceases to report, the system must either use a prior (potentially stale) or crash; in DS theory, the missing sensor simply contributes a vacuous mass function ($m(\Theta) = 1.0$), asserting ignorance without distorting the consensus.

This discussion formalizes the complete WBF pipeline: from raw telemetry ingestion and variance-based evidence discounting, through mass function construction and inter-domain fusion via Dempster's Rule of Combination, to the final access decision derived via Pignistic Probability transformation.

---

## 2. Theoretical Foundations: Dempster-Shafer Evidence Theory

### 2.1 The Frame of Discernment

Dempster-Shafer theory operates over a **Frame of Discernment** ($\Theta$)—a finite, exhaustive, and mutually exclusive set of possible states. For the trust evaluation engine, the binary frame is defined as:

$$
\Theta = \{\text{Safe},\ \text{Unsafe}\}
$$

This binary frame captures the fundamental question the Policy Decision Point (PDP) must answer at every evaluation epoch: *Is this entity trustworthy enough to access the requested resource, or is it compromised?* The frame is deliberately binary rather than multi-state because access control decisions are ultimately binary (grant or deny); the nuance of "how much access" is handled by the decision thresholds applied to the final Trust Score (Section 6.3), not by expanding $\Theta$.

The **power set** $2^\Theta$ contains all possible subsets of $\Theta$, representing the space over which evidential mass is distributed:

$$
2^\Theta = \left\{ \emptyset,\ \{\text{Safe}\},\ \{\text{Unsafe}\},\ \{\text{Safe, Unsafe}\} \right\}
$$

Under the **Closed World Assumption** (CWA) established by Shafer (1976), mass assigned to the empty set $\emptyset$ is zero ($m(\emptyset) = 0$). The CWA asserts that the true state of the world *must* lie within $\Theta$—the entity is either Safe or Unsafe; there is no third possibility. This is a reasonable constraint for access control: a session is either authorized or it is not. The practical consequence of the CWA is that all evidential mass must be distributed across the three non-empty focal elements: $\{\text{Safe}\}$, $\{\text{Unsafe}\}$, and $\{\text{Safe, Unsafe}\}$, which represents complete ignorance about which of the two states is true.

### 2.2 The Basic Probability Assignment (BPA)

A **Basic Probability Assignment** (also termed a *mass function*), denoted $m: 2^\Theta \rightarrow [0, 1]$, distributes evidential support across the subsets of $\Theta$ subject to two axioms:

$$
m(\emptyset) = 0
$$

$$
\sum_{A \subseteq \Theta} m(A) = 1
$$

The first axiom enforces the Closed World Assumption. The second axiom ensures that all available evidence—whether committed to a specific hypothesis or distributed as uncertainty—is fully accounted for. Together, these axioms guarantee that the mass function constitutes a valid probability distribution over the power set, not over $\Theta$ itself.

For the binary trust frame, every evidence source produces exactly three mass values:

| Mass Component | Notation | Interpretation |
|:---|:---|:---|
| $m(\{\text{Safe}\})$ | Belief in Safety | Direct evidential support that the entity is trustworthy |
| $m(\{\text{Unsafe}\})$ | Belief in Danger | Direct evidential support that the entity is compromised |
| $m(\{\text{Safe, Unsafe}\})$ | Uncertainty ($m(\Theta)$) | Absence of decisive evidence; represents epistemic ignorance |

Any subset of $\Theta$ to which a non-zero mass is assigned is called a **focal element**. In the binary trust frame, there are at most three focal elements. The critical distinction from classical probability is that mass can be assigned to the *composite* set $\{\text{Safe, Unsafe}\}$, representing evidence that exists but is insufficient to distinguish between the two states. This is fundamentally different from a probability of $0.50$ for Safe, which would falsely imply a balanced belief; $m(\Theta) = 1.0$ instead means "I have *zero* information."

> [!IMPORTANT]
> The explicit representation of **Uncertainty** ($m(\Theta)$) is the decisive advantage of DS theory over Bayesian models in Zero Trust contexts. An absent sensor reading does not default to "Safe" or "Unsafe"—it defaults to "Unknown," preventing both false positives (granting access to compromised entities) and false negatives (denying access to legitimate users) from incomplete data.

### 2.3 Belief, Disbelief, and Plausibility

From a mass function, two bounding measures are derived that bracket the true probability of any hypothesis.

**Belief** ($Bel$) quantifies the minimum guaranteed support for a hypothesis $A$. It is computed as the sum of masses of all subsets entirely contained within $A$:

$$
Bel(A) = \sum_{B \subseteq A} m(B)
$$

In plain terms, $Bel(A)$ answers: *"What is the total evidence that commits exclusively to $A$ and nothing else?"* For the singleton $\{\text{Safe}\}$, the only subset of $\{\text{Safe}\}$ is itself, so $Bel(\{\text{Safe}\}) = m(\{\text{Safe}\})$. This is the *floor* of our confidence—the portion of evidence that unambiguously supports Safety.

**Plausibility** ($Pl$) quantifies the maximum possible support for $A$—the sum of masses of all subsets that are *compatible* with $A$ (i.e., do not contradict it):

$$
Pl(A) = \sum_{B \cap A \neq \emptyset} m(B) = 1 - Bel(\bar{A})
$$

$Pl(A)$ answers: *"If all the uncertain evidence were to ultimately resolve in favor of $A$, how much total support would $A$ have?"* For $\{\text{Safe}\}$:

$$
Pl(\{\text{Safe}\}) = m(\{\text{Safe}\}) + m(\{\text{Safe, Unsafe}\})
$$

This is the *ceiling* of our confidence—the maximum belief in Safety if all ignorance were resolved favorably.

The interval $[Bel(A),\ Pl(A)]$ brackets the true probability of $A$:

$$
Bel(\{\text{Safe}\}) = m(\{\text{Safe}\})
$$

$$
Pl(\{\text{Safe}\}) = m(\{\text{Safe}\}) + m(\Theta)
$$

The **width** of this interval, $Pl(A) - Bel(A) = m(\Theta)$, directly quantifies the degree of residual uncertainty. A narrow interval indicates strong, committed evidence; a wide interval signals that the system is operating with significant epistemic ignorance. In operational terms, a trust evaluation with $Bel(\text{Safe}) = 0.30$ and $Pl(\text{Safe}) = 0.85$ tells the PDP: *"I'm at least 30% confident the entity is safe, but it could be as high as 85%—the 55% gap represents evidence I simply don't have."* This interval representation is far richer than any single-point probability estimate.

---

## 3. Dynamic Variance-Based Contextual Weighting

### 3.1 The Problem: Heterogeneous Sensor Reliability

In a multi-domain Zero Trust architecture, telemetry is ingested from four independent domain sensors: **Identity** ($i$), **Device** ($d$), **Network** ($n$), and **Application/Data** ($a$). Each domain generates a **Domain Trust Score** $S_k \in [0, 1]$ from its constituent parameters. However, not all domain scores carry equal evidential merit at every instant. A device sensor on a managed corporate endpoint transmits highly stable, reliable readings; the same class of sensor on a BYOD device under active attack generates erratic, high-variance signals. Treating these signals with equal authority—as cumulative and averaging models do—fundamentally violates the principle of proportional evidential weighting (Mui et al., 2002).

The challenge is two-dimensional: the system must evaluate both the *content* of the signal (what it reports) and the *quality* of the signal (how reliably it reports it). A domain score of $S = 0.90$ from a sensor that has consistently reported $S \approx 0.90$ over the past 10 evaluation cycles carries far greater evidential weight than the same score from a sensor that previously oscillated between $0.30$ and $0.95$. The latter may be reporting $0.90$ by coincidence, or worse, because an attacker has temporarily stabilized a compromised feed to evade detection.

### 3.2 Variance as a Reliability Proxy

The WBF engine operationalizes the principle that **stability is a proxy for reliability** by computing the statistical variance ($\sigma_k^2$) of each domain's trust score over a sliding historical window of $N$ observations:

$$
\sigma_k^2 = \frac{1}{N} \sum_{j=1}^{N} \left(S_{k,j} - \bar{S}_k \right)^2
$$

where $\bar{S}_k = \frac{1}{N} \sum_{j=1}^{N} S_{k,j}$ is the arithmetic mean of the domain score over the observation window.

**What this equation computes:** The variance measures the average squared deviation of each individual score from the domain's mean score. If a domain consistently reports $S = 0.90$, then each $(S_{k,j} - \bar{S}_k)^2 \approx 0$ and $\sigma_k^2 \approx 0$. If the domain oscillates wildly—say between $0.30$ and $0.95$—then the deviations are large and $\sigma_k^2$ rises sharply. The key insight is that variance captures the *second-order behavior* of the signal: not what it says, but how consistently it says it.

A domain exhibiting stable, consistent readings ($\sigma_k^2 \approx 0$) is rewarded with a high weight; a domain producing chaotic, oscillating signals ($\sigma_k^2 \gg 0$) is penalized. This is encoded via an **inverse-variance weighting function**:

$$
\boxed{W_{\text{raw}, k} = \frac{1}{1 + \alpha \cdot \sigma_k^2}}
$$

**What this equation does:** This is a **logistic-style decay function** that maps variance to a weight between 0 and 1. When variance is zero ($\sigma_k^2 = 0$), the denominator is $1 + 0 = 1$, so $W_{\text{raw}} = 1.0$—the domain receives full evidential authority. As variance increases, the denominator grows, driving $W_{\text{raw}}$ toward zero. The function is bounded: it can never go below zero (a domain can never have "negative" influence) or above one (a domain can never have more than full influence). The decay is smooth and monotonic, meaning that gradual increases in instability produce gradual, proportional reductions in trust weight—there are no abrupt thresholds or discontinuities.

The term $\alpha \cdot \sigma_k^2$ in the denominator represents the *penalized variance*: the raw variance scaled by the sensitivity parameter. This product determines how quickly the weight decays. Mathematically, the half-weight point (where $W_{\text{raw}} = 0.5$) occurs when $\alpha \cdot \sigma_k^2 = 1$, i.e., $\sigma_k^2 = 1/\alpha$.

### 3.3 The Sensitivity Parameter ($\alpha$)

The parameter $\alpha > 0$ functions as the **variance penalty amplifier**. It governs exactly how aggressively the system penalizes signal instability within a specific domain. A higher $\alpha$ means the system is more suspicious of variance; a lower $\alpha$ means it is more tolerant.

| Configuration | Behavior | Half-Weight Variance ($\sigma^2 = 1/\alpha$) | Use Case |
|:---|:---|:---|:---|
| $\alpha = 1$ (Low) | Tolerant; absorbs moderate jitter | $\sigma^2 = 1.0$ | Standard corporate environments with ambient sensor noise |
| $\alpha = 5$ (Balanced) | Logistic-style decay; penalizes sustained oscillation while absorbing negligible micro-jitter | $\sigma^2 = 0.2$ | Enterprise ZTA default (recommended by Jøsang, 2016) |
| $\alpha \geq 10$ (High) | Aggressive; even minor variance collapses the weight toward zero | $\sigma^2 \leq 0.1$ | Critical infrastructure, NIST AAL3 environments, financial systems |

The "half-weight variance" column illustrates a useful interpretation: with $\alpha = 5$, a domain must exhibit a variance of $0.2$ before its evidential weight is halved. For $\alpha = 10$, only $\sigma^2 = 0.1$ is needed to halve the weight—a significantly more paranoid configuration.

The functional dynamics are illustrated by evaluating $W_{\text{raw}}$ at varying variance levels with $\alpha = 5$:

| $\sigma^2$ | $\alpha \cdot \sigma^2$ | $W_{\text{raw}}$ | Interpretation |
|:---|:---|:---|:---|
| $0.00$ | $0.00$ | $1.000$ | Perfect stability → Full evidential weight; all evidence is committed |
| $0.02$ | $0.10$ | $0.909$ | Minimal jitter → Negligible penalty; normal operational noise is absorbed |
| $0.10$ | $0.50$ | $0.667$ | Moderate instability → One-third of evidence shifted to uncertainty |
| $0.20$ | $1.00$ | $0.500$ | Half-weight point → Half the evidence is uncertain |
| $0.25$ | $1.25$ | $0.444$ | High volatility → Majority of evidence discounted to ignorance |
| $0.50$ | $2.50$ | $0.286$ | Severe instability → Evidence largely ignored; domain is nearly vacuous |

> [!NOTE]
> The choice of $\alpha$ should be empirically calibrated against the operational risk appetite and the baseline noise of the deployment environment. Jøsang (2016) emphasizes that evidence discounting factors must be tied to the expected environmental noise floor. An $\alpha$ too low in a high-security enclave permits unstable signals to retain disproportionate influence; an $\alpha$ too high in a noisy but benign environment (e.g., cellular IoT devices) would discard legitimate evidence as unreliable.

### 3.4 Weight Normalization

The raw weights $W_{\text{raw}, k}$ are computed independently for each domain and do not necessarily sum to any specific value. To ensure the contextual weights form a proper influence distribution across the $K$ active domains—such that the total evidential "budget" is fully allocated—the raw weights are normalized:

$$
\boxed{W_{\text{final}, k} = \frac{W_{\text{raw}, k}}{\sum_{j=1}^{K} W_{\text{raw}, j}}}
$$

This normalization guarantees:

$$
\sum_{k=1}^{K} W_{\text{final}, k} = 1.0
$$

**What this equation achieves:** Normalization converts absolute weights into *relative proportions* of evidential influence. The normalization has two critical operational implications:

1. **Redistribution of Influence**: If one domain's raw weight collapses due to high variance (e.g., the Network domain during a public Wi-Fi connection), its proportional share is **redistributed** to the remaining stable domains. The total evidential influence within the fusion engine is preserved at 100%; the system does not progressively lose overall confidence merely because one sensor exhibits noise. Instead, the stable domains—Device, Identity, Application—absorb the freed influence and drive the decision.

2. **Relative, Not Absolute, Authority**: Normalization ensures that a domain's influence depends not only on its own stability but also on the stability of its peers. If *all* domains are moderately volatile, they may each retain similar normalized weights despite individually low raw weights. If only *one* domain is volatile while the rest are stable, the volatile domain's normalized weight is dramatically suppressed because the denominator is dominated by the stable domains' high raw weights.

---

## 4. Evidence Construction: Mass Function via Discounting

### 4.1 The Discounting Mechanism

Having computed the normalized contextual weight $W_k \in [0, 1]$ for each domain $k$, the engine constructs a **Dempster-Shafer Mass Function** by using the weight as a *discounting factor*. Conceptually, two distinct pieces of information are synthesized into a single mass function:

- The domain's **trust score** $S_k$ dictates the *proportion* of available evidence supporting Safety versus Danger. A score of $S_k = 0.80$ means that 80% of the domain's observable indicators suggest the entity is safe and 20% suggest it is compromised.
- The domain's **contextual weight** $W_k$ dictates *how much* of this evidence is confidently committed versus assigned to uncertainty. A weight of $W_k = 0.60$ means that only 60% of the evidence is actually "spent" on the Safe/Unsafe hypotheses; the remaining 40% is withheld as epistemic ignorance.

This decomposition yields the three mass components:

$$
\boxed{m_k(\{\text{Safe}\}) = S_k \cdot W_k}
$$

$$
\boxed{m_k(\{\text{Unsafe}\}) = (1 - S_k) \cdot W_k}
$$

$$
\boxed{m_k(\{\text{Safe, Unsafe}\}) = 1 - W_k}
$$

**Interpretation in plain terms:** The weight $W_k$ acts as a gate. It determines how much of the domain's opinion is allowed to pass through into the fusion engine as committed evidence. The portion that passes through is split between Safe and Unsafe according to the domain score $S_k$. The portion that does *not* pass through (because the domain's historical behavior is too erratic to trust) is converted into uncertainty—a mathematical acknowledgment that the system cannot confidently rely on this domain's testimony.

This mechanism is closely related to Shafer's (1976) original concept of **evidence discounting**, where the reliability of a source modulates the degree to which its testimony is accepted. In Shafer's formalization, discounting at rate $r$ transforms $m(A) \rightarrow (1-r) \cdot m(A)$ for singletons, with the residual mass moved to $\Theta$. The WBF discounting is equivalent, with the discount rate $r = 1 - W_k$.

### 4.2 Mathematical Verification

These three mass components satisfy the BPA axioms by construction. We verify that they sum to unity:

$$
m_k(\{\text{Safe}\}) + m_k(\{\text{Unsafe}\}) + m_k(\Theta) = S_k W_k + (1 - S_k) W_k + (1 - W_k)
$$

Factoring the first two terms:

$$
= W_k \left[ S_k + (1 - S_k) \right] + (1 - W_k) = W_k \cdot 1 + (1 - W_k) = 1.0 \quad \checkmark
$$

Additionally, since $S_k \in [0, 1]$ and $W_k \in [0, 1]$, all three mass values are non-negative, satisfying $m(A) \geq 0$ for all $A$. The empty set mass is $m(\emptyset) = 0$ by the Closed World Assumption. Therefore, the construction produces a valid BPA for all possible input combinations.

### 4.3 Interpretation of Limiting Cases

The discounting mechanism produces intuitive behavior at boundary conditions, which validates the mathematical design:

**Case 1: Perfect Reliability ($W_k = 1.0$, $\sigma_k^2 = 0$)**

$$
m(\{\text{Safe}\}) = S_k, \quad m(\{\text{Unsafe}\}) = 1 - S_k, \quad m(\Theta) = 0
$$

The domain's evidence is fully committed—zero residual uncertainty. The mass function directly mirrors the domain score. This represents a sensor with a perfectly stable historical track record: the engine has complete confidence in the veracity of the reported signal. In operational terms, this corresponds to a managed corporate device on a stable, wired network with no historical anomalies. The system trusts the signal completely and assigns all evidential mass to the specific hypotheses.

**Case 2: Complete Unreliability ($W_k = 0$, $\sigma_k^2 \rightarrow \infty$)**

$$
m(\{\text{Safe}\}) = 0, \quad m(\{\text{Unsafe}\}) = 0, \quad m(\Theta) = 1.0
$$

The domain contributes **pure vacuous evidence** (total ignorance). Crucially, this does not assert danger; it asserts the *absence of knowledge*. The domain has effectively been mathematically neutralized—it provides no information whatsoever. Under the Pignistic transformation (Section 6), vacuous evidence distributes equally as $BetP(\text{Safe}) = BetP(\text{Unsafe}) = 0.5$—a neutral, non-committal baseline.

> [!NOTE]
> This behavior is the linchpin of WBF's superiority over static models. An erratic sensor producing $W_k \approx 0$ does not block access (which would cause false denials) nor does it grant access (which would cause false positives); it simply **removes itself from the evidential consensus**, preventing it from sabotaging the decision in either direction. The remaining stable domains drive the outcome. This is fundamentally different from a zero-score in a cumulative model, which would actively pull the aggregate downward.

**Case 3: High Score, Low Weight ($S_k = 0.95$, $W_k = 0.15$)**

$$
m(\{\text{Safe}\}) = 0.1425, \quad m(\{\text{Unsafe}\}) = 0.0075, \quad m(\Theta) = 0.85
$$

Despite the domain reporting high safety ($S_k = 0.95$), the engine is deeply uncertain about this claim due to the domain's historical instability. Only 15% of the evidence is committed to specific hypotheses; 85% remains as ignorance. This case is particularly important for spoofing resistance: an attacker who compromises a sensor and forces it to broadcast artificially high scores will simultaneously introduce variance into the historical signal (the sudden jump from normal readings to artificially high readings). The variance triggers weight suppression, which converts the spoofed testimony into mostly ignorance—preventing the attack from dominating the fusion output.

**Case 4: Low Score, High Weight ($S_k = 0.10$, $W_k = 0.90$)**

$$
m(\{\text{Safe}\}) = 0.09, \quad m(\{\text{Unsafe}\}) = 0.81, \quad m(\Theta) = 0.10
$$

A stable domain confidently reporting danger. The high weight means the system commits 90% of the evidence, and most of that evidence ($81\%$) supports the Unsafe hypothesis. This is the "reliable alarm" scenario: the sensor has a consistent track record and is now consistently reporting bad news. The system should—and does—take this very seriously. A single domain in this state can heavily influence the fused result toward denial.

---

## 5. Inter-Domain Fusion: Dempster's Rule of Combination

### 5.1 The Combination Rule

Given two independent mass functions $m_1$ and $m_2$ (from two separate domains), Dempster's Rule of Combination produces a fused mass function $m_{1,2}$. For any non-empty focal element $A \subseteq \Theta$:

$$
\boxed{m_{1,2}(A) = \frac{1}{1 - \kappa} \sum_{\substack{B \cap C = A \\ B, C \subseteq \Theta}} m_1(B) \cdot m_2(C)}
$$

where $\kappa$ is the **degree of conflict** between the two sources:

$$
\kappa = \sum_{\substack{B \cap C = \emptyset \\ B, C \subseteq \Theta}} m_1(B) \cdot m_2(C)
$$

**What this equation does, step by step:**

1. **Product computation**: Every pair of focal elements (one from $m_1$, one from $m_2$) is multiplied together. Because the sources are independent, the joint probability of both claims being simultaneously true is the product of their individual masses.

2. **Intersection classification**: Each product is classified by the intersection of the two focal elements. If the intersection is non-empty (the two claims are compatible), the product contributes to the combined mass on that intersection. If the intersection is empty (the two claims directly contradict each other—e.g., one says Safe, the other says Unsafe), the product contributes to the conflict mass $\kappa$.

3. **Conflict normalization**: The factor $\frac{1}{1-\kappa}$ redistributes the conflicting mass proportionally across the non-conflicting focal elements. This ensures the combined mass function still sums to 1.0. The normalization prevents the accumulation of paradoxical evidence: if two domains partially contradict each other, the contradiction is acknowledged but not allowed to paralyze the system.

4. **Conflict interpretation**: The value $\kappa \in [0, 1)$ quantifies how much the two sources disagree. A $\kappa$ near zero means the sources largely agree; a $\kappa$ approaching 1.0 means near-total contradiction. When $\kappa = 1.0$ exactly, the sources are in total conflict and cannot be combined—a pathological edge case that the engine handles by retaining the most recent evidence.

### 5.2 Application to the Binary Trust Frame

For the binary frame $\Theta = \{\text{Safe, Unsafe}\}$ with three focal elements per mass function, the combination produces nine product terms ($3 \times 3$). The following table exhaustively enumerates the intersections:

| $m_1$ Focal Element | $m_2$ Focal Element | Intersection | Contribution |
|:---|:---|:---|:---|
| $\{\text{Safe}\}$ | $\{\text{Safe}\}$ | $\{\text{Safe}\}$ | $m_1(S) \cdot m_2(S)$ — Both domains agree on Safety |
| $\{\text{Safe}\}$ | $\{\text{Unsafe}\}$ | $\emptyset$ | **Conflict**: $m_1(S) \cdot m_2(U)$ — Direct contradiction |
| $\{\text{Safe}\}$ | $\Theta$ | $\{\text{Safe}\}$ | $m_1(S) \cdot m_2(\Theta)$ — Domain 1 says Safe; Domain 2 is ignorant, so Safety survives |
| $\{\text{Unsafe}\}$ | $\{\text{Safe}\}$ | $\emptyset$ | **Conflict**: $m_1(U) \cdot m_2(S)$ — Direct contradiction |
| $\{\text{Unsafe}\}$ | $\{\text{Unsafe}\}$ | $\{\text{Unsafe}\}$ | $m_1(U) \cdot m_2(U)$ — Both domains agree on Danger |
| $\{\text{Unsafe}\}$ | $\Theta$ | $\{\text{Unsafe}\}$ | $m_1(U) \cdot m_2(\Theta)$ — Domain 1 says Unsafe; Domain 2 is ignorant, so Danger survives |
| $\Theta$ | $\{\text{Safe}\}$ | $\{\text{Safe}\}$ | $m_1(\Theta) \cdot m_2(S)$ — Domain 1 is ignorant; Domain 2 says Safe |
| $\Theta$ | $\{\text{Unsafe}\}$ | $\{\text{Unsafe}\}$ | $m_1(\Theta) \cdot m_2(U)$ — Domain 1 is ignorant; Domain 2 says Unsafe |
| $\Theta$ | $\Theta$ | $\Theta$ | $m_1(\Theta) \cdot m_2(\Theta)$ — Both domains are ignorant; ignorance persists |

Collecting terms by focal element, the unnormalized fused masses are:

$$
m'(\{\text{Safe}\}) = m_1(S) m_2(S) + m_1(S) m_2(\Theta) + m_1(\Theta) m_2(S)
$$

This expression shows that belief in Safety is strengthened by three mechanisms: (a) both domains agreeing on Safety, (b) one domain affirming Safety while the other is uncertain, and (c) the reverse of (b). Mechanism (a) provides the strongest reinforcement; mechanisms (b) and (c) provide partial reinforcement, modulated by the uncertain domain's ignorance.

$$
m'(\{\text{Unsafe}\}) = m_1(U) m_2(U) + m_1(U) m_2(\Theta) + m_1(\Theta) m_2(U)
$$

Symmetrically, belief in Danger is reinforced by the same three mechanisms operating on the Unsafe hypothesis.

$$
m'(\Theta) = m_1(\Theta) \cdot m_2(\Theta)
$$

**This is critical**: Residual uncertainty in the fused output is the *product* of the individual uncertainties. Because this is a product of two values less than 1.0, the fused uncertainty is always **smaller** than either individual uncertainty. This means that every informative evidence source (where $m(\Theta) < 1.0$) reduces the system's overall ignorance. Evidential combination is inherently a *knowledge-gaining* operation.

$$
\kappa = m_1(S) m_2(U) + m_1(U) m_2(S)
$$

The conflict arises exclusively from the cross-terms where one domain asserts Safety while the other asserts Danger. These are the pairings where the evidence is mutually exclusive and cannot simultaneously be true.

The normalized fused mass function is:

$$
m_{1,2}(A) = \frac{m'(A)}{1 - \kappa}, \quad \forall A \in \left\{\{\text{Safe}\},\ \{\text{Unsafe}\},\ \Theta\right\}
$$

### 5.3 Properties of Dempster's Rule

Several axiomatic properties make Dempster's Rule ideally suited for multi-domain trust fusion:

1.  **Commutativity**: $m_1 \oplus m_2 = m_2 \oplus m_1$. The order of evidence presentation does not affect the outcome. This is essential because domain telemetry may arrive asynchronously; the fusion result is identical regardless of which domain is processed first.

2.  **Associativity**: $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$. Evidence can be fused incrementally without loss of mathematical consistency. This permits the engine to process domains sequentially as they report, rather than requiring all domains to report simultaneously.

3.  **Uncertainty Reduction**: Successive combination with informative (non-vacuous) evidence monotonically reduces $m(\Theta)$, driving the system toward a committed decision. Each additional informative source narrows the $[Bel, Pl]$ interval.

4.  **Vacuous Element Identity**: Combining with a vacuous mass function ($m(\Theta) = 1.0$) produces the original mass function unchanged: $m \oplus m_{\text{vacuous}} = m$. This ensures that an unreliable domain (high variance → $W_k \approx 0$ → near-vacuous mass) does not distort the fusion output.

> [!TIP]
> Property 4 (Vacuous Identity) is operationally critical. It mathematically guarantees that a domain rendered vacuous by high variance **cannot harm** the fusion consensus. This is fundamentally different from a system that would assign a "zero score" to an unreliable domain—which would actively pull the aggregate downward—versus assigning "no opinion," which is neutral. An unreliable domain is *mathematically invisible* in the fusion.

### 5.4 The Spatial Fusion Pipeline

At each evaluation time step $t$, the engine performs **Spatial Fusion** by sequentially combining the mass functions from all $K$ active domains:

$$
m_{\text{spatial}}^{(t)} = m_1^{(t)} \oplus m_2^{(t)} \oplus \cdots \oplus m_K^{(t)}
$$

Due to associativity, this is equivalently computed iteratively:

```
m_fused ← m_1
for k = 2 to K:
    m_fused ← m_fused ⊕ m_k
```

This spatial fusion collapses the multi-domain evidence into a single composite mass function representing the system's aggregate assessment of the entity's trustworthiness at time $t$. The result captures the combined testimony of all domains, weighted by their individual reliability, with inter-domain conflicts explicitly resolved through Dempster's normalization.

---

## 6. Pignistic Probability: From Belief to Decision

### 6.1 The Decision Problem

Dempster-Shafer belief functions produce intervals $[Bel(A), Pl(A)]$ rather than point probabilities. While this interval representation is richer for reasoning under uncertainty, access control decisions require a **point estimate** to evaluate against policy thresholds—the system must ultimately output "Full Access," "Limited Access," or "No Access," not an interval. The Pignistic Probability transformation, introduced by Smets (1990) within the Transferable Belief Model (TBM), provides a principled mechanism for extracting a decision-making probability from a mass function.

The word "pignistic" derives from the Latin *pignus* (a bet), reflecting the idea that when forced to make a decision (place a bet), one should distribute uncertain evidence equally across the outcomes it supports.

### 6.2 The Pignistic Transformation

For each singleton hypothesis $x \in \Theta$, the Pignistic Probability $BetP(x)$ is computed by distributing the mass of each focal element equally among its constituent singletons:

$$
\boxed{BetP(x) = \sum_{\substack{A \subseteq \Theta \\ x \in A}} \frac{m(A)}{|A|}}
$$

**What this equation does:** For each focal element $A$ that contains the hypothesis $x$, the mass $m(A)$ is divided equally among the $|A|$ elements of $A$, and $x$'s share is summed. This implements the principle of **insufficient reason**: when evidence supports a set of hypotheses without distinguishing between them, each hypothesis in the set receives an equal share.

For the binary frame $\Theta = \{\text{Safe, Unsafe}\}$:

$$
BetP(\text{Safe}) = \frac{m(\{\text{Safe}\})}{|\{\text{Safe}\}|} + \frac{m(\{\text{Safe, Unsafe}\})}{|\{\text{Safe, Unsafe}\}|} = m(\{\text{Safe}\}) + \frac{m(\Theta)}{2}
$$

$$
BetP(\text{Unsafe}) = m(\{\text{Unsafe}\}) + \frac{m(\Theta)}{2}
$$

**In plain terms:** The Pignistic transformation takes all the committed mass on Safety, then adds half of the uncertain mass (since the uncertainty is between two equally plausible outcomes). This produces a single number that represents the system's "best bet" on the entity's safety.

By construction, $BetP(\text{Safe}) + BetP(\text{Unsafe}) = 1.0$, forming a proper probability distribution suitable for threshold-based decision-making.

### 6.3 Decision Thresholds

The WBF engine maps the Pignistic Probability $BetP(\text{Safe})$—designated as the **Trust Score**—to an access decision using a tiered policy structure:

$$
\text{Decision} = 
\begin{cases}
\textbf{Full Access} & \text{if } BetP(\text{Safe}) > 0.75 \\
\textbf{Limited Access} & \text{if } 0.45 \leq BetP(\text{Safe}) \leq 0.75 \\
\textbf{No Access} & \text{if } BetP(\text{Safe}) < 0.45
\end{cases}
$$

> [!NOTE]
> The "Limited Access" tier represents the system's capacity for **granular quarantine**—a capability absent from binary Allow/Deny models. When evidence is contradictory or uncertain, the engine neither blindly trusts nor catastrophically locks out; it proportionally restricts privileges, reflecting the true epistemic state of the evidence. This tier operationalizes the principle that access control is not binary—a user on an untrusted device may be permitted to read non-sensitive documents but denied access to production databases.

---

## 7. Temporal Fusion: Trust as a Time-Series

### 7.1 Cumulative Temporal Combination

Beyond spatial fusion at a single time step, WBF supports **Temporal Fusion** by cumulatively combining successive spatial mass functions across time steps. The cumulative belief state at time $t$ is:

$$
m_{\text{cum}}^{(t)} = m_{\text{cum}}^{(t-1)} \oplus m_{\text{spatial}}^{(t)}
$$

with the initial state set to a vacuous prior:

$$
m_{\text{cum}}^{(0)} = m_{\text{vacuous}} \quad \text{where} \quad m_{\text{vacuous}}(\Theta) = 1.0
$$

**What this equation does:** The system begins with total ignorance ($m(\Theta) = 1.0$) at session inception—no preconceived trust or distrust. At each time step, the new spatial evidence is combined with the cumulative historical evidence using Dempster's Rule. Because the Vacuous Identity property holds (Property 4 of Section 5.3), the first spatial fusion simply replaces the vacuous prior: $m_{\text{vacuous}} \oplus m_{\text{spatial}}^{(1)} = m_{\text{spatial}}^{(1)}$.

This cumulative combination progressively reduces uncertainty as consistent evidence accumulates. By the uncertainty reduction property, $m_{\text{cum}}^{(t)}(\Theta) \leq m_{\text{cum}}^{(t-1)}(\Theta)$ whenever informative evidence is added, meaning the system's confidence monotonically increases with consistent inputs. Conversely, contradictory evidence across time steps increases the conflict term $\kappa$, slowing convergence and maintaining higher residual uncertainty.

### 7.2 Behavioral Inertia

The cumulative temporal fusion creates what is operationally termed **Behavioral Inertia**—a historical mathematical memory of the entity's operational cadence. After $t$ time steps of consistent behavior, the accumulated mass $m_{\text{cum}}^{(t)}(\{\text{Safe}\})$ is significant, and the residual uncertainty $m_{\text{cum}}^{(t)}(\Theta)$ is minimal. A single anomalous reading at time $t+1$ introduces a small amount of conflicting evidence, but the established cumulative mass absorbs this perturbation. The Trust Score may dip slightly but does not crash.

This behavior is desirable for operational continuity: a brief network jitter during a trusted employee's session should not trigger immediate lockout. However, *sustained* anomalous behavior (multiple consecutive anomalous readings) progressively erodes the cumulative mass, eventually degrading the Trust Score below the access thresholds. This creates a natural tension between stability (inertia resists noise) and responsiveness (inertia eventually yields to persistent threats).

### 7.3 Convergence Dynamics

The system exhibits a characteristic **Convergence Interval** determined by the sliding window size $N$ of the variance computation. During the initialization phase ($t < N$):

- Variance estimates are statistically immature ($\sigma_k^2 \approx 0$ from insufficient samples)
- Weights default to near-uniform ($W_k \approx 1/K$)
- The trust score reflects a "naïve" assessment without contextual discounting

After convergence ($t \geq N$), variance stabilizes, weights lock into their contextual steady-state values, and the Trust Score reflects the *true* weighted evidential consensus.

$$
\lim_{t \to N} \text{Trust}(S) \neq \text{Trust}(S_{t=0})
$$

This confirms that trust is not a snapshot but an integral over time. Steps $0$ through $N-1$ represent the calculation of this integral—the system's journey from ignorance to informed judgment.

---

## 8. Worked Numerical Example

To concretize the abstract mathematics, this section traces a complete evaluation cycle through the WBF pipeline for a two-domain scenario (Device and Network) under a "Public Wi-Fi" context.

**Given:**
- Device domain: $S_d = 0.90$ (strong endpoint health), $\sigma_d^2 = 0.01$ (stable)
- Network domain: $S_n = 0.35$ (weak transport security), $\sigma_n^2 = 0.20$ (volatile)
- Sensitivity: $\alpha = 5$

### Stage 1–2: Scores and Variance
The scores and variances are given directly above.

### Stage 3: Dynamic Weight Calculation

$$
W_{\text{raw}, d} = \frac{1}{1 + 5 \times 0.01} = \frac{1}{1.05} = 0.952
$$

$$
W_{\text{raw}, n} = \frac{1}{1 + 5 \times 0.20} = \frac{1}{2.0} = 0.500
$$

Normalized:

$$
W_{\text{final}, d} = \frac{0.952}{0.952 + 0.500} = \frac{0.952}{1.452} = 0.656
$$

$$
W_{\text{final}, n} = \frac{0.500}{1.452} = 0.344
$$

**Interpretation:** The Device domain, being highly stable, receives roughly twice the evidential influence (65.6%) as the volatile Network domain (34.4%). The volatile Network is not silenced—it still has a voice—but its influence is proportionally reduced.

### Stage 4: Evidence Construction

**Device mass function:**
$$
m_d(\{\text{Safe}\}) = 0.90 \times 0.656 = 0.590
$$
$$
m_d(\{\text{Unsafe}\}) = 0.10 \times 0.656 = 0.066
$$
$$
m_d(\Theta) = 1 - 0.656 = 0.344
$$

**Network mass function:**
$$
m_n(\{\text{Safe}\}) = 0.35 \times 0.344 = 0.120
$$
$$
m_n(\{\text{Unsafe}\}) = 0.65 \times 0.344 = 0.224
$$
$$
m_n(\Theta) = 1 - 0.344 = 0.656
$$

**Interpretation:** The Device commits 65.6% of its evidence, heavily biased toward Safe. The Network commits only 34.4%, slightly biased toward Unsafe. The Network retains 65.6% as uncertainty—the system acknowledges it cannot rely on this signal.

### Stage 5: Spatial Fusion (Dempster's Rule)

Computing the nine products:

| Term | Product | Value |
|:---|:---|:---|
| $m_d(S) \cdot m_n(S) \rightarrow \{\text{Safe}\}$ | $0.590 \times 0.120$ | $0.0708$ |
| $m_d(S) \cdot m_n(U) \rightarrow \emptyset$ | $0.590 \times 0.224$ | $0.1322$ (**conflict**) |
| $m_d(S) \cdot m_n(\Theta) \rightarrow \{\text{Safe}\}$ | $0.590 \times 0.656$ | $0.3870$ |
| $m_d(U) \cdot m_n(S) \rightarrow \emptyset$ | $0.066 \times 0.120$ | $0.0079$ (**conflict**) |
| $m_d(U) \cdot m_n(U) \rightarrow \{\text{Unsafe}\}$ | $0.066 \times 0.224$ | $0.0148$ |
| $m_d(U) \cdot m_n(\Theta) \rightarrow \{\text{Unsafe}\}$ | $0.066 \times 0.656$ | $0.0433$ |
| $m_d(\Theta) \cdot m_n(S) \rightarrow \{\text{Safe}\}$ | $0.344 \times 0.120$ | $0.0413$ |
| $m_d(\Theta) \cdot m_n(U) \rightarrow \{\text{Unsafe}\}$ | $0.344 \times 0.224$ | $0.0771$ |
| $m_d(\Theta) \cdot m_n(\Theta) \rightarrow \Theta$ | $0.344 \times 0.656$ | $0.2257$ |

Collecting terms:

$$
m'(\{\text{Safe}\}) = 0.0708 + 0.3870 + 0.0413 = 0.4991
$$
$$
m'(\{\text{Unsafe}\}) = 0.0148 + 0.0433 + 0.0771 = 0.1352
$$
$$
m'(\Theta) = 0.2257
$$
$$
\kappa = 0.1322 + 0.0079 = 0.1401
$$

Normalizing:

$$
m_{\text{fused}}(\{\text{Safe}\}) = \frac{0.4991}{1 - 0.1401} = \frac{0.4991}{0.8599} = 0.5804
$$

$$
m_{\text{fused}}(\{\text{Unsafe}\}) = \frac{0.1352}{0.8599} = 0.1572
$$

$$
m_{\text{fused}}(\Theta) = \frac{0.2257}{0.8599} = 0.2625
$$

### Stage 7: Pignistic Decision

$$
BetP(\text{Safe}) = 0.5804 + \frac{0.2625}{2} = 0.5804 + 0.1312 = 0.7116
$$

**Decision:** $0.45 \leq 0.7116 \leq 0.75$ → **Limited Access**

**Interpretation:** Despite the Device domain reporting strong safety ($S_d = 0.90$), the volatile and low-trust Network domain introduces sufficient uncertainty and counter-evidence to prevent Full Access. The system grants Limited Access—a proportionate response that permits basic functionality while restricting access to sensitive resources. If the Network stabilizes over subsequent time steps (reducing $\sigma_n^2$), its weight will increase, potentially upgrading the decision to Full Access. If it continues to deteriorate, the Trust Score will decline further.

---

## 9. The Complete WBF Pipeline: A Formal Summary

The end-to-end Weighted Belief Fusion pipeline is formalized as the following sequential computation, executed at each evaluation epoch $t$:

### Stage 1: Domain Score Computation
For each domain $k \in \{i, d, n, a\}$, aggregate raw telemetry parameters into a domain score:
$$
S_k^{(t)} = f_k\left(\text{telemetry}_k^{(t)}\right), \quad S_k \in [0, 1]
$$

### Stage 2: Variance Computation
Compute the historical variance over a sliding window of $N$ observations:
$$
\sigma_k^{2,(t)} = \frac{1}{N} \sum_{j=t-N+1}^{t} \left(S_{k}^{(j)} - \bar{S}_k^{(t)}\right)^2
$$

### Stage 3: Dynamic Weight Calculation
$$
W_{\text{raw}, k}^{(t)} = \frac{1}{1 + \alpha \cdot \sigma_k^{2,(t)}}, \quad W_{\text{final}, k}^{(t)} = \frac{W_{\text{raw}, k}^{(t)}}{\sum_{j} W_{\text{raw}, j}^{(t)}}
$$

### Stage 4: Evidence Construction (Mass Function via Discounting)
$$
m_k^{(t)}(\{\text{Safe}\}) = S_k^{(t)} \cdot W_{\text{final}, k}^{(t)}
$$
$$
m_k^{(t)}(\{\text{Unsafe}\}) = (1 - S_k^{(t)}) \cdot W_{\text{final}, k}^{(t)}
$$
$$
m_k^{(t)}(\Theta) = 1 - W_{\text{final}, k}^{(t)}
$$

### Stage 5: Spatial Fusion (Dempster's Rule)
$$
m_{\text{spatial}}^{(t)} = \bigoplus_{k=1}^{K} m_k^{(t)}
$$

### Stage 6: Temporal Fusion
$$
m_{\text{cum}}^{(t)} = m_{\text{cum}}^{(t-1)} \oplus m_{\text{spatial}}^{(t)}
$$

### Stage 7: Decision via Pignistic Probability
$$
\text{Trust Score} = BetP(\text{Safe}) = m_{\text{cum}}^{(t)}(\{\text{Safe}\}) + \frac{m_{\text{cum}}^{(t)}(\Theta)}{2}
$$

$$
\text{Access Decision} = \text{Policy}(BetP(\text{Safe}))
$$

---

## 10. Comparative Analysis: WBF vs. Naïve Fusion Models

The following table summarizes the structural superiority of Weighted Belief Fusion over the cumulative and averaging approaches discussed in Sections 4.1.1 and 4.1.2 of Chapter Four:

| Property | Cumulative Fusion | Average Fusion | Weighted Belief Fusion |
|:---|:---|:---|:---|
| **Conflict Resolution** | None; conflicting evidence is summed blindly | Smoothed by averaging; conflicts hidden behind the median | Explicit via Dempster's normalization factor ($\kappa$) |
| **Sensor Reliability** | All sensors equally trusted regardless of behavior | All sensors equally trusted regardless of behavior | Dynamically weighted by historical variance ($\sigma_k^2$) |
| **Uncertainty Representation** | Absent; missing data is ignored or defaults to zero | Absent; missing data distorts the arithmetic mean | Explicit via $m(\Theta)$; missing data maps to ignorance |
| **Spoofing Resistance** | Vulnerable; one high score can eclipse catastrophic failures | Vulnerable; strong vectors camouflage weak ones via averaging | Resilient; spoofed sensors exhibit high variance → weight is suppressed |
| **Graceful Degradation** | Binary Allow/Deny only | Smoothed but still no graduated response | Tiered access (Full/Limited/No) proportional to evidential uncertainty |
| **Mathematical Foundation** | Arithmetic summation with min-cap | Arithmetic mean | Dempster-Shafer Evidence Theory with Pignistic transformation |
| **Adversarial Difficulty** | Trivial; spoof one domain to dominate | Moderate; average across domains | High; must simultaneously spoof multiple stable histories |

---

## 11. Conclusion

Weighted Belief Fusion transforms the Zero Trust decision engine from a deterministic Boolean gatekeeper into a **probabilistic evidential reasoner**. By grounding access decisions in the formal mathematics of Dempster-Shafer theory, the architecture achieves three critical capabilities unavailable to static or naïve fusion models:

1.  **Epistemic Humility**: The explicit modeling of uncertainty ($m(\Theta)$) ensures that absent, incomplete, or unreliable evidence is treated as ignorance—not as danger (which would cause false denials) and not as safety (which would cause false grants). Missing data maps to "I don't know," a mathematically neutral stance that prevents both Type I and Type II errors from incomplete telemetry.

2.  **Dynamic Contextualization**: Variance-based weighting continuously recalibrates the relative influence of each domain, ensuring that the fusion consensus is driven by the most stable and reliable sensors at every evaluation epoch. Erratic sensors are mathematically neutralized—not silenced (they retain a voice if they stabilize), but discounted proportionally to their demonstrated unreliability. This creates **Behavioral Inertia**: a historical mathematical memory of the entity's operational cadence that absorbs transient noise while eventually yielding to persistent threats.

3.  **Principled Decision-Making**: The Pignistic Probability transformation provides a mathematically grounded bridge between the rich interval-valued belief representation of DS theory and the operational requirement for point-estimate access decisions. Rather than arbitrarily picking a point within the $[Bel, Pl]$ interval, the Pignistic transformation applies the principle of insufficient reason to distribute uncertain mass equally, producing a defensible, reproducible Trust Score.

The result is an architecture that mathematically isolates uncertainty from truth, forces adversaries into a combinatorial paradox of multi-domain behavioral mimicry, and provides a continuously adaptive defense posture aligned with the foundational tenets of Zero Trust: *never trust, always verify* (Rose et al., 2020; Chen et al., 2024).

---

## References

Chen, Y., Wang, L., & Zheng, K. (2024). Dynamic trust evaluation based on evidence theory and behavioral metrics in zero trust networks. *IEEE Internet of Things Journal, 11*(5), 8832–8845.

Dempster, A. P. (1967). Upper and lower probabilities induced by a multivalued mapping. *The Annals of Mathematical Statistics, 38*(2), 325–339.

Jøsang, A. (2016). *Subjective Logic: A Formalism for Reasoning Under Uncertainty*. Springer.

Liu, S., Zhang, H., & Chen, X. (2023). Continuous authentication and adaptive access control leveraging Dempster-Shafer evidence theory. *Proceedings of the 2023 IEEE International Conference on Cyber Security*, 112–119.

Mui, L., Mohtashemi, M., & Halberstadt, A. (2002). A computational model of trust and reputation. *Proceedings of the 35th Annual Hawaii International Conference on System Sciences*, 2431–2439.

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero Trust Architecture* (NIST SP 800-207). National Institute of Standards and Technology.

Shafer, G. (1976). *A Mathematical Theory of Evidence*. Princeton University Press.

Smets, P. (1990). The combination of evidence in the transferable belief model. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 12*(5), 447–458.

Smets, P., & Kennes, R. (1994). The transferable belief model. *Artificial Intelligence, 66*(2), 191–234.
