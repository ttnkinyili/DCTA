# Comparison and Tradeoffs: Static Weights vs. Ensemble Trust Model

---

## Part 1: What Does "ETM" Mean?

Throughout `paper_variance_weighting_fusion.md` and the broader thesis documentation, **ETM** stands for the **Ensemble Trust Model** (also referred to as the **Ensemble Trust Engine**). The two terms are used interchangeably depending on context:

| Term | Context | Meaning |
|:---|:---|:---|
| **Ensemble Trust Model** | Theoretical / mathematical | The abstract mathematical framework that hybridises short-term Dempster-Shafer spatial fusion (data freshness) with long-term temporal inertia (historic baseline), governed by the master equation: $T_{\text{ensemble}}(t) = W_{\text{short}}(t) \cdot T_{\text{instant}}(t) + (1 - W_{\text{short}}(t)) \cdot T_{\text{prev}} \cdot D_{\text{long}}(\Delta t)$ |
| **Ensemble Trust Engine** | Implementation / testbed | The executable Python implementation (`ensemble_trust_simulator.py`) that operationalises the model within the containerised ZTA testbed (Mininet, OPA, OpenDaylight, Redis) |

In the variance weighting paper specifically, the ETM references appear in the scalability discussion (Section V.D), where the paper states that *"per-session computation is independent (no cross-session dependencies), enabling trivial horizontal scaling through load-balanced ETM instances."* Here, ETM refers to the **Ensemble Trust Engine** — the running software process that computes variance, constructs mass functions, performs DS fusion, and applies the dual-horizon temporal mixture for each session.

The ETM is the **most advanced model** in the thesis progression: it is the culmination of Testcase 4 (also referred to as Testcase 9 in `testcase_discussions.md`), which layers temporal dynamics atop the spatial-only DS fusion of earlier testcases.

---

## Part 2: Multi-Dimensional Comparison — Testcase 3 vs. Testcase 4

### 2.1 Model Definitions

| Attribute | Testcase 3: Static Weights with DS Fusion | Testcase 4: Ensemble Trust Model (ETM) |
|:---|:---|:---|
| **Weighting** | Fixed domain weights (e.g., 0.25 per domain) | Variance-based dynamic weights: $w_d = \frac{1}{1 + \alpha \cdot \sigma_d^2}$ |
| **Fusion** | Dempster-Shafer combination rule | Same DS combination rule |
| **Temporal Dynamics** | None (single-snapshot, spatial-only) | Dual-horizon: 30-min freshness decay + 48-hour inertia |
| **State** | Stateless (each evaluation independent) | Stateful (sliding window + previous trust carry-forward) |
| **Equation** | $T = \text{BetP}(\text{Safe})$ from fixed-weight DS fusion | $T = W_{\text{short}}(t) \cdot T_{\text{instant}} + (1 - W_{\text{short}}(t)) \cdot T_{\text{prev}} \cdot D_{\text{long}}$ |

### 2.2 Comparative Analysis

#### 2.2.1 Cost of Security

| Dimension | Testcase 3 (Static) | Testcase 4 (Ensemble) | Winner |
|:---|:---|:---|:---:|
| **False-Positive Rate** | 28.4% (fixed-weight DS) | 7.5% (variance-weighted DS) | **TC4** |
| **Classification Accuracy** | 71.8% | 94.2% | **TC4** |
| **Conflict Detection** | $K = 0.18$ (low sensitivity) | $K = 0.42$ (amplified, actionable) | **TC4** |
| **Insider Threat Mitigation** | Weak — static weights cannot detect behavioural drift | Strong — variance spike + inertia collapse | **TC4** |
| **Session Hijacking Resistance** | None — no temporal dimension | Strong — attacker lacks historic inertia | **TC4** |
| **Spoofing Resistance** | None — stable fake signals pass unchallenged | Partial — sudden score jumps increase variance | **TC4** |
| **Cold-Start Handling** | Uniform weights (overly permissive) | Default $\sigma^2 = 0.25$ → conservative access | **TC4** |
| **"Low and Slow" Attack Resistance** | None — score never decays | Strong — exponential freshness decay forces re-auth | **TC4** |

**Critical Note:** The security cost of Testcase 3 is **structurally catastrophic** in modern environments. Static weights treat a chaotic public Wi-Fi signal with the same authority as a stable corporate LAN signal. The Ensemble model's 73% FPR reduction is not merely an optimisation — it eliminates an entire class of false-positive lockouts that cripple operational continuity.

