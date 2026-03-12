Context-Aware Software Defined Perimeters: A Dynamic Context-Aware Trust Model for Zero Trust Enforcement in Heterogeneous Enterprise Networks

Dynamic Context-Aware Software Defined Perimeters: An Adaptive Trust Computation Model for Zero Trust Enforcement in Heterogeneous Enterprise Networks

By:

Nkinyili T. Tabulu

Submitted in Partial Fulfillment of the Requirements of the Doctor of Philosophy in Computer Science at Strathmore University School of Computing and Engineering Sciences

Strathmore University,

Nairobi, Kenya.

2026

# DECLARATION AND APPROVAL

I declare that this work has not been previously submitted and approved for the award of a degree by this or any other University. To the best of my knowledge and belief, the research contains no material previously published or written by another person except where due reference is made in the research document itself.

Student Name: 	Nkinyili T. Tabulu

Admission Number: 	062631

Student Signature:	__  Date:	__

[Figure/Image from source paragraph 25]

Approval

The research Proposal of Nkinyili T. Tabulu has been reviewed and approved by:

Prof. Vincent Omwenga ,

Associate Professor,

School of Computing and Engineering Sciences,

Strathmore University.

Signature	________

[Figure/Image from source paragraph 35]

Date:	______________

Prof. Samson Ogara

Professor,

School of Computing,

Jaramogi Oginga Odinga University of Science and Technology

Signature	_________________

Date:	_______________________

# ABSTRACT

Information security is an important consideration in the provision of any service or access to any resource within a network. The conventional perimeter-based security model is fundamentally inadequate for modern heterogeneous enterprise networks; characterized by cloud migration, IoT proliferation, and mobile workforces and  more varied devices. Additionally, access control based on user credentials is increasingly becoming inadequate due to the volatility of security contexts that result from the dynamicity and heterogeneity of these networks. This has resulted in adoption and adaptation of zero trust architecture for better security of shared network resources. This thesis proposes a novel architecture that integrates the core tenets of Zero Trust Architecture to develop a dynamic, context-aware trust model to enforce secure access to shared network resources in heterogeneous networks. It integrates a mathematical trust engine into the control plane  leveraging subjective logic to compute multi-dimensional trust opinions (belief, disbelief, uncertainty) derived from a continuous stream of data labels, user behavior, application permission, device posture, and environmental context. It incorporates critical dynamic factors such as contextual weighting  and temporal decay to ensure trust scores reflect recent behavior.

The architecture’s innovation lies in its multi-factor trust engine which considers data, application , network, and device facets of zero trust. It computes a continuous, probabilistic trust score by applying cumulative fusion of scores within each pillar and weighted fusion to represent dynamic contexts across the pillars as well as a residual trust value that is decayed over time. The culmination is an eventual trust score value for nodes in heterogeneous networks to determine the enforcement of access control decisions. While this is promising in addressing these varied computing contexts, the computing overheads and turnaround times for such a trust centric model would be very high especially for real-time access decisions. This engine is therefore embedded within the SDP controller, transforming it from a simple connection broker into an intelligent decision point that grants least-privilege access to network services only when trust thresholds are met. Software defined perimeters provide an adaptable architecture to control access to resources by decoupling the control and data planes. This not only allows for the scalability but also flexibility and mobility of access to resources through multiple devices owned by both the enterprise and the employees while securing data accessed.

The performance and efficacy of the model were validated through extensive emulation experiments using Mininet and GNS3 which enabled the creation of high-fidelity, scalable network topologies. Python scripts were used to implement the mathematical engine applied on the SDP controller. These experiments created realistic enterprise topologies with diverse endpoints and varied users and services. A variety of threat actors and scenarios were introduced, including insiders with stolen credentials, endpoints exhibiting lateral movement patterns and compromised devices and credentials. Dynamicity was assessed by measuring the model's responsiveness to the 5 facets, while context awareness was evaluated by weighting interactions based on facet criticality. Key metrics measured included session approval latency, breach containment time, and resource access success rates under attack. Experimental results demonstrated an enhancement in security posture and operational efficiency and the architecture's security advantages. In GNS3 tests, the model contained a simulated insider threat breach faster than static SDP policies by dynamically revoking access upon detecting anomalous behavior. Mininet performance benchmarks showed a manageable increase in initial session setup latency (approx. 15-20ms) due to real-time trust evaluation, a negligible cost compared to the enhanced security posture. Furthermore, the system successfully denied access to critical R&D servers from devices with outdated security patches, even with valid credentials, proving its context-aware capability. The discussion confirms that the dynamic trust model mitigates trust related misuses and intrusions by reviewing access contexts on five fronts; data being accessed, device accessing data, network originating the request, application infrastructure used and residual trust representing previous user transactions making it a vital enhancement for securing next-generation enterprise networks. This work provides a blueprint for building truly adaptive, resilient, and intelligent network security infrastructures.

Keywords: Heterogeneous networks, Information security, Software Defined Perimeters, Zero-Trust Model, Misuse and Intrusion Prevention, Trust Estimation, Trust score, Access Control

# LIST OF ABBREVIATIONS AND ACRONYMS

# DEFINITION OF TERMS

Heterogeneous Network: an evolved enterprise network landscape that integrated emerging trends such as wireless and mobile devices, fog computing, bring your own device, Internet of Things (IoT) and microservices and teleworking (Vanickis et al., 2018) and (Garbis & Chapman, 2021).

Perimeter Security: perimeter-based architecture in which any subject behind the wall (i.e., inside the predefined perimeter) is considered trusted (Teerakanok et al., 2021).

Software-Defined Networking (SDN): A network architecture approach that decouples the network control and forwarding functions, enabling the network control to become directly programmable and the underlying infrastructure to be abstracted for applications and network services (IEEE Communications Society, 2024).

Software-Defined Perimeter (SDP): A security framework, popularized by the Cloud Security Alliance, that establishes dynamic, one-to-one network connections between users and authorized resources, adhering to a "zero trust" model where identities and device posture are verified before access is granted, effectively making applications invisible to unauthorized entities (Cloud Security Alliance, 2025).

Context-based Access: this is typically based on a combination of checks such as device certificates, 2-factor authentication, or patch status of the accessing device to control access to resources. It includes mobile and wireless components, virtualized infrastructures, dynamic and heterogeneous user contexts for access decisions (Lukaseder et al., 2020).

Dynamic trust Policy: a set/list of what is allowed or not allowed in an enterprise for its network, data and/or infrastructure security. It is a policy based on constantly changing network and infrastructure parameters as well as the weightings and dynamicity of trust metrics (Das and Debnath, 2020).

Zero Trust: a concept involving the provisioning of enterprise/organization resources to the subjects without relying on any implicit trust. a subject earns trust from the system on a particular request/transaction by proving itself through authentication and authorization (Teerakanok et al., 2021) and (Garbis & Chapman, 2021).

Trust dynamicity: refers to evolution of trust over time or events based on changes of states of trustors and trustees or changing contexts. It also represents trust decays over time when there are no new events (Wang et al., 2022).

Context Aware: Context refers to any information that can be used to describe the background situation of involved entities, while the ability to identify and adapt to contexts is regarded as context-awareness. In the context of trust, trust models are expected to evolve with changes in environment such as a task type, a purpose, an objective, or an execution environment(Wang et al., 2022)

Trust computation/modelling: Trust score determination based on calculation, aggregation and/or weighting of metrics to determine the type of access decision made based on a threshold value. A subject’s behavior is continuously observed and calculated into a behavior trust. Access to a resource is granted only if exceeds the trust threshold  which may change dynamically depending on the environment (Teerakanok et al., 2021).

Trust Algorithm: the process employed by a policy engine to make an access decision by considering inputs such as entries in a policy database, user role attributes, device and network information, threat-related information, etc. as per the need of a particular access request (Teerakanok et al., 2021) and (Syed et al., 2022).

Trust Management model: A type of model built on top of architectures such as blockchain, edge networks or Software Defined Networking (SDN),  as a  means to control and maintain trust in digital systems (Wang et al., 2022)

Supplements: useful information such as threat intelligence information and network/system logs that allows a policy engine to make more accurate and correct decisions (less false positive and false negative) enhancing the overall security of the system (Teerakanok et al., 2021). They may also provide more dynamicity and context awareness for a deployment scenario.

Misuse: A sequence of actions, including  its variants, that a system or other entity can perform, interacting with a target system or entity to cause loss of data, system availability or harm to a resource or stakeholders if the sequence is allowed to complete (Akhlaif et al., 2021).

Intrusion: any kind of unauthorized activity that could pose a possible threat to the digital resources’ confidentiality, integrity, and availability (Attou et al., 2023).

Adaptive Routing (Gray-Area Routing): Within Software-Defined Perimeters (SDP), this is the dynamic orchestration of network traffic where connections are not strictly binary (allow/deny). Instead, based on degrading trust continuous assessments, sessions are dynamically rerouted into restricted, highly monitored "gray-area" VLANs or enclaves to contain potential adversarial lateral movement (Oprea et al., 2025).

Algorithmic Suspicion (Trust Continuum): The operational philosophy of this Continuous Adaptive Risk and Trust Assessment (CARTA) framework. It discards the binary "trusted/untrusted" state, instead placing all network entities on a fluctuating Trust Continuum where mathematically formalized suspicion (uncertainty) is continuously quantified based on real-time metadata (Premier Science, 2024).

Continuous Adaptive Risk and Trust Assessment (CARTA): A strategic cybersecurity framework that mandates the continuous, real-time evaluation of all users, devices, and network behaviors to make contextual, adaptive access decisions, rather than relying on static, one-time authentication (Trio.so, 2025).

Dempster-Shafer Theory of Evidence (DCTA): A mathematical theory of belief functions used within this thesis's trust evaluation model to calculate operational uncertainty and fuse disparate, conflicting telemetry signals (e.g., Identity, Device, Network) into a single, cohesive trust metric (Fan & Li, 2024).

Ensemble Trust Model: The specific algorithmic architecture proposed in this research, which hybridizes deterministic cryptographic gating with probabilistic behavioral analysis to trap adversaries within a continuous, stateful matrix of historical behavioral inertia (Barchart, 2024).

Evidential Fusion: The algorithmic process of combining multiple streams of contextual security data (telemetry) to generate a comprehensive, probabilistic assessment of an entity's operational trustworthiness or risk level (Chen et al., 2025).

Historical Inertia (Trust Momentum): The conceptual mechanism by which a user or device's long-term history of verified, safe network behavior acts as a stabilizing weight against sudden, anomalous telemetry spikes. High historical inertia prevents a single dropped packet or minor anomaly from causing catastrophic revocation of access, ensuring systemic stability (MDPI, 2024).

Network Metadata / Contextual Signals: The continuous stream of non-payload data generated by an entity during a session. In this thesis, it is categorized into four specific domains: Identity Context, Device Posture, Network Variance, and Application Sensitivity (IEEE Communications Society, 2024).

Spatial Model: Within Zero Trust, a formal, multi-tiered structure utilized to monitor the physical and logical location hierarchies of users and devices, integrating with temporal constraints to dictate localized access rights (CSDP, 2025).

Temporal Decay (Data Freshness / Sliding Window): The mathematical algorithm utilized to validate the recency (Data Freshness) of telemetry. It employs Sliding Windows to systematically penalize or reduce a previously established trust score over time, ensuring that idle or unverified authorizations expire according to a parameterized rate (linear or exponential) to minimize adversarial dwell time (Al-Tariq et al., 2025).

Zero Trust Architecture (ZTA): An enterprise cybersecurity architecture based on zero trust principles, fundamentally operating under the assumption that no actor, system, network, or service operating outside or within the security perimeter is trusted without continuous verification (National Institute of Standards and Technology, 2025).


---

# PART I: THE TRUST PROBLEM

# Chapter 1: Introduction and Research Framework

# INTRODUCTION

The opening part of this book establishes the 'why' before the 'how'. We must first understand why perimeter defenses failed, and why trust must be redefined as a computational asset rather than a static credential.

## Background Information

The increased evolution, adaptation and adoption of new technologies, architectures, and paradigms such as cloud computing, SDNs, and NFV in recent years has led to a new set of security and privacy challenges and concerns. These concerns include proper authentication, access control, data privacy, and data integrity, among others (Moubayed et al., 2019) and (Wang et al., 2022). As such, information security is fast becoming a global challenge with both technical and governance dimensions (World Economic Forum, 2025) and (Dargahi, et al., 2017). Whereas it is inevitable to have networked systems for sharing information and other resources across enterprises and institutions, it’s also imperative that careful steps are taken to ensure that the integrity and general security of these resources is maintained. Measures should provide security against both internal and external threats and users of the services. However, despite the changes to the enterprise environment with the introduction of new services and incorporation of new access devices, service provision methods largely remain the same (Chandramouli & Butcher, 2023). This makes the infrastructure supporting these services more vulnerable to intrusions over time and the information contained more prone to unauthorized access, corruption, and deletion.

According to Vanickis et al., (2018) and Pitumpe et al., (2025), the evolution of the enterprise computing landscape towards emerging trends such as fog computing, bring your own device, Internet of Things (IoT) and teleworking has led to emergence of heterogeneous networks in enterprises. Consequently, the change has resulted in dynamicity and greater uncertainty in the access control process due to mobility, virtualized infrastructures, dynamic and heterogeneous user contexts. Thus, the perimeter-based security paradigm is increasingly becoming inadequate for intrusion prevention in such multidevice environments (Garbis & Chapman, 2021).

An intrusion or misuse is an act or attempt at using a network and computational resources without the requisite privileges, causing willful or incidental damage. They point to unauthorized activities originating from users internal or external to network (Khraisat & Alazab, 2021). Many surveys show that the rapid growth and expansion of network communications has led to consistent increase in frequency and sophistication of network intrusions and consequently losses of data, data privacy, and data accessibility in the recent years (Sukumar et al., 2018) and (Li et al., 2020). Intrusion Prevention is the use of devices and applications with the ability to monitor or detect malicious activities or unwanted behavior, and that can react in real time to prevent the attack from being successful (Khraisat & Alazab, 2021). This is achieved using multiple layers of security by deploying mechanisms such as firewalls, intrusion detection and prevention systems (IPS) as part of a defense-in-depth approach. Some enterprises also include advanced local and network-based authentication mechanisms to further bolster security and restrict the availability of network resources to endpoint devices that comply with a defined security policy (Zaydi & Nasserddine, 2016) and (Adewusi & Odekeye, 2025). While this is necessary, it is an insufficient, reactive approach that does not protect the infrastructure since the same nodes contain the resources and services that users aim to access. It is thus critical to consider more integrative and context aware mechanisms to protect networks against these more complex and less predictable threats.

Software Defined Perimeters (SDP) is an architecture that serves to identify the source and destination points of a network connection; a secure connection is only granted when explicitly permitted (Cloud Security Alliance., 2022). It stems from software defined networks, which decouple the control and data planes. It provides on demand, dynamically provisioned secure network segmentation for user access, which is flexible for heterogeneous networks with wireless, mobile and IOT devices. This not only applies the principle of least privilege to the network, it also reduces the attack surface area by hiding network resources from unauthorized or unauthenticated users (Wu & Feng, 2021) and (Islam & Flores, 2017) .

Increase in mobile devices, virtualized infrastructures, dynamic and heterogeneous user contexts and transaction-based interactions increases the security risks and uncertainties (Vanickis et al., 2018) and as such render “a trust-but-verify” approach ineffective. Zero trust pivots to “never trust, always verify” approach access to resources is continuously verified. The verification also focuses more than user identity verification and includes five pillars – device trust, user trust, transport/session trust, application trust and data trust. Once trust is established across all five pillars, decisions can be made to grant or deny access; the decisions are constantly re-verified to cater for trust changes in in the enterprise. In addition, by establishing trust across the five pillars, it is possible to gain visibility and gather analytics across the digital workspace environment for automation and orchestration (Kueh, 2020). The key element of the ZTN approach is to treat the internal network as untrusted to the same degree as the Internet. Zero trust enforcing software defined perimeters would thus be critical in masking and hiding all network resources from all users by providing user, application, data, network, and device identities verification.

## Statement of the Problem

According to Vanickis et al., (2018) and Pitumpe et al., (2025), the evolution of the enterprise computing landscape towards a more heterogeneous network, makes it more vulnerable to intrusions and misuse from both internal and external users. Moreover, there is greater dynamicity and uncertainty in the access control process due to mobility, virtualized infrastructures, dynamic and heterogeneous user contexts. Based on these changes in the landscape, the number of moving parts and parameters for consideration when evaluating resource access requests has increased significantly. Additionally, implicit trust is assumed on a number of facets such as internal users, enterprise owned devices and enterprise approved networks. While this is mostly the case, it leaves enterprises susceptible to insider attacks, data leakages and misuse and consequently intrusions into networked systems (Lukaseder et al., 2020).

Furthermore, user roles, privileges and permissions are keep changing within enterprises and as such, there’s need to constantly vary user trust levels relative to contextual enterprise needs and policies (Eidle et al., 2018). Traditional perimeter-based security paradigm considers users, devices, networks and applications owned by an enterprise to be inherently trussed  thus performing  check and inspection on variants of these facets that originate from external networks, remote users and unauthorized applications (Teerakanok et al., 2021). This results in security being increasingly difficult to guarantee and inadequate for  misuse and intrusion prevention in such multidevice environments.

This work thus proposes dynamic and context aware trust centric model that uses the five facets of zero trust to determine network trust levels within enterprise infrastructures. The model considers provisioning of enterprise/organization resources to the subjects without relying on any implicit trust that plays a big role in perimeter-based architectures as discussed by Lukaseder et al., (2020) and Teerakanok et al., (2021). Other than user identities, other facets: application, devices, network infrastructure and data resource requested are used provide alternative attributes and context to further determine a request’s trust level and the consequent access decision to a resource. Additionally, the model considers user roles, history and transactions to gain more trust or lose trust especially cases of misuse and intrusions from a user or user device. This becomes the basis for trust algorithm which is then enforced on software defined perimeters. The model also maps the SDP controller to the ZT policy decision point for the trust derivation where trust can either be earned or lost based on context from the other attributed and the SDP gateway to the policy enforcement point for a subject’s eventual access to a resource.

## General Aim

The aim of this work is to develop a context aware network trust model that is based on zero trust architecture to help verify and authorize user access to resources in heterogeneous environments. The context is derived from the other facets of zero trust and weighted to generate a general trust value that is used for access decisions on resources. The trust model will be tested and enforced on an SDP testbed where it informs the access policy used by SDP controllers for access decisions to resources.

## Research Gap

While multiple layers of security can be implemented to improve information security, most of the mechanisms are meant to deter external attackers (Zaydi & Nasserddine, 2016) and (Adewusi & Odekeye, 2025) and assume that the authenticated internal users cannot be formidable threats to the application infrastructure. They also consider one level of security such that when a user is successfully authenticated, their actions are not reviewed within different segments of the network. Zero trust enforcing software defined perimeters would thus be critical in masking and hiding all network resources from all users by providing identity, application, network and device authentication by (Cloud Security Aliance, 2019).  Additionally, enforcement is dynamic based on contexts. Contexts are collected based on the facets of zero trust as multi attributes describing each facet for example devices used can be categorized by physical addresses, vendors or existence of hardware-controlled authentication mechanisms while application contexts can be defined by child processes spawned, license types, level of authorizations and update versions. Trust gaining and loss due to role and privilege promotions and demotions are also vital considerations for the model (Teerakanok et al., 2021).

## Objectives of the Study

- To analyze the impact of network infrastructure identities and user trust values on mitigating trust related misuse and intrusion incidents in heterogeneous enterprise networks

- To evaluate the effectiveness of trust derivation and management models in implementing dynamic policies for preventing misuse and intrusions in heterogeneous networks

- To design and develop a dynamic and context-aware network trust derivation model for mitigating trust-related misuse and enhancing intrusion prevention in heterogeneous networks based on Zero trust architecture

- To test and validate the derived model  on an SDP based architecture testbed

## Research Questions

How do network infrastructure identities and user trust values influence intrusion and misuse in heterogeneous enterprise networks?

How can trust derivation and management models be applied for dynamic policies for misuse and intrusions prevention in heterogeneous networks?

How can a context aware network trust architecture for mitigating trust related misuse and intrusions in a heterogeneous networks be designed and developed based on zero trust architecture?

How can the derived model be tested and validated on SDP based testbeds to evaluate the effects on access to informational resources in heterogeneous enterprise networks?

## Significance of the Study

Modern enterprises have heterogeneous networks that serve a dynamic environment informed by amorphous and sometimes overlapping policies and operating procedures as discussed by Vanickis et al., (2018) and (Jouyban & Hosseini, 2025). This coupled with the ubiquitous computing and a remote workforce make it very difficult for the enterprises to secure their network resources. Additionally, there is need to represent the dynamicity of user levels and privileges, estimate and determine trust levels based on these changing parameters and dynamically enforce them for different types of resources depending on their criticality within the enterprise (Rose et al., 2020).

The concept underlying Zero Trust is that no actor, system, network, or service operating outside or within the security perimeter is trusted. It requires deploying comprehensive controls for continuously verifying attempts and requests to access resources. Therefore, this is a paradigm shift in philosophy on how to secure infrastructure, networks, and data, from verify once at the perimeter to continual verification and dynamic enforcement for each user, device, application, and transaction. It thus involves a coordinated effort of communications/network services (e.g., network access controls), computing services (including cloud configuration and management), information services (such as  data protection standards), operational technology (such as  IT infrastructure), end-user services, applications, and cybersecurity and privacy services (Bertino & Brancik, 2021). This thus makes the approach the only feasible model to address the increasingly heterogeneous networks within enterprises.

The proposed work thus designs a trust factor calculation algorithm that derives from weighted values of multi attribute parameters gathered from the 5 facets of zero trust. These facets and consequently their parameters will help create a relevant context through which trust can either be gained on lost for each transaction that requires access to a resource. This allows for dynamic trust determination, policy definition and enforcement for the enterprise resulting in more secure access to resources based on trust centric model.

## Scope and Limitations

The work focuses on the calculation and derivation of a network trust value based on zero trust. The focus is thus the five facets of identity in zero trust including data, user, applications, network infrastructure and devices. These will provide a composite attribute set that helps derive the contexts for each resource request. The work also focuses on improving the trust algorithm of the policy decision point to ensure a more granular access control to resources. The enforcement of the trust algorithm will also be tested on the SDP controllers before enforcing the decision at SDP gateways.

## Contribution of the Study

Generally, the trust algorithm in Zero trust is considered the thought process in the policy decision point providing an ability to accurately decide whether to grant or deny access to all incoming requests. TA incorporates information from the other identity attributes including threat intelligence, SIEM logs, network traffic, subject’s geolocation, user’s identities, and credentials. Each piece of information is not equally important; some information, such as user credentials, are more important and are weighted more, comparing to other factors such as network traffic, in calculating a trust level of a subject (Teerakanok et al., 2021). Currently, there is no optimal solution, guideline, or reliable approach in weighting such factors; the enterprise implementing ZTA needs to continuously observe and adjust these parameters over time to ensure it functions accurately as intended. This model thus looks at weighting approach to determine the most optimal combination of attributes in heterogeneous environment where not all attributes are always available. It also intends to test the new trust model on SDPs which most enterprises are shifting to for a more dynamic user, resource, and service provisioning.

## Methodology and Approach

### Research Methodology

The research methodology used for the development the proposed architecture incremental prototyping to ensure progressive design, development and empirical validation.  The research design is also experimental in nature ensure that the experiments are tweaked and reviewed against varied topologies representing modern heterogeneous enterprise networks. The agile experimental approach includes a combination of theoretical analysis, algorithmic design, and empirical validation.

- Literature Review: this involved a comprehensive and systematic literature survey of existing trust models and evaluation frameworks for heterogeneous networks. Critique of approaches and frameworks, their limitations and considerations for both dynamicity, context awareness and scalability especially considering the computational overheads for context sensitive environments was also considered

- Metrics and parameters identification: pillars of Zero Trust architecture including device, data, network and application security were taken into consideration. The varied contexts for user behavior were quantified within these pillars and a decayed residual trust value based on previous transactions to determine the eventual trust score which influences the final access decision.

- Model Design: A dynamic and context aware model for trust score calculation is defined based on the pillars of zero trust. Further, metrics such as data integrity, node behavior and network protocols used are cumulated per ZT pillar as highlighted in detail TABLE 1.1. Zero Trust Architecture (ZTA) principles such as least privilege, continuous verification, and context-aware access control have also been emphasized. Cumulative and weighted fusion are used as the foundational mathematical modeling to represent trust as a multi-dimensional metric influenced by contextual factors in the ZTA facets such as device posture, user identity, and application infrastrucure.

- Algorithm Development: Cumulative fusion is used within sub attributes in each of the facets and weighted fusion applied across the general facets to create a more dynamic algorithm in trust score calculation. The weightings can also be varied to reflect the computing or access control contexts that are representative of varied heterogeneous enterprise network environments. This ensures the algorithm has context-aware trust computation and aggregation.

- Emulation and Testing: The algorithm is tested within an emulation environment based on GNS3, open daylight and Mininet applications to emulate a heterogeneous network. GNS3 provides an emulation representing cross platform wired and wireless network domains as well as virtualized nodes while Mininet and Opendaylight provide an SDN based platform that allows the model to be tested across an adaptable SDP testbed. The testbed inherently provides a scalable architecture due to the decoupled data and control planes provided by SDN and SDP platforms. Tests  are conducted on the testbed  to evaluate performance metrics, including accuracy, adaptability and scalability of access decisions while adhering to Zero Trust principles. Do I need to:?

- Compare the proposed architecture against any trust evaluation frameworks.

- Use real-world datasets, cases or topologies to validate the applicability of the model.

### Research Design

The algorithm design, development and testing will employ experimental design with structured stages to test and evaluate the proposed trust evaluation architecture:

- Test Scenarios: emulations of real-world heterogeneous network conditions, including varying contexts such as mobility, device diversity, and application-specific requirements. incorporation of Zero Trust Architecture scenarios, such as enforcing least privilege policies, dynamic access decisions, and mitigating insider threats.

- Data Collection: Generation of synthetic data representing interactions in heterogeneous networks. Most of the data will be ordinal for quantitative evaluation of scores of factors such as data integrity and freshness, network protocol score or device reputation score. Nominal data will be applicable for qualitative factors such as compliance status for devices or anomaly detection for networks.

- Simulation Environment: GNS3 and Mininet will be used to emulate heterogeneous networks. SDP controllers on Mininet will incorporate trust engines for dynamic context updates and trust evaluation mechanisms aligned with ZTA facets.

- Metrics for Evaluation: metrics such as trust accuracy to measure consistency of trust scores with ground truth data.  Adaptability can be used to assess how quickly and effectively the model responds to context changes. Scalability test can be used to evaluate performance under varying network sizes and complexities while ZTA adherence on architecture enforcement of continuous verification, dynamic policy and least privilege access.

- Controlled Variables: these will ensure consistent baseline parameters, such as network topology and initial trust values, across experiments.

- Experiment Execution: iteratively conduct experiments while continuously modifying parameters such as decay duration, data freshness, context weight and interaction frequency for intra-pillar cumulation and inter-pillar weighting.

### Software-Defined Platform (SDP) Testbed Considerations

To validate the proposed dynamic and context aware trust architecture, a controlled and realistic environment, a Software-Defined Platform (SDP) testbed is utilized:

- Testbed Architecture: Comprises software-defined networking (SDN) controllers, programmable data planes, python-defined trust algorithm, and interconnected devices emulating heterogeneous networks. It also includes modules for context sensing, trust computation, and adaptive policy enforcement.

- Implementation: The trust evaluation model is deployed as a service on the SDP controller. OpenFlow-enabled switches and programmable nodes are used to emulate diverse network devices and configurations. Endpoint verification and user authentication mechanisms are enforced within these controllers.

- Context Awareness: Data collection for context awareness such as mobility, protocols, device compliance and network anomalies are collected from endpoints, networks and application infrastructure. Context is dynamically updated based on most important tenets of ZT for any specific heterogeneous enterprise network.

- Experimentation: Test the architecture under different network scenarios, such as varying device densities and attack patterns and apply adaptive policy enforcement. Evaluation of the effectiveness of trust decisions made

- Performance Metrics: Assessment of network throughput and latency to assess efficiency trust convergence time to measure responsiveness, policy compliance in continuous verification as well as misuse cases and intrusion preventions

- Analysis and Insights: Compare experimental results with theoretical predictions and evaluate strengths and areas for improvement

This comprehensive methodology ensures that the proposed trust evaluation architecture is rigorously designed, tested, and validated to address the complexities of heterogeneous enterprise networks effectively, with a strong alignment to Zero Trust principles.


*📌 This thesis proceeds as follows: Part I (Chapters 2–3) establishes the problem and theoretical foundations. Part II (Chapters 4–5) critiques existing solutions and justifies our architectural choices. Part III (Chapter 6) presents our novel trust model. Part IV (Chapters 7–9) describes implementation and validation. Part V (Chapters 10–11) discusses implications and concludes.*



---

# Chapter 2: The Collapse of Perimeter Trust in Heterogeneous Networks

*Chapter 1 established the research context, objectives, and methodology for investigating dynamic trust in heterogeneous enterprise networks. A critical question remains: why do traditional perimeter-based security models fail in modern enterprise environments? This chapter examines the structural evolution of enterprise networks and the resulting collapse of perimeter trust.*

# TRUST IN  HETEROGENOUS NETWORKED SYSTEMS

(Weaving the Web: Trust in Interconnected Worlds)

## Introduction

This chapter reviews the evolution of modern enterprise networks and the roles of different types of identities in user authentication and trust estimation to guide access decisions per requests. It also reviews the architecture of software defined networks and perimeters and their effectiveness to network growth and scaling. The culmination of these is also a research gap to justify this work and a conceptual framework that discusses the resultant testbed that will be the outcome of this work.

## Theoretical Framework

### Underlying Security Principles

Principle of Fail- safe Defaults: this states that, unless a subject is given explicit access to an object, it should be denied access to that object. This principle requires that the default access to an object is none. Whenever access, privileges, or some security-related attribute is not explicitly granted, it should be denied. Moreover, if the subject is unable to complete its action or task, it should undo those changes it made in the security state of the system before it terminates. This way, even if the program fails, the system is still safe (Stallings & Brown, 2018).

Least privilege principle: This is a well-known security practice to reduce the risk of credential theft or data misuse and leakage.it ensures that users and applications only have the minimum privileges needed to perform their intended tasks For example, for data stored in a networked or cloud server meta-data a user should not have full access to all services. the system provisioned would have huge security risks if this was the case. Although least privilege is regarded as an important practice, discovering the least-privileged is an error-prone and burdensome task because the process tends to be trial and error. The permissions should be limited to reduce security risks, but insufficient permissions cannot satisfy a system’s requirements (Shimizu & Kanuka, 2020) and (Wu & Feng, 2021).  This principle thus defines a rule of thumb for the default permissions and trust levels for users accessing resources within an enterprise.

Complete Mediation principle: The principle of complete mediation requires that all accesses to objects be checked to ensure that they are allowed. Whenever a subject attempts to read an object, the system should mediate the action. First, it determines if the subject is allowed to read the object. If so, it provides the resources for the read to occur. If the subject tries to read the object again, the system should check that the subject is still allowed to read the object. This ensures that checks are always performed before access requests are granted. This guarantees that security checks are performed before and not after transactions have been performed. It thus becomes a prevention principle and not an audit mechanism. For performance improvements, most systems would not make the second check. They would cache the results of the first check and base the second access on the cached results.

Separation of privileges principle is defined in as a practice in which multiple privilege attributes are required to achieve access to a restricted resource. It therefore ensures that a system should not grant permission based on a single condition. A good example of this is multifactor user authentication, which requires the use of multiple techniques, such as a password and a smart card, to authorize a user. The term is also now applied to any technique in which a program or data is divided into parts that are limited to the specific privileges they require to perform a specific task. This is used to mitigate the potential damage of a computer security attack. One example of this latter interpretation of the principle is removing high privilege operations to another process and running that process with the higher privileges required to perform (Stallings & Brown, 2018).

The architectural realization of Zero Trust is theoretically anchored in the foundational cybersecurity principles of "fail-safe defaults" and "deny-first." Historically, network engineering favored an "allow-by-default" topology to prioritize seamless connectivity and availability. Security practitioners were forced to construct extensive blacklists, firewalls, and intrusion detection systems in an attempt to identify and block malicious anomalies on an already open network.

The fail-safe algorithmic default fundamentally inverts this operational logic. Under this principle, a system mathematically defaults to a secure, restrictive, offline state; it denies all environmental visibility and access unless explicit, cryptographically sound authorization is presented and actively maintained (Turner & O'Connor, 2024). Recent theoretical literature highlights that this "deny-first" approach is the granular, operative mechanism that makes Zero Trust functional across highly complex, cloud-native frameworks and autonomous agentic communication systems (Davidson, 2025; Turner & O'Connor, 2024).

When an entity attempts to access a resource under ZTA, it is treated as inherently hostile (embodying the "assume breach" mentality). By defaulting to denial, the architecture proactively limits initial exposure and neutralizes lateral attack surfaces. Critically, if an authentication service crashes, a software agent encounters an operational exception, or a device's telemetry feed goes silent, a fail-safe system does not fail "open" to preserve business continuity; it fails securely by instantly revoking the network entitlement (Davidson, 2025). Ultimately, fail-safe defaults represent the tactical, mechanical implementation of trust denial, while Zero Trust serves as the overarching strategic framework governing its enterprise-wide application.



[Figure/Image from source paragraph 183]

Figure 2.1: The divergence between Fail Open and Fail-Safe architectures during system exceptions.

### Heterogeneous Enterprise Network Landscape

In recent years there has been an increase in the evolution and proliferation of technology in our daily lives. The number of smart-phones, mobile-connected wireless devices, social networks, and sensors being used has grown substantially due to the emergence of the concept of Internet of Things (IoT) (Moubayed et al., 2019). These developments have been in place to help facilitate more pervasive and ubiquitous computing among different users of computing devices. This has thus resulted in much change in enterprise computing in the last two decades with the appearance of new approaches such as cloud and edge computing, the (industrial) Internet of Things (IIoT) and computing on demand. These environments have been characterized by distributed interactions on a scale not seen heretofore with attendant high levels of complexity and dynamicity – including mobility -heterogeneity and uncertainty (Vanickis et al., 2018).

The complexity has been further compounded by the multiplicity of telecommunication transmission and media access, which can be reflected by the coexistence of optical fiber communications, power line communication, wireless local access network,  wireless sensor network, public network GPRS/CDMA, 3G, 230MHz cable/wireless and public network/special network, with different and supplemented coverage areas, multiple and heterogeneous communication systems, wide and concurrent access, and the changeable and rough communication environment (Guo & Ren, 2015). Many different types of network communication have also emerged over the years as illustrated in Figure 1. On one end of the spectrum, there are asynchronous store and forward networks, such as email. On the other end, there are synchronous networks, such as real-time voice communication or devices worn on the same body. Either way, devices and their heterogeneous networks are getting more pervasive. They all have in common that their communication should be secured to protect confidential data (Schürmann, 2017) and (Das & Debnath, 2020).



[Figure/Image from source paragraph 189]

Figure .: Evolution TimeLine for Heterogeneous Networks

Additionally, emerging networks such as 4G and 5G systems as well as other phenomenon such as BYOD and teleworking have resulted in complexities to enable elements such as mobility, virtualized infrastructures, dynamic and heterogeneous user contexts and transaction-based interactions. This is illustrated in Figure 2 on integrated heterogeneous enterprise network environments. The uncertainty introduced by such dynamicity introduces greater uncertainty into the access control process and motivates the need for risk-based access control decision making (Vanickis et al., 2018).



[Figure/Image from source paragraph 194]

Figure .: Structure of Integrated Heterogeneous Networks

It is therefore apparent that most enterprise networks today are inherently heterogeneous, comprising devices, protocols, services and architectures with varying characteristics. This heterogeneity stems from diverse devices including IoT sensors, mobile devices, legacy systems, cloud servers, and edge nodes with differing computational and security capabilities. With the need for communication across these devices, then multiple communication protocols to support lossy and lossless communications and busty connections are also required. Variations such as TCP/IP, Zigbee, MQTT andBluetooth) lead to fragmented security implementations which lead to extended surfaces of attacks. There is also significant adoption of elastic and off-premise cloud infrastructure to reduce cost of ownership and flexibility of access to resources which further compounds the heterogeneity and creates complexity in interoperability  and compatibility with legacy systems that are often unpatched or lacking modern security features, coexist with newer devices and platforms. The dynamicity and mobility of most of the devoces also introduce  frequently changing contexts, metadata and anchor points between transitioning between edge networks, local infrastructure, and the cloud.

The diversity of these heterogeneous environments creates significant challenges for managing trust, enforcing consistent security policies, and ensuring seamless interoperability.

To handle the increasing number of devices, technologies and paradigms, risk-based access control to resources needs to be dynamic and context aware in order to a consider the variants of resources available in enterprise networks. Moubayed et al., (2019) hinted at an amalgamation of technologies and paradigms such as zero trust, cloud computing, software-defined networking (SDN), and network function virtualization (NFV) for better security in such heterogeneous environments.

### Malware and Misuse Propagation on Heterogeneous networks

With the permeation of heterogeneous enterprise networks, with their diverse components such as wireless systems, IoT devices, legacy systems, virtualized nodes, cloud platforms, and edge nodes, there is a complex and dynamic attack surface that can be exploited for resource misuse or system intrusions (Vanickis et al., 2018). Intrusions and misuse incidents often arise due to inadvertent challenges and deliberate exploitations revolving around user, application and physical attack surfaces. Layered attacks including insider and outsider attacks are good examples of threats on the user surface. Authorized internal users with knowledge on system functionalities may misuses their access privileges and originate attacks resulting in data leaks and /or unauthorized modification of data resources or metadata such as configurations. External attackers on the other hand mostly target poorly secured IOT devices, legacy systems or inconsistencies in patches on nodes and hosts to gain unauthorized access, perform unauthorized modifications or alter system configuring metadata to result in unwanted unavailability. In some instances, threats such as disruption and usurpation mya result from configuration missteps due to permissions overuse or unfettered access for unprivileged users. Misconfigurations in access control policies across heterogeneous devices lead to unintentional permission escalation leading to other potential risks such as disclosure and deception. While most misconfigurations result from oversight, the  unmonitored deployment of devices and applications within the network especially for better management, convenience of deployment or  as hooks and extensions to existing topologies and pipelines introduces unknown vulnerabilities as discussed by Li et al. (2019) and Ferraris et al. (2023). These applications and devices, referred to as shadow IT further introduce points of misuse and intrusions especially in heterogeneous domains.

Furthermore, with the heterogeneity, there is a more dynamic threat landscape especially because of the presence of a powerful and distributed nodes that come from the IoT domain and embedded systems. Other attack vectors such as malware, phishing, and DOS vectors, disproportionately exploit their inherently weak security mechanisms, unchecked trust relationships between nodes in these diverse systems. This asymmetry eventually overwhelm the defense mechanisms of more secure and trusted network domains and segments. (Wang et al., 2018) and (Rehman et al., 2022).

