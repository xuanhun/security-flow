# play [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列26（超详细分析）_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `play [XCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/play-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列26（超详细分析）_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/play-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9726%EF%BC%88%E8%B6%85%E8%AF%A6%E7%BB%86%E5%88%86%E6%9E%90%EF%BC%89_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/play-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列26（超详细分析）_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-service challenges.

## Input Signals

- Artifacts: binary, web-service
- Tools: netcat, nmap
- Techniques: binary-exploitation, integer-overflow, service-enumeration, stack-overflow

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `1`
- `docs/img/5b2832c93a7fb6da33f6684300572d18.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, nmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, nmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: play [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列26（超详细分析）_3riC5r的博客-CSDN博客

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use netcat, nmap with the extracted filter/query `if ( nChoice != 2 )` and inspect the matching evidence.
- Tools: netcat, nmap
- Filters or commands:
  - `if ( nChoice != 2 )`
  - `if ( nChoice == 3 )`
  - `if ( nChoice == 4 )`
  - `if ( nChoice != 1 )`
  - `if ( access(g_tmp_db_dir, 0) && mkdir(g_tmp_db_dir, 0x1EDu) == -1 )`
  - `if ( gMonster->pMonsterSkillType->dwHidenPlusNum && gMonster->m2 > 4 && rand() % 3 == 1 )`
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use netcat, nmap with the extracted filter/query `if ( nChoice != 2 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5b2832c93a7fb6da33f6684300572d18`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
