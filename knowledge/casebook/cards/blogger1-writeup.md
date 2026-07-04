# Blogger1

## Case Metadata

- Category: `Pentesting`
- Platform: `VulnHub`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/blogger1_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: burp, gobuster, nmap, wpscan
- Techniques: http-analysis, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Discovering the Target IP

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, nmap, wpscan to collect the smallest evidence slice that answers the goal.
- Tools: gobuster, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, nmap, wpscan to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.100.20`

### Step 2: Enumeration:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o Ports: 22 (SSH) and 80 (HTTP)`

### Step 3: Exploring Port 80

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: Enumerating WordPress

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, nmap, wpscan to collect the smallest evidence slice that answers the goal.
- Tools: gobuster, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, nmap, wpscan to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: Exploiting the RCE Vulnerability

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, gobuster, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, gobuster, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use burp, gobuster, nmap, wpscan to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `php-reverse-shell.php`

### Step 6: Finding the Flags

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap, wpscan with the extracted filter/query `If you navigate to the home directory, you can see a directory for james that contains a flag,` and inspect the matching evidence.
- Tools: gobuster, nmap, wpscan
- Filters or commands:
  - `If you navigate to the home directory, you can see a directory for james that contains a flag,`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap, wpscan with the extracted filter/query `If you navigate to the home directory, you can see a directory for james that contains a flag,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `unfortunately we don’t have permission to view it:`

### Step 7: Privilege Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap, wpscan to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `hacking!`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