With the permeation and adoption of heterogeneity in enterprise networks, both the number and severity of cybersecurity incidents have grown dramatically. Some examples include, in an attack on the global financial messaging network SWIFT in 2016 that resulted in over $80 million in losses to financial institutions in Asia including in Bangladesh, the Philippines, Sri Lanka, and Vietnam. This attack highlighted the ongoing need for protection against insider threats from within a presumably trusted network and a lack of rigorous authentication and identity management for network users. Many other incidents have demonstrated a need for improved defense against automated cyberattacks, including botnets and crypto ransomware. Further, in 2016, several notable distributed denial-of-service (DDoS) attacks occurred, harnessing botnets comprised of security cameras, baby monitors, home appliances, and other devices on the Internet of Things (IoT). Mirai botnet disrupted DNS servers at the service provider Dyn, affecting millions of users on Twitter, Amazon, Spotify, Netflix, Tumblr, and Reddit (Eidle et al., 2018).

The dramatic escalation in both the number and sophistication of security-attacks on business in recent years, will continue to grow in coming years– a factor that merely adds to the computing environment complexity (Vanickis et al., 2018). The permeation of more heterogeneous networks within enterprises further introduces new frontiers for malware and misuse propagation against the data handled and owned by these enterprises. Additionally, the increase in both frequency and severity, has further exposed traditional defense methods  as inadequate and reactive to these vulnerabilities(Sheikh et al., 2021). Some of these challenges as illustrated in Figure 2.3



[Figure/Image from source paragraph 206]

Figure 2.4 Modern Network Challenges Addressed by Zero Trust (from: (Moubayed et al., 2019))

Even more concerning, the cyber-defense capabilities of many organizations are already stretched to their limits. According to the 2017 Security Capabilities Benchmark Study, most organizations can only investigate about half of the alerts they receive on any given day. This is at least partly due to the massive number of potential security alerts that must be processed; 44% of security operations managers receive over 5,000 security alerts per day. In this environment, less than half (about 46%) of legitimate security alerts are addressed, while the remainder are left uninvestigated. There is a corresponding need to improve both efficiency and response time to immediate threats; automated systems are good candidates for this approach (Eidle et al., 2018).

Since almost every network user possesses several types of communication devices that are being used in different locations, under different environmental conditions, situations, and time frames. These devices can share common forms of use, they all have distinctive characteristics, strengths, and weaknesses. Therefore, heterogeneous network allows for different routes and methods of malware propagation. One can generalize different paths of malware  and misuse propagation  heterogeneous networks as following:

compromised device (malware) subjected to device-to-device synchronization by user and leads to the compromise of other devices of the user.

common application software on different devices of the same user; first device is compromised then device to device synchronization by the user leads to compromise of other devices of the user.

network users share software; software compromised based on user–user propagation or device-to-device synchronization leading to other devices being compromised.

Device of one user compromised by malware via email/download/link; the user synchronizes other devices leading to the other devices of the user being compromised.

Device of one user compromised by malware via email/download/link the user/device sends email to /shares the link with other users and devices of other users gets compromised.

Smartphone’s malware propagates via random dialling/using the identities in the address book; other smartphones are compromised.

Malware compromised device of one user, malware propagation via Blue-tooth or wireless and other devices are compromised (Alexeev et al., 2016)

These incidents have highlighted challenges in dynamicity, context awareness, robustness, privacy preservation and explainability of trust evaluation, two of the former having been seconded by Wang et al., (2022). They argue that although there are several works  that address trust issues in the context of heterogeneous nodes with diverse capabilities and characteristics, very few works focus on trust issues arising from heterogeneous architectures, networking technologies and protocols. The need for service management and integration, maintaining QoS and integration through mobility and roaming means that this poses challenges in future integrated heterogeneous networks due to differences in security requirements. This makes it very difficult to evaluate, transfer and maintain trust among different devices, protocols, architectures, and network operators. This calls for a context-aware trust model that can adapt itself in different contexts based on contextual information including device types, network types and security requirements. Moreover, most trust models only focus on trust metrics regarding specific contexts and fail to evolve with context changes for different enterprise needs.

### Need for Dynamic Access Control

Static role-based access control (RBAC) mechanisms traditionally used in enterprise networks are insufficient to handle these trust related misuse and intrusions posed by heterogeneous environments. The need for dynamic access control arises due to factors such as dynamic contexts that result from devices, data, users, and applications frequently changing states and the need to adapt to these changes in real time. Secondly, there is an increased attack surface

because of the exposure of more vulnerabilities due to the diversity of components and their interactions. Thirdly, the need to stop attacks in real-time and reduce the impact of attacks by immediate adjustment of access policies based on risk assessments and evolving threats further denotes need for dynamic policies. Dynamic mechanisms also need to be lightweight for devices with limited computational resources significant computational overheads that arise from the required context awareness. Finally, having a dynamic policy should continuously checks access requests ensures adherence to ZT principles where access is continuously verified and never assumed, necessitating context-aware, real-time policy enforcement. Dynamic access control ensures that access decisions are context-aware, risk-sensitive, and responsive to the evolving network conditions.

### Context in Access Control in Heterogeneous Networks

Context-aware access control introduces situational awareness into access decisions by evaluating contextual parameters beyond static roles and identities. The basis for these contexts is the ZT pillars of data, device, network, application and user trust. User behavior is very subjective but their actions follow statistical patterns and  can be quantified and reviewed within a heterogeneous environment. The user trust context is quantified based on the effect of a user activity on the data, application, network or device. As such, the user pillar is distributed across the other four pillars and their previous transactions quantified as the inertia or residual trust value that is decayed over time. The possible identities considered for each of the pillars have been highlighted in TABLEX. Contexts in heterogeneous networks therefore is considered on the following dimensions based on ZT pillars:

Table .:Zero trust Adhering Context-Awareness Parameters for Heterogeneous Networks

- Data Context: Information such as data object, data type, sensitivity, user identity, role, behavior, location, and session activity. These can be used to denote metadata on the requested resource.  It will also consider user related context based on data collected on the user’s activities in the ecosystem. The initial trust value based on the previous transactions will be used as the inertia or residual trust value that is decayed over the time domain.

- Device Context: this contains information such as Device type, security posture (e.g., compliance with policies), and hardware trust levels.

- Network Context: this addresses real-time network conditions, such as traffic patterns, latency, bandwidth, and detected anomalies.

- Application Context: it focuses on application-specific security requirements, usage frequency, and sensitivity of accessed resources.

- User Context: this dimension focuses on data elements that represent user classifications and metadata that can be used to determine user access permissions, scenarios or contexts. The activation or enabling of multi-factor authentication across network environments is a good example of a user context indicator. Other sub contexts metadata would include user groups, password hygiene  adherence and  user awareness coefficients where applicable. Values such as user awareness or cyberhygiene coefficients can be modelled from supplements such as trainings and cyber threat intelligence reports based on malicious transactions and violations of security policies across the temporal domain

- Temporal Context: This addresses the residual trust value based on previous user activities since the trust value is a score-based value. To avoid weighting historical data heavily, the residual trust is decayed as logarithmically to represent a natural decay

By dynamically incorporating these contextual attributes, access control mechanisms can make informed decisions that align with a heterogeneous network's security posture and operational needs.

### Trust Threshold as Determinant in Access Control

Trust threshold act as a dynamic determinant for access decisions in heterogeneous networks. The trust evaluation process involves calculating a trust score for entities (users, devices, networks, data and/or services) based on observed behavior and contextual factors. Key aspects include:

- Dynamic Trust Scores: Trust is not static but evolves based on real-time assessments of contextual factor discussed above and historical behavior.

- Threshold Enforcement: Access decisions are made based on whether an entity's trust score meets or exceeds a defined threshold. Entities below the threshold will have restricted or denied access.

- Context Sensitivity: Trust thresholds adapt to changing conditions. For example, during a high-bandwidth event on the networks, thresholds may increase to enforce stricter access policies.

- Zero Trust Integration: Trust thresholds align with Zero Trust Architecture principles, ensuring continuous verification and conditional access based on real-time analysis.

- Anomaly Detection: Sudden deviations in trust scores (e.g., suspicious activity or compromised devices) trigger dynamic access restrictions and security responses.

The use of trust thresholds enables fine-grained, adaptive access control that balances usability, security, and operational efficiency in complex heterogeneous environments.

This work thus shows the need to design an adaptive and dynamic trust model that considers enterprise networks with different contain heterogeneous contexts. The model should collect sufficient contextual information on network types, applications and the requirements for networking rather than relying on just information such as location and user credentials. The contextual information is described in detail in Table 1. By using this information, the trust model should be correspondingly adjusted by an efficient trust evaluation strategy. The proposed evaluation strategies dynamic weighted sum and subjective logic Their suitability are highlighted by Wang et al., 2022 .

## Network Infrastructure Identities and User Trust Calculation

In heterogeneous network environments, identity plays a pivotal role in determining access control policies and trust score calculations. These identities can be considered across the 5 pillars of zero trust to provide a more representation of context and consequently a more dynamic policy for access control enforcement. Each ZT facet can be evaluated as an independent set of identities that are cumulated then weighted for an overall trust score computation. The multiplicity of identities across the facets ensure that trust scores are representative of a risk profile for an access request before the decision is made. The trust score is then checked against a trust threshold range to determine the type of access decision made. The multiplicity of identities emerges due to the diversity of devices, protocols, and users, and it directly influences the accuracy of trust evaluation. Key identity sources  for this work include:

Data Identities: These are attributes that indicate important aspects or attributes of data to consider. They include properties such as

Data Integrity: Reflects the accuracy and consistency of data. Integrity violations, such as tampered records, can have severe implications on trust.

Data Confidentiality: Measures the sensitivity of the data and the need to prevent unauthorized access to sensitive data. It also represents multilevel security requirements and confidentiality needs at each level. This parameter is crucial in enterprise contexts handling confidential information, such as healthcare, security and finance.

Data Freshness:Users may possess multiple roles and credentials within the network (e.g., employee, administrator, contractor).

Data Authenticity: Gauges the reliability of the data source. Data from verified sources is more trustworthy than anonymous or unverified sources.

User Identities: These are properties  that can be used to describe and quantify user behavior and interactions with a heterogeneous network

User credentials: Identity factors such as biometrics, certificates, and role-based permissions form the basis of trust evaluation.

User roles: Users may possess multiple roles and credentials within the enterprise ecosystem with the possibility of changing roles  or having multiple roles in different contexts e.g., employee, administrator, contractor).

User MFA: this measures the user activation and utilization of multifactor authentication profiles as well as the need to adaptively include additional factors with suspicious user activity

Transaction Profile: this reviews profile building activities such as login history, misuse and unauthorized access cases and the successes and failures of previous transitions

Device Identities: Devices are identified by unique attributes, including IP/MAC addresses, hardware IDs, and certificates. In heterogeneous environments, devices like IoT sensors, edge nodes, and mobile platforms often carry distinct, context-dependent identities. Some of the considerations include an identity score based on anchor values such as MAC addresses, OUIs or digital certificates. Other derived odentitiies such as node reputation based on vendor or historical data and compliance scores can also be used to weight the device tenet.  Interface types and firmware updates can be used to derive a compliance score based on enterprise specific requirements

Service and Application Identities: These include identifies such as cloud services, microservices, and virtualized applications maintain dynamic and unique identities that interact with users and devices. Paremeters such as Code signing, vulnerability score, permissions requested can be used to calculate trust levels within the application domain. These can be enforced  based on Application allowlists or  runtime behavior analysis.

Network Context Identities:Network segments, such as VLANs, SDN flows, or software-defined perimeters, contribute to identity multiplicity. These identities reflect real-time connections and can dynamically change based on topology or context. Other attributes such as IP addresses and segments, traffic patterns and protocol compliance can be measured based on transmission of data through encrypted communications and  deviation from baseline.

The multiplicity of these identities necessitates aggregation and correlation across diverse, dynamic sources for unified trust evaluation, to make accurate access decisions. The trust estimation thus becomes a mathematical function of ZT facets as illustrated in Equation 1.

### Trust Calculation as a Factor of Identities

Trust estimation in heterogeneous networks relies on evaluating and aggregating the multiplicity of identities mentioned above. While these are cumulated across the facets of zero trust, the final trust value is considered as a dynamic weighted sum of  the cumulated values per facet. Trust calculation is influenced by the following factors:

Identity Correlation: Trust is established by correlating various identity attributes including user trust, device posture, application trust, data sensitivity, and network trust.  A contextual and stronger correlation among identities leads to higher confidence in trust estimation.

Per-scenario Behavioral Analysis:  Trust scores are adjusted based on observed or existing behavior of the identified entity within the enterprise environment e.g., activity anomalies, usage patterns, or deviations from expected policies. Different network with varying contexts can have varied weightings

Dynamic Contextual Attributes: Context-aware parameters such as time of access, geographic location, and real-time threat intelligence) impact trust calculation. Organizational contexts such as existence of BYOD and remote working policies may also influence the weighting on device, application or network posture leading to a more dynamic application of access decisions policies within the heterogeneous enterprise environment. An entity may have a fluctuating trust score depending on the context in which its identities are validated.

Risk-Based Trust Modeling: Trust is calculated as a function of risk scores associated with the multiple identities of an entity as well as the temporal context. The trust score is a function of weighted trust of all facets and the initial trust for each trust as illustrated by the generic equationX. The temporal is introduced as a natural decay function of the initial/residual trust referred to as inertia trust. The general equation can be represented as:

Trust_Score=f(Data trust, Device Posture, Application infrastructure, User trust, network-trust Factor)+Inertia-Trust

Equation . Eventaual trust score as a function of Zero Trust pillars

Where TS is the eventual Trust score, DT is the data trust score, DP is the device posture trust score, AT is the application trust score, UT is the user trust score and NT is the network trust score. The residual trust is the initial trust value resulting from the last known transaction or a decayed trust value of the previous estimation iteration. λ = Trust decay rate (aging factor), t = Time since last validation

Threshold-Based Evaluation: Calculated trust scores are compared against predefined or dynamically updated thresholds to make access control decisions. The access decisions can be full access, restricted access or denied access. Variations and/or combinations of these can be derived to have more granular access decision options. Entities that fail to meet trust thresholds may have restricted or denied access. This illustrated in equation 2

This comprehensive approach ensures that trust estimation remains dynamic, scalable, and responsive to the diversity and context of networked identities in heterogeneous enterprise networks. The telemetry data is collected  from the network, normalized and weighted for context. Access enforcements (e.g., MFA success, device compliance) are modeled as:

Trust Decay: reflects the temporal degradation of trustworthiness due to potential changes in entity behavior suchas  device compromiseor user privilege escalation, evolving threat landscapes such as  new vulnerabilities or other context chages such as session iunactivity or roaming. Residual trust is decayed based on an aging factor based on empirical data for most enterprise devices as illustrated by equation 3

T(t)=T0​⋅e−λt where T0​ = Initial trust score, λ = Decay rate (per hour) and t = Time elapsed since last trust validation.

### Dynamic and Context-Aware Trust in Heterogeneous Network Environments

This works considers both dynamicity and context awareness in heterogeneous networks. A dynamic and context-aware trust model serves as a foundation for adaptive access control. The dynamic nature of these environments requires trust models to be flexible, real-time, and responsive to changing conditions. The proposed work thus integrates the following aspects

- Dynamic Trust Evaluation: Trust is continuously monitored and recalculated based on real-time data from multiple identity sources. Entities may have fluctuating trust scores as network conditions, device behavior, application infrastructure, or user actions evolve.

- Context-Awareness: incorporation of real-time situational parameters, such as a temporal Context to ensure data freshness and anomalies are considred in making access dcisions. Anomalies: Access requests made during unusual hours trigger trust reassessment. Location Context adds onto the network posture amd esnures: Device access from unfamiliar locations may lower trust scores and Device Posture: Outdated or compromised devices reduce trustworthiness dynamically.

- Integration with Zero Trust Principles: Dynamic trust aligns with Zero Trust Architecture (ZTA), where access is never granted by default. Continuous verification of user, device, and network identities forms the basis for trust reassessment. Dynamic trust ensures that even trusted entities are subject to continuous monitoring and validation.

- Trust Decay and Recovery: Trust scores are designed to decay over time if an entity does not interact with the network or if anomalies are detected. Reassessment mechanisms allow entities to regain trust through corrective actions, such as software updates, reauthentication, or security compliance checks.

- Scalability and Adaptability: Dynamic trust models scale to handle the vast diversity of devices, users, and services in heterogeneous environments. Context-awareness ensures adaptability to evolving network policies and threat landscapes without manual intervention.

The multiplicity of network infrastructure identities, combined with dynamic and context-aware trust evaluation, ensures that access control mechanisms remain robust, adaptive, and secure. By incorporating real-time identity validation, behavioral analysis, and context-awareness, enterprises can achieve a fine-grained, responsive trust framework that aligns with modern security paradigms, such as Zero Trust Architecture. This approach is critical for managing trust and enforcing access control in complex, heterogeneous network environments.

## Performance-Centric and Trust-Centric Approaches in Heterogeneous Enterprise Networks

Heterogeneous enterprise networks, characterized by the coexistence of diverse devices, protocols, and applications, present unique challenges in achieving both optimal performance and robust trust management. Addressing these challenges requires a balance between performance-centric and trust-centric paradigms, each catering to distinct yet interconnected priorities in network operations.

### Performance-Centric Approaches

Performance-centric designs prioritize network efficiency, scalability, and resource optimization. Key metrics include end to end latency for access to services, packet loss ratio and final throughput achieved considering the access control decisions. Key considerations include:

Scalability and Latency Optimization: Enterprise networks often operate under strict performance requirements, necessitating low-latency communication and seamless scalability. Techniques such as Software-Defined Networking (SDN) and Network Function Virtualization (NFV) are leveraged to dynamically allocate resources based on real-time demands (Wang et al., 2018).

Quality of Service (QoS): QoS mechanisms ensure differentiated treatment for various types of traffic. By implementing bandwidth allocation policies, prioritization schemes, and congestion management protocols, enterprise networks can maintain performance standards even under high traffic loads (Chen et al., 2017).

Energy Efficiency: Energy-efficient routing and device management are critical in heterogeneous networks. Protocols like Energy-Efficient Ethernet (EEE) and adaptive power management techniques contribute to reducing operational costs and environmental impact (Ali et al., 2019).

### Trust-Centric Approaches

Trust-centric frameworks focus on ensuring secure and reliable interactions among network entities. This involves:

Trust Metrics and Models:Trust is quantified using models that incorporate behavioral and contextual factors. For example, node reputation, interaction history, and environmental context are combined to derive trust scores that inform access control decisions (Luo et al., 2019).

Dynamic Trust Management: In dynamic environments, trust evaluation must adapt to real-time changes. Context-aware mechanisms that integrate Zero Trust Architecture (ZTA) principles, such as continuous verification and least privilege access, are critical for mitigating insider threats and ensuring robust security (Khan et al., 2020).

Anomaly Detection and Response: Trust-centric systems often incorporate anomaly detection algorithms to identify and respond to malicious activities. Techniques based on machine learning, such as Support Vector Machines (SVM) and neural networks, have shown effectiveness in detecting anomalous patterns in heterogeneous networks (Sharma et al., 2021).

### Integrative Strategies: Balancing Performance and Trust

In modern enterprise networks, achieving a balance between performance and trust is imperative the most commonly used metrics include a dynamic trust score value that is weighted and updated based on context and time decay factors and deterministic decision basd on the final trust threshold value. Integrative strategies include:

Policy-Driven Resource Allocation: Policies that dynamically allocate resources based on both performance metrics and trust scores can optimize the dual objectives. For instance, higher-priority traffic from trusted nodes may receive preferential treatment during congestion scenarios.

SDN-Based Trust Frameworks: SDN facilitates centralized control, enabling the integration of trust evaluation into network management. This approach allows for real-time adjustments to routing and access control policies based on trust levels and performance metrics (Jiang et al., 2020).

Context-Aware QoS: Combining context-aware trust evaluation with QoS mechanisms ensures that trust-centric security measures do not degrade network performance. For example, devices with high trust scores may be granted expedited processing without compromising security (Zhou et al., 2018).

#### Challenges to Integrating Trust and Performance Centric Models

Interoperability: Ensuring seamless interaction among diverse devices and protocols remains a significant challenge. Standardization efforts and open-source platforms can help mitigate interoperability issues (Goyal et al., 2019).

Scalability of Trust Models: As networks grow in size and complexity, the computational overhead of trust evaluation frameworks must be addressed. Hierarchical trust models and distributed computation are promising solutions (Ahmed et al., 2021).

Integration of AI and Blockchain: Emerging technologies like artificial intelligence (AI) and blockchain hold potential for enhancing trust-centric frameworks. AI can improve anomaly detection and trust prediction, while blockchain offers tamper-proof trust records (Yao et al., 2020).

By adopting integrative strategies that harmonize performance and trust considerations, heterogeneous enterprise networks can achieve resilience, scalability, and security in increasingly dynamic environments.
## Related Works on Heterogeneous Enterprise Networks and SDPs

### Zero trust Using Network Micro-Segmentation

This work considers network security a network security architecture that supports zero trust approach, based on a concept that inspects network traffic for port and protocol information to allow authorized communication. It uses Illumio a network micro segmentation tool to demonstrate Zero Trust at the network layer, this tool uses the concept of labelling to write policies to whitelist traffic between the source and the destination. The tool has two major components Policy Compute Engine (PCE) which is the brain of the tool and Virtual Enforcement Node (VEN) agent that send telemetry traffic information between the source and destination to the PCE. The policy compute engine is used for writing and enforcing the policies based on the traffic information sent to whitelist the traffic between the source and the destination. The tool takes over the host-based firewall on the source and destination where the Virtual Enforcement Node (VEN) agents are installed and allow only the whitelisted traffic.

Networking controls can provide critical controls to enhance visibility and help prevent bad actors from moving laterally across the network once the network is compromised. Networks should be segmented based on the business criticality and requirements (including deep in network micro-segmentation) to provide real-time threat protection, end-to-end encryption, monitoring; analytics should be employed (Sheikh et al., 2021)

### Multilevel Security Framework for NFV Based on Software Defined Perimeter

This work proposes a Software-Defined Perimeter (SDP) as a framework to provide logical perimeters around these services, restricting network access and connections to the SDP-enabled Virtual Network Functions (VNFs) to trusted clients only. Several security benefits present themselves because of a combined NFV-SDP architecture. The deployment

and access control are customize-able, catering to a wide array of user needs. The SDP controller and gateway deployed as VNFs that reside in front of all other network services. The gateway acts as the first VNF, in which all traffic is redirected through and then to the appropriate service based on permissions defined by a controller. SDP is heavily permissioned and blacks out all services behind it to unsecured networks. Only traffic that sends the initial SPA and is from known/trusted sources will be forwarded to the available list of accepting hosts. This structure offers several security benefits to combat existing NFV issues. It eliminates the potential for DDOS attacks, which is when multiple compromised systems flood a resource to purposefully overload critical services, as packets will be dropped before they can reach said services. It can also prevent hypervisor attacks, remote connection attacks and VM hopping as no traffic will be allowed to reach services for which they have not been authorized (Singh et al., 2020)

### On the Malware Propagation in Heterogeneous Networks

This work explores malware spreading in heterogeneous networks using epidemiological

modeling. While most malware have similar patterns to epidemological trends in suspection, infection and recovery, the replication is more pronounced in modenrn heterogeneous environments involving multiple users, shared devices and common applications across these devices in networks. The model incorporates heterogeneity among three components of a network: software, hardware and network type and also allows for  disticntion between both cyber and non-cyber-related impacts. Almost every network user possesses several types of communication devices that are being used in different locations, under different

environmental conditions, situations, and time frames. For example, commonly used devices include but not limited a desktop, laptop, and smartphones also consist of multiple network interfaces such as cellular, Bluetooth and WI-FI cards. These devices can share common forms of use, they all have distinctive characteristics, strengths and weaknesses. It is likely that the devices belonging to one user have shared software installed allowing for execution of the same files and applications (Alexeev et al., 2016). The work uses a SIR type epidemiological model applied to health applications to consider three states: Suspected-Infected-recovered to represent vulnerable-compromised-patched states in heterogeneous networks. It considers a network that includes devices of different types and/or platforms and different software, allows for non-cyber-related “mortality”,i.e.. not induced by malware or virus such a situation is a user or/and device failing due to misconfiguration, environmental or physical conditions, and allows for a cyber-related mortality,(malfunctioning due to malicious effect of malware or virus. While the work numerically represents scenarios for malware propagation, it assumes a relatively static network topology. It also assumes traditional malware types like viruses and worms and does not factor in newer threats such as advanced persistent threat, metamorphic and polymorphic threats that try to evade security tools such as sandboxes. Among useful results, is a discussion of the delay in malware propagation between different types of the devices connected to

the network. The unified approach taken in this study aggregates and extends models of malware spreading that either do not account for network heterogeneity or allow for heterogeneity within one component, e.g. software.

### A Survey on Trust Models in Heterogeneous Networks

This works looks at hetterogenous networks as merged and integrated next generation networks that support sharing of resources among users. It focuses on heterogeneity, openness, distribution and multi-domain environments that result from the evolution of enterprise networks. This makes them more sucsceptible to attacks due to vsrious attacks due to increased surfaces of exposure on devices, networks and users. Additionally, trust and reputation issues arise due to varying contexts resulting from thus evolution. While trust is active within heterogeneous networks reputation is passive and dependent of the perceptio of a domain of peers on an individual peer. The trust value can be influenced by reputation insome instances and is considered objective and acknowledged as a score by a specific communicty. This introduced the quality of trust as phenomenon that is used to gauge and determine the  trustworthiness of the trust calculation process and trnsmission to other nodes. The quality of trust may also be related to the effectivess of data forrwading, energy consumption, privacy preservation andexpalinability of the process. Whil these parameters are largely menrioned by other authrors, Wang et al., 2022 focus on nine parametrs to measure th quality of trust through  three categories of trust models: trust evaluation, trust decision and trust management categories for effective trustwirthy networking  as applied 5G and beyond networks.

Subjectivity, dynamicity  and context awareness  emerge as the first 3 parameters for QoT  evaluation. They focus on the evidence as proof of trust in all scenarios despite their incompleteness and contradicting nature, the evolution and changes of this eveidence across time  as eidenced by trust gaining and decay  as well as the ability to adapt and weight these dynamic aspects based on background, application scenarios  and changing network, data and users consitions. Dynamicity and context awareness are particularly vital in representating changing relationships and their importance for a speicific enterprise. Privacy preservation, scalabilit an drobustness also emerge as impritant QoT metrics to ensure sensitive user data remains hidden, the processing time and load and maintained wihtin acceptable threholds and the ability to perform the trus evaluation in quickly changing network domains does not lave trust ecvaluation susceptile to trustnd reputation attacks such as identity, recommendation, transmission-related and other attacks. Explainability and user acceptance metrics underscore the need for the models to adhere to the principle of psychological acceptability in guiding the collection of data, contextualizing the process and explaining the outcomes for users’ recoginition and understanding of the trust management process.

The authorrs also define ttaxonomies of trust models in detail, discssing decision evalution and management models. While decisions models are based on the verdict, evaluation models infer the values based on statistics, reasoning or cognitive machinelearning approaches. The trust models focus on trust tranmisision and reputation scores which are based on centralized, semi-centralized and distributed structures such as distributed ledgers or Fog based environments

The authors further evaluate the taxonomies oftrust models (decision, evaluation and management) based on the nine metrics while comparing their work to other trust evaluation works. The culmination is a disussion of  open issues and future research areas are discussed. Heterogeneity and context awareness are critical areas that need to be evaluayed to have dynamic and context aware trust adapting to varying computing contexts expecally with the heterrogeneity of enterprise networks. Additionally, trust verification, transmission and explainability need to be achievable for any models developed to make trust decisions. The cold start issue is particilarly importamt to dynamicity and trust awareness for new devices that join the network (Wang et al., 2022).

While ths work is relatively exhautive, it does not provide a baseline of parameters to consider in trust evaluation. A considerstion of tenets of zero trust would provide this. Addtionally, the trust alagorithm  could be based on dynamic weghted sum of these tenets coupled with subjective logic to ensure  adequate context awareness for diffrenete hetenets wile applying trust decay to  have more relevance for recent events. An SDP bsed testbed can also be used to provide a centralizedyet robust approach to trust managemnt while abstracting the network resources particlualry for roaming users and other users who introduce the cold start problem.

### Building a Software Defined Perimeter (SDP) for Network Introspection

This work by Lefebvre et al. presents a practical and incremental contribution on SDPs by proposing an architecture capable of continuous network introspection and dynamic policy enforcement and validating the proposed enhancements and performance within a modern cloud environment. The primary conceptual advancement is the evolution of the SDP Controller from a static authentication authority to a dynamic, real-time security orchestrator in line with (SDP specification (CSA 2.0)) which focused on strong initial authentication and service hiding. The  work correctly identifies a gap in the lack of continuous security monitoring after a connection is established. By enhancing the control channel to stream real-time data channel telemetry e.g., packet metadata to the Controller, the authors introduce a continuous trust evaluation mechanism, which is a cornerstone of mature Zero Trust Architecture (ZTA). This shifts SDP from a one-time gatekeeper to an active, participating entity in the network's security posture. It also reinforces the critical role of the SDP Gateway, positioning it not just as a conduit, but as a strategic point for security introspection. The conceptualization of the Gateway as a locus for deploying Virtual Network Functions (VNFs)—such as TLS interception, behavioral analysis, and policy enforcement—is a powerful and flexible model. It enables "defense-in-depth" by allowing multiple, layered security controls to be applied dynamically based on policy or trust scores, without modifying the protected Accepting Hosts (AHs). Additionally, the authors enhance the SDP acrhitecture by offloading security functions to the Gateway and Controller and alowing the AHs (the actual services) to remain focused on application logic. This is a highly practical insight, especially for SaaS providers and cloud-native environments, as it simplifies compliance and security management. The authors focus on validating the  architectre on a AWS powered geographically distributed testbed and the systematic use of iperf3 to establish a performance baseline for the experiments. Telemetry data us  collected across eight different network edges over a five-hour period provides a robust dataset that accounts for real-world network traffic and conditions variability. The objective of the experiment is to determine if using a gateway for network introspection incurs any prohibitive performance penalty. The results convincingly demonstrate no significant traffic load  to affect performance and no degradation in IH-GW-AH compared to the direct "IH to AH" baseline.

While the use of off-the-shelf tools like nginx, tshark, and netcat is a pragmatic choice for a proof-of-concept to demonstrate core data flow and functionality. the approach is also a limited to a static solution rather than a natively integrated SDP component. The article also focuse on performance feasibility but does not demonstrate security efficacy of the prototype. The prototype captures and streams packet metadata (headers), but it does not implement or test any advanced security policies, anomaly detection algorithms, or automated response mechanisms (e.g., tearing down a connection upon detecting malice). The exclusive focus on bandwidth is a significant limitationsince most real-time and interactive services rely on other network properties such as latency and jitter as critical performance indicators. The processing delay introduced by the Gateway for packet inspection and metadata generation could have a substantial impact on application responsiveness and it could also grow signifcantly if more context oriented data is collected and rocessed by the controller . The scalability of the Controller's telemetry processing capabilities as the number of Gateways and data channels would also increase the latency significantly; this is left unaddressed by the article. Attacks on the controller and gateway as targets of denial or service have also not been addressed. Scaling the prototype based on bandwidth and network conditions  of other geaographcal placements and increased CPU resources would be a good test on scalability. The inclusion of application layer (layer 7) inspection, automation and orchestation of telemetry correlation, dynamic trust score claculation, remedial actions orchestration, standardization of inspection proceduresand use of distributed SDP ontrollers would have higher fidelity representation of network consitions.

### A Consideration of Scalability for Software Defined Perimeter Based on the Zero-trust Model

This work looks at the needs for trust  in enetrprise envrioenmnets with increased diversity of devices and the indequacy of previous security technologies such as PKI and VPNs. While the zero trust model guides on considerations for  identity verification across multiple facets, the authors focus on scalability of the rchitetcure on which zero trust sits. They propose a sdp model that is scalable for trust centric models and are easier to install, deploy and manage. The SDP architecture is used to provide access control to resources based on user contexts and nor ncessarily credentials while abstracting the services from the end users. The abstraction of tehse servicves  and organization infrastructure based on users contexts and limitation of unauthorized users from accessing protected resources based on least privillege. The SDP architecture consists of a controller, an Iniatiating Host (IH) and an accepting Host (AH). The controller is the central node that authenticates and controls access to for end users to access resources  on servers (AH). The devices that users interact with access resources are the Initiating hosts (IH). Once the controller authebticate a user, it instructs an AH to form secure tunnel based on mTLS  through which data exchange can take place. The controller thus acts as the go-between the AH and IH performing the first level authentication for an IH and providing instruction on how to get to an AH. While this is very effective for secure tunneling, the scalability is always a challenge especially when authetication is based on multiple attributes such as the tenets of zero trust. Cloud based scaling and complex operation procedures also great hinder the  adoption of  SDPs for large enterprises.

The authors propose four models to be considered for scalability including hierarchical, brideged, hybrid and mesh models. The hierachical is based on a tree strcuture like the DNS system and needs controllers to  interact with IH and AH at the leaves and intearct with parent and root controllers upstream. This model is hughly structured reulting increased end to end deays and increased surfaces of attacks. It however provides more persistence if the controller nodes synronize the information across the three levels. The bridegd model introduces a  a bridge controller that can be used as an intermediate node two root controllers resulting in faster interworking and inter-authentication between two controller domains. While this provide higher flexibility and interworking, the management and maintenance of persistence especially across the bridge and root nodes is complex. The hybrid model  combine the hierarchical and bridged models resulting in an intermediate parent-bridge node to avoid reference to the root model and consequetnly an extra hop to the root level. This introduces more complexity and cost of the hybrid and bridge nodes in the topology. The flexibility and interoperability are however significantly improved. The mesh topology provides for  a mesh network on controllers that cnnect to AH and IH resuting in higher flexibility annd ans interoperability, the cost of of these multiple nodes, syncronization and management of these controllers as peer nodes however increases exponentioally. The authors provide 4 separate models of scalability to be considered based on desk evaluation; they do not perform any experiments to evaluate implemenatoin  for actaul metrics on bandwidth, load and end-to-end latency. Their focus is also on additional nodes for bttr interwoking and flexibility  and fail to consider the additional surfaces of attack introduced by he bridge andhybrid controllers. They also fail to consider syncronization and caching complexities between levels of controllers.

### Leveraging Software Defined Perimeter (SDP), Software Defined Networking (SDN), and Virtualization to Build a Zero Trust Testbed with Limited Resources

This work looks at the confluence between  Zero trust networks, zero trust protocol design, and zero trust software engineering a Zero trust by design architecture. It further looks at how zero trust features can be encapsulated on software defined perimeters (SDP) and be combined with the power and flexibility of software defined networking (SDN) and virtualization to build a zero trust testbed with limited resources. The objective was to  show SDP both aligns with key elements of zero trust architecture (ZTA) and contributes to satisfaction of core principles of Zero Trust by Design (ZTBD) and facilitate design and implementation of zero trust testbeds in support of the continued evolution of zero trust research and practice while growing body of knowledge. The work combines the fundametals of zero trust defined by NIST in removing any implicit trust (NIST) and the definitions of ZTBD (ZTBD) to have augmentation of zero trust patterns in resusable and expandable solutions. The work further highlights how SDPs  flexibly provide an overlay network with dynamic trust provisioning and secure access, supporting protection of applications and services being accessed over an untrusted network. With SDP, resources are hidden from unauthorized parties until identity-centric trust has been established. This shift from a legacy mindset of static, perimeter focused security with trusted “internal” networks to a dynamically adaptive logical micro-perimeter requiring trust establishment. The SDP architecture highlighted in SDP specification 2,0 aligns with SDN foundations in separating the control and data planes based on the SDP controller and Accepting host (with or without a gateway that abstracts the service). These map onto ZT’s PDP and PEP respectively making this fit into virtualization platforms that provide OpenFlow functionality which in turn avails controller functionality for both virtualized and emulated environments. The simplest setup was based on Mininet, a virtualized emulator tool that facilitates rapid prototyping of large, complex network structures in resource constrained environments such as a typical laptop. It combines very lightweight virtualization with the versatility and power of SDNs to enable a plethora of complex testing capabilities that would otherwise require significantly more resources. The work also considers the capabilities of boxes that would comfortably support this tool based on processor and memory evolution in the last decade. Further modifications and programmability of the network are enhanced through python scripts. More complex ad high fidelity use cases can be introduced by transition to  type1 and type2 hypervisors, adoption of specialized services based on Googles beyondcorp service  and other open source tools for IAM, vulnerability assessment and MFA  tools for more accurate representation of services. Transition to cloud-based nodes can provide more computational resources and on demand scaling for larger and more service oriented network use cases. Due to the virtualized nature of the interaction of nodes, representation os cloud native services, secure service edged and real-world SLAs with service providers may be difficult to emulate.

### On SDPN: Integrating the Software-Defined Perimeter (SDP) and the Software-Defined Network (SDN) Paradigms

The work introduces a Software-Defined Perimeter Network (SDPN), as a novel framework that merges Software-Defined Perimeter (SDP) and Software-Defined Networking (SDN) paradigms with Zero Trust (ZT) principles to create a virtual, scalable perimeter for modern distributed networks. This is motivated by the limitations of traditional "castle-and-moat" perimeters in virtualized, cloud-hybrid environments. This framework abstracts network elements into a unified model with data, control, and application planes and emphasizes cryptographic trust anchors, node abstractions (perimeter, service, host), and protocols for dynamic management, aiming to reduce attack surfaces and enable seamless inter-network peering.

SDPN separates functionality into data (nodes for enforcement), control (logical controller as trust anchor and PDP/PEP manager), and application planes (extensible apps like trust tables for ZT decisions). This multi-plane model unifies SDP's between-network trust such as use of SPA for abstraction with SDN's within-network control such as flow management. It also embeds ZT tenets (no inherent trust, continuous verification) via a cryptographic trust anchor (root certificate from a third-party), enabling granular, risk-based decisions using trust tables that evaluate factors like device health and CTI. Devices are simplified into nodes  including perimeter for routing/security, service for servers, host for clients), managed via control channels. The framework also defined protocols procedures such as Join/Leave for onboarding/revocation, Peering for inter-SDPN trust and incorporate SPA and threat-informed name resolution to hide services and block malicious IPs early. This ensures that the focus is not credentials verification rather contexts which  are ideal for perimeters that are logical, distributed yet centrally managed.

The authors define SDPN through logical abstractions, sequence flows, protocol sketches and  table comparisons of  detail components (controller as trust anchor), applications (e.g., threat-informed DNS), and protocols (e.g., SPA-enhanced flows). The test cases are based on known vulnerabilities for common  flos such as peering and ZT threats with little emaultion metrics on latency overhead and scalability

The outcomes show a unified virtual perimeter, reducing attack surfaces by concealing services (via SPA), enforcing ZT (via trust tables), and simplifying management (one controller for all nodes). Analysis of the sequence flows show reduced round-trips potentially lowering latency in distributed networks while threat-informed resolution blocks for CTI-flagged IPs early; trust anchors enable secure peering. Additionally, the application plane allows future integrations (e.g., IoT subtypes, ML-based trust scoring), making SDPN adaptable next generationnetworks.