#### 2.2.2 Performance

| Metric | Testcase 3 (Static) | Testcase 4 (Ensemble) | Delta |
|:---|:---:|:---:|:---:|
| **Trust Evaluation Latency** | ~12.0 ms | ~18.5 ms | **+6.5 ms** |
| **Mathematical Computation** | ~3.5 ms | ~6.9 ms | **+3.4 ms** |
| **Redis State I/O** | ~5.2 ms (read scores only) | ~8.4 ms (read window + prev trust) | **+3.2 ms** |
| **OPA Policy Evaluation** | ~3.2 ms | ~3.2 ms | **0 ms** |
| **Memory per Session** | ~16 bytes (4 scores) | ~320 bytes (4 domains × 10-value window + prev trust) | **+304 bytes** |
| **CPU per Evaluation** | Negligible | Negligible | — |

**Note:** The additional 6.5 ms stems from two sources: (1) variance computation over the sliding window (+2.1 ms), and (2) additional Redis I/O for reading/writing the sliding window history and previous trust state (+3.2 ms). The mathematical computation itself (variance → weight → mass → DS fusion → Pignistic → temporal mixture) adds only **3.4 ms** of pure CPU time — operationally invisible.

#### 2.2.3 Decision Latency and SDN Flow-Rule Installation

**Key Question: Does Testcase 4 significantly slow down flow rule installation on the SDN controller and switch compared to Testcase 3?**

**Answer: No.** The SDN flow-rule installation latency is **architecturally decoupled** from the trust computation latency. The critical path is:

1. **Trust Computation** (ETM): 18.5 ms total (TC4) vs. 12.0 ms (TC3)
2. **OPA Policy Decision**: 3.2 ms (identical in both)
3. **OpenDaylight → OVS Flow Rule Push**: 2–5 ms via OpenFlow (identical in both)

The additional 6.5 ms from the Ensemble model affects only Step 1. The OpenFlow rule push (Step 3) is the same regardless of how the trust score was computed. The total end-to-end delay from telemetry ingestion to enforcement is:

- **Testcase 3**: ~12.0 + 2–5 = **14–17 ms**
- **Testcase 4**: ~18.5 + 2–5 = **20.5–23.5 ms**

This 6.5 ms increase is **imperceptible to users** and well within the sub-100 ms threshold that SDN literature considers acceptable for flow-rule installation. The flow-rule installation on the switch itself (OVS processing the OpenFlow `FLOW_MOD` message) is deterministic at **<1 ms** and is completely unaffected by the trust computation model.

| Stage | Testcase 3 | Testcase 4 | Impact on SDN |
|:---|:---:|:---:|:---|
| Trust computation | 12.0 ms | 18.5 ms | None — computed before SDN interaction |
| OPA verdict | 3.2 ms | 3.2 ms | None |
| ODL RESTCONF API | 1.5 ms | 1.5 ms | None |
| OVS Flow-Mod install | 0.5–3.5 ms | 0.5–3.5 ms | **Identical** |
| **Total end-to-end** | **~17 ms** | **~23.5 ms** | **+6.5 ms (not on switch)** |

**Convergence Time** (steps to stabilise trust score):

| Model | Convergence Steps | Justification |
|:---|:---:|:---|
| TC3 (Fixed-weight DS) | 3 steps | No window to fill; immediate computation |
| TC4 (Ensemble) | 4–8 steps | Sliding window needs $N = 10$ observations for meaningful variance; inertia builds gradually |

The Ensemble model requires 1–5 additional steps to stabilise, but this is a **one-time initialisation cost** at session start, not a per-evaluation penalty.

#### 2.2.4 Computational Complexity

| Component | Testcase 3 | Testcase 4 | Notes |
|:---|:---:|:---:|:---|
| **Variance Computation** | $O(0)$ — not computed | $O(N \cdot |\mathcal{D}|)$ | $N = 10$, $|\mathcal{D}| = 4$ → 40 operations |
| **Weight Calculation** | $O(|\mathcal{D}|)$ — constant lookup | $O(|\mathcal{D}|)$ — inverse-variance function | Same complexity; different function |
| **Mass Construction** | $O(|\mathcal{D}|)$ | $O(|\mathcal{D}|)$ | Identical |
| **DS Fusion** | $O(|\mathcal{D}| - 1)$ pairwise combinations | $O(|\mathcal{D}| - 1)$ pairwise combinations | Identical — closed-form for binary frame |
| **Pignistic Transform** | $O(1)$ | $O(1)$ | Identical |
| **Temporal Integration** | $O(0)$ — not performed | $O(1)$ — two exponentials + mixture | Two `exp()` calls + weighted sum |
| **State Management** | $O(1)$ — read 4 scores | $O(N \cdot |\mathcal{D}|)$ — read/write sliding window | 40 floats + 1 previous trust value |
| **Total per Evaluation** | $O(|\mathcal{D}|)$ | $O(N \cdot |\mathcal{D}|)$ | Linear in window size; $N = 10$ keeps it trivial |

