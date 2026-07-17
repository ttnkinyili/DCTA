# Temporal + Beyond the Perimeter: Combination Analysis and Task Summary

---

# Part I: Combination Analysis

## 1. Context: The Three-Paper Landscape

Following the previous merger, the papers directory now contains:

| Paper | Type | Core Contribution |
|:---|:---|:---|
| paper_variance_weighting_beyond_the_perimeter.md | **Already combined** | Five-paradigm critique → variance-based DS weighting (spatial dimension) |
| paper_beyond_the_perimeter.md | Literature review | Five-paradigm critical analysis → DCTA as resolution |
| paper_trust_decay_temporal.md | Research article | Temporal trust decay: exponential discounting, dual sliding windows, session lifecycle, hysteresis |

The critical constraint: **the combined paper must not repeat content already covered in `paper_variance_weighting_beyond_the_perimeter.md`**.

---

## 2. Assessment: Is Combining These Two Papers Apt?

### 2.1 Verdict: **Yes — combining is appropriate, but the angle must be sharply differentiated**

The combination is viable and advisable for the following reasons:

### 2.2 Shared Infrastructure (Why They Belong Together)

| Dimension | Beyond the Perimeter | Trust Decay Temporal |
|:---|:---|:---|
| **Central problem** | Implicit trust period across 5 paradigms | Implicit trust period as a temporal vulnerability |
| **DS framework** | DS fusion with binary frame $\Theta = \{\text{Safe}, \text{Unsafe}\}$ | DS evidence discounting with same binary frame |
| **Temporal decay formula** | $D(t) = e^{-\lambda t/T}$ in §7.2.3 | $\alpha(t) = e^{-\lambda t/T}$ — **identical** |
| **Dual-window architecture** | 30-min short / 48-hr long mentioned in §7.2.3 | Full formal treatment of both windows (§V) |
| **Pignistic transformation** | BetP(Safe) with Full/Limited/No thresholds in §7.2.4 | Same thresholds with hysteresis (§VII) |
| **Testbed** | References companion testbed validation | Same Mininet/OVS/ODL testbed, 6 scenarios, 50 runs |
| **Limitation overlap** | Binary frame, stable-but-false attack, hardware attestation | Same limitations acknowledged |

### 2.3 Unique Contributions (Why the Temporal Paper Adds Value)

The Trust Decay paper contributes material that is **not present** in the already-combined variance paper:

| Unique to Trust Decay Paper | Present in Variance-BtP Combined Paper? |
|:---|:---:|
| **Formal linear vs. exponential decay comparison** (§III) — residual weight table, 78% reduction proof | No — Only mentions exponential decay briefly in §IV-E |
| **DS evidence discounting operator** $m_\alpha(A) = \alpha(t) \cdot m(A)$ with BPA axiom verification (§IV) | No — Not covered at all |
| **Dual sliding-window architecture** with forgetting factor analysis (§V) | No — Mentioned in one paragraph (§IV-E), not formalised |
| **Three-phase session lifecycle** — Initialisation → Handover → Maturity (§VI) | No — Not covered |
| **Hysteresis mechanism** with asymmetric margins $\delta_{\text{up}} = 0.03$, $\delta_{\text{down}} = 0.02$ (§VII-B) | No — Not covered |
| **Dynamic threshold calibration** based on threat intelligence (§VII-C) | No — Not covered |
| **Effective session length comparison** across 4 decay models (Table IX) | No — Not covered |
| **False revocation rate** — 89.9% (pure exponential) → 2.0% (ensemble) (Table XI) | No — Not covered |
| **Ablation study** decomposing decay + inertia + hysteresis (Table XIIa) | No — Different ablation (variance + DS) |
| **Sensitivity analysis** across $\lambda \in \{1, 2, 3, 5, 7\}$ (Table XIIb) | No — Sensitivity is across $\alpha$, not $\lambda$ |
| **Security-usability paradox resolution** — formal demonstration | No — Not addressed |
| **Clock synchronisation** requirement discussion | No — Not discussed |

### 2.4 Content That Must Be Excluded (Already in the Variance-BtP Paper)

