# [SDCTF 2022]Horoscope

## Case Metadata

- Category: `Pwn`
- Platform: `SDCTF 2022`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/Horoscope.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/Horoscope.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/Horoscope.md`
- Challenge URL: `https://www.nssctf.cn/problem/2381`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, python-pwntools, pwntools
- Techniques: binary-exploitation, http-analysis, ret2text, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `pwn/images/horo-func.png`
- `pwn/images/horo-backdoor.png`
- `pwn/images/horo-vuln.png`
- `pwn/images/horo-processInput.png`
- `pwn/images/horo-switch.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat with the extracted filter/query `发现test函数是后门，需求temp==1，同时debug函数可以设置temp=1` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `发现test函数是后门，需求temp==1，同时debug函数可以设置temp=1`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat with the extracted filter/query `发现test函数是后门，需求temp==1，同时debug函数可以设置temp=1` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 注意到非1到12的前序输入会导致程序提前exit，因此需要特殊处理前序字节`

### Step 2: 第一轮

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, python-pwntools, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, python-pwntools, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, python-pwntools, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 跳转至backdoor（test）`

### Step 3: 第二轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python-pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 可以直接跳过test的校验，直接跳转至系统调用`

### Step 4: 第一轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python-pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- test_addr = 0x400950`

### Step 5: 第二轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python-pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- backdoor = 0x40095f`

### Step 6: Payload

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use gdb, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use gdb, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
