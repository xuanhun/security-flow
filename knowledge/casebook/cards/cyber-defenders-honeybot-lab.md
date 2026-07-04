# HoneyBOT Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_honeybot_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: virustotal, wireshark
- Techniques: cti-enrichment, http-analysis, network-forensics, service-enumeration

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the attacker's IP address?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - The proof is the packet/conversation statistic matching the exact endpoints and protocol.
- Evidence rule: The proof is the packet/conversation statistic matching the exact endpoints and protocol.

### Step 2: When approaching network forensics, I like to begin by baselining the traffic, which involves

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `98.114.205.102`

### Step 3: how 98.114.205.102 is connecting to 192.150.11.111 over known ports like 445 (SMB).

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `98.114.205.102`

### Step 4: What is the target's IP address?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.150.11.111`

### Step 5: How many TCP sessions are present in the captured traffic?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5`

### Step 6: How long did it take to perform the attack (in seconds)?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `16`

### Step 7: Which protocol was used to carry over the exploit?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use virustotal, wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use virustotal, wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `SMB`

### Step 8: Which protocol did the attacker use to download additional malicious files to the target system?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark with the extracted filter/query `tcp.stream eq 3` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `tcp.stream eq 3`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark with the extracted filter/query `tcp.stream eq 3` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ftp`

### Step 9: What is the name of the downloaded malware?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal, wireshark with the extracted filter/query `_path=="files" source=="FTP_DATA"` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `_path=="files" source=="FTP_DATA"`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal, wireshark with the extracted filter/query `_path=="files" source=="FTP_DATA"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ssms.exe`

### Step 10: When was the involved malware first submitted to VirusTotal for analysis? Format: YYYY- MM-DD

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, wireshark to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, wireshark to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2007-06-27`

### Step 11: What is the key used to encode the shellcode?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0x99`

### Step 12: What is the port number the shellcode binds to?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1957`

### Step 13: OS file being queried during this process?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 14: which is a function of Kernel32.dll.

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Kernel32.dll`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
