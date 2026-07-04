# Agent Sudo

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/agent_sudo_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for disk-image, web-service challenges.

## Input Signals

- Artifacts: disk-image, web-service
- Tools: autopsy, binwalk, hydra, john, nmap, steghide
- Techniques: http-analysis, password-cracking, privilege-escalation, service-enumeration, stego-extraction

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o 21 (FTP), 22 (SSH), and 80 (HTTP)`

### Step 2: Investigating Port 80

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, hydra, nmap, steghide to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use binwalk, hydra, nmap, steghide to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 3: user-agent.

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, hydra, nmap, steghide to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use binwalk, hydra, nmap, steghide to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `we get:`

### Step 4: Brute Forcing FTP

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: Steganography and Zip Cracking

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, john, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, john, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, john, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Let’s download them and investigate the files locally:`

### Step 6: Exploring Image using Steghide

- Route type: `binwalk-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as binwalk-driven evidence lookup.
  - Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `tool:`

### Step 7: SSH Login

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `It worked:`

### Step 8: Privilege Escalation

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use binwalk, hydra, nmap, steghide to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use binwalk, hydra, nmap, steghide to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Questions Answered:`

### Step 9: FTP password

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `o crystal`

### Step 10: Zip file password

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `o alien`

### Step 11: Steg password

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `o Area51`

### Step 12: SSH password

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, hydra, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `o hackerrules!`

### Step 13: What is the user flag?

- Route type: `binwalk-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as binwalk-driven evidence lookup.
  - Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b03d975e8c92a7c04146cfa7a5a313c7`

### Step 14: CVE number for the escalation

- Route type: `binwalk-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as binwalk-driven evidence lookup.
  - Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CVE-2019-14287`

### Step 15: What is the root flag?

- Route type: `binwalk-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as binwalk-driven evidence lookup.
  - Use binwalk, hydra, nmap, steghide to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b53a02f55b57d4439e3341834d70c062`

### Step 16: Who is Agent R? o DesKel

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use binwalk, hydra, nmap, steghide to enumerate processes, network sockets, injected regions, and command lines.
- Tools: binwalk, hydra, nmap, steghide
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use binwalk, hydra, nmap, steghide to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