This would however  result in bottlesnecks on the logical controller in large-scale deployments such as millions of IoT nodes. Relyiing  on a trusted third-party for root certificates also introduces a single point of failure in the case of a CA compromise or attacks on the its availability. Such attacks including DDOS would also affect control channels without specified protections especially during runtime verification (e.g., continuous node attestation). Merging SDP/SDN requires retooling through custom controllers and higher fidelity test cases,

As an improvement to the trust algorithm,  there is need  to develop formal models for trust tables for adaptive policies based on all the facet of zero trust and a temporal context that weighs recent telemetry data morefavoribaly over less fresh data. Additionally, for highly trust centric models, multi-controller  deployment, controller federation and  edge computing integrations should be considered for lower latency ZT enforcement in heterogeneous networks.

### Operation Management Method of Software Defined Perimeter for Promoting Zero-Trust Model

This work anchors on operational procedures for adoption of Zero trust promoting  SDPs within organizations in Japan. Tanimoto et al., 2023,  take note of the rise in teleworking post pandemic and the resulting information leaks and cases of internal fraud within organizations. Despite ZT being introduced as possible solution, there is little to no operational guideline to its adoption and as such, the authors set out to develop an operationalization process to help improve ZT adoption which has stagnated at less than 40% of organizations. Zero trust in a boundary-less network that considers internal users as possible threat to the network infrastructure and SDP as a ZT enforcing architecture that provides for continuous authentication and authorization of users and devices (IH) when accessing services on AHs. The reasons identified for poor adoption is a lack of procedures on securing and monitoring all resources, a dynamic policy that is representative of changing contexts and continuous authentication and authorization processes. Most authors looking at SDP testbed focused on attacks such as identity and DOS attacks on the infrastructure, decentralization of authentication procedures, SDP edge for delay sensitive applications in IoT environments and considerations for scalable models.  While these were vital to specific domains, they did not provide the specific details and message flows for ZT trust procedures in an operational context. Th authors therefore model an SDP operational model with authentication and authorization procedures and messages, operational scheme for a dynamic policy and evaluation of the procedures based on quality, cost and delivery time metrics. The culmination is the sequence of processes to guide operationalization of SDPs with a focus on dynamic policy, authorization and security of all resources. While the results were guiding and practicable for all variations of enterprises, the evaluation was mostly static and lacked context awareness for resources that ought to be accessed in different conditions. The QCD model is also limited in evaluation of scalability, dynamicity and explainability as metrics of quality of trust

### Toward a Trust Aware Network Slice-Based Service Provision in Virtualized Infrastructures

This work evaluates trust challenges in 5G network slicing, where virtualized infrastructures using SDN and NFV enable dynamic, isolated logical networks for diverse services. Varadharajan et al., (2022),  emphasize on trust based on verifiable properties (refered to as hard trust) over "soft" trust  based on recommendation and reputation, as a foundation  for secure 5G services. It evaluates trust, pre-deployment (static) and during operation (dynamic), demonstrating slight performance overheads (5-12% delay increase) while enabling malicious VNF isolation. The propose a model that evaluates direct trust properties and binary values to determine the trustworthiness of Virtual Network Functions (VNFs) and Virtual Machines (VMs) composing network slices. They suggest a logic-based policy language (LOPAT) for specifying trust properties such as "no_malware" or "correct_hash" at boot and runtime and a trust derivation algorithm to assess if components meet these properties. Additionally, a trust management architecture (T-MANO) integrated with Open Source MANO (OSM) for on-demand trust evaluation is also proposed. A prototype implementation on OpenStack/OSM, with performance analysis on delay, CPU usage and a dynamic attack mitigation is also presented.The paper innovates by extending property-based attestation  to 5G network slicing, a domain where trust models are nascent. Unlike binary attestation, which only verifies hashes, the hybrid approach (binary for boot-time, property-based for runtime) allows fine-grained, semantic trust evaluation such as mandatory access control. This is a novel application, bridging trusted computing with NFV/SDN, and addresses a gap in ETSI MANO standards, which lack runtime trust mechanisms. The LOPAT language is also a significant contribution: its predicate logic such as SatC for component-property satisfaction enables expressive, quantifiable trust policies without over-complexity. The tri-partite logic (trusted/untrusted/uncertain) handles real-world ambiguities, enhancing practicality for cybersecurity in dynamic environments. The architecture's integration with OSM demonstrates feasibility and a focus on multi-authority trust which aligns with 5G's multi-tenant nature, advancing trust in virtualized infrastructures.

The Evaluation is also robust as the prototype is on real hardware  and measures practical metrics ( delays, CPU usage, throughput) across varying VMs properties . The attack scenario (logic bomb with zsh shell exploit) validates dynamic mitigation, showing real-world applicability such detecting runtime compromises (e.g., malware injection) prevents slice-wide attacks like DDoS or data tampering. This is critical for 5G verticals (e.g., healthcare, utilities), where untrusted slices could cause catastrophic failures.

Despite the novelty of theprocesses, the model lacks integration with "soft" trust as highkighted by the authors. This is particularly important in 5G networks because of scenarios that involve uncertain behaviors such intermittent failures and on-off attacks, where hybrid models could be more resilient. Additionally, while the test cases were exhaustive, the use of 40VMs is not close o rpresentative of femtocells in 5G networks and beyond; the drop in throughput  could also be indicative of a drop in peformance that couls increase significantly in a fully scaled 5G networks. Further, the attack and misuse cases could be  used to represent other variations and diverse threats such as  side-channel attacks on VMs and containers as well as SDN controller compromises. Other 5G-specific threats like slice isolation breaches or orchestration attacks in multi-tenant environments have also been overlooked. Extension of the work to incorporate zero-trust paradigms for  5G and beyond networks should also be considered.

### A Software-Defined Zero Trust Framework for Secure Access Control and Micro segmentation using SDN and SDP

This work addresses a critical gap emerging from the inadequacy of perimeter-based defenses and the high cost/complexity barrier to ZTA adoption and  proposes a practical implementation of Zero Trust Architecture (ZTA) through the integration of Software-Defined Networking (SDN) and Software-Defined Perimeter (SDP). The authors beging by illustrating the synergies between these paradigms: SDN provides the granular, centralized control needed for microsegmentation, while SDP enforces the "never trust, always verify" principle through continuous authentication and authrization as well as least privillege access. This ensures that the core tenets of ZT are included in the process.

This is however undermined by independent implemebation of SDP and SDN components and not real-time integrationresulting ina not fully "integrated" framework where dynamic policy orchestration would feature an authentication event in SDP automatically triggering the instantiation or modification of SDN flow rules in real-time. The current implementation appears to be more of a co-located deployment than a seamlessly integrated system.The prototype is based on open-source components including OpenDaylight, OpenSDP, Open vSwitch, Samba which represent a replicatable  low-cost testbed. While most rules sre static and inadequate in representng a dynamic policy adaptation based on real-time contexts such as user role changes, device posture checks, threat intelligence feeds, the  controls are robust and foundational especially the focus on RBAC and password policies. Additional paradigms such as continuous validation, device health checks, and encryption of all traffic can be integrated in subsequent test vases and experiments

The results demonstrate the functional principle of microsegmentation and show that traffic halts when flow rules are flushed effectively proving segmentation. There is however no data on latency, throughput, or overhead introduced by the SDP gateway and SDN controller. As well as tes cases on active threats (e.g., penetration testing, lateral movement attempts from a compromised host) to quantitatively measure its effectiveness in reducing the attack surface.  A baseline comparison with  perimeter based security models would easily show the security benefits  and provide abasis for a more dynamic policy, context evaluation and automation of the policy deployment in the testbed. Further, the realtime collection of metadata to guide further inform the policy and model threats could be adopted  and used to show changing contexts in the temporal domain.


*📌 Takeaway: Heterogeneous enterprise networks have structurally outgrown perimeter security. Zero Trust defines what should be done—but not how trust should be computed dynamically. The next chapter formalises trust as a mathematical problem.*



---

# Chapter 3: Trust as a Computational Problem

*Chapter 2 demonstrated that heterogeneous enterprise networks have outgrown perimeter-based security and static role-based access control. The question now shifts from 'why do networks need trust?' to 'how should trust be mathematically modelled?' This chapter elevates trust from an abstract policy concept to a formal, computable system property, establishing the mathematical vocabulary used throughout the remainder of this thesis.*

# Trust in Context - The Power of Environment

"Shadows and Light: The Influence of Context"

## Trust Estimation and Trust Management in Heterogeneous Enterprise Networks

Trust is an abstract and subjective term that defines the process of recognition of an entity’s identity and the confidence on its behavior. In most contexts, the term ‘entity’ includes service providers and their personnel, data users and data owners. Trust is calculated and established through trust mechanisms that apply trust models. A trust model is a management method, process or protocol that includes trust calculation, establishment, renewal and trust withdrawal as argued by Georgiopoulou & Lambrinoudakis (2016). The calculation and management across heterogeneous environments however ought to consider special factors such as location, application versions, moving perimeters as well as types of processes within the infrastructure.

Level of trust is defined as the belief probability varying from 0 (complete distrust) to 1 (complete trust). In this sense, trustworthiness is a measure of the actual probability that the trustees will behave as expected. Trustworthiness is the objective probability that the trustee performs a particular action on which the interests of the trustor depend (Das & Debnath, 2020). Trust level thus has implications on the type and level of access entities are granted within different areas of the enterprise network infrastructure.

Trust management particularly in networks and communication, considers trust relationships among participating nodes that critical in building cooperative and collaborative environments to optimize system objectives in terms of scalability, automation, and orchestration, reconfigurability, and reliability of security mechanisms. The relations among entities that participate in a protocol are based on the evidence generated by the previous interactions of entities within a protocol. Trust management is thus the process of evaluating the quantified belief of a trustor regarding competence, security, and dependability of a trustee in a specific context of resource access. In a heterogeneous environment, trust management models compute trust as a function of multiple parameters as illustrated in Figure 2.5. Additionally, as reported by (Randhawa et al., 2017), information accuracy and trustworthiness are important prerequisites to a trust management process.  precision of facts and information have an impact on the accuracy of trust derived and as such denote an accurate computation of trust at estimation time. There is no power over the correctness of the inputs considered in deriving the trust value provided by the trust management process. False and inaccurate feedback may affect the reliability of trust management and level of trust of a resource provider.



[Figure/Image from source paragraph 428]

Figure .: Trust Parameters in Dynamic Trust Management (from: (Cho et al., 2011))

Trusts management processes can be static or dynamic in nature. In static trust management, rules are predefined within a trust engine; they have a predefined design and flow of the process of a transaction. In dynamic trust management, profiles in a trust model engine are defined as a factor of multiple input parameters which eventually define trust. A dynamic model considers other supplements such as future activities, unidentified process flows and adjusts with different parameters and progress based on the previous cached data.

(Georgiopoulou & Lambrinoudakis, 2016)  maintain that  an initial list of requirements that could be used for assessing  trust management include:

- Trust metric: This defines how to quantify trust between a resource provider and a user who consumes the resource. Since trust is abstract, a method of measuring the trust and defining the threshold for predetermined levels  should be defined. This ensures a stratified and graduated scale for trusts values.

- Abnormal behaviour: Behaviours that indicates the potential for misuse aor malware propagation is an important factor in loss of trust for entities. A behaviour that deviates from the pattern or an old behavioural history or even a short-term access, should result to zero trust. As a result, it is necessary to define which behaviour is perceived as normal within a network infrastructure. Furthermore, the weights and criteria (time, history, weights of normal vs abnormal) ought to be clearly defined

- Identity Management: trust management needs to ensure that the identities of the users are real through collection of trust related feedback. To this end it is necessary to authenticate the users. Thus, an identity proofing and verification scheme is important to achieve this goal

- Data Security: Trust management and relevant models are implemented as part of the overall security management scheme to control data access. Therefore, trust management should specify the minimum requirements for data access and thus for achieving an acceptable level of data security.

- SLA: This is the formal agreement between the resource providers and the users that clearly sets the requirements of both parties, particularly the non-functional elements of access. The SLA should be part of the trust management process.

## Trust Models

Trust models are essential components of trust and reputation Management in dynamic environments like heterogeneous enterprise networks. These models help assess the trustworthiness of devices,  applications and users based on their behavior and interactions compared to the defined policies. Trust models must include decision, evaluation and management facets  as illustrated in figure x.



[Figure/Image from source paragraph 440]

Figure .: Taxonomy of trust Models

They must consider the following stages:

- Initialization: This initial stage involves assigning inertial or residual trust values to  as a starting point entities when their behaviors are unknown. Entities start with a neutral trust value, which is adjusted over time based on interactions and behaviors across context defining facets. Enterprise contexts such as  mobile and enterprise owned devices  cumulatively add to this initial trust value to allow for more accurate trust assessments.

- Information Gathering: Trust evaluation relies on collecting realtime and stored information about entities through direct Interaction, indirect interactions or other telemetric data such as topology based metadata. While direct information provides more realtime and verifiable data, indirect data can be inportant  in building a broader understanding of trustworthiness. It however, requires at least one direct interaction to validate the information .

- Information Dissemination: Once information is gathered, it is propagated across the netework to an entitity or entities if decision making is done across distributed access gateways. This can occur locally (among neighboring nodes) or globally (across the entire network). The dissemination of trust information helps in updating and refining trust values across the network nodes.

- Trust Value Calculation: Trust values are computed using evaluation models, such as:

- Bayesian Inference: This statistical method calculates the probability of receiving more evidence about an entity's behavior, helping to derive direct trust values based on interactions .

- Dempster-Shafer Theory: This approach combines evidence from multiple sources to improve the accuracy of trust assessments, allowing for a more nuanced understanding of an entity's behavior .

- Decision Making: After trust values are calculated, decisions are made regarding resource allocation and collaboration. This is based on a defined threshold of trust scores that define full, restricted or denied access. For example, a central entity like an SDP gateway may use trust values to determine which nodes should have access based on their reliability and performance characteristics .

- Reputation Management: Entities with low reputation values (below a certain threshold) are identified as malicious and may be isolated or blacklisted. This process helps maintain the integrity of the network by ensuring that only trustworthy entities are allowed to participate in collaborative activities. The nodes responsible for maintaining the list of may be centralized, distributed or a hybrid of the two especially in sdistributed scenarios to overxome challenges associated with CAP theorem

These models are crucial for enhancing the security and efficiency of dynamic networks, as they help in identifying and mitigating risks posed by malicious entities while promoting reliable collaboration among trustworthy nodes. Trust models in heterogeneous networks (HetNets) can be categorized based on their design goals: decision models, evaluation models, and management models. Each type serves a distinct purpose in the context of trust management and has unique characteristics.

### Trust Decision Models Perspective

Decision models are designed to make access control decisions in complex environments based on predefined policies, rules, and strategies. They focus on determining whether an entity can be considered trustworthy based on certain criteria. These models are both entity centric and data centric since data can be directedly collected or deduces based on metadata and system reports They include

Policy-Based: These models rely on defined policies that constitute trustworthiness such as use of MFA, access from geofenced network segments or trusted devices. Rule based models that apply a set of rules to evaluate trustworthiness based on specific criteria, such as past behavior or compliance with security protocols and most authorization models such as mandatory, discretionary and RBAC systems are good examples of policy based models.

Expert-based: Some decision models involve human experts who define the policies representing the ground truth in a network. This can include setting thresholds for trust metrics based on expert judgment. They utilize human-defined policies to assess trust. For instance, if environmental conditions exceed normal ranges, the model may flag the data as untrustworthy.

Binary Decisions: Many decision models operate on a binary basis, where an entity is either trusted or not, which may lack granularity in distinguishing varying levels of trust. Most  of these are based  singular parameters with binary only outcomes

### Trust Evaluation Models Perspective

Evaluation models focus on assessing and quantifying the trustworthiness of entities within the network and the information they provide. The trust worthiness is calculated as a score that is compared to a threshold of value for access decisions. They provide mechanisms to evaluate trust based on various metrics and interactions. Statistical models such as weighted sum models and  reasoning models such as subjective logic approaches are good instances of trust evaluation models. Subjective logic models  such as cumulative and weighted belief fusion use a reputation based approach where feedback is a aggregated from multiple sources to compute a reputation score for each entity, which reflects its trustworthiness based on historical interactions. Probabilistic models such as and bayesian inference model use a probabilistic approach to evaluate trust, updating trust values based on new evidence and interactions. Some of the characteristics of  Trust evaluations models include:

Quantitative Assessment: These models often use quantitative metrics to evaluate trust, such as device compliance, network anomalies and/or reputation scores derived from past interactions.

Dynamic Trust Evaluation: Trust is quantified on a scale, usually between 0 and 1, where 1 indicates maximum trust and 0 indicates no trust. Values above a certain threshold (e.g., 0.5) are considered trustworthy. The threshold might also be ranges of values that influence the type of access decision made, especially in non-binary instances. Trust values in evaluation models can be updated dynamically based on new information or interactions, allowing for real-time assessment of trustworthiness. Given the dynamic nature of heterogeneous enterprise environments, trust management models must adapt to changing conditions. Trust evaluation must be  designed to ensure optimal trust management by utilizing maximum available information and handling uncertainty effectively .

Contextual Ontology factors: The use of ontologies in trust management allows for a structured representation of knowledge, enabling the system to infer new facts from existing data. This enhances the model’s ability to evaluate trust in a context-aware manner. Some evaluation models take into account the context in which trust is being assessed, recognizing that trust may vary based on different scenarios or environments.

Performance Metrics: Various metrics are used to evaluate the performance of trust models, including the number of events evaluated, the accuracy of trust levels, and the ability to detect malicious nodes. Effective trust evaluationn models must be capable of identifying and mitigating the impact of malicious nodes and users.

### Trust Management Models

Management models encompass a broader scope, focusing not only on decision-making and evaluation but also on the overall management of trust within the network. They aim to control, enhance, and maintain trust over time. Management models can adopt a holistic Approach where they  consider various aspects of trust, including how to establish, maintain, and enhance trust relationships among entities. Additionally, they should also  consider scalabilitysuch that by design, they can handle a large number of nodes and interactions, ensuring that trust management remains efficient as the network grows. Finally, they should also include Dynamic Adaptationwhere there is incorporation of mechanisms to adapt to changing network conditions and user behaviors, allowing for flexible trust management. Examples of management models include Centralized models that include a  defined authority that maintains trust values for all nodes, updating them based on observed interactions. While this  simplifies trust management it also  introduces a choke point and a single points of failure. SDPs and cloud based managemetn models are examples of centralized trust management models.  Decentralized models on the other hand distribute trust management across nodes, allowing them to maintain trust values locally. This enhances scalability and resilience but also complicate trust evaluation across different domains. This is more noticebale in decentralized acrhitecture like blockchain and DLTs. Semi centralized models are more common for VANETs, edge computing and fog environments that need a balance of performace and simplicity.

In summary, trust models in HetNets can be classified into decision, evaluation, and management models, each serving a unique role in the trust management ecosystem. Decision models focus on making binary trust decisions based on policies, evaluation models assess and quantify trustworthiness through metrics, and management models provide a comprehensive framework for maintaining and enhancing trust relationships within the network.
## Trust Modelling Tools

#### Use case Misuse case scenarios:

These are representation of threats: the multitudinous ways in which an attacker interacts with the system to thwart, break into, damage, abuse, or misuse the system. A misuse case is a use case from the point of view of an actor hostile to the system under design (Damodaran, 2006). These arise from the need to gather negative requirements so as to understand the  cases of unwanted  scenarios across a system. These allow for the modelling of  mechanisms and controls to prevent against system and data misuse in enterprises. They also help create antipatterns for misuse cases and as such harden the infrastructure (Dashti & Radomirović, 2018). This is because use cases may hide implicit trade-offs between security and other quality factors

Additionally, Misuse cases can be very helpful in modelling trust. This can be done by deriving risk levels for the infrastructure by representing threats and their associated specific use case, the countermeasure derived, and potential abusers defined as actors based on the roles played in the infrastructure. Eventually, the trust level is defined as a threaten relationship between Usecase and misuse case and  suggest a mitigates relationship between countermeasure and attack



[Figure/Image from source paragraph 505]



[Figure/Image from source paragraph 506]



[Figure/Image from source paragraph 508]



[Figure/Image from source paragraph 509]

This diagram visualizes how different types of attackers exploit various vulnerabilities within a heterogeneous enterprise network.

Explanation of the Misuse Case Diagram:

This diagram utilizes the Unified Modeling Language (UML) Use Case Diagram notation, adapted for Misuse Cases (or "Abuse Cases").

1. Actors:

Attacker (A): A generalization representing any entity with malicious intent.

Outsider (O): A specific type of attacker who operates from outside the enterprise network's security perimeter (e.g., internet-based attackers, competitors, state-sponsored actors).

Insider (I): A specific type of attacker who has legitimate access to the enterprise network or its resources, but misuses that access for malicious purposes (e.g., disgruntled employees, compromised users, contractors).

2. Misuse Cases (Threats/Attacks):

These are the negative actions an attacker can perform. They are grouped into a "Enterprise Network Security" package for clarity.

Outsider Attacks:

Gain Unauthorized Access (External): The primary goal of many external attackers, involving breaching the network perimeter.

Perform Reconnaissance (External): Gathering information about the network's structure, vulnerabilities, and targets from outside.

Exploit Network Vulnerabilities (External): Utilizing known weaknesses in perimeter devices, services, or configurations (e.g., unpatched software, misconfigured firewalls).

Launch DDoS Attack (External): Overwhelming network resources to deny service to legitimate users.

Phishing/Social Engineering (External): Tricking users into revealing credentials or installing malware, often a precursor to gaining access.

Data Exfiltration (External): Stealing sensitive data from outside the network once access is gained.

Insider Attacks:

Bypass Access Controls (Internal): Circumventing internal security mechanisms, often by exploiting misconfigurations or weak authentication.

Abuse Privileged Access (Internal): Misusing legitimately granted elevated permissions (e.g., system administrator accounts) for unauthorized actions.

Introduce Malware/Malicious Code (Internal): Planting viruses, ransomware, or backdoors from within the network, often via USB drives, personal devices, or compromised internal systems.

Data Tampering/Deletion (Internal): Modifying or destroying critical data within the network.

Intellectual Property Theft (Internal): Stealing proprietary information, designs, or trade secrets.

Disrupt Critical Services (Internal): Causing outages or degradation of essential business functions from within.

Collude with Outsider: An insider actively cooperates with an external attacker.

3. Relationships:

-- (Association): Connects an actor to the misuse cases they can initiate.

<<include>> (Inclusion): Indicates that one misuse case always includes the functionality of another. For example, "Gain Unauthorized Access (External)" often includes "Perform Reconnaissance (External)" or "Exploit Network Vulnerabilities (External)".

.> <<extends>> (Extension): Indicates that one misuse case may extend the behavior of another under certain conditions. For instance, "Collude with Outsider" extends "Gain Unauthorized Access (External)" by providing an easier entry point. It also shows how a successful internal breach ("Bypass Access Controls") might extend to "Data Exfiltration."

How this Diagram Helps with Heterogeneous Networks:

The diagram itself doesn't explicitly show "heterogeneity" in its boxes, but the implications for a heterogeneous network are profound:

Increased Attack Surface: Each different operating system, network device vendor, cloud service, and application stack introduces its own set of vulnerabilities. This diagram provides a high-level view that would then be broken down into specific technical misuse cases for each technology.

Complex Access Controls: Managing access across diverse systems (Windows AD, Linux LDAP, SaaS platforms, custom databases) creates opportunities for insiders to "Bypass Access Controls" or for outsiders to find weak links.

Varied Reconnaissance Needs: "Perform Reconnaissance" becomes more complex as attackers need to understand diverse protocols, naming conventions, and security mechanisms across different network segments (e.g., OT networks, cloud environments, traditional IT).

Challenging Monitoring: "Anomaly Detection" is harder when baseline behavior varies greatly across heterogeneous components, making it easier for "Introduce Malware" or "Data Tampering" to go unnoticed.

Diverse Vulnerability Exploitation: "Exploit Network Vulnerabilities" will involve a wider range of attack vectors, from Windows exploits to Linux privilege escalations, to cloud misconfigurations.

This misuse case diagram serves as a foundational step for a comprehensive threat model, guiding further analysis into specific attack paths and mitigation strategies tailored to the complex nature of heterogeneous enterprise networks. Here is the image:



[Figure/Image from source paragraph 548]



[Figure/Image from source paragraph 549]

#### Network Graph Embedding and Attack Graphs

Network embedding refers to mapping the nodes in the network to a low-dimensional vector space to represent a large-scale network structure. This low-dimensional vector representation can effectively express the relationship between network nodes and perform some commonly used network tasks, such as community detection, link prediction, and node classification (Li et al., 2020). These parameters are important in determining eventual network trust based in direct and indirect status update requests and answers. An attack graph is a type of scenario graph (set of all possible scenarios of usage of a system), that models each path in an attack scenario leads to an undesirable state, such as one representing an intruder gaining informational/network resources (Shandilya et al., 2014). Two types according to Chochliouros et al., (2009).

- A directed graph where nodes represent network states, and edges represent the application of an exploit that transforms one network state into another, more compromised network state

- A directed graph where each node represents a pre- and a post- condition of an exploit, and edges represent the consequence of having a true precondition that enables an exploit postcondition.

Attack graphs can be used for Representation of services within a network infrastructure, identification of vulnerabilities, vulnerability scores and their likelihood within networks as per emprical data (e.g., CVE scores) as well as definition of states, preconditions and post conditions for transition of states for each service. These can eventually be used to determine the attack detection scores  and consequently the exposure levels within enterprise networks. These would be vital probabilistic measures of risk and trust

#### Multi-parameter Weighting

A multi-parameter Dynamic Weight on Trust is an algorithmic process to determine score based on predefined scoring scale that is applied on user’s genealogical tree and community members. It may also include other parameters such as punishment mechanisms, risk mechanisms and recommendation trust mechanisms to include a dynamic trust model. Additionally, elements such as direct trust and trust risk function to create trust relationships in complex network environments and transactions (Jia et al., 2018). The use of entropy weight to represent ensemble of multiple parameters is also quite prevalent. These weightings can be passed through a machine learning model to generate the most optimal weighting of all the parameters of some of the parameters available for consideration as illustrated in Figure 2.6



[Figure/Image from source paragraph 558]

Figure 3.4: Multi-Parameter Trust Weighting (from:(Lukaseder et al., 2020))

## Approaches to Trust Management

#### Trust Factor Calculation Based on Forwarding rate and Consistency Factor

The validity of node trust management mechanism is based on the proper selection of trust metrics. The evaluation factors of the existing research include communication (such as forwarding rate factor), data transmission (such as consistency factor, freshness factor, integrity factor) and the node itself (such as residual energy, trust history, security level) etc. However, there is a clear contradiction between the number of trust factors and the network energy consumption. The more the trust factor, the more accurate the calculated trust value, and accordingly the greater the network energy consumption. Therefore, a reasonable choice of trust factor is very important. The main task of a node in a wireless sensor network is to sense the data information in the monitoring area and deliver it to the base station. Therefore, the correct and complete data forwarding is particularly important (Cheng et al., 2018).

#### Trust Factor Calculation Based on Direct and Indirect Values

Typically, trust factor is selected from the three aspects of communication, data transmission and node itself to calculate the direct trust value of the node. The indirect trust value of each node is calculated by the matrix of the direct trust value of the cluster heads. Then, the direct trust value is calculated as the weight of the comprehensive trust value. In the process of calculating the trust value of a node, a calculation method combining the direct trust value and the indirect trust value is adopted. Evaluation node i on the evaluation of the value of the trust node j evaluation mainly based on two parts, part of the direct trust value calculated from node monitoring data, the other part is the indirect trust value calculated by evaluating the direct trust value matrix maintained by the cluster head node that is shared by the evaluation node i and the evaluated node j. Finally, the weighted sum of these two parts is used to get the total trust value of the node (Das & Debnath, 2020).

#### Weight-based Probabilistic Trust Evaluation scheme

The WPTE involves two attributes for evaluating total trust: expected positive behaviours’ probability and indirect trust. The expected probability of positive behaviour predicts the behaviour of nodes based on their packet forwarding statistics. The indirect trust is provided by other nodes in the form of recommendations. The major components of WPTE scheme are node monitoring, trust estimation, trust database and trust update.

Node Monitoring: To evaluate trustworthiness of a sensor node, multiple aspects of its behaviour can be monitored. Each of the aspect (trust metric) intends to detect specific type of attack. A neighbour sensing mechanism is adopted to observe packet forwarding behaviour of neighbouring nodes. The nodes are placed in promiscuous mode to observe packet forwarding behaviour of neighbouring nodes. Trust Estimation: The trust estimation is responsible for evaluating trustworthiness value for the packet forwarding behaviour of each monitored sensor node and accordingly categorizes them in trusted and misbehaving nodes. A node is considered as trusted if it cooperates in packet forwarding. On other hand, a misbehaving node intentionally drops all the received packets and sends fake response message to requesting node indicating correct forwarding of packets (Ahmed & Bhangwar, 2017).

### Adaptive Deployment Model

An adaptive deployment model is essential to adequately address the contexts for resources access requests. Threshold assigned by credentialing policies limit access by means of context sensitive, dynamic extension. Besides, the process of determination of something (user, device, application, process, etc.) being trustworthy in this trust-centric shift is so difficult problem to begin countering with. Moreover, traditionally all the data and transactions are assumed to be trusted whereas device compromises, data breaches, and malicious activities contribute to degrade that trust. However, Zero-Trust strategy begins with an assumption that all the data and transactions are required to be deemed as untrusted from the inception. With this, a new problem gets countered as how to gain sufficient trust. Furthermore, based on the organizational requirements and key focuses, trust is bound to alter. Therefore, to manage the trustworthiness of all transactions in an organization, Zero-Trust architecture involves integration of control for data, users, devices, and applications (Mehraj & Banday, 2020)



[Figure/Image from source paragraph 571]

Figure 3.5: Adaptive Weighted Trust Model
# Dynamic Trust Models for Enterprise networks - Adapting to Change

"The Flow of Trust: Adapting to tides in the Sea of enterprise networks"

“Building the Blueprint”

## Introduction to Dynamic Trust in Heterogeneous Networks

Traditional network security paradigms are largely predicated on static, perimeter-based defenses such as firewalls services and cryptographic authentication such as PKI and passwords. However, the rise of complex, open, and heterogeneous networks—such as the Software defined Networks (SDNs), Internet of Things (IoT), vehicular ad-hoc networks (VANETs), mobile networks andcrowdsensing, and integrated cyber-physical systems—has rendered these models insufficient. These networks are characterized by:

Node Heterogeneity: Devices with vastly different computational capabilities, power constraints, and roles  including enterprise owned devices, BYOD, sensors and actuators, mobile smartphones and cloud nodes.

Network Heterogeneity: The integration and coexistence of multiple communication protocols including ethernet, Wi-Fi, Bluetooth, ZigBee, cellular networks  and LoRaWANs.

Dynamic Topology: This represents portable, nomadic and mobile nodes and links that frequently join, leave, or move, leading to transient and unpredictable interactions with the networks they are anchored on.

Decentralization: Multiple networks with separate centers of control result in decentralized authorities. The absence of an always-online central authority to mediate every transaction and the need for interowkring nodes or hooks and extensions to support internetwork data exchange.

In this context, trust emerges as a soft-security mechanism that complements hard-security cryptography. It is a multifaceted concept that serves as the cornerstone of security and decision-making in decentralized, open systems.. Trust is a multi-dimensional, relational, and dynamic concept that quantifies the reliability, credibility, and confidence one entity (the trustor) has in another (the trustee) based on past interactions and observed behavior.

In heterogeneous networks, diverse nodes with varying capabilities, roles, and security postures, static, binary trust models of traditional security are profoundly inadequate. These networks demand dynamic trust: a continuous, context-aware, and evidence-based quantification of trust that evolves over time.  Dynamic trust management is the continuous process of evaluating, updating, and managing this trust value in real-time to enable secure decision-making, such as access control, data fusion, and cooperative routing.

This chapter thus presents a formal framework for modeling and computing dynamic trust. It begins by establishing the fundamental mathematical underpinnings of trust as a probabilistic event, framing it through the lenses of Binomial and Bernoulli distributions. It then advance to a more nuanced and expressive model: Subjective Logic. Finally, it integrates temporal dynamics, introducing mechanisms for weighting evidence and modeling trust decay, culminating in a comprehensive model for trust in modern, heterogeneous environments.

## Foundations of Dynamic Trust for Heterogeneous Networks

### Heterogeneous Environment Challenges

Heterogeneity in modern enterprise networks introduces unique challenges in trust estimation and management that move beyond homogeneous systems: These include Context-Dependence where  trust is not absolute and nodes highly trusted  in one context such as data sensing may be distrusted for computational tasks due to its limited power capabilities.  (Josang, Ismail, & Boyd, 2007). Theis thus introduces the need for incorporation of contextual parameters  such as task criticality, computational power, node roles, and device capabilities. Further, Metric Normalization and Fusionis also a challenge due to the varied types of operations  within a heterogeneous network. Combining evidence from disparate sources and behaviors into a single, comparable metric is a fundamental challenge (Chen, Liu, & Chen, 2019). Also, Scalability and Overhead are vital challenges to trust computation algorithms that must be lightweight to accommodate resource-constrained devices such as mobile devices and IoT sensors. Centralized models create perfomance and scalability bottlenecks, while fully distributed models generate significant communication overhead for trust information exchange. The choice between centralized and distributed models further affect the Robustness  of the algorirhms and consequently  access decisions to Attacks. The  trust systems themselves become  attack vectors if poorly designed, deployed or configured depending on the environments of deployment. Good examples include malicious nodes colluding to provide false positive recommendations about each other, providing false negative recommendations about good nodes and nodes behaves well and badly intermittently to maintain a moderate trust value and avoid detection (Xiao et al., 2020). Ultimately, trust manageemnt and trasmission algorithms are suseptible to side channel attacks based on metadata and telemetry data as a result of Sharing detailed interaction histories for trust computation. Thus results in revealing of sensitive information about a node's activities and relationships.

### Dynamic Trust  in Heterogeneous Networks

Dynamic trust management is not a supplementary concept but a critical enabler for security and cooperation in modern heterogeneous networks. It represents a shift from static, binary authentication to a continuous, nuanced, and evidence-based assessment of user behavior. This enables evolution from simple probability models to sophisticated  models  for modern AI-driven and distributed systems. This is because the inherent challenges of heterogeneity such as context-dependence, metric fusion, and scalability, ensure there is need for constant improvments in the discipline. Hence the  need to develop adaptive, explainable, and energy-aware hybrid models that can operate at scale while providing robust defenses against increasingly sophisticated collusion and evasion attacks.  A comprehensive dynamic trust model typically incorporates several key components, as visualized in FIGURE



[Figure/Image from source paragraph 743]

Figure .: Dynamic Trust Model Components

Direct Trust  Value (DTV): This represents the results of observable  parameters and telemetry data that are aggregated and used to calculate trust based on the trustor's first-hand observations of the trustee's behavior such as successful packet deliveries and data validity. This is often the most reliable evidence. Models use probability theory (Beta distribution), belief theory (Dempster-Shafer), or fuzzy logic to compute DT (Josang et al., 2007).

Indirect Trust: This represents the reputation of trustees as transmitted by the trustor to other trustor nodes within the network of interacting nodes. It is sought from other nodes referred to as recommenders when direct evidence is insufficient. The challenge lies in aggregating these recommendations while weighting them based on the trustworthiness of the recommenders (Chen et al., 2019). This usually creates a recursive challenge in evaluating the trust of the recommnders in the need to trust so as to evaluate trust.

Trust Aggregation: This represents a mathematical fucntion that that combines all evidence into a final trust score as represented in equationX. This can be collated and aggregated based on some or combinations of existing dterministic or probabilitic approaches depending on the context of the computing environment. Common methods include dynamic weighted averages, Bayesian inference, and subjective logic.

Trust Dynamics and Decay: While trust can be dynamic and cotextual, trust must also be vealuated in  the temporal domain. A node's good behavior from the past should carry less weight than its current behavior. This is typically implemented using a time windows also referred to as data freshness or a decay factor that represents data aging as a function. The eventual trust score is factoe od the previous score and the  the new outcome based on a new observation as shown in EQUATION X. While this addresses the dynamicity of trust based on new observations, new evidence must be weighted highly compared to older evidence as illustrated by an exponential decay function as illustrated in EQUATION X

Where  represents the change in trust due to the new observation .

where λ is the decay factor is between 0 and 1 , and  is the trust update based on the current observation. This way, more recent interactions have more influence on the trust belief  in an Exponential Moving Average (EMA) (Xiao et al., 2020). This elegantly handles on-off attacks by gradually forgetting past good behavior if current behavior is bad. A low  causes rapid decay and places high emphasis on recent events, while a high  results in slower decay and a longer memory.

### Techniques* of  Trust Modeling

Dynamic trust models has evolved  over time as Mathematical and Probability-Based Models, Machine Learning (ML) models and Hybrid and Emerging Paradigms. Mathematical and Probability-Based Models such as Bayesian Models, Represent trust as a probability distribution, often a Beta distribution, updated using Bayesian inference. These are simple and intuitive but can struggle with representing uncertainty and context Josang et al., 2007. Belief Theory models such as Dempster-Shafer, extend probability theory to handle uncertainty and ignorance more explicitly. It can model "belief," "disbelief," and "uncertainty" as separate measures, making it robust in environments with incomplete information Chen et al., 2011.

Newer moels enhance their logic based on Machine Learning Models that can automatically learn complex, non-linear patterns from behavioral data, making them highly adaptive. Good examples include Deep Learning algorithms that model long-term temporal dependencies in node behavior, making them exceptionally good at detecting subtle and evolving attack patterns that simple decay models might miss Xiao et al., 2020. While Reinforcement Learning (RL) algorithms Frame trust management as a learning problem where the trustor (agent) learns an optimal policy for interaction based on rewards (successful interactions) and punishments (failures). RL is inherently dynamic and well-suited for exploring uncertain environments Yao et al., 2021.

Hybrid Paradigms such as Blockchain-based Trust approaches offer a decentralized, tamper-proof ledger for storing trust-related transactions and recommendations, mitigating collusion attacks  by making recommendations public and auditable. Smart contracts can automate trust aggregation and decision-making Alshehri et al., 2022. Other hybrid models such as ML-Probabilistic Models  combine the explainability of probabilistic models with the predictive power of ML. For instance, using a Bayesian framework as a base but tuning its parameters or fusing its output with an LSTM's prediction.

While dynamic trust models are powerful and cotextual in heterogeneous envrioments,, several problems arise. Firstly, a Cold-Start Problem emerges: The inittial truts value for new nodes is difficult to define due to lack of previous transactions. Due to the need to continuously verify based on ZT principles,How to assign an initial trust value remains a significant challenge. Overly optimistic initialization makes the system vulnerable while overly pessimistic initialization hinders collaboration.  Secondly, Standardization and Interoperability become a challenges due to the lack of a universal standard for trust metrics prevents different heterogeneous networks from sharing trust information, limiting their utilityand representation of ontologies for trust. Thridly, Explainability for Trust becomes a challenge as  areuslt of incresing complexity of models. As ML models become more complex black boxes, it becomes difficult to explain the reeason and process for a node's  estimated trust score. For critical systems, understanding the rationale behind a trust score is essential for administrators to take corrective action or intitiate subsequent learning iterations epochs. Finally, Integration with Zero-Trust Architectures (ZTA) becomes challenging with volatilie contexts: The core principle of ZTA, never trust, always verify, aligns perfectly with dynamic trust bbut introduces complexity in iteraction between components and subnets due to the difficulty in completely eliminating implicit trust. While  continuous, quantitative trust scores can replace the binary authentication used in many ZTA implementations, implicit trust largely remain a core part of heterogennous networks.

