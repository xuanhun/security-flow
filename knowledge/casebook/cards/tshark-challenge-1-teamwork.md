# TShark Challenge 1: Teamwork

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/tshark_challenge_1_teamwork.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, pcap challenges.

## Input Signals

- Artifacts: email, pcap
- Tools: cyberchef, john, tshark, virustotal
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics, password-cracking

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the full URL of the malicious/suspicious domain address. Enter your answer in defanged format.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, tshark, virustotal with the extracted filter/query `To find the full URL of the malicious/suspicious domain address, we can extract the http.host` and inspect the matching evidence.
- Tools: cyberchef, tshark, virustotal
- Filters or commands:
  - `To find the full URL of the malicious/suspicious domain address, we can extract the http.host`
  - `tshark -r teamwork.pcap -T fields -e http.host -e ip.dst | awk NF | sort -r | uniq -c | sort -r`
  - `awk NF removes the empty lines`
  - `uniq -c shows unique values and calculates the number of occurrences for each value,`
  - `Note, you could also find the answer by extracting the dns.qry.name field to see domain names`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, tshark, virustotal with the extracted filter/query `To find the full URL of the malicious/suspicious domain address, we can extract the http.host` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `that have been resolved.`

### Step 2: Which known service was the domain trying to impersonate?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: tshark, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What is the IP address of the malicious domain?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use tshark, virustotal with the extracted filter/query `tshark -r teamwork.pcap -Y 'http.host ==` and inspect the matching evidence.
- Tools: tshark, virustotal
- Filters or commands:
  - `tshark -r teamwork.pcap -Y 'http.host ==`
  - `http.host -e ip.dst | awk NF | sort -r | uniq -c | sort -r`
  - `http.host -e ip.dst -E header=y | awk NF | uniq -c`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use tshark, virustotal with the extracted filter/query `tshark -r teamwork.pcap -Y 'http.host ==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `"www.paypal.com4uswebappsresetaccountrecovery.timeseaways.com"' -T fields -e`

### Step 4: What is the email address that was used?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, john, tshark, virustotal with the extracted filter/query `tshark -r teamwork.pcap -Y "http.request.method == POST" -T fields -e http.host -e` and inspect the matching evidence.
- Tools: cyberchef, john, tshark, virustotal
- Filters or commands:
  - `tshark -r teamwork.pcap -Y "http.request.method == POST" -T fields -e http.host -e`
  - `http.request.uri -e urlencoded-form.key -e urlencoded-form.value`
  - `various fields within the pcap file. By identifying the http.host and ip.dst fields, we pinpointed`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, john, tshark, virustotal with the extracted filter/query `tshark -r teamwork.pcap -Y "http.request.method == POST" -T fields -e http.host -e` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `handling of the data.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
