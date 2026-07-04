# XMLRat Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_xlmrat_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap, pe-malware challenges.

## Input Signals

- Artifacts: pcap, pe-malware
- Tools: cyberchef, detect-it-easy, pestudio, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-static, network-forensics, timeline-analysis

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: When investigating a packet capture I am not familiar with, I like to begin by checking Statistics

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://45.126.209.4:222/mdm.jpg`

### Step 2: Which hosting provider owns the associated IP address?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ReliableSite.Net`

### Step 3: executable. What is the SHA256 of the malware executable?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1eb7b02e18f67420f42b1d94e74f3b6289d92672a0fb1786c30c03d68e81d798`

### Step 4: What is the malware family label based on Alibaba?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AsyncRat`

### Step 5: What is the timestamp of the malware's creation?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef, detect-it-easy, pestudio, virustotal to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef, detect-it-easy, pestudio, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef, detect-it-easy, pestudio, virustotal to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2023-10-30 15:08`

### Step 6: Which LOLBin is leveraged for stealthy process execution in this script? Provide the full path.

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, virustotal, wireshark to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegSvcs.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
