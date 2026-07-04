# Phishy Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_phishy_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, ids, office-document challenges.

## Input Signals

- Artifacts: disk-image, ids, office-document, registry
- Tools: autopsy, cyberchef, db-browser-sqlite, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, maldoc-analysis, registry-forensics

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the hostname of the victim machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, cyberchef, ftk-imager, oledump to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, cyberchef, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, cyberchef, ftk-imager, oledump to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `WIN-NF3JQEU4G0T`

### Step 2: What is the messaging app installed on the victim machine?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use autopsy, cyberchef, ftk-imager, oledump with the extracted filter/query `Another approach is to look at the AppData\Local directory, which contains application-specific` and inspect the matching evidence.
- Tools: autopsy, cyberchef, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Filters or commands:
  - `Another approach is to look at the AppData\Local directory, which contains application-specific`
  - `the stream number. In this case, the highest stream that contains a macro is 10.`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use autopsy, cyberchef, ftk-imager, oledump with the extracted filter/query `Another approach is to look at the AppData\Local directory, which contains application-specific` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `WhatsApp`

### Step 3: The macro executed a program. Provide the program name?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use autopsy, cyberchef, ftk-imager, oledump to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: autopsy, cyberchef, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use autopsy, cyberchef, ftk-imager, oledump to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `powershell`

### Step 4: Where was the malicious file downloaded to? (Provide the full path)

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, cyberchef, ftk-imager, oledump to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, cyberchef, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, cyberchef, ftk-imager, oledump to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\Temp\IPhone.exe`

### Step 5: What is the name of the framework used to create the malware?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use autopsy, cyberchef, ftk-imager, oledump to extract macros, streams, embedded URLs, and decoded script content.
- Tools: autopsy, cyberchef, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use autopsy, cyberchef, ftk-imager, oledump to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Metasploit`

### Step 6: What is the attacker's IP address?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use autopsy, cyberchef, db-browser-sqlite, ftk-imager with the extracted filter/query `We can find a SQLite database called places.sqlite that contains the browsing history for` and inspect the matching evidence.
- Tools: autopsy, cyberchef, db-browser-sqlite, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Filters or commands:
  - `We can find a SQLite database called places.sqlite that contains the browsing history for`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use autopsy, cyberchef, db-browser-sqlite, ftk-imager with the extracted filter/query `We can find a SQLite database called places.sqlite that contains the browsing history for` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `155.94.69.27`

### Step 7: What is the password the user submitted to the login page?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use autopsy, cyberchef, ftk-imager, oledump to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: autopsy, cyberchef, ftk-imager, oledump, olevba, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use autopsy, cyberchef, ftk-imager, oledump to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `GacsriicUZMY4xiAF4yl`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
