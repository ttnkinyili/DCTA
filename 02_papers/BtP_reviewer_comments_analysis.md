# Reference List Aptness Review

## Summary

| Category | Count | References |
|:---|:---:|:---|
| ✅ Strong / Verified | 28 | [1]–[6], [10]–[13], [17], [19], [21], [22], [25], [27]–[33], [35], [37]–[39], [41]–[43] |
| 🟡 Acceptable (lower-tier or grey lit) | 8 | [7], [8], [9], [14], [15], [16], [20], [34] |
| 🟡 Marginal relevance | 2 | [23] (Fintech trust), [26] (2017 aeronautical, old/weak) |
| 🔴 Problematic — should replace/remove | 4 | [24], [36], [40], [44] |

---

## Detailed Assessment

### ✅ Strong / Verified References

| # | Ref | Assessment | Apt For |
|:---:|:---|:---|:---|
| 1 | Rose et al. (2020) NIST SP 800-207 | Essential standard | §5: NIST critique |
| 2 | IBM Security (2024) | Essential data source | §1, §3: breach statistics |
| 3 | CISA AA24-038A (2024) | Verified advisory — note: specifically about PRC state actors, not generic VPN exploitation | §3: VPN credential exploitation |
| 5 | Buck et al. (2022) *Comput. & Security* | Verified, highly cited ZTA MLR | §1, §4, §6: ZTA gaps |
| 6 | Aaqib et al. (2025) *Neural Comput. Appl.* | Verified, directly relevant — DS fusion + trust + IoT | §8: DS fusion resolution |
| 10 | Sandhu et al. (1996) | Classic RBAC reference | §4: RBAC |
| 11 | Das et al. (2021) *PeerJ CS* | Verified, RBAC microservices | §4: RBAC role explosion |
| 12 | Iqal et al. (2023) *IEEE Access* | Verified, IoT access control survey | §4: RBAC limitations in IoT |
| 13 | Meng et al. (2022) *China Commun.* | Verified, continuous auth without trust authority | §5: NIST gaps |
| 17 | Wang et al. (2022) *IEEE COMST* | Verified, highly relevant trust models survey | §1, §3: heterogeneous trust challenges |
| 19 | Syed et al. (2022) *IEEE Access* | Verified, comprehensive ZTA survey | §1, §5: ZTA gaps |
| 21 | Harshavardini & Bertia (2025) IEEE conf | Verified, SDN/SDP/ZT framework | §6, §7: SDP + SDN |
| 22 | Wang et al. (2025) *Cybersecurity* | Verified, dynamic ZT access control | §5: NIST resolution |
| 25 | Mekdad et al. (2023) *Comput. Networks* | Verified, UAV/heterogeneous security | §7: heterogeneous attack surfaces |
| 27 | CSA SDP Spec v2.0 (2022) | Essential standard | §6: SDP critique |
| 28 | Moubayed et al. (2019) *IEEE Network* | Verified, SDP state of art | §6: SDP analysis |
| 29 | Jeong & Yang (2025) *Applied Sciences* | Verified, trust score ZTA — highly relevant | §8: trust scoring resolution |
| 30 | Smiliotopoulos et al. (2024) *Heliyon* | Verified, lateral movement detection | §3: lateral movement |
| 31 | CSA SDP Arch Guide V3 (2025) | CSA publication | §6: SDP architecture |
| 32 | CSA SDP Arch Guide (2019) | CSA publication | §6: SDP architecture |
| 33 | Lefebvre et al. (2021) IEEE NFV-SDN | Verified, building SDP | §6: SDP implementation |
| 35 | Ali et al. (2020) IEEE DASC | Verified, adversarial IDS — key §7 reference | §7: AI-IDS adversarial attacks |
| 37 | Ji et al. (2023) *Information Sciences* | Verified, weighted DS fusion — directly relevant | §8: DS fusion mechanism |
| 38 | Shafer (1976) | Essential DS theory | §7, §8: DS framework |
| 39 | Yan et al. (2015) *IEEE COMST* | Verified, SDN/DDoS survey | §7: SDN vulnerabilities |
| 41 | Saltzer & Schroeder (1975) | Classic security principles | §8: separation of privilege |
| 42 | Jøsang (2016) | Essential subjective logic | §8: uncertainty representation |
| 43 | Wang et al. (2018) IEEE SmartWorld | Verified, time decay trust — directly relevant | §8: temporal decay mechanism |

