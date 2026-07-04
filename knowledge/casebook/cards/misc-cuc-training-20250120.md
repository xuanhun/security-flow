# 20 题解

## Case Metadata

- Category: `Misc`
- Platform: `cuc`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/cuc_training_20250120.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/cuc_training_20250120.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/cuc_training_20250120.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, memory, pcap challenges.

## Input Signals

- Artifacts: ciphertext, memory, pcap, registry, web-app
- Tools: cyberchef, netcat, radare2, volatility, wireshark
- Techniques: browser-forensics, classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, memory-forensics, misc-analysis, network-forensics, sql-injection, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Solve Thinking

### Step 1: [2022蓝帽杯]手机取证1

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef, netcat, radare2, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef, netcat, radare2, volatility, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use cyberchef, netcat, radare2, volatility to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 工具：盘古石阅读器`

### Step 2: [2023陇剑杯]Wireshark1_1

- Route type: `conversation statistics`
- Why: Packet-count questions usually reduce to conversation statistics after endpoint and protocol constraints are fixed.
- Probe: Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
- Tools: wireshark
- Reasoning chain:
  - Recognize the section as conversation statistics.
  - Use wireshark to inspect conversation statistics or packet counts for the constrained endpoints and protocol.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.246.28`

### Step 3: [2022蓝帽杯]网站取证_2

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, netcat with the extracted filter/query `$str = 'P3LMJ4uCbkFJ/RarywrCvA==';` and inspect the matching evidence.
- Tools: cyberchef, netcat
- Filters or commands:
  - `$str = 'P3LMJ4uCbkFJ/RarywrCvA==';`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, netcat with the extracted filter/query `$str = 'P3LMJ4uCbkFJ/RarywrCvA==';` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `config.php`

### Step 4: 加密后的字符串

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `encrypted_str = 'P3LMJ4uCbkFJ/RarywrCvA=='` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `encrypted_str = 'P3LMJ4uCbkFJ/RarywrCvA=='`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `encrypted_str = 'P3LMJ4uCbkFJ/RarywrCvA=='` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `encrypted_str = 'P3LMJ4uCbkFJ/RarywrCvA=='`

### Step 5: 密钥

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, radare2, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat, radare2, volatility, wireshark
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, radare2, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `key = b'PanGuShi'`

### Step 6: 使用空字节填充密钥到16字节

- Route type: `cyberchef-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat, radare2, volatility to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat, radare2, volatility, wireshark
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat, radare2, volatility to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `iv=b'130f028b5c4b9e1b'`

### Step 7: base64解码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `encrypted_data = base64.b64decode(encrypted_str)`

### Step 8: 创建AES解密器 (CBC模式)

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, netcat, radare2, volatility to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: cyberchef, netcat, radare2, volatility, wireshark
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, netcat, radare2, volatility to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cipher = AES.new(padded_key, AES.MODE_CBC, iv)`

### Step 9: 解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `decrypted_data = cipher.decrypt(encrypted_data)`

### Step 10: 去除填充

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef with the extracted filter/query `(base) ubuntu@MyROG:~$ echo -ne "PanGuShi\x00\x00\x00\x00\x00\x00\x00\x00" | base64` and inspect the matching evidence.
- Tools: cyberchef
- Filters or commands:
  - `(base) ubuntu@MyROG:~$ echo -ne "PanGuShi\x00\x00\x00\x00\x00\x00\x00\x00" | base64`
  - `UGFuR3VTaGkAAAAAAAAAAA==`
  - `(base) ubuntu@MyROG:~$ echo -ne "PanGuShi\x00\x00\x00\x00\x00\x00\x00\x00" | xxd -p`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef with the extracted filter/query `(base) ubuntu@MyROG:~$ echo -ne "PanGuShi\x00\x00\x00\x00\x00\x00\x00\x00" | base64` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `50616e47755368690000000000000000`

### Step 11: [OtterCTF 2018]General Info

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use radare2, volatility with the extracted filter/query `Volatility Foundation Volatility Framework 2.6` and inspect the matching evidence.
- Tools: radare2, volatility
- Filters or commands:
  - `Volatility Foundation Volatility Framework 2.6`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use radare2, volatility with the extracted filter/query `Volatility Foundation Volatility Framework 2.6` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0:1900`

### Step 12: [应急响应]welog1

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use cyberchef to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use cyberchef to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `192.168.150.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
