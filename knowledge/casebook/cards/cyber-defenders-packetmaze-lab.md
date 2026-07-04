# PacketMaze Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_packetmaze_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: exiftool, wireshark
- Techniques: dns-analysis, http-analysis, network-forensics, service-enumeration, stego-extraction

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the FTP password?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AfricaCTF2021`

### Step 2: What is the IPv6 address of the DNS server used by 192.168.1.26?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use wireshark with the extracted filter/query `ip.src == 192.168.1.26 and dns` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `ip.src == 192.168.1.26 and dns`
  - `eth.addr==c8:09:a8:57:47:93`
  - `ipv6.addr==fe80::b011:ed39:8665:3b0a &&`
  - `ipv6.addr==fe80::c80b:adff:feaa:1db7`
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use wireshark with the extracted filter/query `ip.src == 192.168.1.26 and dns` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fe80::c80b:adff:feaa:1db7`

### Step 3: What domain is the user looking up in packet 15174?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark with the extracted filter/query `frame.number == 15174` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `frame.number == 15174`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark with the extracted filter/query `frame.number == 15174` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `www.7-zip.org`

### Step 4: How many UDP packets were sent from 192.168.1.26 to 24.39.217.246?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10`

### Step 5: What is the MAC address of the system under investigation in the PCAP file?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c8:09:a8:57:47:93`

### Step 6: What was the camera model name used to take picture 20210429_152157.jpg?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use exiftool, wireshark with the extracted filter/query `exiftool 20210429_152157.jpg | grep -i model` and inspect the matching evidence.
- Tools: exiftool, wireshark
- Filters or commands:
  - `exiftool 20210429_152157.jpg | grep -i model`
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use exiftool, wireshark with the extracted filter/query `exiftool 20210429_152157.jpg | grep -i model` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `LM-Q725K`

### Step 7: What is the ephemeral public key provided by the server during the TLS handshake in the session with the session ID:

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use wireshark with the extracted filter/query `tls.handshake.session_id ==` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `tls.handshake.session_id ==`
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use wireshark with the extracted filter/query `tls.handshake.session_id ==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `04edcc123af7b13e90ce101a31c2f996f471a7c8f48a1b81d765085f548059a550f3f4f62ca1f0e8f`

### Step 8: What is the first TLS 1.3 client random that was used to establish a connection with protonmail.com?

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use wireshark with the extracted filter/query `frame contains "protonmail.com"` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `frame contains "protonmail.com"`
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use wireshark with the extracted filter/query `frame contains "protonmail.com"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `24e92513b97a0348f733d16996929a79be21b0b1400cd7e2862a732ce7775b70`

### Step 9: Which country is the manufacturer of the FTP server’s MAC address registered in?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `United States`

### Step 10: What time was a non-standard folder created on the FTP server on the 20th of April?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `17:53`

### Step 11: What URL was visited by the user and connected to the IP address 104.21.89.171?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark with the extracted filter/query `http and ip.addr == 104.21.89.171` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `http and ip.addr == 104.21.89.171`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark with the extracted filter/query `http and ip.addr == 104.21.89.171` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://dfir.science/`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
