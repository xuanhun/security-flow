# PWN collision [pwnable.kr]CTF writeup题解系列2_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `PWN collision`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-collision-[pwnable.kr]CTF-writeup题解系列2_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-collision-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%972_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-collision-[pwnable.kr]CTF-writeup题解系列2_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, pwntools
- Techniques: binary-exploitation, browser-forensics, command-injection, ret2libc, reverse-engineering, service-enumeration, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `1`
- `docs/img/a900ac35f45f044f5c0a4a59cf1efd49.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN collision [pwnable.kr]CTF writeup题解系列2_3riC5r的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use gdb, ida, pwntools with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
- Tools: gdb, ida, pwntools
- Filters or commands:
  - `| \| |__| || \ / || \ | | / _] | |/ ]| \`
  - `| o ) | | || _ || o || o )| | / [_ | ' / | D )`
  - `| _/| | | || | || || || |___ | _] | \ | /`
  - `| | | ` ' || | || _ || O || || [_ __ | \| \`
  - `| | \ / | | || | || || || || || . || . \`
  - `|__| \_/\_/ |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use gdb, ida, pwntools with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `125.238.93.17`

### Step 3: elf = ELF(process_name)

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use pwntools with the extracted filter/query `Python 2.7.12 (default, Nov 12 2018, 14:36:49)` and inspect the matching evidence.
- Tools: pwntools
- Filters or commands:
  - `Python 2.7.12 (default, Nov 12 2018, 14:36:49)`
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Use pwntools with the extracted filter/query `Python 2.7.12 (default, Nov 12 2018, 14:36:49)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `[*] Got EOF while sending in interactive`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
