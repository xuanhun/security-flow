# NukeTheBrowser Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Hard`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_nuke_the_browser_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for ids, pcap challenges.

## Input Signals

- Artifacts: ids, pcap
- Tools: virustotal, wireshark
- Techniques: cti-enrichment, dns-analysis, http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: When approaching network forensics, I like to begin by baselining the traffic, which involves

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use virustotal, wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `10.0.5.15`

### Step 2: What protocol do you think the attack was carried over?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `_path=="http" | cut ts, id.orig_h, id.resp_h, id_resp_p, method,` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `_path=="http" | cut ts, id.orig_h, id.resp_h, id_resp_p, method,`
  - `_path=="files" id.resp_h==192.168.56.50`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `_path=="http" | cut ts, id.orig_h, id.resp_h, id_resp_p, method,` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http`

### Step 3: What was the URL for the page used to serve malicious executables (don't include URL parameters)?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark with the extracted filter/query `There are multiple ways of finding executables downloaded over HTTP. The easiest method is` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `There are multiple ways of finding executables downloaded over HTTP. The easiest method is`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark with the extracted filter/query `There are multiple ways of finding executables downloaded over HTTP. The easiest method is` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `http://sploitme.com.cn/fg/load.php`

### Step 4: and probably is an indicator for Geo-based targeting?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `http contains “www.google.fr”` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `http contains “www.google.fr”`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `http contains “www.google.fr”` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `299`

### Step 5: What was the CMS used to generate the page 'shop.honeynet.sg/catalog/'? (Three words, space in between)

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `http.host=="shop.honeynet.sg" && http.request.uri == "/catalog/"` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `http.host=="shop.honeynet.sg" && http.request.uri == "/catalog/"`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `http.host=="shop.honeynet.sg" && http.request.uri == "/catalog/"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `osCommerce Online Merchant`

### Step 6: same host twice?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark with the extracted filter/query `http.request.uri contains "show.php"` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `http.request.uri contains "show.php"`
  - `ip.addr==192.168.56.52 && http && ip.addr==10.0.3.15`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark with the extracted filter/query `http.request.uri contains "show.php"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `366`

### Step 7: What is the name of the executable being served via

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark with the extracted filter/query `ip.addr==192.168.56.52 && http` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `ip.addr==192.168.56.52 && http`
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark with the extracted filter/query `ip.addr==192.168.56.52 && http` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.56.52`

### Step 8: Convert those bytes into a Base64 string.

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 9: Base64-decode and UTF-8-decode the result.

- Route type: `virustotal-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as virustotal-driven evidence lookup.
  - Use virustotal, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(decrypt_crypt_obfuscation(data))`

### Step 10: extract anything useful:

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal, wireshark with the extracted filter/query `_path=="files" "78873f791"` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `_path=="files" "78873f791"`
  - `ip.addr==192.168.56.52 && http`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal, wireshark with the extracted filter/query `_path=="files" "78873f791"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e.exe`

### Step 11: What is the name of the function that hosted the shellcode relevant to

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use virustotal, wireshark with the extracted filter/query `http.host=="shop.honeynet.sg" && http.request.uri == "/catalog/"` and inspect the matching evidence.
- Tools: virustotal, wireshark
- Filters or commands:
  - `http.host=="shop.honeynet.sg" && http.request.uri == "/catalog/"`
  - `http.host=="rapidshare.com.eyu32.ru" && http.request.uri ==`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use virustotal, wireshark with the extracted filter/query `http.host=="shop.honeynet.sg" && http.request.uri == "/catalog/"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `aolwinamp`

### Step 12: What was the version of 'mingw-gcc' that compiled the malware?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3.4.5`

### Step 13: to the compromised host. What is the name of the function?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: virustotal, wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use virustotal, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `URLDownloadToFile`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
