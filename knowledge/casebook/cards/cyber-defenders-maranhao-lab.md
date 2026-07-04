# Maranhao Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_maranhao_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, registry, windows-events challenges.

## Input Signals

- Artifacts: disk-image, registry, windows-events
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, malware-dynamic, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: disguised as a legitimate game utility?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://drive.usercontent.google.com/uc?id=1mIxhfZXmcUT2mbKNuahsRI4S_rzVUFKW&export`

### Step 2: adversary's delivery vector entering the victim environment as a ZIP file?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-09-17 10:10`

### Step 3: uniquely represents the dropper binary that initiated further payload deployment?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `FCB94C06FA80CE277B47E545B3805AB38BB6ACF4`

### Step 4: C2 identification. What globally unique string was provided as the argument?

- Route type: `db-browser-sqlite-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to collect the smallest evidence slice that answers the goal.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as db-browser-sqlite-driven evidence lookup.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e90de8b2-eb79-4614-94f8-308f0f81573b`

### Step 5: mechanism to guarantee re-execution after reboot?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Levi\AppData\Local\Programs\Microsoft Updater\updater.exe`

### Step 6: locked in. What is the date and time this key entry was created?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2025-09-17 10:13`

### Step 7: directories hidden and system-protected?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to recover or open the referenced file and inspect its metadata fields.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to recover or open the referenced file and inspect its metadata fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `attrib +h +s`

### Step 8: exact query facilitated this operating system enumeration?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `wmic os get Caption`

### Step 9: machine. Which query would return the video controller model?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `wmic path win32_VideoController get Name`

### Step 10: responsible for collecting this globally unique identifier?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `wmic csproduct get UUID`

### Step 11: produced this disk inventory?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wmic logicaldisk get Caption,FreeSpace,Size,Description /format:list`

### Step 12: terminate all browser processes?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `taskkill /F /IM msedge.exe`

### Step 13: named pipe was created to ferry stolen browser data?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ChromeDecryptIPC_e7e223c5-50d5-40ae-8513-64c9962789c2`

### Step 14: resolver. Which service endpoint did it query?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ip-api.com`

### Step 15: geolocation API. Which single IP must be blacklisted?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `208.95.112.1`

### Step 16: attacker infrastructure. Which two IP addresses were returned as part of this resolution?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: db-browser-sqlite, evtxecmd, ftk-imager, mftecmd, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use db-browser-sqlite, evtxecmd, ftk-imager, mftecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `104.21.71.100, 172.67.144.96`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
