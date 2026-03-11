# Probabilistic Foundations of Trust Aggregation: From Bernoulli Facets to Nested Binomial Domain Scores

## 1. Introduction: Trust as a Probabilistic Phenomenon

The trust evaluation architecture developed in this thesis treats each access decision as the outcome of a structured probabilistic inference process operating across four independent telemetry domains: Identity Context ($\mathcal{D}_i$), Device Posture ($\mathcal{D}_d$), Network Variance ($\mathcal{D}_n$), and Application/Data Sensitivity ($\mathcal{D}_a$). Within each domain, multiple individual security attributes—termed *facets*—are continuously assessed. The question that this section formalizes is: **How do the atomic, binary outcomes of individual facet checks compose mathematically into the continuous domain trust scores $S_k \in [0, 1]$ that feed the Dempster-Shafer fusion pipeline?**

The answer lies in a hierarchical probabilistic architecture grounded in classical distribution theory. Each individual facet check constitutes a *Bernoulli trial*—a single binary observation of compliance or non-compliance. Within a domain, the aggregation of $n_k$ independent Bernoulli facets produces a *Binomial distribution* governing the number of successful trust checks. At the composite level, the domain scores themselves—each derived from an independent binomial process—are further combined in a *nested binomial* structure that propagates uncertainty upward through the architectural hierarchy. This nested composition ensures that the eventual trust value $S_{\text{composite}}$ inherits the full probabilistic machinery of the Bernoulli-Binomial family, including analytically tractable variance, well-characterized confidence intervals, and natural compatibility with the Dempster-Shafer mass function construction described in Chapter Four (Casella & Berger, 2002; Jøsang, 2016).

---

## 2. Stage 1: Trust Facets as Bernoulli Random Variables

### 2.1 The Bernoulli Model of Facet Assessment

Within each trust domain $\mathcal{D}_k$, the evaluation engine assesses $n_k$ individual facets. Each facet $j$ within domain $k$ represents a discrete, binary security check:

$$
X_{k,j} \sim \text{Bernoulli}(p_{k,j})
$$

where $X_{k,j} \in \{0, 1\}$ and $p_{k,j} = P(X_{k,j} = 1)$ is the probability that facet $j$ in domain $k$ returns a compliant ("trustworthy") outcome at a given evaluation epoch. The probability mass function is:

$$
P(X_{k,j} = x) = p_{k,j}^{x} \cdot (1 - p_{k,j})^{1-x}, \quad x \in \{0, 1\}
$$

The mean and variance of each Bernoulli facet are:

$$
\mathbb{E}[X_{k,j}] = p_{k,j}, \quad \text{Var}(X_{k,j}) = p_{k,j}(1 - p_{k,j})
$$

The Bernoulli model is appropriate because each individual facet check is inherently dichotomous: a device either has an up-to-date patch or it does not; a session token either passes cryptographic validation or it fails; an IP address either matches the whitelisted geographic region or it falls outside it (Blitzstein & Hwang, 2019). This binary observational structure is not an approximation imposed for mathematical convenience—it reflects the actual operational semantics of security telemetry, where compliance is evaluated against discrete, unambiguous thresholds defined by the Policy Decision Point (Rose et al., 2020).

### 2.2 Concrete Facet Decomposition by Domain

To ground the Bernoulli model in the specific architecture of this thesis, the following table enumerates representative facets within each of the four trust domains:

