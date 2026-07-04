# T1598.002 Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_t1598_002_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, office-document challenges.

## Input Signals

- Artifacts: email, office-document
- Tools: oledump, virustotal
- Techniques: cti-enrichment, dns-analysis, email-header-analysis, http-analysis, maldoc-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What plugin is included in the oledump directory that scans streams in MSG files?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use oledump to extract macros, streams, embedded URLs, and decoded script content.
- Tools: oledump
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use oledump to extract macros, streams, embedded URLs, and decoded script content.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `plugin_msg`

### Step 2: What are the 8-digit hexadecimal codes related to the "Attach long filename" stream?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg` and inspect the matching evidence.
- Tools: oledump
- Filters or commands:
  - `python .\oledump.py -p plugin_msg`
  - `C:\Users\Administrator\Desktop\Challenge\T1598.msg | Select-String`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0x3707 001F`

### Step 3: During the analysis of the streams. What is the message class?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg` and inspect the matching evidence.
- Tools: oledump
- Filters or commands:
  - `python .\oledump.py -p plugin_msg`
  - `C:\Users\Administrator\Desktop\Challenge\T1598.msg | Select-String`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `IPM.Note`

### Step 4: sender's IP address?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg_summary --pluginoptions -H` and inspect the matching evidence.
- Tools: oledump
- Filters or commands:
  - `python .\oledump.py -p plugin_msg_summary --pluginoptions -H`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg_summary --pluginoptions -H` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `210.134.168.89`

### Step 5: What was the total delay (in seconds) between the sender and the email receiver?

- Route type: `oledump-driven evidence lookup`
- Why: For Endpoint Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use oledump to collect the smallest evidence slice that answers the goal.
- Tools: oledump
- Reasoning chain:
  - Recognize the goal as oledump-driven evidence lookup.
  - Use oledump to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3`

### Step 6: What is the company that developed the antispam software used by the target?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg_summary --pluginoptions -H` and inspect the matching evidence.
- Tools: oledump
- Filters or commands:
  - `python .\oledump.py -p plugin_msg_summary --pluginoptions -H`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg_summary --pluginoptions -H` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ESET`

### Step 7: file's MD5 hash?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use oledump, virustotal with the extracted filter/query `python .\oledump.py -p plugin_msg_summary -s 4 -d` and inspect the matching evidence.
- Tools: oledump, virustotal
- Filters or commands:
  - `python .\oledump.py -p plugin_msg_summary -s 4 -d`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use oledump, virustotal with the extracted filter/query `python .\oledump.py -p plugin_msg_summary -s 4 -d` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7E42F69B2ADCE7166408F635A093266E`

### Step 8: What full URL is used by the malicious shortcut embedded in the zip file?

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg_summary --pluginoptions -b` and inspect the matching evidence.
- Tools: oledump
- Filters or commands:
  - `python .\oledump.py -p plugin_msg_summary --pluginoptions -b`
- Reasoning chain:
  - Recognize the goal as maldoc analysis.
  - Use oledump with the extracted filter/query `python .\oledump.py -p plugin_msg_summary --pluginoptions -b` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://23.29.125.210/herALook.dat`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
