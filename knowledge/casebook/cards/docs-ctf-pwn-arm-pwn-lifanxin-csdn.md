# CTF pwn -- ARM架构的pwn题详解___lifanxin的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `CTF pwn`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-pwn----ARM架构的pwn题详解___lifanxin的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-pwn----ARM%E6%9E%B6%E6%9E%84%E7%9A%84pwn%E9%A2%98%E8%AF%A6%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-pwn----ARM架构的pwn题详解___lifanxin的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, netcat, pwntools
- Techniques: binary-exploitation, command-injection, ret2libc, reverse-engineering, stack-overflow

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `8`
- `docs/img/ad33bd1f5fc8e45c16663cc240b91256.png`
- `docs/img/746443cbc5027f9d8ea031a56d10b923.png`
- `docs/img/8f8b88f1d8c298705f0ffc00fb2aeb39.png`
- `docs/img/2db0c300c70b3a63608dc7084cfacc5e.png`
- `docs/img/e9c51c9f945b4175787c8a98a2114bdb.png`
- `docs/img/ac7b9ce45db1d927174f9b8d36e94738.png`
- `docs/img/a3d6506c4519beee20ca533dd4415217.png`
- `docs/img/9eb1f68cddcf8656529e17b59b49de96.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF pwn -- ARM架构的pwn题详解___lifanxin的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/116780827](https://blog.csdn.net/A951860555/article/details/116780827)`

### Step 3: 概述

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: 使用QEMU

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, ida, netcat, pwntools with the extracted filter/query `sudo apt search "libc6" | grep arm` and inspect the matching evidence.
- Tools: gdb, ida, netcat, pwntools
- Filters or commands:
  - `sudo apt search "libc6" | grep arm`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, ida, netcat, pwntools with the extracted filter/query `sudo apt search "libc6" | grep arm` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ad33bd1f5fc8e45c16663cc240b91256`

### Step 5: 使用gdb-multiarch

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `746443cbc5027f9d8ea031a56d10b923`

### Step 6: arm32位寄存器介绍

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2db0c300c70b3a63608dc7084cfacc5e`

### Step 7: arm64位寄存器介绍

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e9c51c9f945b4175787c8a98a2114bdb`

### Step 8: 一道例题

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ac7b9ce45db1d927174f9b8d36e94738`

### Step 9: 参考博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[ctf-wiki: arm_rop_zh](https://wiki.x10sec.org/pwn/linux/arm/arm_rop-zh/)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
