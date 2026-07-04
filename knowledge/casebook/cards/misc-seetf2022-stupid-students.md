# 题目：[SEETF 2022]Stupid students

## Case Metadata

- Category: `Misc`
- Platform: `SEETF2022`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/SEETF2022_Stupid_students.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/SEETF2022_Stupid_students.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/SEETF2022_Stupid_students.md`

## Why This Case Matters

Use this case as a Misc reference for ids, stego-media, web-app challenges.

## Input Signals

- Artifacts: ids, stego-media, web-app
- Tools: netcat
- Techniques: command-injection, encoding-analysis, http-analysis, image-analysis, misc-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `10`
- `misc/images/SEETF2022_Stupid_students/Header.png`
- `misc/images/SEETF2022_Stupid_students/Root.png`
- `misc/images/SEETF2022_Stupid_students/26_0_obj.png`
- `misc/images/SEETF2022_Stupid_students/Kids.png`
- `misc/images/SEETF2022_Stupid_students/2_0_obj.png`
- `misc/images/SEETF2022_Stupid_students/1_0_obj.png`
- `misc/images/SEETF2022_Stupid_students/12_0_obj.png`
- `misc/images/SEETF2022_Stupid_students/22_0_obj.png`
- `misc/images/SEETF2022_Stupid_students/flag.png`
- `misc/images/SEETF2022_Stupid_students/map.png`

## Solve Thinking

### Step 1: 考点：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `>Fix the PDF to get the flag`

### Step 2: 思路：

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- flag：NSSCTF{1_l0v3_pdf_fil3s_27f80154b082e53f7a19b58f7061a6cf}`

### Step 3: 参考链接

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[PDF-Explained](images/https://zxyle.github.io/PDF-Explained/)`

### Step 4: PDF本质：

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `由数值（整数、浮点数）；布尔值（true/false）；字符串；数组（列表）；字典（哈希表）等常见的数据形式组装起来的一个数据包。以上的种种数据格式，在PDF里面称为**object（对象）**，其中**stream**是PDF里面一种特殊的对象格式，可以储存任意的二进制数据，通常是嵌入PDF的字体、图片等非文本内容`

### Step 5: 树状结构

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- `/Contents`指向内容流stream（文本、图像、路径），没有Contents,Page存在，但是无法渲染。`

### Step 6: 推荐工具

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `直接编辑 PDF 二进制,修补 `/Pages`、`/Kids`等`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
