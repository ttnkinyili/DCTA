# DCTA Repository — File Structure & Reorganisation Record

> **Project:** Dynamic Context-Aware Trust Architecture (DCTA)
> **Date:** 28 May 2026
> **Status:** Restructuring complete — pending Git commit

---

## 1. Overview

The DCTA repository supports research into dynamic trust computation for Zero Trust Architectures. It contains thesis chapters, research papers, Python simulation code, experimental results, and project planning documents.

Before this restructuring, **all 79 files sat in a single flat directory**. This made it difficult to locate specific files, understand the project at a glance, or onboard collaborators. The repository has now been reorganised into **8 purpose-driven subdirectories** with clear separation of concerns.

---

## 2. Directory Structure

```
DCTA/
├── .git/                      Git version control (do not modify)
├── .gitignore                 Ignore rules (updated)
├── README.md                  Project overview (root-level, public-facing)
├── FILE_STRUCTURE.md          This document
│
├── 01_thesis/                 Thesis chapters, sections, and references
├── 02_papers/                 Standalone research papers for publication
├── 03_analysis/               Supporting analysis, critiques, and discussions
├── 04_src/                    All Python source code
├── 05_results/                Simulation outputs (PNGs, CSVs, logs)
│   ├── base_model/            Variance-weighted model (no temporal decay)
│   ├── time_decay/            Linear temporal decay model
│   ├── time_decay_exp/        Exponential temporal decay model
│   └── ensemble/              Ensemble trust fusion model
├── 06_docs/                   Project planning, conference docs, Word files
├── 07_config/                 Scenario definitions and static resources
├── 08_assets/                 Standalone images and visual assets
│
└── venv/                      Python virtual environment (gitignored)
```

---

## 3. Directory Descriptions

### 01_thesis/ — 19 files

Contains all files that form part of the written thesis document. Each file maps to a specific thesis section or chapter.

| File | Description |
|------|-------------|
| `full_thesis_outline.md` | Master outline of all thesis chapters |
| `thesis_abstract.md` | Thesis abstract |
| `thesis_chapter3.md` | Chapter 3 — Methodology |
| `thesis_chapter4.md` | Chapter 4 — System Design |
| `thesis_lit_review_addition.md` | Extended literature review additions |
| `thesis_literature_cohesive.md` | Cohesive literature review narrative |
| `thesis_literature_critiques.md` | Critical analysis of reviewed literature |
| `thesis_bernoulli_binomial_trust.md` | Mathematical foundations (Bernoulli/Binomial trust) |
| `thesis_evaluation_of_models.md` | Comparative evaluation of trust models |
| `thesis_discussion.md` | General discussion section |
| `thesis_discussion_ensemble.md` | Discussion — Ensemble model findings |
| `thesis_discussion_time.md` | Discussion — Linear temporal decay findings |
| `thesis_discussion_time_exp.md` | Discussion — Exponential temporal decay findings |
| `thesis_discussion_wbf.md` | Discussion — Weighted Belief Fusion findings |
| `thesis_conclusions.md` | Conclusions and future work |
| `thesis_scope_limitations.md` | Scope and limitations |
| `thesis_appendices.md` | Appendices |
| `thesis_abbreviations_table.md` | Table of abbreviations and acronyms |
| `thesis_references.bib` | BibTeX reference library |

### 02_papers/ — 7 files

Standalone research papers written for conference or journal submission. Each paper is self-contained with its own abstract, methodology, and references.

| File | Description |
|------|-------------|
| `paper_ensemble_flagship.md` | **Flagship paper** — Ensemble Trust Model (ETM) with DS theory and dual-horizon decay |
| `paper_beyond_the_perimeter.md` | Paper on moving beyond perimeter-based security |
| `paper_probabilistic_trust_aggregation.md` | Probabilistic approaches to trust aggregation |
| `paper_reproducible_testbed.md` | Reproducible SDN/ZTA testbed design |
| `paper_trust_computation_survey.md` | Survey of trust computation methods |
| `paper_trust_decay_temporal.md` | Temporal trust decay mechanisms |
| `paper_variance_weighting_fusion.md` | Variance-based weighting and evidence fusion |

### 03_analysis/ — 22 files

Supporting research notes, model discussions, critiques, justifications, and results interpretation. These files inform the thesis and papers but are not direct thesis sections.

