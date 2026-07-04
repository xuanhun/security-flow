# Kali Framework Map

This skill follows the broad Kali Linux menu and metapackage shape while
running on a normal Linux host when possible.

## Modules

| Kali-style area | Skill module | Default action |
| --- | --- | --- |
| Information Gathering | `information_gathering.py` | safe target discovery, TCP scan, optional nmap |
| Vulnerability Analysis | `vulnerability_analysis.py` | gated scanners and evidence routing |
| Web Applications | `web_applications.py` | HTTP baseline, optional whatweb |
| Database Assessment | planned | identify exposed services and route manual checks |
| Password Attacks | planned | offline audit only; online attacks gated |
| Wireless | planned | lab workflow and tool detection only |
| Reverse Engineering | planned | file triage and binary tooling |
| Exploitation | `exploitation_gate.py` | gate only |
| Sniffing & Spoofing | planned | gate only |
| Post Exploitation | planned | gate only |
| Forensics | planned | hash and artifact inventory |
| Reporting | `core/report.py` | Markdown and JSON report |
| Structured Memory | `core/memory.py` | candidate routes, negative evidence, verification state, next constraints |

## Workflow

1. Initialize project and scope.
2. Check environment and install only approved tool profiles.
3. Validate scope.
4. Run information gathering.
5. Run web or service baselines.
6. Review `kali.py memory --summary` and `memory --next` before repeating or
   escalating probes.
7. Add vulnerability analysis only when the authorization supports it.
8. Record candidate routes with `candidate` and outcomes with `attempt` when
   the route is not already captured by a built-in command.
9. Review findings, negative evidence, verification state, and next
   constraints.
10. Generate report.
11. Distill reusable lessons into quality notes, not runtime evidence.