The following content from `paper_beyond_the_perimeter.md` is **already fully covered** in the combined variance paper and must NOT be repeated:

| Content Block | Already in Variance-BtP Paper |
|:---|:---:|
| Five-paradigm critical analysis (§2–6) | Yes — Condensed in §II |
| Unified failure mapping (Table 1) | Yes — Table I |
| Variance weighting formula $w_d = 1/(1+\alpha\sigma_d^2)$ | Yes — §IV-A |
| DS combination rule derivation | Yes — §IV-D |
| Multi-domain telemetry architecture (4 domains) | Yes — §IV-B, Table V |
| Pignistic transformation + three-tier thresholds | Yes — §IV-D |
| Anti-spoofing property via variance coupling | Yes — §IV-F Property 2 |
| Architectural integration table (Table 3/VIII) | Yes — §IV-G, Table VIII |

---

## 3. Differentiation Strategy

The combined paper must occupy a **distinct niche** from the variance-BtP paper:

| Paper | Focus | Central Question |
|:---|:---|:---|
| **Variance-Weighting BtP** | *Spatial* dimension: How to weight and fuse evidence from multiple domains at any instant | "Which evidence should we trust right now?" |
| **Temporal-Decay Continuous BtP** (new) | *Temporal* dimension: How evidence value depreciates over time and how sessions evolve | "How long should we trust evidence, and what replaces it?" |

> **IMPORTANT**: The framing must be: "Where the companion paper [ref] addresses the *spatial* question of which domain evidence to trust at each evaluation instant, this paper addresses the *temporal* question of how that evidence ages, how sessions transition from identity-based to behaviour-based trust, and how access decisions resist oscillation."

---

## 4. Structural Plan for the Combined Paper

```
Title: "Temporal Decay as Continuous Verification Beyond Static Sessions:
        Exponential Discounting, Dual Sliding Windows, and Graduated 
        Thresholds for Zero Trust in Heterogeneous Networks"

I. Introduction
   - The implicit trust period problem (condensed from BtP §1, 
     ~500 words — avoid repeating the 5-paradigm deep dive)
   - The temporal paradox: aggressive decay is necessary but 
     operationally destructive (from TDT §III-D)
   - Explicit differentiation from the spatial/variance companion paper
   - Research questions (RQ1–RQ3 from TDT)
   - Contributions

II. The Temporal Trust Gap in Current Paradigms
   - NOT a re-analysis of the 5 paradigms — just the temporal 
     dimension extracted from each (~1,500 words total):
     § Perimeter: VPN temporal passport persists indefinitely
     § RBAC: authenticate-once-access-forever
     § NIST: temporal dynamics left unspecified
     § SDP: post-authentication silence (SPA point-in-time)
     § AI-IDS/SDN: detection-enforcement temporal gap
   - Unified temporal failure mapping (new table — 
     temporal-specific, not the full paradigm table)

III. Background and Related Work
   - EWMA in signal processing (from TDT §II-A)
   - Bayesian evidence discounting (from TDT §II-B)
   - DS discounting (from TDT §II-C)
   - Existing temporal trust models (from TDT §II-D)
   - Identified temporal gap (from TDT §II-E)

IV. Linear vs. Exponential Decay: Formal Comparison
   - Mathematical definitions (from TDT §III)
   - Residual weight comparison table (Table I from TDT)
   - Architectural implications (Table II from TDT)
   - The pure-decay paradox (from TDT §III-D)

V. DS Evidence Discounting with Exponential Decay
   - The discounting mechanism: m_alpha(A) = alpha(t) * m(A) 
     (from TDT §IV)
   - BPA axiom verification
   - Worked example with temporal evolution table
   - Interaction with Dempster's combination rule
   - NOTE: Cross-reference the companion paper for the spatial 
     fusion mechanics, do NOT re-derive DS combination rule

VI. Dual Sliding-Window Architecture
   - Dual-horizon design (from TDT §V-A)
   - Forgetting factor implementation (from TDT §V-B)
   - Freshness-inertia ensemble formula (from TDT §V-C)

VII. Three-Phase Session Lifecycle
   - Initialisation -> Handover -> Maturity (from TDT §VI)
   - Phase summary table

VIII. Trust Thresholds and Decision Architecture
   - Graduated three-tier access (from TDT §VII-A)
   - Hysteresis mechanism (from TDT §VII-B)
   - Dynamic calibration (from TDT §VII-C)
   - NOTE: Reference the companion paper for how the spatial 
     trust score Psi is computed; this paper governs how 
     Psi evolves over time and maps to decisions

IX. Experimental Evaluation
   - Setup (testbed, same 6 scenarios)
   - Effective session length comparison (Table IX from TDT)
   - Trust score trajectories (Table X from TDT)
   - False revocation rate (Table XI from TDT)
   - Hysteresis effectiveness
   - Ablation study (Table XIIa from TDT)
   - Sensitivity to lambda (Table XIIb from TDT)

X. Discussion
   - Security-usability resolution
   - Parameter guidance (Table XIII from TDT)
   - Clock synchronisation
   - Limitations

XI. Conclusion and Future Work
```

