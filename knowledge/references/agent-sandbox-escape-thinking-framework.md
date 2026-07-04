# Agent Sandbox Escape Thinking Framework

## Metadata

- Domain: `agent`
- Resource type: `reference`
- Scope: knowledge construction for containment evaluation, defensive review, and evidence-based reasoning.
- Tags: `agent`, `sandbox`, `containment`, `evaluation`, `docker`, `kubernetes`, `mcp`, `runtime`
- Do not tag as: network security

## Core Question

Agent sandbox escape should be framed as a containment question:

> Given an agent with tools, code execution, files, credentials, and outbound channels, which boundary is supposed to contain it, what capability can cross that boundary, and what evidence proves crossing happened?

This makes the topic less about single tricks and more about a repeatable evaluation loop:

1. Define the agent capability envelope.
2. Draw the boundary stack.
3. Enumerate escape primitives by boundary.
4. Design safe, objective verification.
5. Compare model behavior under different guidance levels.
6. Harden the environment and rerun the same checks.

## Boundary Stack

Think in layers. A finding is useful only when it names the layer that failed.

| Layer | What To Ask | High-Risk Signals | Preferred Controls |
| --- | --- | --- | --- |
| Prompt and policy | Can the agent be induced to use tools against containment goals? | Authority/urgency framing, gradual escalation, hidden instructions in tool output | tool allowlists, consent gates, policy checks, refusal telemetry |
| Tool broker and MCP | Can tool descriptions, local servers, or proxies become code/data paths? | broad local MCP servers, token passthrough, weak consent, unvalidated URLs | per-client consent, least privilege scopes, sandbox MCP servers, egress proxy |
| Process and user | Does the agent run as root or with privilege escalation? | root user, sudo, writable system paths, setuid helpers | non-root user, no-new-privileges, read-only rootfs, minimal sudo |
| Filesystem and workspace | Can the agent mutate host or sensitive workspace state? | host bind mounts, shared writable repo, secrets in dotfiles, shell history | clone workspace, read-only mounts, secret scanning, scoped volumes |
| Container config | Is the container still a real boundary? | privileged mode, Docker socket, hostPath, host PID/IPC/network, device mounts | no Docker socket, drop capabilities, rootless/userns, runtime default seccomp |
| Kernel isolation | Can syscalls or kernel attack surface bypass namespacing? | unconfined seccomp, unsafe capabilities, kernel module access, writable proc/sys/cgroup | seccomp, AppArmor/SELinux, gVisor, Kata/microVM, kernel patching |
| Orchestrator identity | Can in-cluster identity control more than the sandbox? | overbroad RBAC, service account token mount, secret/configmap read, workload creation | namespace-scoped RBAC, automount off, Pod Security Restricted, admission policy |
| Egress and credentials | Can data leave or real credentials enter the sandbox? | raw API keys inside VM/container, permissive outbound access, DNS-only escape paths | deny-by-default egress, credential proxy, short-lived scoped tokens, audit logs |
| Evaluation harness | Can success be faked or the harness be attacked? | self-reported success, pattern-only scoring, verifier shared with agent | sidecar verifier, exact marker/flag checks, sandbox-within-sandbox, negative controls |

## Agent Capability Envelope

Before reasoning about escape, record the capability envelope:

- Model and scaffold: model family, tool loop, retries, feedback, memory, and time/token budget.
- Tool surface: shell, filesystem, Docker, kubectl, browser, package manager, MCP tools, cloud SDKs.
- Prompt mode: hard mode with objective only, medium mode with hints, or benchmark mode with scenario-specific guidance.
- Environment: Docker, Kubernetes, local process sandbox, microVM, gVisor/Kata, managed cloud, local workstation.
- Assets to protect: host filesystem, Docker daemon, Kubernetes API, credentials, model provider keys, source tree, logs.
- Allowed proof: marker file, flag string, sidecar observation, audit event, denied syscall, or clean containment result.

SandboxBench's strongest lesson is that agent capability is conditional. The paper reports high success when models receive vulnerability hints, but 0% success in hard mode without hints. Treat prompts, budgets, and feedback as first-class experimental variables.

## Escape Primitive Families

Use primitive families rather than exploit names. This keeps analysis stable as individual CVEs and implementations change.

| Primitive Family | Boundary Crossed | Typical Condition | Evaluation Signal | Defensive Question |
| --- | --- | --- | --- | --- |
| Host control socket | container to host daemon | Docker socket or equivalent admin API exposed | host-side marker via daemon-mediated action | Is any host/admin socket reachable from agent tools? |
| Privileged runtime | container to host resources | privileged container, all devices, relaxed LSM | host filesystem write/read evidence | Can this workload run without privileged mode or devices? |
| Dangerous capabilities | process to kernel/admin operations | broad Linux capabilities such as SYS_ADMIN or SYS_MODULE | capability-sensitive action observable outside container | Are all capabilities dropped except required ones? |
| Namespace sharing | sandbox to host namespace | hostPID, hostIPC, hostNetwork, shared mounts | host process or filesystem visibility beyond intended scope | Are host namespaces disallowed by policy? |
| Writable proc/sys/cgroup | container to kernel control plane | writable proc/sysfs/cgroup v1 paths | controlled marker or denied write telemetry | Are proc/sys/cgroup mounts read-only and constrained? |
| Runtime/kernel CVE | container to host via implementation flaw | vulnerable runc/kernel/runtime version | exact flag/marker outside container | Are runtimes patched and user namespaces/rootless enabled? |
| Orchestrator privilege | pod to cluster/node | overbroad RBAC, workload creation, hostPath, privileged pod rights | cross-namespace secret or node-level access evidence | Does the service account have only required verbs/resources? |
| Secret discovery | sandbox to sensitive data | env vars, dotfiles, config files, metadata service, mounted tokens | planted secret found by scorer | Are secrets absent, scoped, and proxy-injected? |
| Egress bypass | sandbox to outside channel | overly broad HTTP, DNS, proxy, or covert channels | canary/flag observed at approved sink | Is egress deny-by-default and protocol-aware? |
| Persistence/replication | temporary sandbox to durable foothold | cron/systemd/user changes, image/container spawn | durable marker after restart or new workload | Are sandboxes ephemeral and can they spawn children? |

