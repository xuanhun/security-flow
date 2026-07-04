# Carnage

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/carnage_writeup.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, ids, pcap challenges.

## Input Signals

- Artifacts: email, ids, pcap
- Tools: virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What was the date and time for the first HTTP connection to the malicious IP?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark with the extracted filter/query `tcp.port == 80` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `tcp.port == 80`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark with the extracted filter/query `tcp.port == 80` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- tcp.port == 80`

### Step 2: What caught my attention is the GET requests made to 85.187.128.24, where a zip file was

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What is the name of the zip file that was downloaded?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: What was the domain hosting the malicious zip file?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: Without downloading the file, what is the name of the file in the zip file?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bottom:`

### Step 6: What is the name of the webserver of the malicious IP from which the zip file was downloaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `you can see the name of the webserver:`

### Step 7: What is the version of the webserver from the previous question?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `answer is:`

### Step 8: Malicious files were downloaded to the victim host from multiple domains. What were

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `tls.handshake.type == 1 && frame.time >= "Sep 24, 2021 16:45:11" && frame.time <=` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `tls.handshake.type == 1 && frame.time >= "Sep 24, 2021 16:45:11" && frame.time <=`
  - `tls.handshake.type == 1 simply filters for TLS Client Hello messages, and`
  - `frame.time >= "Sep 24, 2021 16:45:11" && frame.time <= "Sep 24, 2021 16:45:30"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `tls.handshake.type == 1 && frame.time >= "Sep 24, 2021 16:45:11" && frame.time <=` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `"Sep 24, 2021 16:45:30"`

### Step 9: Which certificate authority issued the SSL certificate to the first domain from the previous question?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - The proof is the DNS packet, resolver, queried domain, or response record.
- Evidence rule: The proof is the DNS packet, resolver, queried domain, or response record.

### Step 10: What are the two IP addresses of the Cobalt Strike servers? Use VirusTotal (the

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `http.request.method == GET` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `http.request.method == GET`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `http.request.method == GET` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- http.request.method == GET`

### Step 11: What is the host header for the first Cobalt Strike IP address from the previous question?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- ocsp.verisign.com`

### Step 12: What is the domain name for the first IP address of the Cobalt Strike Server? You may

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 13: What is the domain name of the second Cobalt Strike server IP? You may use VirusTotal

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `185.125.204.174`

### Step 14: What is the domain name of the post-infection traffic?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `http.request.method == POST` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `http.request.method == POST`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `http.request.method == POST` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `maldivehost.net:`

### Step 15: What are the first eleven characters that the victim host sends out to the malicious

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 16: domain involved in the post-infection traffic?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 17: What was the length for the first packet sent out to the C2 server?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `questions ago:`

### Step 18: What was the sever header for the malicious domain from the previous question?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 19: The malware used an API to check for the IP address of the victim’s machine. What was

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 20: the date and time when the DNS query for the IP check domain occurred?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `You could use a display filter like frame.contains “api” , however, I simply queried for all DNS` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `You could use a display filter like frame.contains “api” , however, I simply queried for all DNS`
  - `udp.port == 53`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `You could use a display filter like frame.contains “api” , however, I simply queried for all DNS` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- udp.port == 53`

### Step 21: What was the domain in the DNS query from the previous question?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `in the image above.`

### Step 22: first MAIL FROM address observed in the traffic?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 23: which filters for SMTP traffic that contains the text “MAIL FROM”:

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark with the extracted filter/query `smtp && frame contains "MAIL FROM"` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `smtp && frame contains "MAIL FROM"`
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark with the extracted filter/query `smtp && frame contains "MAIL FROM"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `first packet to see the from address:`

### Step 24: How many packets were observed for the SMTP traffic?

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 25: Conclusion

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `This writeup analysed a pcap file which contains traffic of a malicious campaign involving` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `This writeup analysed a pcap file which contains traffic of a malicious campaign involving`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `This writeup analysed a pcap file which contains traffic of a malicious campaign involving` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
