# 2024长城杯&CISCN-威胁流量分析-zeroshell · 玄机 - EDISEC https://xj.edisec.net/challenges/104

## Case Metadata

- Category: `Incident Response`
- Platform: `2024长城杯&CISCN`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `应急响应/2024长城杯&CISCN-威胁流量分析-zeroshell.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/2024%E9%95%BF%E5%9F%8E%E6%9D%AF%26CISCN-%E5%A8%81%E8%83%81%E6%B5%81%E9%87%8F%E5%88%86%E6%9E%90-zeroshell.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/应急响应/2024长城杯&CISCN-威胁流量分析-zeroshell.md`

## Why This Case Matters

Use this case as a Incident Response reference for binary, ciphertext, pcap challenges.

## Input Signals

- Artifacts: binary, ciphertext, pcap, web-app
- Tools: wireshark, ghidra
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, misc-analysis, network-forensics, reverse-engineering, traffic-analysis, web-exploitation

## First-Principles Route

- Anchor the case in the supplied host, log, or traffic artifact and build a time-bounded incident narrative.
- Correlate users, processes, files, timestamps, and network indicators before trusting any single log line.
- Preserve the exact log field or recovered artifact that proves each conclusion.

## Linked Assets

- Referenced assets: `15`
- `应急响应/images/未命名_搭建防火墙环境.png`
- `应急响应/images/未命名_谷歌查找结果.png`
- `应急响应/images/未命名_查看验证漏洞poc.png`
- `应急响应/images/未命名_流量包poc.png`
- `应急响应/images/未命名_发现正确的位置.png`
- `应急响应/images/未命名_base64解码得到.png`
- `应急响应/images/未命名_查找文件中带flag.png`
- `应急响应/images/未命名_读取文件flag.png`
- `应急响应/images/未命名_外联进程相关id.png`
- `应急响应/images/未命名_进程对应的文件.png`
- `应急响应/images/未命名_读取木马文件后准备导出.png`
- `应急响应/images/未命名_打印可打印字符串.png`
- ... and `3` more

## Solve Thinking

### Step 1: 2024长城杯&CISCN-威胁流量分析-zeroshell · 玄机 - EDISEC https://xj.edisec.net/challenges/104

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ghidra, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ghidra, wireshark
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ghidra, wireshark to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 工具清单: wireshark、ghidra`

### Step 2: 第一问：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use wireshark, ghidra to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use wireshark, ghidra to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `base64解码得：`

### Step 3: flag值

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{6C2E38DA-D8E4-8D84-4A4F-E2ABD07A1F3A}`

### Step 4: 第二问：

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cat%20/Database/flag`

### Step 5: flag值

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{c6045435-6e6e-41d0-be09-95682a4f65c4}`

### Step 6: 第三问：

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `16.122.33.44`

### Step 7: flag值

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `202.115.89.103`

### Step 8: 第四问：

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ls%20-l%20/proc/10794%20%7C%20grep%20exe`

### Step 9: flag值

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{.nginx}`

### Step 10: 第五问：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `此外，也可以通过逆向分析elf文件的反连地址来获得flag`

### Step 11: flag值

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{11223344qweasdzxc}`

### Step 12: 第六问：

- Route type: `wireshark-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
- Tools: wireshark, ghidra
- Reasoning chain:
  - Recognize the section as wireshark-driven evidence lookup.
  - Use wireshark, ghidra to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `>请写出驻留木马的启动项，注意写出启动文件的完整路径。结果提交形式：flag{xxxx}，如flag{/a/b/c}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
