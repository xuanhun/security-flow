# [CISCN 2019华北]PWN1

## Case Metadata

- Category: `Pwn`
- Platform: `CISCN 2019华北`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[CISCN 2019华北]PWN1.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BCISCN%202019%E5%8D%8E%E5%8C%97%5DPWN1.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[CISCN 2019华北]PWN1.md`
- Challenge URL: `https://www.nssctf.cn/problem/100`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ghidra, netcat, pwntools
- Techniques: binary-exploitation, command-injection, http-analysis, ret2libc, ret2text, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `pwn/images/CISCN_2019_PWN1_file.png`
- `pwn/images/CISCN_2019_PWN1_backdoor.png`
- `pwn/images/CISCN_2019_PWN1_func.png`
- `pwn/images/CISCN_2019_PWN1_addr.png`
- `pwn/images/CISCN_2019_PWN1_catflag.png`

## Solve Thinking

### Step 1: 附件分析

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ghidra, netcat, pwntools with the extracted filter/query `grep -E "(flag|system|/bin/sh)"尝试查找关键字符串**` and inspect the matching evidence.
- Tools: ghidra, netcat, pwntools
- Filters or commands:
  - `grep -E "(flag|system|/bin/sh)"尝试查找关键字符串**`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ghidra, netcat, pwntools with the extracted filter/query `grep -E "(flag|system|/bin/sh)"尝试查找关键字符串**` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 推测存在后门函数直接调用了`system(cat / flag)``

### Step 2: 想到什么解题思路

- Route type: `ghidra-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ghidra, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: ghidra, netcat, pwntools
- Reasoning chain:
  - Recognize the section as ghidra-driven evidence lookup.
  - Use ghidra, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 覆盖返回地址 直接读取 flag`

### Step 3: 尝试过程和结果记录

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ghidra, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ghidra, netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ghidra, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![addr](./images/CISCN_2019_PWN1_addr.png)`

### Step 4: Payload

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![catflag](./images/CISCN_2019_PWN1_catflag.png)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
