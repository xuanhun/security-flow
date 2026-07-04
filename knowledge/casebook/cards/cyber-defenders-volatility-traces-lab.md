# Volatility Traces Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_volatility_traces_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for ids, memory, pe-malware challenges.

## Input Signals

- Artifacts: ids, memory, pe-malware
- Tools: capa, volatility
- Techniques: dns-analysis, http-analysis, malware-static, memory-forensics

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: same parent process, is identified?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `RegSvcs.exe`

### Step 2: the previously altered application's settings?

- Route type: `volatility-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use volatility to collect the smallest evidence slice that answers the goal.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as volatility-driven evidence lookup.
  - Use volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HcdmIYYf.exe, InvoiceCheckList.exe`

### Step 3: aim to disable or modify antivirus settings to evade detection during incident analysis?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `T1562.001`

### Step 4: account is linked to the malicious processes?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Lee`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
