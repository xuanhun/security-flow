# [GHCTF 2025]Hello_world

## Case Metadata

- Category: `Pwn`
- Platform: `GHCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/Hello_World.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/Hello_World.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/Hello_World.md`
- Challenge URL: `https://www.nssctf.cn/problem/6543`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: 无, gdb, netcat, pwntools
- Techniques: binary-exploitation, http-analysis, ret2libc, ret2text, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `17`
- `pwn/images/GHCTF_2025Hello_worldpwntools.png`
- `pwn/images/GHCTF_2025Hello_worldpwntools-result.png`
- `pwn/images/GHCTF_2025Hello_worldgdb-info-func.png`
- `pwn/images/GHCTF_2025Hello_worldinit.png`
- `pwn/images/GHCTF_2025Hello_worldout.png`
- `pwn/images/GHCTF_2025Hello_worldfunc1.png`
- `pwn/images/GHCTF_2025Hello_worldmain.png`
- `pwn/images/GHCTF_2025Hello_worldbackdoor.png`
- `pwn/images/GHCTF_2025Hello_worldpayload1.png`
- `pwn/images/GHCTF_2025Hello_worldstack1.png`
- `pwn/images/GHCTF_2025Hello_worldstack2.png`
- `pwn/images/GHCTF_2025Hello_worldpayload2.png`
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
- Result: `![gdb-info-func.png](./images/GHCTF_2025Hello_worldgdb-info-func.png)`

### Step 2: 第一轮

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use 无, gdb, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: 无, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use 无, gdb, netcat, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- **PIE绕过**：尝试寻找**泄露函数地址**的地方`

### Step 3: 第二轮

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: 无, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 局部覆盖地址`

### Step 4: 第三轮

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: 无, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 局部覆盖，未知位爆破`

### Step 5: 第一轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 转了一圈发现全程没有泄露过地址，泄露地址的思路泡汤。`

### Step 6: 第二轮

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: 无, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `![try1.png](./images/GHCTF_2025Hello_worldtry1.png)`

### Step 7: 第三轮

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: 无, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![flag.png](./images/GHCTF_2025Hello_worldflag.png)`

### Step 8: 本地工具环境配置

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `pip install pwntools`

### Step 9: Payload

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `break`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
