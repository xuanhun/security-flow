# TShark

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/tshark.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap, pe-malware challenges.

## Input Signals

- Artifacts: pcap, pe-malware
- Tools: capa, cyberchef, tshark, wireshark
- Techniques: dns-analysis, malware-static, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: Introduction to TShark

- Route type: `tshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use tshark, wireshark with the extracted filter/query `TShark is a network protocol analyser, and is quite literally a CLI version of Wireshark. It enables` and inspect the matching evidence.
- Tools: tshark, wireshark
- Filters or commands:
  - `TShark is a network protocol analyser, and is quite literally a CLI version of Wireshark. It enables`
- Reasoning chain:
  - Recognize the goal as tshark-driven evidence lookup.
  - Use tshark, wireshark with the extracted filter/query `TShark is a network protocol analyser, and is quite literally a CLI version of Wireshark. It enables` and inspect the matching evidence.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: Verifying TShark Installation

- Route type: `tshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use tshark, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: tshark, wireshark
- Reasoning chain:
  - Recognize the goal as tshark-driven evidence lookup.
  - Use tshark, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `command:`

### Step 3: Reading a Capture File

- Route type: `tshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use tshark to collect the smallest evidence slice that answers the goal.
- Tools: tshark
- Reasoning chain:
  - Recognize the goal as tshark-driven evidence lookup.
  - Use tshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: Utilising Display Filters

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: tshark, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `enter:`

### Step 5: Extracting Specific Fields

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark with the extracted filter/query `As you can see, the command above only prints out the dns.qry.name field which is simply the` and inspect the matching evidence.
- Tools: tshark
- Filters or commands:
  - `As you can see, the command above only prints out the dns.qry.name field which is simply the`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark with the extracted filter/query `As you can see, the command above only prints out the dns.qry.name field which is simply the` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: How many packets are in the dns.cap file?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: tshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is 38.`

### Step 7: How many A records are in the capture? (including responses)

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark with the extracted filter/query `To find all the A records, all we need to do is enter the display filter ‘dns.qry.type == 1’ after the -Y` and inspect the matching evidence.
- Tools: tshark
- Filters or commands:
  - `To find all the A records, all we need to do is enter the display filter ‘dns.qry.type == 1’ after the -Y`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark with the extracted filter/query `To find all the A records, all we need to do is enter the display filter ‘dns.qry.type == 1’ after the -Y` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is 6.`

### Step 8: Which A record was present the most?

- Route type: `tshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use tshark to collect the smallest evidence slice that answers the goal.
- Tools: tshark
- Reasoning chain:
  - Recognize the goal as tshark-driven evidence lookup.
  - Use tshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 9: can you find it?

- Route type: `tshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use tshark, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: tshark, wireshark
- Reasoning chain:
  - Recognize the goal as tshark-driven evidence lookup.
  - Use tshark, wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 10: identify suspicious items in Wireshark, pivot to TShark to extract relevant information.

- Route type: `tshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use tshark, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: tshark, wireshark
- Reasoning chain:
  - Recognize the goal as tshark-driven evidence lookup.
  - Use tshark, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Wireshark).`

### Step 11: How many packets are in this capture?

- Route type: `tshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use tshark to collect the smallest evidence slice that answers the goal.
- Tools: tshark
- Reasoning chain:
  - Recognize the goal as tshark-driven evidence lookup.
  - Use tshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is 125.`

### Step 12: How many DNS queries are in this pcap? (Not responses!)

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: tshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is 56.`

### Step 13: What is the DNS transaction ID of the suspicious queries (in hex)?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: tshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `field values:`

### Step 14: What is the string extracted from the DNS queries?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark with the extracted filter/query `cut -c 1 simply cuts and prints the first character, it is then piped to tr -d which removes the` and inspect the matching evidence.
- Tools: tshark
- Filters or commands:
  - `cut -c 1 simply cuts and prints the first character, it is then piped to tr -d which removes the`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark with the extracted filter/query `cut -c 1 simply cuts and prints the first character, it is then piped to tr -d which removes the` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `the answer.`

### Step 15: What is the flag?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, tshark to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, tshark
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, tshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
