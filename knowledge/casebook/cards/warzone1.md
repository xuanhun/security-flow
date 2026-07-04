# Warzone 1

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/warzone1.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: cyberchef, suricata, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What was the alert signature for Malware Command and Control Activity Detected?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use suricata, virustotal, wireshark with the extracted filter/query `event_type=="alert" | cut src_ip, dest_ip, dest_port, alert.signature` and inspect the matching evidence.
- Tools: suricata, virustotal, wireshark
- Filters or commands:
  - `event_type=="alert" | cut src_ip, dest_ip, dest_port, alert.signature`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use suricata, virustotal, wireshark with the extracted filter/query `event_type=="alert" | cut src_ip, dest_ip, dest_port, alert.signature` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- event_type=="alert" | cut src_ip, dest_ip, dest_port, alert.signature`

### Step 2: What is the source IP address? Enter your answer in a defanged format.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What IP address was the destination IP in the alert? Enter your answer in a defanged format.

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `threat group TA505 which is the answer:`

### Step 4: What is the malware family?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `MirrorBlast is a trojan that targets browsers.`

### Step 5: listed under Communicating Files?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Windows Installer.`

### Step 6: Inspect the web traffic for the flagged IP address; what is the user-agent in the traffic?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, suricata, virustotal, wireshark with the extracted filter/query `_path=="http" id.orig_h==172.16.1.102 | cut id.orig_h, id.resp_h, id.resp_p,` and inspect the matching evidence.
- Tools: cyberchef, suricata, virustotal, wireshark
- Filters or commands:
  - `_path=="http" id.orig_h==172.16.1.102 | cut id.orig_h, id.resp_h, id.resp_p,`
  - `method,host, uri, user_agent | uniq -c`
  - `_path=="http" id.resp_h!=169.239.128.11 | cut id.orig_h, id.resp_h, id.resp_p,`
  - `method,host, uri | uniq -c`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, suricata, virustotal, wireshark with the extracted filter/query `_path=="http" id.orig_h==172.16.1.102 | cut id.orig_h, id.resp_h, id.resp_p,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `172.16.1.102`

### Step 7: What were the file names of the downloaded files? Enter the answer in the order to the IP

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `each step is clearly documented and easily reproducible.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
