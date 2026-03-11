You are an expert academic writing assistant. Your task is to restructure a PhD thesis on "Dynamic Context-Aware Software Defined Perimeters" according to the detailed outline and requirements provided below. The goal is to transform the original thesis (which suffers from fragmented argument progression, chapter identity drift, and limited reader roadmap) into a coherent, book-like narrative that follows the logic: Problem → Theory → Failure → Design → Proof → Meaning.

### Guidelines for Restructuring

1. **Preserve all original content** – Do not delete any substantive content. Instead, move sections, paragraphs, and figures to their appropriate new chapters. Some rewriting may be needed to improve flow, but avoid introducing new ideas or removing existing ones.

2. **Follow the new chapter outline exactly** – The thesis must be divided into the chapters and sections listed below. Use the provided titles and purposes to guide content placement.

3. **Eliminate repetition** – Ensure that concepts (e.g., heterogeneity, Zero Trust principles, trust decay) are introduced and developed in one chapter only, then referenced later without re-explanation.

4. **Create strong transitions** – At the beginning of each chapter (except Chapter 1), add a paragraph that:
   - Summarizes what was established in the previous chapter
   - States what remains unresolved
   - Explains how this chapter advances the solution

5. **Add reader signposts** – At the end of each chapter, include a short paragraph (marked with 📌) that:
   - Recaps the chapter's main takeaway
   - Hints at what the next chapter will address

6. **Anchor technical content** – Equations, architectures, and detailed technical explanations should appear only after the reader understands the motivation. For example:
   - Trust equations go in Chapter 3 (theory) and Chapter 6 (model)
   - SDP architecture goes in Chapter 5 (enforcement substrate)
   - Implementation details go in Chapters 7–8

7. **Ensure chapter identity** – Each chapter must have a single dominant purpose (as stated in the outline). Do not mix background, theory, design, and results within one chapter.

8. **Maintain academic tone and citation style** – Keep all references intact; they should remain with the content they originally supported, unless moved to a more appropriate location.

### New Thesis Structure (with Chapter Purposes and Key Content)

#### Front Matter
- Abstract (retain original)
- Keywords (retain)
- List of Abbreviations and Acronyms (retain)
- Definition of Terms (retain)

---

#### Chapter 1: Introduction and Research Framework
**Purpose:** Establish research context, objectives, and methodology.
**Content:**
- 1.1 Background Information
- 1.2 Statement of the Problem
- 1.3 General Aim
- 1.4 Research Gap
- 1.5 Objectives of the Study
- 1.6 Research Questions
- 1.7 Significance of the Study
- 1.8 Scope and Limitations
- 1.9 Contribution of the Study
- 1.10 Methodology and Approach
   - 1.10.1 Research Methodology
   - 1.10.2 Research Design
   - 1.10.3 Software-Defined Platform (SDP) Testbed Considerations

**retain** detailed methodology (original 1.10)

**End chapter with** a thesis roadmap paragraph (provided below).

---

#### Chapter 2: The Collapse of Perimeter Trust in Heterogeneous Networks
**Purpose:** Establish the problem space.
**Content:**
- Evolution of enterprise networks → heterogeneity → volatility
- Why perimeter security and static RBAC fail
- Insider threats, misuse propagation, implicit trust
- Motivation for Zero Trust—but unresolved gaps
- Malware/misuse examples (SWIFT, Mirai)
- Related works on heterogeneous networks, malware propagation
**End with:** "Zero Trust defines *what* should be done—but not *how* trust should be computed dynamically."

---

#### Chapter 3: Trust as a Computational Problem
**Purpose:** Elevate trust from policy to formal system property.
**Content:**
- Trust definitions, static vs dynamic trust
- Trust taxonomy (decision, evaluation, management models)
- Trust in distributed systems
- Related works on trust models
- Trust computation: static, weighted sum, dynamic weighted sum
- Trust thresholds: binary, ternary, contextual gray-area routing
- Subjective logic: Dempster-Shafer, belief fusion (cumulative, average, weighted)
- Trust decay equations (linear, exponential)
**End with:** "Existing trust models are fragmented, static, or context-limited."

---

#### Chapter 4: Zero Trust Architecture: Strengths and Blind Spots
**Purpose:** Critically evaluate ZTA.
**Begin with** transition from Chapter 3 (provided below).
**Content:**
- ZTA pillars (user, device, network, app, data)
- ZTA principles and architecture (PDP/PEP, supplements)
- NIST SP 800-207
- Where ZTA excels (visibility, least privilege)
- Where ZTA fails: no formal trust aggregation, no adaptive weighting, no temporal reasoning
- Trust assumptions critique
**End with:** "ZTA provides the *what* but lacks a *how* (trust engine) and *where* (enforcement substrate)."

---

#### Chapter 5: Software-Defined Perimeters as Underlying Substrate
**Purpose:** Justify SDP as the execution layer.
**Begin with** transition from Chapter 4 (provided below).
**Content:**
- SDP architecture and evolution (v1→v2)
- SDP vs VPN vs SDN; SPA, mTLS, gateways
- SDP-SDN convergence
- SDP operational processes: trust anchor, domain, join, leave
- Mapping SDP to ZTA
- Why SDP supports dynamic trust enforcement
**End with:** "SDP provides enforcement—but not intelligence."

