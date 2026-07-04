# [GHCTF 2025]Hello_world

## Case Metadata

- Category: `Pwn`
- Platform: `GHCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[GHCTF 2025]Hello_world.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BGHCTF%202025%5DHello_world.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[GHCTF 2025]Hello_world.md`
- Challenge URL: `https://www.nssctf.cn/problem/6543`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ida, pwntools
- Techniques: binary-exploitation, http-analysis, ret2text, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `4`
- `pwn/images/GHCTF_2025_Hello_world_file.png`
- `pwn/images/GHCTF_2025_Hello_world_func1.png`
- `pwn/images/GHCTF_2025_Hello_world_backdoor.png`
- `pwn/images/GHCTF_2025_Hello_world_getshell.png`

## Solve Thinking

### Step 1: 文件分析

- Route type: `ida-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- PIE保护开启 （地址随机化）`

### Step 2: IDA 分析

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 目标：覆盖返回地址 控制流跳转到 backdoor 函数`

### Step 3: 想到什么解题思路

- Route type: `ida-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 小端序写入 `\xC1\x09` 高位保持不变`

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
- Result: `![GHCTF_2025_Hello_world_getshell](./images/GHCTF_2025_Hello_world_getshell.png)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