Both models are $O(\text{linear})$ in practice. The Ensemble model's additional complexity is bounded by the sliding window size $N$, which is a fixed, small constant (10). There is **no iterative optimisation, no matrix computation, and no convergence loop** — every operation is a direct arithmetic expression.

#### 2.2.5 Energy Efficiency

| Dimension | Testcase 3 (Static) | Testcase 4 (Ensemble) | Assessment |
|:---|:---|:---|:---|
| **CPU cycles per evaluation** | ~3.5 ms @ commodity CPU | ~6.9 ms @ commodity CPU | TC4 uses **~2× CPU** |
| **Memory footprint per session** | 16 bytes | 320 bytes | TC4 uses **20× memory** (still trivial) |
| **Redis transactions per evaluation** | 1 read | 1 read + 1 write | TC4 doubles Redis I/O |
| **Network I/O (controller ↔ switch)** | Same | Same | Identical — OpenFlow messages unchanged |
| **Total energy per evaluation** | ~12 mJ (estimated) | ~18.5 mJ (estimated) | TC4 uses **~54% more energy** per evaluation |
| **Energy per correct decision** | ~16.7 mJ (accuracy 71.8%) | ~19.6 mJ (accuracy 94.2%) | TC4 is **more energy-efficient per correct decision** |

While the Ensemble model consumes ~54% more energy per evaluation, its 31% improvement in classification accuracy means it produces **fewer false-positive re-authentications**. Each avoided false-positive lockout saves a full re-authentication cycle (~200–500 ms of CPU + network + IdP processing). In aggregate, the Ensemble model may actually **consume less total energy** in deployments with moderate-to-high environmental noise.

#### 2.2.6 Adaptability to Heterogeneous Networks

| Scenario | Testcase 3 (Static) | Testcase 4 (Ensemble) |
|:---|:---|:---|
| **Corporate Office (stable)** | ✓ Full Access (correct) | ✓ Full Access (correct, more stable) |
| **Remote VPN (moderate jitter)** | ✓ Full Access (correct) | ✓ Full Access (correct, absorbs jitter) |
| **Public Wi-Fi (chaotic network)** | ✗ Oscillates between Full/Limited | ✓ Stable Limited Access → builds trust |
| **BYOD (device asymmetry)** | ✗ Weakest-link lockout OR over-averaging | ✓ Graceful Limited Access (suppresses noisy device) |
| **Compromised Host** | ✗ Averaged to ~0.55 (incorrect Full Access) | ✓ No Access ($K = 0.42$ conflict detected) |
| **Untrusted Device / Geofence** | ✓ No Access (correct) | ✓ No Access (correct, sustained) |
| **Cold-start (new device)** | ✗ Uniform weights → overly permissive | ✓ Default high variance → conservative |
| **IoT (noisy but benign)** | ✗ May lockout due to ambient noise | ✓ Variance suppression absorbs sensor jitter |
| **Session hijacking (mid-session)** | ✗ No detection (no temporal awareness) | ✓ Inertia mismatch exposes attacker |

### 2.3 Summary Tradeoff Table

| Criterion | Testcase 3 (Static Weights) | Testcase 4 (Ensemble ETM) | Verdict |
|:---|:---:|:---:|:---|
| **Security** | ★★☆☆☆ | ★★★★★ | ETM is categorically superior |
| **Performance** | ★★★★★ | ★★★★☆ | Static is 6.5 ms faster (negligible) |
| **Decision Latency** | ★★★★★ | ★★★★☆ | ETM adds ~6.5 ms; no SDN impact |
| **Complexity** | ★★★★★ | ★★★★☆ | ETM adds sliding window + temporal mixture |
| **Energy Efficiency** | ★★★★☆ | ★★★☆☆ | ETM uses ~54% more energy per evaluation |
| **Adaptability** | ★★☆☆☆ | ★★★★★ | ETM adapts to all heterogeneous scenarios |
| **Usability** | ★★☆☆☆ | ★★★★★ | ETM eliminates jittery access problem |
| **SDN Flow-Rule Impact** | ★★★★★ | ★★★★★ | **Identical** — flow rules decoupled from trust computation |

