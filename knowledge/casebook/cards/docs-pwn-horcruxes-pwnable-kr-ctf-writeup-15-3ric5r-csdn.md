# PWN horcruxes [pwnable.kr]CTF writeup题解系列15_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `PWN horcruxes`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-horcruxes-[pwnable.kr]CTF-writeup题解系列15_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-horcruxes-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9715_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-horcruxes-[pwnable.kr]CTF-writeup题解系列15_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, gdb, netcat, pwntools
- Techniques: binary-exploitation, command-injection, service-enumeration, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/3be4740a196ec8d70a5dad22df3b4ad1.png`
- `docs/img/e6e89864c9c559e2352f5dc7266280dd.png`

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

### Step 2: PWN horcruxes [pwnable.kr]CTF writeup题解系列15_3riC5r的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
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
  - Recognize the section as command execution path.
  - Use checksec, gdb, netcat, pwntools with the extracted filter/query `| \| |__| || \ / || \ | | / _] | |/ ]| \` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `141.85.0.116`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
