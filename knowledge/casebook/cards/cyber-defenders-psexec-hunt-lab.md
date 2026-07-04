# PsExec Hunt

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_psexec_hunt_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: wireshark
- Techniques: dns-analysis, http-analysis, network-forensics, service-enumeration

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: address of the machine from which the attacker initially gained accessed to our network?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.0.0.130`

### Step 2: to which the attacker first pivoted?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `10.0.0.130`

### Step 3: username utilised by the attacker for authentication?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `authenticated to the “ssales” user:`

### Step 4: on the target?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.0.0.133`

### Step 5: Which network share did PsExec use for communication? IPC$

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 6: hostname to which the attacker attempted to pivot within our network?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SMB traffic.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
