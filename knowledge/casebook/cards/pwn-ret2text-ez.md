# [MoeCTF 2021]ret2text_ez

## Case Metadata

- Category: `Pwn`
- Platform: `MoeCTF 2021`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/ret2text_ez.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/ret2text_ez.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/ret2text_ez.md`
- Challenge URL: `https://www.nssctf.cn/problem/3406`

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

- Referenced assets: `2`
- `pwn/images/r2ez-func.png`
- `pwn/images/r2ez-vuln.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat, radare2 to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat, radare2 to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- vuln函数是栈溢出漏洞函数（read溢出0x12），backdoor函数后门函数，直接调用shell`

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
- Result: `- 直接栈溢出+ret2text跳转至backdoor`

### Step 3: 第一轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, python-pwntools, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, python-pwntools, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- payload = b”a”*0x28 + p64(0x401196)`

### Step 4: Payload

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
