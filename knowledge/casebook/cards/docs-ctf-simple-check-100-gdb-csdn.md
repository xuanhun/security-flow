# [CTF]攻防世界Simple-check-100题解（GDB）_拈花倾城的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[CTF]攻防世界Simple-check-100题解（GDB）_拈花倾城的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BCTF%5D%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8CSimple-check-100%E9%A2%98%E8%A7%A3%EF%BC%88GDB%EF%BC%89_%E6%8B%88%E8%8A%B1%E5%80%BE%E5%9F%8E%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[CTF]攻防世界Simple-check-100题解（GDB）_拈花倾城的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, netcat
- Techniques: crypto-analysis, integer-overflow, misc-analysis, reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `5`
- `docs/img/e40cff2d372e7b58c820850d5db51fad.png`
- `docs/img/e9d26104e19abbe2af1cfd5cae8c9798.png`
- `docs/img/7c8f7d2cc67f65a638cbb948a29b0ed1.png`
- `docs/img/a6db7a90f936f2b6103257e8dcda5762.png`
- `docs/img/09fb9a3985715157376b380d882cc158.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: [CTF]攻防世界Simple-check-100题解（GDB）_拈花倾城的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/m0_46363249/article/details/113585464](https://blog.csdn.net/m0_46363249/article/details/113585464)`

### Step 3: 关于GDB的简单使用

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb with the extracted filter/query `GDB**的实现原理：[其他师傅的文章，很详细](https://blog.csdn.net/z_stand/article/details/108395906)` and inspect the matching evidence.
- Tools: gdb
- Filters or commands:
  - `GDB**的实现原理：[其他师傅的文章，很详细](https://blog.csdn.net/z_stand/article/details/108395906)`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb with the extracted filter/query `GDB**的实现原理：[其他师傅的文章，很详细](https://blog.csdn.net/z_stand/article/details/108395906)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `**GDB**的实现原理：[其他师傅的文章，很详细](https://blog.csdn.net/z_stand/article/details/108395906)`

### Step 4: step 1 获取信息

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e40cff2d372e7b58c820850d5db51fad`

### Step 5: step 2 放入IDA分析一下

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use gdb, netcat to verify the numeric edge case and how it changes the downstream size or bounds check.
- Tools: gdb, netcat
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use gdb, netcat to verify the numeric edge case and how it changes the downstream size or bounds check.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `我们可以得出check_key是核心函数，只要使得`if ( (unsigned int)check_key(v36) )`成功即可。这样我们就可以进入GDB进行调试了。`

### Step 6: step 3 进入GDB进行动态调试

- Route type: `gdb-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb with the extracted filter/query `gdb` and inspect the matching evidence.
- Tools: gdb
- Filters or commands:
  - `gdb`
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb with the extracted filter/query `gdb` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e9d26104e19abbe2af1cfd5cae8c9798`

### Step 7: step 4 跳过check_key函数

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `09fb9a3985715157376b380d882cc158`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
