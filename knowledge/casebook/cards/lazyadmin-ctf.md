# Lazy Admin

## Case Metadata

- Category: `Pentesting`
- Platform: `VulnHub`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/lazyadmin_ctf.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: gobuster, nmap
- Techniques: http-analysis, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Enumeration

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o Ports: 22 (SSH) and 80 (HTTP)`

### Step 2: Exploring Port 80

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `index.php`

### Step 3: Cracking the Hash

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: Logging into SweetRice

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `This worked!`

### Step 5: Exploiting SweetRice CMS

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap with the extracted filter/query `There is also a file that contains mysql_login creds (rice:randompass), so let’s go try login to` and inspect the matching evidence.
- Tools: gobuster, nmap
- Filters or commands:
  - `There is also a file that contains mysql_login creds (rice:randompass), so let’s go try login to`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap with the extracted filter/query `There is also a file that contains mysql_login creds (rice:randompass), so let’s go try login to` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `php-reverse-shell.php`

### Step 6: Privileges Escalation

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `copy.sh`

### Step 7: What is the user flag?

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, nmap to collect the smallest evidence slice that answers the goal.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `63e5bce9271952aad1113b6f1ac28a07`

### Step 8: What is the root flag?

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, nmap to collect the smallest evidence slice that answers the goal.
- Tools: gobuster, nmap
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6637f41d0177b6f37cb20d775124699f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
