# 2025 年 [03-19 ~ 03-25]  题单 by 章艺怀

## Case Metadata

- Category: `Misc`
- Platform: `2025 年 [03`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/cuc_training_20250326.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/cuc_training_20250326.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/cuc_training_20250326.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, pcap challenges.

## Input Signals

- Artifacts: binary, ciphertext, pcap, stego-media, web-app
- Tools: binwalk, foremost, netcat, stegsolve, strings, wireshark
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, malware-static, misc-analysis, network-forensics, qr-analysis, stego-extraction, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `17`
- `misc/images/image.png`
- `misc/images/flag1.png`
- `misc/images/flag2.png`
- `misc/images/flag3.png`
- `misc/images/flag4.png`
- `misc/images/where_is_flag1.png`
- `misc/images/where_is_flag2.png`
- `misc/images/where_is_flag3.png`
- `misc/images/where_is_flag4.png`
- `misc/images/where_is_flag5.png`
- `misc/images/菜刀666_1.png`
- `misc/images/菜刀666_2.png`
- ... and `5` more

## Solve Thinking

### Step 1: 本周题目

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, foremost, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, foremost, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5847c561e29a1f87dfcd5e41badf86b4`

### Step 2: 当堂题目

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, foremost, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, foremost, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 3: 题目描述

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 一个 apng 文件`

### Step 4: 知识点解析

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- apng文件是一种继承自便携式网络图形（PNG）的文件格式，它允许像GIF格式一样播放动态图片，并且拥有GIF不支持的24位图像和8位透明性。 它还保留了与非动画PNG文件的向后兼容性。`

### Step 5: 题解

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: netcat, stegsolve
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `apngdis_gui.exe`

### Step 6: flag

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{a3c7e4e5-9b9d-ad20-0327-288a235370ea}`

### Step 7: 题目描述

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, strings, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, strings, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, strings, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![alt text](images/where_is_flag5.png)`

### Step 8: flag

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{p1e4se_st0p_h1t_7_7}`

### Step 9: 题目描述

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 一个流量包`

### Step 10: 题解

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use foremost to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: foremost
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use foremost to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 最后打开压缩包得到flag`

### Step 11: 答案

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{3OpWdJ-JP6FzK-koCMAK-VkfWBq-75Un2z}`

### Step 12: 题目描述

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 一个压缩包`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
