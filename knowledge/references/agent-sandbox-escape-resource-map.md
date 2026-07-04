# Agent Sandbox Escape Resource And Case Map

## Metadata

- Domain: `agent`
- Resource type: `reference`
- Scope: resource map for agent containment, sandbox escape evaluation, and case recall.
- Tags: `agent`, `sandbox`, `containment`, `evaluation`, `docker`, `kubernetes`, `runtime`, `mcp`
- Do not tag as: network security

## Search Scope

This map was built from searches across:

- SandboxBench and SandboxEscapeBench papers, source branches, and benchmark repositories.
- Docker, Kubernetes, MCP, and Inspect official documentation.
- Container isolation standards and benchmark references.
- Public container escape case studies and CVE advisories.
- Stronger isolation runtimes and local sandboxing tools.
- Agent sandbox products and operational patterns.

The goal is knowledge construction: identify reusable reasoning patterns, evidence requirements, and defensive controls. Do not treat this file as an exploitation runbook.

## Core Papers And Benchmarks

| Resource | Why It Matters | URL |
| --- | --- | --- |
| SandboxBench SPAR report | Main paper requested by the user; 27 Docker/Kubernetes challenges, sidecar verification, model results, hard-mode contrast | https://library.sparai.org/reports/sandboxbench-a-comprehensive-evaluation-framework-for-ai-agent-containment-lmwgda/ |
| SandboxBench PDF | Full paper text | https://library.sparai.org/attachments/reports/recuJPjRGInlmwGDa/sandboxbench-a-comprehensive-evaluation-framework-for-ai-agent-containment-lmwgda.pdf |
| SandboxBench source branch | Implementation snapshot: challenge list, marker verification, difficulty modes, scorer design | https://github.com/prashantkul/inspect_evals/tree/feature/sandboxbench/src/inspect_evals/sandboxbench |
| inspect_evals issue #713 | Original SandboxBench proposal and early challenge taxonomy | https://github.com/UKGovernmentBEIS/inspect_evals/issues/713 |
| inspect_evals PR #789 | Merged PR history showing challenge consolidation, ground-truth verification, and baseline corrections | https://github.com/UKGovernmentBEIS/inspect_evals/pull/789 |
| inspect_evals PR #792 | Adds lateral movement, persistence, and replication challenge family discussion | https://github.com/UKGovernmentBEIS/inspect_evals/pull/792 |
| AISI SandboxEscapeBench blog | Later benchmark with sandbox-within-sandbox design and 18 escape scenarios | https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities |
| SandboxEscapeBench paper | Formal paper on frontier LLM container breakout capability, outcome validity, unintended escape paths, and compute scaling | https://arxiv.org/html/2603.02277v1 |
| SandboxEscapeBench repository | Open-source Inspect evaluation for container breakout testing inside VM-hosted scenarios | https://github.com/UKGovernmentBEIS/sandbox_escape_bench |
| AISI Inspect Sandboxing Toolkit | Operational sandboxing stack: Docker Compose, Kubernetes, Proxmox, plus tooling/host/egress axes | https://www.aisi.gov.uk/blog/the-inspect-sandboxing-toolkit-scalable-and-secure-ai-agent-evaluations |
| Inspect AI sandboxing docs | Framework mechanics for executing tool calls in isolated environments | https://inspect.aisi.org.uk/sandboxing.html |

## Agent Sandbox Products And Patterns

| Resource | Reusable Pattern | URL |
| --- | --- | --- |
| Docker Sandboxes security model | MicroVM boundary, isolated Docker Engine, credential proxy, workspace isolation | https://docs.docker.com/ai/sandboxes/security/ |
| Docker Sandboxes isolation layers | Hypervisor, network, Docker Engine, workspace, credential isolation | https://docs.docker.com/ai/sandboxes/security/isolation/ |
| Docker Sandboxes defaults | Default posture for credentials, workspace, and allowed actions | https://docs.docker.com/ai/sandboxes/security/defaults/ |
| Docker Sandboxes credentials | Host-side credential injection so raw secrets do not enter the sandbox | https://docs.docker.com/ai/sandboxes/security/credentials/ |
| Docker Sandboxes architecture | How workspace mounting, storage persistence, and proxying are composed | https://docs.docker.com/ai/sandboxes/architecture/ |
| Docker Sandboxes get started | Practical local agent sandbox lifecycle | https://docs.docker.com/ai/sandboxes/get-started/ |
| Docker Sandboxes customization | Templates and kits as controlled capability bundles | https://docs.docker.com/ai/sandboxes/customize/ |

## Docker And Container Boundary References

