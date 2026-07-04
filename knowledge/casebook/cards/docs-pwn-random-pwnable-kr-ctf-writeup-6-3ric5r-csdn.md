# PWN random [pwnable.kr]CTF writeup题解系列6_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `PWN random [pwnable.kr]CTF writeup题解系列6`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-random-[pwnable.kr]CTF-writeup题解系列6_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-random-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%976_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-random-[pwnable.kr]CTF-writeup题解系列6_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: checksec, gdb, netcat, pwntools
- Techniques: binary-exploitation, browser-forensics, command-injection, crypto-analysis, file-inclusion, image-analysis, integer-overflow, ret2libc, service-enumeration, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `docs/img/b0210234d3cd344a7f41688468afccfb.png`
- `docs/img/8af16a319705c476e1a5f04a5bc17bf8.png`
- `docs/img/1ae7cb3e46d3f7feefa595198e5edaed.png`

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN random [pwnable.kr]CTF writeup题解系列6_3riC5r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 0x01 题目

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, gdb, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b0210234d3cd344a7f41688468afccfb`

### Step 4: 0x02 解题思路

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use checksec, gdb, netcat, pwntools with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
- Tools: checksec, gdb, netcat, pwntools
- Filters or commands:
  - `| \| |__| || \ / || \ | | / _] | |/ ]| \`
  - `| o ) | | || _ || o || o )| | / [_ | ' / | D )`
  - `| _/| | | || | || || || |___ | _] | \ | /`
  - `| | | ` ' || | || _ || O || || [_ __ | \| \`
  - `| | \ / | | || | || || || || || . || . \`
  - `|__| \_/\_/ |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use checksec, gdb, netcat, pwntools with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `220.127.44.200`

### Step 5: 0x03 题解

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p = process(process_name)`

### Step 6: elf = ELF(process_name)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use checksec, gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: checksec, gdb, netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use checksec, gdb, netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `libc = cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc-2.23.so')`

### Step 7: libc.srand(1)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools with the extracted filter/query `Python 2.7.12 (default, Nov 12 2018, 14:36:49)` and inspect the matching evidence.
- Tools: pwntools
- Filters or commands:
  - `Python 2.7.12 (default, Nov 12 2018, 14:36:49)`
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools with the extracted filter/query `Python 2.7.12 (default, Nov 12 2018, 14:36:49)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1ae7cb3e46d3f7feefa595198e5edaed`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
