# Zeek Exercises

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/zeek_exercises.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, pcap, web-service challenges.

## Input Signals

- Artifacts: email, pcap, web-service
- Tools: cyberchef, nmap, virustotal, zeek
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics, service-enumeration

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: DNS records linked to the IPv6 address?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, zeek with the extracted filter/query `zeek -C -r dns-tunneling.pcap` and inspect the matching evidence.
- Tools: cyberchef, virustotal, zeek
- Filters or commands:
  - `zeek -C -r dns-tunneling.pcap`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, zeek with the extracted filter/query `zeek -C -r dns-tunneling.pcap` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- zeek -C -r dns-tunneling.pcap`

### Step 2: Investigate the conn.log file. What is the longest connection duration?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, zeek with the extracted filter/query `Investigate the http.log file. Which domain address were the malicious files downloaded` and inspect the matching evidence.
- Tools: cyberchef, virustotal, zeek
- Filters or commands:
  - `Investigate the http.log file. Which domain address were the malicious files downloaded`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, zeek with the extracted filter/query `Investigate the http.log file. Which domain address were the malicious files downloaded` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.6.27.102`

### Step 3: Investigate the extracted malicious .exe file. What is the given file name in VirusTotal?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use cyberchef, virustotal, zeek with the extracted filter/query `Investigate the http.log file. What is the request name of the downloaded malicious .exe` and inspect the matching evidence.
- Tools: cyberchef, virustotal, zeek
- Filters or commands:
  - `Investigate the http.log file. What is the request name of the downloaded malicious .exe`
  - `We can grep the log file with the mime_type or simply cat the http.log file and use zeek-cut to`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use cyberchef, virustotal, zeek with the extracted filter/query `Investigate the http.log file. What is the request name of the downloaded malicious .exe` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Investigate the malicious .exe file in VirusTotal. What is the contacted domain name? Enter`

### Step 4: signature.log file. What is the number of signature hits?

- Route type: `cyberchef-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, virustotal, zeek to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, virustotal, zeek
- Reasoning chain:
  - Recognize the goal as cyberchef-driven evidence lookup.
  - Use cyberchef, virustotal, zeek to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: Investigate the http.log file. Which tool is used for scanning?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, nmap, virustotal, zeek with the extracted filter/query `nmap was used for scanning.` and inspect the matching evidence.
- Tools: cyberchef, nmap, virustotal, zeek
- Filters or commands:
  - `nmap was used for scanning.`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, nmap, virustotal, zeek with the extracted filter/query `nmap was used for scanning.` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `nmap was used for scanning.`

### Step 6: Investigate the http.log file. What is the extension of the exploit file?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, virustotal, zeek with the extracted filter/query `I found the answer by simply printing the http.log file, piping it to zeek-cut and the rest of the` and inspect the matching evidence.
- Tools: cyberchef, virustotal, zeek
- Filters or commands:
  - `I found the answer by simply printing the http.log file, piping it to zeek-cut and the rest of the`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use cyberchef, virustotal, zeek with the extracted filter/query `I found the answer by simply printing the http.log file, piping it to zeek-cut and the rest of the` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `crated file?`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