| Domain $\mathcal{D}_k$ | Facet $X_{k,j}$ | Bernoulli Interpretation ($X = 1$: Compliant) |
|:---|:---|:---|
| **Identity** ($\mathcal{D}_i$) | $X_{i,1}$: MFA Completion | Multi-factor authentication ceremony successfully completed |
| | $X_{i,2}$: Credential Freshness | Authentication token issued within the valid TTL window |
| | $X_{i,3}$: Role Authorization | User role matches the requested resource's RBAC policy |
| | $X_{i,4}$: Behavioral Biometric | Keystroke/mouse dynamics match the enrolled behavioral profile |
| **Device** ($\mathcal{D}_d$) | $X_{d,1}$: Patch Currency | Operating system and critical software patches are current |
| | $X_{d,2}$: Endpoint Protection | EDR/antivirus agent is active and reporting |
| | $X_{d,3}$: Disk Encryption | Full-disk encryption (e.g., BitLocker, FileVault) is enabled |
| | $X_{d,4}$: Hardware Attestation | TPM attestation chain validates device integrity |
| | $X_{d,5}$: Jailbreak/Root Status | Device has not been jailbroken or rooted |
| **Network** ($\mathcal{D}_n$) | $X_{n,1}$: Encryption Protocol | Connection uses TLS 1.3 or higher |
| | $X_{n,2}$: Geographic Compliance | Source IP falls within the authorized geographic region |
| | $X_{n,3}$: DNS Integrity | DNS responses validate against DNSSEC signatures |
| | $X_{n,4}$: Proxy/VPN Detection | Connection does not originate from a known anonymizing proxy |
| **Application** ($\mathcal{D}_a$) | $X_{a,1}$: Data Classification Match | Requested resource sensitivity matches the user's clearance |
| | $X_{a,2}$: Access Pattern Normality | Request frequency and volume fall within baseline parameters |
| | $X_{a,3}$: API Authentication | Application-layer API token is valid and unexpired |

Each of these facets produces a single Bernoulli observation at every evaluation epoch $t$. The probability parameters $p_{k,j}$ are not static constants but are themselves functions of the entity's current contextual state—a device that has been consistently patched for 30 consecutive evaluation cycles has an empirical $\hat{p}_{d,1} \approx 1.0$, whereas a BYOD device with a spotty patching history may exhibit $\hat{p}_{d,1} \approx 0.6$ (Grassi et al., 2017; National Institute of Standards and Technology [NIST], 2020).

---

## 3. Stage 2: Domain Trust Scores as Binomial Proportions

### 3.1 Aggregation Within a Domain: The Homogeneous Case

When the $n_k$ facets within a domain are independent and share a common compliance probability $p_k$ (the homogeneous case), the total number of compliant facets follows a classical Binomial distribution:

$$
Y_k = \sum_{j=1}^{n_k} X_{k,j} \sim \text{Binomial}(n_k, p_k)
$$

The probability mass function is:

$$
P(Y_k = y) = \binom{n_k}{y} p_k^{y} (1 - p_k)^{n_k - y}, \quad y \in \{0, 1, \ldots, n_k\}
$$

The **domain trust score** $S_k$ is then defined as the *binomial proportion*—the fraction of facets within the domain that return compliant:

$$
\boxed{S_k = \frac{Y_k}{n_k} = \frac{1}{n_k} \sum_{j=1}^{n_k} X_{k,j}}
$$

This proportion is a sufficient statistic for $p_k$ and constitutes the maximum likelihood estimator of the underlying domain compliance probability (Casella & Berger, 2002). Its expectation and variance are:

$$
\mathbb{E}[S_k] = p_k, \quad \text{Var}(S_k) = \frac{p_k(1 - p_k)}{n_k}
$$

The variance of the domain trust score is inversely proportional to the number of facets $n_k$. This has a critical operational implication: domains with *more* constituent facets produce *more precise* trust scores. The Identity domain, with four facets, has a minimum variance of $\frac{p_i(1-p_i)}{4}$, while the Device domain, with five facets, achieves a tighter variance of $\frac{p_d(1-p_d)}{5}$. This precision differential is automatically captured by our variance-based dynamic weighting mechanism ($W_d = \frac{1}{1 + \alpha \cdot \sigma_k^2}$), which rewards domains with lower variance (more facets, more precision) with higher evidential weights in the Dempster-Shafer fusion pipeline.

