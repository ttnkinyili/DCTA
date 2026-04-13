# Probabilistic Trust Aggregation in Zero Trust Architectures: A Nested Bernoulli-Binomial Framework with Dempster-Shafer Mass Construction

---

**Abstract.** Contemporary Zero Trust Architectures (ZTA) require continuous, context-aware trust evaluation, yet the dominant approaches rely on deterministic scoring functions that conflate epistemic uncertainty with aleatory risk and lack formal mechanisms for propagating measurement imprecision across architectural layers. This paper presents a hierarchical probabilistic framework that models individual security checks as Bernoulli trials, aggregates them into Binomial (and Poisson-Binomial) domain proportions, and composes domain scores into a nested composite structure whose variance is *doubly attenuated*—first by within-domain facet counts and second by cross-domain weight diversification. The analytically tractable variance at each level drives a self-calibrating Dempster-Shafer mass construction: stable domains commit evidence as focal-element mass; erratic domains collapse into vacuous uncertainty. A conjugate Beta-Binomial prior provides principled regularisation during data-scarce initialisation phases. We prove the double-attenuation property, derive per-facet sensitivity gradients, present a complete worked example under a Corporate VPN scenario, and demonstrate that the framework satisfies the monotone likelihood ratio property, ensuring that higher compliance counts constitute monotonically stronger evidence for trust.

**Keywords:** Zero Trust Architecture, Bernoulli trials, Binomial proportion, Dempster-Shafer theory, evidence fusion, Beta-Binomial, trust computation, epistemic uncertainty

---

## 1. Introduction

The foundational tenet of Zero Trust Architecture—*never trust, always verify* (Rose et al., 2020)—demands that every access request undergoes continuous, context-dependent trust evaluation. Yet the overwhelming majority of deployed trust engines compute trust as a deterministic weighted sum of heterogeneous telemetry signals, yielding a single scalar score devoid of any formal uncertainty semantics. Such deterministic scoring introduces three structural vulnerabilities that are incompatible with the security guarantees ZTA purports to offer.

**First**, deterministic scores conflate measurement precision with measurement content. A domain reporting a trust score of 0.85 from five independent, highly consistent sensors is treated identically to a domain reporting 0.85 from a single, volatile sensor—despite the former carrying substantially more evidential weight. Without a formal variance model, the trust engine cannot distinguish a well-supported estimate from an unreliable one.

**Second**, deterministic aggregation provides no principled treatment of missing or degraded telemetry. When a sensor fails to report, deterministic engines must resort to ad hoc imputation—defaulting to a "safe" value (creating a false-positive vulnerability) or a "dangerous" value (causing false denials). Neither strategy is defensible from a decision-theoretic standpoint.

**Third**, the absence of a probabilistic foundation prevents the trust engine from quantifying the *confidence* it should place in its own output. Decision thresholds—"grant access if trust exceeds 0.75"—are applied to point estimates without any accompanying confidence interval, rendering the access decision insensitive to the epistemic state of the underlying evidence.

This paper resolves these vulnerabilities by reformulating trust evaluation as a hierarchical probabilistic inference problem grounded in classical distribution theory. The key insight is structural: individual security checks are inherently binary (a device is either patched or it is not; an MFA challenge either succeeds or it fails), and binary observations are naturally modelled by Bernoulli random variables. The aggregation of independent Bernoulli facets within a domain produces Binomial proportions with analytically tractable variance. The composition of domain-level proportions into a system-wide trust score creates a *nested Binomial* structure whose variance cascade is doubly attenuated—a property we prove formally and connect to Markowitz's (1952) diversification principle from portfolio theory.

The variance at each architectural level serves a dual purpose: it quantifies estimation precision *and* drives the construction of Dempster-Shafer (DS) mass functions, creating a self-calibrating loop in which stable domains commit evidence as specific belief mass while erratic domains automatically collapse into vacuous uncertainty. A conjugate Beta prior provides Bayesian regularisation during the initialisation phase when observations are sparse, yielding the overdispersed Beta-Binomial predictive distribution that naturally enforces conservative trust estimates under data scarcity.

The remainder of this paper is organised as follows. Section 2 reviews the mathematical preliminaries. Sections 3–7 develop the five stages of the framework. Section 8 presents a worked numerical example with sensitivity analysis. Section 9 discusses key statistical properties. Section 10 concludes.

---

## 2. Preliminaries

### 2.1 Bernoulli Trials

A Bernoulli trial is a single random experiment with exactly two outcomes: success ($X = 1$) with probability $p$ and failure ($X = 0$) with probability $1 - p$. The probability mass function, expectation, and variance are:

$$
P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}
$$

$$
\mathbb{E}[X] = p, \quad \text{Var}(X) = p(1-p)
$$

The maximum variance of $0.25$ is attained at $p = 0.5$; as $p \to 0$ or $p \to 1$, variance vanishes. This parabolic variance profile is central to the self-calibrating behaviour of the trust pipeline: facets with extreme compliance probabilities contribute minimal uncertainty, while equivocal facets contribute maximal uncertainty (Blitzstein & Hwang, 2019).

### 2.2 Binomial and Poisson-Binomial Distributions

