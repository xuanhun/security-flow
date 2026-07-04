# HTTP Basic Auth

## Case Metadata

- Category: `Network Forensics`
- Platform: `LetsDefend`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/lets_defend_http_basic_auth.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: tshark, wireshark
- Techniques: http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: How many HTTP GET requests are in pcap?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use tshark, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: tshark, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use tshark, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 2: What is the server operating system?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `is running on FreeBSD:`

### Step 3: What is the client’s user-agent information?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Lynx/2.8.7rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8n`

### Step 4: What is the username used for Basic Authentication?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The username is webadmin`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
