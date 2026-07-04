# Silent Breach

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_silent_breach_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, pe-malware challenges.

## Input Signals

- Artifacts: disk-image, email, pe-malware
- Tools: db-browser-sqlite, floss, ftk-imager, strings
- Techniques: browser-forensics, http-analysis, malware-static, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the MD5 hash of the potentially malicious EXE file the user downloaded?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, ftk-imager, strings to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, ftk-imager, strings
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, ftk-imager, strings to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `336a7cf476ebc7548c93507339196abb`

### Step 2: What is the URL from which the file was downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, strings
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://192.168.16.128:8000/IMF-Info.pdf.exe`

### Step 3: What application did the user use to download this file?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, ftk-imager, strings to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, ftk-imager, strings
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, ftk-imager, strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Microsoft Edge`

### Step 4: addresses of servers that are at risk or compromised. What are the IP addresses?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, floss, ftk-imager, strings with the extracted filter/query `# === Configuration ===` and inspect the matching evidence.
- Tools: db-browser-sqlite, floss, ftk-imager, strings
- Filters or commands:
  - `# === Configuration ===`
  - `# === Derive Key and IV ===`
  - `# === Decrypt Function ===`
  - `# === Main Script ===`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, floss, ftk-imager, strings with the extracted filter/query `# === Configuration ===` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `145.67.29.88, 212.33.10.112, 192.168.16.128`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