When $n$ independent Bernoulli trials share a common success probability $p$, their sum $Y = \sum_{j=1}^n X_j$ follows a Binomial distribution:

$$
Y \sim \text{Binomial}(n, p), \quad P(Y = y) = \binom{n}{y} p^y (1-p)^{n-y}
$$

$$
\mathbb{E}[Y] = np, \quad \text{Var}(Y) = np(1-p)
$$

When the trials have heterogeneous success probabilities $p_1, p_2, \ldots, p_n$, the sum follows the **Poisson-Binomial distribution** (Wang, 1993; Hong, 2013):

$$
Y \sim \text{Poisson-Binomial}(p_1, \ldots, p_n)
$$

$$
\mathbb{E}[Y] = \sum_{j=1}^n p_j, \quad \text{Var}(Y) = \sum_{j=1}^n p_j(1-p_j)
$$

The sample proportion $\hat{p} = Y/n$ is a sufficient statistic for the underlying compliance probability and constitutes the maximum likelihood estimator under the Binomial model (Casella & Berger, 2002).

### 2.3 Dempster-Shafer Theory of Evidence

Dempster-Shafer (DS) theory operates over a *frame of discernment* $\Theta$—a finite, exhaustive, mutually exclusive set of possible states. A *basic probability assignment* (BPA), or mass function, $m: 2^\Theta \to [0,1]$ satisfies:

$$
m(\emptyset) = 0, \quad \sum_{A \subseteq \Theta} m(A) = 1
$$

For a binary trust frame $\Theta = \{\text{Safe}, \text{Unsafe}\}$, the power set yields three non-empty focal elements: $\{\text{Safe}\}$, $\{\text{Unsafe}\}$, and $\Theta$ itself, where $m(\Theta)$ represents *epistemic uncertainty*—evidence that is insufficient to discriminate between the two hypotheses (Shafer, 1976).

Two independent mass functions $m_1$ and $m_2$ are combined via **Dempster's Rule of Combination**:

$$
m_{1,2}(A) = \frac{1}{1-\kappa} \sum_{\substack{B \cap C = A \\ B, C \subseteq \Theta}} m_1(B) \cdot m_2(C), \quad A \neq \emptyset
$$

where $\kappa = \sum_{B \cap C = \emptyset} m_1(B) \cdot m_2(C)$ is the inter-source conflict. The rule is commutative, associative, and admits the vacuous mass function $m(\Theta) = 1$ as an identity element—properties essential for incremental, order-independent fusion of multi-domain telemetry (Jøsang, 2016).

For decision-making, mass functions are converted to point probabilities via the **Pignistic transformation** (Smets, 1990):

$$
BetP(x) = \sum_{\substack{A \subseteq \Theta \\ x \in A}} \frac{m(A)}{|A|}
$$

Under the binary frame: $BetP(\text{Safe}) = m(\{\text{Safe}\}) + m(\Theta)/2$.

---

## 3. Stage 1: Trust Facets as Bernoulli Random Variables

### 3.1 The Bernoulli Model of Facet Assessment

The trust evaluation architecture assesses $n_k$ individual facets within each of four trust domains $\mathcal{D}_k$, where $k \in \{i, d, n, a\}$ indexes the Identity, Device, Network, and Application/Data domains respectively. Each facet $j$ within domain $k$ constitutes a discrete, binary security check:

$$
X_{k,j} \sim \text{Bernoulli}(p_{k,j})
$$

where $X_{k,j} \in \{0, 1\}$ and $p_{k,j} = P(X_{k,j} = 1)$ is the probability that facet $j$ in domain $k$ returns a compliant ("trustworthy") outcome at a given evaluation epoch. The Bernoulli model is not imposed for mathematical convenience—it reflects the actual operational semantics of security telemetry, where compliance is evaluated against discrete, unambiguous thresholds defined by the Policy Decision Point: a device either has an up-to-date patch or it does not; a session token either passes cryptographic validation or it fails; an IP address either matches the whitelisted geographic region or it falls outside it (Grassi et al., 2017; NIST, 2020).

### 3.2 Concrete Facet Decomposition

To anchor the Bernoulli model in operational reality, Table 1 enumerates the 16 representative facets across the four trust domains.

**Table 1.** Bernoulli facet decomposition across the four trust domains ($N = 16$ total facets).