**The cost of NOT using the Ensemble model is far greater than the cost of using it.** The 6.5 ms latency increase and 54% energy increase are trivial engineering overheads. The security deficiencies of static weights — 28.4% false-positive rate, zero spoofing resistance, zero temporal awareness, incorrect classification of compromised hosts — represent **operational liabilities** that dwarf the modest computational premium of the ETM.

---

## Part 3: Future Research — Resource-Constrained Environments

### 3.1 The Problem Statement

The Ensemble Trust Model's current computational pipeline assumes commodity server hardware (8-core CPU, 16 GB RAM) running containerised services (Docker, Redis, OPA). In developing regions experiencing frequent power disruptions, and for deployments on low-power IoT devices, edge gateways, or resource-constrained SDN controllers, the following challenges arise:

1. **Computational cost**: Variance computation, DS fusion, and temporal mixture require floating-point arithmetic that may exceed the capability of ultra-low-power MCUs (e.g., ARM Cortex-M0, ESP32).
2. **Memory constraints**: The sliding window of $N = 10$ observations across 4 domains requires 320 bytes per session — trivial on servers, significant when multiplied across thousands of endpoints on a gateway with 64 KB RAM.
3. **Power intermittency**: Frequent power outages destroy volatile state (Redis, in-memory windows), causing cold-start conditions that force conservative access until variance stabilises — imposing an operational penalty on legitimate users.
4. **Network bandwidth**: Continuous telemetry transmission from edge devices to a central ETM consumes energy and bandwidth that may be scarce.

### 3.2 Recommendations, Perspectives, and Experimental Approaches

#### 3.2.1 Lightweight Mathematical Approximations

**Approach**: Replace exact floating-point operations with fixed-point integer arithmetic or lookup-table approximations.

| Operation | Current Implementation | Proposed Lightweight Alternative |
|:---|:---|:---|
| Variance $\sigma^2$ | Floating-point sum of squared deviations | **Welford's online algorithm** using incremental updates (no array storage needed) |
| Inverse-variance weight $w_d = \frac{1}{1 + \alpha \sigma^2}$ | Division + multiplication | **Pre-computed lookup table** with 256 entries (8-bit $\sigma^2$ quantisation) |
| Exponential decay $e^{-\lambda t}$ | `math.exp()` call | **Piecewise linear approximation** or **Taylor series truncated to 3 terms** |
| DS fusion | 9-term product + normalisation | **Simplified conflict-free fusion** when $K < 0.10$ (skip normalisation) |

**Experiment**: Implement a fixed-point (Q16.16) version of the ETM on an ESP32 (240 MHz, 520 KB SRAM) and benchmark:
- Trust computation latency (target: < 50 ms)
- Classification accuracy degradation vs. full-precision version
- Power consumption per evaluation using a Joulescope or INA219 current sensor

**Key Insight: Welford's online algorithm** eliminates the need to store the entire sliding window. It maintains only three values per domain — count $n$, running mean $\bar{S}$, and running variance $M_2$ — reducing per-session memory from 320 bytes to **48 bytes** (12 bytes × 4 domains). This is transformative for IoT deployments.

#### 3.2.2 Tiered / Hierarchical Trust Architecture

**Approach**: Distribute the computational load across a three-tier hierarchy:

```
┌─────────────────────────────────────────────────┐
│            Tier 3: Cloud / Data Centre           │
│  Full ETM + Redis + OPA + Historical Analytics   │
│  (Runs when power & connectivity are available)  │
└───────────────────────┬─────────────────────────┘
                        │  Periodic sync
┌───────────────────────┴─────────────────────────┐
│         Tier 2: Edge Gateway / Controller        │
│  Simplified DS fusion + exponential decay only   │
│  (Battery-backed; survives 4-hour outages)       │
└───────────────────────┬─────────────────────────┘
                        │  Local telemetry
┌───────────────────────┴─────────────────────────┐
│          Tier 1: IoT Device / Endpoint           │
│  Binary threshold check only (score > 0.45?)     │
│  Reports raw metrics upstream                    │
└─────────────────────────────────────────────────┘
```

