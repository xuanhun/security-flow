# Agent Sandbox Escape Actual Case Map

## Metadata

- Domain: `agent`
- Resource type: `reference`
- Scope: public case and vulnerability-class map for agent containment review, authorized lab design, and evidence-based recall.
- Tags: `agent`
- Do not tag as: network security

## Use Boundaries

This map is for knowledge construction and authorized evaluation. It should not
be used as a live exploitation runbook. For real systems, prefer version
inventory, configuration review, negative controls, and isolated lab replicas
over running exploit code.

## Case Families

| Family | Public Anchor | Boundary Crossed | Key Condition | Evidence To Require | Defensive Recall |
| --- | --- | --- | --- | --- | --- |
| runc binary overwrite | CVE-2019-5736 | Container process to host runtime binary | Affected runc lineage and a container context that can influence host-side runtime execution | Patched/unpatched version evidence; in lab, an out-of-band host marker rather than model self-report | Patch runtime; avoid trusted-host execution of attacker-controlled containers; use user namespaces/rootless where practical |
| runc fd leak / cwd breakout | CVE-2024-21626 | Container process to host filesystem namespace | runc 1.1.11 or earlier with leaked internal file descriptors and unsafe working-directory handling | Runtime version, patched 1.1.12 or later, and lab-only host flag check if reproducing | Patch runc; constrain `process.cwd`; close fds before exec; verify cwd stays inside container |
| cgroup v1 release_agent bug | CVE-2022-0492 | Container to kernel cgroup control plane | Vulnerable kernel, cgroup v1 exposure, and permissive namespace/capability posture | Kernel version, cgroup mode, capability/mount evidence, and blocked write telemetry | Patch kernel; prefer cgroup v2; avoid `CAP_SYS_ADMIN`; constrain cgroup/proc/sys mounts |
| Docker daemon socket exposure | Docker daemon API | Container to host daemon | `/var/run/docker.sock` or remote Docker API exposed to the sandbox | Socket mount/API reachability inventory and daemon audit logs | Never mount host docker.sock into untrusted agent sandboxes; use an isolated inner Docker daemon or VM |
| Privileged container / broad capabilities | Docker/Kubernetes runtime config | Container to host devices, namespaces, and kernel surfaces | `privileged`, broad capabilities, host namespaces, devices, or relaxed LSM/seccomp | Pod/container spec, `CapEff`, namespace identity, and denied/allowed policy result | Drop capabilities; use non-root, no-new-privileges, seccomp, AppArmor/SELinux, read-only rootfs |
| Kubernetes hostPath | Kubernetes volume model | Pod to node filesystem/runtime sockets | Host filesystem path mounted into pod, especially read-write | Pod spec, admission result, mounted path inventory, and host-side marker only in lab | Forbid hostPath for untrusted pods; if unavoidable, read-only, narrow path, admin-only namespace |
| Kubernetes RBAC and service account | Kubernetes API identity | Pod identity to namespace/cluster privileges | Workload creation, secret/list permissions, service account token automount, or wildcard verbs | `kubectl auth can-i` matrix, service account token state, audit events | Least privilege RBAC; disable automount where not needed; separate namespaces; enforce Pod Security Baseline/Restricted |
| vm2 / in-process JavaScript sandbox | Node.js process boundary | Untrusted JS to host Node process | In-process sandbox library, vulnerable vm2 versions, callbacks/proxies/errors/async behavior | Package version/advisory match and outer process/container isolation result | Do not rely on in-process JS sandbox alone for arbitrary code; combine with process/OS/VM isolation |
| Python pyjail / filter sandbox | Python interpreter boundary | Restricted Python to interpreter capability or host process | Filter/blacklist mistakes, builtins/object graph reachability, exception/frame leakage | Challenge source, available names/characters, and flag-only CTF proof | For real untrusted Python, use OS isolation; treat language filters as CTF puzzles, not durable controls |
| seccomp/BPF CTF sandbox | Syscall filter boundary | Process to allowed syscall side effects | Incorrect allow/deny list, missing architecture checks, inherited fds, or monitor interactions | Extracted BPF policy, syscall allowlist, architecture handling, fd inventory | Seccomp reduces kernel surface but is not a full sandbox; combine with namespaces, LSM, filesystem and egress controls |

## Agent-Specific Lessons

- A sandbox failure can be a runtime bug, a configuration decision, an
  orchestrator identity issue, or a language-level sandbox mistake. Name the
  failed boundary before naming the trick.
- Direct misconfigurations such as Docker sockets, privileged containers, and
  hostPath mounts are more reliable agent routes than deep kernel chains.
- Version-only checks are appropriate for known CVEs in production. Exploit
  reproduction belongs in disposable nested labs with a host-side verifier.
- A model's narrative is not evidence. Use daemon logs, Kubernetes audit,
  policy-controller decisions, denied syscall logs, or exact host-side markers.
- Language sandboxes such as vm2 and pyjails are inner layers. Treat process,
  container, VM, egress, and credential boundaries as the real controls.

## Source Anchors

- runc CVE-2019-5736 NVD: https://nvd.nist.gov/vuln/detail/cve-2019-5736
- AWS anatomy of CVE-2019-5736: https://aws.amazon.com/blogs/compute/anatomy-of-cve-2019-5736-a-runc-container-escape/
- runc CVE-2024-21626 advisory: https://github.com/opencontainers/runc/security/advisories/GHSA-xr7r-f8xq-vfvv
- CVE-2022-0492 NVD: https://nvd.nist.gov/vuln/detail/CVE-2022-0492
- Unit 42 CVE-2022-0492 analysis: https://unit42.paloaltonetworks.com/cve-2022-0492-cgroups/
- Docker Engine security: https://docs.docker.com/engine/security/
- Docker daemon socket protection: https://docs.docker.com/engine/security/protect-access/
- Trail of Bits Docker container escapes: https://blog.trailofbits.com/2019/07/19/understanding-docker-container-escapes/
- Kubernetes hostPath volumes: https://kubernetes.io/docs/concepts/storage/volumes/#hostpath
- Kubernetes RBAC good practices: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
- Kubernetes service accounts: https://kubernetes.io/docs/concepts/security/service-accounts/
- Kubernetes Pod Security Standards: https://kubernetes.io/docs/concepts/security/pod-security-standards/
- vm2 repository and security disclaimer: https://github.com/patriksimek/vm2
- vm2 custom inspect advisory: https://github.com/patriksimek/vm2/security/advisories/GHSA-g644-9gfx-q4q4
- vm2 2026 advisory example: https://github.com/patriksimek/vm2/security/advisories/GHSA-grj5-jjm8-h35p
- CTF Wiki Python sandbox: https://ctf-wiki.mahaloz.re/pwn/linux/sandbox/python-sandbox-escape/
- Pyjailbreaker: https://github.com/jailctf/pyjailbreaker
- Linux kernel seccomp filter docs: https://docs.kernel.org/userspace-api/seccomp_filter.html
- seccomp-tools: https://github.com/david942j/seccomp-tools

## Related Local Resources

- `knowledge/references/agent-sandbox-escape-thinking-framework.md`
- `knowledge/references/agent-sandbox-escape-resource-map.md`
- `knowledge/casebook/cards/agent-sandboxbench-containment-evaluation.md`
- `knowledge/casebook/cards/agent-sandboxescapebench-nested-evaluation.md`
