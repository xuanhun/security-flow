# Masterminds

## Case Metadata

- Category: `Network Forensics`
- Platform: `TryHackMe`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/masterminds.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, ids, pcap challenges.

## Input Signals

- Artifacts: email, ids, pcap
- Tools: suricata, urlhaus, virustotal, zeek
- Techniques: browser-forensics, cti-enrichment, dns-analysis, http-analysis, network-forensics

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: determine who stands behind the attack. Infection 1

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use suricata, virustotal, zeek with the extracted filter/query `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip` and inspect the matching evidence.
- Tools: suricata, virustotal, zeek
- Filters or commands:
  - `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip`
  - `_path=="http" status_code==404 | cut id.orig_h, id.resp_h, id.resp_p, host, uri,`
  - `_path=="http" response_body_len==1309 | cut id.orig_h, id.resp_h, id.resp_p, host,`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use suricata, virustotal, zeek with the extracted filter/query `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `The answer is host,id.resp_h.`

### Step 2: How many unique DNS requests were made to cab[.]myfkn[.]com domain (including the capitalised domain)?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal with the extracted filter/query `_path=="dns" CAB.MYKFN.COM cab.mykfn.com | count() by query | sort -r` and inspect the matching evidence.
- Tools: virustotal
- Filters or commands:
  - `_path=="dns" CAB.MYKFN.COM cab.mykfn.com | count() by query | sort -r`
  - `_path=="http" host=="bhaktivrind.com" | cut host, uri`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal with the extracted filter/query `_path=="dns" CAB.MYKFN.COM cab.mykfn.com | count() by query | sort -r` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `downloaded from the server.`

### Step 3: where I noticed a GET request with the uri /catzx.exe:

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use suricata, virustotal with the extracted filter/query `_path=="http" host=="hdmilg.xyz" | cut id.resp_h, uri` and inspect the matching evidence.
- Tools: suricata, virustotal
- Filters or commands:
  - `_path=="http" host=="hdmilg.xyz" | cut id.resp_h, uri`
  - `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip`
  - `_path=="http" 192.168.75.146 method=="POST" | cut id.resp_h, method, host, uri`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use suricata, virustotal with the extracted filter/query `_path=="http" host=="hdmilg.xyz" | cut id.resp_h, uri` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `185.239.234.112`

### Step 4: How many POST connections were made to the IP address in the previous question?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use suricata, virustotal with the extracted filter/query `_path=="http" 192.168.75.146 method=="POST" | cut id.resp_h, method, host | count()` and inspect the matching evidence.
- Tools: suricata, virustotal
- Filters or commands:
  - `_path=="http" 192.168.75.146 method=="POST" | cut id.resp_h, method, host | count()`
  - `_path=="http" _path=="http" | cut id.orig_h, id.resp_p, id.resp_h, host, uri`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use suricata, virustotal with the extracted filter/query `_path=="http" 192.168.75.146 method=="POST" | cut id.resp_h, method, host | count()` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.75.146`

### Step 5: destination IP addresses?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use suricata, urlhaus, virustotal with the extracted filter/query `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip, ts | sort ts` and inspect the matching evidence.
- Tools: suricata, urlhaus, virustotal
- Filters or commands:
  - `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip, ts | sort ts`
  - `_path=="http" | cut ts, id.orig_h, id.resp_h, id.resp_p, method, host, uri`
  - `_path=="http" | cut ts, id.orig_h, id.resp_h, id.resp_p, method, host, uri | sort ts`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use suricata, urlhaus, virustotal with the extracted filter/query `event_type=="alert" | alerts := union(alert.category) by src_ip, dest_ip, ts | sort ts` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.75.146`

### Step 6: address from the previous answer?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal with the extracted filter/query `_path=="dns" 162.217.98.146 | count() by query | sort -r` and inspect the matching evidence.
- Tools: virustotal
- Filters or commands:
  - `_path=="dns" 162.217.98.146 | count() by query | sort -r`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal with the extracted filter/query `_path=="dns" 162.217.98.146 | count() by query | sort -r` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `162.217.98.146`

### Step 7: How many binaries were downloaded from the above domain in total?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use virustotal with the extracted filter/query `_path=="http" efhoahegue.ru | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri` and inspect the matching evidence.
- Tools: virustotal
- Filters or commands:
  - `_path=="http" efhoahegue.ru | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri`
  - `_path=="http" | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri, user_agent`
  - `_path=="dns" | count()`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use virustotal with the extracted filter/query `_path=="http" efhoahegue.ru | cut id.orig_h, id.resp_h, id.resp_p, method,host, uri` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `there.`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
