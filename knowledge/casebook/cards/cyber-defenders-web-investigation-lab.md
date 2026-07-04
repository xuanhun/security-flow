# Web Investigation

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_web_investigation_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap, web-service challenges.

## Input Signals

- Artifacts: pcap, web-service
- Tools: gobuster, wireshark
- Techniques: http-analysis, network-forensics, timeline-analysis, web-enumeration

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: Can you provide the attacker’s IP?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.224.250.131`

### Step 2: determine the origin city of the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 3: provide the vulnerable script name?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `search.php`

### Step 4: the complete request URI of the first SQLi attempt by the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `search.php`

### Step 5: the name of the directory discovered by the attacker?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: compromise. What’s the credentials used by the attacker for logging in?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `login.php`

### Step 7: What’s the name of the malicious script uploaded by the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gobuster, wireshark with the extracted filter/query `Alternatively, you can look for HTTP POST requests by using the http.request.method == POST` and inspect the matching evidence.
- Tools: gobuster, wireshark
- Filters or commands:
  - `Alternatively, you can look for HTTP POST requests by using the http.request.method == POST`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use gobuster, wireshark with the extracted filter/query `Alternatively, you can look for HTTP POST requests by using the http.request.method == POST` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `NVri2vhp.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
