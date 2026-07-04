# TheTruth Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_thetruth_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for apk-mobile, disk-image, email challenges.

## Input Signals

- Artifacts: apk-mobile, disk-image, email, pe-malware
- Tools: autopsy, capa, db-browser-sqlite, jadx, john, virustotal
- Techniques: browser-forensics, cti-enrichment, http-analysis, malware-static, mobile-forensics, password-cracking, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Identify the suspect's friend he claims to have picked up from the airport. What is this friend's name?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use autopsy, db-browser-sqlite, jadx to align timestamps and identify the event that satisfies the question.
- Tools: autopsy, db-browser-sqlite, jadx
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use autopsy, db-browser-sqlite, jadx to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Shady`

### Step 2: of the last legitimate use of the credit card as per the suspect's browser data?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, db-browser-sqlite, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, db-browser-sqlite, jadx
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, db-browser-sqlite, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `19-12-2023 00:13:48`

### Step 3: address for the suspicious email received?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, db-browser-sqlite, jadx, john to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, db-browser-sqlite, jadx, john
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, db-browser-sqlite, jadx, john to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `john@numrent.com`

### Step 4: Can you determine the exact name of this APK file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, capa, db-browser-sqlite, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, capa, db-browser-sqlite, jadx
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, capa, db-browser-sqlite, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `numrent`

### Step 5: impact. What is the name of the malware family associated with the suspicious APK?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, db-browser-sqlite, jadx, virustotal with the extracted filter/query `gci -Recurse -Force | sls 'Numrent'` and inspect the matching evidence.
- Tools: autopsy, db-browser-sqlite, jadx, virustotal
- Filters or commands:
  - `gci -Recurse -Force | sls 'Numrent'`
  - `Rdw==\com.example.confirmcode-FPzER1iWROYkcvW1xvY9TA==\base.apk`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, db-browser-sqlite, jadx, virustotal with the extracted filter/query `gci -Recurse -Force | sls 'Numrent'` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ratmilad`

### Step 6: malware's C2 server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, db-browser-sqlite, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, db-browser-sqlite, jadx
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, db-browser-sqlite, jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `api.numrent.shop`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
