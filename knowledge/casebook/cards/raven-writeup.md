# Raven 1

## Case Metadata

- Category: `Pentesting`
- Platform: `VulnHub`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/raven_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: gobuster, hydra, john, nikto, nmap, wpscan
- Techniques: http-analysis, password-cracking, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Discovering the Target IP

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, hydra, nikto, nmap to collect the smallest evidence slice that answers the goal.
- Tools: gobuster, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, hydra, nikto, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.100.17`

### Step 2: Enumeration:

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, nikto, nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `the accounts might be for SSH.`

### Step 3: find the wp-config.php file which contains hardcoded credentials like seen below:

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hydra, john, nikto to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hydra, john, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hydra, john, nikto to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `config.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
