# AgentTesla Lab

## Case Metadata

- Category: `Malware Analysis`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_agenttesla_lab.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for pe-malware challenges.

## Input Signals

- Artifacts: pe-malware
- Tools: capa, cyberchef, detect-it-easy, dnspy, floss, strings
- Techniques: dns-analysis, http-analysis, malware-dynamic, malware-static, reverse-engineering, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: in this executable?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, dnspy to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, dnspy
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, dnspy to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AutoIt`

### Step 2: is a bin file. What is the MD5 hash of this file?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, dnspy to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, dnspy
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, dnspy to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `A657189456D164A28B0EB9F5A2654B26`

### Step 3: and screen logging?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, detect-it-easy, dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, detect-it-easy, dnspy
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, detect-it-easy, dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `asQXUhiK0j`

### Step 4: output of the malware keylogging functionality?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, detect-it-easy, dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, detect-it-easy, dnspy
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, detect-it-easy, dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HTML`

### Step 5: of data using Telegram?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, detect-it-easy, dnspy, floss to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, detect-it-easy, dnspy, floss, strings
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, detect-it-easy, dnspy, floss to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `https://api.telegram.org/bot6900973449:AAF8wx9iUPZvdsBE34vKz_RL7sCyp2owiPA/`

### Step 6: of the file that was dropped by the malware as part of its persistence mechanism?

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, dnspy to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, dnspy
- Reasoning chain:
  - Recognize the goal as reverse engineering.
  - Use cyberchef, detect-it-easy, dnspy to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `DHL8900067.vbs`

### Step 7: address of the victim?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, detect-it-easy, dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, detect-it-easy, dnspy
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, detect-it-easy, dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ipify`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