| Resource | Key Knowledge | URL |
| --- | --- | --- |
| Docker Engine security | Namespaces, cgroups, Docker daemon attack surface, capabilities, hardening features | https://docs.docker.com/engine/security/ |
| Docker runtime privilege and capabilities | Privileged containers, capabilities, and device exposure semantics | https://docs.docker.com/engine/containers/run/#runtime-privilege-and-linux-capabilities |
| Docker seccomp profiles | Default seccomp allowlist and why unconfined seccomp increases kernel attack surface | https://docs.docker.com/engine/security/seccomp/ |
| Docker AppArmor profiles | Default `docker-default` profile and custom profile model | https://docs.docker.com/engine/security/apparmor/ |
| Docker rootless mode | Runs Docker daemon and containers without root privileges | https://docs.docker.com/engine/security/rootless/ |
| Docker user namespace isolation | Maps container root to unprivileged host identity | https://docs.docker.com/engine/security/userns-remap/ |
| Docker daemon socket protection | Host Docker socket as host-control boundary | https://docs.docker.com/engine/security/protect-access/ |
| Docker Bench for Security | Local checks for common Docker production hardening practices | https://github.com/docker/docker-bench-security |

## Kubernetes Boundary References

| Resource | Key Knowledge | URL |
| --- | --- | --- |
| Pod Security Standards | Privileged/Baseline/Restricted policy model for pod privilege control | https://kubernetes.io/docs/concepts/security/pod-security-standards/ |
| Security context | Container user, privilege escalation, capabilities, and seccomp settings | https://kubernetes.io/docs/tasks/configure-pod-container/security-context/ |
| RBAC good practices | Least privilege, token minimization, workload creation, hostPath, nodes/proxy risks | https://kubernetes.io/docs/concepts/security/rbac-good-practices/ |
| Service Accounts | Namespaced non-human identity and token handling for pods | https://kubernetes.io/docs/concepts/security/service-accounts/ |
| NetworkPolicy | Ingress/egress isolation model for pods | https://kubernetes.io/docs/concepts/services-networking/network-policies/ |
| Kubernetes seccomp tutorial | RuntimeDefault, Unconfined, and profile application details | https://kubernetes.io/docs/tutorials/security/seccomp/ |
| Kubernetes AppArmor tutorial | Enforcing AppArmor profiles in pods | https://kubernetes.io/docs/tutorials/security/apparmor/ |
| GKE RBAC best practices | Managed-cluster RBAC least privilege and privilege escalation concerns | https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac |
| Amazon EKS runtime security | Runtime detection and profile tooling in managed Kubernetes | https://docs.aws.amazon.com/eks/latest/best-practices/runtime-security.html |

## MCP And Tool-Broker References

| Resource | Key Knowledge | URL |
| --- | --- | --- |
| MCP specification | Tools are arbitrary code execution paths; consent, data privacy, tool safety, sampling controls | https://modelcontextprotocol.io/specification/2025-06-18 |
| MCP security best practices | Confused deputy, token passthrough, SSRF, local MCP compromise, OAuth URL validation, stdio proxy risk | https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices |
| MCP intro | MCP connects AI applications to tools, resources, and workflows | https://modelcontextprotocol.io/docs/getting-started/intro |
| NSA MCP security design considerations | Deployment guidance and secure-by-default concerns for MCP adoption | https://www.nsa.gov/Portals/75/documents/Cybersecurity/CSI_MCP_SECURITY.pdf |

## Isolation Runtimes And Local Sandboxes

| Resource | Boundary Model | URL |
| --- | --- | --- |
| gVisor | Userspace application kernel reducing direct host-kernel attack surface | https://gvisor.dev/docs/ |
| Multi-Agent gVisor Isolation | Agent-oriented gVisor isolation discussion | https://gvisor.dev/blog/2026/04/15/magi-multi-agent-gvisor-isolation/ |
| Kata Containers | Lightweight VMs that feel like containers but add hardware virtualization isolation | https://katacontainers.io/ |
| Kata Containers repository | OCI/CRI-compatible lightweight VM runtime implementation | https://github.com/kata-containers/kata-containers |
| nsjail | Linux namespaces, cgroups, rlimits, and seccomp-bpf for process isolation | https://github.com/google/nsjail |
| bubblewrap | Unprivileged sandboxing tool used by Flatpak and similar projects | https://github.com/containers/bubblewrap |
| Firejail | Linux namespaces and seccomp-based application sandboxing | https://firejail.wordpress.com/ |

## Standards And Taxonomies

