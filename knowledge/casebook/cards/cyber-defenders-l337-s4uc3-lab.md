# l337 S4uc3 Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_l337_S4uc3_Lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, memory, pcap challenges.

## Input Signals

- Artifacts: ids, memory, pcap
- Tools: suricata, virustotal, volatility, wireshark, zeek
- Techniques: cti-enrichment, dns-analysis, http-analysis, memory-forensics, network-forensics, timeline-analysis

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: received earlier today. First, determine the Public IP Address of the webserver?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `74.204.41.73`

### Step 2: PCAP: What version number of PHP is the development.wse.local server running?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5.3.2`

### Step 3: PCAP: What version number of Apache is the development.wse.local web server using?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2.2.14`

### Step 4: IR: What is the common name of the malware reported by the IDS alert provided?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use volatility, wireshark with the extracted filter/query `Within the references section of the alert, you can file a link that contains a query to zeus, we` and inspect the matching evidence.
- Tools: volatility, wireshark
- Filters or commands:
  - `Within the references section of the alert, you can file a link that contains a query to zeus, we`
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use volatility, wireshark with the extracted filter/query `Within the references section of the alert, you can file a link that contains a query to zeus, we` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `zeus`

### Step 5: connectivity. What was the IP address of the website pinged?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use suricata, volatility, wireshark, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: suricata, volatility, wireshark, zeek
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use suricata, volatility, wireshark, zeek to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `74.125.225.112`

### Step 6: WordPress page around 6:59 PM EST?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use volatility, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use volatility, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wM812ugu`

### Step 7: the access time or you will be fired. Please provide the time of the accessed Designs page?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use volatility, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use volatility, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `23:04:04 UTC`

### Step 8: run by the attacker?

- Route type: `volatility-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use volatility, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as volatility-driven evidence lookup.
  - Use volatility, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2.6.32-38-server`

### Step 9: PCAP: What is the value of the token passed in frame 3897?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b7aad621db97d56771d6316a6d0b71e9`

### Step 10: PCAP: What is the download file name the user launched the Zeus bot?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, volatility, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, volatility, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bt.exe`

### Step 11: Memory: What is the Parent Process ID of the two 'sh' sessions?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility, wireshark to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility, wireshark to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1042`

### Step 12: Memory: What is the latency_record_count for PID 1274?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility, wireshark to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility, wireshark to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0`

### Step 13: Memory: For the PID 1274, what is the first mapped file path?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility, wireshark to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility, wireshark to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

### Step 14: which shows details of process memory, including heaps, stacks, and shared libraries.

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: volatility, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/bin/dash`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
