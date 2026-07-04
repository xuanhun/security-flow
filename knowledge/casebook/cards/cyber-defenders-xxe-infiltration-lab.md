# XXE Infiltration Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_xxe_infiltration_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: radare2, suricata, wireshark, zeek
- Techniques: http-analysis, network-forensics, timeline-analysis

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: which contained MySQL database credentials. The XXE vulnerability was further used to drop a

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `booking.php`

### Step 2: which suggests a potential XXE (XML External Entity) Injection attack. This raises concerns

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `immediate investigation.`

### Step 3: identify how the attacker gained access and what actions they took.

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: is open on the victim's web server?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark with the extracted filter/query `tcp.flags.syn==1 && tcp.flags.ack==1` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `tcp.flags.syn==1 && tcp.flags.ack==1`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use wireshark with the extracted filter/query `tcp.flags.syn==1 && tcp.flags.ack==1` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3306`

### Step 5: the vulnerability. What's the complete URI of the PHP script vulnerable to XXE Injection?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use suricata, wireshark, zeek with the extracted filter/query `Zeek, Suricata, and Wireshark into a user-friendly GUI application. Using the following filter, we` and inspect the matching evidence.
- Tools: suricata, wireshark, zeek
- Filters or commands:
  - `Zeek, Suricata, and Wireshark into a user-friendly GUI application. Using the following filter, we`
  - `_path=="http" | cut ts, id.orig_h, id.resp_h, method, host, uri,`
  - `user_agent | method=="POST"`
  - `http.request.method==POST`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use suricata, wireshark, zeek with the extracted filter/query `Zeek, Suricata, and Wireshark into a user-friendly GUI application. Using the following filter, we` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/review/upload.php`

### Step 6: name of the first malicious XML file uploaded by the attacker?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark with the extracted filter/query `_path=="files" | mime_type=="application/xml" |` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `_path=="files" | mime_type=="application/xml" |`
  - `id.orig_h==210.106.114.183`
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark with the extracted filter/query `_path=="files" | mime_type=="application/xml" |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `TheGreatGatsby.xml`

### Step 7: impact. What's the name of the web app configuration file the attacker read?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark with the extracted filter/query `http.request.method==POST` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `http.request.method==POST`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark with the extracted filter/query `http.request.method==POST` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `config.php`

### Step 8: user?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use radare2, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: radare2, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use radare2, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Winter2024`

### Step 9: connection to the MySQL server using the compromised credentials after the exposure?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-05-31 12:08`

### Step 10: of the web shell that the attacker uploaded for remote code execution and persistence?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark with the extracted filter/query `_path=="http" | cut ts, id.orig_h, id.resp_h, method, host, uri,` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `_path=="http" | cut ts, id.orig_h, id.resp_h, method, host, uri,`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark with the extracted filter/query `_path=="http" | cut ts, id.orig_h, id.resp_h, method, host, uri,` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `booking.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
