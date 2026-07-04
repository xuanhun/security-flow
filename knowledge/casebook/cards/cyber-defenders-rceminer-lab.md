# RCEMiner Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_rceminer_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: cyberchef, strings, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-static, network-forensics, service-enumeration, stego-extraction

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: identify how the attacker gained access and what actions they took on the compromised server.

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: initial access to the public webserver?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 3: When approaching network forensics, I like to begin by baselining the traffic, which involves

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - The proof is the packet/conversation statistic matching the exact endpoints and protocol.
- Evidence rule: The proof is the packet/conversation statistic matching the exact endpoints and protocol.

### Step 4: identify top talkers within this PCAP , we can navigate to Statistics > Conversations > IPv4:

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use strings, virustotal, wireshark with the extracted filter/query `conversations, and 1.80.23.4 is likely the threat actor or some sort of malicious IP. We can` and inspect the matching evidence.
- Tools: strings, virustotal, wireshark
- Filters or commands:
  - `conversations, and 1.80.23.4 is likely the threat actor or some sort of malicious IP. We can`
  - `http && ip.src == 36.96.48.3`
  - `ip.src == 36.96.48.3 && http`
  - `ip.dst == 36.96.48.3 && http && http.request.uri contains "%AD"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use strings, virustotal, wireshark with the extracted filter/query `conversations, and 1.80.23.4 is likely the threat actor or some sort of malicious IP. We can` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CVE-2024-4577`

### Step 5: Unicode code point of this character?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `As explained in advisories, and observed in the previous question, if a request contains a “soft` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `As explained in advisories, and observed in the previous question, if a request contains a “soft`
  - `ip.dst == 36.96.48.3 && http && http.request.uri contains "%AD"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `As explained in advisories, and observed in the previous question, if a request contains a “soft` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0xAD`

### Step 6: with elevated permissions?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark with the extracted filter/query `ip.src == 36.96.48.3 && http.request.method == GET` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `ip.src == 36.96.48.3 && http.request.method == GET`
  - `ip.dst == 36.96.48.3 && http.request.uri contains "%AD"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark with the extracted filter/query `ip.src == 36.96.48.3 && http.request.method == GET` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Start-Process C:\Windows\Temp\2.exe -Verb RunAs`

### Step 7: attacks from the compromised server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ThinkPHP`

### Step 8: involves the use of DNS queries for command-and-control purposes?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1071.004`

### Step 9: stored after being downloaded from the compromised server?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\ProgramData\spread.exe`

### Step 10: What is the IP address and port number to which this data was sent?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `ip.src == 36.96.48.3` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `ip.src == 36.96.48.3`
  - `ip.addr==36.96.48.3 && ip.addr==218.244.58.70 && tcp.port==9011`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `ip.src == 36.96.48.3` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `218.244.58.70:9011`

### Step 11: software and version was used?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `XMRig/5.5.0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
