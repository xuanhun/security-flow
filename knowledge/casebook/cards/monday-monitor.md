# Monday Monitor

## Case Metadata

- Category: `SIEM (ELK, Splunk, etc.)`
- Platform: `TryHackMe`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/monday_monitor.pdf`

## Why This Case Matters

Use this case as a SIEM (ELK, Splunk, etc.) reference for office-document, registry, siem challenges.

## Input Signals

- Artifacts: office-document, registry, siem, windows-events
- Tools: cyberchef, john, wazuh
- Techniques: dns-analysis, http-analysis, password-cracking, service-enumeration, windows-event-analysis

## First-Principles Route

- Translate the question into searchable fields such as host, user, process, index, sourcetype, URI, IP, hash, or event code.
- Run broad time-bounded searches first, then narrow by event type, field value, and correlation chain.
- Keep the exact query shape and the evidence field that proves each answer.

## Solve Thinking

### Step 1: what? You’re the cyber sleuth they’ve called in to crack the code!

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, wazuh to enumerate processes, network sockets, injected regions, and command lines.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, wazuh to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Swiftspend’s defences.`

### Step 2: Initial access was established using a downloaded file. What is the file name saved on the

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, wazuh to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, wazuh to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `answer that way).`

### Step 3: What is the full command run to create a scheduled task?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, wazuh to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, wazuh to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- Executes the decoded command.`

### Step 4: What time is the scheduled task meant to run?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use cyberchef, wazuh to align timestamps and identify the event that satisfies the question.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use cyberchef, wazuh to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: What was encoded?

- Route type: `cyberchef-driven evidence lookup`
- Why: For SIEM (ELK, Splunk, etc.), keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, wazuh to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, wazuh to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: What password was set for the new user account?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use cyberchef, wazuh to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use cyberchef, wazuh to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `I_AM_M0NIT0R1NG:`

### Step 7: What is the name of the .exe that was used to dump credentials?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, wazuh to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, wazuh to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `memotech.exe`

### Step 8: Data was exfiltrated from the host. What was the flag that was part of the data?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, wazuh to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, wazuh
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, wazuh to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `you can too.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
