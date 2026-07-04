# HawkEye Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_hawkeye_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, pcap challenges.

## Input Signals

- Artifacts: email, pcap
- Tools: cyberchef, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: How many packets does the capture have?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4003`

### Step 2: At what time was the first packet captured?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use virustotal, wireshark to align timestamps and identify the event that satisfies the question.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use virustotal, wireshark to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2019-04-10 20:37`

### Step 3: What is the duration of the capture?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `01:03:41`

### Step 4: What is the most active computer at the link level?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use virustotal, wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use virustotal, wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `00:08:02:1c:47:ae`

### Step 5: Manufacturer of the NIC of the most active system at the link level?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use virustotal, wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use virustotal, wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Hewlett-Packard`

### Step 6: computer at the link level?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Palo Alto`

### Step 7: the organization are involved in the capture?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3`

### Step 8: What is the name of the most active computer at the network level?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark with the extracted filter/query `(ip.addr==10.4.10.132) && (dhcp)` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `(ip.addr==10.4.10.132) && (dhcp)`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark with the extracted filter/query `(ip.addr==10.4.10.132) && (dhcp)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Beijing-5cd1-PC`

### Step 9: What is the IP of the organization's DNS server?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `_path=="dns"` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `_path=="dns"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `_path=="dns"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.4.10.4`

### Step 10: What domain is the victim asking about in packet 204?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `proforma-invoices.com`

### Step 11: What is the IP of the domain in the previous question?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `ip.addr==217.182.138.150` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `ip.addr==217.182.138.150`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `ip.addr==217.182.138.150` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `217.182.138.150`

### Step 12: What operating system does the victim's computer run?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark with the extracted filter/query `ip.addr==10.4.10.132 && http` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `ip.addr==10.4.10.132 && http`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark with the extracted filter/query `ip.addr==10.4.10.132 && http` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Windows NT 6.1`

### Step 13: What is the name of the malicious file downloaded by the accountant?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `tkraw_Protected99.exe`

### Step 14: What is the md5 hash of the downloaded file?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `71826BA081E303866CE2A2534491A2F7`

### Step 15: What software runs the webserver that hosts the malware?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `LiteSpeed`

### Step 16: What is the public IP of the victim's computer?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `173.66.146.112`

### Step 17: In which country is the email server to which the stolen information is sent?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.addr==10.4.10.132` and inspect the matching evidence.
- Tools: cyberchef, virustotal, wireshark
- Filters or commands:
  - `ip.addr==10.4.10.132`
  - `(ip.addr==10.4.10.132 ) && (smtp)`
  - `sales.del@macwinlogistics.in to sales.del@macwinlogistics.in that contains a Base64 encoded`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use cyberchef, virustotal, wireshark with the extracted filter/query `ip.addr==10.4.10.132` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `United States`

### Step 18: the stolen data is sent?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Exim 4.91`

### Step 19: To which email account is the stolen information sent?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sales.del@macwinlogistics.in`

### Step 20: What is the password used by the malware to send the email?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Sales@23`

### Step 21: Which malware variant exfiltrated the data?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Reborn V9`

### Step 22: What are the bankofamerica access credentials? (username:password)

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `roman.mcguire:P@ssw0rd$`

### Step 23: Every how many minutes does the collected data get exfiltrated?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark with the extracted filter/query `(ip.addr==10.4.10.132 ) && ( smtp.req.command == EHLO)` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `(ip.addr==10.4.10.132 ) && ( smtp.req.command == EHLO)`
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark with the extracted filter/query `(ip.addr==10.4.10.132 ) && ( smtp.req.command == EHLO)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
