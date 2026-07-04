# Suspicious USB Stick

## Case Metadata

- Category: `Malware Analysis`
- Platform: `BTLO`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_suspicious_usb_stick.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for email challenges.

## Input Signals

- Artifacts: email
- Tools: strings, virustotal
- Techniques: cti-enrichment, http-analysis, malware-static, stego-extraction

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: What file is the autorun.inf running?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `It opens up README.pdf.`

### Step 2: Does the pdf file pass virustotal scan?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Therefore, the answer is false.`

### Step 3: Does the file have the correct magic number?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `signature:`

### Step 4: What OS type can the file exploit? (Linux, MacOS, Windows, etc)

- Route type: `strings-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings, virustotal to collect the smallest evidence slice that answers the goal.
- Tools: strings, virustotal
- Reasoning chain:
  - Recognize the goal as strings-driven evidence lookup.
  - Use strings, virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `exploit Windows machine, including:`

### Step 5: A Windows executable is mentioned in the pdf file, what is it?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cmd.exe`

### Step 6: How many suspicious /OpenAction elements does the file have?

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 7: determine the number of suspicious OpenAction elements by entering:

- Route type: `virustotal-driven evidence lookup`
- Why: For Malware Analysis, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal to collect the smallest evidence slice that answers the goal.
- Tools: virustotal
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `The answer is therefore 1.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
