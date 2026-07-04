# [HNCTF 2022 Week1]easyoverflow

## Case Metadata

- Category: `Pwn`
- Platform: `HNCTF 2022 Week1`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[HNCTF 2022 Week1]easyoverflow.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BHNCTF%202022%20Week1%5Deasyoverflow.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[HNCTF 2022 Week1]easyoverflow.md`
- Challenge URL: `https://www.nssctf.cn/problem/2941`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, netcat, pwntools
- Techniques: binary-exploitation, command-injection, file-inclusion, http-analysis, ret2libc, ret2text, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `pwn/images/HNCTF_2022_Week1easyoverflow-file.png`
- `pwn/images/HNCTF_2022_Week1easyoverflow-disassemble_main.png`
- `pwn/images/HNCTF_2022_Week1easyoverflow-stack_status.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if(number!=0){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(number!=0){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if(number!=0){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- easy_overflow:可执行程序，可用于`动态或者静态调试``

### Step 2: 想到什么解题思路

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb to collect the smallest evidence slice that answers the goal.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 使用gdb静态调试,判断需要溢出的位置,编写`exp`将参数传到`远程环境``

### Step 3: 尝试过程与结果记录

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat, pwntools with the extracted filter/query `gdb easy_overflow` and inspect the matching evidence.
- Tools: gdb, netcat, pwntools
- Filters or commands:
  - `gdb easy_overflow`
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat, pwntools with the extracted filter/query `gdb easy_overflow` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `n.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
