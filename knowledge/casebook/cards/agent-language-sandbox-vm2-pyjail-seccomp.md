# Agent Language Sandbox Vm2 Pyjail Seccomp

## Case Metadata

- Category: `Agent`
- Source: vm2 advisories, CTF Wiki, pyjail resources, Linux seccomp docs
- Sources:
  - https://github.com/patriksimek/vm2
  - https://github.com/patriksimek/vm2/security/advisories/GHSA-g644-9gfx-q4q4
  - https://github.com/patriksimek/vm2/security/advisories/GHSA-grj5-jjm8-h35p
  - https://ctf-wiki.mahaloz.re/pwn/linux/sandbox/python-sandbox-escape/
  - https://github.com/jailctf/pyjailbreaker
  - https://jia.je/ctf-writeups/misc/pyjail.html
  - https://docs.kernel.org/userspace-api/seccomp_filter.html
  - https://github.com/david942j/seccomp-tools

## Why This Case Matters

Agent tooling often embeds interpreters, JavaScript evaluators, notebook
kernels, template engines, and command filters. vm2, pyjails, and seccomp CTFs
show three different failure modes: in-process object mediation, language-level
filter bypass, and syscall-policy misunderstanding.

## Input Signals

- Agent can run untrusted JavaScript, Python, pickle, template code, or shell
  snippets.
- Sandbox is described only as "vm", "vm2", "jail", "filtered eval", "safe
  Python", "seccomp", or "chroot" without an outer boundary.
- The tool process has filesystem, network, credentials, Docker, or Kubernetes
  access outside the language sandbox.
- CTF challenge includes severe syntax constraints or a dumped seccomp policy.

## First-Principles Route

1. Identify the actual boundary: language object graph, Node process, OS
   process, syscall filter, container, or VM.
2. Inventory what crosses the boundary: host objects, callbacks, exceptions,
   files, fds, modules, tokens, environment, and egress.
3. For CTF, solve toward the exact flag or verifier. For real systems, do not
   treat language filters as containment.
4. For defense, wrap language sandboxes in process/container/VM isolation and
   keep host secrets out of the interpreter process.

## Case Findings

- vm2's own documentation describes the difficulty of airtight in-process
  JavaScript sandboxing and recommends defense in depth. Public advisories show
  repeated sandbox-breakout classes across versions.
- Pyjail writeups and cheat sheets are useful CTF recall sources because they
  catalog parser constraints, object graph access, builtins recovery, Unicode
  normalization, exception/frame paths, and import surfaces.
- Linux kernel seccomp docs explicitly frame seccomp as syscall-surface
  reduction, not a complete sandbox. It cannot reason about filesystem path
  strings by dereferencing pointers.
- seccomp-tools is useful for CTF and lab analysis because it dumps and
  disassembles BPF policies into a readable form.

## Knowledge Patterns

### In-Process Is Not Host Isolation

- Signal: sandbox runs untrusted code inside the same Node or Python process.
- Probe: identify host objects and privileges available to that process.
- Evidence rule: a sandbox escape is at least host-process code execution; host
  machine impact depends on the outer process boundary.

### Filter Puzzle vs Security Boundary

- Signal: challenge bans strings, characters, builtins, imports, or syntax.
- Probe: inventory constraints and reachable interpreter features.
- Evidence rule: CTF proof is a flag; production proof should be an isolation
  design review, not a payload contest.

### Seccomp Policy Understanding

- Signal: binary loads seccomp or challenge mentions BPF.
- Probe: preserve extracted policy, syscall allow/deny lists, architecture
  checks, and inherited fd assumptions.
- Evidence rule: explain the allowed proof path from policy facts.

## Reuse Guidance

- Query local knowledge with: `agent vm2 pyjail seccomp language sandbox`.
- Pair with the CTF thinking reference for challenge work.
- Pair with the authorized test plan for any real agent runtime evaluation.

## Related Local Resources

- `knowledge/references/agent-sandbox-escape-ctf-thinking.md`
- `knowledge/references/agent-sandbox-escape-test-plan.md`
- `knowledge/references/agent-sandbox-escape-actual-case-map.md`