| Domain $\mathcal{D}_k$ | Facet $X_{k,j}$ | Bernoulli Interpretation ($X = 1$: Compliant) |
|:---|:---|:---|
| **Identity** ($\mathcal{D}_i$, $n_i = 4$) | $X_{i,1}$: MFA Completion | Multi-factor authentication ceremony completed |
| | $X_{i,2}$: Credential Freshness | Token issued within valid TTL window |
| | $X_{i,3}$: Role Authorisation | User role matches RBAC policy |
| | $X_{i,4}$: Behavioural Biometric | Keystroke/mouse dynamics match enrolled profile |
| **Device** ($\mathcal{D}_d$, $n_d = 5$) | $X_{d,1}$: Patch Currency | OS and critical software patches current |
| | $X_{d,2}$: Endpoint Protection | EDR/antivirus agent active and reporting |
| | $X_{d,3}$: Disk Encryption | Full-disk encryption enabled |
| | $X_{d,4}$: Hardware Attestation | TPM attestation chain validates integrity |
| | $X_{d,5}$: Jailbreak/Root Status | Device not jailbroken or rooted |
| **Network** ($\mathcal{D}_n$, $n_n = 4$) | $X_{n,1}$: Encryption Protocol | Connection uses TLS 1.3 or higher |
| | $X_{n,2}$: Geographic Compliance | Source IP within authorised region |
| | $X_{n,3}$: DNS Integrity | DNS responses validate against DNSSEC |
| | $X_{n,4}$: Proxy/VPN Detection | No anonymising proxy detected |
| **Application** ($\mathcal{D}_a$, $n_a = 3$) | $X_{a,1}$: Data Classification Match | Resource sensitivity matches clearance |
| | $X_{a,2}$: Access Pattern Normality | Request frequency within baseline |
| | $X_{a,3}$: API Authentication | Application-layer token valid |

The probability parameters $p_{k,j}$ are not static constants but are themselves functions of the entity's current contextual state. A device with 30 consecutive successful patch checks has an empirical $\hat{p}_{d,1} \approx 1.0$; a BYOD device with intermittent patching may exhibit $\hat{p}_{d,1} \approx 0.6$ (Grassi et al., 2017).

### 3.3 Weighted Facet Aggregation

Not all facets carry equal security significance. The failure of hardware attestation ($X_{d,4} = 0$) represents a more severe compromise than the absence of disk encryption ($X_{d,3} = 0$). To accommodate this operational reality, the domain trust score is computed as a *weighted* proportion:

$$
\boxed{S_k = \frac{\sum_{j=1}^{n_k} w_{k,j} \cdot X_{k,j}}{\sum_{j=1}^{n_k} w_{k,j}}}
$$

where $w_{k,j} > 0$ is the policy-defined importance weight of facet $j$ within domain $k$. The weighted formulation preserves $S_k \in [0, 1]$ and remains a function of independent Bernoulli observations. Its variance is:

$$
\text{Var}(S_k) = \frac{\sum_{j=1}^{n_k} w_{k,j}^2 \cdot p_{k,j}(1 - p_{k,j})}{\left(\sum_{j=1}^{n_k} w_{k,j}\right)^2}
$$

This weighted variance directly feeds the dynamic weighting mechanism in the Dempster-Shafer pipeline: domains where high-weight facets exhibit instability (high $p_{k,j}(1-p_{k,j})$) produce elevated $\sigma_k^2$, triggering proportional weight suppression through $W_k = (1 + \alpha \cdot \sigma_k^2)^{-1}$.

---

## 4. Stage 2: Domain Trust Scores as Binomial Proportions

### 4.1 The Homogeneous Case

When the $n_k$ facets within a domain share a common compliance probability $p_k$, the total number of compliant facets follows a classical Binomial distribution:

$$
Y_k = \sum_{j=1}^{n_k} X_{k,j} \sim \text{Binomial}(n_k, p_k)
$$

The **domain trust score** is the binomial proportion:

$$
S_k = \frac{Y_k}{n_k}
$$

This proportion is the maximum likelihood estimator of the underlying domain compliance probability (Casella & Berger, 2002). Its expectation and variance are:

$$
\mathbb{E}[S_k] = p_k, \quad \text{Var}(S_k) = \frac{p_k(1 - p_k)}{n_k}
$$

The inverse-$n_k$ variance scaling has a critical operational implication: **domains with more constituent facets produce more precise trust scores**. The Identity domain ($n_i = 4$) has a maximum variance of $0.25/4 = 0.0625$; the Device domain ($n_d = 5$) achieves a tighter maximum of $0.25/5 = 0.05$. This precision differential is automatically captured by the variance-based weighting mechanism.

### 4.2 The Heterogeneous Case: Poisson-Binomial Generalisation

In operational deployments, the assumption of a common $p_k$ is unrealistic. A user's MFA completion probability ($p_{i,1} \approx 0.99$) may far exceed their behavioural biometric match probability ($p_{i,4} \approx 0.85$). Under heterogeneous facet probabilities, $Y_k$ follows the Poisson-Binomial distribution, and the domain trust score has:

$$
\mathbb{E}[S_k] = \frac{1}{n_k} \sum_{j=1}^{n_k} p_{k,j} = \bar{p}_k, \quad \text{Var}(S_k) = \frac{1}{n_k^2} \sum_{j=1}^{n_k} p_{k,j}(1 - p_{k,j})
$$

**Proposition 1** (Variance reduction under heterogeneity). *Under the Poisson-Binomial model, $\text{Var}(S_k) \leq \frac{\bar{p}_k(1 - \bar{p}_k)}{n_k}$, with equality holding only when all $p_{k,j}$ are identical.*

*Proof.* By the concavity of $f(p) = p(1-p)$ on $[0,1]$ and Jensen's inequality, $\frac{1}{n_k}\sum_j p_{k,j}(1-p_{k,j}) \leq \bar{p}_k(1-\bar{p}_k)$. Dividing both sides by $n_k$ yields the result. $\square$

