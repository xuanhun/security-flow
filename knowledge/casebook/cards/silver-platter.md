# Silver Platter

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/silver_platter.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: burp, gobuster, nmap
- Techniques: http-analysis, password-cracking, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use burp, gobuster, nmap with the extracted filter/query `SSH Login` and inspect the matching evidence.
- Tools: burp, gobuster, nmap
- Filters or commands:
  - `SSH Login`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use burp, gobuster, nmap with the extracted filter/query `SSH Login` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Boom, we have the user flag.`

### Step 2: Privilege Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `let’s simply switch to root user:`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
