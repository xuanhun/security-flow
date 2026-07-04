# 题目：[GCCCTF 2025]DNS Courier

## Case Metadata

- Category: `Misc`
- Platform: `GCCCTF2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/GCCCTF2025_DNS_Courier.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/GCCCTF2025_DNS_Courier.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/GCCCTF2025_DNS_Courier.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, pcap challenges.

## Input Signals

- Artifacts: binary, ciphertext, pcap, stego-media
- Tools: netcat, wireshark
- Techniques: crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, http-analysis, image-analysis, misc-analysis, network-forensics, php-tricks, qr-analysis, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `11`
- `misc/images/DNS_Courier/dns-analyse.png`
- `misc/images/DNS_Courier/encrypt.png`
- `misc/images/DNS_Courier/tail.png`
- `misc/images/DNS_Courier/hash.png`
- `misc/images/DNS_Courier/dorking.png`
- `misc/images/DNS_Courier/crc.png`
- `misc/images/DNS_Courier/result.png`
- `misc/images/DNS_Courier/mask-pattern.png`
- `misc/images/DNS_Courier/flag.png`
- `misc/images/DNS_Courier/flag-1.png`
- `misc/images/DNS_Courier/chatgpt5.png`

## Solve Thinking

### Step 1: 考点：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use netcat, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use netcat, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#流量分析 #dns外带 #已知明文攻击 #二维码结构`

### Step 2: 思路：

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat, wireshark with the extracted filter/query `dns.flags.response== 0&&ip.addr==8.8.8.8&&dns.qry.name contains "google.com"` and inspect the matching evidence.
- Tools: netcat, wireshark
- Filters or commands:
  - `dns.flags.response== 0&&ip.addr==8.8.8.8&&dns.qry.name contains "google.com"`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat, wireshark with the extracted filter/query `dns.flags.response== 0&&ip.addr==8.8.8.8&&dns.qry.name contains "google.com"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.33.167`

### Step 3: ---------- 通用工具 ----------

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark with the extracted filter/query `if j == -1: break` and inspect the matching evidence.
- Tools: netcat, wireshark
- Filters or commands:
  - `if j == -1: break`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark with the extracted filter/query `if j == -1: break` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print(msg, flush=True)`

### Step 4: ---------- 识别/解压 ----------

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `with zipfile.ZipFile(io.BytesIO(b)) as zf:`

### Step 5: 列出内容

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `human(f" - {zi.filename} | Compressed={zi.compress_size} | Uncompressed={zi.file_size} | Encrypted={enc}")` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `human(f" - {zi.filename} | Compressed={zi.compress_size} | Uncompressed={zi.file_size} | Encrypted={enc}")`
  - `human(f" - {ti.name} | Size={ti.size}")`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `human(f" - {zi.filename} | Compressed={zi.compress_size} | Uncompressed={zi.file_size} | Encrypted={enc}")` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `head = payload[:8]`

### Step 6: ZIP

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return try_extract_zip_bytes(payload, out_dir)`

### Step 7: GZIP

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `return True`

### Step 8: 7Z

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return True`

### Step 9: RAR4/5

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return True`

### Step 10: XZ

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `return True`

### Step 11: 常见文件（便于识别）

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `return True`

### Step 12: 尝试在中间寻找 PNG 魔术字（有时前缀会插入标记）

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: netcat, wireshark
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `return True`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
