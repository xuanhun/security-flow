# PWN mistake [pwnable.kr]CTF writeup题解系列8_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `PWN mistake [pwnable.kr]CTF writeup题解系列8`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-mistake-[pwnable.kr]CTF-writeup题解系列8_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-mistake-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%978_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-mistake-[pwnable.kr]CTF-writeup题解系列8_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: checksec, gdb, ida, netcat, pwntools
- Techniques: binary-exploitation, browser-forensics, command-injection, crypto-analysis, file-inclusion, integer-overflow, ret2libc, reverse-engineering, service-enumeration

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `docs/img/1f7d5c45fca993be37cb65c7b9b2a7b2.png`
- `docs/img/d1bc4094305cc2d74020d6631b3a2cb2.png`
- `docs/img/ee18242a709da4c994a7f5a1e49ba2d2.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN mistake [pwnable.kr]CTF writeup题解系列8_3riC5r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 0x01 题目

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1f7d5c45fca993be37cb65c7b9b2a7b2`

### Step 4: 0x02 解题思路

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use checksec, gdb, ida, netcat with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
- Tools: checksec, gdb, ida, netcat, pwntools
- Filters or commands:
  - `| \| |__| || \ / || \ | | / _] | |/ ]| \`
  - `| o ) | | || _ || o || o )| | / [_ | ' / | D )`
  - `| _/| | | || | || || || |___ | _] | \ | /`
  - `| | | ` ' || | || _ || O || || [_ __ | \| \`
  - `| | \ / | | || | || || || || || . || . \`
  - `|__| \_/\_/ |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use checksec, gdb, ida, netcat with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `182.96.176.177`

### Step 5: 0x03 题解

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
- Tools: gdb
- Filters or commands:
  - `| \| |__| || \ / || \ | | / _] | |/ ]| \`
  - `| o ) | | || _ || o || o )| | / [_ | ' / | D )`
  - `| _/| | | || | || || || |___ | _] | \ | /`
  - `| | | ` ' || | || _ || O || || [_ __ | \| \`
  - `| | \ / | | || | || || || || || . || . \`
  - `|__| \_/\_/ |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.84.12.64`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
