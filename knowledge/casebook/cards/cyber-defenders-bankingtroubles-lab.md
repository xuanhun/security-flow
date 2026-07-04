# BankingTroubles Lab

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_bankingtroubles_lab.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for email, ids, memory challenges.

## Input Signals

- Artifacts: email, ids, memory, pe-malware, registry
- Tools: strings, virustotal, volatility
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, malware-static, memory-forensics, stego-extraction

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: What was the local IP address of the victim's machine?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.0.176`

### Step 2: What was the OS environment variable's value?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility with the extracted filter/query `profile=WinXPSP2x86 -g 0x80544ce0 envars | Select-String -Pattern` and inspect the matching evidence.
- Tools: strings, volatility
- Filters or commands:
  - `profile=WinXPSP2x86 -g 0x80544ce0 envars | Select-String -Pattern`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility with the extracted filter/query `profile=WinXPSP2x86 -g 0x80544ce0 envars | Select-String -Pattern` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Windows_NT`

### Step 3: What was the Administrator's password?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use strings, volatility to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `password`

### Step 4: Which process was most likely responsible for the initial exploit?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: strings, volatility
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `AcroRd32.exe`

### Step 5: What is the extension of the malicious file retrieved from the process responsible for the initial exploit?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `profile=WinXPSP2x86 -g 0x80544ce0 filescan | Select-String -Pattern` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `profile=WinXPSP2x86 -g 0x80544ce0 filescan | Select-String -Pattern`
  - `profile=WinXPSP2x86 -g 0x80544ce0 malfind | Select-String -Pattern`
  - `strings Bob.vmem | grep -F '.php' | grep '^http:'`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use strings, virustotal, volatility with the extracted filter/query `profile=WinXPSP2x86 -g 0x80544ce0 filescan | Select-String -Pattern` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `pdf`

### Step 6: "528afe08e437765cc" . When was this file first submitted for analysis on VirusTotal?

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use strings, volatility with the extracted filter/query `md5sum * | grep "528afe08e437765cc"` and inspect the matching evidence.
- Tools: strings, volatility
- Filters or commands:
  - `md5sum * | grep "528afe08e437765cc"`
- Reasoning chain:
  - Recognize the goal as indicator enrichment.
  - Use strings, volatility with the extracted filter/query `md5sum * | grep "528afe08e437765cc"` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2010-03-29 19:31:45`

### Step 7: What was the PID of the process that loaded the file PDF .php?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, virustotal, volatility with the extracted filter/query `strings 1752.dmp | grep "PDF.php"` and inspect the matching evidence.
- Tools: strings, virustotal, volatility
- Filters or commands:
  - `strings 1752.dmp | grep "PDF.php"`
  - `o This command extracts the object “1054” which contains JavaScript code as`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, virustotal, volatility with the extracted filter/query `strings 1752.dmp | grep "PDF.php"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1752`

### Step 8: '\WINDOWS\system32\config\software' , and is variant of ZeuS trojan?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use strings, volatility with the extracted filter/query `strings Bob.vmem | grep "^http:"` and inspect the matching evidence.
- Tools: strings, volatility
- Filters or commands:
  - `strings Bob.vmem | grep "^http:"`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use strings, volatility with the extracted filter/query `strings Bob.vmem | grep "^http:"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sdra64.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
