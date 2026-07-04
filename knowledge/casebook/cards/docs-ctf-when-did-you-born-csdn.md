# CTF|入门题目when_did_you_born解题思路以个人总结_一个不融化的雪人的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `CTF|入门题目when`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF｜入门题目when_did_you_born解题思路以个人总结_一个不融化的雪人的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%EF%BD%9C%E5%85%A5%E9%97%A8%E9%A2%98%E7%9B%AEwhen_did_you_born%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E4%BB%A5%E4%B8%AA%E4%BA%BA%E6%80%BB%E7%BB%93_%E4%B8%80%E4%B8%AA%E4%B8%8D%E8%9E%8D%E5%8C%96%E7%9A%84%E9%9B%AA%E4%BA%BA%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF｜入门题目when_did_you_born解题思路以个人总结_一个不融化的雪人的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, pwntools
- Techniques: binary-exploitation, image-analysis, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/403c0f596bb7bddb06f5ef3160c86b07.png`
- `docs/img/2c87f1b6e48a1f36ba746504f2aff952.png`
- `docs/img/76301f06beba9e0f4dd9446cb13c0ce2.png`
- `docs/img/1d92a249f026dad1d641c613f8a2ee43.png`
- `docs/img/5ade1e6aff7f8f4585e4af6068ba0b75.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF|入门题目when_did_you_born解题思路以个人总结_一个不融化的雪人的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/skyattractive/article/details/106461710](https://blog.csdn.net/skyattractive/article/details/106461710)`

### Step 3: 解题思路

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `124.126.19.106`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