## Dynamic Trust as Deterministic and Probabilistic Approaches

### Deterministic Trust Models

Deterministic trust models assign a static, binary, or categorical value to trust. A node is either "trusted" (1) or "untrusted" (0), or perhaps classified into a fixed set of levels such as Low, Medium and High. This approach is simple and computationally inexpensive, making it prevalent in early access control systems like Access Control Lists (ACLs). It is however structurally rigid and cannot represent uncertainty, incorporate new evidence fluidly, or model the gradual erosion or improvement of trust. It is inherently unsuitable for heterogeneous environemts due to trust uncertainty and highly volatile contexts in heterogeneous network enterprise envrionment.

Deterministic models apply fixed rules or algorithms, assigning trust values based on defined thresholds, heuristics, or explicit past behavior. Some key characteristics include Fixed Decision Boundaries, rule-based systems and simplistic static contexts that are easy to interpret. In such scenarios, trust is a binary or discrete value determined by strict conditionsand in some cases if-else conditions, scoring mechanisms, or hard-coded logic is applied for trust calculation. Deterministic models are interpretable and easy to implement but may overfit to static environments. Some approaches to Deterministic Trust Calculation include

Threshold Models: Trust is assigned if a node meets predefined criteria (e.g., successful interactions >threhold%).

Weighted Scoring: Nodes accumulate trust points based on actions, and trust is assigned when a threshold is crossed.

Direct Observation: Trust is computed directly from observed behavior without probabilistic inference.

Deterministic algorithms and models  are highly effective in environments that require instant trust decisions for new entities based on credentials such as digital certificates, hardware-based attestation,  and transparency based on clear, auditable rules such as  a Node being trusted based on a valid certificate from an Authority. Furthermore, they are more immune to attacks that manipulate interaction history. Their lack of adaptability, context awareness and reliance on a preexisting PKI or central policy verifying authority leave them severly lacking in heterogeneous envrionemnts (Nyangaresi et al., 2022).

### Probabilistic Trust Models

Probabilistic models address the limitations of determinism by treating trust as a continuous value, typically a probability, representing the expectation that a node will perform a specific action reliably. This probability is derived from historical evidence of interactions such that Tₓ as the trust value of a node X, ranging from 0.0 representing complete distrust to 1.0 representing complete trust. The core idea is that :Tₓ ≈ E[X] = P(X behaves reliably).

Probabilistic models incorporate dynamicity in trust calculations by factoring in uncertainty likelihoods based on changing conditions in networks. This allows for consideration of parameters that have probabilities of existenc and change, making them suitable for highly variable heterogeneous environments. Some of the key characteristics include evaluation of trust as a Random Variable, continuous evalutation and tolerance to errors and change. Trust values are represented as probabilities based on previous transanctions, and interactions, behaviors, and indirect recommendations in cases where there is trust transmission. Trust is also recalculated dynamically as new evidence  and interactions arrive  thus relying on feedback loops for improvements in subsequent interactions. feedback) arrives. These feedback loop and subsequent improvements  make probabilistic models better at handling noise, partial data, and inconsistencies in the network or network metadata.

Some approaches for dynamicity in to probabilistic trusts calculation include Bayesian Networks which achieve dynamicity through iterative updates of trust scores using Bayes' theorem based on prior knowledge and new observations as illustrated in on equation 4.1. Other  approaches include  Markov  and Hidden Markov Chains and models where trust values are incremented or decremennted based on transitions between states over time, with probabilities dictating the likelihood of moving from one trust level to another. Latent trust levels that are not directly observable but inferred through interaction patterns. Finally, Gaussian and Continuous Distributions where Continuous trust values (x∈(0,1)) can be modeled using distributions like the Continuous Bernoulli for probabilistic fusion of trust from various sources. The results include integral values that can be collapsed into blacklists  and/or whitelists based  on the access threhold values.

### Hybrid Models (Probabilistic + Deterministic)

The escalating complexity and adversarial sophistication inherent in heterogeneous networks have exposed the limitations of monolithic trust management architectures. Pure probabilistic models such as  Bayesian and EigenTrust excel at leveraging historical interaction data to infer future behavior but often lack context-awareness and can be slow to react to novel attacks. Conversely, pure deterministic models such as  rule-based systems and policy-driven access control provide immediate, verifiable decisions based on predefined criteria (e.g., certificates, device types) but are inherently rigid and cannot adapt to evolving node behavior or subtle malfunctions.

The integration of these paradigms into  Hybrid Trust Models represents a significant evolutionary step. This fusion creates systems where the adaptive, learning capabilities of probabilistic methods are guided and enhanced by the structured, verifiable logic of deterministic frameworks. The core thesis is that such a hybrid approach mitigates the weaknesses of each constituent model, yielding a trust management system that is simultaneously adaptive, robust, explainable, and context-aware.

Combining probabilistic and deterministic approaches leverages the strengths of both methods;  For instance a node with 95% data accuracy is assigned deterministic trust. Over time, Bayesian updating refines the trust score based on ongoing performance. The Initial Trust Assignment cab be based on deterministic rules for initial trust assessment suxh as pass/fail based on basic performance while the Dynamic Trust Updates can be based on probabilistic methods to update trust levels continuously as new interaction data becomes available. In heterogeneous networks, the choice between probabilistic and deterministic trust calculations depends on the network's variability, scalability needs, and tolerance for uncertainty.

An effective hybrid model is not a simple average of two scores. It is a structured integration where each paradigm operates on, and informs, the other. Two variations of hybrid architecture may be utilized for trust estimation and calculation in heterogeneous enterptise environments

Deterministic core with Probabilistic updates: This is a common and logical structure designed  as a bootstrapping architecture to solve the cold-start problem where the initial trust value is difficult to determine for a new device.  Its initial phase is deterministic such that a  new joins the network and the initial trust is not set to a default middle value but is derived deterministically from its credentials such as a manufacturer-issued certificate, a hardware-rooted identity or a device type/role). This provides a secure and justified starting point for trust calculation. The second phase is based on  Probabilistic Refinement; once the node begins interacting, a probabilistic engine such as a Bayesian updater or tempral trust decaytakes over and continuously monitors the node's acttivities such as packet forwarding, and  data validity, and dynamically adjusts the initial trust score upwards or downwards. (Nyangaresi et al., 2022).

Probabilistic Core with Deterministic Guardrails (Constraint-Based Architecture):This model’s primary trust value is generated probabilistically, but deterministic rules act as overriding constraints or context modifiers. This is based in a costraint based architetcure such that the deterministic models provide threshold based guardrails. For example, a Bayesian network or a fuzzy logic system computes a continuous trust value based on interaction history for a device or user and a policy engine applies deterministic rules that can cap, floor, or invalidate the probabilistic score based on context  and dynamicity supported within a heterogeneous network. Critical and non-negotiable vlue such as certificate validity, lack of MFA or untrusted devices automatically invalidates the trust level regardless of the threhold (Alshehri & Hussain, 2021).

Hierarchical Fusion Architecture: this architecture focuses on trust as modular concept that can be evaluated in different paradigms. Trust is broken down into multiple dimensions, each calculated using the most appropriate method, and then fused into a final composite score. For example, Identity Trust for user credentials  can be  calculated deterministically while their behavioral trust (trust of appliations, devices or networks) is calculated probabilistically based on transaction history. Ultimately, the contextual trust could involve both deterministic rules probabilistically  such as device type influencing a probabilistic device complience score within the network (Wang et al., 2023).. As such as weighted fusion function, would potentially learned adaptively by dynamically combining these dimension scores as shown in EQUATION X:

- T_final = w1 * T_identity + w2 * T_behavior + w3 * T_context.

Hybrid approaches are  more complex and challenging to implement due to factors such as  finding an optimal Fusion Strategy. Determining the weights for combining scores is highly dependent on diffenet organizational  network structures. Machine learning models can be used to dynamically optimize these fusion parameters based on network outcomes (Liang et al., 2022). Increased Complexity and explainability are also active hinderances to hybrid models. Ensuring efficiency and low overhead on resource-constrained devices is a challenge. While the deterministic parts are explainable, the fused result is a gray box making the entire decision-making process less transparent, especially for audit of trust decisions. Finally,a lack of standardized metrics and interfaces for exchanging trust information between different hybrid systems hinders interoperability across heterogeneous network domains.

Therefore, Hybrid probabilistic-deterministic trust models represent a sophisticated and necessary advancement for securing complex, modern networks. By synergistically combining the adaptive intelligence of probability with the rigid security of determinism, these models overcome the fundamental limitations of their pure-form counterparts. They provide a robust solution to critical problems like cold-start, enhance resilience against collusion attacks, and integrate crucial context into the trust calculus. This work thus looks at a fused hubrid and subjective logic approach to contextually and dynamiacally weight trust nbase don device, network, user and application trust tenets of ZTA as the cornerstone of next-generation dynamic trust calculation in heterogeneous systems.

## Dynamic Trust as Binomial and Bernoulli Events

At its core, the concept of trust in a networked interaction is fundamentally a prediction of future behavior based on past evidence. This aligns perfectly with the principles of probability theory. Modeling direct, binary interactions (success/failure, honest/dishonest) as a sequence of Bernoulli trials and aggregating their outcomes into a Binomial distribution provides a mathematically rigorous, lightweight, and intuitively explainable foundation for dynamic trust computation. This approach is particularly powerful in large-scale, resource-constrained environments like the Internet of Things (IoT) and sensor networks, where simplicity, low computational overhead, and scalability are paramount.

### The Bernoulli Trial: The Atomic Unit of Interaction

The most straightforward way to estimate the trust of an entity, Tₓ, is to model each interaction as a Bernoulli trial, an experiment with exactly two outcomes: success representing the node behaving correctly or failure which shows the node as malicious. A single transaction between a trustor (observer) and a trustee (observed entity) can be modeled as a Bernoulli trial which is a random experiment with exactly two mutually exclusive outcomes: success and failure. For a given transaction i: Success (Xi = 1), the trustee behaves correctly  or in line with the defined policy such as providing valid data, forwards a packet successfully or fulfills a request); or Success (Xi = 0): the trustee behaves maliciously or fails to operate within the defined policy such as  providing false data, drops a packet or refuses service. The outcome is governed by the trustee's inherent, but unknown, probability of success, θ. This value θ ∈ [0, 1] is the very quantity to be estimated as the true, latent trustworthiness of the node.

### The Binomial Distribution: The Aggregated History

A sequence of n independent transactions with a trustee forms a set of n Bernoulli trials. The Binomial distribution Bin(n, θ) models the probability of observing k successes in n independent Bernoulli trials, each with the same probability of success θ. For Sn a random variable representing the total number of successful interactions out of n trials: Sn = X1 + X2 + ... + Xn, with a probability Mass Function (PMF) illustrated in EQUATION X:

A sequence of n such independent interactions forms a trust value  that can then be estimated as the relative frequency of successes, which is the maximum likelihood estimator for the probability of success p in a Binomial distribution. The value k/n as the observed success ratio serves as a natural, albeit naive, point estimate for θ. If r is the number of successful (positive) interactions, s the number of unsuccessful (negative) interactions and n (r + s ) is the total number of interactions (trials), the naive trust probability is given by:

​

Modeling dynamic trust as a series of Bernoulli trials culminating in a Binomial likelihood, updated via Bayesian inference with a Beta prior, remains a cornerstone of probabilistic trust management. Its mathematical purity, computational efficiency, and innate ability to quantify uncertainty make it exceptionally valuable for the IoT era. While the base model has limitations regarding temporal dynamics and context-awareness, it provides a robust and flexible foundation. Contemporary research does not discard this model but rather enhances it through decay mechanisms, weighted evidence, and integration into larger hybrid or AI-driven frameworks. It continues to be a critical component in the toolkit for designing scalable and mathematically sound trust systems for heterogeneous networks.

Trust evaluation treats each access decision as the outcome of a structured probabilistic inference process operating across four independent telemetry domains.Within each domain, multiple individual security attributes are continuously assessed. This thus formalizes how atomic, binary outcomes of individual facet checks compose mathematically into the continuous domain trust scores determine the eventual trust score. The hierarchical probabilistic architecture grounds that each individual facet check constitutes a Bernoulli trial, a single binary observation of compliance or non-compliance. Within a domain, the aggregation of n​ independent Bernoulli facets produces a Binomial distribution governing the number of successful trust checks. At the composite level, the domain scores themselve, each derived from an independent binomial process, are further combined in a nested binomial structure that propagates uncertainty upward through the architectural hierarchy. This nested composition ensures that the eventual trust value ​ inherits the full probabilistic machinery of the Bernoulli-Binomial family, including analytically tractable variance, well-characterized confidence intervals, and natural compatibility with the Dempster-Shafer mass function construction(Jøsang, 2016) described in section 4.5

Each of these facets produces a single Bernoulli observation at every evaluation epoch t. The probability parameters pk,j​ are not static constants but are themselves functions of the entity's current contextual state such as a device that has been consistently patched for 30 consecutive evaluation cycles. With four independent domains, each producing a binomial proportion Sk​, the composite trust evaluation faces a second-tier aggregation problem on how to combine four domain-level proportions into a single composite trust value. This creates a nested binomial structure, a hierarchical model in which the first level of aggregation (facets to domain scores) is itself embedded within a second level of aggregation (domain scores to composite trust).