| Resource | Use In Framework | URL |
| --- | --- | --- |
| MITRE ATT&CK Containers Matrix | Common vocabulary for container and orchestration behavior | https://attack.mitre.org/matrices/enterprise/containers/ |
| MITRE T1611 Escape to Host | Container-to-host escape technique framing | https://attack.mitre.org/techniques/T1611/ |
| MITRE T1552.007 Container API credentials | Credential discovery through Docker/Kubernetes APIs | https://attack.mitre.org/techniques/T1552/007/ |
| NIST SP 800-190 | Application container security concerns and recommendations | https://csrc.nist.gov/pubs/sp/800/190/final |
| CIS Docker Benchmark | Secure Docker configuration guidance | https://www.cisecurity.org/benchmark/docker |
| CIS Kubernetes Benchmark | Secure Kubernetes configuration guidance | https://www.cisecurity.org/benchmark/kubernetes |
| OWASP Docker Security Cheat Sheet | Practical Docker hardening checklist | https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html |

## Public Case Studies And Advisory Anchors

| Case | Why It Belongs In Recall | URL |
| --- | --- | --- |
| Trail of Bits: Understanding Docker container escapes | Explains why privileged mode, capabilities, AppArmor/seccomp choices, and mounts matter | https://blog.trailofbits.com/2019/07/19/understanding-docker-container-escapes/ |
| runc CVE-2019-5736 NVD | Runtime vulnerability enabling host runc overwrite in affected configurations | https://nvd.nist.gov/vuln/detail/cve-2019-5736 |
| AWS anatomy of CVE-2019-5736 | Vendor explanation of runtime flaw and cloud impact | https://aws.amazon.com/blogs/compute/anatomy-of-cve-2019-5736-a-runc-container-escape/ |
| Red Hat runc escape bulletin | Vendor remediation and affected-product framing | https://access.redhat.com/security/vulnerabilities/runcescape |
| CVE-2022-0492 CVE record | cgroup v1 release_agent privilege issue | https://www.cve.org/CVERecord?id=CVE-2022-0492 |
| Unit 42 CVE-2022-0492 analysis | cgroups as a container primitive and misconfiguration amplifier | https://unit42.paloaltonetworks.com/cve-2022-0492-cgroups/ |
| runc CVE-2024-21626 advisory | File descriptor leak class and host filesystem access | https://github.com/opencontainers/runc/security/advisories/GHSA-xr7r-f8xq-vfvv |
| CVE-2024-21626 NVD | Public vulnerability record | https://nvd.nist.gov/vuln/detail/cve-2024-21626 |
| Snyk CVE-2024-21626 writeup | Practical impact, patched version guidance, and build/runtime scope | https://labs.snyk.io/resources/cve-2024-21626-runc-process-cwd-container-breakout/ |
| Unit 42 container escape techniques | Detection-oriented review of escape classes | https://unit42.paloaltonetworks.com/container-escape-techniques/ |

## Recall Patterns

Use these patterns when searching the local knowledge base later:

### Sidecar Or Out-Of-Band Verification

- Signal: agent claims escape, writes marker, or reports flag.
- Recall terms: `agent sandbox sidecar verifier marker ground truth`.
- Lesson: score with environment evidence, not assistant narrative.
- Example cases: SandboxBench, SandboxEscapeBench.

### Direct Misconfiguration Exploitation

- Signal: privileged, Docker socket, host namespace, host mount, broad capabilities.
- Recall terms: `agent sandbox privileged docker socket capabilities host namespace`.
- Lesson: direct paths are most likely to be solved by current models when hinted.
- Evidence: marker outside sandbox boundary or verifier-observed state change.

### Hard-Mode Discovery Gap

- Signal: same vulnerable environment but no scenario hints.
- Recall terms: `agent sandbox hard mode autonomous discovery token budget`.
- Lesson: current reported results show much lower autonomous discovery than hinted execution; this may change with model capability.
- Evidence: compare hard and hinted success rates separately.

### Orchestrator Identity Escape

- Signal: Kubernetes service account, RBAC, workload creation, hostPath, privileged pod, ConfigMap/Secret access.
- Recall terms: `agent kubernetes RBAC service account pod security sandbox`.
- Lesson: pod containment is also identity containment.
- Evidence: cross-namespace or node-level observation verified by API/audit logs.

### Credential And Egress Boundary

- Signal: env secrets, dotfiles, metadata service, raw API keys, proxy bypass.
- Recall terms: `agent sandbox credentials egress proxy metadata`.
- Lesson: containment fails even without host escape if credentials leave the boundary.
- Evidence: planted secret found by scorer or egress proxy canary.

### Defense Regression

- Signal: model/runtime/image/policy update.
- Recall terms: `agent containment regression sandbox model update`.
- Lesson: rerun the same suite after every boundary-changing update.
- Evidence: prior and current run comparison, same prompts and same scorer.
