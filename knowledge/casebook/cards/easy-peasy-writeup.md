# Easy peasy

## Case Metadata

- Category: `Pentesting`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/easy_peasy_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: binwalk, cyberchef, gobuster, john, nmap, steghide
- Techniques: http-analysis, password-cracking, privilege-escalation, service-enumeration, stego-extraction, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, gobuster, nmap, steghide to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, gobuster, nmap, steghide to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `command that was used:`

### Step 2: Exploring Port 80 and 65524

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, cyberchef, gobuster, john with the extracted filter/query `It is just a static page that contains an image, nothing was found in the source code either. Note,` and inspect the matching evidence.
- Tools: binwalk, cyberchef, gobuster, john, nmap, steghide
- Filters or commands:
  - `It is just a static page that contains an image, nothing was found in the source code either. Note,`
  - `I explored the robots.txt file for port 80 but it contains nothing of use. I decided to download the`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, cyberchef, gobuster, john with the extracted filter/query `It is just a static page that contains an image, nothing was found in the source code either. Note,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `provided wordlist:`

### Step 3: Steganography

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, cyberchef, gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use binwalk, cyberchef, gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: Privileges Escalation

- Route type: `cyberchef-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, gobuster, nmap, steghide to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, gobuster, nmap, steghide to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Questions Answered:`

### Step 5: Using GoBuster, find flag 1

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use cyberchef, gobuster, nmap, steghide to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use cyberchef, gobuster, nmap, steghide to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o flag{f1rs7_fl4g}`

### Step 6: Further enumerate the machine, what is flag 2?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, gobuster, nmap, steghide to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, gobuster, nmap, steghide to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9fdafbd64c47471a8f54cd3fc64cd312`

### Step 7: Crack the hash with easypeasy.txt, What is the flag 3?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9fdafbd64c47471a8f54cd3fc64cd312`

### Step 8: Using the wordlist that is provided to you in this task crack the hash. What is the

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, gobuster, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, gobuster, nmap, steghide to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `o mypasswordforthatjob`

### Step 9: What is the root flag?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use cyberchef, gobuster, nmap, steghide to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: cyberchef, gobuster, nmap, steghide
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use cyberchef, gobuster, nmap, steghide to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `63a9f0ea7bb98050796b649e85481845`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
