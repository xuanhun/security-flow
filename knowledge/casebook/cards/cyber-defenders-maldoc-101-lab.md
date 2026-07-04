# Maldoc101

## Case Metadata

- Category: `Malware Analysis`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_maldoc_101_lab.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for email, office-document challenges.

## Input Signals

- Artifacts: email, office-document
- Tools: cyberchef, oledump, olevba, virustotal
- Techniques: cti-enrichment, dns-analysis, maldoc-analysis

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: What event is used to begin the execution of the macros?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use cyberchef, oledump, olevba, virustotal to extract macros, streams, embedded URLs, and decoded script content.
- Tools: cyberchef, oledump, olevba, virustotal
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use cyberchef, oledump, olevba, virustotal to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `the 13th object a little closer:`

### Step 2: What malware family was this maldoc attempting to drop?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use cyberchef, oledump, olevba, virustotal to extract macros, streams, embedded URLs, and decoded script content.
- Tools: cyberchef, oledump, olevba, virustotal
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use cyberchef, oledump, olevba, virustotal to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `associations tab:`

### Step 3: What stream is responsible for the storage of the base64-encoded string?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use cyberchef, oledump, olevba, virustotal with the extracted filter/query `This stream contains the base64-encoded string.` and inspect the matching evidence.
- Tools: cyberchef, oledump, olevba, virustotal
- Filters or commands:
  - `This stream contains the base64-encoded string.`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use cyberchef, oledump, olevba, virustotal with the extracted filter/query `This stream contains the base64-encoded string.` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `random text in the OLE stream ‘Macros/roubhaol/i09/0’:`

### Step 4: This document contains a user-form. Provide the name?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use cyberchef, oledump, olevba, virustotal with the extracted filter/query `This document contains an obfuscated base64 encoded string: what value is used to pad` and inspect the matching evidence.
- Tools: cyberchef, oledump, olevba, virustotal
- Filters or commands:
  - `This document contains an obfuscated base64 encoded string: what value is used to pad`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use cyberchef, oledump, olevba, virustotal with the extracted filter/query `This document contains an obfuscated base64 encoded string: what value is used to pad` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Therefore, the answer is roubhaol.`

### Step 5: (or obfuscate) this string?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use cyberchef, oledump, olevba, virustotal with the extracted filter/query `If we dump stream 15 which contains the malicious macro, we can see a string of characters` and inspect the matching evidence.
- Tools: cyberchef, oledump, olevba, virustotal
- Filters or commands:
  - `If we dump stream 15 which contains the malicious macro, we can see a string of characters`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use cyberchef, oledump, olevba, virustotal with the extracted filter/query `If we dump stream 15 which contains the malicious macro, we can see a string of characters` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `that is repeated several times:`

### Step 6: What is the program executed by the base64 encoded string?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, oledump, olevba, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, oledump, olevba, virustotal
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, oledump, olevba, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `program executed by the base64 encoded string.`

### Step 7: What WMI class is used to create the process to launch the trojan?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, oledump, olevba, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, oledump, olevba, virustotal
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, oledump, olevba, virustotal to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `is a perfect room.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
