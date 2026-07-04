# shell [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列25_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `shell [XCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/shell-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列25_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/shell-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9725_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/shell-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列25_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ida, netcat, pwntools
- Techniques: binary-exploitation, file-inclusion, integer-overflow, reverse-engineering, stack-overflow

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/bba3b233ceae6f95bc6634a402d099ca.png`
- `docs/img/46d4711675582a9bcd973600faf59725.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: shell [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列25_3riC5r的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat, pwntools with the extracted filter/query `if ( *((_DWORD *)addr_cmd + 4) != 1 || bAuth == 1 )` and inspect the matching evidence.
- Tools: ida, netcat, pwntools
- Filters or commands:
  - `if ( *((_DWORD *)addr_cmd + 4) != 1 || bAuth == 1 )`
  - `if ( bAuth != 1 )`
  - `if (fp == NULL)`
  - `while ((read = getline(&line, &len, fp)) != -1)`
  - `if(p != NULL & p1 != NULL)`
  - `printf("==>%s:%s", p, p1);`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat, pwntools with the extracted filter/query `if ( *((_DWORD *)addr_cmd + 4) != 1 || bAuth == 1 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bba3b233ceae6f95bc6634a402d099ca`

### Step 3: p = process([process_name], env={'LD_LIBRARY_PATH':'./'})

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `111.198.29.45`

### Step 4: pop_rdi_ret = 0x400f33

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ida, netcat, pwntools to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use ida, netcat, pwntools to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.198.29.45`

### Step 5: $ sh

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6ead2b810d6eb8f605a7c153ca1c5044`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
