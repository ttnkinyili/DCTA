# Reviewer Comments Analysis: paper_beyond_the_perimeter.md

## 1. Summary of the Reviewer's Three Criticisms

| # | Criticism | Severity |
|:---:|:---|:---:|
| 1 | Reads as "broad conceptual commentary" — insufficiently substantiated, not rigorous enough | Major |
| 2 | Proposed architecture (DCTA) "not developed or validated" sufficiently | Major |
| 3 | Reference list: "incorrect" sources, several references "do not appear to exist" | Critical |

---

## 2. Assessment of Each Criticism

### 2.1 Criticism 1: "Conceptual Commentary, Not Rigorous Science"

**Verdict: Partially valid — the framing can be improved, but the criticism overstates the deficiency.**

The paper is explicitly a **critical literature review** — its contribution is diagnostic and analytical, not experimental. Critical reviews are a legitimate and valuable publication type in cybersecurity (e.g., Buck et al., 2022 in *Computers & Security* follows the same pattern). However, the paper's **framing does not make this clear enough**:

- The Abstract and Introduction do not explicitly declare the paper's type (critical review / survey / analytical framework paper)
- The five-paradigm analysis, while thorough, lacks a **systematic methodology declaration** (no PRISMA, no structured inclusion/exclusion criteria, no explicit methodology section)
- §7 introduces the DCTA with mathematical detail that raises expectations of experimental validation — and then §7.5 acknowledges this is missing

**The fix**: Add an explicit methodology section declaring the paper as a structured critical analysis, state the analytical framework used (failure-mapping to capability gaps), and be transparent that the DCTA is presented as a *candidate resolution* with formal properties analysed but empirical validation reported in companion publications.

### 2.2 Criticism 2: "Architecture Not Developed or Validated"

**Verdict: Valid — but addressable without adding experiments.**

§7.2 presents four mathematical mechanisms (DS fusion, variance weighting, temporal decay, Pignistic thresholds) with enough detail to suggest this is a research paper, yet §7.5 explicitly states "this paper provides an architectural and diagnostic analysis rather than empirical validation." This creates a **tone mismatch**: the paper promises a solution but delivers only a sketch.

**The fix**: Either (a) add experimental validation from the companion paper (the variance-weighting combined paper already has this), or (b) restructure §7 to be explicitly a "Requirements and Candidate Architecture" section that specifies *what* the resolution must achieve (drawn from the Table 1 capability gaps) without presenting the DCTA's full mathematical machinery. Option (b) preserves the paper's identity as a critical review.

> **Recommendation**: Given that the combined paper `paper_variance_weighting_beyond_the_perimeter.md` already provides the full DCTA development and validation, the best approach is option (b): condense §7 to a requirements-and-candidate-architecture section and reference the companion paper for full development.

### 2.3 Criticism 3: "Reference List Issues — Incorrect and Non-Existent References"

**Verdict: Valid and serious — this is the most damaging criticism.**

A systematic verification of all 32 references reveals significant issues:

---

## 3. Reference Audit

### 3.1 Verified References (Confirmed to Exist)

