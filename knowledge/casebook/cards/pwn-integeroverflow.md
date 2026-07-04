# [SWPUCTF 2022 新生赛]Integer Overflow

## Case Metadata

- Category: `Pwn`
- Platform: `SWPUCTF 2022 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/IntegerOverflow.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/IntegerOverflow.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/IntegerOverflow.md`
- Challenge URL: `https://www.nssctf.cn/problem/2634`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, python-pwntools, redare2, netcat, pwntools
- Techniques: binary-exploitation, http-analysis, integer-overflow, ret2libc, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `7`
- `pwn/images/intOf-info.png`
- `pwn/images/intOf-func.png`
- `pwn/images/intOf-code.png`
- `pwn/images/intOf-vuln.png`
- `pwn/images/intOf-choice.png`
- `pwn/images/intOf-backdoor.png`
- `pwn/images/intOf-bin_sh.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use netcat to verify the numeric edge case and how it changes the downstream size or bounds check.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use netcat to verify the numeric edge case and how it changes the downstream size or bounds check.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 全局找shell字符串，找到“/bin/sh”`

### Step 2: 第一轮

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, python-pwntools, redare2, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, python-pwntools, redare2, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, python-pwntools, redare2, netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 由于32位程序，直接后跟shell字符串地址，调用时返回地址入栈，可以直接触发入栈传参。`

### Step 3: 第一轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python-pwntools, redare2, netcat to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python-pwntools, redare2, netcat, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python-pwntools, redare2, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 直接构造payload=padding * b’a’+p32(sys)+p32(sh_addr)`

### Step 4: Payload

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
