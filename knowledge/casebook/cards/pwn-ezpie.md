# [NISACTF 2022]ezpie

## Case Metadata

- Category: `Pwn`
- Platform: `NISACTF 2022`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/ezpie.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/ezpie.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/ezpie.md`
- Challenge URL: `https://www.nssctf.cn/problem/2330`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, python:pwntools, pwntools
- Techniques: binary-exploitation, http-analysis, ret2libc, ret2text, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `17`
- `pwn/images/NISACTF_2022ezpiepwntools.png`
- `pwn/images/NISACTF_2022ezpiepwntool-out.png`
- `pwn/images/NISACTF_2022ezpieinfo_func.png`
- `pwn/images/NISACTF_2022ezpiefuncs.png`
- `pwn/images/NISACTF_2022ezpiemain1.png`
- `pwn/images/NISACTF_2022ezpiemain2.png`
- `pwn/images/NISACTF_2022ezpievuln.png`
- `pwn/images/NISACTF_2022ezpieshell.png`
- `pwn/images/NISACTF_2022ezpieaddr.png`
- `pwn/images/NISACTF_2022ezpieframe.png`
- `pwn/images/NISACTF_2022ezpieaddr_counting.png`
- `pwn/images/NISACTF_2022ezpiepayload1.png`
- ... and `5` more

## Solve Thinking

### Step 1: 第一轮

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![main1.png](./images/NISACTF_2022ezpiemain1.png)`

### Step 2: 第一轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python:pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python:pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python:pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 先`start`运行了再反汇编看看`

### Step 3: 第一轮

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, python:pwntools, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb, python:pwntools, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, python:pwntools, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 如此，确定攻击方式为**栈溢出**，需要完成的任务是**PIE绕过**和**ret2text**，其中**PIE绕过**是通过**泄露任意函数地址**作为**基地址**、使用函数之间的**相对位置关系**计算出跳转地址的**偏移量**。攻击者可以使用**基地址+偏移量**的方式来绕过PIE保护、确定希望跳转的地址。`

### Step 4: 第二轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python:pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python:pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python:pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `按理来说没错，但是出乎意料地失败了，于是回去debug`

### Step 5: 第三轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python:pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python:pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python:pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![flag.png](./images/NISACTF_2022ezpieflag.png)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
