# Colddbox THM

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/colddbox_thm_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for pe-malware, web-service challenges.

## Input Signals

- Artifacts: pe-malware, web-service
- Tools: capa, gobuster, hydra, nmap, wpscan
- Techniques: http-analysis, malware-static, password-cracking, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, hydra, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, hydra, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o Ports: 80 (HTTP) and 4512 (SSH)`

### Step 2: Exploring Port 80

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, hydra, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, hydra, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `for any vulnerabilities:`

### Step 3: Brute Forcing Login Credentials

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use capa, gobuster, hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: capa, gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use capa, gobuster, hydra, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: Gaining a Reverse Shell

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `404.php`

### Step 5: Privilege Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Questions Answered:`

### Step 6: user.txt

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, hydra, nmap, wpscan with the extracted filter/query `o RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==` and inspect the matching evidence.
- Tools: gobuster, hydra, nmap, wpscan
- Filters or commands:
  - `o RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==`
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, hydra, nmap, wpscan with the extracted filter/query `o RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==`

### Step 7: root.txt

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `reach out. Happy hacking!`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
