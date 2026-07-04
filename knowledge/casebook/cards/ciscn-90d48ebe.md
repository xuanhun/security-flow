# 第二届长城杯&CISCN半决赛-应急响应 · 玄机 - EDISEC https://xj.edisec.net/challenges/117

## Case Metadata

- Category: `Incident Response`
- Platform: `第二届长城杯&CISCN半决赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `应急响应/第二届长城杯&CISCN半决赛-应急响应.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/%E7%AC%AC%E4%BA%8C%E5%B1%8A%E9%95%BF%E5%9F%8E%E6%9D%AF%26CISCN%E5%8D%8A%E5%86%B3%E8%B5%9B-%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/应急响应/第二届长城杯&CISCN半决赛-应急响应.md`

## Why This Case Matters

Use this case as a Incident Response reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: R-studio, ghidra或IDA, ghidra, ida, radare2, strings
- Techniques: crypto-analysis, http-analysis, malware-static, php-tricks, qr-analysis, reverse-engineering, stego-extraction, web-exploitation

## First-Principles Route

- Anchor the case in the supplied host, log, or traffic artifact and build a time-bounded incident narrative.
- Correlate users, processes, files, timestamps, and network indicators before trusting any single log line.
- Preserve the exact log field or recovered artifact that proves each conclusion.

## Linked Assets

- Referenced assets: `3`
- `应急响应/images/3-26wp_1txt.png`
- `应急响应/images/3-26wp_strings.png`
- `应急响应/images/3-26wp_key.png`

## Solve Thinking

### Step 1: 第二届长城杯&CISCN半决赛-应急响应 · 玄机 - EDISEC https://xj.edisec.net/challenges/117

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use ghidra, ida to anchor the event in time, user, host, and file/process context before answering.
- Tools: ghidra, ida
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use ghidra, ida to anchor the event in time, user, host, and file/process context before answering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 工具清单：R-studio、ghidra或IDA`

### Step 2: 第一问：

- Route type: `R-studio-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
- Tools: R-studio, ghidra或IDA, ghidra, ida, radare2
- Reasoning chain:
  - Recognize the section as R-studio-driven evidence lookup.
  - Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ````txt`

### Step 3: File marks:

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use ghidra, ida, strings with the extracted filter/query `|4,48,6,0,1740374317,"/etc/systemd/system/system-upgrade.service"` and inspect the matching evidence.
- Tools: ghidra, ida, strings
- Filters or commands:
  - `|4,48,6,0,1740374317,"/etc/systemd/system/system-upgrade.service"`
  - `|4,49,6,0,1740374161,"/etc/systemd/system/system-upgrade.service"`
  - `|4,50,5,7,1740374151,"/etc/systemd/system/system-upgrade.service"`
  - `|4,51,5,7,1740374151,"/etc/systemd/system/system-upgrade.service"`
  - `|4,52,5,7,1740374151,"/etc/systemd/system/system-upgrade.service"`
  - `|4,53,5,7,1740374151,"/etc/systemd/system/system-upgrade.service"`
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use ghidra, ida, strings with the extracted filter/query `|4,48,6,0,1740374317,"/etc/systemd/system/system-upgrade.service"` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `192.168.57.203:4948`

### Step 4: 第二问：

- Route type: `R-studio-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
- Tools: R-studio, ghidra或IDA, ghidra, ida, radare2
- Reasoning chain:
  - Recognize the section as R-studio-driven evidence lookup.
  - Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `对第一问中得到的`systemd-agentd`找到文件路径然后对文件进行MD5即可`

### Step 5: 第三问：

- Route type: `R-studio-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
- Tools: R-studio, ghidra或IDA, ghidra, ida, radare2
- Reasoning chain:
  - Recognize the section as R-studio-driven evidence lookup.
  - Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `对我们第一问中得到的`system_upgrade.ko`找到文件路径然后对文件进行md5即可`

### Step 6: 第四问：

- Route type: `R-studio-driven evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
- Tools: R-studio, ghidra或IDA, ghidra, ida, radare2
- Reasoning chain:
  - Recognize the section as R-studio-driven evidence lookup.
  - Use R-studio, ghidra或IDA, ghidra, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `将第一问中的1.txt中的程序植入名称`.system_upgrade`进行MD5即可`

### Step 7: 第五问：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use radare2, strings with the extracted filter/query `while (iVar1 = FUN_00457bc0(param_1,param_2,&DAT_004beff6), iVar1 != -1) {` and inspect the matching evidence.
- Tools: radare2, strings
- Filters or commands:
  - `while (iVar1 = FUN_00457bc0(param_1,param_2,&DAT_004beff6), iVar1 != -1) {`
  - `if (iVar1 == 0x70) {`
  - `if (DAT_006eb160 == 0) {`
  - `else if (iVar1 == 0x73) {`
  - `if (iVar1 != 99) {`
  - `if (DAT_006f62b0 == (char *)0x0) {`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use radare2, strings with the extracted filter/query `while (iVar1 = FUN_00457bc0(param_1,param_2,&DAT_004beff6), iVar1 != -1) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `可以得到加密密钥`ThIS_1S_th3_S3cR3t_fl@g``

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
