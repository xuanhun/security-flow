# AfricanFalls Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_africanfalls_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, web-service challenges.

## Input Signals

- Artifacts: disk-image, email, web-service
- Tools: db-browser-sqlite, ftk-imager, john, nmap, pecmd
- Techniques: browser-forensics, password-cracking, service-enumeration, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the MD5 hash value of the suspect disk?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: ftk-imager, pecmd
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9471e69c95d8909ae60ddff30d50ffa1`

### Step 2: What phrase did the suspect search for on 2021-04-29 18:17:38 UTC? (three words, two spaces in between)

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, ftk-imager, john, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, ftk-imager, john, pecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, ftk-imager, john, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `password cracking lists`

### Step 3: What is the IPv4 address of the FTP server the suspect connected to?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager, john, pecmd with the extracted filter/query `see that FileZilla is present. Within the FileZilla directory is a recentservers.xml file that contains` and inspect the matching evidence.
- Tools: ftk-imager, john, pecmd
- Filters or commands:
  - `see that FileZilla is present. Within the FileZilla directory is a recentservers.xml file that contains`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager, john, pecmd with the extracted filter/query `see that FileZilla is present. Within the FileZilla directory is a recentservers.xml file that contains` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.1.20`

### Step 4: What date and time was a password list deleted in UTC? (YYYY-MM-DD HH:MM:SS UTC)

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use ftk-imager, pecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: ftk-imager, pecmd
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use ftk-imager, pecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2021-04-29 18:22:17 UTC`

### Step 5: How many times was Tor Browser ran on the suspect's computer? (number only)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager, pecmd
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager, pecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0`

### Step 6: What is the suspect's email address?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, pecmd
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, pecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dreammaker82@protonmail.com`

### Step 7: What is the FQDN did the suspect port scan?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ftk-imager, nmap, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ftk-imager, nmap, pecmd
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use ftk-imager, nmap, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dfir.science`

### Step 8: What country was picture "20210429_152043.jpg" allegedly taken in?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use ftk-imager, pecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: ftk-imager, pecmd
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use ftk-imager, pecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Zambia`

### Step 9: copy it to "contact" folder on his desktop?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager, john, pecmd to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager, john, pecmd
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager, john, pecmd to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Camera`

### Step 10: A Windows password hashes for an account are below. What is the user's password?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ftk-imager, pecmd
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `AFR1CA!`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