### 4.1 Key Editing Principles

1. **Condense the paradigm analysis to temporal aspects only** — The BtP paper's §2–6 covers five paradigms in ~9,000 words with full structural analysis. The variance-BtP paper already condensed this to ~3,500 words. This new paper should extract ONLY the temporal dimension (~1,500 words) — each paradigm gets 2–3 sentences focused on its temporal failure.

2. **Do NOT re-derive shared mathematical apparatus** — The DS combination rule, variance weighting formula, Pignistic transformation, and multi-domain telemetry are already in the variance-BtP paper. Cross-reference them.

3. **DO preserve the temporal-specific mathematics** — The DS discounting operator ($m_\alpha$), the dual-window ensemble formula, the forgetting factor, the hysteresis margins, and the linear-vs-exponential comparison are all unique to the temporal paper and must be retained in full.

4. **DO preserve all temporal experimental results** — The effective session length, false revocation rate, trust trajectories, temporal ablation, and lambda sensitivity are distinct from the variance paper's alpha sensitivity and FPR results.

5. **Explicit cross-referencing** — At key junctures, cite the companion variance-BtP paper for spatial fusion details: "The spatial trust score Psi is computed via variance-weighted DS fusion as detailed in [companion ref]; this paper addresses how Psi evolves temporally."

### 4.2 Target Length

- Beyond the Perimeter (temporal-relevant content): ~3,000 words extractable
- Trust Decay Temporal: ~8,500 words of unique content  
- Target merged length: ~8,000–9,000 words (condensing BtP temporal content, retaining TDT in near-full)
- Appropriate for a journal article

---

## 5. Risk Assessment

| Risk | Mitigation |
|:---|:---|
| Content overlap with variance-BtP paper | Explicit cross-referencing; temporal-only paradigm analysis; no re-derivation of shared mathematics |
| Loss of BtP's five-paradigm depth | Temporal dimension is sufficient — the full critique exists in the companion paper |
| Reviewer may flag similarity with companion | The Introduction must explicitly position this as the temporal companion to the spatial paper |
| Self-citation concern | Appropriate — the two papers address orthogonal dimensions (spatial vs. temporal) of the same architecture |

---

## 6. Summary

| Aspect | Assessment |
|:---|:---|
| **Is combining apt?** | Yes — the papers share the same problem diagnosis and DS framework |
| **Is it differentiated from the variance-BtP paper?** | Yes — this paper addresses temporal dynamics exclusively; the other addresses spatial weighting |
| **What makes it a distinct contribution?** | DS evidence discounting, dual sliding windows, three-phase lifecycle, hysteresis — all absent from the companion |
| **What must be excluded?** | Five-paradigm deep analysis, variance weighting formula, DS combination rule derivation, multi-domain telemetry table, anti-spoofing property |
| **Target length** | ~8,000–9,000 words |

---
---

# Part II: Task Summary — What Was Done

## 1. Papers Reviewed

- **paper_beyond_the_perimeter.md** — 427 lines, ~8,700 words (literature review)
- **paper_trust_decay_temporal.md** — 520 lines, ~7,400 words (temporal research)
- **paper_variance_weighting_beyond_the_perimeter.md** — 608 lines, ~7,900 words (already-combined companion)

