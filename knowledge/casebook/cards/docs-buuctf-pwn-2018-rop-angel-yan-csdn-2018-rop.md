# [BUUCTF]PWN——铁人三项(第五赛区)_2018_rop_Angel~Yan的博客-CSDN博客_铁人三项(第五赛区)_2018_rop

## Case Metadata

- Category: `Pwn`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[BUUCTF]PWN——铁人三项(第五赛区)_2018_rop_Angel~Yan的博客-CSDN博客_铁人三项(第五赛区)_2018_rop.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BBUUCTF%5DPWN%E2%80%94%E2%80%94%E9%93%81%E4%BA%BA%E4%B8%89%E9%A1%B9%28%E7%AC%AC%E4%BA%94%E8%B5%9B%E5%8C%BA%29_2018_rop_Angel~Yan%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E9%93%81%E4%BA%BA%E4%B8%89%E9%A1%B9%28%E7%AC%AC%E4%BA%94%E8%B5%9B%E5%8C%BA%29_2018_rop.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[BUUCTF]PWN——铁人三项(第五赛区)_2018_rop_Angel~Yan的博客-CSDN博客_铁人三项(第五赛区)_2018_rop.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, pwntools
- Techniques: binary-exploitation, ret2libc, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/08b023b51f3fc2167085dd2f308cebf8.png`
- `docs/img/a1de8d95ab4c9b09912e0227937fdc96.png`
- `docs/img/830923640e26e418b25ebe5c0fee6445.png`
- `docs/img/866834073b3caed72e5fc9309ca2dbae.png`
- `docs/img/54ee56afdf4e884eb3bba580b9f47b8d.png`

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

### Step 2: [BUUCTF]PWN——铁人三项(第五赛区)_2018_rop_Angel~Yan的博客-CSDN博客_铁人三项(第五赛区)_2018_rop

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/mcmuyanga/article/details/108939218](https://blog.csdn.net/mcmuyanga/article/details/108939218)`

### Step 3: 铁人三项(第五赛区)_2018_rop[32位libc泄露]

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `70baa0a3faa2a7b72be9efd44c04782e`

### Step 4: 利用思路：

- Route type: `ida-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, pwntools to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: 利用过程：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `54ee56afdf4e884eb3bba580b9f47b8d`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
