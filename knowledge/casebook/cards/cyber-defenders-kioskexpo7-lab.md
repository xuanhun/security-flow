# KioskExpo7 Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_kioskexpo7_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, pe-malware challenges.

## Input Signals

- Artifacts: disk-image, email, pe-malware, registry
- Tools: capa, db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Techniques: browser-forensics, http-analysis, malware-dynamic, malware-static, privilege-escalation, registry-forensics, timeline-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Initial Access

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 2: browser instance outside kiosk restrictions?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://go.microsoft.com/fwlink/?LinkID=2004230`

### Step 3: executable configured to launch at kiosk start?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `msedge.exe`

### Step 4: What are the full command-line arguments used with the kiosk application?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `--no-first-run --kiosk file:///C:/Users/kiosk/Desktop/index.html --kiosk-idle-timeout-`

### Step 5: file downloaded by the threat actor after escaping the kiosk?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cmd.exe`

### Step 6: Privilege Escalation

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 7: threat actor downloaded the privilege escalation enumeration script?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://file.bsxwwdsdsa.dev/lightpeas.bat`

### Step 8: new process as the KioskAdmin user?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to enumerate processes, network sockets, injected regions, and command lines.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `runas /user:KioskAdmin powershell`

### Step 9: What is the name of the registry value that was set to 0 to disable User Account Control?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `EnableLUA`

### Step 10: When did the threat actor overwrite the PowerShell command history file to remove

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-10-18 09:43:28`

### Step 11: What is the name of this file in the recycle bin?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `$R0BD893.exe`

### Step 12: retrieved from the registry?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use capa, db-browser-sqlite, mftecmd, pecmd with the extracted filter/query `Contains critical Windows logon, logoff, startup, and shutdown processes. Within this key, there` and inspect the matching evidence.
- Tools: capa, db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Filters or commands:
  - `Contains critical Windows logon, logoff, startup, and shutdown processes. Within this key, there`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use capa, db-browser-sqlite, mftecmd, pecmd with the extracted filter/query `Contains critical Windows logon, logoff, startup, and shutdown processes. Within this key, there` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `KioskAdmin`

### Step 13: system's public IP address?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to recover or open the referenced file and inspect its metadata fields.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://ipinfo.io/json`

### Step 14: full folder path where the threat actor created the PowerShell persistence scripts?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `C:\ProgramData\Maintenance`

### Step 15: are the names of the two scheduled tasks created by the threat actor?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `KioskStatusCheck, KioskUpdate`

### Step 16: would be fetched and executed when the C2 server returned "1"?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `quickupdate.txt`

### Step 17: when was it placed on the desktop? (Format: filename, YYYY-MM-DD HH:MM:SS)

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `qr.png,2025-10-18 09:30:14`

### Step 18: legitimate registration page. What is the URL of the phishing page that is now displayed?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, mftecmd, pecmd, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, mftecmd, pecmd, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://registerr.wowzaconf.dev/register.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
