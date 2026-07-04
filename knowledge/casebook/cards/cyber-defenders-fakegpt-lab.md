# FakeGPT

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_fakegpt_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for artifact-driven challenges.

## Input Signals

- Artifacts: not detected
- Tools: cyberchef
- Techniques: dns-analysis, http-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: them more difficult to detect during analysis?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `answer.`

### Step 2: Which website does the extension monitor for data theft, targeting user accounts to steal sensitive information?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 3: What is the first specific condition in the code that triggers the extension to deactivate itself? navigator.plugins.length === 0

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: Which encryption algorithm is applied to secure the data before sending?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: What does the extension access to store or manipulate session-related data and authentication information?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `it.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