| File | Description |
|------|-------------|
| `comparison_and_tradeoffs.md` | Model trade-off analysis |
| `ai_ids_sdn_critique.md` | Critique of AI-based IDS in SDN environments |
| `access_policy_justification.md` | Justification for access policy thresholds |
| `session_length_justification.md` | Justification for session duration parameters |
| `ensemble_analysis.md` | Ensemble model behaviour analysis |
| `ensemble_output_explained.md` | Explanation of ensemble simulation outputs |
| `trust_decay_discussion.md` | Deep-dive into trust decay behaviour |
| `trust_weight_matrix.md` | Domain weight matrix documentation |
| `wbf.md` | Weighted Belief Fusion notes |
| `test_results_analysis.md` | Base model results interpretation |
| `test_results_analysis_time.md` | Linear decay results interpretation |
| `test_results_analysis_time_exp.md` | Exponential decay results interpretation |
| `research_gap_section.md` | Research gap identification |
| `perimeter_rbac_failure.md` | Analysis of perimeter/RBAC failure modes |
| `testcase_discussions.md` | Detailed test case walkthroughs |
| `Linear_Exponential_comparison.md` | Linear vs. exponential decay comparison |
| `Step_roles_ensemble.md` | Step-by-step role breakdown (ensemble) |
| `Steps_roles.md` | Step-by-step role breakdown (base) |
| `Steps_roles_time.md` | Step-by-step role breakdown (time decay) |
| `Steps_roles_time_exp.md` | Step-by-step role breakdown (exp decay) |
| `Reproducible Testbed_V1.md` | Testbed design notes (version 1) |
| `leveraging virtualization and emulation achor.md` | Virtualisation and emulation anchor notes |

### 04_src/ — 14 files

All Python source code, organised by function.

**Core Trust Models:**

| File | Description |
|------|-------------|
| `dynamic_trust_weighting.py` | Base trust model — variance-based dynamic weighting, no temporal decay |
| `dynamic_trust_weighting_time.py` | Extended model — adds linear temporal decay |
| `dynamic_trust_weighting_time_exp.py` | Extended model — adds exponential temporal decay |
| `ensemble_trust_simulator.py` | Ensemble trust fusion simulator (combines all models) |

**Dempster-Shafer Fusion:**

| File | Description |
|------|-------------|
| `ds_utils.py` | Dempster-Shafer utility functions (MassFunction class) |
| `weighted_belief_fusion.py` | WBF v1 — spatial + temporal fusion, no session decay |
| `weighted_belief_fusion_2_newest.py` | **WBF v2 (newest)** — adds exponential session decay and session expiry |

**Scenario Runners:**

| File | Description |
|------|-------------|
| `run_scenarios.py` | Runs all 6 scenarios through the base model |
| `run_scenarios_time.py` | Runs scenarios through the linear decay model |
| `run_scenarios_time_exp.py` | Runs scenarios through the exponential decay model |
| `run_ensemble_scenarios.py` | Runs scenarios through the ensemble fusion model |

**Utilities:**

| File | Description |
|------|-------------|
| `generate_visuals.py` | Generates plots and charts from simulation data |
| `check_citations.py` | Validates citation references in markdown files |
| `update_thesis.py` | Thesis document assembly/update helper |

### 05_results/ — 50 files across 4 subdirectories

Simulation outputs organised by model variant. Each subdirectory contains PNGs (belief evolution and domain score charts), CSV data, and text logs for the 6 canonical scenarios: Corporate Office, Remote VPN, Public WiFi, BYOD, Compromised Device, and Untrusted Device + Geofence.

| Subdirectory | Model Variant | Files |
|---|---|---|
| `base_model/` | Variance-weighted (no decay) | 14 |
| `time_decay/` | Linear temporal decay | 14 |
| `time_decay_exp/` | Exponential temporal decay | 14 |
| `ensemble/` | Ensemble trust fusion | 8 |

### 06_docs/ — 8 files

Project management, planning documents, and Word-format deliverables.

| File | Description |
|------|-------------|
| `project_tasks.md` | Task tracker and TODO list |
| `implementation_plan.md` | Technical implementation plan |
| `reorganization.md` | Notes on repository reorganisation (prior to this restructure) |
| `conference_paper_recommendation.md` | Conference targeting recommendations |
| `journal_paper_proposals.md` | Journal submission proposals |
| `Ensemble paper FedCSIS conference instructions.md` | FedCSIS conference formatting instructions |
| `Implementation Chapter.docx` | Word-format implementation chapter |
| `Trust_Computation_Equation.docx` | Word-format trust equation documentation |

