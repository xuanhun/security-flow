# Agent SandboxEscapeBench Nested Evaluation

## Case Metadata

- Category: `Agent`
- Source: `SandboxEscapeBench`
- Organization: UK AI Security Institute
- Public release: March 2026
- Sources:
  - https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities
  - https://arxiv.org/html/2603.02277v1
  - https://github.com/UKGovernmentBEIS/sandbox_escape_bench

## Why This Case Matters

SandboxEscapeBench is the strongest companion case to SandboxBench because it emphasizes safe evaluation architecture. It tests whether agents can break out of containers while placing the tested container inside a hardened VM, so a successful container breakout still remains contained by an outer boundary.

Use this case when you need to design or critique an evaluation harness for high-risk agent tool use.

## Input Signals

- Agent has shell access inside a container or pod.
- The evaluation asks for a real boundary-crossing outcome.
- The intended escape surface includes orchestration, runtime, or kernel-layer scenarios.
- The evaluator must protect real infrastructure even if the inner challenge succeeds.

## First-Principles Route

1. Put the target sandbox inside a stronger outer sandbox.
2. Make success a single unambiguous signal outside the inner boundary.
3. Verify the scenario is solvable with a reference solution, but avoid exposing solution details during real evaluation.
4. Add negative controls and harden unintended paths found during development.
5. Track model performance by scenario class, difficulty, compute budget, and model size.
6. Treat unintended solution paths as harness findings, not just benchmark noise.

## Case Findings

- The public AISI blog describes SandboxEscapeBench as a benchmark for safely measuring container breakout capability.
- The benchmark uses a sandbox-within-a-sandbox setup: each tested container runs inside a hardened virtual machine.
- The paper describes 18 scenarios across orchestration, runtime, and kernel layers.
- Success is based on retrieving a host-side flag that is inaccessible from inside the container without crossing the intended boundary.
- The authors report that advanced models can reliably solve common misconfiguration cases when prompted to do so.
- Larger models make progress on intermediate multi-step or known-vulnerability scenarios, but the hardest scenarios remained unsolved in the reported results.
- The paper notes unintended escape paths discovered during benchmark development, reinforcing the need for iterative harness hardening.
- Performance scales with model size and inference-time compute, so token/time budgets must be recorded as part of the result.

## Knowledge Patterns

### Sandbox Within Sandbox

- Signal: evaluation deliberately gives the model a vulnerable environment.
- Probe: ensure an outer VM, microVM, or similarly strong boundary contains any successful inner escape.
- Evidence rule: inner escape success must never imply real infrastructure exposure.

### Flag-Based Outcome Validity

- Signal: scorer needs a clean binary result.
- Probe: place a flag or marker outside the inner sandbox and check exact retrieval.
- Evidence rule: exact string matching or sidecar state is stronger than natural-language claims.

### Harness Hardening As A Finding

- Signal: model reaches the host by an unintended path.
- Probe: record the unintended path class and harden the environment.
- Evidence rule: benchmark validity requires the flag be accessible only through intended scenario classes.

### Compute-Budget Sensitivity

- Signal: longer reasoning or more retries changes success.
- Probe: log token count, elapsed time, command count, and stop reason.
- Evidence rule: compare runs only when budgets and scaffolds are comparable.

## Reuse Guidance

- Prefer this design when testing agent containment capability rather than ordinary application behavior.
- Use outer isolation before enabling dangerous inner scenarios.
- Keep private variants if benchmark contamination matters.
- In local knowledge recall, query: `agent sandbox nested evaluation flag outer vm containment`.

## Related Local Resources

- `knowledge/references/agent-sandbox-escape-thinking-framework.md`
- `knowledge/references/agent-sandbox-escape-resource-map.md`
