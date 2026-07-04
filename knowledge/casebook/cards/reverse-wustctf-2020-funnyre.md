# [WUSTCTF 2020] funnyre

## Case Metadata

- Category: `Reverse`
- Platform: `WUSTCTF 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[WUSTCTF 2020] funnyre.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5BWUSTCTF%202020%5D%20funnyre.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[WUSTCTF 2020] funnyre.md`
- Challenge URL: `https://www.nssctf.cn/problem/2000`

## Why This Case Matters

Use this case as a Reverse reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: IDA Pro, angr, ida
- Techniques: http-analysis, reverse-engineering, symbolic-execution, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `6`
- `reverse/images/[WUSTCTF 2020] funnyre_1.png`
- `reverse/images/[WUSTCTF 2020] funnyre_2.png`
- `reverse/images/[WUSTCTF 2020] funnyre_3.png`
- `reverse/images/[WUSTCTF 2020] funnyre_4.png`
- `reverse/images/[WUSTCTF 2020] funnyre_5.png`
- `reverse/images/[WUSTCTF 2020] funnyre_6.png`

## Solve Thinking

### Step 1: 基础：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use IDA Pro, angr, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: IDA Pro, angr, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use IDA Pro, angr, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `上面只是基础的花指令，只增加“垃圾”，不十分影响反汇编，但是还有**进阶的花指令**`

### Step 2: 进阶：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `按照我**自己对这种花指令的理解**就是：像你拿了一本书，但有人故意在每页加了乱码、跳转标记、断页，你根本读不出它原来讲了啥。`

### Step 3: 处理花指令：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use IDA Pro, angr, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: IDA Pro, angr, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use IDA Pro, angr, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `当然还有很多需要跟踪跳转必要时才nop等等。`

### Step 4: 1 看到什么

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use IDA Pro, angr, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: IDA Pro, angr, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use IDA Pro, angr, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `下载附件后发现是ELF文件（同样是可执行文件，是Unix/Linux系统下的可执行文件）`

### Step 5: 2 解题思路

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `由于花指令，所以先尝试能不能把花指令除去，然后去修复代码，使得能正常F5查看伪代码方便进行逆向分析，最后写出脚本得出flag。`

### Step 6: 3 ✅ 尝试过程和结果记录

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use angr, ida to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: angr, ida
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use angr, ida to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1dc20f6e3d497d15cef47d9a66d6f1af`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
