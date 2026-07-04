# 2025 年 [04-11~04-16]  题单 by LimeCocoa

## Case Metadata

- Category: `Misc`
- Platform: `2025 年 [04`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/cuc_training_20250416.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/cuc_training_20250416.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/cuc_training_20250416.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, pcap challenges.

## Input Signals

- Artifacts: binary, ciphertext, pcap, web-app, web-service
- Tools: burp, strings, wireshark
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, malware-static, misc-analysis, network-forensics, stego-extraction, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `9`
- `misc/images/tcp.png`
- `misc/images/ps.png`
- `misc/images/DB_flag.png`
- `misc/images/flag2.png`
- `misc/images/可疑IP.png`
- `misc/images/exe.png`
- `misc/images/xxd.png`
- `misc/images/nginx.png`
- `misc/images/flag4.png`

## Solve Thinking

### Step 1: 本周主题关键词

- Route type: `burp-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, strings, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, strings, wireshark
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, strings, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `威胁检测与网络流量分析`

### Step 2: 本周题目

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, strings, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, strings, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, strings, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `解压密码：11b0526b-9cfb-4ac4-8a75-10ad9097b7ce`

### Step 3: 当堂题目

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, strings, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, strings, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, strings, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [ ] 2024长城杯&CISCN-威胁流量分析-zeroshell_6 https://xj.edisec.net/challenges/104`

### Step 4: 2024长城杯&CISCN-威胁流量分析-zeroshell_1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use wireshark with the extracted filter/query `![](./images/tcp.png)` and inspect the matching evidence.
- Tools: wireshark
- Filters or commands:
  - `![](./images/tcp.png)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use wireshark with the extracted filter/query `![](./images/tcp.png)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{6C2E38DA-D8E4-8D84-4A4F-E2ABD07A1F3A}`

### Step 5: 2024长城杯&CISCN-威胁流量分析-zeroshell_2

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{c6045425-6e6e-41d0-be09-95682a4f65c4}`

### Step 6: 2024长城杯&CISCN-威胁流量分析-zeroshell_3

- Route type: `burp-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, strings, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, strings, wireshark
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, strings, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `16.122.33.44`

### Step 7: 2024长城杯&CISCN-威胁流量分析-zeroshell_4

- Route type: `burp-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, strings, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, strings, wireshark
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, strings, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{.nginx}`

### Step 8: 2024长城杯&CISCN-威胁流量分析-zeroshell_5

- Route type: `strings-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings to collect the smallest evidence slice that answers the goal.
- Tools: strings
- Reasoning chain:
  - Recognize the section as strings-driven evidence lookup.
  - Use strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{11223344qweasdzxc}`

### Step 9: 2024长城杯&CISCN-威胁流量分析-zeroshell_6

- Route type: `burp-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, strings, wireshark with the extracted filter/query `| 变量名 | 含义 |` and inspect the matching evidence.
- Tools: burp, strings, wireshark
- Filters or commands:
  - `| 变量名 | 含义 |`
  - `| ---------------------------------------------- | ------------------------------------------------------------ |`
  - `| `CONSOLE=/dev/console` | 指定系统控制台设备，通常用于 early boot 或 init 阶段输出。 |`
  - `| `SCRIPT=./File` | 表示执行的脚本名为 `./File`，说明是运行当前目录下名为 `File` 的脚本。 |`
  - `| `INIT_VERSION=sysvinit-2.85` | 当前系统使用的是 sysvinit v2.85 初始化系统。 |`
  - `| `PATH=...` | 当前进程的环境变量 PATH，决定了查找可执行文件的路径顺序。 |`
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, strings, wireshark with the extracted filter/query `| 变量名 | 含义 |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{/var/register/system/startup/scripts/nat/File}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
