# WireDive Lab

## Case Metadata

- Category: `Network Forensics`
- Platform: `CyberDefenders`
- Difficulty: `Medium`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/cyber_defenders_wiredive_lab.pdf`

## Why This Case Matters

Use this case as a Network Forensics reference for email, pcap challenges.

## Input Signals

- Artifacts: email, pcap
- Tools: wireshark
- Techniques: dns-analysis, http-analysis, network-forensics, service-enumeration

## First-Principles Route

- Inventory capture files and identify dominant protocols, endpoints, and conversations.
- Prioritize cleartext protocols, credentials, DNS, HTTP objects, files, and suspicious long sessions.
- Use packet filters or stream following to connect each question to a specific packet, stream, or extracted object.
- When a file is recovered from traffic, pivot into file metadata and strings before deeper analysis.

## Solve Thinking

### Step 1: What IP address is requested by the client?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.2.244`

### Step 2: What is the transaction ID for the DHCP release?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0x9f8fa557`

### Step 3: What is the MAC address of the client?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use wireshark with the extracted filter/query `File: dns.pcapng` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `File: dns.pcapng`
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use wireshark with the extracted filter/query `File: dns.pcapng` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `00:0c:29:82:f5:94`

### Step 4: What is the response for the lookup for flag.fruitinc.xyz?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ACOOLDNSFLAG`

### Step 5: Which root server responds to the google.com query? Hostname.

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e.root-servers.net`

### Step 6: What is the path of the file that is opened?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HelloWorld\TradeSecrets.txt`

### Step 7: What was the hex status code when the user SAMBA\jtomato logs in?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0xc000006d`

### Step 8: What is the tree that is being browsed?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `\\192.168.2.10\public`

### Step 9: What is the flag in the file?

- Route type: `service-to-access path`
- Why: Boot2root routes chain enumeration, access, and local privilege checks; each hop needs proof.
- Probe: Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as service-to-access path.
  - Use wireshark to enumerate exposed services, then pivot to credentials, known flaws, or misconfigurations.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `OneSuperDuperSecret`

### Step 10: What port is the shell listening on?

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark with the extracted filter/query `ip.addr==192.168.2.5 && ip.addr==192.168.2.244` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `ip.addr==192.168.2.5 && ip.addr==192.168.2.244`
- Reasoning chain:
  - Recognize the goal as conversation statistics.
  - Use wireshark with the extracted filter/query `ip.addr==192.168.2.5 && ip.addr==192.168.2.244` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4444`

### Step 11: What is the port for the second shell?

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use wireshark with the extracted filter/query `ip.addr==192.168.2.244 && tcp.port==34972 && ip.addr==192.168.2.5 &&` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `ip.addr==192.168.2.244 && tcp.port==34972 && ip.addr==192.168.2.5 &&`
  - `tcp.port==9999`
  - `The TCP stream contains the /etc/passwd file.`
- Reasoning chain:
  - Recognize the goal as timeline reconstruction.
  - Use wireshark with the extracted filter/query `ip.addr==192.168.2.244 && tcp.port==34972 && ip.addr==192.168.2.5 &&` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9999`

### Step 12: What version of netcat is installed?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1.10-41.1`

### Step 13: What file is added to the second shell We found this earlier:

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/etc/passwd`

### Step 14: What password is used to elevate the shell? See above.

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `*umR@Q%4V&RC`

### Step 15: When the threat actor installs netcat, we can see the codename of the target system:

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `bionic`

### Step 16: How many users are on the target system?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `31`

### Step 17: What is the IPv6 NTP server IP?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2003:51:6012:110::dcf7:123`

### Step 18: What is the first IP address that is requested by the DHCP client?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.20.11`

### Step 19: What is the first authoritative name server returned for the domain that is being queried?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark with the extracted filter/query `dns.qry.name == "blog.webernetz.net" and dns.response_to` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `dns.qry.name == "blog.webernetz.net" and dns.response_to`
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark with the extracted filter/query `dns.qry.name == "blog.webernetz.net" and dns.response_to` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ns1.hans.hosteurope.de`

### Step 20: What is the number of the first VLAN to have a topology change occur?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark with the extracted filter/query `stp.flags.tc == 1` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `stp.flags.tc == 1`
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark with the extracted filter/query `stp.flags.tc == 1` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `20`

### Step 21: What is the port for CDP for CCNP-LAB-S2?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `GigabitEthernet0/2`

### Step 22: What is the MAC address for the root bridge for VLAN 60? • vlan.id == 60

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use wireshark to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `00:21:1b:ae:31:80`

### Step 23: What is the IOS version running on CCNP-LAB-S2?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `12.1(22)EA14`

### Step 24: What is the virtual IP address used for HSRP group 121? • hsrp2.group == 121

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.121.1`

### Step 25: How many router solicitations were sent? • icmpv6.type==133

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3`

### Step 26: What is the management address of CCNP-LAB-S2? • cdp

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.121.20`

### Step 27: What is the interface being reported on in the first SNMP query? • snmp

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use wireshark to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Fa0/1`

### Step 28: When was the NVRAM config last updated?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2017-03-03 21:02`

### Step 29: What is the IPv6 of the RADIUS server?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2001:DB8::1812`

### Step 30: What has been added to web interaction with web01.fruitinc.xyz?

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use wireshark to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use wireshark to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `y2*Lg4cHe@Ps`

### Step 31: What is the name of the photo that is viewed in slack?

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as http evidence extraction.
  - Use wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `get_a_new_phone_today__720.jpg`

### Step 32: What is the username and password to login to 192.168.2.1?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark with the extracted filter/query `ip.dst == 192.168.2.1 && http2` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `ip.dst == 192.168.2.1 && http2`
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark with the extracted filter/query `ip.dst == 192.168.2.1 && http2` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `admin:Ac5R4D9iyqD5bSh`

### Step 33: What is the certStatus for the certificate with a serial number of

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use wireshark to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as tls handshake inspection.
  - Use wireshark to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `good`

### Step 34: What is the email of someone who needs to change their password?

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as credential discovery.
  - Use wireshark to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Jim.Tomato@fruitinc.xyz`

### Step 35: A service is assigned to an interface. What is the interface, and what is the service?

- Route type: `wireshark-driven evidence lookup`
- Why: For Network Forensics, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark to collect the smallest evidence slice that answers the goal.
- Tools: wireshark
- Reasoning chain:
  - Recognize the goal as wireshark-driven evidence lookup.
  - Use wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `lan:ntp`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