### 🟡 Acceptable References (Use With Awareness)

| # | Ref | Issue | Recommendation |
|:---:|:---|:---|:---|
| 4 | Lefebvre et al. (2022) IEEE CNS | ✅ Verified conference paper | Use — good SDP/SDN integration reference |
| 7 | Verma (2025) IJCTT | Lower-tier journal but has DOI | Acceptable for cloud-native ZTA point |
| 8 | Adorno (2025) Zscaler blog | Vendor blog, not peer-reviewed | Acceptable as supplementary industry source only |
| 9 | Lev & Black (2025) Akamai blog | Vendor blog, not peer-reviewed | Acceptable as supplementary industry source only |
| 14 | Nasiruzzaman et al. (2025) IEEE conf | Verified conference paper | Use — good ZTA evolution reference |
| 15 | Mohseni-Ejiyeh (2023) arXiv | **Preprint, not peer-reviewed** | Acceptable only if no better alternative; flag as preprint |
| 16 | Pule et al. (2026) *Applied Sciences* | MDPI journal, DOI present | Acceptable — note 2026 date |
| 18 | Thirumalairai & Pradeesh (2024) IEEE conf | Verified conference paper | Use for SDN trust |
| 20 | Wu et al. (2024) *Heliyon* | Verified, IoT observability | Marginal relevance but acceptable |
| 34 | Pagadala-Sekar (2025) WJAETS | Lower-tier journal | Acceptable for SDP/ZT integration point |

### 🔴 Problematic References — Replace or Remove

| # | Ref | Issue | Recommendation |
|:---:|:---|:---|:---|
| **23** | Jafri et al. (2023) *Heliyon* — Fintech trust | **Irrelevant topic** — about trust in Fintech banking, not network security | **Remove** — does not support any claim in this paper |
| **24** | Hassan & Sanni (2026) — XAI ZT critical infrastructure | **No venue, no DOI, no publisher specified** — appears unpublished/preprint | **Remove or replace** with a published XAI+ZT reference |
| **26** | Suman & Rani (2017) *IJCST* — Aeronautical data comm | **Old (2017), very low-tier journal** (no impact factor) | **Remove** — [25] (Mekdad 2023) covers the same ground better |
| **36** | Thorne et al. (2026) — Adversarial attacks IDS | **No venue, no DOI, no publisher** — appears unpublished | **Remove or replace** — [35] (Ali 2020) already covers this |
| **40** | IEEE Communications Society (2024) — SDN security | **Suspicious authorship** — IEEE COMST does not publish papers authored by "IEEE Communications Society"; no DOI; likely fabricated | **Remove** — [39] (Yan 2015) covers SDN security |
| **44** | Johnson (2024) — VPN to SDP migration | **Not found in any database**; generic author name; no DOI | **Remove** — [4], [8], [9] cover VPN→SDP transition |

---

## Mapping to Paper Sections

| Paper Section | Best References from This List |
|:---|:---|
| §1 Introduction | [1], [2], [3], [5], [17], [19] |
| §2 Methodology | [5], [19] (as methodological models) |
| §3 Perimeter Dissolution | [2], [3], [7], [8], [9], [17], [30] |
| §4 Static RBAC | [10], [11], [12], [13], [14], [15] |
| §5 NIST SP 800-207 | [1], [5], [19], [22], [29] |
| §6 CSA SDP | [4], [27], [28], [31], [32], [33], [34], [21] |
| §7 AI-IDS in SDN | [35], [25], [38], [39], [18] |
| §8 Resolution | [6], [37], [38], [42], [43], [41], [29] |
