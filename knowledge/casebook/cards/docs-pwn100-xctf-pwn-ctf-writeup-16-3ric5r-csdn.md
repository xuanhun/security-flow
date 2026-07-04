# pwn100 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列16_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `pwn100 [XCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/pwn100-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列16_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/pwn100-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9716_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/pwn100-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列16_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, ida, netcat, pwntools, ropgadget
- Techniques: binary-exploitation, command-injection, integer-overflow, ret2libc, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `1`
- `docs/img/73ead50b24afe3f0672e6d2bbf2197ed.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: pwn100 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列16_3riC5r的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, ida, pwntools, ropgadget with the extracted filter/query `root@mypwn:/ctf/work/python/pwn-100# ROPgadget --binary d0b5f9b486bb480c9035839ec896252e --only "pop|ret" | grep rdi` and inspect the matching evidence.
- Tools: checksec, ida, pwntools, ropgadget
- Filters or commands:
  - `root@mypwn:/ctf/work/python/pwn-100# ROPgadget --binary d0b5f9b486bb480c9035839ec896252e --only "pop|ret" | grep rdi`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, ida, pwntools, ropgadget with the extracted filter/query `root@mypwn:/ctf/work/python/pwn-100# ROPgadget --binary d0b5f9b486bb480c9035839ec896252e --only "pop|ret" | grep rdi` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `73ead50b24afe3f0672e6d2bbf2197ed`

### Step 3: context.log_level = 'debug'

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d0b5f9b486bb480c9035839ec896252e`

### Step 4: p = process(process_name)

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.198.29.45`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
