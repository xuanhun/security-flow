# TeleStealer Lab

## Case Metadata

- Category: `Malware Analysis`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_telestealer_lab.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for pcap, pe-malware, registry challenges.

## Input Signals

- Artifacts: pcap, pe-malware, registry
- Tools: detect-it-easy, wireshark
- Techniques: dns-analysis, http-analysis, malware-dynamic, malware-static, network-forensics

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: analysis with ProcMon, the sample was observed dropping a second-stage PowerShell script to

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use detect-it-easy, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: detect-it-easy, wireshark
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use detect-it-easy, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - The proof is the parsed registry key/value and its timestamp or user context.
- Evidence rule: The proof is the parsed registry key/value and its timestamp or user context.

### Step 2: analysis of the second-stage payload revealed a data staging script that recursively harvested

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use detect-it-easy, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: detect-it-easy, wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use detect-it-easy, wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `intermediate-advanced level dynamic analysis.`

### Step 3: When you load an executable into DiE, it provides extensive information about the file:

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, wireshark
- Reasoning chain:
  - Recognize the goal as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `UPX`

### Step 4: malware place the second stage?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use detect-it-easy, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: detect-it-easy, wireshark
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use detect-it-easy, wireshark to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `C:\Users\Administrator\AppData\Roaming\Dropper`

### Step 5: uses to do this?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use detect-it-easy, wireshark with the extracted filter/query `Get-ChildItem -Path C:\Users\Administrator\Desktop -Recurse -File |` and inspect the matching evidence.
- Tools: detect-it-easy, wireshark
- Filters or commands:
  - `Get-ChildItem -Path C:\Users\Administrator\Desktop -Recurse -File |`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use detect-it-easy, wireshark with the extracted filter/query `Get-ChildItem -Path C:\Users\Administrator\Desktop -Recurse -File |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

### Step 6: domain that the malware uses to exfiltrate the data?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use detect-it-easy, wireshark with the extracted filter/query `python -m http.server 80` and inspect the matching evidence.
- Tools: detect-it-easy, wireshark
- Filters or commands:
  - `python -m http.server 80`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use detect-it-easy, wireshark with the extracted filter/query `python -m http.server 80` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `api.telegram.org`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