This means that **diversifying the types of checks within a domain**—mixing high-confidence checks (MFA) with lower-confidence checks (behavioural biometrics)—produces more stable domain scores than relying on checks of identical reliability (Johnson et al., 2005).

---

## 5. Stage 3: The Nested Composite Structure

### 5.1 Nested Architecture

With four independent domains, each producing a binomial proportion $S_k$, the composite trust score is:

$$
\boxed{S_{\text{composite}} = \sum_{k \in \{i,d,n,a\}} W_k \cdot S_k}
$$

where $W_k$ are the normalised dynamic weights satisfying $\sum_k W_k = 1$. This weighted sum of binomial proportions constitutes the *nested Binomial composite*—a second-level aggregation operating on the outputs of four first-level Binomial processes.

### 5.2 Double-Attenuation Variance Property

**Theorem 1** (Double Attenuation). *The variance of the nested composite trust score is doubly attenuated:*

$$
\text{Var}(S_{\text{composite}}) = \sum_k W_k^2 \cdot \frac{p_k(1-p_k)}{n_k}
$$

*where the first attenuation factor $1/n_k$ arises from within-domain Binomial aggregation and the second attenuation factor $W_k^2$ arises from cross-domain weight diversification.*

*Proof.* Since the four domains collect telemetry from physically and logically independent sensor subsystems, the domain scores $S_i, S_d, S_n, S_a$ are mutually independent. For independent random variables and constants $W_k$:

$$
\text{Var}\left(\sum_k W_k S_k\right) = \sum_k W_k^2 \cdot \text{Var}(S_k) = \sum_k W_k^2 \cdot \frac{p_k(1-p_k)}{n_k}
$$

The first equality follows from the independence of the $S_k$; the second substitutes $\text{Var}(S_k) = p_k(1-p_k)/n_k$ from the Binomial proportion. $\square$

### 5.3 The Variance Cascade

The full variance decomposition through the nested hierarchy reveals a three-stage cascade:

**Stage 1 — Facet-Level (Bernoulli):**

$$
\text{Var}(X_{k,j}) = p_{k,j}(1-p_{k,j}) \leq 0.25
$$

**Stage 2 — Domain-Level (Binomial Proportion):**

$$
\text{Var}(S_k) = \frac{p_k(1-p_k)}{n_k} \leq \frac{0.25}{n_k}
$$

For the Device domain with $n_d = 5$, the maximum domain variance is $0.05$—a five-fold reduction from the facet level.

**Stage 3 — Composite-Level (Nested Binomial):**

$$
\text{Var}(S_{\text{composite}}) = \sum_k W_k^2 \cdot \frac{p_k(1-p_k)}{n_k} \leq \frac{0.25}{n_{\min}} \cdot \sum_k W_k^2
$$

Since $\sum_k W_k = 1$ and $W_k \leq 1$, we have $\sum_k W_k^2 \leq 1$, with equality only if all weight concentrates on a single domain. For approximately equal weights ($W_k \approx 0.25$ for $K = 4$), $\sum_k W_k^2 \approx 0.0625$, yielding a composite variance upper bound of approximately $\frac{0.25}{n_{\min}} \times 0.0625 = \frac{0.0156}{n_{\min}}$—an **order-of-magnitude reduction** from the domain level.

This variance cascade demonstrates that the nested Binomial architecture is inherently *self-stabilising*: the more facets per domain and the more domains in the fusion, the more precise the composite trust estimate becomes.

### 5.4 Connection to Portfolio Diversification

The double-attenuation property is a direct instance of the diversification principle formalised by Markowitz (1952) in modern portfolio theory. In Markowitz's framework, the variance of a portfolio of $K$ uncorrelated assets with weights $W_k$ and individual variances $\sigma_k^2$ is:

$$
\sigma_{\text{portfolio}}^2 = \sum_k W_k^2 \cdot \sigma_k^2
$$

The trust architecture exploits this same mechanism: by distributing evidential "investment" across four independent domains, the composite trust estimate achieves variance reduction that no single domain could provide in isolation. The analogy extends further: just as Markowitz proved that equally-weighted portfolios minimise variance when asset variances are equal, the trust engine achieves minimum composite variance when $W_k = 1/K$ and all domains have identical $\text{Var}(S_k)$—the *maximally diversified* trust posture (Clemen & Winkler, 1999).

---

## 6. Stage 4: Dempster-Shafer Mass Construction from Binomial Variance

### 6.1 Variance-Driven Dynamic Weighting

The binomial variance $\sigma_k^2 = \text{Var}(S_k)$, computed over a sliding window of $N$ evaluation epochs, serves as the input to a dynamic weighting function that modulates each domain's evidential authority:

$$
\boxed{W_{\text{raw},k} = \frac{1}{1 + \alpha \cdot \sigma_k^2}}
$$

where $\alpha > 0$ is the **variance penalty amplifier** governing the aggressiveness of instability penalisation. The weighting function satisfies the following properties:

