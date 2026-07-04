# Shiba Insider

## Case Metadata

- Category: `Network Forensics`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_shiba_insider.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for pcap challenges.

## Input Signals

- Artifacts: pcap
- Tools: exiftool, steghide, wireshark
- Techniques: http-analysis, network-forensics, stego-extraction

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What is the response message obtained from the PCAP file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use exiftool, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: exiftool, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use exiftool, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: What is the password of the ZIP file?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use exiftool, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: exiftool, wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use exiftool, wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `D`

### Step 3: What is the name of a widely-used tool that can be used to obtain file information?

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use exiftool, wireshark with the extracted filter/query `Exiftool is the name of a widely-used tool that can be used to obtain file metadata.` and inspect the matching evidence.
- Tools: exiftool, wireshark
- Filters or commands:
  - `Exiftool is the name of a widely-used tool that can be used to obtain file metadata.`
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use exiftool, wireshark with the extracted filter/query `Exiftool is the name of a widely-used tool that can be used to obtain file metadata.` and inspect the matching evidence.
  - The proof is the recovered file metadata field, not the filename alone.
- Evidence rule: The proof is the recovered file metadata field, not the filename alone.

### Step 4: What is the name and value of the interesting information obtained from the image file metadata? The answer is technique:steganography

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use exiftool, wireshark to recover or open the referenced file and inspect its metadata fields.
- Tools: exiftool, wireshark
- Reasoning chain:
  - Recognize the goal as file metadata extraction.
  - Use exiftool, wireshark to recover or open the referenced file and inspect its metadata fields.
  - The proof is the recovered file metadata field, not the filename alone.
- Evidence rule: The proof is the recovered file metadata field, not the filename alone.

### Step 5: information hidden in the file?

- Route type: `exiftool-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use exiftool, steghide, wireshark with the extracted filter/query `Steghide.` and inspect the matching evidence.
- Tools: exiftool, steghide, wireshark
- Filters or commands:
  - `Steghide.`
- Reasoning chain:
  - Recognize the goal as exiftool-driven evidence lookup.
  - Use exiftool, steghide, wireshark with the extracted filter/query `Steghide.` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `“idInsider.txt” containing the following ID: 0726ba878ea47de571777a.`

### Step 6: What is the profile name of the attacker?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use exiftool, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: exiftool, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use exiftool, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
