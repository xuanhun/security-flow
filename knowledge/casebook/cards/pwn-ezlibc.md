# [SWPUCTF 2023 秋季新生赛]ezlibc

## Case Metadata

- Category: `Pwn`
- Platform: `SWPUCTF 2023 秋季新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/ezlibc.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/ezlibc.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/ezlibc.md`
- Challenge URL: `https://www.nssctf.cn/problem/4544`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, python-pwntools, python-LibcSearcher, netcat, pwntools
- Techniques: binary-exploitation, encoding-analysis, http-analysis, ret2libc, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `pwn/images/ezlibc-func.png`
- `pwn/images/ezlibc-vuln.png`
- `pwn/images/ezlibc-calc-libc.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- dofunc存在read栈溢出，同时调用了plt链接的write函数`

### Step 2: 第一轮

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 通过ROP来跳转回dofunc初始地址，重复执行dofunc来利用之前获取到的地址构造gadget获取shell`

### Step 3: 第一轮

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.send(payload2)`

### Step 4: Payload

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `padding = b'A' * 0x14`

### Step 5: 栈溢出覆盖地址跳转至plt表记录的write函数，并传入参数write(write_got,1,8),意为将内存中got表中记录的write函数存储地址定向写到标准输出，8是地址长度

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, python-pwntools, python-LibcSearcher, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, python-pwntools, python-LibcSearcher, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, python-pwntools, python-LibcSearcher, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
