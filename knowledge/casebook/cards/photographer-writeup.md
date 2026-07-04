# Photographer

## Case Metadata

- Category: `Pentesting`
- Platform: `VulnHub`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/photographer_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for email, web-service challenges.

## Input Signals

- Artifacts: email, web-service
- Tools: burp, gobuster, nikto, nmap
- Techniques: http-analysis, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Discovering the Target IP

- Route type: `burp-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, gobuster, nikto, nmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as burp-driven evidence lookup.
  - Use burp, gobuster, nikto, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.100.16`

### Step 2: Enumeration:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use burp, gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 3: Exploring Port 80

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use burp, gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `source code:`

### Step 4: Exploring Port 8000

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use burp, gobuster, nikto, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `shell.php`

### Step 5: Brute Forcing and Scanning

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use burp, gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use burp, gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `page.`

### Step 6: Analysing SMB Shares

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use burp, gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use burp, gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wp-config-sample.php`

### Step 7: Exploiting Koken CMS

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use burp, gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use burp, gobuster, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `reverse-shell.php`

### Step 8: Privileges Escalation

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use burp, gobuster, nikto, nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: burp, gobuster, nikto, nmap
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use burp, gobuster, nikto, nmap to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `hacking!`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
