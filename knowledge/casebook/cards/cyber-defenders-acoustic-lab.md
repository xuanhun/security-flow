# Acoustic Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_acoustic_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: strings, wireshark
- Techniques: dns-analysis, http-analysis, malware-static, network-forensics, service-enumeration, stego-extraction

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the transport protocol being used?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use strings, wireshark with the extracted filter/query `_path=="http" | count() by user_agent | sort -r count` and inspect the matching evidence.
- Tools: strings, wireshark
- Filters or commands:
  - `_path=="http" | count() by user_agent | sort -r count`
  - `cat log.txt | grep "User-Agent:" | sort | uniq -c | sort -r`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use strings, wireshark with the extracted filter/query `_path=="http" | count() by user_agent | sort -r count` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `UDP`

### Step 2: What is the User-Agent of the victim system?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Asterisk PBX 1.6.0.10-FONCORE-r40`

### Step 3: Which tool was only used against the following extensions: 100,101,102,103, and 111?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `svcrack.py`

### Step 4: Which extension on the honeypot does NOT require authentication?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `100`

### Step 5: How many extensions were scanned in total?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark with the extracted filter/query `awk '/User-Agent: friendly-scanner/{inblock=1} /To:/{if(inblock){ if` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `awk '/User-Agent: friendly-scanner/{inblock=1} /To:/{if(inblock){ if`
  - `(match($0,/sip:([^@>]+)/,m)) {print m[1]} }} /^$/{inblock=0}' log.txt | sort -u | wc -l`
  - `grep "User-Agent:" log.txt | sort | uniq -c | sort -r`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark with the extracted filter/query `awk '/User-Agent: friendly-scanner/{inblock=1} /To:/{if(inblock){ if` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2652`

### Step 6: number dialed from extension 101?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark with the extracted filter/query `grep -Ei 'From: "Unknown"<sip:101' log.txt -B8 | grep INVITE` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `grep -Ei 'From: "Unknown"<sip:101' log.txt -B8 | grep INVITE`
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark with the extracted filter/query `grep -Ei 'From: "Unknown"<sip:101' log.txt -B8 | grep INVITE` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `00112524021`

### Step 7: What are the default credentials used in the attempted basic authentication? (format is username:password)

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `maint:password`

### Step 8: Which codec does the RTP stream use? (3 words, 2 spaces in between)

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ITU-T G.711 PCMU`

### Step 9: How long is the sampling time (in milliseconds)?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use wireshark to align timestamps and identify the event that satisfies the question.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use wireshark to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0.125`

### Step 10: What was the password for the account with username 555?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1234`

### Step 11: Which RTP packet header field can be used to reorder out of sync RTP packets in the correct sequence?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use wireshark to align timestamps and identify the event that satisfies the question.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use wireshark to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `timestamp`

### Step 12: The trace includes a secret hidden message. Can you hear it?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `mexico`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
