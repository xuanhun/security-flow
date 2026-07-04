# Agent Sandbox Escape CTF Thinking

## Metadata

- Domain: `agent`
- Resource type: `reference`
- Scope: CTF and challenge-solving reasoning patterns for sandbox escape topics, adapted for agent knowledge recall.
- Tags: `agent`
- Do not tag as: network security

## CTF Boundary First

Before choosing a technique, identify which sandbox is actually present:

| Sandbox Type | First Questions | Durable Thinking Pattern |
| --- | --- | --- |
| Python pyjail | Is input passed to `eval`, `exec`, pickle, template code, or a REPL? Which characters, builtins, globals, imports, exceptions, frames, and files are reachable? | Treat it as a language object-graph and parser-constraint puzzle. Inventory before payloads. |
| Node/vm/vm2 | Is this Node's built-in `vm`, vm2, isolated-vm, worker, or a containerized runner? Which modules, callbacks, errors, promises, inspectors, and host objects cross contexts? | In-process JavaScript isolation is brittle; version and host-object mediation matter. |
| Shell/chroot jail | What is the root, cwd, PATH, environment, file descriptors, mount namespace, user, and available binaries? | Many jails fail through inherited fds, writable paths, interpreter escapes, or bad assumptions about chroot. |
| seccomp/BPF | Is the policy allowlist or denylist? Are architecture checks present? Which syscalls and arguments survive? Are fds already open? | Dump and reason about the BPF policy before exploit design. Seccomp narrows syscalls; it is not a complete sandbox. |
| Container/Docker | Is the challenge intentionally privileged, socket-mounted, host-mounted, host-networked, or vulnerable runtime based? | Check config primitives first; direct exposed control planes beat deep chains. |
| Kubernetes | Which service account is mounted? Can this identity create workloads, read secrets, use hostPath, or request privileged pods? | Pod containment is also API identity containment. RBAC and admission decide the route. |

## Pyjail Recall Checklist

Use this for CTF challenges, not for real untrusted-code containment:

- Parse path: `eval`, `exec`, AST transformation, pickle, template engine,
  custom REPL, or expression-only filter.
- Constraint shape: banned substrings, character set, length, one-line input,
  no quotes, no digits, no dots, no brackets, no calls, no builtins, no imports.
- Object graph: class hierarchy, existing objects, magic methods, exceptions,
  tracebacks, frames, globals, closures, descriptors, and module caches.
- Parser tricks: Unicode normalization, alternate syntax, decorators,
  comprehensions, assignment expressions, format strings, and implicit calls.
- Side channels: error text, repr/str hooks, help/license printers, open file
  descriptors, environment variables, cwd, and preloaded modules.
- Proof: exact challenge flag, not shell access as a default goal.

## vm2 / JavaScript Sandbox Recall Checklist

- Confirm package and version. For vm2, check GitHub advisories and npm lock
  files before assuming the sandbox is current.
- Identify bridge surfaces: Proxies, host exceptions, custom inspection,
  async/promises, getters/setters, Buffer, module loading, and host-provided
  objects.
- Treat a vm2 escape in a challenge as a host-process escape, not a host-machine
  escape unless the Node process itself has useful OS privileges.
- For defensive recall, recommend process/container/VM isolation around any
  in-process sandbox that runs untrusted JavaScript.

## Seccomp/BPF CTF Recall Checklist

- Extract the rules with a trusted local tool such as `seccomp-tools` or from
  source/decompiler output.
- Classify the filter: strict mode, allowlist, denylist, user notification,
  ptrace/monitor interaction, or layered filters.
- Check architecture handling: x86_64, x86, x32, aarch64, and whether the
  policy validates the syscall ABI.
- Inventory allowed syscalls, syscall substitutes, and inherited file
  descriptors. In many CTFs, reading a flag is an ORW-style proof rather than a
  shell.
- Confirm whether paths, pointers, and string contents are actually visible to
  seccomp. Kernel docs emphasize that BPF filters do not dereference pointers.
- Proof should be the challenge flag or verifier result, with the extracted
  policy preserved as evidence.

## Container And Kubernetes CTF Recall Checklist

- Start with environment facts: user, capabilities, mounts, namespaces, cgroup
  mode, seccomp/AppArmor/SELinux, Docker socket, runtime version, and kernel
  version.
- In Kubernetes, record namespace, service account, mounted token, API server
  reachability, RBAC verbs, and admission restrictions.
- Look for intentional CTF clues: hostPath, privileged pod, hostPID/hostIPC,
  Docker-in-Docker, exposed daemon API, node kubeconfig, or overly broad
  service account.
- Keep host proof narrow: marker or flag from the lab host/VM, never unrelated
  host data.

## Wrong Turns

- Treating every sandbox as a kernel exploit problem.
- Treating seccomp as if it controls filesystem paths.
- Trusting an agent's "escaped" claim without a verifier.
- Mixing hard-mode and hinted-mode model results.
- Running public exploit code on a non-disposable host when version inventory
  would answer the production question.
- Assuming language-level filters provide containment for real untrusted code.

## Source Anchors

- CTF Wiki Python sandbox: https://ctf-wiki.mahaloz.re/pwn/linux/sandbox/python-sandbox-escape/
- Pyjailbreaker: https://github.com/jailctf/pyjailbreaker
- Pyjail cheatsheet: https://shirajuki.js.org/blog/pyjail-cheatsheet/
- Python jail writeup collection: https://jia.je/ctf-writeups/misc/pyjail.html
- Linux kernel seccomp filter docs: https://docs.kernel.org/userspace-api/seccomp_filter.html
- seccomp-tools: https://github.com/david942j/seccomp-tools
- Guide of Seccomp in CTF: https://n132.github.io/2022/07/03/Guide-of-Seccomp-in-CTF.html
- Google CTF 2022 S2 writeup: https://n132.github.io/2022/07/04/S2.html
- Practical CTF sandboxes: https://book.jorianwoltjer.com/binary-exploitation/sandboxes-chroot-seccomp-and-namespaces
- Google CTF 2019 Sandstone writeup: https://voidma.in/posts/writeups/2019/06/24/writeup-gctf19quals-sandstone.html
- Local ApacheCN import summary: `engagements/legacy-test-reports/apachecn-ctf-wiki-import-2026-06-24/summary.md`
