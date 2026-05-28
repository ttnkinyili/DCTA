# Conference Paper Recommendation — From Journal Paper Proposals

## 1. The Five Proposed Papers

From [journal_paper_proposals.md](file:///Users/admin/Desktop/DCTA/journal_paper_proposals.md):

| # | Title | Type | Readiness | Already Generated? |
|:--|:------|:-----|:---------:|:------------------:|
| **P1** | An Ensemble Trust Architecture for Continuous Zero Trust Enforcement: Fusing DS Theory with Dual-Horizon Temporal Decay | Flagship / Systems | ★★★★☆ | ✗ |
| **P2** | Probabilistic Trust Aggregation in Zero Trust Architectures: A Nested Bernoulli-Binomial Framework with DS Mass Construction | Theoretical / Mathematical | ★★★★★ | ✅ `paper_probabilistic_trust_aggregation.md` |
| **P3** | Trust Decay as Continuous Verification: Exponential Evidence Discounting, Sliding Windows, and Graduated Thresholds | Temporal Dynamics | ★★★★☆ | ✗ |
| **P4** | Beyond the Perimeter: Why Static RBAC, SDP, and AI-Augmented Detection Fail Without Dynamic Trust | Critical Review / Position | ★★★★☆ | ✅ `paper_beyond_the_perimeter.md` |
| **P5** | A Lightweight Zero Trust Testbed for Validating Dynamic Trust Models in Software-Defined Enterprise Networks | Applied / Testbed | ★★★☆☆ | ✗ |

> [!NOTE]
> The previously generated [paper_trust_computation_survey.md](file:///Users/admin/Desktop/DCTA/paper_trust_computation_survey.md) is a **sixth paper** (Survey) not listed in `journal_paper_proposals.md`. It is included in the analysis below as **P6** for completeness.

---

## 2. Conference Structure

### Main Tracks

| # | Track |
|:--|:------|
| T1 | Advanced Artificial Intelligence Approaches |
| T2 | Intelligent Data Processing and Infrastructure |
| T3 | Security of AI and AI for Security |
| T4 | Intelligence Technologies for Business and Society |
| T5 | Intelligent Software, System, and Service Engineering |

### Thematic Sessions

| Code | Full Name | Domain |
|:-----|:---------|:-------|
| Agentic AI in SC | Agentic AI in Smart Cities | AI + Urban |
| AgriAI | AI in Agriculture | AI + Agriculture |
| AI-HuSo | AI in Digital Humanities, Computational Social Sciences and Economics Research | AI + Social Science |
| AIWAVOM | AI for Inland Water, Atmospheric Environments, and Ocean Modelling | AI + Environmental |
| APL | Advances in Programming Languages | CS Theory |
| CANA | Computer Aspects of Numerical Algorithms | Numerical Computing |
| CNLPS | Challenges for Natural Language Processing | NLP |
| CO | Computational Optimization | Optimization |
| DSH | Data Science in Health, Ecology and Commerce | Data Science |
| EDUC-AI-TION | Education & AI Systems | AI + Education |
| IoT-ECAW | IoT Enablers, Challenges and Applications | IoT |
| ISM | Information Systems Management | IS Management |
| MDASD | Model Driven Approaches in System Development | Software Engineering |
| MMAP | Multimedia Applications and Processing | Multimedia |
| **NEMESIS** | **International Forum on Cyber Security, Privacy, and Trust** | **Cybersecurity** |
| SLSAS | Self Learning and Self Adaptive Systems | Adaptive Systems |

---

## 3. Paper-to-Conference Compatibility Matrix

### 3.1 Main Track Alignment

Scoring: **✓✓** = strong primary fit | **✓** = solid secondary fit | **◐** = tangential | **✗** = no fit

| Track | P1 (Ensemble) | P2 (Bernoulli) | P3 (Temporal) | P4 (Critical Review) | P5 (Testbed) | P6 (Survey) |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|
| **T1: Advanced AI** | ◐ | ✗ | ✗ | ◐ | ✗ | ◐ |
| **T2: Data & Infrastructure** | ✓ | ◐ | ◐ | ◐ | **✓✓** | ◐ |
| **T3: Security of AI / AI for Security** | **✓✓** | ✓ | ✓ | **✓✓** | ✓ | **✓✓** |
| **T4: Business & Society** | ◐ | ✗ | ✗ | ✓ | ◐ | ◐ |
| **T5: Software & Systems Engineering** | ✓ | ◐ | ◐ | ◐ | **✓✓** | ✓ |

### 3.2 Thematic Session Alignment

| Session | P1 | P2 | P3 | P4 | P5 | P6 | Notes |
|:--------|:---:|:---:|:---:|:---:|:---:|:---:|:------|
| Agentic AI in SC | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Smart cities — no ZTA focus |
| AgriAI | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Agriculture domain |
| AI-HuSo | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Humanities/social science |
| AIWAVOM | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Environmental modelling |
| APL | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Programming languages |
| CANA | ✗ | ◐ | ✗ | ✗ | ✗ | ✗ | P2's numerical algorithms are tangential |
| CNLPS | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | NLP domain |
| CO | ✗ | ◐ | ✗ | ✗ | ✗ | ✗ | P2's variance optimisation is tangential |
| DSH | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Health/ecology/commerce |
| EDUC-AI-TION | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Education domain |
| **IoT-ECAW** | ✓ | ◐ | ◐ | **✓✓** | ✓ | ✓ | P4 critiques IoT trust gaps; P1/P5 address IoT heterogeneity |
| **ISM** | ◐ | ✗ | ✗ | ✓ | ◐ | **✓** | P6's standardisation recs fit ISM; P4's enterprise critique relevant |
| MDASD | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ | Model-driven development — very tangential |
| MMAP | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Multimedia domain |
| **NEMESIS** | **✓✓** | ✓✓ | ✓✓ | **✓✓✓** | ✓✓ | **✓✓✓** | **Primary target** — dedicated cybersecurity, privacy, trust forum |
| **SLSAS** | ✓ | ◐ | ✓ | ◐ | ◐ | ◐ | P1's self-calibrating weights and P3's adaptive decay are self-learning |

---

## 4. Recommendation

### 🏆 Best Fit: **P4 — "Beyond the Perimeter"** (Critical Review / Position Paper)

**Target:** Thematic Session **NEMESIS** (*Cyber Security, Privacy, and Trust*) under **Main Track 3** (*Security of AI and AI for Security*)

**Manuscript:** Already generated as [paper_beyond_the_perimeter.md](file:///Users/admin/Desktop/DCTA/paper_beyond_the_perimeter.md)

### Detailed Rationale

| Criterion | Why P4 Wins |
|:----------|:------------|
| **NEMESIS alignment** | P4 is a paper **about cybersecurity trust** — it systematically diagnoses why five security paradigms fail without dynamic trust. This is the *exact* scope of a forum on "Cyber Security, Privacy, and Trust" |
| **Breadth of coverage** | P4 traverses **five paradigms** (Perimeter, RBAC, NIST SP 800-207, CSA SDP, AI-IDS/SDN) — touching multiple sub-communities in a single presentation. Conference audiences strongly prefer broad, integrative papers over narrow, single-method contributions |
| **AI for Security angle** | P4's Section 6 critically analyses **AI-augmented IDS** in SDN — specifically data poisoning, adversarial attacks on ML classifiers, and belief fusion corruption (Ali et al., 2024). This directly fits Main Track 3's "AI for Security" scope and distinguishes P4 from a pure security paper |
| **Diagnostic + constructive** | P4 is not merely a critique — it maps each paradigm's failure to a specific missing capability (Table 1) and then presents the **DCTA Ensemble Model** as the architectural bridge (Table 3). This diagnostic-constructive arc is exactly what conference reviewers seek |
| **Unified failure mapping** | The paper's central Table 1 (structural failure mapping) and Table 3 (DCTA architectural integration) are visually compelling, self-contained conference presentation assets. Audiences grasp the argument from these two tables alone |
| **Conference format vs. journal format** | P4's argumentative structure — sequential critique followed by unified resolution — maps perfectly to a **25–30 minute conference talk**. The five paradigms provide natural slide progression. Pure mathematical papers (P2) and extensive empirical papers (P5) are harder to present in this format |
| **Manuscript readiness** | P4 is **already fully generated** at 406 lines / ~7,500 words. At conference page limits (8–12 pages), P4 requires minimal condensing — primarily tightening the per-paradigm critiques |

### Close Runner-Up: P6 (Trust Computation Survey)

P6 is equally strong for NEMESIS. Its six-criteria evaluation framework (C1–C6) and seven comparison tables make it exceptionally conference-ready. **The choice between P4 and P6 depends on conference emphasis:**

| If the conference emphasises... | Submit... | Reason |
|:-------------------------------|:----------|:-------|
| **Architectural critique and position** | P4 | Stronger narrative arc; diagnostic power |
| **Systematic evaluation and benchmarking** | P6 | Novel framework (C1–C6); broader model coverage; actionable standardisation recs |

> [!TIP]
> If the conference permits **two submissions**, submit **P4 to NEMESIS** and **P6 to ISM** (Information Systems Management) — their scopes are complementary with minimal self-overlap.

---

## 5. Why Not the Other Papers?

| Paper | Limitation for This Conference |
|:------|:-------------------------------|
| **P1** (Ensemble Systems) | A strong systems paper, but it needs the **full empirical validation pipeline** (testbed data, latency metrics, adversarial survival time) to compete with P4's diagnostic breadth. Better suited for a journal (*IEEE TIFS*, *IEEE TDSC*) where length permits full system + evaluation coverage |
| **P2** (Bernoulli-Binomial) | Pure mathematical/statistical theory. Bernoulli trials, Beta-Binomial regularisation, Markowitz diversification proof — too specialised for a multi-disciplinary conference audience. None of the 16 thematic sessions targets formal probability theory. **Best venue:** *Information Fusion* or *Information Sciences* |
| **P3** (Temporal Decay) | Narrow focus on a single mechanism (temporal decay). While NEMESIS-relevant, it cannot compete with P4 or P6's breadth. It also overlaps substantially with P1's temporal dynamics section. **Best venue:** *IEEE TNSM* or *JNCA* as a focused journal contribution |
| **P5** (Testbed) | Requires additional experiments and data (★★★☆☆ readiness). Its systems engineering focus fits T5 and potentially IoT-ECAW, but the paper needs completion before submission. **Best venue:** *Journal of Systems Architecture* or *SoftwareX* after P1 is published |

---

## 6. Ranked Submission Strategy

| Priority | Paper | Target | Track | Readiness |
|:---------|:------|:-------|:------|:---------:|
| 🥇 **Primary** | **P4** (Critical Review) | **NEMESIS** | Track 3 | ✅ Ready |
| 🥈 **Alternative** | **P6** (Survey) | **NEMESIS** or **ISM** | Track 3 or 5 | ✅ Ready |
| 🥉 **If 2 submissions allowed** | P4 → NEMESIS, P6 → ISM | Both | Track 3 + Track 5 | ✅ Both ready |
| 4th | P1 (Ensemble) | NEMESIS | Track 3 | Requires generation |
| 5th | P5 (Testbed) | IoT-ECAW | Track 2 or 5 | Requires completion |
| — | P2, P3 | Not recommended for this conference | — | Journal-only |

---

## 7. Preparation Checklist for P4 Submission

- [ ] **Page limit check**: Conference typically requires 8–12 pages (full) or 4–6 (short). P4 at ~7,500 words fits 10–12 pages in IEEE/Springer format — likely needs light condensing
- [ ] **Template conversion**: Convert [paper_beyond_the_perimeter.md](file:///Users/admin/Desktop/DCTA/paper_beyond_the_perimeter.md) to conference LaTeX/Word template (likely IEEE or Springer LNCS)
- [ ] **Abstract tightening**: Current abstract (~180 words) → trim to conference limit (typically 100–150 words)
- [ ] **Presentation arc**:
  - Slides 1–2: The "implicit trust period" — the universal vulnerability
  - Slides 3–4: Perimeter dissolution + RBAC temporal passport
  - Slides 5–6: NIST SP 800-207 unspecified Trust Algorithm
  - Slides 7–8: CSA SDP post-authentication silence
  - Slides 9–10: AI-IDS adversarial fragility (data poisoning)
  - Slides 11–13: Unified failure mapping (Table 1) + DCTA resolution (Table 3)
  - Slides 14–15: Formal properties + conclusion
- [ ] **Author details**: Add Strathmore University affiliation and supervisor information
- [ ] **Reference verification**: Verify all 2024–2025 dates and DOIs
- [ ] **Submission deadline**: Confirm and calendar the deadline
- [ ] **Camera-ready adjustments**: Reserve time for reviewer feedback incorporation

> [!IMPORTANT]
> P4 is already generated and manuscript-ready. Begin template conversion immediately upon confirming submission deadline.
