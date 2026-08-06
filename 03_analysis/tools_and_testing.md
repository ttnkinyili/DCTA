# Tools and Testing Reference: DCTA Zero Trust Testbed

> **Companion to:** *A Reproducible, Lightweight Zero Trust Testbed for Validating Dynamic Trust Models Based on Virtualization, Emulation, and Simulation*
> **Date:** 23 July 2026

---

## 1. Overview

This document catalogues the tools, utilities, and benchmarking instruments required to test, measure, and validate the performance, scalability, and correctness of the DCTA Zero Trust testbed. Tools are organised into three tiers:

1. **Testbed Infrastructure** — components that form the testbed itself and produce intrinsic metrics.
2. **Benchmarking & Measurement Utilities** — external tools used to generate load, measure latency, and capture system-level metrics.
3. **Analysis & Validation** — statistical and visualisation tools used to process experimental outputs.

Each entry specifies the tool's role, the metrics it measures, and its relevance to the testbed's evaluation objectives.

---

## 2. Testbed Infrastructure Components

These are the core components of the testbed that double as sources of performance telemetry and test instrumentation.

| Tool | Role in Testbed | Metrics Produced | Licence |
|:---|:---|:---|:---|
| **Docker / Docker Compose** | Container orchestration for IdP, PDP, PA, PEP services | Container startup time, resource isolation, image sizes | Apache 2.0 |
| **Mininet** | SDN network emulation; creates lightweight hosts and OVS switches via Linux namespaces | Emulated link latency, bandwidth, packet loss; host-to-host RTT; topology scalability | BSD-style |
| **Open vSwitch (OVS) 3.3.4** | L3/L4 Policy Enforcement Point; OpenFlow-based micro-segmentation | Flow rule install latency (2–5 ms), flow table sizes, per-flow packet/byte counters | Apache 2.0 |
| **OpenDaylight (Fluorine)** | SDN controller / Policy Administrator; translates trust verdicts to OpenFlow rules | RESTCONF API response time, flow rule installation latency, controller CPU/memory | EPL 1.0 |
| **Keycloak 24.x** | Identity Provider (IdP); OIDC/SAML authentication, JWT issuance | Authentication latency, token issuance time, concurrent session handling | Apache 2.0 |
| **Open Policy Agent (OPA)** | Policy Decision Point; evaluates Rego policies against trust scores | Policy evaluation latency (measured at 3.2 ms), decision throughput (req/s) | Apache 2.0 |
| **Envoy Proxy** | L7 Policy Enforcement Point; application-layer request filtering, JWT validation | Request latency, upstream/downstream connection counts, L7 filter processing time | Apache 2.0 |
| **Redis 7.x** | Session state store; sliding window maintenance, variance tracking | State read/write I/O latency (measured at 8.4 ms), memory consumption, ops/sec | BSD 3-Clause |
| **GNS3** (optional) | Full-system hardware emulation for high-fidelity device/service emulation (Cisco IOS, legacy OS) | Device boot time, forwarding latency, protocol compliance | GPL v3 |
| **Python 3.12 (Trust Engine)** | Ensemble Trust Engine implementation; variance computation, DS fusion, temporal integration | Per-component computation latency (6.9 ms mathematical core), trust score convergence time | PSF |

---

## 3. Network Performance & Latency Testing Tools

These tools are used to benchmark network performance, measure latency, Round-Trip Time (RTT), bandwidth, and packet loss within the emulated Mininet topology and between containerised services.

### 3.1 iperf / iperf3