### 3.2 The Heterogeneous Case: Poisson-Binomial Generalization

In operational deployments, the assumption of a common compliance probability $p_k$ across all facets within a domain is unrealistic. A user's MFA completion probability ($p_{i,1} \approx 0.99$) may be substantially higher than their behavioral biometric match probability ($p_{i,4} \approx 0.85$). When facets have heterogeneous success probabilities $p_{k,1}, p_{k,2}, \ldots, p_{k,n_k}$, the sum $Y_k = \sum_{j=1}^{n_k} X_{k,j}$ follows the **Poisson-Binomial distribution** (Wang, 1993; Hong, 2013):

$$
Y_k \sim \text{Poisson-Binomial}(p_{k,1}, p_{k,2}, \ldots, p_{k,n_k})
$$

The Poisson-Binomial distribution generalizes the Binomial by allowing each trial to have its own success probability. Its mean and variance are:

$$
\mathbb{E}[Y_k] = \sum_{j=1}^{n_k} p_{k,j}, \quad \text{Var}(Y_k) = \sum_{j=1}^{n_k} p_{k,j}(1 - p_{k,j})
$$

The domain trust score under the heterogeneous model becomes:

$$
S_k = \frac{Y_k}{n_k} = \frac{1}{n_k} \sum_{j=1}^{n_k} X_{k,j}
$$

with:

$$
\mathbb{E}[S_k] = \frac{1}{n_k} \sum_{j=1}^{n_k} p_{k,j} = \bar{p}_k, \quad \text{Var}(S_k) = \frac{1}{n_k^2} \sum_{j=1}^{n_k} p_{k,j}(1 - p_{k,j})
$$

where $\bar{p}_k$ is the average facet compliance probability within domain $k$. Under the Poisson-Binomial model, $\text{Var}(S_k) \leq \frac{\bar{p}_k(1 - \bar{p}_k)}{n_k}$, with equality holding only in the homogeneous case. This means that heterogeneous facet probabilities *reduce* domain-level variance relative to the homogeneous Binomial—a beneficial property, because it implies that diversifying the types of checks within a domain (mixing high-confidence checks like MFA with lower-confidence checks like behavioral biometrics) produces *more stable* domain scores than relying on multiple checks of identical reliability (Johnson et al., 2005).

### 3.3 Weighted Facet Aggregation

In practice, not all facets within a domain carry equal security significance. The failure of hardware attestation ($X_{d,4} = 0$) represents a more severe compromise than the absence of disk encryption ($X_{d,3} = 0$). To accommodate this operational reality, the domain trust score can be computed as a *weighted* binomial proportion:

$$
S_k = \frac{\sum_{j=1}^{n_k} w_{k,j} \cdot X_{k,j}}{\sum_{j=1}^{n_k} w_{k,j}}
$$

where $w_{k,j} > 0$ is the policy-defined importance weight of facet $j$ within domain $k$. The weighted formulation preserves the $S_k \in [0, 1]$ constraint and remains a function of independent Bernoulli observations. Its variance is:

$$
\text{Var}(S_k) = \frac{\sum_{j=1}^{n_k} w_{k,j}^2 \cdot p_{k,j}(1 - p_{k,j})}{\left(\sum_{j=1}^{n_k} w_{k,j}\right)^2}
$$

This weighted variance directly feeds the dynamic weighting mechanism in the Dempster-Shafer pipeline: domains where high-weight facets exhibit instability (high $p_{k,j}(1 - p_{k,j})$) will produce elevated $\sigma_k^2$, triggering proportional weight suppression through $W_d = \frac{1}{1 + \alpha \cdot \sigma_k^2}$ (Jøsang, 2016).

---

## 4. Stage 3: Composite Trust as a Nested Binomial Structure

### 4.1 The Nesting Architecture

