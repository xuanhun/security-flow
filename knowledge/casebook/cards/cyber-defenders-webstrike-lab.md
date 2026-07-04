# WebStrike

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_webstrike_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: wireshark
- Techniques: browser-forensics, http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: threat intelligence analysis. What city did the attack originate from?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 2: attacker’s user agent?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0`

### Step 3: malicious web shell uploaded?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `jpg.php`

### Step 4: blocking unauthorised outbound traffic. What port was used by the malicious web shell?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark with the extracted filter/query `If we use the tcp.dstport == 8080 filter and look through the results, we can find a packet that is` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `If we use the tcp.dstport == 8080 filter and look through the results, we can find a packet that is`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark with the extracted filter/query `If we use the tcp.dstport == 8080 filter and look through the results, we can find a packet that is` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `117.11.88.124`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
