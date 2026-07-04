# Dunkle Materie

## Case Metadata

- Category: `Malware Analysis`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/dunkle_materie_writeup.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for ids, pcap, registry challenges.

## Input Signals

- Artifacts: ids, pcap, registry
- Tools: strings, virustotal, wireshark
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, malware-dynamic, malware-static, network-forensics, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: host and what ransomware was involved in the attack?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `explorer.exe`

### Step 2: When you open the three-dot menu, select the system process like as follows:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `exploreer.exe`

### Step 3: encryption results to two domains over HTTP POST. What are the two C2 domains?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `146.112.61.108`

### Step 4: What are the IPs of the malicious domains?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `146.112.61.108`

### Step 5: Provide the user-agent used to transfer the encrypted data to the C2 channel?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Aka Firefox/89.0.`

### Step 6: rather than all processes:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The wallpaper file is ley9kpi9r.bmp.`

### Step 7: Find the PID (Process ID) of the process which attempted to change the background

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use virustotal to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ransomware used in the attack.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
