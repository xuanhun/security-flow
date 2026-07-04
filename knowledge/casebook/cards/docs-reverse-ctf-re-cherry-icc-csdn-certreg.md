# 软件逆向分析初试reverse；ctf-re 入门题，详解_Cherry_icc的博客-CSDN博客_certreg是什么程序

## Case Metadata

- Category: `Reverse`
- Platform: `软件逆向分析初试reverse；ctf`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/软件逆向分析初试reverse；ctf-re-入门题，详解_Cherry_icc的博客-CSDN博客_certreg是什么程序.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E8%BD%AF%E4%BB%B6%E9%80%86%E5%90%91%E5%88%86%E6%9E%90%E5%88%9D%E8%AF%95reverse%EF%BC%9Bctf-re-%E5%85%A5%E9%97%A8%E9%A2%98%EF%BC%8C%E8%AF%A6%E8%A7%A3_Cherry_icc%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_certreg%E6%98%AF%E4%BB%80%E4%B9%88%E7%A8%8B%E5%BA%8F.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/软件逆向分析初试reverse；ctf-re-入门题，详解_Cherry_icc的博客-CSDN博客_certreg是什么程序.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ghidra, ida
- Techniques: osint, reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `9`
- `docs/img/5a22591b759241f91e250d8e17e51173.png`
- `docs/img/12269117610227bfba7537f3ba5aac84.png`
- `docs/img/2465c8b0b74c515eb4eb3cafd74d5b62.png`
- `docs/img/08ff6df1b190e745e14c5519d584db9f.png`
- `docs/img/704a82f004d9d4f0dd189fc7698b6693.png`
- `docs/img/ad80c84c0cc92118e0d2bad586581c97.png`
- `docs/img/cfc1879cc8ad7502bb1e5e61f4ca49e3.png`
- `docs/img/1cdcf55fb7afeabf7eeeb36a1e1c7c42.png`
- `docs/img/5e3f6c6c185ffe2c9833dfcf71432d19.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ghidra, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 软件逆向分析初试reverse；ctf-re 入门题，详解_Cherry_icc的博客-CSDN博客_certreg是什么程序

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ghidra, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ghidra, ida
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ghidra, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/CHERRY_cong/article/details/116333941](https://blog.csdn.net/CHERRY_cong/article/details/116333941)`

### Step 3: 软件逆向分析初试re；ctf

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ghidra, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `实验内容：reverseme；文件链接[https://gitee.com/cherry_ccl/homework_code](https://gitee.com/cherry_ccl/homework_code)`

### Step 4: 程序逻辑分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ghidra to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ghidra
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ghidra to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5a22591b759241f91e250d8e17e51173`

### Step 5: Game1

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ghidra to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ghidra
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ghidra to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `12269117610227bfba7537f3ba5aac84`

### Step 6: Game2

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ghidra, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2465c8b0b74c515eb4eb3cafd74d5b62`

### Step 7: Game3

- Route type: `gdb-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb to collect the smallest evidence slice that answers the goal.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `704a82f004d9d4f0dd189fc7698b6693`

### Step 8: 程序运行结果

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ghidra, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ghidra, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5e3f6c6c185ffe2c9833dfcf71432d19`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
