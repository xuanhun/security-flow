# Kraken Keylogger Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_krakenkeylogger_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: cyberchef, db-browser-sqlite
- Techniques: dns-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the the web messaging app the employee used to talk to the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Telegram`

### Step 2: What is the password for the protected ZIP file sent by the attacker to the employee?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `@1122d`

### Step 3: What domain did the attacker use to download the second stage of the malware? This zip file can be found in OMEN’s Download directory, within this ZIP file is a shortcut (.lnk) file:

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, db-browser-sqlite to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, db-browser-sqlite
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, db-browser-sqlite to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `masherofmasters.cyou`

### Step 4: LOLAPPS on the machine to achieve persistence?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `jlhgfjhdflghjhuhuh`

### Step 5: What is the complete path of the malicious file that the attacker used to achieve persistence?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\OMEN\AppData\Local\Temp\templet.lnk`

### Step 6: What is the name of the application the attacker utilized for data exfiltration?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AnyDesk`

### Step 7: What is the IP address of the attacker?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, db-browser-sqlite with the extracted filter/query `In order to find the IP address of the attacker, we need to examine the ad.trace file contains` and inspect the matching evidence.
- Tools: cyberchef, db-browser-sqlite
- Filters or commands:
  - `In order to find the IP address of the attacker, we need to examine the ad.trace file contains`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, db-browser-sqlite with the extracted filter/query `In order to find the IP address of the attacker, we need to examine the ad.trace file contains` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `77.232.122.31`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