| Attribute | Detail |
|:---|:---|
| **Tool** | `iperf3` (preferred) / `iperf` |
| **Purpose** | Network bandwidth and throughput measurement between testbed hosts |
| **Metrics** | TCP/UDP throughput (Mbps/Gbps), jitter, packet loss rate, retransmissions |
| **Relevance** | Validates Mininet link bandwidth configurations (1 Gbps corporate, 10–100 Mbps remote); measures data-plane throughput under varying trust-enforcement flow rules; stress-tests OVS forwarding performance under load |
| **Usage Context** | Run between Mininet hosts to verify configured link characteristics; measure throughput degradation when OVS flow rules are actively enforced vs. baseline (no-policy) |
| **Example** | `iperf3 -s` (server on h1), `iperf3 -c <h1_ip> -t 30 -i 1` (client on h2) |
| **Install** | `sudo apt install -y iperf3` |

### 3.2 hping3

| Attribute | Detail |
|:---|:---|
| **Tool** | `hping3` |
| **Purpose** | Advanced packet crafting and RTT/latency measurement; TCP/UDP/ICMP probing with microsecond precision |
| **Metrics** | RTT per packet (min/avg/max), packet loss, TCP handshake latency, SYN flood simulation for stress testing |
| **Relevance** | Measures precise RTT between Mininet hosts across different network segments (Corporate 2 ms, DMZ 5 ms, Remote 20–200 ms); validates OVS flow rule enforcement latency by timing TCP SYN-ACK responses before and after policy changes; simulates adversarial traffic patterns (SYN floods) to test breach detection response time |
| **Usage Context** | Precision latency profiling across the three-tier topology; verifying that flow rule modifications by OpenDaylight are reflected in packet-level timing; testing trust engine response to anomalous traffic patterns |
| **Example** | `hping3 -S -p 80 -c 100 <target_ip>` (100 SYN packets), `hping3 --traceroute -S -p 80 <target_ip>` |
| **Install** | `sudo apt install -y hping3` |

### 3.3 ping / fping

| Attribute | Detail |
|:---|:---|
| **Tool** | `ping` (standard), `fping` (parallel multi-host) |
| **Purpose** | Basic ICMP RTT measurement and host reachability validation |
| **Metrics** | RTT (min/avg/max/mdev), packet loss percentage, host availability |
| **Relevance** | Baseline connectivity verification across Mininet topology (`pingall`); continuous RTT monitoring during trust evaluation cycles; validates that access revocation (No Access) results in host unreachability; `fping` enables parallel probing of all hosts in scalability tests (6 to 50+ hosts) |
| **Usage Context** | Pre-test baseline validation; post-policy-enforcement reachability checks; RTT monitoring during breach containment timing experiments |
| **Example** | `ping -c 100 -i 0.1 <target_ip>`, `fping -g 10.0.0.0/24 -c 10` |
| **Install** | `sudo apt install -y fping` (ping is pre-installed) |

### 3.4 tc (Traffic Control) / netem

| Attribute | Detail |
|:---|:---|
| **Tool** | `tc` with `netem` (Network Emulator) — part of `iproute2` |
| **Purpose** | Configurable network impairment: latency injection, bandwidth shaping, packet loss, jitter simulation |
| **Metrics** | Configured impairments (delay, loss, bandwidth); validates that Mininet's TCLink parameters are correctly applied |
| **Relevance** | Essential for configuring the Remote Segment's variable conditions (20–200 ms latency, 0–5% packet loss); simulates Public Wi-Fi degradation scenarios; enables controlled testing of how network impairment affects trust score variance and the variance-based weighting mechanism ($w_d = 1/(1 + \alpha \sigma^2)$) |
| **Usage Context** | Applied to Mininet links via TCLink class; independently verified with `tc -s qdisc show` to confirm impairment parameters |
| **Example** | `tc qdisc add dev eth0 root netem delay 100ms 20ms loss 2%` |
| **Install** | Pre-installed with `iproute2` |

### 3.5 traceroute / mtr