## 2. Combination Analysis Produced

Key findings:
- Combining is **appropriate** — the papers share the same problem diagnosis and DS framework
- Must be **sharply differentiated** from the companion variance-BtP paper
- Framing: variance paper = *spatial* dimension ("which evidence to trust") vs. temporal paper = *temporal* dimension ("how long to trust evidence")
- 12 unique contributions in the temporal paper that are absent from the companion

## 3. Combined Paper Created

- **paper_temporal_decay_continuous_beyond_static.md** — 541 lines, ~6,500 words

## 4. How the Papers Were Combined

| Section | Source | Treatment |
|:---|:---|:---|
| Introduction (§I) | Both | BtP implicit trust problem condensed to ~500 words; temporal paradox from TDT §III-D; explicit companion paper differentiation |
| Temporal Trust Gap (§II) | BtP §2–6 | **Temporal dimension only** — each paradigm gets 2–3 sentences on its temporal failure, NOT a full structural analysis (~1,500 words vs. BtP's ~9,000) |
| Related Work (§III) | TDT §II | Retained: EWMA, Bayesian discounting, DS discounting, existing models, gap |
| Linear vs. Exponential (§IV) | TDT §III | Retained in full — unique to temporal paper |
| DS Evidence Discounting (§V) | TDT §IV | Retained in full with cross-reference to companion for spatial fusion |
| Dual Sliding Windows (§VI) | TDT §V | Retained in full |
| Session Lifecycle (§VII) | TDT §VI | Retained in full |
| Thresholds + Hysteresis (§VIII) | TDT §VII | Retained in full |
| Experiments (§IX) | TDT §VIII | Retained in full (session length, trajectories, FPR, ablation, λ sensitivity) |
| Discussion (§X) | Both | TDT discussion + BtP temporal implications merged |
| References | Both | 33 references, de-duplicated, IEEE numbered format |

## 5. Content Exclusion (Avoiding Overlap with Companion Paper)

The following content was deliberately **excluded** because it already appears in the variance-BtP combined paper:

| Excluded Content | Where It Already Exists |
|:---|:---|
| Five-paradigm full structural analysis | Companion §II (~3,500 words) |
| Variance weighting formula $w_d = 1/(1+\alpha\sigma^2)$ | Companion §IV-A |
| DS combination rule derivation | Companion §IV-D |
| Multi-domain telemetry architecture table | Companion Table V |
| Pignistic transformation derivation | Companion §IV-D |
| Anti-spoofing / self-calibration properties | Companion §IV-F |
| Architectural integration table | Companion Table VIII |
| Spatial ablation study (variance + DS) | Companion Table XIII |
| α sensitivity analysis | Companion Table XIV |

## 6. Key Metrics

| Metric | Original (2 papers) | Combined | Companion Paper |
|:---|:---:|:---:|:---:|
| **Total words** | ~16,100 | ~6,500 | ~7,900 |
| **Reduction** | — | **60%** | — |
| **Tables** | ~18 (with overlap) | 15 (unique) | 16 (unique) |
| **References** | ~38 (with overlap) | 33 | 50 |
| **Content overlap with companion** | N/A | **None** | N/A |

## 7. Differentiation Between the Two Combined Papers

| Dimension | Variance-BtP Paper | Temporal-BtP Paper |
|:---|:---|:---|
| **Central question** | Which evidence to trust? | How long to trust evidence? |
| **Mathematical core** | $w_d = 1/(1+\alpha\sigma^2)$ + DS combination rule | $\alpha(t) = e^{-\lambda t}$ + DS discounting operator |
| **Architecture** | Multi-domain telemetry + variance-weighted mass construction | Dual sliding windows + session lifecycle + hysteresis |
| **Key parameter** | $\alpha$ (variance penalty) | $\lambda$ (decay rate) |
| **Paradigm analysis** | Full structural critique (~3,500 words) | Temporal dimension only (~1,500 words) |
| **Experimental focus** | Classification accuracy, FPR, latency, conflict detection | Session length, trust trajectories, false revocation, containment speed |
