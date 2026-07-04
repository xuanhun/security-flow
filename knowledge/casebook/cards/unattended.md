# Unattended

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/unattended.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, registry challenges.

## Input Signals

- Artifacts: disk-image, registry
- Tools: autopsy, registry-explorer
- Techniques: browser-forensics, dns-analysis, http-analysis, registry-forensics

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What file type was searched for using the search bar in Windows Explorer?

- Route type: `autopsy-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use autopsy, registry-explorer to collect the smallest evidence slice that answers the goal.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as autopsy-driven evidence lookup.
  - Use autopsy, registry-explorer to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: find what the user searched for using the search bar in Windows Explorer by investigating the following registry location:

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use autopsy, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use autopsy, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What top-secret keyword was searched for using the search bar in Windows Explorer?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use autopsy, registry-explorer to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use autopsy, registry-explorer to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `‘continental’:`

### Step 4: What is the name of the downloaded file to the Downloads folder?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7z2201-x64.exe`

### Step 5: When was the file from the previous question downloaded?

- Route type: `registry artifact correlation`
- Why: Registry artifacts are strongest when paired with timestamp and user context.
- Probe: Use autopsy, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as registry artifact correlation.
  - Use autopsy, registry-explorer to inspect registry hives or parsed registry artifacts for persistence and user activity.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `investigate, in this case it is the following:`

### Step 6: A text file was created in the Desktop folder. How many times was this file opened?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use autopsy, registry-explorer to align timestamps and identify the event that satisfies the question.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use autopsy, registry-explorer to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `JLECmd.exe`

### Step 7: When was the text file from the previous question last modified?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `three results:`

### Step 8: What is the string that was copied to the Pastebin URL?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use autopsy, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: autopsy, registry-explorer
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use autopsy, registry-explorer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Make sure to remove ‘- Pastebin.com’.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
