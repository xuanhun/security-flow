# [SUCTF 2018 招新赛]stack

## Case Metadata

- Category: `Pwn`
- Platform: `SUCTF 2018 招新赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/stack.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/stack.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/stack.md`
- Challenge URL: `https://www.nssctf.cn/problem/2333`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: 无, pwntools
- Techniques: binary-exploitation, http-analysis, ret2text, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `pwn/images/SUCTF_2018_招新赛_gdb-disas.png`
- `pwn/images/SUCTF_2018_招新赛_payload-stack.png`
- `pwn/images/SUCTF_2018_招新赛_flag-stack.png`

## Solve Thinking

### Step 1: 第一轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb to collect the smallest evidence slice that answers the goal.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `![gdb-disas.png](./images/SUCTF_2018_招新赛_gdb-disas.png)`

### Step 2: 第一轮

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use 无, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: 无, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use 无, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- **栈溢出+ret2text**`

### Step 3: 第一轮

- Route type: `无-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: 无, pwntools
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![flag-stack.png](./images/SUCTF_2018_招新赛_flag-stack.png)`

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
