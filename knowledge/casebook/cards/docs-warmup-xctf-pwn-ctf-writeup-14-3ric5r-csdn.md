# warmup [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列14_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `warmup [XCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/warmup-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列14_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/warmup-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9714_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/warmup-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列14_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: netcat, pwntools
- Techniques: binary-exploitation, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `1`
- `docs/img/d84c17827d344c3b7f77e7b89075c757.png`

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

### Step 2: warmup [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列14_3riC5r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `111.198.29.45`

### Step 3: context.log_level = 'debug'

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.198.29.45`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
