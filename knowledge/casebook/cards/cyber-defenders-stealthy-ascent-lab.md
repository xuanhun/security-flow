# Stealthy Ascent Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_stealthy_ascent_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, linux-logs challenges.

## Input Signals

- Artifacts: email, linux-logs
- Tools: john, strings
- Techniques: browser-forensics, http-analysis, malware-static, password-cracking, privilege-escalation, service-enumeration, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: which encrypted t3m0’s downloads directory. Prior to ransomware deployment, the threat actor

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use john, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use john, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - The proof is the authentication field or stream showing the credential value.
- Evidence rule: The proof is the authentication field or stream showing the credential value.

### Step 2: What is the attacker's email address?

- Route type: `john-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use john, strings with the extracted filter/query `This folder contains the user’s Thunderbird emails. For context, Thunderbird is an open-source` and inspect the matching evidence.
- Tools: john, strings
- Filters or commands:
  - `This folder contains the user’s Thunderbird emails. For context, Thunderbird is an open-source`
  - `Within this folder, there is a file called “INBOX” which contains the user’s inbox. Let’s begin by`
  - `grep "From:" INBOX`
  - `grep "inf0.s3c1337@gmail.com" -A 25 INBOX`
- Reasoning chain:
  - Recognize the goal as john-driven evidence lookup.
  - Use john, strings with the extracted filter/query `This folder contains the user’s Thunderbird emails. For context, Thunderbird is an open-source` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `inf0.s3c1337@gmail.com`

### Step 3: What is the name of the attachment the attacker sent to the victim?

- Route type: `john-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use john, strings to collect the smallest evidence slice that answers the goal.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as john-driven evidence lookup.
  - Use john, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Important.docx`

### Step 4: What is the full URL the attacker used to download the malicious file on the victim's machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings with the extracted filter/query `grep 'filename="Important.docx"' -A 550 INBOX` and inspect the matching evidence.
- Tools: strings
- Filters or commands:
  - `grep 'filename="Important.docx"' -A 550 INBOX`
  - `cat <file_name> | base64 -d > out.docx`
  - `strings recovery.jsonlz4 | grep "update.sh"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings with the extracted filter/query `grep 'filename="Important.docx"' -A 550 INBOX` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://192.168.190.129/update.sh`

### Step 5: What is the full file path where this malicious persistence service was created?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use john, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use john, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/etc/systemd/system/persistence.service`

### Step 6: What is the path of the persistence file that is created or modified to maintain the attacker's access?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use john, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use john, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/tmp/P3r515t3nc3.sh`

### Step 7: related to safe browsing were flagged, specifically those with the .vlpset extension?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use john, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use john, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `goog-badbinurl-proto.vlpset, goog-downloadwhite-proto.vlpset, goog-malware-`

### Step 8: When did the attacker successfully connect to the victim for the first time?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use john, strings with the extracted filter/query `grep "Accepted password" auth.log` and inspect the matching evidence.
- Tools: john, strings
- Filters or commands:
  - `grep "Accepted password" auth.log`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use john, strings with the extracted filter/query `grep "Accepted password" auth.log` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-07-30 13:51`

### Step 9: What is the name of the file that is responsible for encrypting folders with the specific extension?

- Route type: `john-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use john, strings to collect the smallest evidence slice that answers the goal.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as john-driven evidence lookup.
  - Use john, strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ransomware.sh`

### Step 10: What is the original file path of the program that encrypts folders? We discovered this previously:

- Route type: `john-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use john, strings to collect the smallest evidence slice that answers the goal.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as john-driven evidence lookup.
  - Use john, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/home/t3m0/.local/share/Trash/files/ransomware.sh`

### Step 11: What is the encryption key the attacker used to encrypt the files?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use john, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use john, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `s3cr3t_k3y`

### Step 12: name of this file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use john to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: john
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use john to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `unshadowed.txt`

### Step 13: spawn a shell when the file was encrypted?

- Route type: `john-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use john, strings to collect the smallest evidence slice that answers the goal.
- Tools: john, strings
- Reasoning chain:
  - Recognize the goal as john-driven evidence lookup.
  - Use john, strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0,/bin/sh`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