| Attribute | Detail |
|:---|:---|
| **Tool** | `traceroute`, `mtr` (My Traceroute — combines ping and traceroute) |
| **Purpose** | Path analysis and per-hop latency measurement through the emulated topology |
| **Metrics** | Per-hop RTT, packet loss per hop, path changes after flow rule modification |
| **Relevance** | Validates the three-tier topology (Core → Corporate/DMZ/Remote) routing; verifies that SDN flow rule changes by OpenDaylight actually alter packet paths; `mtr` provides continuous path monitoring during trust evaluation to correlate latency spikes with trust score changes |
| **Usage Context** | Topology validation; path verification after micro-segmentation enforcement |
| **Example** | `mtr --report --report-cycles 50 <target_ip>` |
| **Install** | `sudo apt install -y mtr-tiny traceroute` |

---

## 4. System Resource & Utilisation Monitoring Tools

These tools measure CPU, memory, and I/O utilisation of the host system and containerised services — both at baseline (before models run) and under load.

### 4.1 vmstat

| Attribute | Detail |
|:---|:---|
| **Tool** | `vmstat` (Virtual Memory Statistics) |
| **Purpose** | Real-time system-level resource monitoring: CPU, memory, swap, I/O, context switches |
| **Metrics** | CPU utilisation (user/system/idle/wait), free/used/swap memory, block I/O, interrupts, context switches per second |
| **Relevance** | Captures baseline resource utilisation **before** any trust models are running (paper reports ~3.2 GB RAM, 10–15% CPU at idle); monitors resource consumption **during** trust evaluation across 6 scenarios; identifies CPU saturation during scalability tests (6 → 50 → 100 concurrent sessions); validates the paper's claim of 35–40% peak CPU at 100 sessions |
| **Usage Context** | Run continuously during all test phases: baseline (idle testbed), warm-up (services starting), active evaluation (scenario execution), and stress (scalability testing) |
| **Example** | `vmstat 1 300 > vmstat_baseline.log` (1-second intervals for 5 minutes) |
| **Install** | Pre-installed (part of `procps`) |

### 4.2 top / htop

| Attribute | Detail |
|:---|:---|
| **Tool** | `top` (standard), `htop` (interactive, visual) |
| **Purpose** | Per-process CPU and memory monitoring; identifies resource-heavy containers and processes |
| **Metrics** | Per-process CPU %, memory (RES/VIRT/SHR), thread counts, load average |
| **Relevance** | Identifies which testbed component (OPA, Keycloak, OpenDaylight, Redis, Trust Engine) consumes the most resources; monitors per-container overhead; validates that the trust engine's Python process remains lightweight during evaluation |
| **Usage Context** | Real-time observation during test runs; batch-mode logging for post-test analysis |
| **Example** | `top -b -n 60 -d 1 > top_output.log` (batch mode, 60 snapshots at 1s intervals) |
| **Install** | `sudo apt install -y htop` (top is pre-installed) |

### 4.3 docker stats

| Attribute | Detail |
|:---|:---|
| **Tool** | `docker stats` |
| **Purpose** | Container-specific resource monitoring; CPU, memory, network I/O, and block I/O per container |
| **Metrics** | Per-container: CPU %, memory usage/limit, network I/O (Rx/Tx bytes), block I/O |
| **Relevance** | Isolates resource consumption per testbed component (Keycloak, OPA, OpenDaylight, Redis, Envoy); validates the paper's aggregate resource claims (3.2 GB idle, 4.1 GB at 100 sessions); identifies memory leaks or CPU spikes in specific containers during extended test runs |
| **Usage Context** | Run alongside all scenario executions; compare idle vs. loaded resource profiles |
| **Example** | `docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" > docker_stats.log` |
| **Install** | Included with Docker Engine |

### 4.4 mpstat

| Attribute | Detail |
|:---|:---|
| **Tool** | `mpstat` (part of `sysstat`) |
| **Purpose** | Per-CPU core utilisation reporting; identifies uneven load distribution |
| **Metrics** | Per-core CPU % (user, system, iowait, idle, irq, softirq) |
| **Relevance** | Validates that Mininet's network namespace processes distribute across cores; identifies CPU bottlenecks in specific cores during OpenDaylight flow processing or OPA policy evaluation; important for the 8-core recommended configuration |
| **Usage Context** | Parallel to vmstat during scalability tests |
| **Example** | `mpstat -P ALL 1 60 > mpstat_output.log` |
| **Install** | `sudo apt install -y sysstat` |

