# [GCCCTF 2025] constraint

## Case Metadata

- Category: `Reverse`
- Platform: `GCCCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[GCCCTF 2025] constraint.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5BGCCCTF%202025%5D%20constraint.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[GCCCTF 2025] constraint.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, netcat, z3
- Techniques: reverse-engineering, stack-overflow, symbolic-execution

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: 看到什么

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use ida, netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: ida, netcat, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use ida, netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这是一道综合性的Reverse题目，涉及壳识别、脱壳、静态分析和约束求解。题目给出一个Windows PE 64位可执行文件calme.exe。`

### Step 2: 想到什么解题思路

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这些特征表明程序使用了 **UPX壳** 进行压缩。`

### Step 3: 尝试过程和结果记录

- Route type: `ida-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat, z3
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 4: 安装UPX（macOS）

- Route type: `ida-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat, z3
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `brew install upx`

### Step 5: 解包

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `calme.exe`

### Step 6: 静态分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `使用IDA Pro分析解包后的程序，找到两个关键函数：`

### Step 7: main函数 (0x4016ee)

- Route type: `netcat-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `if (len > 0 && Buffer[len-1] == '\n')` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (len > 0 && Buffer[len-1] == '\n')`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `if (len > 0 && Buffer[len-1] == '\n')` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `}`

### Step 8: verify_flag函数 (0x401560)

- Route type: `ida-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, z3 with the extracted filter/query `if (strlen(a1) != 16)` and inspect the matching evidence.
- Tools: ida, netcat, z3
- Filters or commands:
  - `if (strlen(a1) != 16)`
  - `if (memcmp(a1, "GCCCTF{", 7) != 0)`
  - `if (a1[15] != '}')`
  - `if (7*v5 + 3*v6 + 11*v7 + 13*v9 != 2145)`
  - `if (8*v6 + 12*v8 + 9*v10 + 4*v12 != 2491)`
  - `if (6*v5 + 5*v7 + 8*v11 + 7*v12 != 2299)`
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, z3 with the extracted filter/query `if (strlen(a1) != 16)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `}`

### Step 9: 建立数学模型

- Route type: `ida-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat, z3
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 所有变量必须是可打印ASCII字符（33-126）`

### Step 10: 编写求解脚本

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `print("=== Constraint Solver ===")` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `print("=== Constraint Solver ===")`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `print("=== Constraint Solver ===")` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print("=== Constraint Solver ===")`

### Step 11: 创建Z3求解器

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use ida, netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: ida, netcat, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use ida, netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `solver.set("timeout", 10000)`

### Step 12: 定义8个整数变量

- Route type: `ida-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: ida, netcat, z3
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b = [Int(f'b{i}') for i in range(8)]`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
