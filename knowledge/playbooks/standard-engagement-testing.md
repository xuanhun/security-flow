# Standard Engagement Testing Playbook

Use this playbook for CTF, lab, and authorized penetration testing work.

## Required Loop

1. Validate scope.
2. Enter or confirm the current phase.
3. Run knowledge recall for that phase.
4. Choose the smallest safe probe that answers the current question.
5. Store evidence under the engagement.
6. Extract observed terms and search local knowledge again.
7. Record candidate routes, attempts, negative evidence, and next constraints.
8. Exit the phase only after knowledge recall and context are current.

## Evidence Terms To Extract

- URLs, routes, hosts, ports, protocols, parameters, cookies, headers.
- File names, extensions, hashes, archive members, metadata, magic bytes.
- Framework names, server banners, package names, JavaScript chunks.
- Error strings, CVEs, stack traces, auth roles, object IDs.

## Default Gates

Keep these gated unless scope explicitly approves them: exploitation, online
password attacks, sniffing/spoofing, wireless attacks, post-exploitation,
destructive fuzzing, heavy scans, and third-party token validation.
