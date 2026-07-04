# Anakus

## Case Metadata

- Category: `Malware Analysis`
- Platform: `BTLO`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/btlo_anakus.pdf`

## Why This Case Matters

Use this case as a Malware Analysis reference for pcap, pe-malware challenges.

## Input Signals

- Artifacts: pcap, pe-malware
- Tools: detect-it-easy, strings, virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, malware-dynamic, malware-static, network-forensics, stego-extraction, timeline-analysis

## First-Principles Route

- Classify the artifact and packer/runtime before deep reversing.
- Extract strings, imports, capabilities, configuration, embedded URLs, hashes, and persistence behavior.
- Correlate static indicators with sandbox or process-monitor evidence when available.

## Solve Thinking

### Step 1: an entropy above 7.2 is considered malicious, what is the name of this section in question?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use detect-it-easy, strings, virustotal, wireshark with the extracted filter/query `0.tcp.ngrok.io` and inspect the matching evidence.
- Tools: detect-it-easy, strings, virustotal, wireshark
- Filters or commands:
  - `0.tcp.ngrok.io`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use detect-it-easy, strings, virustotal, wireshark with the extracted filter/query `0.tcp.ngrok.io` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `hataker.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