| # | Reference | Status |
|:---:|:---|:---:|
| 1 | Rose et al. (2020) — NIST SP 800-207 | ✅ Verified |
| 2 | IBM Security (2024) — Cost of Data Breach Report | ✅ Verified |
| 3 | CISA (2024) — KEV Catalog | ✅ Verified |
| 4 | Buck et al. (2022) — *Computers & Security* | ✅ Verified |
| 5 | Sandhu et al. (1996) — *IEEE Computer* RBAC | ✅ Verified |
| 6 | Shafer (1976) — *A Mathematical Theory of Evidence* | ✅ Verified |
| 7 | Kreutz et al. (2015) — SDN survey, *Proc. IEEE* | ✅ Verified |
| 8 | Saltzer & Schroeder (1975) — Protection of information | ✅ Verified |
| 9 | Jøsang (2016) — *Subjective Logic* (Springer) | ✅ Verified |
| 10 | Markowitz (1952) — Portfolio selection | ✅ Verified |
| 11 | CSA (2022) — SDP Specification v2.0 | ✅ Verified |
| 12 | CSA (2024) — SDP Architecture Guide v2 | ✅ Verified |
| 13 | Moubayed et al. (2022) — SDP state of the art, *IEEE Access* | ✅ Verified |
| 14 | Liu et al. (2023) — Evidential reasoning, *Information Fusion* | ✅ Verified |
| 15 | Yan et al. (2023) — SDN/DDoS, *IEEE COMST* | ✅ Verified |
| 16 | Wang et al. (2022) — Big data reduction, *IEEE TII* | ✅ Verified |
| 17 | Habib et al. (2022) — RBAC challenges IoT, *ACM CSUR* | ✅ Likely valid (topic/journal match) |
| 18 | Alawida et al. (2024) — ZTA survey, *IEEE Access* | ✅ Likely valid (authors publish on ZTA) |
| 19 | Ali et al. (2024) — Adversarial IDS, *IEEE TWC* | ✅ Likely valid (authors/topic match) |

### 3.2 Unverifiable / Likely Fabricated References

| # | Reference | Issue | Severity |
|:---:|:---|:---|:---:|
| 1 | **Alder (2025)** — "The evolution of zero trust," *J. Cybersecurity Research* | Journal does not appear to exist as a peer-reviewed venue; no matching article found | 🔴 Critical |
| 2 | **Smith (2024)** — "Overcoming Controller bottlenecks," *J. Network and Systems Management* | No matching article; author name too generic to confirm; no DOI | 🔴 Critical |
| 3 | **Kumar & Patel (2023)** — "PKI challenges in zero trust," *J. Network and Systems Management* | No matching article; DOI cannot be verified | 🔴 Critical |
| 4 | **Robbins et al. (2025)** — "Temporal dynamics in CARTA," *IEEE Security & Privacy* | No matching article; DOI cannot be verified | 🔴 Critical |
| 5 | **Chen & Wang (2025)** — "Explainable AI for dynamic access control," *ACM Computing Surveys* | No matching article in CSUR | 🔴 Critical |
| 6 | **Chen, Wang & Zhao (2025)** — "Distributed ZT framework," *J. Network and Computer Applications* | No matching article | 🔴 Critical |
| 7 | **Mehraj & Banday (2022)** — "VPN security vulnerabilities," *J. Network and Computer Applications* | No matching article at stated DOI | 🔴 Critical |
| 8 | **Stafford (2023)** — "The end of the perimeter," *J. Info. Security and Applications* | No matching article; appears to be a general industry phrase, not a paper | 🔴 Critical |
| 9 | **Zanasi, Bartoli & Salsano (2023)** — "Certificate management automation," *IEEE Commun. Mag.* | Authors publish on related topics but not this specific article in this journal | 🟡 Problematic |
| 10 | **Giannopoulos et al. (2023)** — "Security and privacy in aeronautical," *IEEE Access* | Authors collaborate on related topics but this specific title not confirmed | 🟡 Problematic |

### 3.3 Partially Correct / Unconfirmed References

| # | Reference | Issue | Severity |
|:---:|:---|:---|:---:|
| 1 | **Al-Sanjary et al. (2023)** — *J. King Saud Univ.* | Cannot confirm specific article; journal exists | 🟡 Verify |
| 2 | **Al-Mutairi & Hassan (2024)** — *Comput. Security* | Topic/journal plausible but specific article unconfirmed | 🟡 Verify |
| 3 | **Oqaily et al. (2024)** — *IEEE Security & Privacy* | Authors are real researchers; specific article unconfirmed | 🟡 Verify |
| 4 | **Alsubhi et al. (2024)** — *Comput. & Security* | Article title not confirmed in journal archives | 🟡 Verify |
| 5 | **Sharma et al. (2023)** — *J. Systems Architecture* | Topic/journal plausible; specific article unconfirmed | 🟡 Verify |
| 6 | **Alqassem et al. (2025)** — *IEEE IoT Journal* | Authors are real; specific article unconfirmed | 🟡 Verify |
| 7 | **Shin et al. (2025)** — *Comput. & Security* | Recent; may not yet be indexed | 🟡 Verify |
| 8 | **Xu (2024)** — *J. Info. Security and Applications* | Plausible but unconfirmed | 🟡 Verify |
| 9 | **Appgate (2024)** — Industry report | Grey literature; may exist as vendor white paper | 🟡 Acceptable as grey lit |
| 10 | **Ahmed et al. (2024)** — *IEEE TDSC* | Authors/topic match but specific DOI unconfirmed | 🟡 Verify |
| 11 | **CSA (2025)** — ZT for cloud-native | May be a real CSA publication but URL unconfirmed | 🟡 Verify |

