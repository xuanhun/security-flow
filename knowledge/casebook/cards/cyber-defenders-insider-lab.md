# Insider Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_insider_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for disk-image, linux-logs challenges.

## Input Signals

- Artifacts: disk-image, linux-logs
- Tools: binwalk, ftk-imager
- Techniques: browser-forensics, http-analysis, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Which Linux distribution is being used on this machine?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Kali`

### Step 2: What is the MD5 hash of the Apache access.log file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ftk-imager to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use ftk-imager to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d41d8cd98f00b204e9800998ecf8427e`

### Step 3: A super-secret file was created. What is the absolute path to this file?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/root/Desktop/SuperSecretFile.txt`

### Step 4: What program used the file didyouthinkwedmakeiteasy.jpg during its execution?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, ftk-imager with the extracted filter/query `Binwalk is a tool that can identify and extract files and data that is embedded inside other files.` and inspect the matching evidence.
- Tools: binwalk, ftk-imager
- Filters or commands:
  - `Binwalk is a tool that can identify and extract files and data that is embedded inside other files.`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use binwalk, ftk-imager with the extracted filter/query `Binwalk is a tool that can identify and extract files and data that is embedded inside other files.` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `binwalk`

### Step 5: What is the third goal from the checklist Karen created?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Profit`

### Step 6: How many times was Apache run?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager with the extracted filter/query `This machine was used to launch an attack on another. Which file contains the evidence` and inspect the matching evidence.
- Tools: ftk-imager
- Filters or commands:
  - `This machine was used to launch an attack on another. Which file contains the evidence`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager with the extracted filter/query `This machine was used to launch an attack on another. Which file contains the evidence` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0`

### Step 7: the Documents directory. Who was the expert that Karen was taunting?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use ftk-imager to align timestamps and identify the event that satisfies the question.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use ftk-imager to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `young`

### Step 8: user?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Postgres`

### Step 9: Based on the bash history, what is the current working directory?

- Route type: `ftk-imager-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ftk-imager to collect the smallest evidence slice that answers the goal.
- Tools: ftk-imager
- Reasoning chain:
  - Recognize the goal as ftk-imager-driven evidence lookup.
  - Use ftk-imager to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/root/Documents/myfirsthack/`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