1. **Boundedness**: $W_{\text{raw},k} \in (0, 1]$ for all $\sigma_k^2 \geq 0$.
2. **Monotone decay**: $W_{\text{raw},k}$ is strictly decreasing in $\sigma_k^2$.
3. **Half-weight characterisation**: $W_{\text{raw},k} = 0.5$ when $\sigma_k^2 = 1/\alpha$.
4. **Limiting behaviour**: $W_{\text{raw},k} \to 1$ as $\sigma_k^2 \to 0$; $W_{\text{raw},k} \to 0$ as $\sigma_k^2 \to \infty$.

**Table 2.** Weight dynamics under varying variance levels ($\alpha = 5$).

| $\sigma^2$ | $\alpha \cdot \sigma^2$ | $W_{\text{raw}}$ | Interpretation |
|:---|:---|:---|:---|
| $0.00$ | $0.00$ | $1.000$ | Perfect stability → full evidential weight |
| $0.02$ | $0.10$ | $0.909$ | Minimal jitter → negligible penalty |
| $0.10$ | $0.50$ | $0.667$ | Moderate instability → one-third of evidence shifted to uncertainty |
| $0.20$ | $1.00$ | $0.500$ | Half-weight point → half the evidence is uncertain |
| $0.25$ | $1.25$ | $0.444$ | High volatility → majority of evidence discounted |
| $0.50$ | $2.50$ | $0.286$ | Severe instability → domain nearly vacuous |

The raw weights are normalised to form a proper distribution:

$$
W_k = \frac{W_{\text{raw},k}}{\sum_{j=1}^K W_{\text{raw},j}}, \quad \sum_{k=1}^K W_k = 1
$$

### 6.2 Mass Function Construction via Discounting

Having computed the normalised weight $W_k$ for each domain, the engine constructs a Dempster-Shafer mass function by using the weight as a *discounting factor*. Two pieces of information are synthesised: (i) the domain score $S_k$ dictates the *proportion* of evidence supporting Safety versus Danger; (ii) the weight $W_k$ dictates *how much* of this evidence is confidently committed versus reserved as uncertainty.

$$
\boxed{m_k(\{\text{Safe}\}) = S_k \cdot W_k}
$$

$$
\boxed{m_k(\{\text{Unsafe}\}) = (1 - S_k) \cdot W_k}
$$

$$
\boxed{m_k(\Theta) = 1 - W_k}
$$

**Verification of BPA axioms.** These three components sum to unity by construction:

$$
S_k W_k + (1-S_k)W_k + (1-W_k) = W_k[S_k + 1 - S_k] + 1 - W_k = W_k + 1 - W_k = 1 \;\;\checkmark
$$

Since $S_k \in [0,1]$ and $W_k \in [0,1]$, all three masses are non-negative. The empty set mass is $m(\emptyset) = 0$ by the Closed World Assumption. The construction therefore produces a valid BPA for all possible input combinations.

This mechanism is closely related to Shafer's (1976) original concept of **evidence discounting**, where the reliability of a source modulates the degree to which its testimony is accepted. In Shafer's formalisation, discounting at rate $r$ transforms $m(A) \to (1-r) \cdot m(A)$ for singletons, with the residual mass moved to $\Theta$. The construction above is equivalent, with the discount rate $r = 1 - W_k$.

### 6.3 Self-Calibrating Uncertainty

The construction creates a mathematically elegant feedback circuit:

1. **Bernoulli facets** generate **Binomial proportions** $S_k$.
2. **Binomial variance** $\sigma_k^2$ governs the **dynamic weight** $W_k = (1 + \alpha\sigma_k^2)^{-1}$.
3. **The weight** modulates how much of $S_k$ is committed as DS mass versus reserved as epistemic uncertainty $m_k(\Theta)$.

The self-calibration manifests at the boundary conditions:

**Table 3.** Behaviour at limiting and intermediate conditions.

| Condition | $W_k$ | $m(\{\text{Safe}\})$ | $m(\Theta)$ | Interpretation |
|:---|:---|:---|:---|:---|
| Perfect stability ($\sigma_k^2 = 0$) | $1.0$ | $S_k$ | $0$ | Full evidential commitment |
| Complete chaos ($\sigma_k^2 \to \infty$) | $\to 0$ | $\to 0$ | $\to 1$ | Vacuous—domain mathematically invisible |
| High score, low weight ($S_k=0.95, W_k=0.15$) | $0.15$ | $0.143$ | $0.85$ | Anti-spoofing: erratic high scores mostly ignored |
| Low score, high weight ($S_k=0.10, W_k=0.90$) | $0.90$ | $0.09$ | $0.10$ | Reliable alarm: stable bad news heavily weighted |

The anti-spoofing property is particularly significant: an attacker who compromises a sensor and forces it to broadcast artificially high scores will simultaneously introduce variance into the historical signal. The induced variance triggers weight suppression, converting the spoofed testimony into mostly ignorance—preventing the attack from dominating the fusion output. The **vacuous identity property** of Dempster's Rule ($m \oplus m_{\text{vacuous}} = m$) guarantees that a domain rendered vacuous by high variance cannot harm the fusion consensus; it is mathematically invisible (Jøsang, 2016).

---

## 7. Stage 5: Beta-Binomial Regularisation