---

#### Chapter 6: A Context-Aware Dynamic Trust Model (Core Contribution)
**Purpose:** Present the novel framework.
**Content:**
- Five trust facets as computational inputs (user distributed into data, device, application, network; three parameters each)
- Contextual weighting (equations)
- Dynamic weighted sum + weighted fusion (fusion equation)
- Residual/inertia trust (inertia equations)
- Temporal decay (linear/exponential equations)
- Ensemble model: contextual weighted fusion + temporal decay + inertia (combined equation)
- Context tables, identity aggregation logic
**End with:** "Mathematical engine needs virtualization-powered enforcement."

---

#### Chapter 7: Testbed Design and Implementation
**Purpose:** Describe methodology and testbed setup.
**Content:**
- Experimental methodology (moved from original Ch1)
- Testbed setup: virtualization tools, resource optimization
- GNS3 + Mininet rationale
- Component deployment: PDP, PEP, PAP, Policy Engine as decoupled services
- Parsing trust engine → SDP Controller
**End with:** "Virtualization makes trust executable."

---

#### Chapter 8: Trust-Driven Zero Trust Enforcement via SDP
**Purpose:** Show integration of trust engine with SDP.
**Content:**
- Mapping trust engine to SDP components
- Scenario construction: trust thresholds → access outcomes, metrics, continuous re-evaluation, policy lifecycle
- Testbed reusability, custom policies
**End with:** "Testbed reusable for different scenarios."

---

#### Chapter 9: Results, Analysis, and Interpretation
**Purpose:** Demonstrate effectiveness.
**Begin with** experimental overview (scenarios, evaluation framework).
**Content:**
- Latency trade-offs
- Breach containment
- Context sensitivity
- Comparative evaluation across models
**End with:** (no specific signpost needed; results interpreted)

---

#### Chapter 10: Implications for Enterprise Security Design
**Purpose:** Translate findings to practice and theory.
**Content:**
- Architectural implications
- Policy design
- Performance vs trust trade-offs
- Alignment with future AI-driven security
**End with:** (implications interpreted)

---

#### Chapter 11: Conclusion and Research Trajectory
**Purpose:** Close the narrative loop.
**Content:**
- What problem was solved
- What changed conceptually
- Limitations
- Future research directions

---

### Provided Transition and Signpost Texts

**Chapter 1 End (Roadmap):**
> "This thesis proceeds as follows: Part I (Chapters 2–3) establishes the problem and theoretical foundations. Part II (Chapters 4–5) critiques existing solutions and justifies our architectural choices. Part III (Chapter 6) presents our novel trust model. Part IV (Chapters 7–9) describes implementation and validation. Part V (Chapters 10–11) discusses implications and concludes."

**Chapter 4 Beginning (Transition):**
> "Chapter 3 established trust as a computational problem with mathematical foundations in subjective logic and temporal decay. However, the question remains: do existing security architectures implement these computational trust principles? This chapter examines Zero Trust Architecture—the dominant paradigm for modern network security—to evaluate whether it provides the mathematical trust engine that heterogeneous networks require."

**Chapter 5 Beginning (Transition):**
> "Before we can build the *how* (trust engine), we must establish the *where*—the enforcement architecture that can execute dynamic trust decisions."

**Chapter 9 Beginning (Experimental Overview):**
> (Insert a brief recap of the 5–6 canonical scenarios tested, the evaluation framework, and how results will be presented.)

**Chapter End Signposts (📌)** – Use the ones provided in the outline for Chapters 2–8.

---

### Instructions for Moving Content

- Use the original thesis document as the source. Identify which sections belong in each new chapter based on the content descriptions above.
- Where content overlaps multiple chapters, split it appropriately. For example:
  - General background on networks and threats → Chapter 2
  - Trust theory and equations → Chapter 3
  - Zero Trust principles and critique → Chapter 4
  - SDP architecture details → Chapter 5
  - Proposed model equations and tables → Chapter 6
  - Testbed setup and tools → Chapter 7
  - Policy implementation and scenarios → Chapter 8
  - Results and analysis → Chapter 9
  - Discussion and future work → Chapters 10–11
- Ensure that all figures, tables, and citations move with their relevant content.
- If a section contains both problem motivation and theory (e.g., "Need for Dynamic Access Control" in original), decide its primary home and move it there; if necessary, split into two parts.
- Add the required transition paragraphs and signposts where indicated.
- After restructuring, the document should flow as a single, coherent argument with no abrupt jumps or unexplained concepts.

### Output Format

Provide the restructured thesis as a single Markdown document with clear chapter headings (## Chapter X: Title) and section headings (### X.Y Title). Preserve all original text except where moved or lightly edited for flow. Include all front matter. Ensure that the final document is ready for further refinement.

Begin now.