# XWorm Lab

## Case Metadata

- Category: `Malware Analysis`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_xworm_lab.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for email, ids, pe-malware challenges.

## Input Signals

- Artifacts: email, ids, pe-malware, registry
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Techniques: cti-enrichment, dns-analysis, malware-dynamic, malware-static, reverse-engineering

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: What is the compile timestamp (UTC) of the sample?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2024-02-25 22:53`

### Step 2: Which legitimate company does the malware impersonate in an attempt to appear trustworthy?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Adobe`

### Step 3: How many anti-analysis checks does the malware perform to detect/evade sandboxes and debugging environments?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use detect-it-easy, dnspy, pestudio, virustotal to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5`

### Step 4: What is the name of the scheduled task created by the malware to achieve execution with elevated privileges?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use detect-it-easy, dnspy, pestudio, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `schtasks.exe`

### Step 5: submit this sample to ANY .RUN, or view an already generated report, we can see that it created

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `WmiPrvSE`

### Step 6: What is the filename of the malware binary that is dropped in the AppData directory?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `WmiPrvSE.exe`

### Step 7: Which cryptographic algorithm does the malware use to encrypt or obfuscate its configuration data?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use detect-it-easy, dnspy, pestudio, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AES`

### Step 8: What are the Command and Control (C2) IP addresses obtained after the malware decrypts them?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `185.117.250.169, 66.175.239.149,185.117.249.43`

### Step 9: Control (C2) server?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7000`

### Step 10: name of the new copy created on each infected device?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `USB.exe`

### Step 11: extension of these created files?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `lnk`

### Step 12: What is the name of the DLL the malware uses to detect if it is running in a sandbox environment?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `SbieDll.dll`

### Step 13: hidden items in Windows Explorer?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ShowSuperHidden`

### Step 14: termination or interference?

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use detect-it-easy, dnspy, pestudio, virustotal to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `RtlSetProcessIsCritical`

### Step 15: to monitor or capture user input?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `SetWindowsHookEx`

### Step 16: primary functionality or objective?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, dnspy, pestudio, virustotal
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use detect-it-easy, dnspy, pestudio, virustotal to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `keylogger`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