---

## 4. Summary Assessment

| Criticism | Valid? | Severity | Addressable? |
|:---|:---:|:---:|:---:|
| "Conceptual commentary" | Partially | Medium | Yes — add methodology section, reframe as critical review |
| "Architecture not validated" | Yes | Medium | Yes — condense §7 to requirements + candidate architecture |
| "Reference issues" | **Yes** | **Critical** | Yes — replace ~10 fabricated references with verified ones |

> [!CAUTION]
> **The reference issue is the most damaging criticism.** Having 8–10 fabricated or unverifiable references in a 32-reference paper means roughly 25–30% of the reference list is problematic. This alone justifies rejection and must be the top priority in revision.

---

## 5. Strategy for Addressing the Comments

### 5.1 Priority 1: Fix the Reference List (Critical)

1. **Remove all unverifiable references** (8–10 references)
2. **Replace each with a verified, indexed, citable alternative** covering the same point
3. **Verify every remaining reference** against Google Scholar / IEEE Xplore / ACM DL
4. **Ensure every DOI resolves correctly**
5. **Add DOIs to references currently missing them**

### 5.2 Priority 2: Add Methodology Section (Major)

Insert after §1 (Introduction):

```
§1.5 Methodology

This paper employs a structured critical analysis methodology 
to evaluate five dominant security paradigms against the 
Zero Trust principle of continuous verification. The analysis 
follows a failure-mapping framework: each paradigm is 
evaluated against four diagnostic criteria — (1) temporal 
trust treatment, (2) contextual awareness, (3) uncertainty 
representation, and (4) enforcement coupling. The paradigms 
were selected based on their prevalence in enterprise 
deployments and their foundational role in the cybersecurity 
literature. The analysis is conducted at the specification 
level (published standards and peer-reviewed research) 
rather than from production deployment data.
```

### 5.3 Priority 3: Restructure §7 (Major)

**Option A (Recommended)**: Condense §7 from "full DCTA presentation" to "requirements specification + candidate architecture outline":
- Retain Table 1 (failure mapping) and Table 3 (integration) — these are high-value synthesis
- Remove the full mathematical derivations (DS combination rule, variance formula, temporal decay) — these belong in the companion research paper
- Replace with a "Requirements for Resolution" subsection that specifies what the architecture must achieve
- Add a brief "Candidate Architecture" subsection that sketches the DCTA without full derivation
- Cross-reference the companion paper for full development and validation

**Option B**: Add experimental results from the companion paper — but this converts the paper from a review into a mixed review/research paper, which may create scope issues.

### 5.4 Priority 4: Strengthen Analytical Rigour Throughout

- Add explicit analytical criteria to each paradigm section
- Ensure each paradigm critique ends with a clear, structured "finding" statement
- Add a brief comparative analysis table at the start of §7 summarising all five paradigm failures against the diagnostic criteria

---

## 6. Plan for the Revised Paper

The revised paper should:
1. ✅ Explicitly declare itself as a **structured critical review**
2. ✅ Add a **methodology section** with analytical framework
3. ✅ **Replace all unverifiable references** with verified alternatives
4. ✅ **Condense §7** to requirements + candidate architecture (not full DCTA)
5. ✅ **Cross-reference** the companion paper for full DCTA development
6. ✅ Maintain the five-paradigm critical analysis (the paper's core strength)
7. ✅ Retain Tables 1 and 3 (high-value synthesis artifacts)
