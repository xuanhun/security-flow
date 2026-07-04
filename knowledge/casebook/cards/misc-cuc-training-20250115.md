# 15 题解

## Case Metadata

- Category: `Misc`
- Platform: `cuc`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/cuc_training_20250115.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/cuc_training_20250115.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/cuc_training_20250115.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, registry challenges.

## Input Signals

- Artifacts: binary, ciphertext, registry, stego-media, web-app
- Tools: detect-it-easy, ida, netcat, strings
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, image-analysis, malware-static, misc-analysis, osint, qr-analysis, reverse-engineering, stego-extraction, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Solve Thinking

### Step 1: [MoeCTF 2022]寻找黑客的家

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, ida, netcat, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, ida, netcat, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* 工具：百度地图`

### Step 2: [MoeCTF 2022]zip套娃

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* Linux Shell：sudo, apt update, apt install`

### Step 3: 安装 cargo 和 zip-password-finder

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 4: ref: https://mirrors.tuna.tsinghua.edu.cn/help/crates.io-index/

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy, ida, netcat, strings with the extracted filter/query `cat << EOF | tee -a ${CARGO_HOME:-$HOME/.cargo}/config.toml` and inspect the matching evidence.
- Tools: detect-it-easy, ida, netcat, strings
- Filters or commands:
  - `cat << EOF | tee -a ${CARGO_HOME:-$HOME/.cargo}/config.toml`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy, ida, netcat, strings with the extracted filter/query `cat << EOF | tee -a ${CARGO_HOME:-$HOME/.cargo}/config.toml` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `EOF`

### Step 5: ref: https://github.com/agourlay/zip-password-finder

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: 解题

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, ida, netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, ida, netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 7: 默认爆破，找到密码 1235

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 8: 熟悉常用的爆破参数组合使用

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 9: 解压缩，得到新压缩包文件 fl.zip 和 密码.txt

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, ida, netcat, strings to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, ida, netcat, strings to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7z x f.zip -p1235`

### Step 10: 后三位被wuliao吃了

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: detect-it-easy, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy, ida, netcat, strings to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 11: Password found:1234567qwq

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `crunch 3 3 -f tools/charset.lst mixalpha-numeric -o crunch_dict.txt`

### Step 12: 然后将 1234567 作为前缀加入到 crunch_dict.txt 中

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `done < crunch_dict.txt`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
