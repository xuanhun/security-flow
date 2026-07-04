# PWN unlink [pwnable.kr]CTF writeup题解系列14（包含本地解决方法）_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `PWN unlink`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-unlink-[pwnable.kr]CTF-writeup题解系列14（包含本地解决方法）_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-unlink-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9714%EF%BC%88%E5%8C%85%E5%90%AB%E6%9C%AC%E5%9C%B0%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95%EF%BC%89_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-unlink-[pwnable.kr]CTF-writeup题解系列14（包含本地解决方法）_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, pwntools
- Techniques: binary-exploitation, service-enumeration, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/488a695b9467eec34dfa008e97f96398.png`
- `docs/img/6b240374b367e15c3b174a881cf2dda7.png`

## Solve Thinking

### Step 1: Document

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN unlink [pwnable.kr]CTF writeup题解系列14（包含本地解决方法）_3riC5r的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `488a695b9467eec34dfa008e97f96398`

### Step 3: gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.11)

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `本机`

### Step 4: gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use gdb, pwntools to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use gdb, pwntools to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `if debug == 1:`

### Step 5: gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `else:`

### Step 6: gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.11)

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 7: payload = p32(elf.symbols['shell']) + '\x00'*12 + p32(ebp-8) + p32(heap_addr+12)

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `估计有很多同学都会看其他wp，发现都是只给出了在pwnable上的解决办法。至于在本机的解决方法在其他人的wp上并没有仔细阐述，所以我这里也是抛砖引玉，和大家分享。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
