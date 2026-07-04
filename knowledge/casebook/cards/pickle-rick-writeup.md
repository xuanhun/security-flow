# Pickle Rick

## Case Metadata

- Category: `Pentesting`
- Platform: `VulnHub`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/pickle_rick_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: detect-it-easy, gobuster, nikto, nmap
- Techniques: http-analysis, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o Ports: 22 (SSH) and 80 (HTTP)`

### Step 2: Exploring Port 80

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `‘Wubbalubbadubdub’:`

### Step 3: Getting a Reverse Shell

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, nikto, nmap with the extracted filter/query `If you navigate to the home directory, you can find a directory for rick which contains another` and inspect the matching evidence.
- Tools: gobuster, nikto, nmap
- Filters or commands:
  - `If you navigate to the home directory, you can find a directory for rick which contains another`
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, nikto, nmap with the extracted filter/query `If you navigate to the home directory, you can find a directory for rick which contains another` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `interesting file:`

### Step 4: Privileges Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Questions Answered:`

### Step 5: What is the last and final ingredient? o fleeb juice

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `feedback. Happy hacking!`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