### 4.5 iostat

| Attribute | Detail |
|:---|:---|
| **Tool** | `iostat` (part of `sysstat`) |
| **Purpose** | Disk I/O performance monitoring; read/write throughput and queue depth |
| **Metrics** | Disk read/write (KB/s), I/O requests/sec, average queue length, await time (ms) |
| **Relevance** | Monitors Redis disk persistence overhead; validates that CSV/PNG output generation (results writing) doesn't bottleneck evaluation; identifies I/O contention during concurrent container operations |
| **Usage Context** | During data-intensive phases: Redis state persistence, result file generation, Docker image operations |
| **Example** | `iostat -x 1 60 > iostat_output.log` |
| **Install** | `sudo apt install -y sysstat` |

### 4.6 free

| Attribute | Detail |
|:---|:---|
| **Tool** | `free` |
| **Purpose** | Snapshot of system memory allocation: total, used, free, shared, buffers/cache, swap |
| **Metrics** | Total/used/free/available RAM and swap |
| **Relevance** | Quick pre-test and post-test memory comparison; validates the 16 GB recommendation and the 8 GB minimum claim; identifies memory pressure during large-scale topology runs |
| **Usage Context** | Captured at test start, mid-point, and end |
| **Example** | `free -h -s 5 -c 60 > memory_log.txt` (every 5s, 60 samples) |
| **Install** | Pre-installed (part of `procps`) |

### 4.7 /proc/stat and /proc/meminfo

| Attribute | Detail |
|:---|:---|
| **Tool** | Direct reads from `/proc/stat`, `/proc/meminfo`, `/proc/<pid>/status` |
| **Purpose** | Raw kernel-level CPU and memory statistics without tool overhead |
| **Metrics** | CPU jiffies per core, memory allocation breakdown (MemTotal, MemFree, Buffers, Cached, SwapTotal, SwapFree) |
| **Relevance** | Programmatic resource monitoring from Python test scripts; enables automated baseline capture before each scenario run; zero-overhead measurement for accurate resource profiling |
| **Usage Context** | Integrated into Python test orchestration scripts for automated pre/post measurement |
| **Example** | `cat /proc/meminfo | head -5`, or read programmatically from Python |
| **Install** | Kernel-provided; no installation needed |

---

## 5. Latency & Performance Profiling Tools

These tools provide fine-grained latency measurement and profiling of the trust evaluation pipeline.

### 5.1 Python time / timeit Modules

| Attribute | Detail |
|:---|:---|
| **Tool** | `time.perf_counter_ns()`, `timeit` module |
| **Purpose** | Microsecond-precision timing of individual trust engine computation stages |
| **Metrics** | Per-component latency: variance computation (2.1 ms), DS fusion (3.8 ms), Pignistic transformation (0.1 ms), temporal integration (0.2 ms), total pipeline (18.5 ms) |
| **Relevance** | Directly produces the latency breakdown reported in Table VII of the paper; enables reproducible measurement of each computational stage; validates the 20 ms engineering target |
| **Usage Context** | Instrumented within the trust engine code; captures per-evaluation timing across all 30 time steps × 6 scenarios |
| **Example** | `start = time.perf_counter_ns(); ... ; elapsed_ms = (time.perf_counter_ns() - start) / 1e6` |
| **Install** | Part of Python standard library |

### 5.2 cProfile / py-spy