With four independent domains, each producing a binomial proportion $S_k$, the composite trust evaluation faces a second-tier aggregation problem: how to combine four domain-level proportions into a single composite trust value. This creates a **nested binomial** structure—a hierarchical model in which the first level of aggregation (facets → domain scores) is itself embedded within a second level of aggregation (domain scores → composite trust).

The nesting is formalized as follows. Let each domain $k \in \{i, d, n, a\}$ produce a domain trust score $S_k$ that is itself a binomial proportion derived from $n_k$ independent Bernoulli facets. The composite trust score $S_{\text{composite}}$ is then a function of these four binomial proportions:

$$
\boxed{S_{\text{composite}} = g(S_i, S_d, S_n, S_a) = \sum_{k \in \{i,d,n,a\}} W_k \cdot S_k}
$$

where $W_k$ are the normalized dynamic weights satisfying $\sum_k W_k = 1$. This weighted sum of binomial proportions constitutes the *nested binomial* composite—a second-level binomial-like aggregation operating on the outputs of four first-level binomial processes.

### 4.2 Distributional Properties of the Nested Composite

Since $S_k = Y_k / n_k$ where $Y_k \sim \text{Binomial}(n_k, p_k)$, and the four domains are independent (each domain's telemetry is collected from physically and logically independent sensor subsystems), the composite score $S_{\text{composite}}$ is a weighted sum of independent binomial proportions. Its moments are:

**Expected Value:**

$$
\mathbb{E}[S_{\text{composite}}] = \sum_{k} W_k \cdot \mathbb{E}[S_k] = \sum_{k} W_k \cdot p_k
$$

This confirms that the expected composite trust is the weighted average of the underlying domain compliance probabilities, with weights determined by the variance-based dynamic weighting mechanism.

**Variance:**

$$
\text{Var}(S_{\text{composite}}) = \sum_{k} W_k^2 \cdot \text{Var}(S_k) = \sum_{k} W_k^2 \cdot \frac{p_k(1 - p_k)}{n_k}
$$

The composite variance inherits a double attenuation structure:
1. **First attenuation** (within-domain): Each domain's variance is reduced by the factor $1/n_k$ from the binomial aggregation of $n_k$ facets. Domains with more facets contribute more precise scores.
2. **Second attenuation** (cross-domain): The squared weights $W_k^2$ further attenuate each domain's contribution to composite variance. Because $W_k < 1$ and $W_k^2 < W_k$, the weighting operation *compresses* variance. This is a direct consequence of the diversification principle: combining multiple independent information sources always reduces the variance of the aggregate estimate relative to any individual source (Markowitz, 1952; Clemen & Winkler, 1999).

### 4.3 The Variance Cascade: From Facets to Fusion

The full variance decomposition through the nested hierarchy reveals a three-stage cascade:

**Stage 1 — Facet-Level Variance (Bernoulli):**
$$
\text{Var}(X_{k,j}) = p_{k,j}(1 - p_{k,j}) \leq 0.25
$$

The maximum variance of a Bernoulli trial ($0.25$, achieved at $p = 0.5$) establishes the upper bound on individual facet uncertainty. Facets with very high ($p \approx 1$) or very low ($p \approx 0$) compliance probabilities contribute minimal variance.

**Stage 2 — Domain-Level Variance (Binomial Proportion):**
$$
\text{Var}(S_k) = \frac{p_k(1 - p_k)}{n_k} \leq \frac{0.25}{n_k}
$$

The binomial aggregation attenuates facet variance by $1/n_k$. For the Device domain with $n_d = 5$ facets, the maximum domain variance is $0.05$—a five-fold reduction from the facet level.

**Stage 3 — Composite-Level Variance (Nested Binomial):**
$$
\text{Var}(S_{\text{composite}}) = \sum_{k} W_k^2 \cdot \frac{p_k(1 - p_k)}{n_k} \leq \frac{0.25}{n_{\min}} \cdot \sum_k W_k^2
$$

Since $\sum_k W_k = 1$ and $W_k \leq 1$, we have $\sum_k W_k^2 \leq 1$ (with equality only if all weight concentrates on a single domain). For approximately equal weights ($W_k \approx 0.25$ for $K = 4$ domains), $\sum_k W_k^2 \approx 0.0625$, yielding a composite variance upper bound of approximately $\frac{0.25}{n_{\min}} \times 0.0625 = \frac{0.0156}{n_{\min}}$—an order-of-magnitude reduction from the domain level.

This variance cascade demonstrates that the nested binomial architecture is inherently *self-stabilizing*: the more facets per domain and the more domains in the fusion, the more precise the composite trust estimate becomes. This analytical property directly justifies the architectural decision to evaluate trust across four independent multi-faceted domains rather than relying on a single aggregated metric.

### 4.4 Connection to the Dempster-Shafer Mass Function

The nested binomial composite score $S_{\text{composite}}$ serves as the input to the Dempster-Shafer mass function construction described in Chapter Four. Specifically, when the trust evaluation engine constructs mass functions for each domain via discounting:

$$
m_k(\{Safe\}) = S_k \cdot W_k, \quad m_k(\{Unsafe\}) = (1 - S_k) \cdot W_k, \quad m_k(\Theta) = 1 - W_k
$$

the domain score $S_k$ that enters this construction is understood as a binomial proportion derived from $n_k$ independent Bernoulli facets. The *weight* $W_k$ that modulates the committed evidence is computed from the *variance* of $S_k$ over the sliding observation window—and that variance, as shown above, is governed by the binomial variance $p_k(1 - p_k)/n_k$.

This creates a mathematically elegant circuit: the Bernoulli facets generate binomial proportions $S_k$; the binomial variance $\sigma_k^2$ governs the dynamic weight $W_k = \frac{1}{1 + \alpha \cdot \sigma_k^2}$; and the weight modulates how much of the binomial proportion is committed as Dempster-Shafer mass versus reserved as epistemic uncertainty. Domains with high facet consistency ($\sigma_k^2 \approx 0$) receive $W_k \approx 1$, committing nearly all their binomial proportion as evidential mass. Domains with erratic facets ($\sigma_k^2 \gg 0$) receive $W_k \approx 0$, collapsing their contribution to vacuous uncertainty ($m_k(\Theta) \approx 1$).

---

## 5. Stage 4: Bayesian Conjugacy and the Beta-Binomial Prior

### 5.1 The Beta Distribution as a Natural Prior for Facet Probabilities

While the frequentist treatment above computes $S_k$ as a direct sample proportion, a fully Bayesian treatment of the Bernoulli-Binomial hierarchy introduces the **Beta distribution** as the conjugate prior for the facet compliance probability $p_{k,j}$ (Gelman et al., 2013). The conjugacy structure is:

$$
p_{k,j} \sim \text{Beta}(\alpha_0, \beta_0) \quad \text{(prior)}
$$

$$
X_{k,j} \mid p_{k,j} \sim \text{Bernoulli}(p_{k,j}) \quad \text{(likelihood)}
$$

$$
p_{k,j} \mid X_{k,j} \sim \text{Beta}(\alpha_0 + X_{k,j}, \; \beta_0 + 1 - X_{k,j}) \quad \text{(posterior)}
$$

After observing $N$ evaluation epochs with $s$ successes (compliant outcomes) and $f = N - s$ failures, the posterior becomes:

$$
p_{k,j} \mid \text{data} \sim \text{Beta}(\alpha_0 + s, \; \beta_0 + f)
$$

The posterior mean provides a Bayesian point estimate of the facet compliance probability:

$$
\hat{p}_{k,j}^{\text{Bayes}} = \frac{\alpha_0 + s}{\alpha_0 + \beta_0 + N}
$$

This Bayesian estimate exhibits *shrinkage* toward the prior mean $\frac{\alpha_0}{\alpha_0 + \beta_0}$, preventing extreme estimates when data is sparse. This is directly relevant to the convergence dynamics of our trust architecture during the initialization phase ($t < N$, where $N$ is the sliding window length). During initialization, the variance estimates are statistically immature; the Beta prior provides a principled mechanism for regularizing facet probability estimates until sufficient observations accumulate—exactly the behavior our architecture requires during the "naïve assessment" phase described in the Ensemble model's convergence analysis (Jøsang, 2016; Mui et al., 2002).

### 5.2 The Beta-Binomial Compound Distribution

When facet probabilities are themselves uncertain (governed by a Beta prior that has not yet converged), the predictive distribution of the number of compliant facets within a domain follows the **Beta-Binomial compound distribution**:

$$
P(Y_k = y \mid \alpha_0, \beta_0) = \binom{n_k}{y} \frac{B(\alpha_0 + y, \; \beta_0 + n_k - y)}{B(\alpha_0, \beta_0)}
$$

where $B(\cdot, \cdot)$ is the Beta function. The Beta-Binomial is *overdispersed* relative to the Binomial—it has higher variance because it accounts for the additional uncertainty in the probability parameter itself:

$$
\text{Var}_{\text{BB}}(Y_k) = n_k \cdot \frac{\alpha_0 \beta_0 (\alpha_0 + \beta_0 + n_k)}{(\alpha_0 + \beta_0)^2 (\alpha_0 + \beta_0 + 1)}
$$

This overdispersion is operationally significant: during the initialization phase of a session, the trust engine has not yet established a reliable estimate of each facet's compliance probability. The Beta-Binomial model captures this *parameter uncertainty* and propagates it through the domain score to the composite trust, resulting in wider confidence intervals—exactly the conservative behavior a zero-trust system should exhibit when it has insufficient historical data. As observations accumulate, the posterior concentrates ($\alpha_0 + s$ and $\beta_0 + f$ grow), the Beta-Binomial converges to the Binomial, and the trust estimates tighten (Gelman et al., 2013).

---

## 6. Stage 5: The Full Nested Architecture — Formal Statement

### 6.1 Two-Level Hierarchical Model

The complete nested binomial trust architecture is formally stated as the following two-level hierarchical model:

**Level 1 (Facet → Domain):**
For each domain $k \in \{i, d, n, a\}$ with $n_k$ facets:

$$
X_{k,j} \mid p_{k,j} \stackrel{\text{ind}}{\sim} \text{Bernoulli}(p_{k,j}), \quad j = 1, \ldots, n_k
$$

$$
S_k = \frac{1}{n_k} \sum_{j=1}^{n_k} X_{k,j} \sim \frac{1}{n_k} \text{Binomial}(n_k, \bar{p}_k) \quad \text{(homogeneous approximation)}
$$

**Level 2 (Domain → Composite):**

$$
S_{\text{composite}} = \sum_{k \in \{i,d,n,a\}} W_k \cdot S_k = \sum_k W_k \cdot \frac{Y_k}{n_k}
$$

where $W_k = \frac{(1 + \alpha \sigma_k^2)^{-1}}{\sum_j (1 + \alpha \sigma_j^2)^{-1}}$ are the variance-normalized dynamic weights.

**Level 3 (Composite → DS Mass → Trust Decision):**

$$
m(\{Safe\}) = S_{\text{composite}} \cdot W_{\text{agg}}, \quad m(\{Unsafe\}) = (1 - S_{\text{composite}}) \cdot W_{\text{agg}}, \quad m(\Theta) = 1 - W_{\text{agg}}
$$

$$
BetP(Safe) = m(\{Safe\}) + \frac{m(\Theta)}{2} \implies \text{Access Decision}
$$

### 6.2 Worked Example: Bernoulli → Binomial → Composite

Consider a single evaluation epoch for an entity connecting via a corporate VPN:

**Level 1 — Identity Domain ($n_i = 4$ facets):**

| Facet | Observation $X_{i,j}$ | $p_{i,j}$ (estimated) |
|:---|:---:|:---:|
| MFA Completion | 1 (pass) | 0.99 |
| Credential Freshness | 1 (valid) | 0.95 |
| Role Authorization | 1 (match) | 0.98 |
| Behavioral Biometric | 0 (mismatch) | 0.82 |

$$
Y_i = 1 + 1 + 1 + 0 = 3, \quad S_i = \frac{3}{4} = 0.75
$$

**Level 1 — Device Domain ($n_d = 5$ facets):**

| Facet | Observation $X_{d,j}$ | $p_{d,j}$ (estimated) |
|:---|:---:|:---:|
| Patch Currency | 1 | 0.90 |
| Endpoint Protection | 1 | 0.97 |
| Disk Encryption | 1 | 0.99 |
| Hardware Attestation | 1 | 0.95 |
| Jailbreak/Root Status | 1 | 0.98 |

$$
Y_d = 5, \quad S_d = \frac{5}{5} = 1.00
$$

**Level 2 — Composite Trust (assuming equal weights $W_k = 0.25$):**

$$
S_{\text{composite}} = 0.25(0.75) + 0.25(1.00) + 0.25(S_n) + 0.25(S_a)
$$

If $S_n = 0.67$ (2 of 3 network facets compliant) and $S_a = 1.00$ (3 of 3 application facets compliant):

$$
S_{\text{composite}} = 0.25(0.75 + 1.00 + 0.67 + 1.00) = 0.25 \times 3.42 = 0.855
$$

This composite score of $0.855$—derived entirely from the nested aggregation of 16 individual Bernoulli facet checks—enters the Dempster-Shafer pipeline as the input to mass function construction. The Identity domain's score of $0.75$ (caused by the single biometric mismatch) would also exhibit higher rolling variance ($\sigma_i^2$) if such mismatches are intermittent, triggering the dynamic weighting mechanism to reduce the Identity domain's influence on the fused output.

---

## 7. Statistical Properties and Operational Implications

### 7.1 Central Limit Theorem Approximation

By the Central Limit Theorem, for domains with a sufficiently large number of facets, the domain trust score $S_k$ is approximately normally distributed:

$$
S_k \xrightarrow{d} \mathcal{N}\left(p_k, \frac{p_k(1-p_k)}{n_k}\right) \quad \text{as } n_k \rightarrow \infty
$$

For $n_k \geq 5$ (satisfied by the Device domain), the normal approximation provides a practical mechanism for constructing confidence intervals around the domain trust score without computing exact binomial probabilities. A 95% confidence interval for the true compliance probability $p_k$ is:

$$
S_k \pm 1.96 \sqrt{\frac{S_k(1 - S_k)}{n_k}}
$$

These confidence intervals can be propagated through the nested hierarchy to quantify the uncertainty at the composite level—providing an alternative uncertainty metric that complements the Dempster-Shafer $m(\Theta)$ term (Agresti & Coull, 1998).

### 7.2 Sensitivity to Individual Facet Failures

The nested binomial structure exhibits a natural sensitivity gradient: the impact of a single facet failure ($X_{k,j} = 0$) on the composite trust score depends on both the number of facets in the affected domain and the weight of that domain:

$$
\Delta S_{\text{composite}} = -\frac{W_k}{n_k}
$$

For the Identity domain ($n_i = 4$, $W_i = 0.25$): $\Delta S = -0.0625$ per failed facet.
For the Device domain ($n_d = 5$, $W_d = 0.25$): $\Delta S = -0.05$ per failed facet.

Domains with fewer facets are *more sensitive* to individual failures—a single Identity facet failure produces a larger trust score drop than a single Device facet failure. This structural property incentivizes the architect to include more independent facets in critical domains, improving both precision (lower variance) and resilience (lower per-facet impact).

### 7.3 Monotone Likelihood Ratio and Trust Ordering

The Binomial distribution satisfies the *monotone likelihood ratio* (MLR) property: if $p_1 > p_2$, then the likelihood ratio $\frac{P(Y = y \mid p_1)}{P(Y = y \mid p_2)}$ is non-decreasing in $y$ (Casella & Berger, 2002). This guarantees that higher observed compliance counts $Y_k$ constitute *stronger evidence* for higher underlying compliance probabilities, creating a mathematically rigorous trust ordering. The MLR property ensures that the domain trust score $S_k$ is a sufficient statistic for the access decision—no additional information from the individual facet outcomes can improve the decision beyond what $S_k$ already captures.

---

## 8. Conclusion: The Probabilistic Integrity of the Trust Pipeline

The nested Bernoulli-Binomial architecture establishes that the trust evaluation pipeline of this thesis operates on a probabilistically sound foundation. Individual facet checks, being inherently binary, are naturally modeled as Bernoulli trials. The aggregation of multiple independent facets within each domain produces binomial proportions with well-characterized variance that decreases with the number of facets—rewarding architectural breadth with statistical precision. The second-level aggregation across domains creates a nested binomial composite whose variance is doubly attenuated: first by within-domain facet counts, then by cross-domain weight diversification.

This hierarchical structure connects seamlessly to the Dempster-Shafer fusion pipeline: the binomial variance of domain scores governs the dynamic weights, which in turn determine the allocation of evidential mass between committed belief ($m(\{Safe\})$, $m(\{Unsafe\})$) and epistemic uncertainty ($m(\Theta)$). The result is a trust computation architecture in which every layer—from the individual Bernoulli facet check through the nested binomial composite to the final Pignistic access decision—is governed by a coherent, analytically tractable probabilistic framework.

---

## References

Agresti, A., & Coull, B. A. (1998). Approximate is better than "exact" for interval estimation of binomial proportions. *The American Statistician, 52*(2), 119–126. https://doi.org/10.1080/00031305.1998.10480550

Blitzstein, J. K., & Hwang, J. (2019). *Introduction to probability* (2nd ed.). CRC Press/Chapman & Hall.

Casella, G., & Berger, R. L. (2002). *Statistical inference* (2nd ed.). Duxbury/Thomson Learning.

Clemen, R. T., & Winkler, R. L. (1999). Combining probability distributions from experts in risk analysis. *Risk Analysis, 19*(2), 187–203. https://doi.org/10.1111/j.1539-6924.1999.tb00399.x

Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013). *Bayesian data analysis* (3rd ed.). Chapman & Hall/CRC.

