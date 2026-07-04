# PacketDetective

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_pakcet_defective_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap, windows-events challenges.

## Input Signals

- Artifacts: pcap, windows-events
- Tools: wireshark
- Techniques: http-analysis, network-forensics, service-enumeration, timeline-analysis, windows-event-analysis

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the total number of bytes used by the SMB protocol?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `As you can see, the total is 4406.`

### Step 2: was compromised. Which username was utilised for authentication via SMB?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `accessed can reveal the attacker’s intent.`

### Step 3: What is the name of the file that was opened by the attacker?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `attacker’s behaviour .`

### Step 4: What is the timestamp of the attempt to clear the event log?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use wireshark to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The attacker used “named pipes” for communication, suggesting they may have utilised`

### Step 5: this named pipe?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `This is the hex representation of \PIPE.`

### Step 6: 172.16.66.1 and 172.16.66.36?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `PSEXESVC.exe`

### Step 7: which is a non-malicious program part of the sysinternals suite of tools. It is often used by threat

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `actors or malware to remotely execute programs.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