| Attribute | Detail |
|:---|:---|
| **Tool** | `cProfile` (built-in profiler), `py-spy` (sampling profiler) |
| **Purpose** | Function-level profiling of the Python trust engine; identifies computational hotspots |
| **Metrics** | Per-function call count, cumulative time, time-per-call; flame graph visualisation |
| **Relevance** | Identifies which functions dominate the 6.9 ms mathematical core (variance computation, DS combination, Pignistic transformation); validates that the closed-form DS combination for binary frames avoids iterative overhead; detects performance regressions when extending the trust engine |
| **Usage Context** | Profiling runs during development and optimisation; flame graph generation for publication |
| **Example** | `python -m cProfile -o profile.out run_ensemble_scenarios.py`, `py-spy record -o profile.svg -- python run_ensemble_scenarios.py` |
| **Install** | `cProfile` is built-in; `pip install py-spy` |

### 5.3 curl / httpie

| Attribute | Detail |
|:---|:---|
| **Tool** | `curl` (with `-w` timing format), `httpie` |
| **Purpose** | HTTP request timing for OPA REST API, Keycloak token endpoints, and Envoy proxy |
| **Metrics** | DNS resolution time, TCP connect time, TLS handshake time, time-to-first-byte (TTFB), total request time |
| **Relevance** | Measures OPA policy evaluation latency (3.2 ms) via REST API; profiles Keycloak authentication latency; validates Envoy proxy request overhead; tests session setup latency (15–20 ms overhead reported) |
| **Usage Context** | Manual API testing; automated latency benchmarking of control-plane services |
| **Example** | `curl -w "@curl-format.txt" -s -o /dev/null http://localhost:8181/v1/data/trust/policy` |
| **Install** | `sudo apt install -y curl httpie` |

### 5.4 redis-benchmark

| Attribute | Detail |
|:---|:---|
| **Tool** | `redis-benchmark` |
| **Purpose** | Benchmark Redis state store performance; measures GET/SET operations per second |
| **Metrics** | Operations/second, latency percentiles (p50, p99, p99.9), throughput under concurrent connections |
| **Relevance** | Redis I/O dominates total evaluation latency (8.4 ms of 18.5 ms total); validates that Redis can sustain the required throughput for sliding window reads/writes across concurrent sessions; stress-tests Redis under scalability scenarios (100+ sessions) |
| **Usage Context** | Pre-test Redis performance validation; scalability testing with increasing concurrent connections |
| **Example** | `redis-benchmark -h localhost -p 6379 -n 10000 -c 50 -t get,set` |
| **Install** | `sudo apt install -y redis-tools` |

### 5.5 wrk / wrk2 / ab (Apache Bench)

| Attribute | Detail |
|:---|:---|
| **Tool** | `wrk` / `wrk2` (HTTP benchmarking), `ab` (Apache Bench) |
| **Purpose** | HTTP load generation and throughput/latency measurement for the control-plane REST APIs |
| **Metrics** | Requests/second, latency distribution (avg, stdev, max, percentiles), transfer rate, error rate |
| **Relevance** | Stress-tests OPA policy evaluation endpoint under concurrent trust evaluation requests; measures Envoy proxy throughput under high session counts; validates that the control plane sustains performance during scalability tests (10 → 50 → 100 concurrent sessions); identifies saturation points |
| **Usage Context** | Scalability testing of OPA, Keycloak, and Envoy endpoints |
| **Example** | `wrk -t4 -c100 -d30s http://localhost:8181/v1/data/trust/policy` |
| **Install** | `sudo apt install -y apache2-utils` (for ab); build `wrk` from source |

---

## 6. Network Monitoring & Telemetry Tools

### 6.1 tcpdump

| Attribute | Detail |
|:---|:---|
| **Tool** | `tcpdump` |
| **Purpose** | Packet capture and protocol analysis on Mininet interfaces and OVS ports |
| **Metrics** | Packet counts, protocol distribution, flow patterns, timing between packets |
| **Relevance** | Validates that OVS flow rules are correctly enforced (blocked traffic should produce no packets); captures breach containment timing (time between anomaly detection and last forwarded packet); provides ground-truth for RTT validation alongside ping/hping3 |
| **Usage Context** | Packet-level validation of micro-segmentation enforcement; breach containment timing measurement |
| **Example** | `tcpdump -i s1-eth1 -c 1000 -w capture.pcap` |
| **Install** | `sudo apt install -y tcpdump` |

