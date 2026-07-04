# dice_game [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列12_3riC5r的博客-CSDN博客_dice game

## Case Metadata

- Category: `Pwn`
- Platform: `dice`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/dice_game-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列12_3riC5r的博客-CSDN博客_dice-game.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/dice_game-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9712_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_dice-game.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/dice_game-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列12_3riC5r的博客-CSDN博客_dice-game.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, pwntools
- Techniques: binary-exploitation, integer-overflow, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `3`
- `docs/img/a296bd3f656c37d5992d9912a82a2dd1.png`
- `docs/img/77d62ad98f62d4d7191b3145d8c0859e.png`
- `docs/img/ebb810f8375f9a0e6819cccc2344192e.png`

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: dice_game [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列12_3riC5r的博客-CSDN博客_dice game

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, pwntools with the extracted filter/query `if ( nResultGame != 1 )` and inspect the matching evidence.
- Tools: checksec, pwntools
- Filters or commands:
  - `if ( nResultGame != 1 )`
  - `if ( nRound == 50 )`
  - `if ( nInputPoint <= 0 || nInputPoint > 6 || nRandPoint <= 0 || nRandPoint > 6 )`
  - `if ( nInputPoint == nRandPoint )`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, pwntools with the extracted filter/query `if ( nResultGame != 1 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a296bd3f656c37d5992d9912a82a2dd1`

### Step 3: elf = ELF(process_name)

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use checksec, pwntools to enumerate processes, network sockets, injected regions, and command lines.
- Tools: checksec, pwntools
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use checksec, pwntools to enumerate processes, network sockets, injected regions, and command lines.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.198.29.45`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
