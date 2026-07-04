# Colddbox Vulnhub

## Case Metadata

- Category: `Pentesting`
- Platform: `VulnHub`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/colddbox_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: gobuster, hydra, nikto, nmap, wpscan
- Techniques: browser-forensics, http-analysis, password-cracking, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Discovering the Target IP

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, hydra, nmap, wpscan to collect the smallest evidence slice that answers the goal.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, hydra, nmap, wpscan to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.100.14`

### Step 2: Enumeration:

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

### Step 3: Exploring Port 80

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, hydra, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, hydra, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 4: Brute Forcing Login Page

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, nmap, wpscan with the extracted filter/query `hydra -l C0ldd -P /usr/share/wordlists/rockyou.txt 192.168.100.14 http-post-form '/wp-` and inspect the matching evidence.
- Tools: gobuster, hydra, nmap, wpscan
- Filters or commands:
  - `hydra -l C0ldd -P /usr/share/wordlists/rockyou.txt 192.168.100.14 http-post-form '/wp-`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, nmap, wpscan with the extracted filter/query `hydra -l C0ldd -P /usr/share/wordlists/rockyou.txt 192.168.100.14 http-post-form '/wp-` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.100.14`

### Step 5: Gaining a Reverse Shell

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Create a file and add the following code:`

### Step 6: Privilege Escalation (horizontal and vertical)

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use gobuster, hydra, nmap, wpscan to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use gobuster, hydra, nmap, wpscan to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `wp-config.php`

### Step 7: which we can look at to find stored credentials:

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hydra, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `This translates to ‘Congratulations, machine completed!’ .`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