### 7.1 Conjugate Beta Prior

The frequentist treatment above computes $S_k$ as a direct sample proportion. However, during the initialisation phase of a session ($t < N$, where $N$ is the sliding window length), variance estimates are statistically immature and facet probability estimates are unreliable. A Bayesian treatment introduces the **Beta distribution** as the conjugate prior for each facet's compliance probability (Gelman et al., 2013):

$$
p_{k,j} \sim \text{Beta}(\alpha_0, \beta_0) \quad \text{(prior)}
$$

$$
X_{k,j} \mid p_{k,j} \sim \text{Bernoulli}(p_{k,j}) \quad \text{(likelihood)}
$$

After observing $N$ evaluation epochs with $s$ successes and $f = N - s$ failures:

$$
p_{k,j} \mid \text{data} \sim \text{Beta}(\alpha_0 + s, \; \beta_0 + f) \quad \text{(posterior)}
$$

The posterior mean provides a regularised estimate:

$$
\hat{p}_{k,j}^{\text{Bayes}} = \frac{\alpha_0 + s}{\alpha_0 + \beta_0 + N}
$$

This estimate exhibits *shrinkage* toward the prior mean $\alpha_0/(\alpha_0 + \beta_0)$, preventing extreme estimates when data is sparse. This is directly relevant to the convergence dynamics of the trust architecture during the initialisation phase—the Beta prior provides a principled mechanism for regularising facet probability estimates until sufficient observations accumulate (Jøsang, 2016; Mui et al., 2002).

### 7.2 The Beta-Binomial Compound Distribution

When facet probabilities are governed by an incompletely converged Beta prior, the predictive distribution of the number of compliant facets follows the **Beta-Binomial compound distribution**:

$$
P(Y_k = y \mid \alpha_0, \beta_0) = \binom{n_k}{y} \frac{B(\alpha_0 + y, \; \beta_0 + n_k - y)}{B(\alpha_0, \beta_0)}
$$

where $B(\cdot, \cdot)$ is the Beta function. The Beta-Binomial is **overdispersed** relative to the Binomial—its variance exceeds that of the standard Binomial because it accounts for the additional uncertainty in the probability parameter itself:

$$
\text{Var}_{\text{BB}}(Y_k) = n_k \cdot \frac{\alpha_0 \beta_0 (\alpha_0 + \beta_0 + n_k)}{(\alpha_0 + \beta_0)^2 (\alpha_0 + \beta_0 + 1)}
$$

This overdispersion is operationally significant: during the initialisation phase, the trust engine has not yet established a reliable estimate of each facet's compliance probability. The Beta-Binomial model captures this *parameter uncertainty* and propagates it through the domain score to the composite trust, resulting in wider confidence intervals and higher $m(\Theta)$ values—exactly the conservative behaviour a Zero Trust system should exhibit when historical data is insufficient.

### 7.3 Convergence to the Binomial

As observations accumulate ($N \to \infty$), the posterior concentrates ($\alpha_0 + s$ and $\beta_0 + f$ grow large), the Beta-Binomial converges to the standard Binomial, and trust estimates tighten. This provides a principled convergence dynamic: the system transitions automatically from a cautious, regularised regime to a precise, data-driven regime without requiring manual threshold calibration. The convergence interval aligns naturally with the sliding window size $N$ of the variance computation, creating a unified initialisation-to-maturity trajectory (Gelman et al., 2013).

---

## 8. Numerical Example and Sensitivity Analysis

### 8.1 Worked Example: Corporate VPN Scenario

Consider a single evaluation epoch for an entity connecting via a corporate VPN. We trace the complete pipeline from Bernoulli facets to access decision.

#### Level 1 — Facet Observations

**Identity Domain** ($n_i = 4$):

| Facet | $X_{i,j}$ | $\hat{p}_{i,j}$ |
|:---|:---:|:---:|
| MFA Completion | 1 | 0.99 |
| Credential Freshness | 1 | 0.95 |
| Role Authorisation | 1 | 0.98 |
| Behavioural Biometric | 0 | 0.82 |

$$
Y_i = 3, \quad S_i = \frac{3}{4} = 0.750
$$

**Device Domain** ($n_d = 5$):

| Facet | $X_{d,j}$ | $\hat{p}_{d,j}$ |
|:---|:---:|:---:|
| Patch Currency | 1 | 0.90 |
| Endpoint Protection | 1 | 0.97 |
| Disk Encryption | 1 | 0.99 |
| Hardware Attestation | 1 | 0.95 |
| Jailbreak/Root Status | 1 | 0.98 |

$$
Y_d = 5, \quad S_d = \frac{5}{5} = 1.000
$$

**Network Domain** ($n_n = 4$):

| Facet | $X_{n,j}$ | $\hat{p}_{n,j}$ |
|:---|:---:|:---:|
| Encryption Protocol (TLS 1.3) | 1 | 0.97 |
| Geographic Compliance | 1 | 0.99 |
| DNS Integrity | 0 | 0.80 |
| Proxy/VPN Detection | 1 | 0.95 |

$$
Y_n = 3, \quad S_n = \frac{3}{4} = 0.750
$$