Grassi, P. A., Fenton, J. L., Newton, E. M., Perlner, R. A., Regenscheid, A. R., Burr, W. E., & Richer, J. P. (2017). *Digital identity guidelines: Authentication and lifecycle management* (NIST Special Publication 800-63B). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-63b

Hong, Y. (2013). On computing the distribution function for the Poisson binomial distribution. *Computational Statistics & Data Analysis, 59*, 41–51. https://doi.org/10.1016/j.csda.2012.10.006

Johnson, N. L., Kemp, A. W., & Kotz, S. (2005). *Univariate discrete distributions* (3rd ed.). John Wiley & Sons.

Jøsang, A. (2016). *Subjective logic: A formalism for reasoning under uncertainty*. Springer. https://doi.org/10.1007/978-3-319-42337-1

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance, 7*(1), 77–91. https://doi.org/10.2307/2975974

Mui, L., Mohtashemi, M., & Halberstadt, A. (2002). A computational model of trust and reputation. *Proceedings of the 35th Annual Hawaii International Conference on System Sciences*, 2431–2439. https://doi.org/10.1109/HICSS.2002.994181

National Institute of Standards and Technology. (2020). *Zero trust architecture* (NIST Special Publication 800-207). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-207

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology.

Wang, Y. H. (1993). On the number of successes in independent trials. *Statistica Sinica, 3*(2), 295–312.