### 6.2 Wireshark / tshark

| Attribute | Detail |
|:---|:---|
| **Tool** | `tshark` (CLI), `wireshark` (GUI) |
| **Purpose** | Deep packet inspection and protocol analysis; processes pcap files from tcpdump |
| **Metrics** | Protocol hierarchy statistics, conversation analysis, I/O graphs, TCP stream analysis, flow timing |
| **Relevance** | Detailed analysis of OpenFlow control messages between OVS and OpenDaylight; validates JWT tokens in HTTP requests through Envoy; measures SDP/SDN synchronisation delay (4.2 ms median reported) |
| **Usage Context** | Post-capture analysis of tcpdump files; OpenFlow message timing analysis |
| **Example** | `tshark -r capture.pcap -q -z io,stat,1` |
| **Install** | `sudo apt install -y tshark` |

### 6.3 OVS Flow Monitoring (ovs-ofctl / ovs-dpctl)

| Attribute | Detail |
|:---|:---|
| **Tool** | `ovs-ofctl`, `ovs-dpctl`, `ovs-vsctl` |
| **Purpose** | OpenFlow flow table inspection; flow rule statistics and timing |
| **Metrics** | Flow rule count, per-flow packet/byte counters, flow age, flow install/delete events, datapath statistics |
| **Relevance** | Directly measures flow rule installation latency (2–5 ms target); monitors flow table growth during scalability tests (up to 200 concurrent flows); validates that trust score changes result in correct flow modifications; measures SDN enforcement latency for breach containment timing |
| **Usage Context** | Continuous monitoring during all scenario executions |
| **Example** | `ovs-ofctl dump-flows s1`, `ovs-dpctl show`, `ovs-ofctl dump-ports s1` |
| **Install** | Included with Open vSwitch |

### 6.4 Zeek (Future Integration)

| Attribute | Detail |
|:---|:---|
| **Tool** | Zeek (formerly Bro) |
| **Purpose** | Passive network security monitoring; generates structured protocol metadata (conn, dns, ssl, http logs) |
| **Metrics** | Connection records, TLS parameters, DNS queries, file hashes, behavioural baselines |
| **Relevance** | Replaces simulated Gaussian telemetry with real network observation; feeds Network domain ($\mathcal{D}_N$) with actual anomaly detection scores and protocol compliance metrics; addresses Limitation 4 (simulated telemetry) of the paper |
| **Usage Context** | Deployed on Mininet mirror/SPAN port; future testbed extension |
| **Install** | `sudo apt install -y zeek` or from source |

### 6.5 Suricata (Future Integration)

| Attribute | Detail |
|:---|:---|
| **Tool** | Suricata |
| **Purpose** | Real-time IDS/IPS; signature-based and protocol anomaly detection |
| **Metrics** | Alert counts by severity, flow records, protocol anomaly events, EVE JSON output |
| **Relevance** | Provides ground-truth anomaly labels for validating trust engine classification accuracy; can operate in IPS mode for inline blocking complementary to OVS; feeds real threat detection events into the trust engine |
| **Usage Context** | Deployed alongside Zeek on mirror port; future testbed extension |
| **Install** | `sudo apt install -y suricata` |

---

## 7. Scalability Testing Tools

### 7.1 Mininet Scalability Testing (Built-in)

| Attribute | Detail |
|:---|:---|
| **Tool** | Mininet Python API with custom topology scripts |
| **Purpose** | Scale the emulated network from 6 to 50+ hosts; measure per-host overhead |
| **Metrics** | Host creation time, per-host memory overhead, ping convergence time across topology, OVS flow table scaling |
| **Relevance** | Validates linear scalability claim (0.2 ms per additional session); confirms OpenDaylight flow rule installation latency remains < 50 ms with 200+ flows; tests network namespace limits |
| **Usage Context** | Parametric scaling tests with increasing host counts |
| **Example** | Modify `topology.py` to iterate host counts: `for n in [6, 10, 20, 50, 100]: ...` |

