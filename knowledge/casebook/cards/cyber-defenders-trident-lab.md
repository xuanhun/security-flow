# Trident Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_trident_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, ids, pcap challenges.

## Input Signals

- Artifacts: email, ids, pcap
- Tools: ida, strings, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-static, network-forensics, reverse-engineering, stego-extraction

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the victim's email address?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use ida, strings, virustotal, wireshark with the extracted filter/query `responses” . This email also contains a Word document. Given the wording of the email and the` and inspect the matching evidence.
- Tools: ida, strings, virustotal, wireshark
- Filters or commands:
  - `responses” . This email also contains a Word document. Given the wording of the email and the`
  - `The malicious document file contains a URL to a malicious HTML file. Provide the URL for`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use ida, strings, virustotal, wireshark with the extracted filter/query `responses” . This email also contains a Word document. Given the wording of the email and the` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `joshua@cyberdefenders.org`

### Step 2: What is the Microsoft Office version installed on the victim machine?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use ida, strings, virustotal, wireshark with the extracted filter/query `ip.src==192.168.112.139 && ip.dst==192.168.112.128 && http` and inspect the matching evidence.
- Tools: ida, strings, virustotal, wireshark
- Filters or commands:
  - `ip.src==192.168.112.139 && ip.dst==192.168.112.128 && http`
  - `_path=="http" | count() by user_agent | sort -r count`
  - `The malicious HTML contains a js code that points to a malicious CAB file. Provide the URL`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use ida, strings, virustotal, wireshark with the extracted filter/query `ip.src==192.168.112.139 && ip.dst==192.168.112.128 && http` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `15.0.4517`

### Step 3: to the CAB file?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `http://192.168.112.128/word.cab`

### Step 4: The exploit takes advantage of a CAB vulnerability. Provide the vulnerability name?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ZipSlip`

### Step 5: Analyzing the dll file what is the API used to write the shellcode in the process memory?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, strings, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, strings, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ida, strings, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `rundll32.exe`

### Step 6: What stands out is the WriteProcessMemory function, which is used to write data to an area of memory in a specified process. Given this and other imports, we can assume that this malware

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `WriteProcessMemory`

### Step 7: when WriteProcessMemory is called to identify where the shellcode payload is located. Extract

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, strings, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, strings, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ida, strings, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wininet`

### Step 8: Which port was configured to receive the reverse shell?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use ida, virustotal, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `443`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
