# Mr Robot

## Case Metadata

- Category: `Pentesting`
- Platform: `VulnHub`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/mr_robot_writeup.pdf`

## Why This Case Matters

Use this case as a Pentesting reference for web-service challenges.

## Input Signals

- Artifacts: web-service
- Tools: gobuster, hashcat, hydra, nikto, nmap, radare2, wpscan
- Techniques: http-analysis, password-cracking, privilege-escalation, service-enumeration, web-enumeration

## First-Principles Route

- Begin with service discovery and directory/application enumeration.
- Map each exposed service to default credentials, known CVEs, misconfiguration, or content leaks.
- After initial access, enumerate local privilege escalation paths before exploitation.

## Solve Thinking

### Step 1: Discovering the Target IP

- Route type: `gobuster-driven evidence lookup`
- Why: For Pentesting, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gobuster, hashcat, hydra, nikto to collect the smallest evidence slice that answers the goal.
- Tools: gobuster, hashcat, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as gobuster-driven evidence lookup.
  - Use gobuster, hashcat, hydra, nikto to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.100.13`

### Step 2: Enumeration:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, hashcat, hydra, nikto to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, hashcat, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, hashcat, hydra, nikto to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `o Ports: 22 (SSH), 80 and 443 (HTTP)`

### Step 3: Exploring Port 80

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, hashcat, hydra, nikto to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, hashcat, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, hashcat, hydra, nikto to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `source code revealed the site was running WordPress.`

### Step 4: Mr robots.txt

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, hashcat, hydra, nikto to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gobuster, hashcat, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, hashcat, hydra, nikto to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 5: Brute-Forcing Wordpress Login

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hashcat, hydra, nikto with the extracted filter/query `hydra -L cleaned_list.dic -p anything 192.168.100.13 http-post-form '/wp-` and inspect the matching evidence.
- Tools: gobuster, hashcat, hydra, nikto, nmap, radare2, wpscan
- Filters or commands:
  - `hydra -L cleaned_list.dic -p anything 192.168.100.13 http-post-form '/wp-`
  - `hydra -l elliot -P cleaned_list.dic 192.168.100.13 http-post-form '/wp-`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hashcat, hydra, nikto with the extracted filter/query `hydra -L cleaned_list.dic -p anything 192.168.100.13 http-post-form '/wp-` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.100.13`

### Step 6: Gaining a Reverse Shell

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hashcat, hydra, nikto to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hashcat, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hashcat, hydra, nikto to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Create a file and add the following code:`

### Step 7: Hash Cracking

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gobuster, hashcat, hydra, nikto to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gobuster, hashcat, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use gobuster, hashcat, hydra, nikto to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `We can now print the second key/flag:`

### Step 8: Privilege Escalation

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use gobuster, hashcat, hydra, nikto to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: gobuster, hashcat, hydra, nikto, nmap, wpscan
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use gobuster, hashcat, hydra, nikto to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - The proof is the service enumeration result and the exact access or escalation condition.
- Evidence rule: The proof is the service enumeration result and the exact access or escalation condition.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
