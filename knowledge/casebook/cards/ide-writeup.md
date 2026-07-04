# IDE

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/ide_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: john, nmap
- Techniques: browser-forensics, http-analysis, password-cracking, privilege-escalation, service-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `command that was used:`

### Step 2: Exploring FTP

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use john, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: john, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use john, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: Investigation the High Port

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `encountered a login page for Codiad:`

### Step 4: Codiad Login and Exploitation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use john, nmap with the extracted filter/query `python3 49705.py http://thm_ip:port/ username password local_ip local port platform` and inspect the matching evidence.
- Tools: john, nmap
- Filters or commands:
  - `python3 49705.py http://thm_ip:port/ username password local_ip local port platform`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use john, nmap with the extracted filter/query `python3 49705.py http://thm_ip:port/ username password local_ip local port platform` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `reverse shell on the web server:`

### Step 5: Shell Access and Privilege Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Questions Answered:`

### Step 6: user.txt

- Route type: `nmap-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `02930d21a8eb009f6d26361b2d24a466`

### Step 7: root.txt

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use nmap to enumerate processes, network sockets, injected regions, and command lines.
- Tools: nmap
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use nmap to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ce258cb16f47f1c66f0b0b77f4e0fb8d`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
