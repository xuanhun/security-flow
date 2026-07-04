# Agent Kubernetes Goat And Bad Pods Testbeds

## Case Metadata

- Category: `Agent`
- Source: Kubernetes Goat, Bad Pods, Kubernetes documentation, Aqua tools
- Sources:
  - https://github.com/madhuakula/kubernetes-goat
  - https://madhuakula.com/kubernetes-goat/docs/scenarios/scenario-4/container-escape-to-the-host-system-in-kubernetes-containers/welcome/
  - https://github.com/BishopFox/badPods
  - https://bishopfox.com/blog/kubernetes-pod-privilege-escalation
  - https://kubernetes.io/docs/concepts/security/rbac-good-practices/
  - https://kubernetes.io/docs/concepts/security/pod-security-standards/
  - https://github.com/aquasecurity/kube-bench
  - https://github.com/aquasecurity/kube-hunter

## Why This Case Matters

Kubernetes agent sandboxes are not just containers. They inherit pod
configuration, admission policy, service account identity, namespace
permissions, and node mounts. Kubernetes Goat and Bad Pods provide reusable
authorized-lab patterns for testing those layers without touching production.

## Input Signals

- Agent has `kubectl`, in-cluster network access, a service account token, or
  shell access inside a pod.
- Pod specs include hostPath, hostPID, hostIPC, hostNetwork, privileged, broad
  capabilities, or device mounts.
- The identity can create workloads, read secrets, bind roles, request tokens,
  or use a privileged service account.
- A report needs to demonstrate whether admission controls actually deny risky
  pod shapes.

## First-Principles Route

1. Record namespace, service account, token automount state, and RBAC verbs.
2. Check admission policy before creating risky workloads.
3. Use Kubernetes Goat or Bad Pods only in isolated lab clusters.
4. Pair every intentionally vulnerable pod with a hardened negative control.
5. Score with Kubernetes API responses, audit logs, admission events, and
   host-side lab markers.

## Case Findings

- Kubernetes Goat is an intentionally vulnerable cluster playground with
  scenarios including Docker-in-Docker, container escape, Docker/Kubernetes CIS
  checks, namespace issues, RBAC least privilege, runtime detection, and policy
  enforcement topics.
- Bad Pods provides manifests for elevated pod attributes such as hostNetwork,
  hostPID, hostPath, hostIPC, privileged, and combinations. It is useful for
  showing the impact of allowing specific pod attributes.
- Kubernetes RBAC documentation warns that workload creation can imply access
  to namespace resources and service account privileges.
- Kubernetes hostPath documentation warns that host filesystem mounts can expose
  kubelet credentials, runtime sockets, and privileged APIs.
- kube-bench is a CIS configuration scanner. kube-hunter can probe cluster
  weaknesses, but upstream notes it is no longer under active development and
  warns not to run it on clusters you do not own; active mode can change state.

## Knowledge Patterns

### Workload Creation Is Privilege

- Signal: `create pods`, `create deployments`, or related workload verbs.
- Probe: enumerate service accounts and mountable resources in the namespace.
- Evidence rule: report what the identity can create and which service account
  the created workload could run as.

### Admission Policy As Control

- Signal: risky pod spec is the suspected route.
- Probe: dry-run or apply in lab and capture admission allow/deny result.
- Evidence rule: an admission denial is valid containment evidence.

### hostPath And Runtime Sockets

- Signal: hostPath or socket volume appears in a pod spec.
- Probe: identify exact host path, read/write mode, and whether it exposes
  runtime or kubelet credentials.
- Evidence rule: never read unrelated host data; use planted markers in lab.

## Reuse Guidance

- Query local knowledge with: `agent kubernetes hostPath RBAC service account bad pods goat`.
- Use Kubernetes Goat for scenario-driven learning.
- Use Bad Pods to verify admission guardrails against specific dangerous pod
  attributes.
- Use kube-bench for CIS baseline and kube-hunter only inside owned lab scope.

## Related Local Resources

- `knowledge/references/agent-sandbox-escape-test-plan.md`
- `knowledge/references/agent-sandbox-escape-actual-case-map.md`
- `knowledge/references/agent-sandbox-escape-thinking-framework.md`
