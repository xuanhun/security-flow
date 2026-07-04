# [FSCTF 2023]rdi

## Case Metadata

- Category: `Pwn`
- Platform: `FSCTF 2023`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/rdi.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/rdi.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/rdi.md`
- Challenge URL: `https://www.nssctf.cn/problem/4444`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, python-pwntools, pwntools
- Techniques: binary-exploitation, http-analysis, ret2libc, ret2text, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `pwn/images/rdi-info.png`
- `pwn/images/rdi-main.png`
- `pwn/images/rdi-gadget.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python-pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 三个自定义函数（包含main）`

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
- Result: `- 通过修改栈内空间[rbp-0x8]，写入"/bin/sh"`

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
- Result: `- "sh"字符串0x40080d（通过0x4007f4去掉前面的字符）`

### Step 4: 尝试过程和结果记录

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use gdb, python-pwntools, pwntools to align timestamps and identify the event that satisfies the question.
- Tools: gdb, python-pwntools, pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use gdb, python-pwntools, pwntools to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- sendline，成功getshell`

### Step 5: Payload

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
