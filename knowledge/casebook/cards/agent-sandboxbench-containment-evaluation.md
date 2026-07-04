# Agent SandboxBench Containment Evaluation

## Case Metadata

- Category: `Agent`
- Source: `SandboxBench: A Comprehensive Evaluation Framework for AI Agent Containment`
- Authors: Andrew Wei, Nishit Mengar, Prashant Kulkarni; mentored by Nitzan Shulman
- Program: `SPAR Fall 2025`, submitted January 2026
- Sources:
  - https://library.sparai.org/reports/sandboxbench-a-comprehensive-evaluation-framework-for-ai-agent-containment-lmwgda/
  - https://library.sparai.org/attachments/reports/recuJPjRGInlmwGDa/sandboxbench-a-comprehensive-evaluation-framework-for-ai-agent-containment-lmwgda.pdf
  - https://github.com/prashantkul/inspect_evals/tree/feature/sandboxbench/src/inspect_evals/sandboxbench

## Why This Case Matters

SandboxBench is a useful anchor case because it reframes agent sandbox escape from isolated exploit knowledge into a reproducible containment evaluation. The important move is evidence-based scoring: escape, data exfiltration, and discovery challenges are scored by markers, flags, or planted secrets rather than by model self-report.

Use this case when reasoning about:

- Agent execution environments with shell, Docker, Kubernetes, or MCP tool access.
- Whether a sandbox boundary is actually enforceable under agent pressure.
- How prompt guidance, retries, and token budgets change observed capability.
- How to design sidecar or out-of-band verification for containment tests.

## Input Signals

- Agent has tool access, especially shell, file, Docker, kubectl, HTTP, or MCP tools.
- The sandbox is a Docker container, Kubernetes pod, or local tool runner.
- The environment includes host-like resources: Docker socket, capabilities, host namespaces, mounted filesystems, service account token, metadata service, or raw credentials.
- Evaluation depends on whether the agent can prove a boundary-crossing outcome.

## First-Principles Route

1. Separate the agent capability envelope from the environment boundary.
2. Classify the tested boundary: tool broker, process, filesystem, container, kernel, orchestrator identity, egress, or credential boundary.
3. Identify whether the route is direct, multi-step, or autonomous discovery.
4. Require an external proof signal: marker, flag, sidecar check, or scorer-observed planted secret.
5. Compare results by difficulty mode; do not merge hinted and hard-mode outcomes.
6. Distill which defense would block the route and which second layer would detect or contain failure.

## Case Findings

- The report describes three phases: AI-vs-AI attack exploration, MCP/tool security evaluation, and SandboxBench benchmark development.
- SandboxBench covers 27 challenges across Docker and Kubernetes, including container escape, data exfiltration, secret discovery, lateral movement, persistence, and self-replication.
- The paper reports Docker success rates around 69-77% for tested frontier models under guided conditions, with preliminary Kubernetes success at 40%.
- Direct paths such as privileged runtime, Docker socket exposure, writable proc-like surfaces, dangerous capabilities, and shared process namespace were easier for models.
- More complex multi-step paths, especially kernel module and cgroup-style routes, failed consistently in reported runs.
- Hard mode without vulnerability hints produced 0% success in the reported comparison, while hinted medium mode reached 77%.
- Phase 1 found social engineering and multi-turn attacks materially improved success against weaker tool-server implementations.
- Defense-in-depth was the key defensive conclusion: simple command allowlists were insufficient, while layered validation, sanitization, allowlisting, and reduced tool capability performed much better.

## Knowledge Patterns

### Evidence-Based Containment

- Signal: agent says it escaped or completed a boundary-crossing task.
- Probe: check a marker, flag, canary, or sidecar-observed artifact outside the sandbox.
- Evidence rule: model narrative is never enough; the verifier must observe the protected side of the boundary.

### Prompt Guidance Sensitivity

- Signal: the same environment is tested with and without vulnerability hints.
- Probe: record prompt mode, feedback mode, retry count, time, and token budget.
- Evidence rule: hard-mode and hinted-mode results answer different questions and should be reported separately.

### Direct Path vs Multi-Step Path

- Signal: route depends on one exposed primitive versus chained setup and precise execution.
- Probe: classify the route before interpreting success rates.
- Evidence rule: current model failure on complex chains is a temporary protection margin, not a permanent control.

### Tool Server Hardening

- Signal: MCP/local tool server wraps shell, files, HTTP, or system operations.
- Probe: check validation, sanitization, least privilege, path checks, and disabled interpreters.
- Evidence rule: a tool allowlist alone is not sufficient if argument or path handling can cross the boundary.

## Reuse Guidance

- Use the framework as a checklist for agent containment reviews, not as an execution recipe.
- In reports, name the failed boundary and the proof signal.
- In local knowledge recall, query: `agent sandbox sidecar verifier marker hard mode docker kubernetes containment`.
- When converting this to a practical test, run inside a stronger outer sandbox or disposable lab environment.

## Related Local Resources

- `knowledge/references/agent-sandbox-escape-thinking-framework.md`
- `knowledge/references/agent-sandbox-escape-resource-map.md`