### 07_config/ — 2 files

Static configuration and reference files used by the simulation code.

| File | Description |
|------|-------------|
| `scenarios.txt` | Definitions for the 6 canonical test scenarios |
| `equation.html` | Rendered HTML version of the trust computation equation |

### 08_assets/ — 2 files

Standalone image files used in documentation or presentations.

| File | Description |
|------|-------------|
| `scenario_trust_analysis.png` | Scenario trust analysis chart |
| `scenarios_table.png` | Summary table of scenario configurations |

---

## 4. Changes Performed

### 4.1 File Renamed

| Original Name | New Name | Reason |
|---|---|---|
| `weighted_belief_fusion_2.py` | `weighted_belief_fusion_2_newest.py` | Identified as the newer, more evolved version (adds temporal session decay). Renamed for clarity. |

### 4.2 Files Deleted

| File | Reason |
|---|---|
| `~$nal Thesis-Dynamic Trust Management and Context-v1.docx` | Microsoft Word temporary lock file (not project content) |
| `~$nal Thesis-Dynamic Trust Management and Context-v1-copy.docx` | Microsoft Word temporary lock file (not project content) |
| `__pycache__/` | Python bytecode cache (auto-generated, already gitignored) |

### 4.3 Directories Consolidated

The four original results directories were copied into a single `05_results/` parent with clearer subdirectory names:

| Original | New Location |
|---|---|
| `test_results/` | `05_results/base_model/` |
| `test_results_time/` | `05_results/time_decay/` |
| `test_results_time_exp/` | `05_results/time_decay_exp/` |
| `test_results_Ensemble/` | `05_results/ensemble/` |

### 4.4 `.gitignore` Updated

| Change | Detail |
|---|---|
| **Removed** | `scenarios_table.png` and `scenario_trust_analysis.png` (these are now properly filed in `08_assets/` and should be tracked) |
| **Added** | `~$*.docx` pattern to prevent Word temporary lock files from being committed |

### 4.5 No Files Were Modified

No file contents were altered during this restructuring. All moves were file-level only. The content of every `.md`, `.py`, `.docx`, `.bib`, `.csv`, `.png`, and `.txt` file is identical to its pre-restructure state.

---

## 5. Git Status & Next Steps

Because files were moved using `mv` (system move) rather than `git mv`, Git currently sees the changes as deletions from old paths and new untracked files at new paths. **This is cosmetic** — Git will automatically detect the renames once you stage and commit.

### To commit the restructuring:

```bash
cd /Users/admin/Desktop/DCTA

# Stage all changes (deletions + new paths)
git add -A

# Verify Git detected the renames
git status
# You should see "renamed:" entries instead of separate delete/add pairs

# Commit
git commit -m "restructure: organise repository into 8 subdirectories

- Moved thesis chapters to 01_thesis/
- Moved research papers to 02_papers/
- Moved analysis documents to 03_analysis/
- Moved Python source code to 04_src/
- Consolidated test results into 05_results/ with model-specific subdirs
- Moved project docs to 06_docs/
- Moved config files to 07_config/
- Moved image assets to 08_assets/
- Renamed weighted_belief_fusion_2.py to weighted_belief_fusion_2_newest.py
- Updated .gitignore (added ~\$*.docx, removed individual PNG ignores)
- Deleted Word temp lock files and __pycache__"

# Push to remote
git push origin main
```

### If you encounter push errors:

```bash
# If remote has diverged:
git pull --rebase origin main
git push origin main

# If branch name is 'master' instead of 'main':
git push origin master
```

---

## 6. File Count Summary

| Directory | Files | Description |
|---|---|---|
| `01_thesis/` | 19 | Thesis chapters and references |
| `02_papers/` | 7 | Research papers |
| `03_analysis/` | 22 | Analysis and discussion notes |
| `04_src/` | 14 | Python source code |
| `05_results/` | 50 | Simulation outputs (4 subdirectories) |
| `06_docs/` | 8 | Planning and Word documents |
| `07_config/` | 2 | Scenario definitions and static resources |
| `08_assets/` | 2 | Image files |
| **Root** | **3** | `README.md`, `.gitignore`, `FILE_STRUCTURE.md` |
| **Total** | **127** | Including this document |

---

*This document was generated as part of the DCTA repository restructuring on 28 May 2026.*