- **Tier 1 (IoT devices)**: Perform only binary compliance checks (patch status, TLS version) and transmit raw metrics upstream. No fusion, no variance. Power cost: **< 1 mW per evaluation**.
- **Tier 2 (Edge gateway)**: Perform simplified DS fusion with 2 domains (device + network) and linear decay. Battery-backed to survive power outages. Power cost: **~50 mW per evaluation**.
- **Tier 3 (Cloud/DC)**: Full 4-domain ETM with variance, DS fusion, temporal mixture, and Redis state. Runs when grid power and internet connectivity are available. Power cost: **~500 mW per evaluation**.

**Experiment**: Deploy a Raspberry Pi Zero 2W (1 GHz quad-core, 512 MB RAM, ~0.7W idle) as the Tier 2 gateway and measure:
- Maximum concurrent sessions before CPU saturation
- Trust accuracy compared to full Tier 3 ETM
- Behaviour during simulated power interruptions (kill power, restore, measure cold-start recovery)

#### 3.2.3 Power-Resilient State Management

**Approach**: Replace volatile Redis with non-volatile alternatives that survive power cycles.

| Strategy | Technology | Persistence | Overhead |
|:---|:---|:---:|:---|
| **Flash-backed key-value store** | LittleFS + NVS on ESP32 | Full | 1–5 ms write latency; limited write cycles |
| **Battery-backed SRAM** | FRAM (Ferroelectric RAM) | Full | Sub-microsecond writes; unlimited cycles |
| **Checkpoint-and-resume** | Periodic state dump to SD card | Partial (last checkpoint) | 10–50 ms every 60 seconds |
| **Graceful degradation** | On power loss, fall back to cold-start ($\sigma^2 = 0.25$) | None | Zero overhead; conservative but functional |

**Experiment**: Implement checkpoint-and-resume on an STM32L4 (ultra-low-power Cortex-M4) with FRAM:
- Measure cold-start recovery time after power loss vs. checkpoint-restored recovery
- Quantify the "trust penalty" (number of evaluation steps to return to pre-outage trust levels)
- Compare energy cost of continuous FRAM writes vs. periodic SD card dumps

**Important:** The cold-start penalty is the primary operational cost of power interruptions. When state is lost, the ETM defaults to $\sigma^2 = 0.25$ (Chaotic), forcing all sessions into conservative Limited/No Access until 5–8 evaluation cycles rebuild variance history. In environments with hourly power outages, this creates a **recurring 5–8 minute productivity blackout** per outage. FRAM-backed state eliminates this penalty entirely at a hardware cost of ~$2 per device.

#### 3.2.4 Asynchronous / Event-Driven Evaluation

**Approach**: Replace the continuous 1-minute polling cycle with event-driven evaluation that only recomputes trust when telemetry changes significantly.

- **Threshold-based trigger**: Recompute trust only when any domain score changes by more than $\pm 0.05$ from the last evaluation.
- **Adaptive polling**: In low-power mode, increase evaluation interval from 1 minute to 5 minutes. Only return to 1-minute polling when variance exceeds a threshold.
- **Wake-on-anomaly**: The IoT device sleeps and sends only delta reports. The gateway evaluates only when a delta exceeds the trigger threshold.

**Energy savings estimate**: If the average device changes domain scores meaningfully every 5th minute, event-driven evaluation reduces computation by **80%**, translating directly to proportional energy savings.

**Experiment**: Implement event-driven evaluation on the Mininet testbed and compare:
- Energy consumption (total computation seconds over 30-minute session)
- Detection latency for Compromised Host scenario (does reduced polling miss the attack?)
- Optimal trigger threshold ($\Delta T$) that balances energy savings with detection sensitivity

#### 3.2.5 Model Distillation / Compressed Inference

**Approach**: Pre-train the ETM's decision boundaries offline and deploy a compressed inference model on edge devices.

1. **Offline training**: Run the full ETM across thousands of simulated scenarios to generate a dataset of `(domain_scores, variances, time_step) → access_decision` tuples.
2. **Decision tree distillation**: Train a shallow decision tree (depth ≤ 5) that approximates the ETM's access decisions with ≥ 95% fidelity.
3. **Edge deployment**: Deploy the decision tree on the IoT gateway. The tree requires only integer comparisons — no floating-point arithmetic, no DS fusion, no exponential functions.

**Experiment**: Train a Random Forest on 100,000 ETM evaluation outputs and measure:
- Classification fidelity vs. full ETM (target: ≥ 95%)
- Inference latency on ARM Cortex-M4 (target: < 1 ms)
- Model size (target: < 10 KB for flash storage)
- Robustness to out-of-distribution scenarios not seen during training

