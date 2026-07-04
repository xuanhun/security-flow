# PowerShell Script

## Case Metadata

- Category: `Malware Analysis`
- Platform: `LetsDefend`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/lets_defend_powershell_script.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: cyberchef, virustotal
- Techniques: cti-enrichment, http-analysis

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: When you launch the VM, we are given a PowerShell script:

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `following string is Base64-encoded.`

### Step 2: What parameter in the powershell script makes it so that the powershell window is hidden when executed?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `executed.`

### Step 3: What parameter in the Powershell script prevents the user from closing the process?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use virustotal to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `preventing the user from closing it.`

### Step 4: What line of code allows the script to interact with websites and retrieve information from them?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `data from the internet.`

### Step 5: What is the user agent string that is being spoofed in the malicious script?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Gecko”.`

### Step 6: download the malicious payload?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `98.103.103.170:7443`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
