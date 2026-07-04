# 2019 D^3CTF unprintableV详细题解_ha1vk的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `2019 D^3CTF unprintableV详细题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2019-D^3CTF-unprintableV详细题解_ha1vk的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2019-D%5E3CTF-unprintableV%E8%AF%A6%E7%BB%86%E9%A2%98%E8%A7%A3_ha1vk%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2019-D^3CTF-unprintableV详细题解_ha1vk的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ida, netcat, ropgadget
- Techniques: binary-exploitation, encoding-analysis, file-inclusion, format-string, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `16`
- `docs/img/03e60c49d4b970d16be4ded35de48e89.png`
- `docs/img/6f64321454ee83059cfc9d6caeefd133.png`
- `docs/img/2644d0856fe6f5f28c13e3b692049fb2.png`
- `docs/img/c078996b6d39358ac6aacde51682a320.png`
- `docs/img/b12d7d0aa71e1df02d291776fc7826cf.png`
- `docs/img/f06da26b3c5cd3cccfac39da1d1aaaad.png`
- `docs/img/aa83745d59d0724d33b83c56a5662098.png`
- `docs/img/5fa0575cb1d51b8b3a22d59cf8cf10d1.png`
- `docs/img/6501c2c480b92bff014792da1a7c7615.png`
- `docs/img/a183e259e42ed549e49e9fd78a0bb424.png`
- `docs/img/e6e87087ce456786d291dc76f9bb9a1c.png`
- `docs/img/fdb1bd4bd874bbea22d1bb40933c9dcb.png`
- ... and `4` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, ropgadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, ropgadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, ropgadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2019 D^3CTF unprintableV详细题解_ha1vk的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, ropgadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/seaaseesa/article/details/103323810](https://blog.csdn.net/seaaseesa/article/details/103323810)`

### Step 3: unprintableV

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat, ropgadget with the extracted filter/query `ROPgadget --binary libc.so.6 --only 'pop|ret' | grep 'rdx'` and inspect the matching evidence.
- Tools: ida, netcat, ropgadget
- Filters or commands:
  - `ROPgadget --binary libc.so.6 --only 'pop|ret' | grep 'rdx'`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat, ropgadget with the extracted filter/query `ROPgadget --binary libc.so.6 --only 'pop|ret' | grep 'rdx'` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `03e60c49d4b970d16be4ded35de48e89`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