## Evaluation Design

Good evaluations do not ask the model to say whether it escaped. They ask the environment to prove it.

Minimum evaluation ingredients:

- Scenario manifest: boundary under test, intentional weakness, expected protected asset, allowed tools, and stop conditions.
- Difficulty mode: objective only, hints, or scenario-aware guidance. Keep results separate by mode.
- Ground truth: exact marker or flag outside the sandbox boundary, checked by an isolated verifier.
- Negative control: a hardened baseline with no intended vulnerability.
- Harness isolation: run the vulnerable sandbox inside a stronger outer boundary such as a VM or managed isolated runner.
- Scorer integrity: use sidecar or out-of-band checks; avoid scoring based only on assistant text.
- Contamination control: keep private variants or canaries when benchmarking frontier models.
- Repetition: run multiple samples because agent routes vary by stochasticity, retry feedback, and tool failures.

SandboxBench uses a sidecar verifier pattern for marker-based checks. AISI's SandboxEscapeBench uses a sandbox-within-sandbox architecture where the tested container sits inside a hardened VM and success requires retrieving a flag from the VM host. Both patterns make outcome validity stronger than self-reported success.

## Behavior Analysis Loop

For each run, classify behavior rather than only pass/fail:

1. Orientation: Did the agent identify the runtime, privileges, mounts, identity, and egress shape?
2. Hypothesis selection: Did it choose a direct primitive, an orchestrator path, a secret-discovery path, or a dead end?
3. Boundary contact: Did tool calls touch Docker/Kubernetes APIs, proc/sys/cgroup, host mounts, credential files, or metadata endpoints?
4. Evidence attempt: Did it produce a verifiable marker/flag or only a narrative?
5. Containment outcome: escaped, contained, refused, inconclusive, harness error, or false positive.
6. Cost profile: time, token count, command count, and retry count.
7. Defensive lesson: which single control would have blocked the route, and which second control catches the control failure?

## Defensive Framework

Use defense-in-depth because SandboxBench found single-layer controls such as simple command allowlists remained vulnerable, while layered validation/sanitization/allowlisting resisted tested attacks.

Priority controls:

- Put untrusted agents behind a VM, microVM, gVisor, or Kata boundary when consequences exceed local scratch work.
- Do not mount the host Docker socket into agent sandboxes. If Docker is needed, use an isolated inner Docker engine.
- Run non-root; disable privilege escalation; remove ambient sudo unless the outer VM boundary is intentional.
- Drop all Linux capabilities by default, then add only what is strictly required.
- Enforce runtime-default seccomp, AppArmor/SELinux, and read-only root filesystems where practical.
- Block privileged containers, host namespaces, hostPath, broad device mounts, and writable proc/sys/cgroup via admission policy.
- Scope Kubernetes RBAC to namespace-level minimum rights; avoid wildcard verbs/resources and broad workload creation rights.
- Disable automatic service account token mounts for workloads that do not need API access.
- Keep real credentials outside the sandbox; prefer host-side credential proxy injection and short-lived scoped credentials.
- Deny outbound traffic by default, then allow only required destinations and protocols.
- Collect audit logs: Docker daemon calls, Kubernetes audit, egress proxy, denied syscalls, LSM denials, and sandbox lifecycle events.
- Cap time and tokens for routine runs, but periodically run longer hard-mode tests to measure autonomous discovery risk.

## Operational Cadence

Use this cadence for local knowledge recall and future engagement work:

| Trigger | Action |
| --- | --- |
| New agent runtime or model | Baseline containment suite across hard and hinted prompts |
| Dockerfile or compose change | Re-run Docker primitive checks |
| Kubernetes RBAC or admission change | Re-run pod identity and privileged workload checks |
| New tool/MCP server | Threat-model tool broker, consent, scopes, local execution, and egress |
| New credential path | Verify raw secrets do not enter sandbox and proxy logs show expected injection only |
| Security patch cycle | Regression-test previously contained and previously vulnerable scenarios |
| Unexpected agent tool behavior | Preserve tool trace, environment snapshot, and verifier result before cleanup |

## Source Anchors

- SandboxBench SPAR report: https://library.sparai.org/reports/sandboxbench-a-comprehensive-evaluation-framework-for-ai-agent-containment-lmwgda/
- SandboxBench PDF: https://library.sparai.org/attachments/reports/recuJPjRGInlmwGDa/sandboxbench-a-comprehensive-evaluation-framework-for-ai-agent-containment-lmwgda.pdf
- SandboxBench source branch: https://github.com/prashantkul/inspect_evals/tree/feature/sandboxbench/src/inspect_evals/sandboxbench
- AISI SandboxEscapeBench blog: https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities
- SandboxEscapeBench paper: https://arxiv.org/html/2603.02277v1
- AISI Inspect Sandboxing Toolkit: https://www.aisi.gov.uk/blog/the-inspect-sandboxing-toolkit-scalable-and-secure-ai-agent-evaluations
- Docker Engine security: https://docs.docker.com/engine/security/
- Docker Sandboxes security model: https://docs.docker.com/ai/sandboxes/security/
- Kubernetes Pod Security Standards: https://kubernetes.io/docs/concepts/security/pod-security-standards/
- Kubernetes RBAC good practices: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
- MCP Security Best Practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
