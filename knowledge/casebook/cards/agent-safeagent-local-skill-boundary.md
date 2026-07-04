# Agent SafeAgent Local Skill Boundary Case

## Case Metadata

- Category: `Agent`
- Source: local authorized CTF engagement notes, distilled from summarized notes only
- Sensitivity: redacted; no raw WebSocket transcript, challenge key, endpoint IP, session token, or internal host detail included

## Why This Case Matters

This case captures a practical agent sandbox lesson: a conversation-facing
agent can expose enough tool behavior to let an attacker create and execute a
same-session local skill, while still failing to expose host files, backend
source, or authorized marketplace access. It is useful when evaluating whether
"agent has shell in a sandbox" is a real escape or only a local execution
primitive.

## Input Signals

- Agent exposes chat-mediated tools such as shell, read, write, edit, and list.
- The environment advertises a skill marketplace or installer path, but access
  depends on hidden authorization.
- Direct sensitive paths are denied and common challenge paths are absent.
- The sandbox has a tiny visible workspace and a limited toolchain.
- The protocol accepts only chat messages after a proof-of-work or session
  handshake.

## First-Principles Route

1. Separate protocol-channel confusion from tool-invocation behavior.
2. Inventory visible tools and files with short bounded probes.
3. Test read/write boundary behavior with harmless marker files.
4. If local skill creation is possible, verify execution with an external marker
   in the same session.
5. Treat marketplace or installer failures as authorization and egress findings,
   not as evidence of host escape.
6. Stop filesystem traversal once direct-child inventories and path existence
   probes converge on the same negative result.

## Case Findings

- The protocol surface processed chat payloads but did not expose a working
  non-chat tool frame route.
- Same-session shell redirection could create local skill files under a
  workspace-controlled skill directory.
- Explicitly asking the agent to read/use the created skill caused shell script
  execution and marker creation.
- The write tool was less reliable than shell redirection for creating
  shell-visible skill files.
- Relative read paths inside the workspace worked, while absolute paths,
  traversal, symlink escape, and common sensitive paths were denied or absent.
- Public skill installation was blocked by a combination of authorization,
  network policy, and missing runtime tools.
- Generic filesystem traversal became low-value once `/workspace`, `/tmp`, and
  common app/challenge paths repeatedly produced negative evidence.

## Knowledge Patterns

### Local Skill Is Not Host Escape

- Signal: attacker can write a skill and make the agent execute it.
- Probe: require a marker proving where the skill ran.
- Evidence rule: report this as same-session local code execution unless a
  protected resource outside the workspace is reached.

### Tool Boundary Differential

- Signal: shell, read, and write disagree about visible paths or created files.
- Probe: test the same marker through each tool and record which view observed
  it.
- Evidence rule: name the exact tool boundary; avoid treating one tool's result
  as global filesystem truth.

### Installer Authorization Failure

- Signal: a marketplace or skill installer exists conceptually but returns
  unauthorized, access-denied, timeout, or missing-runtime errors.
- Probe: separate public page fetch, download endpoint, runtime dependency, and
  hidden credential hypotheses.
- Evidence rule: do not infer a credential leak from repeated unauthorized
  responses.

### Route Reset Trigger

- Signal: directory inventories, direct path probes, and protocol schema probes
  repeatedly converge on negative findings.
- Probe: pause broad traversal and move to context, policy, or authorization
  hypotheses.
- Evidence rule: record the negative route as a reusable constraint so future
  attempts do not repeat it.

## Reuse Guidance

- Query local knowledge with: `agent safeagent local skill boundary workspace read tool`.
- Pair with `agent-sandbox-escape-ctf-thinking.md` for CTF route planning.
- Pair with `agent-sandbox-escape-test-plan.md` for authorized containment
  validation.

## Related Local Resources

- `knowledge/references/agent-sandbox-escape-ctf-thinking.md`
- `knowledge/references/agent-sandbox-escape-test-plan.md`
- `knowledge/references/agent-sandbox-escape-thinking-framework.md`
