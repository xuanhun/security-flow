# ItsyBitsy

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/itsybitsy.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for ids, siem challenges.

## Input Signals

- Artifacts: ids, siem
- Tools: elk, john
- Techniques: browser-forensics, http-analysis, password-cracking, siem-query, timeline-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: How many events were returned for the month of March 2022?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use elk to align timestamps and identify the event that satisfies the question.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use elk to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `connection_logs index:`

### Step 2: What is the IP associated with the suspected user in the logs?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk with the extracted filter/query `the log file only contains 2 unique source IP addresses, after exploring the second IP address` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `the log file only contains 2 unique source IP addresses, after exploring the second IP address`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk with the extracted filter/query `the log file only contains 2 unique source IP addresses, after exploring the second IP address` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.166.65.54`

### Step 3: What is the name of the binary?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `filesharing site?`

### Step 4: What is the full URL of the C2 to which the infected host is connected?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 5: A file was accessed on the filesharing site. What is the name of the file accessed?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk with the extracted filter/query `The file contains a secret code with the format THM{______}.` and inspect the matching evidence.
- Tools: elk
- Filters or commands:
  - `The file contains a secret code with the format THM{______}.`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use elk with the extracted filter/query `The file contains a secret code with the format THM{______}.` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `this room.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