### 7.2 stress-ng

| Attribute | Detail |
|:---|:---|
| **Tool** | `stress-ng` |
| **Purpose** | System stress testing: CPU, memory, I/O, and network stress generation |
| **Metrics** | Operations/second under stress, failure thresholds, resource exhaustion points |
| **Relevance** | Simulates resource-constrained environments (8 GB minimum RAM claim); stress-tests the trust engine under CPU contention; validates graceful degradation when host resources are limited |
| **Usage Context** | Boundary testing; minimum hardware validation |
| **Example** | `stress-ng --cpu 4 --vm 2 --vm-bytes 4G --timeout 60s` |
| **Install** | `sudo apt install -y stress-ng` |

---

## 8. Statistical Analysis & Validation Tools

These tools support the statistical methodology described in Section V.C of the paper.

### 8.1 Python Scientific Stack

| Tool | Role | Paper Usage |
|:---|:---|:---|
| **NumPy** | Variance computation, array operations | Sliding window variance ($\sigma^2$) calculation across 50 independent runs |
| **Pandas** | Data aggregation, CSV I/O, tabular analysis | Scenario result DataFrames; mean ± std reporting |
| **SciPy (scipy.stats)** | Statistical testing | Wilcoxon signed-rank test ($p < 0.01$); Cliff's delta effect size |
| **Matplotlib** | Trust trajectory visualisation | Trust evolution plots (PNG), decision zone overlays |

### 8.2 Jupyter Notebook (Optional)

| Attribute | Detail |
|:---|:---|
| **Tool** | Jupyter Notebook / JupyterLab |
| **Purpose** | Interactive exploration of experimental results; reproducible analysis notebooks |
| **Relevance** | Facilitates reproducible data analysis aligned with the paper's open-science objectives; enables researchers to independently verify statistical claims |

---

## 9. Metric-to-Tool Mapping Summary

