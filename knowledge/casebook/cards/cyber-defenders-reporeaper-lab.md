# RepoReaper Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_reporeaper_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, email, ids challenges.

## Input Signals

- Artifacts: disk-image, email, ids, registry, windows-events
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, privilege-escalation, registry-forensics, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: analysis checks by testing whether Malwarebytes was installed on the host. Malware

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `regasm.exe`

### Step 2: from which the user downloaded the infected open-source tool?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://github.com/mo4de1/Script2Scene`

### Step 3: When did the user download the malicious tool?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to align timestamps and identify the event that satisfies the question.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-07-11 15:15`

### Step 4: during the project compilation process?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Clcw.ps1.ps1`

### Step 5: was downloaded for payload deployment?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4359ce22-2f6d-43b8-b34d-063d74715562.7z`

### Step 6: core Electron application?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `BD8CB26657654E9CF107AF2218564AB2`

### Step 7: created by the malware?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `RegisterDeviceSecurityAlert, RegisterDevicePowerStateChange,`

### Step 8: exploited by the JavaScript code to achieve privilege escalation?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ComputerDefaults.exe`

### Step 9: When were the registry values modified to disable system backup functionality?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-07-11 15:19`

### Step 10: PowerShell script checks for during execution?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Program Files\Malwarebytes\Anti-Malware\mbuns.exe`

### Step 11: decrypted by the malware loader?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `boot_f, kernel_f, thread_f`

### Step 12: as a legitimate application but was actually dropped by the Electron-based malware?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `NVIDIA CONTROL PANEL.EXE`

### Step 13: command and control server used for data exfiltration?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `api.telegram.org`

### Step 14: SHA1 hash of the executable sample among the related files?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, ftk-imager, mftecmd, pecmd, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, ftk-imager, mftecmd, pecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `27d730e3d16419339d03f4bace3e1c41d7d41cbd`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
