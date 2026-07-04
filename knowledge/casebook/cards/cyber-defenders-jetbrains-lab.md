# JetBrains Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_jetbrains_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: wireshark
- Techniques: dns-analysis, http-analysis, network-forensics, timeline-analysis

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: is the attacker's IP address?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `webshell activity.`

### Step 2: When approaching network forensics, I like to begin by baselining the traffic, which involves

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark with the extracted filter/query `_path=="http" method=="POST" | cut ts, id.orig_h, id.resp_h, host,` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `_path=="http" method=="POST" | cut ts, id.orig_h, id.resp_h, host,`
  - `_path=="http" id.orig_h==23.158.56.196 | cut ts, id.resp_h, host,`
  - `uri, user_agent | count() by uri | sort -r count`
  - `TLDR: Look for a GET request made by the threat actor to a URI that likely contains server`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark with the extracted filter/query `_path=="http" method=="POST" | cut ts, id.orig_h, id.resp_h, host,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `23.158.56.196`

### Step 3: identify the version of the web server running, start by using the following display filter in Wireshark:

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark with the extracted filter/query `ip.dst_host == 172.31.25.119 && ip.src_host == 23.158.56.196 &&` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `ip.dst_host == 172.31.25.119 && ip.src_host == 23.158.56.196 &&`
  - `http.request.method == GET`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark with the extracted filter/query `ip.dst_host == 172.31.25.119 && ip.src_host == 23.158.56.196 &&` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2023.11.3`

### Step 4: the vulnerability the attacker exploited?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CVE-2024-27198`

### Step 5: the file that the attacker uploaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark with the extracted filter/query `ip.dst_host==172.31.25.119 && ip.src_host == 23.158.56.196 &&` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `ip.dst_host==172.31.25.119 && ip.src_host == 23.158.56.196 &&`
  - `http.request.method==POST`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark with the extracted filter/query `ip.dst_host==172.31.25.119 && ip.src_host == 23.158.56.196 &&` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `NSt8bHTg.zip`

### Step 6: When did the attacker execute their first command via the web shell?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-06-30 08:03`

### Step 7: the webserver. What new username and password did the attacker write in the file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a1l4m:youarecompromised`

### Step 8: tampering with the text file?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `T1565.001`

### Step 9: command that he used for that?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `docker run --rm -it -v /:/host ubuntu chroot /host`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