| Metric Category | Specific Metric | Primary Tool(s) | Secondary/Validation Tool(s) |
|:---|:---|:---|:---|
| **Latency** | Per-evaluation pipeline latency (18.5 ms target) | `time.perf_counter_ns()` (Python) | `cProfile`, `py-spy` |
| **Latency** | OPA policy evaluation (3.2 ms) | `curl -w`, `wrk` | `tcpdump` (API timing) |
| **Latency** | Redis state I/O (8.4 ms) | `redis-benchmark` | `time.perf_counter_ns()` |
| **Latency** | Flow rule installation (2–5 ms) | `ovs-ofctl` | `hping3`, `tcpdump` |
| **Latency** | Session setup (15–20 ms overhead) | `curl -w`, `wrk` | `hping3` (TCP handshake) |
| **RTT** | Host-to-host RTT across topology | `ping`, `fping` | `hping3`, `mtr` |
| **RTT** | Per-hop latency in 3-tier topology | `mtr`, `traceroute` | `hping3 --traceroute` |
| **Performance** | Trust engine throughput (evaluations/sec) | `wrk`, `ab` | `cProfile` |
| **Performance** | OPA decision throughput | `wrk`, `ab` | `docker stats` |
| **Performance** | Network throughput (Mbps) | `iperf3` | `tc` (validation of configured BW) |
| **Scalability** | Linear overhead per session (0.2 ms) | Mininet API + Python timing | `vmstat`, `mpstat` |
| **Scalability** | Flow table scaling (200+ flows) | `ovs-ofctl dump-flows` | `docker stats` (ODL memory) |
| **Scalability** | Concurrent session handling (10–100) | `wrk`, Mininet scaling scripts | `vmstat`, `htop` |
| **Memory** | Baseline RAM (3.2 GB idle) | `free`, `vmstat` | `docker stats`, `/proc/meminfo` |
| **Memory** | Peak RAM (4.1 GB at 100 sessions) | `free`, `vmstat` | `docker stats` |
| **Memory** | Per-container memory | `docker stats` | `htop` |
| **CPU** | Baseline CPU (10–15% idle) | `vmstat`, `mpstat` | `top`, `htop` |
| **CPU** | Peak CPU (35–40% at 100 sessions) | `vmstat`, `mpstat` | `top`, `docker stats` |
| **CPU** | Per-core utilisation | `mpstat -P ALL` | `htop` |
| **Disk I/O** | Redis persistence, result file writes | `iostat` | `vmstat` (bi/bo columns) |
| **Utilisation (Pre-Model)** | Idle testbed resource baseline | `vmstat`, `free`, `docker stats` | `mpstat`, `iostat` |
| **Breach Containment** | Detection-to-revocation time (< 15 sec) | Python timing + `ovs-ofctl` | `tcpdump`, `hping3` |
| **Classification Accuracy** | Access tier correctness across scenarios | Python (SciPy: Wilcoxon, Cliff's δ) | Pandas DataFrame analysis |
| **Convergence** | Steps to stabilise within ±0.02 | Python (NumPy) | Matplotlib (visual inspection) |
| **Trust Score Stability** | Max variation at maturity ($\Delta T$) | Python (NumPy) | SciPy (statistical testing) |
| **Packet Loss** | Configured vs. actual loss rates | `ping`, `iperf3` | `hping3`, `tc -s qdisc show` |
| **Network Impairment** | Jitter, delay, loss configuration | `tc` / `netem` | `ping`, `hping3` |

---

## 10. Pre-Test Baseline Measurement Protocol

Before running any trust model evaluation, capture the following baseline measurements to establish resource utilisation with the testbed infrastructure running but **no models active**:

```bash
# 1. Memory baseline
free -h > baseline_memory.log

# 2. CPU baseline (60 seconds at 1-second intervals)
vmstat 1 60 > baseline_vmstat.log

# 3. Per-core CPU baseline
mpstat -P ALL 1 60 > baseline_mpstat.log

# 4. Container resource baseline
docker stats --no-stream > baseline_docker_stats.log

# 5. Disk I/O baseline
iostat -x 1 60 > baseline_iostat.log

# 6. Network baseline (RTT to all hosts)
fping -g 10.0.0.0/24 -c 10 > baseline_rtt.log 2>&1

# 7. OVS flow table baseline
ovs-ofctl dump-flows s1 > baseline_flows.log

# 8. Bandwidth baseline between key host pairs
iperf3 -c <target> -t 10 -J > baseline_bandwidth.json
```

This protocol should be repeated **after** each scenario run to measure incremental resource consumption and validate that the testbed returns to baseline between experiments.

---

## 11. Tool Installation Summary

```bash
# Core measurement utilities
sudo apt install -y \
  iperf3 \
  hping3 \
  fping \
  mtr-tiny \
  traceroute \
  tcpdump \
  tshark \
  sysstat \
  htop \
  stress-ng \
  curl \
  httpie \
  redis-tools \
  apache2-utils

# Python analysis stack (within project venv)
pip install numpy pandas scipy matplotlib jupyter py-spy
```

---

## 12. References

- NIST SP 800-207: Zero Trust Architecture (Rose et al., 2020)
- Paper: *A Reproducible, Lightweight Zero Trust Testbed...* — Section V (Experimental Methodology), Section VI (Results), Table VII (Latency Breakdown)
- Paper: *Reproducible Testbed V1* — Section VI (Experimental Results: Latency, Breach Containment, Resource Utilisation, Scalability)
- Horne, D. — *Leveraging SDP, SDN, and Virtualization to Build a Zero Trust Testbed with Limited Resources*
- Mininet documentation: http://mininet.org/
- Open vSwitch documentation: https://docs.openvswitch.org/
- Redis benchmarking guide: https://redis.io/docs/management/optimization/benchmarks/
