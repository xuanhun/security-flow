# DetectLog4j Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_detectlog4j_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, ids, pe-malware challenges.

## Input Signals

- Artifacts: disk-image, ids, pe-malware, registry, siem, windows-events
- Tools: cyberchef, dnspy, john, registry-explorer, splunk, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-dynamic, password-cracking, registry-forensics, reverse-engineering, service-enumeration, siem-query, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the version of the VMware product installed on the machine?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal with the extracted filter/query `o Contains information about installed applications, including the display name,` and inspect the matching evidence.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Filters or commands:
  - `o Contains information about installed applications, including the display name,`
  - `o Like the previous key but contains information about applications installed for`
  - `o Contains the path to the executable for each installed application.`
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal with the extracted filter/query `o Contains information about installed applications, including the display name,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6.7.0`

### Step 2: What is the version of the log4j library used by the installed VMware product?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2.11.2`

### Step 3: vulnerable. What is the first link of the log4huntress payload?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, john, registry-explorer to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, john, registry-explorer, splunk, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, john, registry-explorer to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `log4shell.huntress.com:1389/b1292f3c-a652-4240-8fb4-59c43141f55a`

### Step 4: What is the attacker's IP address?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.112.128`

### Step 5: What is the script name published by VMware to mitigate log4shell vulnerability?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `vc_log4j_mitigator.py`

### Step 6: the system property needed to set to 'true' to work around the log4shell vulnerability?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `log4j2.formatMsgNoLookups`

### Step 7: identify the earliest version of Log4j that introduced a patch to mitigate this critical vulnerability.

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2.15.0`

### Step 8: What is the value stored in the CONTAINER_JNDI_RESOURCE_PATH_PREFIX variable?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `java:comp/env/`

### Step 9: What is the executable used by the attacker to gain persistence?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `baaaackdooor.exe`

### Step 10: decrypt the URL?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, dnspy, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `GoaahQrC`

### Step 11: What is the ISP that owns that IP that serves the text file?. Use your host for this question

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, dnspy, registry-explorer, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `amazon`

### Step 12: is the second extension the ransomware checks for?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, dnspy, registry-explorer, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, dnspy, registry-explorer, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ini`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
