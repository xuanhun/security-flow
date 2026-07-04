# WinRar 0-Day

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `LetsDefend`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/win_rar_0_day.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for memory challenges.

## Input Signals

- Artifacts: memory
- Tools: cyberchef, malwarebazaar, volatility
- Techniques: dns-analysis, http-analysis, memory-forensics

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What is the suspected process?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use cyberchef, volatility to enumerate processes, network sockets, injected regions, and command lines.
- Tools: cyberchef, volatility
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use cyberchef, volatility to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `WinRAR.exe`

### Step 2: We suspect that the crack had another name. Can you find the old name of that crack?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, volatility
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What is the new crack filename?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, volatility
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `The answer is FIFA23CRACK.rar.`

### Step 4: What is the command that executed the remote request?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, volatility
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: The external link has a username. What is it?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, volatility
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The username is “Elsfa7El4a2y”.`

### Step 6: domain it was downloaded from?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, malwarebazaar, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: cyberchef, malwarebazaar, volatility
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, malwarebazaar, volatility to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0352598565fbafe39866f3c9b5964b613fd259ea12a8fe46410b`

### Step 7: the full location of this file?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, volatility
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `B4cKL4T3R.bat`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
