# ctf逆向解题——re1_FunkyPants的博客-CSDN博客_ctf逆向题

## Case Metadata

- Category: `Reverse`
- Platform: `ctf逆向解题——re1`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf逆向解题——re1_FunkyPants的博客-CSDN博客_ctf逆向题.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf%E9%80%86%E5%90%91%E8%A7%A3%E9%A2%98%E2%80%94%E2%80%94re1_FunkyPants%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E9%80%86%E5%90%91%E9%A2%98.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf逆向解题——re1_FunkyPants的博客-CSDN博客_ctf逆向题.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, strings
- Techniques: encoding-analysis, malware-static, reverse-engineering, stego-extraction

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `8`
- `docs/img/dab24d1cfc630bd2ca8ff86c76fc5dfb.png`
- `docs/img/4416d0f3127afb661054f94e4ff2d31d.png`
- `docs/img/6f55ddda4de65987ee99a16e29610a54.png`
- `docs/img/1dc90be8a7fa712a21d16d1f499211e3.png`
- `docs/img/f0ffbc32d6ba739e83b2ee4de18dc459.png`
- `docs/img/b170559a454bc60a4796a719865e00d9.png`
- `docs/img/8986b8a63c1e8581451b9091099922a2.png`
- `docs/img/d802a56cc8e3d9988e1273264a13f22e.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf逆向解题——re1_FunkyPants的博客-CSDN博客_ctf逆向题

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/FunkyPants/article/details/96843483](https://blog.csdn.net/FunkyPants/article/details/96843483)`

### Step 3: 题目概述

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `链接: [https://pan.baidu.com/s/1ns8LiGSODII313skD1Mi4w](https://pan.baidu.com/s/1ns8LiGSODII313skD1Mi4w) 提取码: m43u`

### Step 4: 题目知识点

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 5: 做题环境

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida with the extracted filter/query `gdb` and inspect the matching evidence.
- Tools: gdb, ida
- Filters or commands:
  - `gdb`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida with the extracted filter/query `gdb` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* gdb`

### Step 6: 脱壳

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `dab24d1cfc630bd2ca8ff86c76fc5dfb`

### Step 7: 1 初步观察

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4416d0f3127afb661054f94e4ff2d31d`

### Step 8: 1 part1

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e95db923472c203d738db1287dc1d69f`

### Step 9: 2 part2

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e74cd4c0f757c202294906c8127f7403`

### Step 10: 3 part3

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6f55ddda4de65987ee99a16e29610a54`

### Step 11: 1 part1

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1dc90be8a7fa712a21d16d1f499211e3`

### Step 12: 2 part2

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, strings with the extracted filter/query `output1 = 4*i & 0x1c | i1 >> 6` and inspect the matching evidence.
- Tools: gdb, ida, strings
- Filters or commands:
  - `output1 = 4*i & 0x1c | i1 >> 6`
  - `000678000 | 0000 0012 -> 0006 7812`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, strings with the extracted filter/query `output1 = 4*i & 0x1c | i1 >> 6` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f0ffbc32d6ba739e83b2ee4de18dc459`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