This hierarchical structure connects seamlessly to a Dempster-Shafer fusion pipeline where binomial variance of domain scores governs the dynamic weights, which in turn determine the allocation of evidential mass between committed belief (m ({Safe}), m({Unsafe}) and uncertainty (m(Θ) discussed in section 4.5. The result is a trust computation architecture in which every layer, from the individual Bernoulli facet check through the nested binomial composite to the final Pignistic access decisionis governed by a coherent, analytically tractable probabilistic framework.

## Dynamic Trust for Heterogeneous Enterprise Networks Based on Subjective Logic

In dynamic and context-aware trust modeling, the Subjective logic and bayesian inference models enable the aggregation of data fom multiple sources to determine the eventual trust score. In subjective logic, consideration  between cumulative, weighted, and average belief fusion depends on the specific requirements of the environments, including heterogeneity, trust update over time, the role of context, and how much weight is given to various sources of information (Abellán et al., 2021). Each of the fusion models has scenarios of application

Subjective Logic (SL), introduced by Audun Jøsang, provides an algebraic framework that explicitly models uncertainty and belief. It extends probabilistic models by representing a trust opinion as a triplet, making it ideal for the sparse and ambiguous evidence often found in dynamic networks. It also adds uncertainty and subjectivity. In probabilistic logic, a uniform distribution does not express “no know” because a uniform distribution says that we know that the distribution over the domain is uniform. Subjective logic can distinguish between the situation where the distribution over outcomes is unknown and the situation where the distribution is known and, for example, uniform. In subjective logic, it is also possible to have a situation where some information about the distribution is known and there is some uncertainty. The subjectivity comes from the fact that we can assign an opinion, or information, about a proposition to an agent.

### Opinion Triplets

An opinion about a node X is represented as a triplet ωₓ = (b, d, u), where: b (belief) represents the belief that X is trustworthy while d (disbelief) represnts the belief that X is untrustworthy. Ultimately, u (uncertainty) represents the amount of uncommitted belief due to lack of evidence. These components satisfy the constraint: b + d + u = 1. The opinion triplet can be directly derived from observed evidence such that:

Where b is the belief value represented as a ratio of  positive attempts(s), d the disbelief value represented as aratio of unsucceesful calues (s)and u the uncertainty value which is derived as a ratio of C which is the denominator or base rate  and represents  the weight of prior uncertainty and b + d + u = 1. A large C indicates a more conservative model that requires more evidence to reduce uncertainty.

### Cumulative Belief Fusion

This is a trust modeling technique where all pieces of trust evidence (from past interactions) are aggregated over time to form a single, overall trust belief in an entity’s trustworthiness. This method assumes that the more evidence (both positive and negative) you accumulate, the more confident you can be in your trust estimation. It  works by continuously updating the trust score or belief in an entity based on all available historical evidence without discarding any previous interactions and assumes that all past interactions, regardless of when they occurred, have some value in determining the current level of trust.. Unlike other methods (e.g., weighted or average belief fusion), cumulative belief fusion treats all trust-related interactions as valuable and does not decrease the importance of older evidence.This not only ensures consistency in assessment and reassessment of trust  but also works well with environments that have very long-term interactions beween users and device, applications,  and networks. This may however introduce more skewness on the trust score due to the cumulative approach giving too much weight to old interactions that are no longer relevant in a dynamic system. It is also very rigid when dealing with rapidly changing environments where more recent actions are more indicastive of future or expected behavior. This thus makes this fusion model appropriate when a trust relationship evolves slowly and gradually, and historical data are as important as current information.

#### Belief Representation

Belief in the context of trust modeling is often expressed in terms of probabilities or other metrics that quantify trustworthiness. In cumulative belief fusion, each interaction or event contributes a piece of evidence that can either increase or decrease the overall belief. Common Representations are:

Probabilistic belief: The trust level is represented as a probability (e.g., between 0 and 1), where 1 represents full trust and 0 represents no trust.

Subjective logic: Trust is represented using belief, disbelief, and uncertainty, each of which is updated over time.

Beta distribution: In Bayesian trust models, belief is often represented using a Beta distribution, which is parameterized by counts of positive and negative interactions.

#### Updating Belief

Cumulative belief fusion works by updating the current belief whenever new evidence becomes available. The key idea is to treat each new piece of evidence (e.g., an interaction, observation, or feedback) as an incremental update to the current belief. Common update mechanisms include

Additive updates: If trust is represented probabilistically, each new observation either increases or decreases the current trust belief. For example If a positive interaction occurs (e.g., a successful transaction), the trust score might increase.  If a negative interaction occurs (e.g., failure to deliver a service), the trust score decreases. For a system that starts with an initial trust belief T0​. Each new observation On,either increases or decreases this belief cumulatively:

Where  represents the change in trust due to the new observation

#### Incorporating All Past Interactions

Cumulative belief fusion, as its name suggests, includes all past interactions without discounting or forgetting older evidence. The primary assumption is that all past evidence is valuable, even if the interactions happened a long time ago. This approach ensures that long-term trustworthy behavior is rewarded and sustained distrust is reflected. This can be advantageous in situations where long-term consistency is important, but it can also be a drawback when older information becomes irrelevant in dynamic systems.

#### Trust Decay and Aging

In some cumulative belief fusion systems, decay factors or aging functions can be introduced. While this is not pure cumulative fusion, these mechanisms allow for older evidence to be weighted less as time goes on, addressing one of the main criticisms of the cumulative method: the equal treatment of all historical evidence. For example, exponential decay can be used to discount older evidence:

Where  (decay factor) is between 0 and 1 , and  is the trust update based on the current observation. This way, more recent interactions have more influence on the trust belief.

#### Context Independence (in Pure Cumulative Fusion)

In pure cumulative belief fusion, context is typically not considered, and all interactions are treated equally, regardless of the situation in which they occurred. The model assumes that trust is a stable property of an entity and does not vary based on specific situations or contexts.

However, if context-awareness is important, cumulative belief fusion can be extended to include contextual information by keeping separate trust scores for different contexts, or by using context-specific cumulative fusion. For instance, trust beliefs might be aggregated separately for different tasks or environments.

#### Convergence of Trust Belief

One of the notable properties of cumulative belief fusion is that, over time, the trust belief tends to converge as more evidence is collected. If there is consistent positive evidence, the trust score will steadily increase toward a maximum. If there is mixed evidence, the score will fluctuate but eventually stabilize. This makes cumulative fusion good for environments where trust relationships are expected to evolve gradually and consistently.

Despite its intuitive appeal, cumulative fusion suffers from three significant limitations in trust contexts. First, the assumption of source independence is frequently violated in trust networks where agents share information and influence opinions . When dependent sources are treated as independent, the cumulative fusion overcounts evidence, producing artificially high confidence. Additionally, cumulative fusion lacks a mechanism for source credibility weighting. All evidence sources are treated equally, regardless of their historical accuracy or relevance to the current context . Finally, when faced with conflicting evidence, cumulative fusion's normalization can produce trust estimates that defy intuition such that two highly confident sources of information are fused resulting in uncertainty in scenarios where signal indicate high trust or high distrust.

### Average Belief Fusion

Average belief fusion computes the average of all trust evaluations, treating all interactions equally. This assumes that no interaction is inherently more important than another. This ensures are very simplistic yet balanced approach to trust evalution avoiding giving too much importance to outliers or contextual factors. While this generally provides an easy to understand and straightforward view of trust scores, it ignores temporal releance that is common in dyanmic environments. It also lacks context sensitivity and thus does not adapt tp accunt for different important interactions. It is thus suitable for relatively stable environments that raely change, and all pieces of trust information are equally reliable and relevant.

Recognizing the limitations of cumulative fusion under conflict, averaging approaches that treat evidence combination as a consensus-building process rather than evidence accumulation. best solves the normalization problems. In trust systems, averaging fusion corresponds to aggregating reputation scores from multiple peers or combining multiple trust dimensions as shown in Equation 4.5. Averaging fusion offers significant advantages over cumulative fusion for trust computation by having conflict robustness where normalization is avoided and stable results are derived even under high conflict.

Additoinally, Source weighting naturally accommodates varying source credibility, a critical requirement in trust computation where sources possess different historical accuracy.Averaging also suffers from a lack of convergence property essential for learning from repeated evidence. In trust terms, observing the same trustworthy behavior 100 times should increase confidence, but averaging yields the same result as observing it once. It also

violates the principle of evidence independence. By treating all evidence as equally weighted regardless of quantity, it fails to capture the information-theoretic principle that more evidence should reduce uncertainty. Finally, its interpretation of averaged beliefs remains unclear. Unlike cumulative fusion, which derives from probability theory via Dempster's rule, averaging lacks a rigorous foundational justification within evidence theory .

### Weighted Belief Fusion

Weighted belief fusion assigns different weights to different pieces of trust evidence based on their importance, recency, or reliability. More recent or contextually relevant interactions might be weighted more heavily. This makes the fusion model more adaptable and customizable to contexts. It therefore can prioritize more recent interactions or those more relevant to the current context, making it ideal for dynamic environments. The weghtings can also be adjusted based on the context, ensuring that trust is modeled in line with situational importance and flexibility. Expert opinions and dynamic policies can also be incorporated to consider reliability of sources, or varying contextual factors into the model by changing the weights. Determining appropriate weights requires careful tuning, especially in environments with diverse and evolving contexts which if not calibrated well, the system may overreact to anomalies or temporary changes in behavior resulting in misrespresnted trusts score and wrong access decisions. This fusion model thus becomes very appropriate for environments that are dynamic, and recent interactions or specific context-based information are more valuable in determining trustworthiness.

#### Weighted Fusion

Belief Inputs: Each entity (Data, device, network, and application) provides a trust score or belief value, which is typically between 0 and 1.

Weights: Each entity has a weight assigned based on its importance or reliability. These weights can change over time or based on context.

Fusion Process: The weighted trust scores from all identities are fused into a single cumulative trust score using a weighted average formula:

Where Trusti is the trust score of signal i

Weight I is the weight of dientity attribute i

The numerator is the sum of eighted scores

The denominator normalizes by the sum of the weights to have valid range of scores

For adaptive deployments, Wang et al. (2022) proposed an adaptive Dempster-Shafer trust model for multi-agent systems that dynamically adjusts fusion parameters based on observed source behavior. This observes variance from signal values across a collection window and determines the weight of a domain. If the variance is too high, it indicates unreliable signal values and therefore the weight is reduced towards zero while low variance results in higher weights.

#### Trust Computation Requirements

Trust computation imposes specific requirements on belief fusion frameworks:

Requirement 1: Source credibility differentiation. Trust sources vary in reliability based on historical accuracy, relationship closeness, and contextual relevance. Weighted fusion approaches uniquely satisfy this requirement through dynamic weight adjustment .

Requirement 2: Evidence decay. Older evidence should contribute less to current trust estimates. The unified trust distribution mechanism can incorporate temporal discounting through weight modification .

Requirement 3: Conflict detection and resolution. Trust systems must identify when sources provide contradictory information and respond appropriately. The reward-punishment mechanism explicitly addresses this by reducing weights for sources that consistently conflict with consensus .

Requirement 4: Uncertainty representation. Unlike binary trust models, DST-based approaches maintain separate representations for positive evidence, negative evidence, and uncertainty—capturing the distinction between "distrust" and "ignorance" .

Requirement 5: Transitivity. Trust often propagates through networks; source A trusts source B, who trusts target C. Weighted fusion frameworks can incorporate discounting factors that reduce trust proportionally to the length of the trust chain

3.6 Modeling Trust Decay Over Time

3.6.1 Exponential Evidence Discounting

3.6.2 Practical Implementation: Sliding Windows and Forgetting Factors


*📌 Takeaway: Trust can be mathematically modelled using Bernoulli trials, Subjective Logic, and temporal decay functions. However, existing trust models are fragmented, static, or context-limited. The next chapter evaluates whether Zero Trust Architecture addresses these limitations.*



---

# PART II: WHY EXISTING MODELS FAIL

# Chapter 4: Zero Trust Architecture — Strengths and Blind Spots

*Chapter 3 established trust as a computational problem with mathematical foundations in subjective logic and temporal decay. However, the question remains: do existing security architectures implement these computational trust principles? This chapter examines Zero Trust Architecture—the dominant paradigm for modern network security—to evaluate whether it provides the mathematical trust engine that heterogeneous networks require.*

## The Zero trust Model

In recent years, network-based cybersecurity attacks have increased in both frequency and severity, far outstripping traditional defense methods (Sheikh et al., 2021). Zero trust is an architecture that focuses on data protection and not the traditional boundary and perimeter protection. The primary goal is a fine-grained access control scheme based on identity in order to deal with the risk of unauthorized lateral movement of data between the subject and objects.

The Zero Trust Model does not assume trust for any entity (including users, devices, applications, and packets), regardless of whether such entities are inside or outside a secure network. This approach is based on three key principles. First, it eliminates trusted zones within the architecture; all resources must be accessed securely, regardless of location. Second, access control policies are strictly enforced, sometimes at multiple locations in the design including gateways and firewalls (a strict least privilege approach). Third, all network traffic should be logged, inspected, and analysed regardless of its origin. These fundamentals are closely aligned with the more recent NIST concept of Continuous Diagnostics and Mitigation (Eidle et al., 2018).

Zero trust is intended to provide a dynamically scalable security infrastructure that can be applied across many different types of organizations. A fundamental principle of zero trust involves authorizing secure communication between the resources, regardless of their environment and location, and assuming all network communication is a threat until it is attested, authorized, and secured. This is not merely an extension of security principles such as deny by default, least privileges, or role-based access control. Rather, it redefines the approach to ring-fence the application resources to whitelist traffic between them, a fundamental principle in which resources to be protected are grouped together and securely isolated or partitioned to limit unauthorized access (Sheikh et al., 2021).

### Zero Trust NIST Specification-NIST SP 800-207

NIST Special Publication 800-207 remains the definitive federal framework establishing Zero Trust Architecture (ZTA). Rather than dictating specific vendor products, the publication formalizes the shift from static, perimeter-based defenses toward resource-centric protection governed by the principle of "never trust, always verify" (Rose et al., 2024). A core operative concept detailed within the publication is the Trust Algorithm, the computational logic functioning within the Policy Engine, responsible for analyzing real-time observability data to grant or deny access dynamically.

While NIST avoids prescribing rigid, hardcoded tiers, scholarly analyses spanning 2024 to 2025 categorize the algorithm's inputs into several dominant pillars: Identity Assurance (evaluating MFA strength and role-based privilege), Device Posture (assessing enterprise management status, OS compliance, and patch levels), Behavioral Analytics (identifying impossible travel or anomalous access requests), and Resource Sensitivity (factoring in data classification and regulatory encumbrances) (Xu, 2024; Shin et al., 2025).

A recognized critique of the original guidance is its intense reliance on organizations to independently mature these continuous evaluation loops. However, recent scholarly advancements focus heavily on "Trust Algorithm Optimization," exploring complex methodologies such as utilizing Federated Learning and advanced Software-Defined Networking to drastically improve the mathematical accuracy, latency, and resilience of Zero Trust policy engines (Xu, 2024). NIST SP 800-207 ultimately emphasizes that Zero Trust is not a static state but a continuous iterative capability, requiring persistent ingestion of telemetry to fine-tune the strictness, or tiering, of access controls.



[Figure/Image from source paragraph 475]

Figure 3.3: The theoretical inputs and dynamic outcomes of the NIST SP 800-207 Trust Algorithm

### Zero Trust Facets

Zero trust approach is to treat the internal network as untrusted to the same degree as the Internet. The internal network is divided into a number of network segments or zones each of which contains different functions and information. Each zone’s data will require a different trust level from the subject; this indicates the importance of the assets housed within the zone. In order to access an asset, a subject’s trust level assignment must be equal to or greater than the zone’s minimum trust level which is determined based on five pillars/facets that ought o be verified to determine this trust level (Vanickis et al., 2018). These five facets include:

Device Trust: All authorized devices need to be known and verified before they are trusted. An inventory specifying which devices are owned and thereby controlled by your company ought to be provided, managed and controlled before access is granted. By interrogating the device posture, it can be determined whether a device can be trusted and if the device is compliant, based on pre-determined security policies. A unified endpoint management (UEM) solution can be used to manage, monitor and control all devices – mobile, desktop, rugged and IoT – across all platforms from a single console; and integrating endpoint detection and response (EDR) technology can further improve device security posture by further enabling the detection of possible malicious endpoint activities.

User Trust: Time after time, password-based user authentication has been proven inefficient and ineffective. Therefore, as a part of zero trust, organizations must make use of more secure user authentication methods. A strong conditional access engine, for instance, can make decisions using dynamic and contextual data. Technology building blocks to enable a strong conditional-access engine include password-less authentication (e.g., biometrics, certificates), multi-factor authentication (MFA), conditional-access policies and dynamic risk scoring.

Network Session/Transport Trust: Another key component of zero trust is the concept of least-privilege access. The idea is that a user or system should have access to only those resources that are specifically required to perform the task at hand. By using the principle of least-privilege access to resources, access to resources is limited for users and granted the minimum permissions required to perform their work. Technology building blocks to help implement least-privilege access include micro-segmentation, transport encryption and session protection. Per-app tunnel, as a specific example, lets certain applications access internal resources on an app-by-app basis. This restriction means that you can enable some apps to access internal resources while you leave others unable to communicate with your back-end systems.

Application Trust: Enabling employees to access any application, including traditional Windows applications, securely and seamlessly from any device is key to creating a digital workspace and enforcing zero trust. With the modernization of user authentication, allowing single sign-on (SSO) to applications, we gain both security and an improved user experience. For traditional applications that are not designed for zero trust, we add protection in the form of isolation. In order to isolate and modernize traditional applications, one can utilize a virtual desktop or application environment to create a bridge between the traditional architecture and the future based on zero trust.

Data Trust: Data is the most critical resource that requires protection. It is vital to protect against data breaches and leaks, and make sure it is the correct, unmodified data that our users are interacting with. Technologies such as data loss prevention (DLP) ensure unwanted exfiltration or destruction of sensitive data. Although data classification and integrity are, for the most part, handled by the application itself, we should enhance the trust level wherever we can when building a zero-trust architecture.

Once trust is established across all five pillars, informed decisions can be made to grant or deny access. Once the decision of granting access has been made, it is critical to constantly re-verify. If the trust level changes, organizations must be able to immediately act. In addition, by establishing trust across the five pillars, it is possible to gain visibility and can gather analytics across the digital workspace environment. And with visibility and analytics, it is possible to actualize automation and orchestration (Kueh, 2020).

### Zero Trust as an Amalgamation of Services

The goal of a Zero Trust (ZT) model is to secure sensitive data, systems, and services hosted in each enterprise or organization. The concept underlying the notion of ZT model is that “no actor, system, network, or service operating outside or within the security perimeter is trusted.” It requires deploying comprehensive controls for continuously verifying access attempts to sensitive resources. Therefore, “It is a dramatic paradigm shift in philosophy of how we secure our infrastructure, networks, and data, from verify once at the perimeter to continual verification of each user, device, application, and transaction.”. It thus involves a coordinated effort of communications/network services (e.g. network access controls, etc.), computing services (i.e. cloud, configuration management, etc.), information services (i.e. data protection standards, etc.), operational technology (i.e. IT infrastructure), end-user services, applications, and cybersecurity and privacy services(Bertino & Brancik, 2021)

### Zero trust Enforcement Guidelines By NIST

Data about Threats: External and internal threats need to be collected and analyzed. The security risk register which captures the specific known high security risks within an enterprise needs to obtained and evaluated.

Foundational Security Patterns: The collected data represent actual and/or potential risks for an organization and solutions to those risks need to be addressed through improved cyber hygiene and the development of a Zero Trust Architecture.

ZT Security Patterns: The output of the foundational security patterns provides linkages to where ZT security patterns are needed in order to identify candidate security services and product and process improvements to establish an initial ZT operational environment.

Selection of Services, Technology and Process Improvements: There are a number of services available to potentially include within a ZTA and this phase requires the initial selection of those services that are to be implemented.

Security Service Implementation: A implementation plan has to be developed and engineered to ensure the solution works as intended. The execution of the plan is critical to the success of the ZTA.

Security Control Testing: A test plan needs to be developed with test cases to capture planned versus actual results.

Performance metrics: The effectiveness of the implemented solution needs to be measured in reducing threats and known risks. Baseline metrics and key performance indicators must be created to demonstrate the value and success of the initial phase(s) of the ZTA(Bertino & Brancik, 2021).

### Zero Trust Electronic Authentication Procedures

NIST SP 800-63B addresses the rigorous guidelines for digital authentication and lifecycle management. Because Zero Trust dictates that identity has replaced the legacy network perimeter, the structural integrity of a ZTA framework is directly proportional to the robustness of its underlying authentication mechanisms (Grassi et al., 2025). The publication categorizes authentication strength into three fundamental Authenticator Assurance Levels (AALs), effectively serving as the trust tiers for identity validation.

AAL1 represents baseline assurance (permitting single-factor or basic multi-factor use), which is insufficient for high-security zero-trust applications. AAL2 serves as the operational standard for enterprise Zero Trust, strictly mandating Multi-Factor Authentication (MFA) backed by approved cryptographic techniques. AAL3, the paramount tier, demands proof of possession of specialized cryptographic keys (e.g., hardware tokens) to neutralize sophisticated, targeted phishing campaigns (Grassi et al., 2025).

The recent comprehensive update to these guidelines (Revision 4, published in 2025) introduces critical improvements directly aligned with Zero Trust modernization. It heavily prioritizes phishing-resistant authenticators (such as FIDO2 and WebAuthn) over traditional, easily compromised SMS-based One-Time Passwords (OTPs) (Grassi et al., 2025; Williams, 2025). Furthermore, Revision 4 modernizes usability by officially supporting syncable authenticators (passkeys) and explicitly advising against forced periodic password rotations, noting that complex, static passwords induce poor human security behaviors. From a ZTA perspective, SP 800-63B (Rev. 4) operates as the definitive scientific calibrator for feeding qualitative "Identity Assurance" telemetry into the SP 800-207 trust algorithm.
## Related works on Trust

### Context-based Access Control and Trust Scores in Zero Trust Campus Networks

This paper analyses the extent  to which Zero Trust Model is applicable to some commercial networks particularly open and heterogeneous research networks of universities. It presents an implementation of an identity-based network model that focuses on components that are necessary for authentication and authorization. Lukaseder et al. (2020), show the feasibility of the model through a prototype that protects access control to a Moodle eLearning platform. They clarify that zero trust does not mean the absence of trust, rather trust must be earned. A client must thus explicitly establish trust based on context before access can be securely granted. This context-based access control is based on a combination of checks such as device certificates, user authentication, or patch status of the accessing device. The basis for this framework is a trust calculation engine that considers a variety of inputs such as authentication attempts of the users (signs that may indicate an attack or compromised user accounts and devices), two factor authentication, client TLS, usage of a trusted VPN service, rough estimation of the location based on IP and browser fingerprinting. Similarly, the type of device, mobile or stationary, gives insights into how trustworthy it is is based on subjective logic. The trust scores are determined using the binomial opinion, which is formed over an entity which can be a network agent, a user, or a device. Subjective logic is a probabilistic logic that explicitly considers the uncertainty and trustworthiness of a source. Subjective opinions represent the belief in the substance of a statement under consideration of a possible uncertainty.

### Zero Trust-Based Adaptive Authentication using Composite Attribute Set

This paper proposes a system that collects a composite attribute set that includes the user behaviour, application attributes, and the device used. This allows for creation of detailed context that allows granular variance calculation and risk score determination. Its model as presented by Krishnan & Sreeja (2021), factors in user, application and device attributes separately to create a behavioural context. This is relevant as applications themselves can be reverse engineered or spoofed by an attacker. Even if the user credentials are entered correctly, a change in the application’s signature should be considered a risk. The approach extends to subsequent resource requests and does not stop with a successful first login or resource access. The attribute sets and contextual variance is considered in every request reaching the system. The variance of the user's current attribute set from established behaviour is used to determine the contextual variance and risk score. Depending on the variance and risk, an alternate authentication scheme that is commensurate with the risk score is chosen to challenge the user. The user’s trust score is re-adjusted to reflect the variance. Every step in the flow is logged by the system for audit and review. The model captures a broader range of variables and defines a storage schema for each attribute set separately. Auxiliary information such as “The server-side application being accessed” and “validity of the session can also be collected. This for better granularity.

### A Trust Computing Model for Future Generation Networks

Das & Debnath (2020), argue that future generation networks are heterogeneous in nature due to variety of nodes, terminals, small-sized networks, private networks, virtual networks, and IoTs , thus making authentication a major issue. Authentication of node is associated with trust, which is the primary behavior of a node in network operations. A major concern is the assessment of trust value of a node before actual data communication.  This paper thus reviews different trust computing models for different scenarios and proposes a novel model to give trust values of nodes in a network based on the maximum possible factors. Trust (i,j) means trust of node i over node j. Here node i is the trustor and node j is trustee. In the proposed model the final trust T(i,j) is nothing but the confidence of a node over another node. The risk is assessed using three factors namely ambiguity, vulnerability, and failure impact. Ambiguity in networks includes location ambiguity, flip ambiguity, and trilateration. Due to the ambiguity, a node is wrongly localized and data packets sent to wrong positioned node may be a futile task. In a versatile network, proper localization is a big task. Vulnerability is the security vulnerability which is very common in adhoc networks. Proper intrusion detection and prevention mechanisms can find out the extent of vulnerability of a node. It is very vital factor as it signifies the attacker’s motive. Failure impact is an index of a node that due to the mishandling and malfunction of a node if any failure occurred in the network environment or not. Though failure is an unpredictable event, it is also a risk factor. Risk factors are very rare but cannot be ignored. In the proposed model there is risk analysis part. If risk is found, the risk value is subtracted from the trust value.

### Research on Trust Management Model of Wireless Sensor Networks

This work presents a trust management model of wireless sensor based on multi-trust factor combination to calculate the trust value. This model has good robustness to many kinds of network attacks. First, the node's direct trust value calculation is divided into communication trust module, data trust module and energy trust module. Secondly, the cluster head uses the direct trust value calculation model to calculate the indirect trust value of nodes in a cluster. Finally, the integrated trust value of nodes is calculated by weighted credibility of direct trust and use the integrated trust value to eliminate malicious nodes, thus ensuring the entire network security.

In WSNs, to optimize the transmission routing, to achieve the purpose of saving energy, usually cluster network topology. This work builds a trust management model based on this network structure and cluster as the basic unit of trust management. In the cluster structure, nodes are generally divided into two types: cluster head nodes and common sensor nodes, which play different roles in this model.  The common sensor nodes in the cluster are responsible for monitoring and recording the communication, data transmission and performance of all its neighbours within a monitoring period. Based on the monitored information, it calculates the direct trust value of its neighbour nodes and regularly uploaded to the cluster head node. The monitoring data includes the number of normal behaviours and the number of abnormal behaviours of the monitored node.  The cluster head node is mainly responsible for collecting the direct trust values uploaded by each sensor node, integrating the multiple direct trust values of all the neighbour nodes of each node, and calculating the indirect trust values of all the nodes in the cluster (Cheng et al., 2018).

### Trust Threshold Policy for Explainable and Adaptive Zero-Trust Defense in Enterprise Networks

This work formulates zero-trust defense as a Partially Observable Markov Decision Process (POMDP), deriving an explainable trust-threshold policy that balances security enforcement against network usability through probabilistic belief updates on observations. The POMDP formulation represents a theoretically sophisticated alternative to the proposed Dempster-Shafer fusion approach among the reviewed works. While both frameworks model trust as a partially observable phenomenon, the POMDP treats the true entity state (adversarial vs. legitimate) as hidden and computes belief distributions over possible states via observation-conditioned updates, while our DS-based architecture models trust as an evidential mass distributed across{Safe}, {Unsafe}, and { Safe,Unsafe} (uncertainty). The critical architectural divergence is that POMDP requires the specification of transition matrices, observation models, and reward functions a priori, making it sensitive to model misspecification. The proposed variance-based DS approach, by contrast, constructs mass functions directly from observed telemetry variance without requiring explicit probabilistic models of attacker behavior, a significant advantage in open HetNet environments where the attacker model is unknown or evolving.

The trust-threshold policy's finding that "highly vulnerable systems or sophisticated attackers require stricter trust thresholds" directly parallels the proposed tiered decision architecture (T>0.75 for Full Access, 0.45≤T≤0.75 for Limited Access, T<0.45 for No Access), but our thresholds are derived from the Pignistic transformation of fused evidential mass rather than from POMDP value iteration. The POMDP approach’s focus on single-account enterprise contexts severely constrains its applicability to the multi-domain, multi-entity HetNet scenarios of this work. The proposed Ensemble model evaluates trust across four simultaneous telemetry domains with independent variance tracking, each contributing independently to the fused belief state.

The explainability advantage claimed by the POMDP threshold policy is matched by our architecture's Pignistic transformation, which provides a transparent, deterministic mapping from belief intervals to access decisions. The POMDP framework validates the theoretical necessity of probabilistic trust modeling but confirms that DS theory's capacity to explicitly model epistemic uncertainty (m(Θ)) without requiring complete probability distributions represents a more operationally deployable approach for heterogeneous environments.

### A Continuous Authentication Protocol Without Trust Authority for Zero Trust Architecture(Meng et al., 2022)

This work proposes a blockchain-based continuous device-to-device authentication protocol eliminating centralized Trust Authorities, using ECC for initial authentication and lightweight continuous verification with formal eCK security proofs. This protocol addresses a critical assumption in the proposed architecture: the integrity of the initial authentication event. The  Ensemble Trust Model treats the "Freshness" component at t=0 as a given, the initial cryptographic proof is assumed to originate from a compliant Identity Provider. This paper's contribution is the decentralization of that initial trust establishment through blockchain consensus, which eliminates the single-point-of-failure vulnerability inherent in centralized IdP architectures.

The continuous D2D authentication aspect directly complements the temporal decay mechanism. Where exponential decay forces re-verification by mathematically degrading trust over time (creating the temporal pressure for re-authentication), this protocol provides the mechanism for that re-authentication at the cryptographic layer. The two approaches operate at different architectural tiers, the Ensemble model computes whether re-authentication is needed based on (BetP(Safe) falling below thresholds, while this blockchain protocol provides how that re-authentication is performed without central coordination.

However, the assumption of blockchain availability is operationally challenging for the envisioned HetNet deployments. PBFT consensus requires a minimum quorum of participating nodes, which may not be achievable in disconnected or partitioned network segments. Additionally, the protocol's focus on D2D authentication does not address the multi-domain telemetry evaluation that the proposed four-domain architecture performs.

This work is architecturally complementary: it provides the decentralized cryptographic substrate that our trust computation engine can consume as its initial Freshness input. The combination of blockchain-based initial auth with the DS-fused temporal evaluation represents a complete zero-trust stack from cryptographic verification through behavioral monitoring.

### A Critical Analysis of Zero Trust Architecture ((Fernandez & Brazhuk, 2022))

This meta-analysis evaluates ZTA through the lens of classical security patterns and principles, constructs a preliminary Security Reference Architecture (SRA), and critically examines the practical feasibility, overhead costs, and implementability of zero-trust deployments.

This paper provides essential intellectual discipline for thework proposed in this thesis by mapping ZTA abstractions back to classical security principles: least privilege, complete mediation, fail-safe defaults, and defense in depth. The proposed architecture explicitly operationalizes several of these principles: the tiered access policy (Full/Limited/No Access) implements least privilege by restricting permissions proportional to evidential support; the continuous evaluation at every time step (t) implements complete mediation by never caching access decisions; and the explicit modeling of uncertainty (m(Θ)) implements fail-safe defaults by routing uncertain evidence toward access restriction rather than implicit grant.

The critical analysis's exposure of ZTA "hype" versus classical substance serves as a valuable check against overclaiming in this thesis. The paper's finding that ZTA overhead concerns remain empirically unanswered is directly relevant; the testbed validation provides partial empirical answers through measured latencies, although scaling to enterprise-grade deployments of 10,000+ nodes remains unvalidated.

The pattern-based approach to ZTA design suggests that the Ensemble model could be formalized as a trust computation pattern within the broader ZTA pattern catalog, making it reusable across different enforcement technologies (SDP, SASE, ZTNA) without modification to the core DS fusion algorithm.

The SRA framework and classical principle mapping provide the theoretical grounding for our architectural claims. The overhead critique directs our future work toward empirical performance benchmarking at enterprise scale.

### TrustS: Probability-based trust management system in smart cities (Mocanu et al., 2022)

TrustS presents a four-state Markov chain model (DOWN/UP/UP-SAFE/UP-UNSAFE) for computing node trust in smart city peer-to-peer overlays, utilizing stationary probabilities for deterministic behavioral assessment independent of overlay topology. The Markov chain formulation offers a computationally efficient alternative for resource-constrained environments. The four-state model captures an additional dimension, node availability (DOWN/UP) that most binary frame (Θ={Safe,Unsafe}) do not explicitly model. This is operationally relevant because most architectures assume continuous sensor availability; a domain that ceases reporting is handled implicitly through variance computation (absent readings increase variance, collapsing the domain weight toward zero), but TrustS's explicit DOWN state provides a cleaner mathematical treatment of intermittent connectivity scenarios common in mobile HetNets and IoT deployments.

However, the Markov model's reliance on accurate transition probability estimation (α, the trust coefficient) is directly analogous to the calibration challenge of our sensitivity parameter (α in ​). While this system is sensitive to  respective parameterizations, but a variance-based approach computes weights empirically from observed signal stability, whereas the Markov model requires predetermined transition probabilities, a disadvantage in unknown or rapidly evolving adversarial environments.

The Markov model computes trust deterministically from stationary distributions, meaning it characterizes the long-run average behavior of a node. This fundamentally conflicts with a core argument that trust must be temporally dynamic: the stationary distribution, by definition, is time-invariant. TrustS cannot capture the session ephemerality or temporal decay that the proposed Ensemble model enforces through the Freshness-Inertia continuum.

The explicit availability state (DOWN/UP) suggests a potential extension to the proposed binary frame to a ternary frame (Θ={Safe,Unsafe,Unavailable}) for IoT deployments. However, the Markov model's time-invariant stationary analysis is architecturally incompatible with the proposed temporal decay requirements.

### An Artificial Intelligence Approach for Deploying Zero Trust Architecture (Hosney et al., 2022)

This work explores Machine Learning classification algorithms  as an alternative to manual zero-trust policy configuration, aiming to automate the prediction of allow/deny decisions from static firewall configurations in simulated environments. The AI-driven policy engine addresses a scalability challenge that the proposed mathematical architecture does not: the configuration of trust parameters. The architecture requires the manual specification of sensitivity parameters (α), temporal decay rates (λ), observation window lengths (N), and access thresholds,all of which are treated as empirically calibrated constants. An ML classifier that could learn optimal parameter configurations from operational data would represent a valuable automation layer atop our fusion engine.

However, the Decision Tree approach applied in this work operates at a fundamentally different abstraction level than our DS-based fusion. The ML classifier produces binary allow/deny predictions from static configurations, which recreates the very binary decision structure our tiered access architecture (Full/Limited/No Access) was designed to transcend. A Decision Tree cannot output "Limited Access with 26.2% residual uncertainty (m(Θ)=0.262)", it can only output a class label. This loss of granularity eliminates the proportional, uncertainty-aware response that constitutes our architecture's primary innovation.

The reliance on synthetic training data is a significant limitation shared with the proposed testbed validation. However, the mathematical approach is deterministic and analytically verifiable, whereas ML models trained on synthetic data face the additional challenge of domain shift when deployed against real-world distributions.

ML-based policy automation represents a viable future enhancement layer for our architecture, particularly for the dynamic calibration of α and λ parameters using supervised learning from operational feedback. This is identified as a future work direction (Unsupervised Machine Learning for Behavioral Inertia).

### Integrating Trusted Computing Mechanisms with Trust Models to Achieve Zero Trust Principles ((Alawneh & Abbadi, 2022))

This work outlines a theoretical framework integrating hardware-based Trusted Computing Group (TCG) mechanisms, specifically TPM modules and Chains of Trust (CoT)—with enterprise trust models to enforce "Never Trust, Always Verify" through continuous hardware/software property attestation.

TCG integration addresses a fundamental assumption in the proposed architecture's Device domain: that the reported device posture telemetry is authentic and has not been tampered with at the hardware level. Our variance-based weighting can detect behavioral inconsistency in device reporting (high variance triggers weight reduction), but it cannot detect a compromised TPM that consistently reports falsified-but-stable posture data. Hardware attestation via CoT provides the cryptographic root-of-trust that validates the authenticity of the signals our fusion engine consumes.

In the proposed architecture, device posture is one of four telemetry domains feeding the DS fusion pipeline. TCG attestation would strengthen this specific domain by providing hardware-verified ground truth, reducing the epistemic uncertainty (m(Θ)) associated with device signals during mass function construction. A hardware-attested device with verified CoT would justify a lower m(Θ) (higher confidence) compared to a software-only attested device, directly influencing the fusion output.

However, the assumption of universal TPM availability is problematic for heterogeneous environments. BYOD devices, consumer IoT sensors, and legacy embedded systems rarely include TPM 2.0 modules. Graceful degradation in the absence of hardware attestationtherfre becomes a strength; the variance-based weighting mechanism treats unreliable or missing attestation signals the same way it treats any unstable telemetry: by discounting the domain weight and shifting mass to uncertainty, ensuring the system degrades safely rather than catastrophically.

Hardware attestation enhances the trustworthiness of the Device domain's input to the fusion engine. The CoT concept maps directly to  "Freshness" component, providing cryptographic proof of device integrity at session initiation that our temporal decay subsequently depreciates.

### Secure Access Service Edge: A Zero Trust Based Framework for Accessing Data Securely ((Yiliyaer & Kim, 2022))

This work reviews SASE framework, converging ZTA with SD-WAN, Secure Web Gateways (SWG), and Cloud Access Security Brokers (CASB) for securing distributed remote workforces with reduced backhaul latency.

SASE represents the cloud-native enforcement topology within which the Ensemble Trust Model would be deployed at scale. Its  architecture's separation of the trust computation engine (PDP) from the enforcement layer (PEP) aligns architecturally with SASE's distributed Points of Presence (POPs), where the DS fusion engine would execute at the POP level to make local access decisions without requiring round-trip consultation with a centralized policy server. This distributed deployment model directly addresses the latency concerns we acknowledge in our testbed limitations.

The SASE framework's incorporation of SWG and CASB provides the application-layer inspection capabilities that correspond to our Application/Data Sensitivity domain. The thesis evaluates this domain through abstract trust scores, but SASE provides the concrete enforcement mechanisms such as URL filtering, DLP policies or API security that would generate the raw telemetry our fusion engine consumes.

The paper's identification of legacy system migration and hybrid-cloud interoperability as barriers directly parallels this thesis delimitations, explicitly assume a baseline level of network modernization and exclude legacy mainframe integration. The financial constraints highlighted by the paper also validate a vendor-agnostic approach: by focusing on mathematical algorithms rather than specific SASE vendors, the contributions remain transferable across commercial implementations.

SASE provides the deployment topology for operationalizing the Ensemble model in cloud-distributed environments. The POP-based architecture validates our PDP/PEP separation and suggests that the DS fusion engine should be designed for edge-distributed execution.

### Towards Zero Trust: The Design and Implementation of a Secure End-Point Device for Remote Working ((Bicakci et al., 2021))

This work presents "ProGun," a secure USB dongle implementing FIDO2 multi-factor authentication, Risk-Based Authentication (RBA), GPS-based location verification, and encrypted trusted boundaries for remote zero-trust enforcement at the endpoint.

ProGun provides tangible hardware instantiation of the "Freshness" component in the proposed  Ensemble model. At t=0, the proposed architecture requires a cryptographic proof of identity that is abstracted as the initial trust score. ProGun's FIDO2 + GPS attestation mechanism generates exactly this proof with hardware-rooted assurance, producing a high-confidence initial Device domain score (Sd​≈0.95) and Identity domain score (Si​≈0.98) that the temporal decay subsequently depreciates.

The RBA component triggering additional authentication challenges based on contextual anomalies is functionally equivalent to behavior when BetP(Safe) crosses a threshold boundary. When the Ensemble model detects that trust has decayed into the "Limited Access" tier, the operational response should be precisely the RBA-style re-authentication challenge that ProGun implements. This establishes a complete feedback loop: the mathematical engine determines when re-authentication is needed; ProGun provides how it is performed at the hardware level.

However, the device-specific nature of ProGun limits its scalability. The dongle addresses a single endpoint; the proposed architecture evaluates trust across the entire session continuum across four domains simultaneously. The paper acknowledges that its rule-based heuristics are insufficient against advanced session hijacking, precisely the attack vector that the Ensemble model's behavioral inertia mechanism is designed to counter. A session hijacker who lacks the victim's historical behavioral baseline will trigger our Inertia Component collapse regardless of possessing the victim's ProGun token.

ProGun and similar hardware tokens serve as the physical authentication substrate that feeds our trust computation engine. The ProGun-to-Ensemble pipeline represents a complete zero-trust stack: hardware-rooted initial verification to continuous DS-fused behavioral evaluation to temporally decaying trust to  proportional access enforcement.

### Design of Network Communication Security Scheme Based on Dynamic Trust Estimation

This work constructs a network communication architecture that dynamically evaluates and updates node trust values using graph-based models, formulating strict communication permission rules combined with encryption and intrusion detection for comprehensive protection.

The dynamic trust estimation approach shares this thesis's core premise of continuous evaluation, but operates at the network topology level  rather than multi-domain evidential level. The graph constraint, currently restricted to undirected networks is a significant limitation that a domain-independent fusion approach avoids. The DS combination rule is agnostic to network topology; it fuses evidence from four independent domains regardless of whether the underlying network is directed, undirected, hierarchical, or mesh.

The work's integration of trust values with encryption and intrusion detection mirrors the proposed architectural vision of embedding trust computation within the broader security stack ; alongside SDP controllers, IDS/IPS, and SIEM platforms. However, the static initial weight assignment and predefined equilibrium coefficients introduce the same inflexibility this thesis identifies as the "Peril of Inflexible Calibration".  Variance-based dynamic weighting eliminates static weight assignment by computing weights empirically from observed signal stability at every evaluation epoch.

The graph-based trust propagation model could complement the proposed point-evaluation architecture by incorporating topological awareness understanding; not just how trustworthy an entity is, but how its trust propagates through the network graph. This is relevant for our lateral movement defense scenarios.

### Targeted Context-Based Attacks on Trust Management Systems in IoT ((Mocanu et al., 2022))

This work proposes and demonstrates "context-based attacks" where adversaries spoof contextual properties such as location and device type to target specific device groups in IoT Trust Management Systems, successfully compromising seven existing trust models and subsequently developing a mitigating TMS using distance scaling and timeout mechanisms.

This paper exposes a vulnerability that is directly relevant to the proposed architecture's variance-based weighting mechanism. If an attacker can manipulate the context rather than the behavior of a domain, for example, spoofing a device posture reading to appear consistently healthy when the device is compromised, the variance (σ2) would remain low (the spoofed signal is stable), and the dynamic weight would remain high, allowing the compromised domain to retain disproportionate influence in the fusion output. This represents a potential attack vector against the Weighted Belief Fusion pipeline that this current architecture does not explicitly address.

However, the multi-domain fusion architecture provides a natural partial defense against context-based attacks that single-domain trust models lack. An attacker who successfully spoofs one domain's context such as Device posture, must simultaneously maintain consistent spoofing across all four independent domains (Identity, Device, Network, Application) to avoid triggering cross-domain conflict in the Dempster's combination rule. The conflict factor   explicitly detects inter-domain disagreements, meaning a spoofed Device domain reporting "Safe" while the Network domain detects anomalous traffic would generate elevated conflict factor, triggering the normalization mechanism that redistributes evidential mass away from the conflicting sources.

The proposed mitigation using distance scaling and behavioral timeouts is conceptually aligned with the temporal decay mechanism since both impose a finite validity window on trust assessments. The timeout mechanism in the mitigation performs the same function as exponential decay forcing periodic re-evaluation regardless of apparent behavioral consistency.

This work validates the necessity of multi-domain fusion (rather than single-domain evaluation) as a defense against context manipulation, and confirms the importance of temporal expiration mechanisms. It also identifies a concrete attack vector (context spoofing with low variance) that represents a limitation of our variance-based weighting approach, explicitly acknowledged in the Limitations section.

### Tag-Based Trust Evaluation In Zero Trust Architecture (Zhang et al., 2022)

This work introduces Tag-Based Trust Evaluation (TBTE), combining score-based and criteria-based approaches through fact, prediction, and model tags derived from user and device data, to create explainable, rule-based trust decisions within ZTA Policy Decision Points.

The TBTE framework addresses a legitimate gap in architecture: the interpretability layer between raw evidential computation and policy enforcement. While the proposed Dempster-Shafer fusion engine produces mathematically rigorous trust scores, the TBTE approach of decomposing entity attributes into discrete, labeled tags (fact tags for static properties, prediction tags for behavioral forecasts, model tags for computed risk categories) provides a complementary mechanism for translating continuous trust scores into human-readable policy justifications. This could enhance the explainability of PDP decisions, particularly for compliance auditing where organizations must demonstrate why a specific access decision was made (Zhang et al., 2022).

However, the TBTE framework suffers from a fundamental limitation: its rule engine operates on static, predefined conditional logic ("if device_health_tag = compromised AND location_tag = external, THEN deny"). This creates precisely the brittle, binary decision structure that Dynamic Weighting with Temporal Decay is designed to eliminate. Additionally, gray-area routing, where ambiguous evidence results in Limited Access rather than a binary Allow/Deny, cannot be replicated by rule-based tag evaluation without exponentially expanding the rule set to cover every intermediate state.

The validation on only 1,000 simulated users and 10 resources is also insufficient for the enterprise-scale scenarios. The TBTE approach provides no mechanism for temporal decay; a tag assigned at authentication time persists until explicitly updated, creating the same "implicit trust period" vulnerability that our exponential decay function eliminates.

The tag taxonomy (fact/prediction/model) could serve as a presentation layer atop an evidential fusion engine, translating mass functions into auditable, human-readable tags for compliance purposes. However, tag-based rules cannot replace the continuous, probabilistic nature of the proposed DS-based evaluation.

## Empirical Framework Summary

The works reviewed in the preceding sections collectively illuminate a convergent set of structural deficiencies that no single existing contribution addresses holistically. This section distils the critiqued literature into four interlocking gap dimensions, culminating in the precise trust reseach cinntributions that this thesis makes.

### 1. Evidential Uncertainty and Multi-Domain Fusion

Among the probabilistic approaches surveyed — Bayesian inference, Hidden Markov Models, POMDP belief states, and Markov chain stationary distributions (TrustS), each imposes a critical assumption: the availability of complete prior distributions over the trust domain. In heterogeneous enterprise networks, where sensor availability is intermittent and attacker models are unknown, this assumption is operationally untenable. Dempster-Shafer theory resolves this constraint by providing explicit uncertainty representation through unprojected belief mass (m(Θ)) — the capacity to mathematically express "I do not have enough evidence to decide", without requiring complete priors.

Yet the surveyed DS applications remain limited to single-domain evaluations. The context-based attack literature demonstrates that single-domain trust is inherently vulnerable to context spoofing: an attacker who compromises one domain can present fabricated metrics that a single-domain model cannot detect. This thesis addresses both limitations simultaneously through its four-domain fusion architecture, where Dempster's combination rule detects inter-domain conflict (κ) when spoofed domains disagree with honest ones — transforming the network's heterogeneity from a liability into a defensive asset. As (Chen et al., 2025) and (Kang et al., 2022) note, robust trust calculation requires both accurate multi-source aggregation and reliable contextual transfer of trust values; this architecture addresses both requirements structurally.

#### Temporal Fragility of Continuous Trust

A striking deficiency across the surveyed literature is the near-universal absence of mathematically rigorous temporal decay. The HetNet trust survey, POMDP framework, tag-based evaluation, and Markov models all compute trust at discrete time points without enforcing session ephemerality.

This gap has profound operational consequences. The Cloud Security Alliance's SDP v2.0 provides exemplary session initiation protocols through Single Packet Authorization and multi-stage posture checks, but treats trust as a binary state achieved at the perimeter boundary — it lacks an algorithmic mechanism for continuously degrading trust over a sustained session. NIST SP 800-207 acknowledges the need for continuous verification, mandating that the Policy Engine ingest observability data, yet explicitly leaves the Trust Algorithm's internal mechanics abstracted: it specifies input variables (Identity Assurance, Device Posture, Behavioral Signals) but offers no standardisation on how to weight, synthesise, or decay them over time. As Shin et al. (2025) and Xu (2024) observe, this forces engineers to rely on rigid linear timeouts or aggressive exponential kill-switches — both conflicting with enterprise productivity.

This thesis fills the temporal gap through the Freshness-Inertia continuum, modelling trust decay as configurable linear and exponential functions (governed by λ) that bridge NIST's architectural mandate for continuous verification with the operational reality of session continuity.

#### 3. Enforcement-Computation Separation

The SDP, SASE, micro-segmentation, and ProGun works provide enforcement mechanisms — the "last mile" translating trust scores into access decisions — but none includes a native, mathematically principled trust computation engine. They assume trust scores arrive from an external source without specifying how those scores should be generated, weighted, or temporally managed. Conversely, relying strictly on static fail-closed enforcement during minor telemetry fluctuations (e.g., a momentary Wi-Fi drop) creates user friction that undermines security adoption.

This confirms the thesis's architectural decision to separate trust computation (Policy Decision Point) from trust enforcement (Policy Enforcement Point). The Ensemble Trust engine remains enforcement-agnostic — capable of driving SDP gateways, SDN flow rules, or Envoy proxy sidecars — while the enforcement layer remains algorithm-agnostic. This decoupling enables graduated response (full, limited, or denied access based on continuous trust scores) rather than binary fail-open/fail-closed behaviour.

#### Convergent Research Gap

The literature demonstrates that while the architecture of Zero Trust (SDP, SDPN) and the standards of Zero Trust (NIST SP 800-207) are highly mature, the algorithmic calculus required to manage dynamic trust across time, domains, and enforcement substrates remains nascent. No existing work simultaneously addresses:

Evidential uncertainty quantification — representing incomplete knowledge as a first-class mathematical object rather than forcing uniform priors;

Temporal trust depreciation — enforcing session ephemerality through continuous decay rather than binary timeout thresholds;

Multi-domain conflict detection — fusing trust from heterogeneous domains while detecting inter-domain inconsistencies indicative of compromise;

Enforcement-agnostic computation — producing trust scores that drive any PEP technology without algorithm-enforcement coupling.

This convergent gap validates the core contribution of this research: a hybridised Ensemble Trust Model that mathematically augments SDP and NIST's cryptographic boundaries with spatial belief fusion, continuous temporal inertia, variance-based weighting, and multi-domain conflict detection — bridging the gap between absolute security and operational continuity.

#### Identified Extensions

The literature suggests three extensions constituting natural future research directions: (1) hardware-rooted attestation via TCG/TPM to validate telemetry authenticity at the silicon level; (2) AI-driven parameter optimisation for α (variance sensitivity) and λ (decay rate) calibration via reinforcement learning; and (3) collusion detection mechanisms to counter coordinated multi-domain compromise. These align with future work directions in Chapter 10.

## Research Gap

On review of security models especially in modern and heterogeneous networks, trust calculation and trust models emerge as an important issue. According to (Randhawa et al., 2017), there are key research issues to be considered in enhancement and development of robust of trust calculation engines: the accuracy of a trust model while computing information gathered from multiple heterogeneous sources, the consensus approach when modeling multiple attributes of heterogeneous networks and how to accurately use trust values in a given context which have been computed in a different context.

This work thus proposes the address the second and third issues by creating a dynamic trust model based on a multi-attribute set for heterogeneous networks. The composite attribute set is based on the pillars of zero trust architecture while the implementation is based on software defined perimeters to optimize the deployment environment. The model acts s guide for dynamic trust calculation though earning and/or loss of trust. This results in context determination for all resource access requests resulting in an appropriate behavioral context to determine subsequent the access decision.

While the reviewed literature collectively establishes a formidable, mathematically rigorous foundation for modern cybersecurity, a critical traversal of these documents reveals a prominent operational gap: the temporal fragility of continuous trust evaluation.

The Cloud Security Alliance's SDP v2.0 and Architecture Guide provide exemplary protocols for the initiation of a Zero Trust session (the "Join" process). By enforcing Single Packet Authorization (SPA) and multi-stage posture checks, they successfully eliminate the implicit trust of legacy VPNs. Furthermore, the integration of Software-Defined Perimeter Networks (SDPN) proves that this identity-centric control can be pushed down to the fundamental routing layer. However, these frameworks largely treat trust as a binary state achieved at the perimeter boundary. They lack a standardized, algorithmic mechanism for continuously degrading that trust over the lifespan of a sustained session without forcing disruptive, repetitive MFA challenges.

NIST SP 800-207 acknowledges this necessity, mandating that the Policy Engine continuously ingest observability data. Yet, the framework explicitly leaves the internal mechanics of the Trust Algorithm highly abstracted. It provides the input variables (Identity Assurance calibrated flawlessly by NIST SP 800-63B, Device Posture, Behavioral Signals) but offers no mathematical standardization on how to weight, synthesize, or decay these variables over time. As highlighted by recent scholarly critiques (Shin et al., 2025; Xu, 2024), this abstraction forces security engineers to rely on rigid, linear session timeouts or hyper-aggressive exponential kill-switches, both of which conflict directly with modern enterprise productivity requirements.

Similarly, while the theoretical framework of "fail-safe defaults" remains the bedrock of Zero Trust denial logic, relying strictly on a static fail-closed mechanism during minor environmental telemetry fluctuations (e.g., a momentary drop in Wi-Fi signal) creates overwhelming user friction.

The literature distinctly demonstrates that while the architecture of Zero Trust (SDP, SDPN) and the standards of Zero Trust (NIST) are highly mature, the algorithmic calculus required to manage dynamic trust across time remains nascent. This synthesis consequently validates the core thesis of this research: there is a distinct, critical necessity for a hybridized Ensemble Trust Model. To operationalize Zero Trust effectively, the uncompromising cryptographic boundaries defined by SDP and NIST must be mathematically augmented to fuse spatial belief verification with continuous temporal inertia—thereby bridging the final gap between absolute security and operational continuity.


*📌 Takeaway: ZTA provides the 'what' but lacks a 'how' (trust computation engine) and a 'where' (enforcement substrate). The next chapter examines Software-Defined Perimeters as the substrate for executing dynamic trust decisions.*



---

# Chapter 5: Software-Defined Perimeters as Underlying Substrate

*Chapter 4 revealed that Zero Trust Architecture defines what should be verified but provides neither the algorithmic engine for computing trust dynamically nor the enforcement substrate for executing trust-driven access decisions. Before we can build the 'how' (trust engine), we must establish the 'where'—the enforcement architecture that can execute dynamic trust decisions. This chapter justifies Software-Defined Perimeters as that substrate.*

## Software Defined Perimeters

### SDP Specification Version 2.0

The Cloud Security Alliance (CSA) released the Software-Defined Perimeter (SDP) Specification v2.0 as a critical evolution to address the inadequacies of legacy perimeter paradigms. Scholarly evaluations spanning 2023 to 2025 highlight that while SDP v1.0 successfully conceptualized "network cloaking," v2.0 explicitly cements SDP as the structural foundation for executing modern Zero Trust Architecture (ZTA), often referred to in literature as "Zero Trust 2.0" (Alawida et al., 2024; Smith & Jones, 2025). Empirical studies demonstrate that executing this architecture drastically reduces the attack surface, with recent deployment metrics showing up to a 94.7% reduction in external network scanning vulnerabilities and a 91.2% decrease in traditional VPN-related security incidents (Oqaily et al., 2024).

A foremost improvement in v2.0 is the profound overhaul of the Single Packet Authorization (SPA) protocol. Moving beyond basic port knocking, v2.0 fortifies the SPA format with cryptographic nonces (to defeat replay attacks), rigorous timestamping, and Hash-based Message Authentication Codes (HMAC) to guarantee payload integrity before any TCP connection is established (Cloud Security Alliance, 2024). This cryptographic rigor is increasingly vital to defend against emerging, AI-native brute-force methodologies that traditional firewalls fail to detect. Furthermore, v2.0 expands operational deployment topologies. It explicitly introduces Gateway-to-Gateway routing protocols essential for securing complex, decentralized topographies such as 6G-Internet of Things (IoT) clusters and federated cloud-edge networks, mitigating massive-scale Botnet and DDoS threats (Chen et al., 2025). Additionally, the specification now mandates Mutual TLS (mTLS) for all internal and external component communications, fundamentally elevating the standard from simple perimeter obfuscation to comprehensive, verifiable cryptographic trust at every network boundary (Appgate, 2024).



[Figure/Image from source paragraph 323]

Figure 2.5:SDP v2.0 Single Packet Authorization (SPA) Workflow emphasizing the "Black Hole" default state.

### SDP Architecture and Operations

The operationalization of SDP is heavily dependent on the harmonious interaction of three core infrastructure components: the SDP Client (Initiating Host), the SDP Controller (Policy Decision Point), and the SDP Gateway (Accepting Host). Recent architectural literature (2024-2025) emphasizes that the strength of this triad lies in its dynamic, identity-centric verification processes, permanently separating the control plane (authentication) from the data plane (access) (Appgate, 2024; Johnson, 2024). A major theoretical limitation of early SDP designs was the Controller acting as a single point of failure and a massive performance bottleneck during high-concurrency access requests. The modern architecture guide resolves this by establishing "Operational Independence." Once the Controller authenticates the Client, it issues cryptographic tokens allowing the Client to communicate directly with highly distributed Gateway clusters. This enables dynamic load-balancing and auto-scaling of Gateways without tethering every packet evaluation back to the Controller, proving highly performant at enterprise scale (Smith, 2024).

The operational processes of joining and leaving the perimeter are rigorously engineered to eradicate implicit trust windows. The Join (Onboarding) process involves a stringent, multi-phased verification workflow. First, the Controller authenticates the user's identity via modern Identity Providers (IdP). Crucially, the Controller simultaneously polls the SDP Client to verify device health telemetry—including OS patching, encryption status, and EDR agents (Appgate, 2024). While this multi-stage validation ensures extreme resilience to DoS and port-scanning, recent performance studies note it incurs a slightly longer initial connection setup latency compared to legacy VPNs (Oqaily et al., 2024). Only upon a successful holistic evaluation does the Controller issue a cryptographic entitlement to the Gateway. The Gateway subsequently opens an individualized, encrypted tunnel to the specific authorized resource, ensuring micro-segmented access that neutralizes lateral attacker movement.

Conversely, the Leave (Offboarding) process abandons legacy session timeouts in favor of highly reactive continuous monitoring. Because trust evaluation in modern SDP architectures is an ongoing dialogue, any deviation in device posture or deactivation of the user account at the IdP results in the immediate, algorithmic revocation of the Gateway entitlement, severing the network connection in real-time (Johnson, 2024).



[Figure/Image from source paragraph 330]

Figure 2.:The SDP Join Operational Workflow detailing the separation of Authentication and Data Access.

## SDP and SDN Confluence

Software-Defined Networking (SDN) and Software-Defined Perimeters (SDP) emerged to solve distinctly different networking challenges. SDN revolutionized network engineering by decoupling the control plane from the data plane, enabling centralized, programmable, and highly efficient traffic routing across enterprise architectures (Lefebvre et al., 2023). However, SDN inherently assumes a degree of internal trust; its primary objective is optimized packet delivery, not granular, identity-based access control. Conversely, SDP enforces absolute Zero Trust principles by authenticating entities before granting network visibility, yet it traditionally lacks the deep, underlying traffic routing optimizations characteristic of SDN.

The Software-Defined Perimeter Network (SDPN) represents the synthesis of these two paradigms, aiming to construct a unified, Zero Trust overlay network that dictates both security and routing logic. As analyzed in contemporary networking literature, SDPN integrates the multi-plane management model of SDN directly with the identity-centric access frameworks of SDP (Al-Mutairi & Hassan, 2024; Lefebvre et al., 2023). Within the SDPN control plane, the routing intelligence of an SDN controller is merged with the authentication gatekeeping of an SDP controller. This creates a singular, logically centralized trust anchor.

At the data layer, servers, endpoint devices, and network functions are flattened into standardized "nodes" managed by the SDPN control channel. By executing this merger, the SDPN controller not only dictates who is cryptographically authorized to communicate, but also programs the exact, optimal network path that the communication must traverse (Lefebvre et al., 2023). This unified architecture effectively drives Zero Trust principles down to the packet routing layer, neutralizing traditional TCP/IP broadcast vulnerabilities while preserving the dynamic performance scalability optimized by SDN.

### Scaling and Separation of Roles

The rapid increase in volume in global IP traffic and the adoption of mobile devices have challenged network service providers to scale and improve infrastructure to meet this new demand. To improve return on investment for scaling networking infrastructure and capitalize on advancements in virtualization technologies, Network Function Virtualization (NFV) has been implemented through software defined systems. One such implementation is the use of software defined perimeters to provision and deprovision identities and privileges. Software- Defined Perimeter (SDP) is a framework to provide logical perimeters around these services, restricting network access and connections to the SDP-enabled endpoints to trusted clients only. The deployment and access control are customize-able, catering to a wide array of user needs (Singh et al., 2020). SDPs are based on the general software defined networks that decouple the control and data planes (as illustrated in Figure 2.1) of the infrastructure as an enabler to better scaling and automation of the configuration processes in the control plane. The separation also allows for addition of components on the transport plane for load balancing and redirection without affecting the instructions and metadata updates shared on the link states of the nodes and their connections as outlined by Sallam et al. (2019). This thus allows allows for specialization of automation and orchestration functions on the control plane while allowing for scaling of data access on the data plane.



[Figure/Image from source paragraph 340]

Figure .: Planes on SDN and SDP (from: (Moubayed et al., 2019))

SDP as an architectural model provides an avenue for securing network-connected infrastructure based on controller- based authentication and authorization to connect clients to resources as illustrated in Figure 2.2.



[Figure/Image from source paragraph 344]

Figure .: SDP Architecture (From: (Singh et al., 2020))

SDP consists of two main building blocks: hosts and controllers. The SDP controller handles which hosts can communicate with each other. They can request identifying hardware and/or software information to verify the connecting host. Hosts can be either initiating or accepting SDP Hosts. Initiating Hosts request from the SDP controller a set of Accepting Hosts to communicate with. Accepting Hosts will only communicate with the SDP controller and any hosts that the controller commands it to. Thus, the SDP effectively separates the control plane and the data plane in a scalable manner (Singh et al., 2020). This thus creates a perimeter on demand based on resource requests by users. The SDP architecture is composed of and relies on five separate security layers.

Single Packet Authentication (SPA): SPA is the cornerstone of device authentication. The SDP uses this SPA to reject traffic to it from unauthorized devices. The first packet is cryptographically sent from the client’s device to the SDP controller where the device’s authorization is verified before giving it access. The SPA is then again sent by the device to the gateway to help it determine the authorized device’s traffic and reject all other traffic.

Mutual Transport Layer Security (mTLS): Transport layer security (TLS) was originally

designed to enable device authentication and confidential communication over the Internet.

Even though the standard offers mutual device authentication, it has typically only been used to authenticate servers to clients. However, the SDP utilizes the full power of the TLS standard to enable mutual two-way cryptographic authentication.

Device Validation (DV): Device validation adds an extra layer of security by ensuring that

the cryptographic key used is held by the proper device, because mTLS only proves that the key has not expired, nor has it been revoked. However, it cannot prove that it has not been stolen. Therefore, DV verifies that the device belongs to an authorized user and is running trusted software.

Dynamic Firewalls: In contrast to traditional static firewalls that can have hundreds or thousands of rules, dynamic firewalls have one constant rule which is to deny all connections. The SDP adopts a dynamic firewall policy at the gateway by vigorously adding and removing rules to allow authenticated and authorized users to access the protected applications and services.

Application Binding (AppB): Application binding refers to the process of forcing authorized

applications to use the encrypted TLS tunnels created by the SDP. This is done after the device and the user are properly authenticated and authorized. This ensures that only authorized applications can communicate through the tunnels while unauthorized applications are blocked (Moubayed et al., 2019).

SDP uses Single Packet Authorization (SPA) to initiate any of the communication channels: Controller to Host or Host to Host. The SPA is expected to be the first message received for any communication, which yields some interesting result. The Accepting Host first communicates with the Controller and authenticates itself to the Controller. Then the Initiating Host connects to and authenticates itself to the Controller. It can then initiate an SPA message, which the Controller relays to the Accepting Hosts and then allows the Initiating Host to establish a mutual TLS connection. The server does not respond to connections until an authentic SPA is received. This essentially ’blackens’ the server from unauthorized connections, meaning that the services are invisible to anyone not authorized to connect. This can ultimately reduce remote connection attacks, as the remote device attempting to connect will not be able to provide the expected SPA message. The use of SPA will also mitigate NFV Controller targeted DoS attacks, as the server can eliminate DoS attempts before they can flood the network with attempted TLS handshakes as illustrated in the sequence diagram in Figure 2.3



[Figure/Image from source paragraph 360]

Figure 2.9: SDP Service Provisioning (From:(Moubayed et al., 2019))

### SDP Open Challenges

Despite the many advantages that the SDP architecture provides with respect to protecting against various network security breaches and attacks, it faces several challenges.

- Possible Network Disruption: Since the SDP architecture is different than traditional security measures deployed in networks, integrating a complete SDP solution can lead to network and infrastructure disruption. This can be problematic due to the size of the services that may be off during such a disruption.

- Configuration Updates: A second challenge is updating all the applications and system configurations in such a manner that they become aware of the SDP. This will allow them to access the workflow and the secure tunnels created within the SDP.

- Controller Vulnerability: Because the SDP controller has a major role in the architecture and hence the overall security of the network, protecting it becomes paramount. Moreover, given that it is a possible centralized point of failure, it needs to be made highly available and secured.
## Context Adaptive Trust Estimation

This works by first collecting and collating  access request data from the five facets covered in zero trust. The data will represent variations of identities that are available for selection and weighting to determine that eventual trust value.  The ratio of weighting for these identities will vary depending on supplements in the heterogeneous networks. The supplements represent the trends and patterns of behavior relating to whitelisted devices, networks and/or users and the data they request access to. These will be used by the policy decision point to adjust the trust factor thus resulting in a dynamic determination of trust values. These parameters guide the context establishment and subsequently the trust/risk value. The variation from the acceptable risk/trust value determines access permission, denial of permission or the requirement for an extra factor of authentication and/or authorization. The result is then shared with the policy decision point while the feedback is relayed back to the user with its determination of the access decision to the resource as shown in Figure 5.4.



[Figure/Image from source paragraph 690]



[Figure/Image from source paragraph 691]

Figure 3.6: Adaptive Context Based Trust Estimation

## Proposed Trust Algorithm

The trust algorithm is responsible for calculating the trust scores for each access request. The trust scores are determined based on the  defined parameters and the available attributes per parameter and a decay/residual trust  value that is based previous access attempts of users. These are checked for signs that may indicate an attack or compromised user accounts and devices. The calculation is a recursive algorithm that estimates trust value as a factor of context awareness and decay value on previous trust. The idea is to reward peers for reliable participation in successful accesses. In addition, the trust value considers unsuccessful accesses by creating a hidden decay/residual value that is applied when the peer performs their next transaction. The trust scores are determined using the binomial opinion, which is formed over an entity which can be a network agent, a user, or a device. Subjective logic is used to calculate the confidence values. Z ∈ {, } a binary range with binomial random variable X ∈ Z. A binomial opinion about the truth of value x is the ordered quadruple.

With

And the corresponding parameters defined as

Due to the nature of the attributes for the parameters defining the contexts, the outcomes can only be binomial opinions i.e. a statement can assume exactly two values, trustworthy or not trustworthy. The different opinions are linked by a cumulative belief fusion to reduce the uncertainty of the individual opinions. A belief fusion is used in this work to fuse different opinions about the trustworthiness of an entity. The cumulative belief fusion describes that increased indications for or against the trustworthiness of an entity are confirmed in their statement and reduce the individual uncertainties. Several independent sources, which point to an offense, can thus increase the belief in this offense. In the case that two binomial opinions A and B show a perfect certainty , their values are fused according to:

=)

=0

=)

Adaptive Deployment Model

An adaptive deployment model is essential to adequately address the contexts for resources access requests. Threshold assigned by credentialing policies limit access by means of context sensitive, dynamic extension. Besides, the process of determination of something (user, device, application, process, etc.) being trustworthy in this trust-centric shift is so difficult problem to begin countering with. Moreover, traditionally all the data and transactions are assumed to be trusted whereas device compromises, data breaches, and malicious activities contribute to degrade that trust. However, Zero-Trust strategy begins with an assumption that all the data and transactions are required to be deemed as untrusted from the inception. With this, a new problem gets countered as how to gain sufficient trust? Furthermore, based on the organizational requirements and key focuses, trust is bound to alter. Therefore, to manage the trustworthiness of all transactions in an organization, Zero-Trust environment involves integration of control for data, users, devices, and applications (Mehraj & Banday, 2020)



[Figure/Image from source paragraph 710]

Figure 3.7: Adaptive Weighted Trust Model

## Conceptual Framework for Context Adaptive Trust Estimation Model on SDP

The proposed model generates a trust level for different correspondent nodes across different networks as illustrated in Figure 2.7: Conceptual Framework. The corresponding node initiates requests for resources through the control plane (1). The requests are received and processed by the SDP controllers which enforce the instructions set as well as the security policies before the bearer channel is allocated between the correspondent node and the SDP gateway for access to data. Before the bearer channel is established the SDP controller enforces the five facets of zero trust; the result of the enforcement is then passed through a weighting model to determine the level of trust for the correspondent node (2,3). If the level of trust based on the zero trust facets meets the acceptable threshold, the controller informs the gateway to create a bearer channel with the necessary QOS requirements with rge correspondent node (4). The feedback and how to access the gateway is then passed back to the correspondent node (5). The node can then access the shared network resources through the gateway (6,7,8,9). The corresponding node subsequently has access to interact with the resource based on the established trust and permissions levels (10). Success or failure in the process is used to inform the trust engine of the changes in the environments either by adjusting the ratio of trust weightings for devices, users, data elements or any of the other parameters of consideration(11)



[Figure/Image from source paragraph 716]

Figure 3.8: Proposed Adaptive model for Zero Trust in SDPs
# : Building a Zero Trust Testbed with Virtualized Resources

Building a Resource-Limited Zero Trust Testbed: A Hybrid Virtualization and Emulation Approach Leveraging Software-Defined Perimeters and Networking

## Introduction

Zero trust is more common within modern security discourses with vendors, service providers and researchers focusin on different domains of implementation. Google for example proclaimed benefits of a zero trust approach in commercial infrastructure through its zero trust centric BeyondCorp initiatives (BeyondCorp). Despite all these, a subset of both researchers and practitioners are still contemplating implementation of zero trust testbeds within their local contexts. Despite the broad range of zero trust documentation such as special publication standards  (NIST), a zero trust evaluation and maturity models (ZT Maturity), reference architectures guiding the design and approach in implementation [CSA Guide 2.0 and Implementation Guide], and other guiding texts such as architectures defined by (Garbis and Chapman), zero trust implementation rarely transition to testbeds, emulation environments or production environments. While the theoretical underpinnings are robust, practical implementation and empirical evaluation remain challenging, particularly for resource-constrained entities like academic institutions, small-to-medium enterprises, and independent security researchers (Chandramouli et al., 2022). The prohibitive cost and complexity of deploying physical ZT pilot environments—encompassing Software-Defined Perimeter (SDP) for identity-centric access and Software-Defined Networking (SDN) for granular micro-segmentation—create a significant barrier to entry for hands-on research, development, and training.

This chapter directly confronts this challenge by proposing and validating a novel methodological framework for constructing a high-fidelity, functionally complete ZT testbed under strict hardware limitations. It  posits that a synergistic hybrid architecture leveraging lightweight virtualization for workload isolation, purpose-built emulation for network topology, and containerization for control-plane services can accurately model the dynamic interactions of a production-grade Zero Trust environment at minimal cost. The  testbed is an operational platform capable of running real security software, generating authentic traffic, and demonstrating tangible security outcomes. Its primary contributions are fourfold: (1) providing a reproducible experimental framework for validating ZT policy efficacy and resilience against lateral movement attacks; (2) enabling empirical study of the control-plane interoperability between SDP and SDN systems; (3) serving as a configurable environment for adversarial emulation and defensive validation; and (4) acting as an accessible pedagogical instrument for advanced cybersecurity education.These show that ZT features of of SDPs can be modeled with the flexibility of  software defined network (SDN) to achieve advanced and higher fidelity test cases using combinations of tvirtaulization and emulation tools for granualr dynamic policies and least privilege enforcement.

## Reference Architectures and Models

### Zero Trust Model

The zero trust reference security model pivots from notions of implicit trust and prior to allowing access; all users, devices, network flows, and resource access requests are subjected to verification processes before being trusted in the particular context. Previous works have evaluated embedding of security within organizations generating  common modern enetrprise security lexicon including zero trust intrusion tolerant systems that assume compromise of systems is inevitable and periodically restore themselves from a trusted backups [7]. Moreover, while most  conversations focuse on ZTA, there is need to review other areas such as zero trust software engineering and zero trust protocol design. Zero Trust by Design (ZTBD) was introduced to harmonize disparate zero trust guidance by distilling it down to fundamental principles to guide zero trust research and practice [9]. The ZTBD principles were further augmented with a set of good practices as well as zero trust patterns for reusable solutions to common challenges in a zero trust context.. These have further evolved to anchor zero trust security models and the underlying architecture.

The zero trust architecture is based on rethinking of the network architecture to abandon the perimeter centric view of a trusted internal network in favor of a zero trust model more formally described in NIST Special Publication (SP) 800-207 (NIST). Figure 5.1 provides a generic reference to the main components of a ZTA as defined by NIST with a clear delineation between the control and the data planes. The eventual goal is to validate a dynamic and contxt aware trust algorithm in the high fidelity ZT testbed for resource access requests. While the trust model will focus on the data, application, device, network and user facets  of zero trust, the testbed will focus on the core tenets of Zero trust migration by NIST.

The testbed design is a direct instantiation of the seven core tenets outlined in NIST SP 800-207. Crucially, it enforces Tenet 1 ("All data sources and computing services are considered resources") by treating every workload—client, server, or controller—as an explicitly secured entity. Tenet 3 ("Access to individual enterprise resources is granted on a per-session basis") is implemented through the dynamic, session-specific rules established by the SDP and SDN controllers. The principle of least-privilege access (Tenet 5) is operationalized at two levels: the SDP governs initial resource admission, while SDN enforces restrictive east-west policies within the trusted zone, a dual-layer approach increasingly recommended for defense-in-depth (Barach 2025). Recent analyses by the Cloud Security Alliance (CSA, 2023) emphasize that such layered controls are essential for mitigating insider threats and advanced persistent threats (APTs) that bypass initial authentication.

Even with NIST SP 800-207, many other zero trust publications, and numerous vendors implementations of zero trust products and services, there is a lack of consensus and misunderstandings still exist. The goal is therefore to design, build and create zero trust testbeds with limited computing resources and related enablers based on virtualization and emulation tools to supplement the growing body of knowledge to benefit zero trust research and practice.



[Figure/Image from source paragraph 1048]

### Software Defined Perimeters (SDP)

Software Defined Perimeters (SDP) flexibly provide an overlay network with dynamic trust provisioning and secure access, supporting protection of applications and services being accessed over an untrusted network. With SDP, resources are hidden from unauthorized parties until identity-centric trust has been established. This shift from a legacy mindset of static, perimeter focused security with trusted “internal” networks to a dynamically adaptive logical micro-perimeter requiring trust establishment aligns well with the zero trust security model and the principles of Zero Trust by Design (ZTBD).

The SDP architecture, standardized by the Cloud Security Alliance (CSA SDP Specification v2.0, 2023), provides the "black cloud" security model where resources are invisible to unauthorized entities. This implementation abstracts a production SDP into three essential components, aligning with the IETF's emerging work on secure service access (Cam-Winget eat al 2023). The SDP Controller performs cryptographic identity verification, leveraging short-lived certificates or token-based authentication (e.g., SPIFFE/SPIRE concepts) as discussed in recent cloud-native identity literature (cardoso 2025). The SDP Initiator establishes a mutually authenticated TLS/DTLS tunnel, ensuring confidentiality and integrity from the client edge. The SDP Gateway functions as a policy enforcement point (PEP), terminating authorized tunnels and forwarding traffic only to sanctioned backend services. This decoupled model allows the testbed to explore novel authentication integrations and failover scenarios relevant to modern hybrid work environments (Fernando & Noureddine, 2024). The specification also allows for utilization of  the Single Packet Authorization (SPA) pattern from ZTBD as a foundational enabler to resource abstraction and redirection of data plane instructions to the gateways.

Fig. 3 shows key components of a notional SDP architecture annotated with corresponding mappings to the key concepts of a ZTA as defined by SDP specification and NIST respectively. The SDP Controller logically resides in the control plane, authenticating entities and authorizing access flows. In this way, the SDP Controller acts as the Policy Decision Point (PDP) in the ZTA framework. The SDP IH1 and IH2 components represent Initiating Hosts, which are user devices or other entities that initiate connections in an SDP enabled environment. The Accepting Host (AH) entities are logical components that guard hidden services, allowing or disallowing access flows much like the Policy Enforcement Point (PEP) of the ZTA framework. The AH can reside with the target resource as depicted with AH1 or it can serve as a physically separate SDP Gateway as depicted with AH2.

The SDP v2.0 specification describes deployment models, outlines onboarding and access workflows, and delineates protocol details such as SPA, mutual TLS authentication between components, and device validation. It also describes the workflows including Joining and leaving a domain area, peering and sequences of exchanges for request decisions as discussed in subsequent sections (operationalization of SDP). Consequently, the reference implementation of SDP based on Opensdp  is a good fit to serve as the cornerstone for building a zero trust testbed with limited resources.



[Figure/Image from source paragraph 1057]

### Software Defined Networking (SDN)

SDNs are important enablers of micro-segmentation, a critical ZT requirement that is rarely achieved ir implemented in traditional networks. This testbed incorporates SDN as the dynamic data-plane orchestrator. The SDN Controller (deployed as Ryu) provides a programmatic northbound interface (NBI) for the policy orchestrator, translating high-level intents ("allow App_User_1 to access Web_Server_2 on port 443") into low-level OpenFlow rules. Openflow is an open interface and protocol enabling access to the forwarding plane of networking equipment previously perceived as inflexible. It is a key enabler of Software Defined Networking (SDN)  which guides the operations of data exchange between components particularly across data and control planes. The SDN OpenFlow protocol, is standardized can manage multiple OpenFlow forwarding devices hence becoming an enabler of ZT enforcing SDPs. Open vSwitch (OVS) serves as the programmable data-plane element within the emulated topology. Recent research demonstrates that OVS, when configured with conntrack-enabled flows, can enforce stateful micro-segmentation policies at near line-rate in virtualized environments, making it an ideal candidate for our testbed's data plane (Mujib and Sari., 2020). This SDN layer is responsible for implementing the "default-deny" posture within the protected zone, a capability highlighted as essential for containing ransomware propagation in recent cybersecurity frameworks (Shaji, 2024).

With SDNs, the control plane is implemented in software and separated from the forwarding logic in the data plane. This shows comparable notions of de control and data planes across SDN, SDP, and ZTA, suggesting shared underlying design principles and possible virtualization of mapped components to achieve a dynamic access control policy. This architecture thus affords several virtualization, emulation and optimization opportunities and the flexibility that comes with its programmatic nature. This thus shows how SDN is a key enabler in testing of large, complex network configurations with limited and virtualized computing resources.


*📌 Takeaway: SDP provides enforcement—but not intelligence. It offers the programmable substrate for executing trust-driven access decisions, but requires a mathematical engine to compute those decisions. The next chapter presents that engine.*



---

# PART III: THE PROPOSED DYNAMIC TRUST ARCHITECTURE

# Chapter 6: A Context-Aware Dynamic Trust Model

*Chapters 2–5 established the problem (perimeter collapse), the theory (trust as computation), the critique (ZTA's blind spots), and the enforcement substrate (SDP). What remains is the core intellectual contribution: a mathematical engine that fuses multi-domain evidence, decays trust temporally, and produces actionable access decisions. This chapter presents that engine—the Context-Aware Dynamic Trust Model.*

## Dynamic Access Control Model in Heterogeneous Networks

Modeling trust in heterogeneous enterprise networks requires considering the interplay between various contextual dimensions such as data, devices, applications, users and network conditions. Trust trust evaluation relies on these multiple contexts dervived from network metadata to guide decisions for access control.  In this work, the modelconsider the four of the previously highlighted five contexts by incoprprating the user context into the others. This particlualrly becayuse user context is mainly a derivation of the user innteraction with the other contexts of Data , application, devices, and network. Heterogeneous enterprise networks have many data elements representing these contexts collected from network assessment metrics or metadata in implementation and operationalization of these networks. As such the proposed model in this work  gtruncates theese data elements and focuses on 3 metrics per context before subjecting them to a weighted sum of  of their values per context and further for all contexts. The eightings within a context and across all contexts will be varied to represent different scenarios for enterprises as highlighted by equation4.3

Where:

Tovr= Overall trust Score and Tdat, Tdev​, Tapp​, Tnet​ are Trust scores for data, devices, applications, and networks (normalized between 0 and 1).

Wd, Wdev,Wapp, Wnet: are weights for the data device, applicatio and network conntexts. The sum of all weights shoild be 1

TrustRes: this is the residual score for a user based  access transaction history

### Trust Model Components

To define trust in this environment, we need to account for the following:

#### Data Context

This context reviews and scores trust basedon three parameters. These partameters are dynamically weighted to generate an eventaul trust score for the data context as illlutsrated by Equation 4.5

Where Tdat is the eventual trust score for the data context and i is the weight assigned to each of the data metrics

Integrity: This considers the trusstworthiness of the data collected from the network metadata. It reflects the accuracy and consistency of data. Integrity violations, such as tampered financial records, can have severe implications. A considerations of protection against unauthorized alterations  is reviewed e.g. checking hashes or checksums and verifying certificates

Fresheness: refers to the timeliness and recency of data used in decision-making processes. It is a critical parameter for the data context in trust models to maintain relevance and accuracy in trust evaluations, especially in environments where conditions change rapidly, such as in IoT networks, financial systems, or cybersecurity operations. it also allows for real-time decision maaking in dynamic environments and adaptive access control particularly in Zero trust environments. The metric will be reviewed against accepted data freshness thresholds in different contexts

Authenticity: this reviews the reputation and gauges the reliability of the data source. Data from verified sources is more trustworthy than anonymous or unverified sources. Trust models often deprioritize unverified sources to avoid misinformation spread in networks.

#### Device Context

This context reviews and scores trust based on three device parameters. These partameters are dynamically weighted to generate an eventaul trust score for the device context as illlutsrated by Equation 4.5

Where:

Tdev is the trust value for the device context

β1​,β2​,β3​: Weights for device trust factors, such that: β1+β2+β3=1

- Device Identity: This considers device identifies that uniquely denote a device. This is because a strong device identity prevents spoofing attacks. Device authentication is  a critical factor in trust management for heterogeneous networks. MAC addresses and other physical level iden ties provide the most commonly used intifiers. Concatenations of Mac, IP addresses and port numners can be used even more ribust identifioiers

- Reputation Score: This represents the device Health in an heterogeneous environment. It also indicates the security posture of a device, such as  existence as an entry in a blacklist, malware scans, SIEM entries, up-to-date patches and antivirus status. This can also be used to distinguish between enterprise owned devices and personal devices in organizations that have varied degrees of BYOD policies. Additionally, the rising incidents of compromise on IOT devices and SCADA systems indicate the importance of device helath and reputation. Based on DDOS cases like the Mirai botnet attack exploiting outdated and vulnerable IoT devices, highlighting there is need to emphasize continuous monitoring of device health to maintain network trust.

- Complaince Behavior: this Tracks anomalies in device activity. Malicious devices often exhibit behavioral deviations. It also evaluate the device platform, utilities and updates on facets such as firmware, hypervisors and virtualization tools in line with the defined guideline within these eneterprise network environments. Thiis behavior can also be used to identiy anomalies such as sudden spikes in outbound traffic from a single device, network segement or segments which might indicate involvement in a DDoS attack or origination of unmonitored traffic.

#### Application Context

This context evaulautes the trust levels for the applications used within a heterogeneous  enterpise network. It also considers three parameters dynamically weighted based on the organnizational contexts as illustrated in EQUSATION 4.6. These parameter include:

Where Tapp is the trust score in the application domain and   is the weights for each application parameer and the sum of all  ()

Behavior consistencey: This reviews compliance with enterprise security guidelines, types of applications and their operayion within one network segment or across multiple segments.

Vulnerability score:  This parameter considers the whether applications up-to-date and free from known vulnerabilities. It also considesrs the presennce of CVEs involving specific client side and server side applications

Access Compliance: this parameter reviews Permissions required for  routine fucntions and  access operations aprticularly to sensitive directories and files.

#### Network Context

Protocol Score: Trust in the network topology, protocol compliance, and link security.

Anomaly Detection: Trust decreases if packet anomalies, spoofing, or unusual traffic patterns are detected.

Segmentation: Trust is higher in segmented networks that enforce Zero Trust principles.

Node Reputationnscore



[Figure/Image from source paragraph 947]

Fill in the individual metrics(easy way is to define i and j)



[Figure/Image from source paragraph 949]

Decay trust on the overall

### Ensemble of Dynamic sum and Weighted Belief Fusion for Dynamic and Context-Aware Trust Modeling

This combination is suitable in environments where there is need to integrate trust inputs cumulatively but also need to give certain sources more weight based on relevance or reliability.

Cumulative Fusion: Sum the belief, disbelief, and uncertainty values to form a single fused opinion.

Weighted Fusion: Calculate a weighted fusion based on the importance or reliability of each source.

Combine: Merge the results, either by averaging or applying a weighting factor to balance cumulative and weighted results.

Uncertainty- probabilistic event

Deterministic guardrail

3.6 Modeling Trust Decay Over Time

3.6.1 Exponential Evidence Discounting

3.6.2 Practical Implementation: Sliding Windows and Forgetting Factors

/* THIS SECTION IS A REFERENCE GUIDE FORT THE CHAPTER*/

Chapter 4: Dynamic Trust Models for Enterprise networks - Adapting to Change

"The Flow of Trust: Adapting to tides in the Sea of enterprise networks"

“Building the Blueprint”

Network Infrastructure Identities and User Trust Values (2st Paper)

Present dynamic models of trust for heteregenous enterprise networks, emphasizing the need for adaptability in real-time scenarios

Merge the dynamicity of networks and context awareness to show how the two can be merged

Discuss dynamic elements such as reputation systems, trust decay for networks, feedback loops, and continuous assessment of trustworthiness.

Examination of real-world incidents and their impact on network security

Highlight how context-aware trust models use real-time data, including environmental cues (e.g., location, behavior patterns, system interactions) to continuously update trustworthiness.

Compare experiments with dynamic and context awareness and absence

Introduce mathematical and algorithmic approaches, but present them as "mechanisms of change" in a system of trust.

Quantitative and qualitative analysis of identity-based vulnerabilities. Case studies or scenarios illustrating the findings

Discuss real-world applications such as IOT domains, BYOD, Cellular systems, virtualized and cloud  environemnts, collaborative systems, online marketplaces or autonomous vehicles.

Introduce mathematical and algorithmic approaches, but present them as "mechanisms of change" in a system of trust.

/* THIS SECTION IS A REFERENCE GUIDE FORT THE CHAPTER*/

Chapter 5: Building and Testing Context-Aware Trust Architecture - A Dance of weighted Multiple Factors

"Trust in Motion: The Dance of factors of Contexts and Actions"

Trust Derivation and Trust Management Models (3nd Paper)

Assessment of existing trust derivations and trust management models

Assessment of existing trust models for dynamic policy implementation

Comparative analysis of model effectiveness in preventing misuse and intrusions

Create a model for trust derivation and trust management

Case studies or simulations demonstrating model application and outcomes

Discuss the use of weighted belief fusions for trust determination across the zero trust pillars

Dive into practical applications where dynamic and context-aware trust models are essential.

Use case studies such as online peer-to-peer systems, collaborative filtering (like in Netflix or Amazon), autonomous systems (e.g., self-driving cars), and multi-agent systems.


*📌 Takeaway: The mathematical engine is defined. It fuses multi-domain evidence via Dempster-Shafer theory, decays trust temporally, and produces tiered access decisions. But equations on paper require validation. The next chapter describes the testbed.*



---

# PART IV: VALIDATION AND EVIDENCE

# Chapter 7: Testbed Design and Implementation

*Chapter 6 defined the mathematical architecture of the Ensemble Trust Model. Equations and algorithms, however, are insufficient without empirical validation. This chapter describes the virtualized testbed that makes trust computation executable—translating theory into a functioning Zero Trust infrastructure.*

## Design of Zero Trust Testbed Virtualized Resources

### Virtualized Network in a PC: Mininet and GNS3for SDN

Mininet tool facilitates rapid prototyping of large, complex network structures in resource constrained environments such as a typical laptop [14]. It  combines very lightweight virtualization with the versatility and power of SDNs to enable a plethora of complex testing capabilities that would otherwise require significantly more resources. Complex network structures can be created from the Mininet command line interface (CLI) or programmatically via the application programming interface (API). While Mininet clearly has some limitations, it can serve as a key enabler for a myriad of zero trust test cases when researchers or practitioners are resource challenged. The tool is accessible as aprebuilt virtual appliance or can be  compiled natively within a Linux operatinf system. Debian based distributions are preferred, particularly ubuntu on which the virtual appliance is built within as illustrated in Figure 5.2



[Figure/Image from source paragraph 1067]

### Virtualized Network in a PC:GNS3 for Enterprise Network Emulation

GNS3 is a graphical network simulator that runs as a VM, supporting Cisco, Juniper, and other device images. Simulates complex networks with low resource usage when run in a VM; useful for testing zero trust gateways and perimeter defenses in an emulated environment.

In network simulation and emulation, Graphical Network Simulator-3 (GNS3) occupies a unique "hybrid" position. While most tools are simulators re-creating behaviors through code, GNS3 is primarily a full-system hardware emulator that is different from Mininet which is a container-based emulator that shares the host kernel. It therefore serves as a mediation layer between high-level graphical orchestration and low-level virtualization binaries. It follows a decoupled, client-server architecture, which is critical for scalability in resource-limited testbeds. The Controller (gns3-server) is a Python-based RESTful API service that manages the project state, topology JSON files, and snapshots, refer to figure 5.5. It handles the "brain" of the network without touching the data plane. The Compute Engine is where the actual virtualization occurs. It interfaces with three distinct backends: (1) Dynamips: A hardware emulator that allows unmodified Cisco IOS binary images (like the 7200 series) to run on x86. It uses Dynamic Recompilation to translate instructions on the fly. (2) QEMU/KVM: The primary engine for modern vendors (Arista, Palo Alto, Cisco IOSv). It provides full hardware virtualization, emulating NICs, CPUs, and specialized ASICs. (3)Docker: Used for lightweight endpoint emulation (web servers, attackers, DNS), refer to figure 5.4.

A central challenge in using GNS3 for a Zero Trust (ZT) testbed is the CPU/RAM overhead. Because GNS3 emulates the hardware, an idle Cisco router would theoretically consume 100% of a host's CPU core because the emulated CPU is constantly polling for instructions. It utilizes the The Idle-PC Optimization where it identifies the "idle loop" in the guest OS's code and tells the host CPU to "sleep" during those cycles.

Unlike Mininet, where switches share a single kernel, every GNS3 node is a separate process. This introduces significant context switching overhead, making GNS3 less efficient for high-density topologies  exceeding 50 nodes compared to SDN-specific tools.

For a Zero Trust testbed, GNS3’s value lies in its fidelity. ZT requires "Assume Breach" testing, which demands a realistic data plane that supports Encapsulation and  tunnels for secure transport, Stateful Inspection  and Deep Packet Inspection (DPI). Since GNS3 allows for Wireshark integration at any link, researchers can verify if identity tokens (like JWTs) are correctly encrypted and validated at each Policy Enforcement Point (PEP).



[Figure/Image from source paragraph 1076]



[Figure/Image from source paragraph 1078]

### Testbed in a Box

The design philosophy is governed by a constraint-first approach, maximizing functional fidelity while minimizing resource consumption. This is critical, as recent surveys indicate that over 60% of cybersecurity labs in academic settings operate under severe hardware budget constraints (Otuom et al., 2025). This therefore needs hybrid strategy focusing on high fidelity and low resource consumption resulting in three key decisions:

Lightweight Virtualization: This focuses on the use of Linux  containers and daemons (LXC/LXD) system containers over full virtual machines (VMs) for the majority of workload nodes. These provide a near-native performance and minimal overhead by sharing the host kernel while maintaining isolated user spaces, filesystems, and networking. For nodes requiring a distinct kernel or specific OS features such as a legacy application server, QEMU/KVM and OS native hypervisors are utilized. This tiered approach optimizes the trade-off between isolation overhead and host resource utilization, a balancing act detailed in contemporary container vs. VM performance analyses (Silva et al., 2023).

Network Emulation:  Mininet is used as a the network fabric emulator. Unlike packet-level simulators, Mininet creates real kernel network namespaces interconnected by virtual switches (OVS), allowing unmodified application binaries and network stacks to run. This provides unparalleled fidelity for testing stateful protocols and security appliances that often fail in purely simulated environments (Lantz 2025). Mininet's Python API enables the programmatic creation of complex, multi-domain topologies on a single host, a feature exploited to model internet, DMZ, and internal zones.

Infrastructure-as-Code for Reproducibility: The entire testbed lifecycle—from topology creation and software installation to policy configuration—is codified using playbooks and bash and Python scripts. This aligns with modern DevOps and research reproducibility best practices (Prates and, 2023). It ensures that experiments are repeatable, facilitates rapid scenario switching (e.g., from a campus network to a cloud architecture), and allows the testbed to be easily shared and extended by the research community.

## A Zero Trust Testbed Design

The network layout of Fig. 4 represents a sample topology for a zero trust testbed with limited resources. The topology includes eight standard hosts connected to several OpenFlow and legacy switches/routers, an SDP Controller, an SDP Gateway, and two SDP Accepting Hosts for access to hidden services. The topology shows how network topologies can be programmatically defined and can be further refined by modifying Python code, or via the Miniedit tool if a graphical user interface is preferred by the network designer for the testbed.



[Figure/Image from source paragraph 1090]

### Testbed Tools and Components

Table 1 lists core software components that can be utilized for development of a  zero trust testbed for limited computing resource environments along with a description of purpose, roles and relevance for each. The lightweight SDN virtualization of Mininet coupled with the resource hiding and authenticate-authorize before access allows for better testing before deployment. The verify before access model enforced by SDP’s SPA, based on a flexible open source models, makes the  process suitable for establishing a zero trust testbed for research and testing. Although Figure 5.3 indicates the easierst and quickest way of using mininet as importing the available Mininet VM Image releases as a starting point, using a native Mininet installation is recommended for maximum flexibility in customizing the testbed environment.

The recommended processors for the resource-limited zero trust testbed are relatively modern architectures for virtualization support, sufficient instructions per second (IPS) single core performance, and core/thread counts for adequate parallel processing. This includes the last couples of generations of Intel, AMD, and ARM processors and chips available on most end devices.

Limitations such as the complexity of properly securing the Mininet environment [16] and lesser isolation offered due to the lightweight virtualization approach are important comsiderations for the testbed. Consequently, a logical next step would be to transition from the lightweight virtualization of Mininet to heavier weight or full virtualization of a Type 1 (bare metal) or Type 2 (host-based) hypervisor environment.  While this increases resource requirements, the use of open source options for virtualization such as QEMU, the Linux Kernel-based Virtual Machine (KVM), or other modern hypervisors can still facilitate an effective testbed assuming adequate hardware.

### Reference Zero Trust Architecture Mapped to the Testbed

Zero Trust Architecture (ZTA), as defined by NIST SP 800-207, fundamentally assumption enforces  continuous verification, explicit authorization, and least-privilege access. It is therefore paramount that the testbed aligns to the reference architcture to eensure that all the tenets are adhered to. This mapping has been illustrated in Table 5.3

This testbed architecture deliberately decouples trust from network location by enforcing access decisions at multiple layers (L3–L7) using SDN and proxy-based controls. The use of OpenDaylight as a Policy Administrator allows high-level identity- and context-based decisions (from OPA and Keycloak) to be translated into low-level forwarding rules in Open vSwitch. This separation reflects real-world Zero Trust systems where control planes are logically centralized but data planes remain distributed.

A critical research advantage of this architecture is policy transparency. OPA policies are declarative and auditable, making them suitable for formal verification, policy conflict analysis, and reproducible experiments—key requirements at the thesis level. Moreover, Mininet’s emulation model allows precise manipulation of topology, latency, and link failures, enabling controlled evaluation of Zero Trust enforcement under dynamic conditions.

While the architecture lacks hardware-based trust anchors (e.g., TPM, secure enclaves), this limitation is acceptable in a resource-constrained academic setting and does not invalidate research into logical trust enforcement, which is the dominant concern of Zero Trust networking

### Minimal Hardware and Software Installation Profile

Resource constraints force architectural discipline. Rather than undermining research quality, this constraint strengthens experimental rigor by eliminating unnecessary complexity. The proposed minimal profile prioritizes control-plane logic and policy evaluation, which are the core research concerns of Zero Trust, over high-throughput performance testing.

The use of containers instead of full virtual machines reflects modern Zero Trust deployments in cloud-native environments. Containers reduce memory overhead, enable rapid reconfiguration, and support repeatable experimentation as shown in Table 5.4. Importantly, this choice does not compromise architectural fidelity, as Zero Trust principles are largely orthogonal to the virtualization substrate.

From a scalability perspective, the testbed is intentionally functionally scalable but not performance scalable. That is, the number of distinct trust relationships, identities, and policies can grow without proportional increases in hardware requirements. This makes the testbed ideal for studying Policy explosion problems, Latency impact of continuous authorization and Controller bottlenecks under dynamic trust evaluation. The installation profile thus aligns with an experimental approach, where the artifact (testbed) is evaluated for correctness, flexibility, and explanatory power rather than raw throughput.

## Testbed Architecture and Implementation

### Physical Layer

The host system runs a minimal Ubuntu Server 24.04 LTS installation, chosen for its robust support of KVM and LXC ptocesses. It is also the most native platfoem for mininnet installations ans therefore results in the most efficient Mininet deployment scenario. The OS is tuned for virtualization (e.g., intel_iommu=on in kernel parameters) and network performance (CPU governor set to performance). It runs on a core i5 processor with 16GB of RAM and atleast 256gb of storage before OS initialization

### Virtualization & Emulation Layer

The core innovation lies in the integration of distinct virtualization technologies under a unified Mininet and GNS3 managed network. Mininet's standard host class is extended to create CustomHost objects. These objects, when instantiated, can launch either an LXC container or a libvirt-managed KVM VM, attaching its primary network interface to a designated OVS switch port. This creates a seamless blend where the network control is emulated, but the endpoints are real, isolated compute instances. Critical control services like the SDP Controller and SDN Controller are deployed as Docker containers for consistency and ease of version management, connected to a dedicated "management" network segment.

### Control & Data Plane Integration

The integration point is the Policy Orchestrator, a custom script powered service that acts as the "brain" of the ZT enforcement. It subscribes to events from the SDP Controller (e.g., USER_AUTHENTICATED). Upon receiving an event, it consults a local policy store (or could query a external policy decision point) and translates the allowed access into a set of network intents. It then invokes the REST API of the SDN Controller to install specific flow entries such as illustrated of Figure 5.6:



[Figure/Image from source paragraph 1131]

This closed-loop automation realizes the dynamic, identity-aware network segmentation that is the hallmark of mature ZT implementations (Ahmed et al., 2024).

### Network Topology

The implemented multi-zone topology is depicted below, designed to reflect a modern enterprise with internet-facing services and protected internal assets:



[Figure/Image from source paragraph 1136]



[Figure/Image from source paragraph 1138]

This topology explicitly creates security domains, allowing for clear experimentation with inter-zone policies and attack vectors.

## Conclusion

This chapter has presented a comprehensive blueprint and functional proof-of-concept for a resource-efficient Zero Trust testbed. By architecting a hybrid environment that strategically layers LXC containers, KVM VMs, Mininet-emulated networks, and Dockerized control services, it collapsed a traditionally multi-rack ZT pilot infrastructure onto a single commodity laptop. The testbed uniquely and effectively demonstrates the critical interplay between SDP's identity-driven access control and SDN's dynamic micro-segmentation, providing a tangible platform to validate the core promise of Zero Trust: significantly reducing the enterprise attack surface and containing breaches.

The capabilities of SDP support implementation of the core components of ZTA and they facilitate alignment with core principles of ZTBD. Meanwhile, the power of SDN and light-weight virtualization can enable emulations with complex network topologies and large numbers of nodes. SDP and SDN can combine with other tools to create a zero trust testbed with very limited resources, supporting a level of zero trust testing and experimentation in a box that might not otherwise be possible. Enhanced testbeds with additional (but still limited) resources and more zero trust tools can provide other advantages to researchers and practitioners by growing repository of freely available zero trust knowledge and resources.  The implementation proves that rigorous cybersecurity research and education in advanced architectures like Zero Trust need not be gated by hardware access. The testbed's code-driven, reproducible nature makes it a valuable asset for the community.
# TESTBED DESIGN AND SETUP

## Introduction

This chapter presents the detailed implementation of a Zero Trust testbed designed to support empirical evaluation of identity-centric, policy-driven access control in software-defined environments. The work builds a baseline testbed focusing on criteria based access control decisions and score based trust evaluation testbed that build up on the former  The primary objective of the testbeds is to demonstrate the transition from implicit network trust to explicit, continuously evaluated trust enforced across network and application layers. The design follows the NIST SP 800-207 Zero Trust Architecture (ZTA) reference model, explicitly separating Policy Decision Points (PDPs), and  Policy Enforcement Points (PEPs). Further, the testbed clearly demarcates Policy Administration Points (PAPs) and the policy engine’s trust algorithm based on a multidomain and score based multi-criteria (score) trust estimation and calculation. The design prioritizes reproducibility, modularity, and extensibility to support multi-domain trust experiments.

concept → setup → deployment → logic → validation → evaluation.

## TestBed Setup Procedure

The testbed design and setup  was done incrementally to clearly demarcate controller and gateway functions as defined by NIST SP 800-207 and CSA SDP in section X.  The testbed setup procedure was  split into 6 steps that sequentily built on each other to develop an incremental prototype to test the trust algorithm as illustrated in figures 8.1 through to 8.4. The steps are:

- Host preparation: The  goal of this step was selection and preparation of tehe host environment on which tesbed was setup.  This was based on. Stable release of linux with  support for sofare defined networks and sofatware defined perimeters implemntation. The virtualization capabilities were lso rviewed  from the firmware to support near-native virtualization for modern Virtual appliances such as GNS3 and Mininet VM appliances. The support for containerization and docker setup, running, deployment and networking were also consoderd. The choice of Ubuntu 24.04 LTS guarantees longterm support for security and functionality patches while secure firmware settings gurantee reduced surface of attacks especially from lateral escalation and side channels attacks

- Installation: This focused on the installation of the relevant packages and utiliies required for request-response cycles of communication, administration and deployment of containers, and resurvce utiliation monitoring tools. Services and utilities such as curl, network and briding utilities were installed to support host-VM-conteiner interaction. Other tools such as spectacle and Vmstat were used to collect screenshot ansd show resource utilization bnchamarks.

- Virtualization and Container setup: This looks at the container setup for the Ubuntu distribution. The Mininet and GNS installations were natively built on the ubuntu and complemented by a GNS VM virtualized on Vmware Workstation on the local device and Vmware Fusion on a remote host

- Component deployment: the PEP, PDP, PAP were deployed as docker containers as OpenVswitch, Open Policy Agent(OPA), Envoy, and Opendaylight respeevtivey.  These help conserve resources while supporting inetractivity between the hosts within the host environemnt.

- Policy Configuration: This reviews the input, logic and outputs for the PDP and PEP. Rego files were generated for OPA decisions based on simulated data and identity information from keycloak and enforced based on openVswitch flows. Postman was used to buid and originate queries  based on json inputs to derive output based on the logic defined by the rego scripts

- Testcases Description: Due to the infinite variations of number of scenarios that could be tested, test cased were described as an evaluation framework to guide assessment of different contexts. Case variations per testcase were also considered to show changing context and dynamicity of trust evalaution

- Topology and Validation: This stage operates in unison with the previous step because  each test case needed evalaution. Variations of testvases were emulated and estimated based on simulated data for varying cases withineach testcase  for dynamicity of contexts. These have further been covered based on the markdown file defined on the git repository as shown in figure 8.5



[Figure/Image from source paragraph 1164]



[Figure/Image from source paragraph 1166]



[Figure/Image from source paragraph 1168]

## Topology and Validation Logic Flows

The logic flows for the topologies are based on basic principles of zero trusts such as least privilege, continuous authentication and authorization as separate processes and assessment of all communciations and resources within heterogeneous networks. The logical flows  have been mapped to fundamental principles of zero trust architecture as discussed in section 3.4. Additionally, NIST priciples for zero trust enforcement have been revewed and considered for the validation topologies. They include:

## TestCase Description

This describes the experiments setup to evaluate incremental policies for zero trust enforcement in heterogeneous enterprise environements. The policies are sequentiaally incremental and consider improvements from a single domain criteria based trust decision to dynamic, multi-domain and contextual score based trst decisions with tempral decay to ensure the history of transactions is consdered albeit with waning effect as time elapses.

### Baseline

No policy, All services and containers can accees and reach each other. This considers the testbed setup before any policies are defined and flows monitored and evaluated

### TestCase 1: Single Domain Criteria based Evaluation

This tescase acts as the  fist layer or access decision evaluation. It restricts access based on  one domain criteria such as an allowed or blacklisted user,  allowed or blocked services and   trusted or untrusted devices

### TestCase 2: Multidomain Evaluation

This testcase addresses scenarios where users have Enterprise Owned Devices and controlled apps(Uknowned user;device known; apps mostly trusted) or user owned devices with applications that have nt been fingerprinted. It considers permutations across multiple domains based on clear deny-first semantics and easy to extend by adding risk scores, time-based rules and dynamic trust calculations. It can also be tested and measured against frameworks such as MITRE ATT&CK conditions for enetrrprise envriroments. Access decisions include clear grant/reject status with detailed reasons for decisions, especially the decision calculation. The flexibilty of policies is also considered as trusted devices can connect from anywhere; Untrusted devices restricted to local network; Admins can access blocked applications. The tescase policy therefore follows the principle of least privilege and provides clear audit trails for access decisions making the deterministic and auditable.

### Testcase 3: Multi-domain with Static trust scores and contextual weights for domains

This testcase extends dynamic policies from labels to numeric trust scores. The motivation is to transition to values that can represent trust as a continuum. Binary trust labels (trusted / untrusted) are overly simplistic for heterogeneous networks enforcing Zero Trust architectures. Modern Zero Trust architectures treat trust as continuous and dynamic, influenced by posture, behavior, and context. This testcase thus considers trust score inputs based contexts of the domains defined in testcase 2 and weights based on the importance of each domain per scenario. These include: User trust scores based on identity assurance, roles and transaction history; Device trust score such as  Trusted (Enterprise owned compared to BYOD),patch levels, EDR-compliance and Application risk score  based on Allowed services, criticality and  exposure. This implementation aligns with continuous trust evaluation, a core principle of Zero Trust (NIST SP 800-207). By replacing static labels with weighted trust aggregation, authorization becomes adaptive rather than declarative.The weighted sum model enables dynamicity and policy tunability and continuous analysis of  trust score changes during experimentation. Additionally, it provides a bridge between rule-based and probabilistic authorization. This design is especially suitable for research testbeds, where trust weighting can be empirically optimized using traffic logs or attack simulations.

### Testcase 4: Proposed Contextual Trust Weighting for Enterprise relevant Zero trust Facets Data(),Device(), Application/Service(), Network()

This testcase considers facets of zero trust selected in section (4.8) that are most relevant in heterogeneous enterprise networks. The testcase is a direct extension of testcase 2and 3 based on the propositions of this work. It considers dynamic weighting of four facets each considering 3 parameters for trust determination. These include the data facet, focusing on the resource being acessed, the device and application facets which evaluate the device posture and application footprint respectively as well as the network facet which considers the network on which an access request originates and whether its trusted or not. This test enforces hierarchical multidomain integration and evaluation where blacklisted users are immediately rejected while verified users with some level of access are evaluated based on the originating network, the device posture, the application requesting access. Multidomain-Domain Integration permutations include: data domain (valid/invalid); Application domain (Allowed/Blocked); Network domain (Remote/Local) ; Device domain (Trusted/Untrusted). The trust score is based in dynamic weighting of the four facets  and the score is further fuswd based on weighted belief fusion. Metadata availability is used to determine belief and disbelief as probabilistic values while uncertaity is modeled based on absence of metadata. The base value is set at 0.4 to esnure that the default decision in the absence of metadata defaults to denial of access based on the threhold matrix shown in table 8.1. Identicle to testcase 2, Access decisions include clear grant/reject status with detailed reasons for decisions, especially the decision calculation. The flexibilty of policies is also considered as trusted devices can connect from anywhere; Untrusted devices restricted to local network; Admins can access blocked applications. The tescase policy therefore follows the principle of least privilege and provides clear audit trails for access decisions making the deterministic and auditable.

### Testcase 5: Trust weighting with temporal decay

This testcase is an extention of testcase 5 and  performs contextual weighting of the four facets and continuously decays trust across time. This introduces both short term and long term memory. The metadata is evaluated against a time session of 30min whichinfluences the short term weight while historical data like last untrusted transactions are reviewed after 48 hours. This was determined based on the best practices shown in table 8.3. A summary of all the testcase is presented in Table 8.1

## Host System Preparation

The testbed is meant to support Zero Trust research and as such demands a deterministic environment free from uncontrolled variables. Ubuntu 24.04 LTS  thus provides Long-Term Support (LTS) stability for the testbed  due to guaranteed security patches and maintenance. The host system was prepared by minimizing unnecessary services that could introduce attack vectors or measurement noise. The minimal installation also reduces side-channel possibilities and ensures Reproducibility and peer validation of results. The host operating system constitutes the trusted computing base (TCB) of the entire experimental platform. Any instability or misconfiguration at this layer undermines higher-level security guarantees. Ubuntu LTS minimizes kernel churn and driver regressions, ensuring consistent Open vSwitch and Docker behavior across experiments.This allows for meaningful comparison with related Zero Trust testbeds reported in the literature.

### Implementation Details

It was provisioned using Ubuntu 24.04 LTS, selected for its long-term stability, kernel maturity, and compatibility with SDN and container orchestration frameworks for hybrid physical-virtual topologies. This ensures temporal consistency thriugh kernel and library stability across multi-year research cycles.The installation setup using a standard user account and not the default root user. This allowed for separation of privilege principle on the hst environemnt. The installation and user details are illustrated in Figure X based on Table X system specifications. The idle resource consumption before adding components was also measured  and observed to have a baeline memory and processor utilization as shown in Figure X.



[Figure/Image from source paragraph 1197]



[Figure/Image from source paragraph 1199]

### System Specifications:

### Utilities and Libraries Installation

This was done to provision the Linux environment into a machine capable of network manipulation, API interaction, and version control. This is because a fresh Ubuntu server is blind to the requirements of SDN emulation. It does not know how to bridge virtual adapters, it does not know how to pull code from GitHub, and it does not have the tools to easily view routing tables in the format most emulation software expects. By executing this, the necessary foundation is laid before installing core virtualization, networking, PEP, PAP and PDP providers like Docker, OVS, and Mininet. Curl, bridge-utils, git and net-tools were installed  for network and bridge functions, versioning and quering and sending data to specific container URLs. This is ilustrated in figure X



[Figure/Image from source paragraph 1205]

## Container and Virtualization Runtime: Docker and Docker Compose

Containerization was adopted to ensure isolation, repeatability, and rapid reconfiguration of testbed components. Containers provide process-level isolation without full virtualization overhead, enabling high-density experimental topologies. Additionally, containerization Eliminates configuration drift, controls fault injection and supports reusability of code and configurations in experimentation. It also mirror enterprise deployments that use containerized microservices. Docker (version 28.2.2, build 28.2.2-0ubuntu1~24.04.1) was installed to the zero trust testbed. Docker enables each Zero Trust component to operate as an independently versioned trust domain, aligning with modern cloud-native security architectures.

This process was considered to provide a more secure and trusted computing base since containers default capabilites adopta a least privilege approach with little to no container escape possibilities despite the evolving threats targeting docker and other container hypervisors. While most containers can be ephemeral in nature, these containers were set-up and run as background daemons to esnure that the states are easily managed and the hosts can easily communicate with each other. This made the  testbed more suitable for the multinode research and representation required for testing of the custom dynamic and context aware trust algorithm For each docker instance, the default user account was defined as the dedicated docker user. These setup and verification processes are illustrated in figures X and Y



[Figure/Image from source paragraph 1210]



[Figure/Image from source paragraph 1211]

## Open vSwitch: Network-Layer Policy Enforcement Point

Open vSwitch (OVS) was deployed as the network-layer PEP, enabling fine-grained flow-based enforcement. OVS replaces static perimeter devices with programmable microsegmentation, a foundational Zero Trust principle. By delegating forwarding decisions to a centralized SDN controller, the network becomes policy-driven rather than topology-driven. It evaluates decisions at the network layer through Flow Tables to Match-action rules derived from higher-level policies and Statistics Collection through Per-flow counters for behavioral analysis. It allows for protocol independence by decoupling from specific L2/L3/L4 protocol implementations. OVS allows precise measurement of Flow installation latency, Enforcement granularity and Lateral movement containment. This is critical in assessing the less evaluated lateral escalation by attackers focusing on aggregation and inference data attacks (D'Silva, 2023). OVS version 3.34 (ovs_version: "3.3.4")  was installe to provide acces to openflow version 1.3 for more granular flow matches at layer 2/3 as shown in figure X



[Figure/Image from source paragraph 1216]

## Mininet: Network Emulation Layer

Mininet was used to emulate a controlled network topology using lightweight Linux namespaces.



[Figure/Image from source paragraph 1220]

Mininet provides deterministic and repeatable network conditions, which are critical for controlled security experiments. Unlike pure simulation, Mininet executes real protocol stacks, striking a balance between realism and experimental control. This makes Mininet particularly suitable for evaluating Zero Trust enforcement effectiveness without introducing unnecessary environmental noise. Mininet also allows us to map individual services, clients and/or users into indivdual hosts such that their bahvior follows that of hosts communicating within the environment. With Karaf (opendaylight) acting as the policy administrtor, opebflow rules can be applied such that openvswitch grants or dnies access toservice and/or client. Mininet allows for automation of the toplogy basedon python scripts which align and syncronize with he docker community engine, its composer and the defiition of custompolicies on Envoy and OpenPolicyAgent. The installation and version is shown in FIGURE 8.5 and an example script is shown in figure 8.6



[Figure/Image from source paragraph 1222]



[Figure/Image from source paragraph 1223]

## OpenDaylight: Policy Administration Point

OpenDaylight (ODL) was deployed as the SDN controller responsible for translating trust decisions into OpenFlow rules. The version setup is 21.2 and is provided as package named karaf that allows for a web API through port 8181, ssh access through port 8101 and openflow access through ports 6653 and 6633 for versions 1 and 1.3 respectively. The testbed works on verion 1.3 which is stable and supports multiflow tables, metering and possible controller failovers. While opendaylight is primarily a PDP, it is used to enforce custom rules based on L2/L3/L4 or L7 conditions and thresholds. It therefore  acts as the Policy Administration Point (PAP) in the Zero Trust architecture. Its role is not to decide trust, but to operationalize trust decisions produced elsewhere. This separation ensures architectural clarity and prevents policy logic from being embedded in the network layer. This decoupling allows independent evaluation of decision quality versus enforcement efficiency. Opendaylight REST API features as well as network flows for openflow protocol and AAA services were also installed to support network flow rules. The container deployment,  configurations, features installed and the available features list are illustrated in Figures 8.7 through to 8.10



[Figure/Image from source paragraph 1227]



[Figure/Image from source paragraph 1228]



[Figure/Image from source paragraph 1229]



[Figure/Image from source paragraph 1230]

## Keycloak: Identity and Device Trust Anchor

Implementation Details

Keycloak was deployed to provide identity, authentication, and device trust attributes. Identities are the primary trust primitive in trust estimation in Zero Trust architectures. Consequently, Keycloak provides a standards-based identify proofing based on OAuth2/OIDC. It also provides a Fine-grained role and claim issuance with extensibility for device posture signals and values. From a research perspective, Keycloak enables attribute-based trust propagation, allowing identity claims to influence network and application-layer decisions. This is essential for evaluating identity-centric security models against legacy perimeter-based designs. The configurations were performed as follows as shown in figure 8.10:



[Figure/Image from source paragraph 1236]

Zero Trust architectures place identity at the center of access control. Keycloak provides cryptographically verifiable claims that propagate trust context across layers. In this testbed, identity and device posture serve as primary trust signals for downstream policy evaluation. This approach reflects contemporary enterprise practice and enables attribute-based access control (ABAC) experimentation.



[Figure/Image from source paragraph 1239]



[Figure/Image from source paragraph 1241]

## Open Policy Agent: Policy Decision Point

OpenPolicyAgent was deployed as the the PDP where polcies are defined based on what is allowed within the network environemnt. OPA enables policy-as-code, transforming trust logic into a formally analyzable artifact. This makes access control auditable, version-controlled and testable. These are defined as rego files where thetrust algorithm is defined as code logic to guide access control decisions. Rego policies function as executable security hypotheses, allowing empirical validation of Zero Trust assumptions. Integrating OPA with service-level proxies enforces policy outside the application resulting in reduced attack surface, improved policy consistency and centralized auditability. This approach supports Zero Trust microsegmentation, where each service request is independently authorized, even within the same network zone. The proxy-OPA pattern enables repeatable experiments on authorization latency, scalability, and failure modes.

### Implementation Details

OPA was deployed as the centralized PDP for identity claims, data descriptio, device posture, application sensitivity, network context. The container was deployed as an OPA container running on port 8182. While the default port is 8181, this conflicts with the default REST port for the ODL container. The setup was deployed such that all addresses with the port number establsh a socket that connects to the service. This was an operational decision for easier interworking withother containers dspite the resutingsecurity risks (0.0.0.0:8182). The version of OPA is(opa:1.12.2-istio-1). Custom policies  as Rego and Json files were used to define the logic and represent input data simulating contextual heterogeneous network metadata. The policies were incrementally  built from single criteria policies (user type, auth-type,application protocol) to Multi-criteria polcies based on the four facets considered and subsequently improved to contextual, multi-domain weighted and fused trust policies as per the testcases defined.



[Figure/Image from source paragraph 1247]



[Figure/Image from source paragraph 1249]



[Figure/Image from source paragraph 1250]



[Figure/Image from source paragraph 1251]



[Figure/Image from source paragraph 1252]

## Envoy Proxy: Application-Layer PEP

Envoy was deployed as the application level PEP and integrates OAuth2 authentication via Keycloak and Authorization checks via OPA. Network-layer controls alone cannot prevent application-level misuse. Envoy enforces per-request authorization, ensuring that every API call is explicitly validated against policy. This closes the gap between network microsegmentation and application security, a critical requirement for Zero Trust completeness. This transformation elevates the policy from RBAC-inspired rules to full ABAC, enabling Fine-grained decisions, Context awareness and Policy scalability. ABAC is particularly suited for Zero Trust because it avoids role explosion and supports dynamic attributes, such as behavioral trust scores and real-time risk signals. It also enables comparative analysis against RBAC and capability-based models, offering measurable advantages in expressiveness and security posture.

### Implementation Details

Envoy was deployed to enforce authorization at Layer 7. Envoy implements the Application PEP through epresents a modular, ordered processing pipeline through which network traffic is evaluated, transformed, and either forwarded or rejected. This is realized through layered network and HTTP filters, each responsible for a discrete concern such as authentication, authorization, rate limiting, or telemetry. This architecture aligns with the principle of progressive trust evaluation, where no single component is implicitly trusted and every request is continuously inspected as it traverses the data plane.  It also provides a lightweight, sandboxed execution environment that allows custom logic to run safely inside the data plane resulting in dynamic policy execution without recompiling or redeploying the proxy. The proxy level metrics and logs also provide additional observability and feedback for policy tweaks od deployment enhancements.



[Figure/Image from source paragraph 1259]



[Figure/Image from source paragraph 1261]


*📌 Takeaway: Virtualization makes trust executable. The testbed provides a reproducible, cost-effective platform for validating trust computation. The next chapter integrates the trust engine with SDP enforcement.*


# Chapter 8: Trust-Driven Zero Trust Enforcement via SDP

*Chapter 7 constructed the virtualized testbed infrastructure. This chapter demonstrates how the trust computation engine integrates with the SDP enforcement layer, mapping Dempster-Shafer fusion outputs to concrete access decisions through Open Policy Agent policies and Envoy proxy enforcement.*

## Mininet Zero Trust Topology Construction

The minimal topology reduces confounding variables while still capturing essential Zero Trust dynamics. This design choice supports controlled experimentation, enabling clear attribution of observed effects to policy enforcement rather than network complexity.

### Implementation Details

A minimal topology was constructed based on 2 hosts (Service-A and Service-B) and later extnded tobased on 6 hosts and a Single OVS switch (controlled by OpenDaylight). The hosts are ODL_Client-A, ODL_Client-B, Trusted-Device, Untrsted-device, Service-A and Service-B



[Figure/Image from source paragraph 1266]



[Figure/Image from source paragraph 1267]



[Figure/Image from source paragraph 1269]



[Figure/Image from source paragraph 1270]



[Figure/Image from source paragraph 1271]

Before policy enforcement: all services could ing each other and access the switch. Testing accessibility using curl on postman also returned a 200-OK. This indicated that both services, represented as hosts on mininet could access the infrastructure. On enforcement a single criteria policy based on allowed services(Service-A) and blocked services (service-B), the result was:

After policy enforcement:Service-A → Allowed and Service-B → Denied



[Figure/Image from source paragraph 1276]



[Figure/Image from source paragraph 1277]



[Figure/Image from source paragraph 1279]



[Figure/Image from source paragraph 1280]



[Figure/Image from source paragraph 1281]

This validation confirms the elimination of implicit trust. The observed behavior demonstrates that access decisions are now policy-driven, identity-aware, and context-sensitive, satisfying the fundamental goals of Zero Trust. This baseline establishes a reference point for subsequent testcases, where dynamic, multi-domain trust extensions are introduced and evaluated as illustrated in Figure 8.7



[Figure/Image from source paragraph 1283]

This chapter detailed the implementation of a reproducible Zero Trust baseline testbed, integrating identity, policy, network, and application enforcement layers. The modular architecture ensures experimental rigor and provides a foundation for advanced trust modeling and adversarial evaluation presented in subsequent chapters.

This experiment operationalizes  core Zero Trust axioms that the network position is irrelevant. This is because both services reside on the same virtual network, yet access outcomes differ based solely on identity and policy. This directly challenges the legacy “trusted internal network” model and provides measurable evidence of Zero Trust enforcement. The experiment is particularly valuable for causal analysis and by holding topology constant and varying identity claims or policy rules, the effect of trust decisions on connectivity can be isolated. This enables quantitative metrics such as Policy decision latency, Flow rule installation time and the Impact of policy complexity on authorization delay

Further, the scenario demonstrates defense-in-depth within Zero Trust such that even with permissive SDN flow rules, Envoy’s L7 enforcement can still deny access, illustrating layered trust enforcement. This duality reflects real enterprise Zero Trust deployments and strengthens the ecological validity of the testbed.  Limitations such as lack of encrypted hardware identity or real user behavior—are explicitly bounded and can be addressed as future work, reinforcing the academic credibility of the study.


*📌 Takeaway: The trust engine drives SDP enforcement through continuous re-evaluation across six canonical scenarios. The testbed is reusable for different organisational contexts. The next chapter presents the empirical results.*



---

# Chapter 9: Results, Analysis, and Interpretation

*Chapters 7–8 described the testbed and its integration with the Dynamic Trust engine. This chapter presents the experimental results across six canonical enterprise scenarios, evaluating four progressive trust models: (1) Spatial Fusion (Base DS), (2) Linear Temporal Decay, (3) Exponential Temporal Decay, and (4) the full Ensemble Trust Model.*

# EVALUATION RESULTS AND DISCUSSIONS

## Introduction

The fundamental premise of Zero Trust Architecture (ZTA) is the elimination of implicit trust. Traditional access control models have historically relied on static, perimeter-based defenses where authentication is a discrete event granting durable access. However, in modern heterogeneous environment, characterized by remote work, Bring Your Own Device (BYOD) policies, and ephemeral cloud infrastructures, the context of a user and their device is highly volatile. A device authenticated as secure at one moment may be compromised minutes later.

This chapter presents a comprehensive evaluation of computational trust models, beginning from baseline No-Policy settings to legacy static paradigms and finally to advanced dynamic trust estimation and fusion architectures. The work analyzes the theoretical and operational implications of six distinct access models: Implicit Trust (No Policy), Single-Domain Criteria Trust, Multidomain Score-Based Trust (Base DS Model), and three advanced Multidomain variations incorporating temporal dynamics (Linear Time, Exponential Time, and Ensemble Inertia). The advanced multidomain models are simulated and tested across six scenarios defined in Table X toemulatecommon access scenarios in heterogeneous enterprise networks. The evaluation explores the structural tension between absolute security verification and operational usability, culminating in a stateful behavioral engine that continuously evaluates risk.

## Evaluation Framework

This sets out a set of reference tables and matrices based on industry practice, best practice or rules of thumb for heterogeneous enterprise environments.

Table 8.4 shows  the base score mapping matrix that determines trust scores for different contexts within enterprise environments. The base scores are Configuration Parameters (Inputs), not Calculations (Outputs) set by the System Designer (or Administrator) to model a specific environment. They  range from very high trust levels (0.9-1.0) as the highest level to untrusted environemnts(less that 0.5) as the lowest tier. The lowest tier primarily indicates that ignorance(lack of metadata or uncertainty) exceeds the leve of information required to make decision. This forms the basis for assigning trust values to different scenarios

Trust Score (Base Score) Legend

A clear distiction between very high and high trust (Gold vs. Silver levels) such as Distinction  between 0.95  and  0.90 scores comes from minute differences reflected ub Assurance Levels (NIST 800-63B). Very High trust represents contexts with highly restricted, strictly managed assets  with requirements such as enterprise owned device with hardware level authentication (Device Certificate + Biometric + Geolocation + No Vulnerabilities and privileged user access). High trust (silver level) represents standard corprte access with requirements such as a healthy device posture with mFA(Password + MFA + Healthy Device and a verified regular user). The silver levels haveslightly lower trust levels becaise most resources access requests are less "hardware-bound" than device-tunnel sessions, slightly increasing risk surface such as through session cookie theft.

The rationale for the matrix is alignment with CVSS matrix and Nist confidence levels cybersecurity frameworks to ensure interoperability. The CVSS matrix allows the model to ingest vulnerability data directly into the App/Device domain scores while NIST defines that access is granted not just on "Identity" but on the "Confidence" in that identity's current state.Variance-based Weighting directly implements a "measure of the distinctiveness and freshness" of the data such that high Variance results in Low Confidence (weights). Table 8.5 shows the reference matrix for signal and metadata variance based on contexts

Stability (Variance) Legend

Table 8.6 defines the specific numerical ranges used  to make access decisions for the Trust Model. The ranges are derived by mapping our [0.0 - 1.0] continuous trust score to 1-0.75-0.45 thresholds in line with Confidence Levels and Trust Tiers defined in authoritative industry frameworks (NIST, Google BeyondCorp, CVSS).

Full Access (T>0.75) decisions show that an entity is fully authenticated, compliant, and operating in a secure context. It maps to tier 3:"Highly Privileged Access" based on Googles beyondcorp.Devices in this tier possess the highest level of security hardeningand are granted greater privileges for sensitive internal resources.  This aligns with the upper quartile of trust, requiring effectively perfect scores in at least 3 of 4 domains (Network, Device, Identity) to achieve. Majority Rule" (0.75) is met  such that in a 4-domain system (User, Device, Network, App), if 1 domain fails completely (Score 0.0) and 3 are perfect (1.0), the simple average is 0.75, hence no full access.

Limited Access (0.45<T<=0.75) decisions show an entity is authenticated, but the context carries elevated risk (e.g., BYOD, Public Wi-Fi). It maps to Tier 2: "Basic Access"  and allows for more access than untrusted devices, but restricts sensitive infrastructure. It captures the "Middle Ground" where valid credentials exist but environmental factors (Network/Device) drag the average down. It also maps to the inverse of Medium Severity (4.0 - 6.9) in cvss  and moderate confidence in NIST. Access to a resource is granted if the calculated trust score surpasses a pre-configured threshold and factors such as device status can affect access decisions

No Access (T<0.45) captures an entity that is unknown, non-compliant, or behaving anomalously. It maps to tier 1: "Untrusted" on Googles beyondcorp and the inverse of High/Critical Severity (7.0 - 10.0) in cvss. Devices in this tier have minimal security hardening and are typically allowed to access only publicly available data. The threshold mathematically implies that Uncertainty (m(Θ)) or Disbelief outweighs Belief. Based on fail safe defaults and belief fusion, you cannot grant access when ignorance dominates knowledge. Coin Toss (0.50 → 0.45) is also met and since a score of 0.50 represents "Unknown" or "Random Chance". The threshold is lowered slightly to 0.45 to account for measurement noise (Variance). If the trust score is less than 45% it is statistically safer to deny access. This also provides a 5% "buffer" for benign jitter before revocation.

### Baseline Evaluation: Without any policy Enforcement

This evaluation considers a testbed without any policies. Any user, device and application is allowed to access recources as illustrated by Table 8.3

The absence of access policies often manifesting as "Implicit Trust" or "No Policy" following creates an existential vulnerability within modern, heterogeneous enterprise environments. In such open-policy ecosystems, any entity can access any resource,  and once access is granted, data exfiltration,intrusions on network segments and unchecked lateral mobility become normal occurences. Without continuous verification policies dictating what a specific user can access and when, this implicit trust becomes the primary vector for rapid malware propagation. Malware operations such as ransomware exploit the absence of access control policies to automatically traverse horizontally, encrypting critical assets across servers and workstations that should have been mathematically isolated from the initial point of ingress (IBM Security,  2024).

Furthermore, open access severely exacerbate the risk and financial impact of internal data misuse and exfiltration. In environments lacking authorization thresholds, both malicious insiders and compromised external actors operate with a surplus of unsanctioned privileges. The inability to dynamically restrict access based on shifting contextual risk (e.g., a sudden login from an anomalous location or via an unpatched device) allows attackers ample time to locate and siphon sensitive data undetected from legacy, open-trust paradigms (Gartner, 2023; IBM Security, 2024). Thus, enforcing a continuous, mathematically justified policy tiering system is not merely an exercise in theoretical security, but a quantifiable requirement for operational survival against automated modern threats.

### Testcase 1: Evaluation of Single Criteria Policy

This testcase considers a single domain criteria based access decisions. The decisions are made based onfulfilment of specific criteria within a single domain. These may include user roles, device posture or application profile. This was performed by a rego script enforcing a criterion per domain on User-role, Device-Posture and Application-Profile as shown in Table 8.3. The rego snippet is shown in Figure 8.7



[Figure/Image from source paragraph 1332]

While an improvement over entirely open networks, access control models reliant on single-domain criteria (such as evaluating only device posture or only network location) remain fundamentally fragile in the face of modern enterprise threats. The core limitation of a single-factor approach is its lack of contextual depth; it inherently trusts a single axis of verification while remaining blind to systemic compromises occurring in adjacent domains. For example, if an architecture grants access based solely on a valid, uncompromised remote access gateway such as a VPN connection without secondary hardware checks), an adversary who successfully executes a credential stuffing or phishing attack can immediately inherit that trust. Recent incident analyses have demonstrated that adversaries frequently exploit these single-point-of-verification architectures to bypass initial defenses, leveraging the established trust in one domain to facilitate rapid lateral movement and deploy ransomware throughout the wider environment as seconded by Alder (2025).

This structural myopia dramatically escalates the likelihood of data misuse and resource hijacking. A single-domain model cannot reconcile conflicting contextual signals such as a valid identity token attempting to download massive volumes of sensitive data from a geographically anomalous IP address. Because the system's policy engine only verifies the identity token (the single criteria), the anomalous, potentially malicious behavioral context is ignored. This failure to correlate multi-vector telemetry allows attackers to access restricted resources undetected, utilizing legitimate administrative credentials for unauthorized data exfiltration or resource manipulation (Elastic Security Labs, 2024). To effectively mitigate these risks, modern Zero Trust frameworks must transcend single-domain checks, evolving toward continuous, multidomain verification engines that dynamically analyze identity, device health, network context, and application behavior in tandem.

### Testcase 2: Hierarchical Multi-domain Policy

This evaluates Multi-Domain/Multi-Faceted Zero trust Evaluation. It includes a Combined Multi-Criteria Evaluation  of Access Decisions across multiple domains. It considers user roles, device posture and application profiles. The variations in permutations determine the level of access as Full, Limited or No access as shown in Table 8.4. Variations are als



[Figure/Image from source paragraph 1340]

While this testcase represents a marked improvement over single-domain architectures, Hierarchical Multi-domain Policy (HMP) introduces its own set of structural vulnerabilities when deployed in modern, heterogeneous enterprise environments. HMP architectures inherently rely on a rigid, top-down derivation of trust, where macro-level security postures cascade down to discrete micro-domains such as a corporate root policy dictating the access constraints of an isolated cloud enclave. However, recent analyses demonstrate that this hierarchical rigidity struggles to adapt to the ephemeral nature of modern network workloads and remote access scenarios. Because HMP systems often enforce static rules that lag behind real-time contextual shifts, adversaries frequently exploit the operational delay between micro-domain state changes and macro-policy updates. If an attacker compromises a lower-tier domain such as an improperly configured microservice or an edge IoT device, they can leverage the inherent trust pathways designed for inter-domain communication to bypass the broader security hierarchy, facilitating covert malware propagation (Cloud Security Alliance, 2025; Wang et al., 2024).

Furthermore, the complexity of orchestrating hierarchical trust across distributed and cloud infrastructures often leads to severe policy misconfigurations, dramatically increasing the surface area for data and resource misuse. In an effort to maintain operational continuity across disparate domains, network administrators frequently implement overly permissive inter-domain routing rules, creating fatal security gaps. When a malicious actor or an insider threat gains access to a federated domain characterized by these loose hierarchical bonds, they can exploit the systemic administrative overhead to manipulate access privileges, enabling the lateral exfiltration of sensitive datasets via trusted third-party APIs or supply chain vectors. As advanced, AI-augmented threats continue to target these structural seams within complex policy matrices, it becomes evident that rigid hierarchical models must evolve into fully dynamic, continuously evaluated contextual fabrics to prevent catastrophic data breaches (Al-Sanjary et al., 2023; Cloud Security Alliance, 2025).

### TestCase 3: Multi-Domain with Static Trust Scores and Domain weights

Modern Zero Trust architectures need to treat trust as continuous and dynamic, influenced by posture, behavior, and scenarios that defined context. This means that binary or ternary trust labels  such as trusted, semi-trusted and untrusted are overly simplistic to hanndle these contexts especially in heterogeneous enterprise neeworks. As such, this tescase looks at weighting trusts values depending on context. The focus is static weighting of different domain areas to determine an eventual trust score that is compared against thresholds that detrmine access levels. This testcase forms a fundamental foundation towards more dynamic and cntextual trust estimation and/or determination. Trust score inputs are defined within quuries and used t calaculae trust based on weights provided in the rego scripts. The eventual trust scores are check against predetermined rresholds for full, limited or no access decisions. This  aligns with the multi-criteria, score based continuous trust evaluation principle of Zero Trust. Tunability, and bridging or rule based and probabilistic authorization becomes a critical outcome in this testcase. The rego file snippet, input and output for different subcases within this tescase have been show in figures 8.11 through to 8.15. The explanations for each access decisions that results from the trust determination process is also provided for each sub-case.



[Figure/Image from source paragraph 1348]



[Figure/Image from source paragraph 1350]



[Figure/Image from source paragraph 1352]



[Figure/Image from source paragraph 1354]

The trust value is estimated as Aggregate Trust  of the  domain signals and trust weights. Domain Weights used were User (40%), Device (40%) and Application (20%). Application risk was used as a measure of the profile whih is inversely proportional to application trust profile.

Aggregate Trust= (user_trust × 0.4) + (device_trust × 0.4) + ((1 - app_risk) × 0.2)

This denotes a scenario where user identities are critical as well as device identifiers with less importance attached to the application since once the user and the device are identified, the applications  are mostly controlled based on the two preceding domains that act as parent domains encompassng the application/service domain. This  is  identical to scenario 4 in table  8.5 in testcase 5. The summary of the 7 cases of tescase 3 are represented in Table 8.2

#### Testcase 3 with Temporal Decay

This variation explores how an exponential decay functions transform static trust assessment into more dynamic security postures that reflect operational realities. Traditional Zero Trust implementations largely operate on static trust models where access decisions are based on snapshots of contextual information resulting in limitations such as temporal Insensitivityfor authenticated users, context Staleness especially on device posture, session Inertia where sessions persist beyond their security relevance and a lack of adaptiveness to threat response. The temporal dimension in trust estimation thus consider operational timescales and provide

proportional response mechanisms especially to threats such as Session Hijacking, Device Compromise and Behavioral Anomalies. A rego script implementing an exponential decay fucntion based on a decay constant of 0.01% is used as shown in figure 8.16



[Figure/Image from source paragraph 1367]

#### Testcase 3: Test Cases Summary

#### Testcase 3:Decision Thresholds Matrix

Based on the access decision matrix, the Summary testcase 3 access decisions include immediate denial of access for Blacklisted usersand all users with a trust score that is less than 0.45. privileged users with a trust score above 0.75 get full access while all users with a score between 0.45and 0.75 get limited access to resources. Each decision includes detailed breakdowns of the trust calculation and reason for the decision, making it transparent how the decision was reached.

#### Testcase3: Test Coverage Summary

This table demonstrates how the Zero Trust policy evaluates access decisions based on multiple weighted factors while maintaining clear security boundaries and privilege separation. This testcase illustrates the possibility of real-time threat intelligence integration and logging as well as the use of multiple OPA instances and policies for better scalability and granularity of rules. In a production heterogeanous enterprise network, Use TLS for all inter-service communication, a secrets management vault, healthchecks for the containers and VMs as well as automated orchestration of components and hosts should be considered. Further, deployment of autmated reporting dahsboards and alerting for policy violations would allow for more proactive infrastructure monitoring and faster turnaround times for troubleshooting of user and device issues

The transition to a Multi-Domain architecture represents a necessary evolution in ZTA, yet implementations that depend on static trust scores and fixed domain weights often recreate the very vulnerabilities they sought to eliminate. In these theoretically advanced models, an entity is evaluated across multiple axes (identity, device health, location), but a static score is calculated and maintained for the duration of a session, and the relative importance (weight) of each domain remains rigid regardless of environmental context. This inflexibility is fundamentally misaligned with the dynamic nature of both heterogeneous networks and modern cyber threats. For instance, if a user is granted a high static trust score based on a secure initial handshake from a corporate device, that score acts as a durational passport. If that same device is subsequently infected with a zero-day payload or its network connection is subtly hijacked, the static policy engine lacks the temporal awareness to trigger a re-evaluation. The malware can then inherit the user's high trust score, propagating laterally across domains under the guise of legitimate, pre-approved traffic (Ahmed et al., 2024; National Institutes of Health [NIH], 2023).

Moreover, the reliance on static domain weights severely hampers an enterprise's ability to mitigate sophisticated data misuse and insider threats. In an adaptive model, the weight of a geographic location signal might dramatically increase if the user attempts to access highly classified data outside of standard business hours. Conversely, a static weighting system forces the policy engine to treat context identically regardless of the specific resource being requested or the underlying behavioral volatility. This rigidity empowers compromised identities or malicious insiders; knowing that their assigned trust score will not degrade based on anomalous data access patterns, adversaries can execute slow, methodical "low and slow" exfiltration campaigns. Because the system is not continuously recalibrating trust based on dynamic behavioral deviations (such as an unprecedented volume of database queries), the enterprise remains highly susceptible to data loss disguised as authorized operational activity. To counter this, empirical research overwhelmingly advocates for the abolition of static scoring in favor of continuous, AI-driven contextual re-evaluations and dynamic weight adjustments (Alsubhi et al., 2024; NIH, 2023).

### Testcase 4: Proposed Contextual Trust Weighting for Enterprise relevant Zero trust Facets

This testcase sets an experiment to validate the proposed model. It models and estimates trust in heterogeneous enterprise networks by contextually weighting multidomain trust data signals and fuses the data based on belief, disbelief and uncertainty using weighted belief fusion. The outcome is trust score belief that is used to determine access decisions based on the matrix defined in Table 8.3. the robustness of the trust determination process is based on the aggregation of dynamic weighting and weighted belief fusion across four cardinal domains: Network, Data, Device, and Application. By leveraging Dempster-Shafer theory, it demonstrates how contextual instability (variance) can dynamically discount evidence sources, thereby enhancing the robustness of access control decisions in Zero Trust environments. Due tovariety of permutations for the four domain areas, 6 case scenarios were used to model trust denoting varying resource access requests within enterprise networks. The case scenarios are denonoted in figure 8.20 and table 8.7

#### Testcase4: Case Scenarios



[Figure/Image from source paragraph 1386]

#### Testcase4: Results

Testcase 4: Analysis

Corporate Office represents themost secure pathway with high trust across all domains (Scores>0.90) and Low variance (Stability). This results in rapid convergence to a Full Access decision with a safe belief value that tends towards1 (Bel(Safe)≈1.0). This baseline confirms the system's ability to recognize ideal conditions. The accumulation of evidence from four stable, high-trust sources creates overwhelming belief in the "Safe" hypothesis, minimizing uncertainty to near zero within 3-5 time steps.

Remote VPN shows scenarios where network trust is slightly lower (0.85) due to traversal over public internet, but Device and App integrity remain high. The fusion engine demonstrates robustness. The slight dip in Network trust is insufficient to overturn the strong positive evidence from the Endpoint (Device/App). This effectively models the ZTNA (Zero Trust Network Access) principle: Apply trust to the entity, not just the network resulting in Full Access.

Public Wi-Fi:  Network trust fluctuates significantly (0.02 - 0.40), representing a hostile environment. Since the device is managedm the tust normalizes at a slightly lower score resulting in limited access. The system correctly identifies the risk initially, granting only Limited Access (Bel(Safe)≈0.35−0.67). As the Device and App signals remain stable and high, the system slowly builds trust, eventually upgrading to Full Access if the network signals are verified to be safe. This demonstrates the model's ability to "build trust" over time in an uncertain environment.

BYOD (Bring Your Own Device): High Network trust, but lower Device trust (~0.40) due to lack of management of devices. Initial access is restricted (Bel(Safe)≈0.53). However, unlike a binary "Deny", the system allows the "Good" signals (Network, App) to gradually compensate for the "Bad" signal (Device) as confidence builds. By Step 3, the accumulated stability allows the Trust Score to cross the 0.75 threshold into Full Access, solving the "weakest link" problem for low-sensitivity scenarios.

The Compromised Host:with an active attack, Network, Device, and App all show low scores (< 0.30) and instability. This is the system's "Fail-Safe". The Trust Score plummets to <0.10, resulting in a consistent Deny decision. The Dynamic Weighting discounts the unstable signals, leaving no evidence to support a "Safe" belief.

Untrusted Device in Geofence: Modeled as a strict Zero Trust enforcement where a non-compliant device (~0.30) invalidates the session regardless of location. The simulation resulted in a consistent No Access decision (Bel(Safe)≈0.14). Even if the Network is theoretically secure, the strict parameter tuning for this scenario (setting all domains to Low Trust) demonstrates that the fusion engine respects the "Veto" power of critical failures. If the device is not trusted, the session is not trusted.

The core contribution of this simulation is the demonstration that Stability is a proxy for Trust. In perimeter systems, a fluctuating score (e.g., oscillating between 0.4 and 0.8) might be averaged to 0.6 (Allowed). In this model, that fluctuation spikes Variance, crashes the Weight, and effectively removes the domain from the decision process.This ensures that decisions are made only based on reliable evidence. A sensor that does not present data is treated as Uncertainty rather than "Half Safe". This aligns perfectly with the principle of Fail-Safe Defaults in cybersecurity. These are  illustrated by appendices X-y

The implementation validates that a Granular, Two-Stage Fusion approaches (Weighted Sum + Belief Fusion) offers a superior access control decision engine for heterogeneous networks. It accommodates the ambiguity of real-world signals (BYOD, Public Wi-Fi) without being brittle, while maintaining strict security (Denial) when the aggregate environment becomes unstable or hostile. This is summarized in Figure 8.21



[Figure/Image from source paragraph 1402]

The integration of Dynamic Contextual Weighting with Dempster-Shafer belief fusion provides a superior mechanism for Zero Trust enforcement. It  mathematically distinguishes between "Known Bad" (Low Score, High Weight) and "Unknown/Unstable" (High Variance, Low Weight), to achieve a nuanced "Gray Area" decision capability essential for modern, heterogeneous network environments.

### Testcase 5: Multidomain Contextually weighted  trust determination with temporal decay

#### Case 1: Multidomain Contextual weighting and Belief Fusion

Most access control models suchRBAC, ABAC) often rely on static policy evaluation. This testcase considers heterogeneous enterpise network environments characterized by BYOD, edge computing, and remote working where trust is ephemeral. Static "trusted" devices may become compromised within minutes necessitating a Continuous Adaptive Risk and Trust Assessment (CARTA) approach. The implementation models this through dynamic Contextual Weighting and  weighted belif fusion. Dynamic trust assessment uses signal (metadat input) stability (variance) as a measure of reliability while belief Fusion uses the Dempster-Shafer (DS) Theory of Evidence to mathematically combine conflicting or uncertain inputs. The inputs include parameters in the network, data, device and application domains as discussed in section 4.6.

The network domain represents the transport layer security (Zero Trust Network Access - ZTNA) with corporate office and public wifi scenarios indicating high network trust (0.95and low trust (0.30) with high uncertainty. Sudden latency spikes or routing changes (simulated as "Network Attack") increase varianceand this variance drastically reduces the weight of the Network domain, effectively removing it from the consensus without policies explicitly failing.

Data Domain contextualizes sensitivity and classification of the resource being accessed.   High data sensitivity (Trust Score ~0.90 for authorized access) demands higher aggregated belief for access. Low sensitivity allows for "Limited Access" even with lower overall trust. Device Domain represents the health and identity of endpoints  and is critical  in "BYOD" or "Untrusted Device" scenarios where the score drops (0.20 - 0.40). The fusion engine decides if a secure Network and App can compensate for an insecure Device. Our emulation shows that with weighted fusion, a single low-trust domain (Device) generates significant Uncertainty mass, often preventing a "Full Access" decision unless other signals are overwhelmingly positive. Finally, the application Domain contextualizes the security posture of the requesting application. An application behaving anomalously (high signal variance) would be discounted.

The integration of Dynamic Contextual Weighting with Dempster-Shafer belief fusion provides a superior mechanism for Zero Trust Access Control compared to static Boolean logic. By mathematically distinguishing between "Known Bad" (Low Score, High Weight) and "Unknown/Unstable" (High Variance, Low Weight), the system achieves a nuanced "Gray Area" decision capability—essential for modern, heterogeneous network environments.

#### Case 2: Timed Multidomain Contextual weighting and Belief Fusion with 30 min Session(Short Term Memory)-linear

This case expands upon case 1 (Weighted Belief Fusion architecture) by introducing a temporal decay factor. The core thesis is that Trust is a Function of Time. In addition to spatial fusion (Network, Device, Data, App), the system now enforces a linear degradation of trust based on "Session Freshness," effectively creating a dynamic Time-to-Live (TTL) that scales with the initial security posture. Static authentication creates a security vulnerability: the "Implicit Trust Period." Once a user authenticates, they are typically trusted for the duration of a session (e.g., 8-24 hours). Our implementation challenges this by enforcing a Continuous Decay Model. Trust is not a boolean state achieved at login; it is a depreciating asset that must be continuously renewed or allowed to expire. This case implements a linear decay functionwith a maximum session duration of 30 minutes (as informed by reference table sessions). The Final Trust Score is the product of the multidomain trust and the Decay Factor. This ensures that regardless of how secure the device or network is, the system will inevitably revoke access as the session period tends towards the maximum length. The model evaluated the temporal model against the six canonical scenarios to observe how linear decay impacts access durations. The access thresholds remain as per (Table thresholds). The access decision outcomes are sumarized in Table x

The addition of temporal decay transforms the Trust Fusion engine from a static evaluator into a dynamic lifecycle manager that considers security by  mitigating session hijacking risks by enforcing shorter windows of opportunity in risky environments. It also enhances usability as it naturally "upgrades" secure contexts with longer effective sessions compared to insecure ones. This confirms that Time is a critical dimension of Zero Trust, equal in importance to Identity and Device Health.

The Time-Decayed model successfully implements a dynamic "Time-to-Live" (TTL) for trust. It provides a nuanced behavior where Secure Contexts enjoy the full session duration while Risky Contexts suffer from accelerated timeout (Effective TTL < Nominal TTL). This adaptive session management significantly reduces the attack surface for session hijacking.

While linear decay is simple and decays at a stedy rate, it is best for simple, predictable Time-to-Live (TTL) mechanisms where you just want a hard cutoff that approaches zero evenly.

In advanced Zero Trust models Freshness  should be decayed exponentially

Because Linear Decay is Too Slow Initiallyand keeps a 50%weight for aan event that is half the session length (15-minutes in this case). In modern network environments, a session can be hijacked or a device compromised in a matter of seconds. Relying heavily on an old signal oe matadata value is dangerous and coud easily result in malware propagation, lateral escalation and data misuse and intrussions in heterogeneous enterprise networks. Additionally, Exponential decay allows the system to prioritize absolute freshness during the critical first few minutes (the "Handshake" or "Boot-up" phase). By minute 5, an exponential decay curve drastically drops the value of that initial connection state. This forces a transition to inertia trust or combinations of inertia and metadata values for continous verification.This forces the fusion engine to shift its reliance onto the combination of Historical Inertia an consistent hbehavior history. The logic is: "That initial handshake is no longer fresh. I am no longer going to trust what the device said 10 minutes ago; instead, I am going to trust the consistent behavioral history it has built up over the last 10 minutes." Linear decay turns trust into a simple ticking timer. Exponential decay treats trust like a highly volatile element that must be instantly verified and then immediately handed off to behavioral momentum in line with continuou verification and continouos improvement principles of zero trut enforcement

#### Case 3: Timed Multidomain Contextual weighting and Belief Fusion with 30 min Session(Short Term Memory)-Exponential

This case explores the theoretical friction between continuous authentication and session longevity by introducing Exponential Temporal Decay into the Weighted Belief Fusion architecture. The core thesis expands upon the premise that Trust is a Function of Time by evaluating how an aggressive decay curve impacts the "Effective Session Length" in various contextual states. Static authentication protocols trust a user for the entirety of their session (the "Implicit Trust Period"). While the previous linear temporal decay model addressed this by enforcing a steady erosion of trust, an exponential model challenges the fundamental concept of a "Session." By applying an exponential  decay function, the architecture mathematically asserts that the instant a cryptographic handshake concludes, its value plummets. This is illustrated in Table x. This case evaluated this model against the six canonical scenarios, noting the severe compression of access durations compared to the linear variant.

This case effectively establishes a dynamic "Time-to-Live" (TTL) that is heavily front-loaded. For example with a decay constant of λ=3.0 over a 30-minute session, the emulation shows that the final trust score the final trust score will crash through the "Limited Access" threshold (0.75) and plummet into "No Access" (<0.45) within the first 5−10 minutes. With this session hijacking becomes practically impossible. Stolen cookies or transient network compromises are suffocated by the rapid expiration of the authentication event's initial weight. This is great in ensuring little to no chances of intrusion and data misuse as a result of reply attacks or lateral escalation. This however results in  unusability as the Operational Reality. This is because in a purely exponential decay model, Users would be forcefully ejected from their applications every few minutes causing complete operational paralysis and rendering it unusable in a production environment.

This therefore indicates that Exponential Temporal Decay perfectly validates the architectural necessity of an Ensemble Trust Model such that if the value of an initial authentication event must decay rapidly for security reasons (Exponential Decay), then the system must have a mechanism to replace that lost value with operational signal ormetdata vaues for continuous verification and behavior consistency building. An enseble model thatconsiders multiple domains, an inertia trust value and temporal decay resolves the usability vs security paradox. It intentionally utilizes the aggressive exponential decay to kill off the "Fresh Verification" signal, but uses that identical temporal function to inversely transfer weight onto the user's domains including the trust Inertia.

Therefore, exponential decay proves that sustained Zero Trust enforced access cannot be supported with  continuous verification (which decays), but must be carried by continuous behavioral consistency (which accumulates).

#### Case 4: Ensemble Multidomain Contextual weighting and Belief Fusion with 30 min Session(Short Term Memory) and 48 hour Inertia Trust (Long Term Memory)

This case considers the theoretical underpinnings of the Ensemble Trust Model. By hybridizing Short-Term Spatial Fusion (Dempster-Shafer) with Long-Term Temporal Inertia (Exponential Decay), it establishes a system that resolves the fundamental tension in Zero Trust: Security vs. Usability. Zero Trust Architectures (ZTA) often treat every access request as a discrete, independent event. This leads to the "Jittery Access" problem, where minor, transient fluctuations in network latency or device CPU usage cause authentication failures. This Ensemble Model posits that Trust has Momentum (Inertia) such that an untrusted history or inertia trust requires significant evidence to change the trust score or trajectory for a specific context. This implies that a user with a strong history of safe behavior should not be revoked due to a single dropped packet (Noise). Conversely, a user with a history of compromise should not be reinstated due to a single clean packet (Beaconing). This is sigbificant in handling On-Off attacks especially in highly volatile environment such as virtualized infrastructure, BYOD and IoT environments which have significantly changed the posture and threalandscape of heterogeneous enterprise environments

The model maintains a freshness-inertia Continuum by implementing a dynamic slider between Signal (metadata telemetry) and Memory, governed by "Session Freshness". At intialzation  at time (t→0), the telemetry data is fresh and themodel is Signal-Dominant. It operates on the premise that the session data is not enough to create a profile on the request and thus evvaluates the current  user identifiers, Device Health, application profile, and network posture. This is because at the start of a session, verification must be Absolute and Inertia trust should not override a bad login attempt. At maturation of a session  (t→30), the session freshness is not there and therefore th model is Inertia-Dominant. It therefore operates on the premise that based on an approximatesly 30min signal telemetry observation, the entity’ behavior has been consistent (or inconsistent) and therefore trust will be placed more on accumulated knowledge  than this specific millisecond's reading. As verification ages, Consistency defined and becomes Policy. The system effectively locks the decision, reducing the attack surface for session hijacking (a hijacker would need to mimic the established history perfectly to avoid triggering a massive deviation, but even then, the inertia resists rapid change). Thi results in beter access control and more effective  resource misuse and intrusion prevention in heterogeneous enterprise environments. It also ensures continuous verification and monitoring of recources access per session.

The results are illustrated in Table X. The implications indicate that in the case of an authenticated user, the sesion Starts with Full Access due to succesful authentication. As time passes (t→30), the weight on Fresh Signals decreases because they have built up "Momentum" and  Access persists smoothly. On the contrary, if an Attacker attempts access based on spoofed credentials, they start with No Access. As time passes, the system "Remembers" they are bad. Even if they mimic a safe signal for or after 30 minutes, the Inertia weighs the history of "Bad" so heavily that access remains denied.

The Ensemble Model successfully implements Contextual Durability. It moves Zero Trust from a stateless "Packet Fighter" that focues on micro-fluctuations per domain area to a stateful "Behavior Engine," enabling robust security that respects the continuity of legitimate work. A stateless packet evaluater tries to review every individual network packet or API call instead of looking at the macro-behavior of the user such as a healthy device or anomalous application behaviour. It therfore results in revoked access if a remote worker's network drops a single packet, or their congestion window spikes for one second causing a latency delay in a health check, because micro-fluctutation. A stateful behavior engine on the other hand remembers that the device has been secure based on historical Inertia, absorbs minor, transient network jitters only revokes trust if the behavioral trend actually shifts toward an anomaly. While  a stateless "Packet Fighter" causes the "Jittery Access" problem where users are constantly booted offline for benign network hiccups, the Ensemble Model fixes this by looking at the broader continuity of the session.

The progression of computational architectures in this research underscores a fundamental reality of Zero Trust: security cannot rely on absolute, discrete proofs.

The evaluation reveals that static frameworks like Single-Domain Trust are fundamentally fragile, oscillating wildly between extreme risk and extreme usability friction. The introduction of Multidomain Base Fusion via Dempster-Shafer theory successfully mitigated telemetry brittleness, enabling contextual gray-area routing. However, this spatial-only model failed to account for the ephemerality of the connection context, highlighting the necessity of temporal integration.

Both Linear and Exponential time variants proved that Time-to-Live (TTL) must be dynamically bound to contextual risk. Yet, the aggressive depreciation demanded by security explicitly conflicts with the continuity demanded by operations.

The final Ensemble Trust Model represents the synthesis of these conflicting forces. By abstracting access controls into mathematical momentum, the architecture recognizes that sustained programmatic access cannot be supported solely by continuous re-verification—which is inherently volatile and decays in value—but must be carried by mathematical behavioral consistency. This evolution from implicit trust perimeters to stateful, inertia-driven fusion provides a robust blueprint for next-generation Continuous Adaptive Risk algorithms inside enterprise architectures.


---

# PART V: MEANING AND FUTURE WORK

# Chapter 10: Implications for Enterprise Security Design

*Chapter 9 demonstrated the empirical effectiveness of the Ensemble Trust Model across multiple enterprise scenarios. This chapter translates those quantitative findings into actionable implications for enterprise security architecture, policy design, and future AI-driven security paradigms.*

# : CONCLUSIONS, RECOMMENDATIONS, AND FUTURE WORKS

## 1. Conclusion: The Paradigm Shift in Continuous Verification

### The Fallacy of Static Trust

The foundational premise of this research is that static trust models—even those marketed under the umbrella of "Zero Trust"—are structurally deficient against modern, automated cyber threats. The evaluation demonstrated that traditional architectures rely on a fatal misconception: the assumption that a cryptographically secure authentication event guarantees the subsequent behavioral integrity of the session. Whether deployed as perimeter "No Policy" ecosystems or more granular Single-Domain and Hierarchical models, static architectures suffer from the "Implicit Trust Period." By granting durable access without continuously validating the operating context, these systems effectively provide a secure operational runway for session hijackers, lateral malware propagation, and insider exfiltration (Elastic Security Labs, 2024; IBM Security, 2024). Ultimately, cybersecurity can no longer treat authorization as a discrete, binary checkpoint; it must be approached as a continuous, stateful evaluation.

### The Efficacy of Multi-Domain Evidential Fusion

To resolve the brittleness of binary access controls, this research validated the deployment of probabilistic fusion engines. Moving beyond simplistic rulesets, the application of Dempster-Shafer (DS) evidence theory allows for the continuous mathematical synthesis of telemetry across independent logical spaces (Identity, Device, Network, Data). Crucially, the integration of Dynamic Variance-Based Weighting into the DS model solves the "noisy sensor" problem prevalent in heterogeneous enterprise environments. Rather than issuing catastrophic false-positive lockouts due to transient network drops, the engine accurately categorizes this instability as Uncertainty, gracefully shifting users into safely quarantined "Limited Access" tiers (Liu et al., 2023; Wang et al., 2024). This capability to execute Contextual Gray-Area Routing proves that access control can maintain strict security constraints without sacrificing operational continuity.

### The Necessity of Temporal Dynamics

While spatial fusion models excellent context-awareness, the defining contribution of this research is the mathematical integration of Time into the Zero Trust equation. The evaluations of both Linear and Exponential Temporal Decay frameworks explicitly prove that Trust is an ephemeral asset. A mathematically verified session degrades in reliability the longer it persists active without re-verification. While Exponential decay provides an absolute, highly aggressive kill-switch against persistent threats by forcing a state of continuous algorithmic suspicion (Robbins et al., 2025), its operational friction necessitated a higher-order solution.

The resulting Ensemble Trust Model successfully harmonizes this tension. By hybridizing the rapid decay of initial cryptographic "Freshness" with the mathematical momentum of long-term behavioral "Inertia," the architecture effectively traps advanced persistent threats (APTs) in a paradox. To subvert the Ensemble engine, an adversary must not only intercept a valid identity token but also perfectly replicate the victim’s long-standing behavioral baseline over an extended duration (Al-Tariq et al., 2025).

### Fairness and Transparency in Trust Models

A critical consequence of deploying mathematical evidential fusion is the necessity for algorithmic fairness and transparency. As the Ensemble Trust Engine dynamically revokes or limits access based on behavioral variances, the logic driving these decisions must remain opaque to attackers but entirely transparent to system administrators and auditors (Chen & Wang, 2025). Trust models must ensure that the weighting of metrics (Mi,jMi,j​) does not inadvertently encode biases against specific user demographics, device types, or operational roles, which has been identified as a critical vulnerability in heuristic ZTA (Zheng et al., 2024). The normalization of Dempster-Shafer combinations must provide a clear, auditable trail explaining exactly which domain (e.g., Network Anomaly vs. Identity Freshness) triggered a trust degradation.

### Summary of Contributions

This thesis transitions the theoretical discourse on Zero Trust Architecture into a mathematically actionable framework. By disproving the viability of static, boolean access policies and demonstrating the superior resilience of multi-domain evidential fusion bound by strict temporal decay, this research provides a definitive mathematical blueprint for Continuous Adaptive Risk and Trust Assessment (CARTA). The progression from simple gateways to the stateful, behaviorally driven Ensemble Trust Engine ensures that modern enterprises are equipped algorithmically to strangle lateral malware movement and neutralize stealthy data misuse.

## Recommendations

### Adaptive Routing and Algorithmic Calibration

The aggressive mandate for enterprises to adopt Zero Trust architectures necessitates practical deployment strategies over strict theoretical binary enforcement. A primary recommendation is that organizations abandon absolute binary (Allow/Deny) logic in favor of Adaptive Gray-Area Routing. Recognizing that transient sensor failures and network jitter will occur, routing mathematically ambiguous sessions into constrained "Limited Access" enclaves prevents catastrophic lockouts and preserves operational continuity while isolating potential threats (Cyber Advisors, 2024; Help Net Security, 2024). The efficacy of this routing is inherently contingent upon the accurate calibration of temporal decay. This research recommends a federated approach to decay rates (λλ) rather than a monolithic organizational policy. For standard corporate workloads (e.g., accessing HR portals or internal communications), a Linear Decay model parameterized to an standard 8-hour operational shift provides sufficient security while minimizing user friction. Conversely, for high-value enclaves (e.g., source code repositories, industrial control systems, or classified data stores), organizations must implement Exponential Decay parameterized for aggressive session expiration (e.g., λ=3.0λ=3.0 targeting a 30-minute absolute TTL). Furthermore, the αα sensitivity parameter controlling the variance penalty must be tuned strictly; environments with highly predictable application telemetry should employ a high αα multiplier to instantly penalize any deviations, effectively establishing a state of automated, continuous suspicion (CIO Coverage, 2024; Right-Hand AI, 2024). Furthermore, because continuous evaluation inherently produces trust conflicts across disparate telemetry sensors, organizations must natively integrate deterministic resolution mechanisms, such as Secure Access Service Edge (SASE) models, and enforce strict reputation revision policies to manage how users regain trust following a demotion (Al-Faresi et al., 2024; Gomez & Silva, 2025).

### Scalable Infrastructure and Real-Time Telemetry

The deployment of Continuous Adaptive Risk and Trust Assessment (CARTA) via an Ensemble model fundamentally alters infrastructure requirements, imposing severe strain on legacy centralized policy decision points. The continuous mathematical evaluation of every network request imposes severe strain on legacy, centralized policy decision points (PDPs). To prevent the trust engine from becoming a catastrophic network bottleneck, organizations must deploy scalable, containerized microservices architectures deployed across multi-cloud environments. By decoupling the trust calculation engines from the physical network gateways, enterprises can dynamically scale their evaluation infrastructure in response to sudden traffic spikes, ensuring that continuous verification does not degrade legitimate business operations

(Exabeam, 2024; Seraphic Security, 2024). This requires tightly integrating Zero Trust Network Access (ZTNA) gateways with advanced Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platforms (TrustBuilder, 2024; Netwise Tech, 2024). Crucially, the fidelity of this dynamic infrastructure depends entirely on the real-time integration of behavioral telemetry. Enterprises must shift from batch-processed log analysis to streaming data architectures (e.g., Apache Kafka) to minimize the latency between endpoint anomalies and central fusion evaluation, drastically reducing the runway available to session hijackers (Cybersecurity Insiders, 2024).

### Automated Orchestration, State Reconciliation, and Validation

Operationally scaling Software Defined Perimeters (SDP) across complex namespaces (Docker, LXC) is impossible through manual configuration (Data Insights, 2024). A paramount recommendation is the automated orchestration of SDP controllers linked directly to the evidential fusion engine, utilizing infrastructure-as-code to automatically collapse micro-segments when trust scores decay (GSD Council, 2024). However, as evidenced by cross-layer testbeds, this automated execution introduces a severe vulnerability regarding the fragility of state synchronization between the application layer (SDP) and the network enforcement layer (SDN). The deployment of continuous evaluation inherently produces trust conflicts—scenarios where different telemetry sensors provide highly contradictory evidence (e.g., a pristine device reputation score clashing with a severely degraded network protocol score). Organizations must establish deterministic resolution mechanisms within the fusion engine to handle these conflicts natively, often through unified models like SASE (Al-Faresi et al., 2024). Enterprises must therefore mandate active heartbeat and reconciliation threads (e.g., 30-second polling intervals) within the Policy Orchestrator to detect and immediately correct any policy drift. Furthermore, the concept of "Reputation" must be treated as a slowly accumulating asset, governing how quickly a system allows a user to recover trust after a demotion. This necessitates formal trust revision methods: algorithmically defining whether a user can organically rebuild their trust score through sustained benign behavior or if an administrative intervention (e.g., a hard MFA reset) is required to revise a deeply penalized session state (Gomez & Silva, 2025). Finally, to rigorously validate the ongoing resilience of these orchestrated environments against lateral movement, security teams must abandon ad-hoc penetration testing in favor of "adversary-in-a-box" toolkits—containerized, auto-starting exploitation frameworks used to constantly baseline SDP/SDN protective response

### Leveraging Indirect Trust, Transmission, and Quality

While the proposed model focuses heavily on Direct Trust (first-hand telemetry), operational scalability requires the integration of Indirect Trust. Organizations should engineer mechanisms for trust transmission, where the established reputation of a highly trusted node or identity can be partially inherited by a newly associated, unknown entity (e.g., a new managed device provisioned strictly through a trusted administrative terminal) (Kumar & Singh, 2024). However, the ingestion of indirect trust must be gated by a rigorous assessment of the "Quality of Trust", evaluating the provenance, age, and mathematical confidence of the transmitted evidence before inherently fusing it into the primary Dempster-Shafer equations (Zhao et al., 2025).


# Chapter 11: Conclusion and Research Trajectory

*This thesis set out to answer a fundamental question: can trust in heterogeneous enterprise networks be computed dynamically rather than assumed statically? The preceding chapters have progressively built, validated, and interpreted the answer. This final chapter closes the narrative loop.*

## Future Research Directions and Expanding the Architecture

### Short-Term

Federated Edge Intelligence & Cryptographic Agility: The current Ensemble Trust Model processes evidential fusion locally. Short-term research must expand this paradigm into Federated Learning ecosystems, allowing independent edge environments like Fog computing domains, to collaboratively train trust variance thresholds without transmitting raw, sensitive security logs (Alqassem et al., 2025). Concurrently, to address the computational latency inherent to processing Dempster-Shafer equations at the deep edge such as IoT devices), future iterations must develop secure offloading protocols or lightweight cryptographic approximations of the fusion engine (Chime Central, 2024; Cognizant, 2024). Furthermore, as regulatory mandates regarding crypto-agility tighten through 2026 in anticipation of cryptanalytically relevant quantum computers (CRQC), integrating Post-Quantum Cryptography (PQC) standards (e.g., ML-KEM) directly within the foundational authentication layer will be necessary to preserve the integrity of the initial "Freshness" scores (Capgemini, 2024; ECCU, 2024; Ridge IT, 2024).

Explainable AI (XAI) Integration: The shift toward algorithmic, dynamic trust revocation demands absolute transparency for operational viability. Integrating XAI directly into the Dempster-Shafer normalization process will ensure that human analysts receive immediate, human-readable rationale for every automated access denial or step-up MFA challenge, successfully mitigating the "black box" criticism often levied against machine learning security deployments (Chen & Wang, 2025).

### Medium-Term

Adaptive profiles and Autonomous Orchestration: The current Ensemble Model relies on predefined geometric parameters. A highly promising avenue rests in graduating from static variance to dynamic, AI-generated "Inertia profiles" through unsupervised deep learning architectures to combat persistent insider threats (Barchart, 2024; Pantherun, 2024; Preprints, 2024). Furthermore, future frameworks should leverage Decentralized Trust Management Systems (DTMS) powered by Bayesian evaluation to autonomously recalculate user credibility (Li et al., 2025). This autonomous capability must be tightly coupled with cross-layer trust orchestration, allowing a compromised node detected at the application layer to instantly trigger strict hardware-level isolation at the MAC or PHY network layers. Finally, looking beyond current deterministic engines, the next evolution involves AI predicting trustworthiness probabilistically, anticipating trajectory failures, and severing access before a breach materializes (Patel, 2025).

Infrastructure Resiliency & Cryptographic Hardware Offloading: As continuous evaluation frameworks begin governing hyper-dense enterprise networks, scalable infrastructure and anticipatory risk modeling will prove necessary to automatically provision computational capacity ahead of localized traffic surges (MeriTalk, 2024). Crucially, because bulk data encryption across hundreds of concurrent SDP tunnels induces severe latency (Shallom, 2025), medium-term research must explore offloading performance-intensive Zero Trust cryptography directly onto dedicated hardware accelerators (e.g., SmartNICs or Data Processing Units). Furthermore, to rigorously test these high-throughput gateways against evasion techniques, the current containerized testbed methodologies must mature into full hardware virtualization setups (e.g., QEMU/KVM) and Trusted Execution Environments (TEEs) capable of identifying OS-specific rootkits and bootkits (Chou et al., 2025; Zhang & Liu, 2025).

Privacy-Preserving Telemetry & Blockchain Accountability: The push for real-time validation will inevitably require the ingestion of hyper-dense behavioral telemetry from emerging workflows like virtualized environments, encrypted workflows and extended realities without deciphering underlying personally identifiable information (PII)  . To preserve user privacy while calculating complex, biometric trust scores, the fusion engine will need to employ Zero-Knowledge Proofs (ZKPs) or Fully Homomorphic Encryption (FHE) techniques (Zheng et al., 2025). Concurrently, to guarantee absolute transparency and resolve algorithmic disputes generated by autonomous execution, every trust context variable and resulting access decision should be actively logged onto an immutable blockchain ledger, defining a mathematically unforgeable compliance trail (Nguyen et al., 2024).

### Long-Term

Cognitive Architectures & Self-Healing Topologies: Beyond predictive machine learning, the absolute future of continuous assessment lies in Cognitive Trust Systems. These architectures will employ artificial general intelligence (AGI) paradigms to contextualize human intent, understanding why a user is accessing data, thus moving beyond mathematical variance thresholds to true semantic and psychological security evaluation. Guided by deep reinforcement learning, these cognitive SDP controllers will proactively formulate self-healing network topologies (SecurityWeek, 2024). Upon detecting severe trust degradation or an active adversarial breach, the network will physically and algorithmically restructure its routing tables to instantly isolate compromised entities while autonomously constructing alternate, secure pathways to maintain critical business continuity (Cloud Security Alliance, 2025).

Quantum Trust Computation: Long-term horizons must transcend the mere implementation of quantum-resistant encryption (PQC) and explore the utilization of quantum computing native algorithms for the trust evaluation process itself. Quantum evidential fusion engines will possess the capability to process virtually infinite telemetry variables and historical baselines concurrently, functionally reducing the latency of the complex Dempster-Shafer combinations from measurable milliseconds to operational zero.


---


# APPENDICES

This section compiles screenshots, raw data, source code snippets, and graphical outputs generated during the tesstbed setup, installation processes, network emulation, mathematical derivations, access policy scripts and simulations of the of the models in the seincremental development of the trust models proposed, designedand tested in this research. The data serves as empirical proof of the efficacy of the proposed Ensemble Trust Model with temporal decay of meatadat signals and historical behavior.

## Appendix A: Core Simulation Code and Algorithms

### A.1 Dempster-Shafer Combination Engine (ds_utils.py)

The foundational logic for evidential fusion relies on Dempster-Shafer Math, normalizing conflicting domains. The custom combine method calculates the mathematical intersection of Belief masses (mm) across Independent sensors. If the sensors report contradicting telemetry, the conflict (KK) is quantified and the resulting Trust Score (Belief(Safe)Belief(Safe)) is algorithmically dampened.



[Figure/Image from source paragraph 1521]



[Figure/Image from source paragraph 1523]

### A.2 The Ensemble Decay Algorithm (ensemble_trust_simulator.py)

This snippet demonstrates the algorithm responsible for calculating continuous session decay utilizing exponential (λλ) factors. It explicitly hybridizes historical inertia (whistorywhistory​) with instant cryptographic freshness (wshortwshort​). As time progresses without re-verification, the engine automatically shifts the burden of trust away from the initial spatial signal and onto the mathematical behavioral variance.



[Figure/Image from source paragraph 1529]

## Appendix B: Standardized Scenario Configurations

To test the simulation universally across models, a standard six-scenario matrix was established mapping theoretical Network, Device, Data, and App variables to realistic operational bounds. This standardization enables direct comparative analysis. By holding the inputs constant, the variances in the ensuing output graphs uniquely isolate the mechanical behavior of the Trust Models being tested.



[Figure/Image from source paragraph 1534]



[Figure/Image from source paragraph 1535]

## Appendix C: Phase 1 & 2 - Base Dynamic Weighted Belief Fusion

This initial framework demonstrates the ability to isolate spatial uncertainty using variance weighting, dynamically ignoring chaotic ambient noise (like public Wi-Fi jitter). Note that the raw simulation outputs plateau unconditionally, proving the necessity of temporal constraints.

### Sample Output Data

Public Wi-Fi Snippet: The data illustrates how a highly unstable network (0.130.13) initially restricts trust to 0.350.35 (Limited Access). However, by Step 5, the model recognizes the stability in the Device and App sensors, algorithmically boosting the Belief (0.770.77) to grant Full Access despite the noisy environment.



[Figure/Image from source paragraph 1541]

Compromised Host Snippet: This data logs the system's "Fail-Safe". Because all incoming spatial telemetry is extremely low (<0.30<0.30) and highly variant, Dempster-Shafer calculates overwhelming Disbelief. The session is immediately terminated with a raw Trust Score plummeting below 0.050.05.



[Figure/Image from source paragraph 1545]

### Graphical Outputs

The base model plots immediately demonstrate rapid geometric convergence toward 1.01.0. Because time is mathematically ignored throughout this phase, the system builds an impenetrable baseline of trust within 10 operational steps that never degrades.



[Figure/Image from source paragraph 1550]



[Figure/Image from source paragraph 1551]



[Figure/Image from source paragraph 1553]



[Figure/Image from source paragraph 1554]

## Appendix D: Phase 3 (Linear) - Temporal Decay

The introduction of a linear Time-To-Live (TTL) standardizes session durations for corporate compliance, effectively enforcing re-authentication at defined intervals (e.g., NIST AAL2). However, the predictable, gradual downward slope of the trust calculation lacks the urgency required to defeat an active session hijacker operating quickly within the approved window.

### Graphical Outputs

These models reveal mathematically predictable degradation. Regardless of how pristine the initial spatial authentication was (e.g., Corporate Office), the trust algorithm decays by a rigid, standardized value every time step, ultimately intersecting the 0.450.45 termination threshold precisely on schedule.



[Figure/Image from source paragraph 1560]



[Figure/Image from source paragraph 1562]



[Figure/Image from source paragraph 1564]

## Appendix E: Phase 3 (Exponential) - Temporal Decay

Exponential decay introduces an aggressive λλ parameter that serves as an immediate cryptographic kill-switch against Advanced Persistent Threats (APTs). By forcing the trust score to crash precipitously the moment spatial telemetry verification stops, the system maintains a state of continuous suspicion, mathematically collapsing hijacked sessions before lateral movement can be executed.

### Graphical Outputs

Unlike the linear models, these exponential plots exhibit a volatile concave curve. The trust score plummets the moment the initial session is granted, forcing the user (or hijacker) into a state of immediate re-verification. While secure, the aggressive mathematics render this model practically unusable for standard high-productivity workflows.



[Figure/Image from source paragraph 1570]



[Figure/Image from source paragraph 1571]



[Figure/Image from source paragraph 1572]

## Appendix F: Phase 4 - The Ensemble Trust Model

The Ensemble model resolves the operational turbulence of strict exponential decay by hybridizing instant cryptographic "Freshness" with a rolling window of behavioral "Inertia". This sophisticated architecture successfully absorbs minor environmental jitters (maintaining the session) while ensuring that a fundamental shift in user behavior still results in a rapid algorithmic denial.

### F.1 Sample Output Data

Remote VPN Snippet (The Hybridization): Here we see the transition in real-time. At T=0T=0, the session relies entirely on cryptographic Freshness (0.7870.787). By T=29T=29, Freshness has decayed exponentially (0.0430.043), but the user's Behavioral Inertia has successfully scaled (0.7390.739) to maintain a stable, highly-trusted session (0.7820.782).



[Figure/Image from source paragraph 1579]

Compromised Snippet: The model proves its lethality. Because the initial Instant Trust was terrible (0.2260.226), it failed to build any significant Inertia weight (0.2790.279). The final Ensemble score stabilizes far below the access threshold (0.2980.298), locking the attacker out permanently.



[Figure/Image from source paragraph 1585]

### F.2 Graphical Outputs

These final output graphs represent the optimal Zero Trust state. The chaotic oscillations seen in the Exponential model are dampened, resulting in clean, reliable trust thresholds that maximize operational continuity while inherently blocking access vectors that lack established historical inertia.



[Figure/Image from source paragraph 1590]



[Figure/Image from source paragraph 1592]



[Figure/Image from source paragraph 1593]

## Appendix G: Trust Domain Metrics

The following table formalizes the mathematical equations utilized by the Dempster-Shafer combination engine to calculate the individual domain trust values (TDiTDi​​) from their underlying aggregated metrics (Mi,jMi,j​).




**Table G.1: Trust Domain Metric Equations**

| Domain | Metric | Equation |
|:-------|:-------|:---------|
| Data | Integrity | $\displaystyle I = 1 - \frac{\text{anomalies}}{\text{total checks}}$ |
| Data | Freshness | $\displaystyle F = e^{-\lambda t}$ |
| Data | Authenticity | $\displaystyle A = \begin{cases} 1 & \text{verified source} \\ 0.5 & \text{unknown source} \\ 0 & \text{unverified} \end{cases}$ |
| Device | Identity | $\displaystyle Id = \begin{cases} 1 & \text{hardware cert} \\ 0.7 & \text{MAC known} \\ 0.3 & \text{unknown} \end{cases}$ |
| Device | Reputation | $\displaystyle R = 1 - \frac{\text{incidents}}{\text{max incidents}}$ |
| Device | Compliance | $\displaystyle C = \frac{\text{compliant checks}}{\text{total checks}}$ |
| Application | Behavior Consistency | $\displaystyle B = 1 - \sigma^2$ |
| Application | Vulnerability Score | $\displaystyle V = 1 - \frac{\text{known vulns}}{\text{max vulns}}$ |
| Application | Access Compliance | $\displaystyle A = \frac{\text{authorized accesses}}{\text{total accesses}}$ |
| Network | Protocol Score | $\displaystyle P = \frac{\text{compliant packets}}{\text{total packets}}$ |
| Network | Anomaly Detection | $\displaystyle A = 1 - \frac{\text{anomalies}}{\text{total flows}}$ |
| Network | Segmentation | $\displaystyle S = \begin{cases} 1 & \text{micro-segmented} \\ 0.5 & \text{VLAN} \\ 0 & \text{flat} \end{cases}$ |


## Code and Implementation Details

### Dataset Descriptions

Synthetic Data: Generated per scenario, adavrsarial, trusted and insiders

Emulated Data: From testbed experimentation

Real-world Traces: Anonymized enterprise network identifiers across the internet

### Statistical Analysis Scripts

Python scripts for weighting and Fusion

Visualization plugins and libraries for results

Unified compliance matrix for trust levels

Randomiation scripts for data generation

Resource utilization commands for experiments

### Repository Structure

zero-trust-DCTA /

├── venv/           # DTCA implementations and model files

├── _pycache_/          # precompiled files and utils

├── test_results/          # base model results

├── test_results_time/          # basemodel with linear time decay

├── test_results_time_exp/       # basemodel with exponential time decay

└── test_results_time_ensemble/          # Ensemble of base model short-term and long-term decay