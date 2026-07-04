# BlueSky Ransomware Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_bluesky_ransomware_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for disk-image, pcap, registry challenges.

## Input Signals

- Artifacts: disk-image, pcap, registry, windows-events
- Tools: cyberchef, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics, privilege-escalation, service-enumeration, timeline-analysis, windows-event-analysis

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: quickly. Can you identify the source IP responsible for potential port scanning activity?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.src_host==87.96.21.84` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `ip.src_host==87.96.21.84`
  - `tcp.flags.syn == 1 and tcp.flags.ack == 1 && (ip.dst == 87.96.21.84) &&`
  - `(ip.src == 87.96.21.81)`
  - `_path=="conn" id.orig_h==87.96.21.84 | cut id.resp_p | sort id.resp_p desc`
  - `_path=="conn" | count() by id.orig_h`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.src_host==87.96.21.84` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `87.96.21.84`

### Step 2: Can you identify the targeted account username?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `(ip.src_host==87.96.21.84) && (tds)` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `(ip.src_host==87.96.21.84) && (tds)`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `(ip.src_host==87.96.21.84) && (tds)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sa`

### Step 3: correct password discovered by the attacker?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cyb3rd3f3nd3r$`

### Step 4: What setting did the attacker enable to control the target host further and execute further commands?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `xp_cmdshell`

### Step 5: process did the attacker inject the C2 into to gain administrative privileges?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `MSFConsole (Metasploit) injected code inside the Winlogon process, likely to escalate` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `MSFConsole (Metasploit) injected code inside the Winlogon process, likely to escalate`
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `MSFConsole (Metasploit) injected code inside the Winlogon process, likely to escalate` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `winlogon.exe`

### Step 6: the URL of this file downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `(http) && (http.request.method==GET) && (ip.src_host==87.96.21.81)` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `(http) && (http.request.method==GET) && (ip.src_host==87.96.21.81)`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `(http) && (http.request.method==GET) && (ip.src_host==87.96.21.81)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://87.96.21.84/checking.ps1`

### Step 7: provide the specific Group SID that is being checked?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use cyberchef, virustotal, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use cyberchef, virustotal, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `S-1-5-32-544`

### Step 8: Can you determine the URL of the second file downloaded by the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `(http) && (http.request.method==GET) && (ip.src_host==87.96.21.81)` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `(http) && (http.request.method==GET) && (ip.src_host==87.96.21.81)`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `(http) && (http.request.method==GET) && (ip.src_host==87.96.21.81)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://87.96.21.84/del.ps1`

### Step 9: attacker to maintain persistence?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `\Microsoft\Windows\MUI\LPupdate`

### Step 10: the second file tries to accomplish?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `TA0005`

### Step 11: What's the invoked PowerShell script used by the attacker for dumping credentials?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `Within the ichigo-lite.ps1 script, it contains a variable called $hashesContent that reads the` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `Within the ichigo-lite.ps1 script, it contains a variable called $hashesContent that reads the`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `Within the ichigo-lite.ps1 script, it contains a variable called $hashesContent that reads the` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Invoke-PowerDump.ps1`

### Step 12: file containing the discovered hosts?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `extracted_hosts.txt`

### Step 13: performing behavioral analysis, what’s the name of the ransom note file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `# DECRYPT FILES BLUESKY #`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
