# Snort Challenge the Basics

## Case Metadata

- Category: `IDS/IPS`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/snort_challenge_the_basics.pdf`

## Why This Case Matters

Use this case as a IDS/IPS reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: cyberchef, snort, strings
- Techniques: http-analysis, malware-static, network-forensics, service-enumeration, stego-extraction

## First-Principles Route

- Start from alerts/signatures, then validate them against packet context and endpoint/network indicators.
- Tune signatures only after confirming the malicious flow and payload boundaries.

## Solve Thinking

### Step 1: What is the number of detected packets?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use snort to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use snort to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `164 TCP packets as seen below:`

### Step 2: What is the destination address of packet 63?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `in my case:`

### Step 3: What is the ACK number of packet 64?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: What is the SEQ number of packet 62?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: port of packet 65?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use snort with the extracted filter/query `FTP runs on TCP port 21, unfortunately we can’t replace tcp with ftp for example as you can only` and inspect the matching evidence.
- Tools: snort
- Filters or commands:
  - `FTP runs on TCP port 21, unfortunately we can’t replace tcp with ftp for example as you can only`
  - `snort -c local.rules -A full -l . -r ftp-png-gif.pcap`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use snort with the extracted filter/query `FTP runs on TCP port 21, unfortunately we can’t replace tcp with ftp for example as you can only` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `the given pcap file:`

### Step 6: What is the number of detected packets?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 7: What is the FTP service name?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use snort, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: snort, strings
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use snort, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `this requirement:`

### Step 8: yet. What is the number of detected packets?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use snort to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use snort to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Let’s modify the local rule file:`

### Step 9: password entered yet. What is the number of detected packets?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use snort, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: snort, strings
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use snort, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `detected packets?`

### Step 10: What is the name of the torrent application?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort, strings to collect the smallest evidence slice that answers the goal.
- Tools: snort, strings
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `“bittorent” is the answer.`

### Step 11: What is the MIME type of the torrent metafile?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort, strings to collect the smallest evidence slice that answers the goal.
- Tools: snort, strings
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort, strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 12: What is the hostname of the torrent metafile?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use snort, strings with the extracted filter/query `sudo snort -c local-X.rules -r mx-1.pcap -A console` and inspect the matching evidence.
- Tools: snort, strings
- Filters or commands:
  - `sudo snort -c local-X.rules -r mx-1.pcap -A console`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use snort, strings with the extracted filter/query `sudo snort -c local-X.rules -r mx-1.pcap -A console` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `detected packets?`

### Step 13: keyboard. What is the number of detected packets?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The number of detected packets is 12:`

### Step 14: What is the requested path?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort, strings to collect the smallest evidence slice that answers the goal.
- Tools: snort, strings
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `It is the second line.`

### Step 15: What is the CVSS v2 score of the MS17-010 vulnerability?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `packets?`

### Step 16: How many rules were triggered?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort with the extracted filter/query `grep -F [**} filters the lines to include only those containing [**].` and inspect the matching evidence.
- Tools: snort
- Filters or commands:
  - `grep -F [**} filters the lines to include only those containing [**].`
  - `uniq removes duplicates, and`
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort with the extracted filter/query `grep -F [**} filters the lines to include only those containing [**].` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- wc -l counts the number of lines.`

### Step 17: What are the first six digits of the triggered rule sids?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `The answer is 210037.`

### Step 18: and 855 bytes. What is the number of detected packets?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 19: What is the name of the used encoding algorithm?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort, strings to collect the smallest evidence slice that answers the goal.
- Tools: snort, strings
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort, strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 20: What is the IP ID of the corresponding packet?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 21: What is the attacker’s command?

- Route type: `cyberchef-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, snort, strings with the extracted filter/query `Enter the base64 encoded payload into cyberchef or by entering echo “base64 encoded text” |` and inspect the matching evidence.
- Tools: cyberchef, snort, strings
- Filters or commands:
  - `Enter the base64 encoded payload into cyberchef or by entering echo “base64 encoded text” |`
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, snort, strings with the extracted filter/query `Enter the base64 encoded payload into cyberchef or by entering echo “base64 encoded text” |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `base64 -d:`

### Step 22: What is the CVSS v2 score of the Log4j vulnerability?

- Route type: `snort-driven evidence lookup`
- Why: For IDS/IPS, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use snort to collect the smallest evidence slice that answers the goal.
- Tools: snort
- Reasoning chain:
  - Recognize the goal as snort-driven evidence lookup.
  - Use snort to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
