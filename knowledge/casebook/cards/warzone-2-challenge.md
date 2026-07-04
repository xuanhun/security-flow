# Warzone 2

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/warzone_2_challenge.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: cyberchef, ida, suricata, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics, reverse-engineering

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What was the alert signature for a Network Trojan Was Detected?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, suricata, virustotal, wireshark with the extracted filter/query `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip, alert.signature |` and inspect the matching evidence.
- Tools: cyberchef, suricata, virustotal, wireshark
- Filters or commands:
  - `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip, alert.signature |`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, suricata, virustotal, wireshark with the extracted filter/query `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip, alert.signature |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `sort alerts`

### Step 2: What was the alert signature for Potential Corporate Privacy Violation?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, suricata, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, suricata, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, suricata, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `signature:`

### Step 3: What was the IP to trigger either alert? Enter your answer in a defanged format.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, suricata, virustotal, wireshark with the extracted filter/query `_path=="http" 185.118.164.8 | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri | uniq` and inspect the matching evidence.
- Tools: cyberchef, suricata, virustotal, wireshark
- Filters or commands:
  - `_path=="http" 185.118.164.8 | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri | uniq`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, suricata, virustotal, wireshark with the extracted filter/query `_path=="http" 185.118.164.8 | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri | uniq` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `185.118.164.8`

### Step 4: What is the name of the payload within the cab file?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `draw.dll`

### Step 5: What is the user-agent associated with this network traffic?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `_path=="http" 185.118.164.8 | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri,` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `_path=="http" 185.118.164.8 | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri,`
  - `user_agent | uniq -c`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `_path=="http" 185.118.164.8 | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri,` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `185.118.164.8`

### Step 6: What other domains do you see in the network traffic that are labelled as malicious by

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 7: determine that a-zcorner.com and knockoutlights.com are malicious domains

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, ida, suricata, virustotal with the extracted filter/query `event_type=="alert" "Not Suspicious Traffic" | cut src_ip, dest_ip, alert.category,` and inspect the matching evidence.
- Tools: cyberchef, ida, suricata, virustotal, wireshark
- Filters or commands:
  - `event_type=="alert" "Not Suspicious Traffic" | cut src_ip, dest_ip, alert.category,`
  - `64.225.65.166 | cut query`
  - `142.93.211.176 | cut query`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, ida, suricata, virustotal with the extracted filter/query `event_type=="alert" "Not Suspicious Traffic" | cut src_ip, dest_ip, alert.category,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `64.225.65.166`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
