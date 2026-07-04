# Boogeyman 2

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/boogeyman2_writeup.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, memory, office-document challenges.

## Input Signals

- Artifacts: email, memory, office-document
- Tools: olevba, strings, volatility
- Techniques: http-analysis, maldoc-analysis, malware-static, memory-forensics, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What email was used to send the phishing email?

- Route type: `olevba-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use olevba, volatility to collect the smallest evidence slice that answers the goal.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as olevba-driven evidence lookup.
  - Use olevba, volatility to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: What is the email of the victim employee?

- Route type: `olevba-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use olevba, volatility to collect the smallest evidence slice that answers the goal.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as olevba-driven evidence lookup.
  - Use olevba, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What is the MD5 hash of the malicious attachment?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `to the installation directory:`

### Step 4: What URL is used to download the stage 2 payload based on the document’s macro?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `aa2a9c53cbb80416d3b47d85538d9971`

### Step 5: What is the name of the process that executed the newly downloaded stage 2 payload?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wscript.exe`

### Step 6: What is the full path of the malicious stage 2 payload?

- Route type: `olevba-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use olevba, volatility to collect the smallest evidence slice that answers the goal.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as olevba-driven evidence lookup.
  - Use olevba, volatility to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 7: What is the PID of the process that executed the stage 2 payload?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wscript.exe`

### Step 8: What is the parent PID of the process that executed the stage 2 payload?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `wscript.exe`

### Step 9: What URL is used to download the malicious binary executed by the stage 2 payload?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `aa2a9c53cbb80416d3b47d85538d9971`

### Step 10: What is the PID of the malicious process used to establish the C2 connection?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `updater.exe`

### Step 11: What is the full path of the malicious process used to establish the C2 connection?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `updater.exe`

### Step 12: What is the IP address and port of the C2 connection initiated by the malicious binary?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use olevba, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `128.199.95.189:8080`

### Step 13: What is the full file path of the malicious email attachment based on the memory dump?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
- Tools: olevba, volatility
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use olevba, volatility to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ZCFI\Resume_WesleyTaylor (002).doc.`

### Step 14: the full command used by the attacker to maintain persistent access?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use olevba, strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: olevba, strings, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use olevba, strings, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `powershell.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
