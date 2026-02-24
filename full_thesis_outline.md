# Full Thesis Outline: Evaluating Zero Trust Models through Evidential Fusion and Temporal Dynamics

*Below is the 8-chapter structure aligning the user's provided skeleton with the specific technical evaluations and models developed throughout this research.*

## CHAPTER ONE: INTRODUCTION
*   **1.1 Background of the Study:** The evolution of network perimeters to perimeter-less environments (Zero Trust frameworks).
*   **1.2 Statement of the Problem:** The persistence of the "Implicit Trust Period" in current Zero Trust implementations and the vulnerabilities stemming from static, binary access control decisions.
*   **1.3 Purpose of the Study:** To mathematically evaluate the progression of trust models, culminating in a dynamic, continuous, stateful "Ensemble Trust Model."
*   **1.4 Research Questions & Hypotheses:** Can evidential fusion coupled with temporal decay effectively neutralize lateral movement and session hijacking compared to legacy models?
*   **1.5 Scope and Limitations:** Focusing on mathematical simulations, Dempster-Shafer fusion, and algorithm modeling rather than a specific vendor installation.

## CHAPTER TWO: TRUST IN HETEROGENOUS NETWORKED SYSTEMS
*   **2.1 The Concept of Trust:** Defining trust as a calculable probability rather than a binary state in distributed networks.
*   **2.2 The Evolution of Access Control:** From implicit trust (traditional perimeters) to explicit multi-domain evaluation architectures (Identity, Device, Network).
*   **2.3 Evidential Fusion in Cybersecurity:** The mathematical application of the Dempster-Shafer (DS) Evidence Theory for calculating risk amid conflicting telemetry.
*   **2.4 The Zero Trust Execution Gap:** Challenges in orchestrating dynamic policies, recognizing "noisy sensors," and the limitations of static gateways.

## CHAPTER THREE: Trust in Context - Zero trust Architecture and The Power of Environment
*   **3.1 Spatial Contextualization:** Defining how spatial telemetry (Location, Device Posture, Time of Day) informs initial trust calculations.
*   **3.2 Contextual Gray-Area Routing:** Introducing the concept of proportional access tiers (Full, Limited, Quarantine) over binary lockouts during ambient environmental noise.
*   **3.3 The Failure of Static Access Control:** Analyzing the brittleness of Single-Domain Criteria and rigid Hierarchical Multi-domain models in complex environments.

## CHAPTER FOUR: Dynamic Trust Models for Enterprise networks - Adapting to Change
*   **4.1 The Integration of Temporal Dynamics:** Examining the concept of session ephemerality and the defining realization that *Trust is an ephemeral asset*.
*   **4.2 Linear Temporal Decay:** Parameterizing proportional session-length degradation mathematically.
*   **4.3 Exponential Temporal Decay:** Utilizing aggressive decay parameters ($\lambda$) as a mathematically verified "kill-switch" against session hijackers.
*   **4.4 Dynamic Weighting and Behavioral Inertia:** Generating historical behavioral baselines using geometric variance tracking over observed operational cadences.

## CHAPTER FIVE: Building a Zero Trust Testbed with Virtualized Resources
*   **5.1 Conceptual System Architecture:** Mapping the logical domains (Identity, Device, Network) to the automated evaluation engine (PDP/PEP structure).
*   **5.2 Mathematical Engine Design:** Programming the Dempster-Shafer combination rules and implementing the decay algorithms natively.
*   **5.3 Scaling the Engine:** Decoupling the calculation engine (containerized microservices) from the physical Software Defined Perimeter (SDP) routing gateways.

## CHAPTER SIX: TESTBED DESIGN AND SETUP
*   **6.1 Architecture Topology:** Defining the simulated enterprise network, incorporating "Full Access" zones, "Limited Access" enclaves, and external threat vectors.
*   **6.2 Simulation Parameters:** Defining the simulation variables across the 9 test cases (initial trust scores, observation windows, variance thresholds $\alpha$).
*   **6.3 Threat Actor Profiles:** Designing the test vectors mimicking Advanced Persistent Threats (APTs), session hijackers, and noisy remote environments.

## CHAPTER SEVEN: Evaluation results and Discussion of results *(Mapped from `thesis_evaluation_of_models.md`)*
*   **7.1 Phase 1 Evaluation (Static Models):** Results tracking lateral movement in Implicit Trust, Single-Domain, and Hierarchical scenarios.
*   **7.2 Phase 2 Evaluation (Evidential Fusion):** Results demonstrating the efficacy of Dynamic Weighting amidst noisy telemetry (categorizing Uncertainty vs. Malware).
*   **7.3 Phase 3 Evaluation (Temporal Models):** Results comparing Linear vs. Exponential Temporal Decay in terminating hijacked sessions.
*   **7.4 Phase 4 Evaluation (The Ensemble Trust Model):** Results demonstrating the hybridization of rapid cryptographic "Freshness" with long-term "Inertia."
*   **7.5 Comparative Discussion:** Synthesizing the data to prove the superiority of stateful, continuous evaluation over static Boolean logic.

## CHAPTER EIGHT: Conclusions and Recommendations *(Mapped from `thesis_conclusions.md`)*
*   **8.1 Conclusion: The Paradigm Shift in Continuous Verification:** Synthesizing the findings (Fallacy of Static Trust, Efficacy of DS Fusion, Necessity of Temporal Dynamics).
*   **8.2 Recommendations for Operational Deployment:**
    *   Transitioning to Adaptive Gray-Area Routing
    *   Algorithmic Calibration of Decay Rates ($\lambda, \alpha$)
    *   Infrastructure Requirements for Ensemble Models (SIEM/SOAR)
    *   Scalable Infrastructure for Trust-Centric Models
    *   Automated Orchestration of SDP Controllers
    *   Real-time Integration of Telemetry Data
*   **8.3 Future Works and Expanding the Architecture:**
    *   Unsupervised Machine Learning for Behavioral Inertia
    *   Decentralized Fusion for Edge and IoMT Constraints
    *   The Imperative of Quantum-Safe Architectures (PQC/ML-KEM)
    *   Predictive Infrastructure Scaling using Anticipatory Risk
    *   AI-Driven SDP Topologies
    *   Advanced Contextual Telemetry via Extended Reality (XR)

## References
*   *(Comprehensive APA formatted bibliography spanning all chapters).*