**Application Domain** ($n_a = 3$):

| Facet | $X_{a,j}$ | $\hat{p}_{a,j}$ |
|:---|:---:|:---:|
| Data Classification Match | 1 | 0.96 |
| Access Pattern Normality | 1 | 0.93 |
| API Authentication | 1 | 0.99 |

$$
Y_a = 3, \quad S_a = \frac{3}{3} = 1.000
$$

#### Level 2 — Composite Trust (Equal Weights)

With $W_k = 0.25$ for all domains:

$$
S_{\text{composite}} = 0.25(0.750) + 0.25(1.000) + 0.25(0.750) + 0.25(1.000)
$$

$$
= 0.1875 + 0.2500 + 0.1875 + 0.2500 = \mathbf{0.875}
$$

#### Level 2 — Composite Variance

$$
\text{Var}(S_{\text{composite}}) = \sum_k (0.25)^2 \cdot \frac{p_k(1-p_k)}{n_k}
$$

Using $p_i \approx 0.935$, $p_d \approx 0.958$, $p_n \approx 0.928$, $p_a \approx 0.960$ (mean facet probabilities):

$$
\approx 0.0625 \left[\frac{0.061}{4} + \frac{0.040}{5} + \frac{0.067}{4} + \frac{0.038}{3}\right]
$$

$$
= 0.0625 \times [0.01525 + 0.00800 + 0.01675 + 0.01267] = 0.0625 \times 0.05267 \approx 0.0033
$$

The composite standard deviation is $\sigma_{\text{composite}} \approx 0.057$, yielding a 95% confidence interval of $0.875 \pm 0.112$, or $[0.763,\; 0.987]$.

#### Level 3 — DS Mass and Access Decision

In this stable corporate scenario, domain variances are low ($\sigma_k^2 \approx 0.01$), so weights converge to approximately $W_k \approx 0.25$. After spatial fusion across all four domains via Dempster's Rule, the resulting Pignistic probability yields:

$$
BetP(\text{Safe}) \approx 0.875 + \frac{m(\Theta)}{2} > 0.75
$$

**Decision: Full Access** ✓

The Identity domain's score of $0.750$ (caused by the single biometric mismatch) would exhibit higher rolling variance if such mismatches are intermittent, triggering the dynamic weighting mechanism to reduce Identity's influence on the fused output.

### 8.2 Per-Facet Failure Sensitivity

The nested Binomial structure exhibits a natural sensitivity gradient. The impact of a single facet failure ($X_{k,j}: 1 \to 0$) on the composite trust score is:

$$
\boxed{\Delta S_{\text{composite}} = -\frac{W_k}{n_k}}
$$

**Table 4.** Per-facet failure sensitivity by domain ($W_k = 0.25$).

| Domain | $n_k$ | $\Delta S_{\text{composite}}$ | Relative Impact |
|:---|:---:|:---:|:---|
| Identity ($\mathcal{D}_i$) | 4 | $-0.0625$ | Moderate |
| Device ($\mathcal{D}_d$) | 5 | $-0.0500$ | Lower |
| Network ($\mathcal{D}_n$) | 4 | $-0.0625$ | Moderate |
| Application ($\mathcal{D}_a$) | 3 | $-0.0833$ | **Highest** |

Domains with *fewer* facets are more sensitive to individual failures. The Application domain, with only 3 facets, suffers the largest per-facet impact ($-0.0833$), while the Device domain demonstrates the most resilience ($-0.0500$). This structural property creates a direct incentive for architects to include more independent facets in critical domains, simultaneously improving both precision (lower variance) and resilience (lower per-facet impact).

### 8.3 Impact of Dynamic Weighting on Sensitivity

When variance-based weighting is active, the sensitivity becomes state-dependent:

$$
\Delta S_{\text{composite}} = -\frac{W_k(\sigma_k^2)}{n_k}
$$

A domain experiencing high variance (e.g., $\sigma_n^2 = 0.20$, $\alpha = 5$) sees its normalised weight drop from 0.25 to approximately 0.17, reducing its per-facet failure impact from $-0.0625$ to approximately $-0.043$. The framework thus provides double protection: unstable domains are simultaneously less trusted in their score contribution *and* less impactful per individual failure.

---

## 9. Statistical Properties and Operational Implications

### 9.1 Central Limit Theorem Approximation

By the Central Limit Theorem, for domains with a sufficiently large number of facets, the domain trust score is approximately normally distributed:

$$
S_k \xrightarrow{d} \mathcal{N}\left(p_k, \frac{p_k(1-p_k)}{n_k}\right) \quad \text{as } n_k \to \infty
$$

For $n_k \geq 5$ (satisfied by the Device domain), the normal approximation provides a practical mechanism for constructing confidence intervals around the domain trust score:

$$
S_k \pm z_{1-\alpha/2} \sqrt{\frac{S_k(1 - S_k)}{n_k}}
$$

These confidence intervals can be propagated through the nested hierarchy to quantify uncertainty at the composite level—providing an alternative uncertainty metric that complements the DS $m(\Theta)$ term (Agresti & Coull, 1998).

### 9.2 Monotone Likelihood Ratio Property

