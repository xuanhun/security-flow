# Tshark Challenge II: Directory

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/tshark_challenge_2_directory.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: cyberchef, tshark, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the name of the malicious/suspicious domain?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, tshark, virustotal with the extracted filter/query `To find name lof the malicious/suspicious domain address, we can extract the dns.query.name` and inspect the matching evidence.
- Tools: cyberchef, tshark, virustotal
- Filters or commands:
  - `To find name lof the malicious/suspicious domain address, we can extract the dns.query.name`
  - `tshark -r directory-curiosity.pcap -T fields -e dns.qry.name | awk NF | sort -r | uniq -c |`
  - `awk NF removes the empty lines`
  - `uniq -c shows unique values and calculates the number of occurrences for each value,`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, tshark, virustotal with the extracted filter/query `To find name lof the malicious/suspicious domain address, we can extract the dns.query.name` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cyberchef to defang the URL:`

### Step 2: What is the total number of HTTP requests sent to the malicious domain?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark, virustotal with the extracted filter/query `As explained in the hint, we can use the http.request.full_uri field to answer this question. All we` and inspect the matching evidence.
- Tools: tshark, virustotal
- Filters or commands:
  - `As explained in the hint, we can use the http.request.full_uri field to answer this question. All we`
  - `tshark -r directory-curiosity.pcap -Y 'http.request.full_uri contains "jx2-bavuong.com"' -T`
  - `fields -e http.request.full_uri | wc -l`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark, virustotal with the extracted filter/query `As explained in the hint, we can use the http.request.full_uri field to answer this question. All we` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fields -e http.request.full_uri | wc -l`

### Step 3: What is the IP address associated with the malicious domain? Enter your answer in a defanged format.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, tshark, virustotal with the extracted filter/query `tshark -r directory-curiosity.pcap -Y 'http.request.full_uri contains "jx2-bavuong.com"' -T` and inspect the matching evidence.
- Tools: cyberchef, tshark, virustotal
- Filters or commands:
  - `tshark -r directory-curiosity.pcap -Y 'http.request.full_uri contains "jx2-bavuong.com"' -T`
  - `fields -e ip.dst | sort | uniq`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, tshark, virustotal with the extracted filter/query `tshark -r directory-curiosity.pcap -Y 'http.request.full_uri contains "jx2-bavuong.com"' -T` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fields -e ip.dst | sort | uniq`

### Step 4: What is the server info of the suspicious domain?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark, virustotal with the extracted filter/query `The server info can be found in the http.server field, so all we need to do is extract this field if it` and inspect the matching evidence.
- Tools: tshark, virustotal
- Filters or commands:
  - `The server info can be found in the http.server field, so all we need to do is extract this field if it`
  - `tshark -r directory-curiosity.pcap -Y 'http contains "jx2-bavuong.com"' -T fields -e`
  - `http.server | awk NF | sort | uniq`
  - `tshark -r directory-curiosity.pcap -z follow,tcp,ascii,0 -q`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark, virustotal with the extracted filter/query `The server info can be found in the http.server field, so all we need to do is extract this field if it` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `screenshot:`

### Step 5: What is the filename of the first file? Enter your answer in a defanged format.

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use tshark, virustotal with the extracted filter/query `tshark -r directory-curiosity.pcap --export-objects http,/home/ubuntu/Desktop -q` and inspect the matching evidence.
- Tools: tshark, virustotal
- Filters or commands:
  - `tshark -r directory-curiosity.pcap --export-objects http,/home/ubuntu/Desktop -q`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use tshark, virustotal with the extracted filter/query `tshark -r directory-curiosity.pcap --export-objects http,/home/ubuntu/Desktop -q` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- tshark -r directory-curiosity.pcap --export-objects http,/home/ubuntu/Desktop -q`

### Step 6: What is the SHA256 value of the malicious file

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: tshark, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 7: Search the SHA256 value of the file on VirusTotal. What is the PEiD packer value?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: tshark, virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `the Basic properties heading:`

### Step 8: What does the LastLine Sandbox flag this as?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: tshark, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `MALWARE TROJAN is the answer.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
