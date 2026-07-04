# Memory Analysis - Ransomware

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `BTLO`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_memory_analysis_ransomware.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: virustotal, volatility
- Techniques: cti-enrichment, memory-forensics

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: investigation to uncover how the ransomware works and how to stop it!

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - The proof is the memory plugin output tied to process/socket/module evidence.
- Evidence rule: The proof is the memory plugin output tied to process/socket/module evidence.

### Step 2: What is the name of the suspicious process?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `malicious process (WannaCry ransomware):`

### Step 3: What is the parent process ID for the suspicious process?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: What is the initial malicious executable that created this process?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use volatility with the extracted filter/query `psscan | grep (PIDhere)), find the process used to delete files` and inspect the matching evidence.
- Tools: volatility
- Filters or commands:
  - `psscan | grep (PIDhere)), find the process used to delete files`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use volatility with the extracted filter/query `psscan | grep (PIDhere)), find the process used to delete files` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `or4qtckT.exe`

### Step 5: Find the path where the malicious file was first executed?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `or4qtckT.exe`

### Step 6: what displays a GUI demanding a ransom. Alternatively, you can dump the executable of the

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal, volatility
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 7: What is the filename for the file with the ransomware public key that was used to encrypt the private key? (.eky extension)

- Route type: `volatility-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use volatility to collect the smallest evidence slice that answers the goal.
- Tools: volatility
- Reasoning chain:
  - Recognize the goal as volatility-driven evidence lookup.
  - Use volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is 00000000.eky (ignore hed).`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