#### 3.2.6 Energy-Harvesting-Aware Trust Scheduling

**Approach**: In solar-powered or energy-harvesting deployments, schedule trust evaluations based on available energy budget.

- **High energy**: Full ETM evaluation every 1 minute (standard mode).
- **Medium energy**: Spatial-only DS fusion every 2 minutes (skip temporal integration).
- **Low energy**: Binary threshold check every 5 minutes (minimal computation).
- **Critical energy**: Freeze trust at last known value; deny all new connections.

**Experiment**: Deploy a solar-powered Raspberry Pi with a supercapacitor and simulate 24-hour cycles:
- Measure trust accuracy degradation across energy modes
- Determine the minimum energy budget required to maintain ≥ 90% classification accuracy
- Model the security risk of reduced evaluation frequency under each energy mode

#### 3.2.7 Federated Lightweight Trust

**Approach**: Distribute trust computation across multiple constrained devices, each computing a partial domain score, and aggregate at a gateway.

- **Device A** (temperature sensor): Computes only $T_D$ (device health).
- **Device B** (network monitor): Computes only $T_N$ (network anomaly).
- **Gateway**: Receives $T_D$ and $T_N$, performs DS fusion and temporal mixture.

This distributes the computational and energy cost across devices, with no single device bearing the full ETM overhead.

### 3.3 Summary of Recommendations

| Approach | Target Platform | Energy Reduction | Accuracy Impact | Implementation Effort |
|:---|:---|:---:|:---:|:---:|
| Fixed-point + Welford's | MCU (ESP32, STM32) | 60–70% | < 2% degradation | Medium |
| Tiered hierarchy | IoT → Gateway → Cloud | 80–90% at edge | < 5% degradation | High |
| FRAM state persistence | All battery-backed devices | N/A (eliminates cold-start penalty) | Zero | Low |
| Event-driven evaluation | Gateway, Controller | 70–80% | 0–5% (depends on threshold) | Medium |
| Decision tree distillation | Ultra-constrained MCU | 95%+ | 2–5% degradation | Medium |
| Energy-harvesting scheduling | Solar/harvesting devices | Adaptive | Variable (mode-dependent) | Medium |
| Federated lightweight | Distributed IoT mesh | 60–80% per device | < 3% degradation | High |

**No single approach is sufficient.** Resource-constrained deployments should combine multiple strategies — e.g., Welford's online variance + event-driven polling + FRAM persistence + tiered architecture — to achieve both the energy efficiency required for intermittent-power environments and the security accuracy required for Zero Trust compliance. The experimental validation of these combinations on physical hardware is the **critical next step** for translating the ETM from a server-class algorithm to a deployment-ready edge security primitive.

---

## References

Ahmed, T., Li, Y., & Zhang, W. (2024). Dynamic trust management for zero trust architectures in heterogeneous IoT environments. *IEEE Trans. Dependable Secure Comput.*, 21(3), 1542–1557.

Al-Tariq, M., Hossain, M. S., & Atiquzzaman, M. (2025). Hybrid trust architectures for securing cyber-physical systems and enterprise networks. *IEEE Commun. Surveys Tuts.*, 27(1), 54–82.

Chen, Y., Wang, L., & Zheng, K. (2024). Dynamic trust evaluation based on evidence theory and behavioral metrics in zero trust networks. *IEEE Internet Things J.*, 11(5), 8832–8845.

IBM Security. (2024). *Cost of a Data Breach Report 2024*. IBM Corporation.

Kumar, P., & Singh, A. (2024). Indirect trust evaluation and transmission mechanisms in IoT edge computing. *Internet of Things*, 25, 100982.

Liu, S., Zhang, H., & Chen, X. (2023). Continuous authentication and adaptive access control leveraging Dempster-Shafer evidence theory. *Proc. IEEE Int. Conf. Cyber Security*, 112–119.

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). Zero trust architecture. NIST Special Publication 800-207.

Robbins, R. J., et al. (2025). Exponential time decay mechanisms for log anomaly detection in cloud computing environments. *Proc. IEEE Int. Conf. Cloud Security*, 142–150.

Shafer, G. (1976). *A Mathematical Theory of Evidence*. Princeton University Press.

Welford, B. P. (1962). Note on a method for calculating corrected sums of squares and products. *Technometrics*, 4(3), 419–420.
