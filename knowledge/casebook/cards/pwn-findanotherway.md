# [SWPUCTF 2022 新生赛]FindanotherWay

## Case Metadata

- Category: `Pwn`
- Platform: `SWPUCTF 2022 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/FindanotherWay.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/FindanotherWay.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/FindanotherWay.md`
- Challenge URL: `https://www.nssctf.cn/problem/2783`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: IDA Pro 非必须, gdb, ida, netcat, pwntools
- Techniques: binary-exploitation, http-analysis, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `15`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-hello.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-func.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-disas_youfindit.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-strings.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-disas_nss.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-disas_vuln.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-disas_main.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-debug_1.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-debug_2.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-ret.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-padding.png`
- `pwn/images/SWPUCTF_2022_新生赛FindanotherWay-shell.png`
- ... and `3` more

## Solve Thinking

### Step 1: 第一轮

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 2: 第一轮

- Route type: `IDA Pro 非必须-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro 非必须, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as IDA Pro 非必须-driven evidence lookup.
  - Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 第一轮

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools, strings to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools, strings
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools, strings to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `p.interactive()`

### Step 4: 关于python pwn库的一些其他用法（GPT解答）

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 5: `pattern_create`

- Route type: `IDA Pro 非必须-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro 非必须, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as IDA Pro 非必须-driven evidence lookup.
  - Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这个函数会生成一个固定长度的、由唯一字符组成的字符串，形式通常是像 `Aa0Aa1Aa2...` 这样的字符序列。利用这种模式，我们可以在程序崩溃时通过查看栈中的内容，快速定位哪个位置覆盖了返回地址。`

### Step 6: 示例：

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `from pwn import *`

### Step 7: 创建一个长度为1000的模式

- Route type: `IDA Pro 非必须-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro 非必须, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as IDA Pro 非必须-driven evidence lookup.
  - Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `------`

### Step 8: `pattern_offset`

- Route type: `IDA Pro 非必须-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro 非必须, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as IDA Pro 非必须-driven evidence lookup.
  - Use IDA Pro 非必须, gdb, ida, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `当你用 `pattern_create` 创建了一个独特的模式并将它发送给程序时，程序会崩溃（通常是因为覆盖了返回地址或其它重要栈数据）。然后，你可以通过获取崩溃时栈中的内容来分析溢出的位置。`pattern_offset` 函数可以帮助你根据崩溃的堆栈内容找出偏移量。`

### Step 9: 如何使用 `pattern_offset`：

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - The proof is the controlled return or call path, plus the program behavior that reaches the target win path.
- Evidence rule: The proof is the controlled return or call path, plus the program behavior that reaches the target win path.

### Step 10: 示例：

- Route type: `pwntools-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use pwntools to collect the smallest evidence slice that answers the goal.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as pwntools-driven evidence lookup.
  - Use pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `from pwn import *`

### Step 11: 假设栈上的值是 0x61616161

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `------`

### Step 12: 具体应用过程

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb to collect the smallest evidence slice that answers the goal.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `------`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
