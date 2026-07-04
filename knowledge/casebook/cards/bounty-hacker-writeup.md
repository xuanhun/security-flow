# Bounty Hacker

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/bounty_hacker_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: hydra, nmap
- Techniques: http-analysis, password-cracking, privilege-escalation, service-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `command that was used:`

### Step 2: Exploring FTP

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `username.`

### Step 3: Brute Force SSH Credentials

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: Privilege Escalation

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use hydra, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use hydra, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 5: Additional Information

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use hydra, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use hydra, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Questions Answered:`

### Step 6: user.txt

- Route type: `hydra-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use hydra, nmap to collect the smallest evidence slice that answers the goal.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as hydra-driven evidence lookup.
  - Use hydra, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o THM{CR1M3_SyNd1C4T3}`

### Step 7: root.txt

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use hydra, nmap to enumerate processes, network sockets, injected regions, and command lines.
- Tools: hydra, nmap
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use hydra, nmap to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Happy hacking!`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
