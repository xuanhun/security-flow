# [NISACTF 2022]ezpie

## Case Metadata

- Category: `Pwn`
- Platform: `NISACTF 2022`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/[NISACTF 2022]ezpie.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%5BNISACTF%202022%5Dezpie.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/[NISACTF 2022]ezpie.md`
- Challenge URL: `https://www.nssctf.cn/problem/2059`

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

- Referenced assets: `7`
- `pwn/images/NISACTF_2022_ezpie_file.png`
- `pwn/images/NISACTF_2022_ezpie_gdb1.png`
- `pwn/images/NISACTF_2022_ezpie_gdb2.png`
- `pwn/images/NISACTF_2022_ezpie_vuln.png`
- `pwn/images/NISACTF_2022_ezpie_shell_func.png`
- `pwn/images/NISACTF_2022_ezpie_main_addr.png`
- `pwn/images/NISACTF_2022_ezpie_getshell.png`

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
- Result: `- 运行程序会直接给出一个泄露地址`

### Step 2: 泄露地址分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 泄露的地址是 PIE 随机加载之后的真实地址`

### Step 3: IDA 分析

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- main 函数偏移 `0x770``

### Step 4: 想到什么解题思路

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `shell_addr = PIE_base + shell_offset`

### Step 5: Payload

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `![NISACTF_2022_ezpie_getshell](./images/NISACTF_2022_ezpie_getshell.png)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
