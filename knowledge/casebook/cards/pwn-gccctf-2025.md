# 辣卤客，我为你带来烩面啦！

## Case Metadata

- Category: `Pwn`
- Platform: `GCCCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[GCCCTF 2025]辣卤客，我为你带来烩面啦！.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BGCCCTF%202025%5D%E8%BE%A3%E5%8D%A4%E5%AE%A2%EF%BC%8C%E6%88%91%E4%B8%BA%E4%BD%A0%E5%B8%A6%E6%9D%A5%E7%83%A9%E9%9D%A2%E5%95%A6%EF%BC%81.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[GCCCTF 2025]辣卤客，我为你带来烩面啦！.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, netcat, pwntools, ropgadget
- Techniques: binary-exploitation, command-injection, encoding-analysis, http-analysis, integer-overflow, ret2libc, ret2text, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Solve Thinking

### Step 1: 辣卤客，我为你带来烩面啦！

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, netcat, pwntools, ropgadget to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, netcat, pwntools, ropgadget to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 考点：栈溢出、整数溢出、伪随机Srand、Canary绕过、PIE绕过、ret2text、ret2libc、ROP、栈对齐`

### Step 2: 原型题

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, netcat, pwntools, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, netcat, pwntools, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://www.nssctf.cn/problem/3773`

### Step 3: 命题思路

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat, pwntools, ropgadget to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这题为了保证能有一定的通过率，涉及的考点都比较常见。Canary和base_addr都以gift的形式给出，可以直接利用构造ROP；`

### Step 4: 解题思路

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, netcat, pwntools, ropgadget to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: gdb, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, netcat, pwntools, ropgadget to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

### Step 5: exp

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use gdb, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use gdb, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `127.0.0.1`

### Step 6: 此处使用seed可以破解伪随机（也可以手动输出寄存器值得到实际随机值）

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, ropgadget to collect the smallest evidence slice that answers the goal.
- Tools: netcat, ropgadget
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, ropgadget to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
