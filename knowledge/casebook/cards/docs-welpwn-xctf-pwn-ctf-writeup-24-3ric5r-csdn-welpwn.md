# welpwn [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列24_3riC5r的博客-CSDN博客_welpwn

## Case Metadata

- Category: `Pwn`
- Platform: `welpwn [XCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/welpwn-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列24_3riC5r的博客-CSDN博客_welpwn.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/welpwn-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9724_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_welpwn.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/welpwn-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列24_3riC5r的博客-CSDN博客_welpwn.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida, pwntools, ropgadget
- Techniques: binary-exploitation, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `4`
- `docs/img/14bfe98f29eea6622b54eefede7a7fe6.png`
- `docs/img/e201459f2ddccff2ff32159f2f107922.png`
- `docs/img/ff7e8b2efadd46b6de062dbe8d8af968.png`
- `docs/img/8bc90461a44e477789961ce2cab85228.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, pwntools, ropgadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, pwntools, ropgadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: welpwn [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列24_3riC5r的博客-CSDN博客_welpwn

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, pwntools, ropgadget with the extracted filter/query `root@mypwn:/ctf/work/python/welpwn# ROPgadget --binary ./a9ad88f80025427592b35612be5492fd --only 'pop|ret'` and inspect the matching evidence.
- Tools: gdb, ida, pwntools, ropgadget
- Filters or commands:
  - `root@mypwn:/ctf/work/python/welpwn# ROPgadget --binary ./a9ad88f80025427592b35612be5492fd --only 'pop|ret'`
  - `============================================================`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, pwntools, ropgadget with the extracted filter/query `root@mypwn:/ctf/work/python/welpwn# ROPgadget --binary ./a9ad88f80025427592b35612be5492fd --only 'pop|ret'` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `14bfe98f29eea6622b54eefede7a7fe6`

### Step 3: p = process([process_name], env={'LD_LIBRARY_PATH':'./'})

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use gdb, ida, pwntools, ropgadget to enumerate processes, network sockets, injected regions, and command lines.
- Tools: gdb, ida, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use gdb, ida, pwntools, ropgadget to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `111.198.29.45`

### Step 4: pause()

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb to collect the smallest evidence slice that answers the goal.
- Tools: gdb
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.198.29.45`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
