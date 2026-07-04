# RevengeHotels APT Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_revengehotels_apt_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, ids, pe-malware challenges.

## Input Signals

- Artifacts: email, ids, pe-malware, registry, windows-events
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd, virustotal
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, malware-dynamic, reverse-engineering, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: name of the JavaScript file downloaded from the phishing link?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd with the extracted filter/query `Here we can find a History file that contains the users Google chrome browsing history. Using a` and inspect the matching evidence.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Filters or commands:
  - `Here we can find a History file that contains the users Google chrome browsing history. Using a`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd with the extracted filter/query `Here we can find a History file that contains the users Google chrome browsing history. Using a` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `• \Users\<username>\AppData\Local\Google\Chrome\User Data\Default`

### Step 2: which contains information about downloaded files. Here we can find a file called “invoice82962.js” downloaded from hxxps[://]hotelx[.]rf[.]gd/?i=1:

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `invoice82962.js`

### Step 3: initial infection. What is the complete domain name that hosted the malicious JS file?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `hotelx.rf.gd`

### Step 4: directory path where the PowerShell script was created from the JS file?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Public\Scripts`

### Step 5: their true nature. What is the actual file type of the second downloaded file?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `exe`

### Step 6: executed it. What is the name of the executed file that was run after conversion?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `swchost.exe`

### Step 7: system defenses. How many registry keys were edited by the malicious executable?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `12`

### Step 8: What is the IP address of the C2 server that the malicious executable contacted?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3.122.239.15`

### Step 9: location. What is the full path where the malware copied itself?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Administrator\AppData\Roaming\host\swchost.exe`

### Step 10: executable for persistence?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `KOoNLZeCGlnQ.vbs`

### Step 11: executable use to mark its process as critical to the system?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, db-browser-sqlite, dnspy, evtxecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, db-browser-sqlite, dnspy, evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `RtlSetProcessIsCritical`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
