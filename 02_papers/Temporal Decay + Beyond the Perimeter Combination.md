# Walkthrough: Temporal Decay + Beyond the Perimeter Combination

## What Was Done

### 1. Reviewed All Relevant Papers
- [paper_beyond_the_perimeter.md](file:///Users/admin/Desktop/DCTA/02_papers/paper_beyond_the_perimeter.md) — 427 lines, ~8,700 words (literature review)
- [paper_trust_decay_temporal.md](file:///Users/admin/Desktop/DCTA/02_papers/paper_trust_decay_temporal.md) — 520 lines, ~7,400 words (temporal research)
- [paper_variance_weighting_beyond_the_perimeter.md](file:///Users/admin/Desktop/DCTA/02_papers/paper_variance_weighting_beyond_the_perimeter.md) — 608 lines, ~7,900 words (already-combined companion)

### 2. Produced Combination Analysis
- [temporal_combination_analysis.md](file:///Users/admin/.gemini/antigravity-ide/brain/2b3ba090-33e7-4ef5-a2bf-7cfd5adb1f59/temporal_combination_analysis.md)
- Key findings:
  - Combining is **appropriate** — the papers share the same problem diagnosis and DS framework
  - Must be **sharply differentiated** from the companion variance-BtP paper
  - Framing: variance paper = *spatial* dimension ("which evidence to trust") vs. temporal paper = *temporal* dimension ("how long to trust evidence")
  - 12 unique contributions in the temporal paper that are absent from the companion

### 3. Created Combined Paper
- [paper_temporal_decay_continuous_beyond_static.md](file:///Users/admin/Desktop/DCTA/02_papers/paper_temporal_decay_continuous_beyond_static.md) — 541 lines, ~6,500 words

## How the Papers Were Combined

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

## Content Exclusion (Avoiding Overlap with Companion Paper)

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

## Key Metrics

| Metric | Original (2 papers) | Combined | Companion Paper |
|:---|:---:|:---:|:---:|
| **Total words** | ~16,100 | ~6,500 | ~7,900 |
| **Reduction** | — | **60%** | — |
| **Tables** | ~18 (with overlap) | 15 (unique) | 16 (unique) |
| **References** | ~38 (with overlap) | 33 | 50 |
| **Content overlap with companion** | N/A | **None** | N/A |

## Differentiation Between the Two Combined Papers

| Dimension | Variance-BtP Paper | Temporal-BtP Paper |
|:---|:---|:---|
| **Central question** | Which evidence to trust? | How long to trust evidence? |
| **Mathematical core** | $w_d = 1/(1+\alpha\sigma^2)$ + DS combination rule | $\alpha(t) = e^{-\lambda t}$ + DS discounting operator |
| **Architecture** | Multi-domain telemetry + variance-weighted mass construction | Dual sliding windows + session lifecycle + hysteresis |
| **Key parameter** | $\alpha$ (variance penalty) | $\lambda$ (decay rate) |
| **Paradigm analysis** | Full structural critique (~3,500 words) | Temporal dimension only (~1,500 words) |
| **Experimental focus** | Classification accuracy, FPR, latency, conflict detection | Session length, trust trajectories, false revocation, containment speed |