**Proposition 2.** *The Binomial distribution satisfies the monotone likelihood ratio (MLR) property: if $p_1 > p_2$, then the likelihood ratio $\frac{P(Y=y \mid p_1)}{P(Y=y \mid p_2)}$ is non-decreasing in $y$.*

This guarantees that higher observed compliance counts constitute *monotonically stronger evidence* for higher underlying compliance probabilities, creating a mathematically rigorous trust ordering. The MLR property ensures that the domain trust score $S_k$ is a sufficient statistic for the access decision—no additional information from individual facet outcomes can improve the decision beyond what $S_k$ already captures (Casella & Berger, 2002).

---

## 10. Conclusion

This paper has established a rigorous probabilistic foundation for trust aggregation in Zero Trust Architectures through a five-stage hierarchical framework.

**Stage 1** models individual security checks as Bernoulli trials, capturing the inherently binary nature of compliance evaluation across 16 facets spanning four independent domains. **Stage 2** aggregates independent Bernoulli facets into Binomial (and, in the heterogeneous case, Poisson-Binomial) domain proportions with analytically tractable variance that decreases inversely with the number of facets—rewarding architectural breadth with statistical precision. **Stage 3** composes domain scores into a nested Binomial composite whose variance is doubly attenuated: first by within-domain facet diversification and second by cross-domain weight diversification, directly instantiating Markowitz's (1952) portfolio diversification principle in the trust evaluation domain. **Stage 4** constructs Dempster-Shafer mass functions from the Binomial variance, creating a self-calibrating pipeline in which stable domains commit evidence as specific focal-element mass while erratic domains collapse into vacuous uncertainty—achieving spoofing resistance, graceful degradation, and epistemic honesty without manual threshold tuning. **Stage 5** introduces a conjugate Beta-Binomial prior that regularises probability estimates during data-scarce initialisation phases, with the overdispersion property enforcing conservative trust until sufficient evidence accumulates.

The resulting architecture ensures that every layer—from the individual Bernoulli facet check through the nested Binomial composite to the final Pignistic access decision—is governed by a coherent, analytically tractable probabilistic framework. The framework transforms the Zero Trust decision engine from a deterministic Boolean gatekeeper into a probabilistic evidential reasoner that explicitly models what it knows, what it does not know, and how confident it is in the distinction.

---

## References

Agresti, A., & Coull, B. A. (1998). Approximate is better than "exact" for interval estimation of binomial proportions. *The American Statistician, 52*(2), 119–126. https://doi.org/10.1080/00031305.1998.10480550

Blitzstein, J. K., & Hwang, J. (2019). *Introduction to probability* (2nd ed.). CRC Press/Chapman & Hall.

Casella, G., & Berger, R. L. (2002). *Statistical inference* (2nd ed.). Duxbury/Thomson Learning.

Clemen, R. T., & Winkler, R. L. (1999). Combining probability distributions from experts in risk analysis. *Risk Analysis, 19*(2), 187–203. https://doi.org/10.1111/j.1539-6924.1999.tb00399.x

Dempster, A. P. (1967). Upper and lower probabilities induced by a multivalued mapping. *The Annals of Mathematical Statistics, 38*(2), 325–339. https://doi.org/10.1214/aoms/1177698950

Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian data analysis* (3rd ed.). Chapman & Hall/CRC.

Grassi, P. A., Fenton, J. L., Newton, E. M., Perlner, R. A., Regenscheid, A. R., Burr, W. E., & Richer, J. P. (2017). *Digital identity guidelines: Authentication and lifecycle management* (NIST Special Publication 800-63B). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-63b

Hong, Y. (2013). On computing the distribution function for the Poisson binomial distribution. *Computational Statistics & Data Analysis, 59*, 41–51. https://doi.org/10.1016/j.csda.2012.10.006

Johnson, N. L., Kemp, A. W., & Kotz, S. (2005). *Univariate discrete distributions* (3rd ed.). John Wiley & Sons.

Jøsang, A. (2016). *Subjective logic: A formalism for reasoning under uncertainty*. Springer. https://doi.org/10.1007/978-3-319-42337-1

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance, 7*(1), 77–91. https://doi.org/10.2307/2975974

Mui, L., Mohtashemi, M., & Halberstadt, A. (2002). A computational model of trust and reputation. *Proceedings of the 35th Annual Hawaii International Conference on System Sciences*, 2431–2439. https://doi.org/10.1109/HICSS.2002.994181

National Institute of Standards and Technology. (2020). *Zero trust architecture* (NIST Special Publication 800-207). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-207

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology.

Shafer, G. (1976). *A mathematical theory of evidence*. Princeton University Press.

Smets, P. (1990). The combination of evidence in the transferable belief model. *IEEE Transactions on Pattern Analysis and Machine Intelligence, 12*(5), 447–458. https://doi.org/10.1109/34.56205

Smets, P., & Kennes, R. (1994). The transferable belief model. *Artificial Intelligence, 66*(2), 191–234. https://doi.org/10.1016/0004-3702(94)90026-4

Wang, Y. H. (1993). On the number of successes in independent trials. *Statistica Sinica, 3*(2), 295–312.
