# ReeHY-main-100 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列22_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `ReeHY`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/4-ReeHY-main-100-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列22_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/4-ReeHY-main-100-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9722_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/4-ReeHY-main-100-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列22_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: netcat, pwntools
- Techniques: binary-exploitation, integer-overflow, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `1`
- `docs/img/e4fe9b9113c758e45eea7b9befadd094.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ReeHY-main-100 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列22_3riC5r的博客-CSDN博客

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat, pwntools with the extracted filter/query `if ( nInputCun == 1 )` and inspect the matching evidence.
- Tools: netcat, pwntools
- Filters or commands:
  - `if ( nInputCun == 1 )`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat, pwntools with the extracted filter/query `if ( nInputCun == 1 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e4fe9b9113c758e45eea7b9befadd094`

### Step 3: p = process([process_name], env={'LD_LIBRARY_PATH':'./'})

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use netcat, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `111.198.29.45`

### Step 4: p.send(p64(write_addr))

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `本题主要需要注意的知识点是：`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
