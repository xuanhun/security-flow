# swpuctf2019 Login pwn详细题解_ha1vk的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `swpuctf2019 Login pwn详细题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/swpuctf2019-Login-pwn详细题解_ha1vk的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/swpuctf2019-Login-pwn%E8%AF%A6%E7%BB%86%E9%A2%98%E8%A7%A3_ha1vk%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/swpuctf2019-Login-pwn详细题解_ha1vk的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida
- Techniques: binary-exploitation, encoding-analysis, format-string, ret2libc, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `4`
- `docs/img/d419b5fae92c348520ba532f6b8eb83b.png`
- `docs/img/332cc67c45752e9d08f24ca17f912e43.png`
- `docs/img/eb2c04458035a9fcb42bec46fdee270a.png`
- `docs/img/719f29edff9a7a7409aefeab2823bc52.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: swpuctf2019 Login pwn详细题解_ha1vk的博客-CSDN博客

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use ida to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: ida
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use ida to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/seaaseesa/article/details/103458308](https://blog.csdn.net/seaaseesa/article/details/103458308)`

### Step 3: Login

- Route type: `format-string control path`
- Why: Format-string routes start with stack discovery and end with the smallest precise read or write.
- Probe: Use ida to map readable and writable stack positions before attempting the final primitive.
- Tools: ida
- Reasoning chain:
  - Recognize the section as format-string control path.
  - Use ida to map readable and writable stack positions before attempting the final primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `108.160.139.79`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
