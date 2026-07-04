# boston-key-party-2016-pwn-simple_calc 题解___lifanxin的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `boston`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/boston-key-party-2016-pwn-simple_calc-题解___lifanxin的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/boston-key-party-2016-pwn-simple_calc-%E9%A2%98%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/boston-key-party-2016-pwn-simple_calc-题解___lifanxin的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, pwntools, ropgadget
- Techniques: binary-exploitation, crypto-analysis, ret2libc, reverse-engineering

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/539c01bd6c53fd549ab63d962b308aa2.png`
- `docs/img/dcebafdad8b4382241b48d20e1ae5459.png`
- `docs/img/85b3fc3f1b8bdcbf5e65fcc69888e61d.png`
- `docs/img/621fab412b6b3c346258b29323bd2d4e.png`
- `docs/img/9ce6bc5fd1851b5c018f57f926791cee.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, pwntools, ropgadget to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, pwntools, ropgadget to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: boston-key-party-2016-pwn-simple_calc 题解___lifanxin的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, pwntools, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, pwntools, ropgadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, pwntools, ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/113841290](https://blog.csdn.net/A951860555/article/details/113841290)`

### Step 3: 文件信息

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `539c01bd6c53fd549ab63d962b308aa2`

### Step 4: 漏洞定位

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `dcebafdad8b4382241b48d20e1ae5459`

### Step 5: 利用分析

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ropgadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ropgadget to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 6: wp

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use pwntools to align timestamps and identify the event that satisfies the question.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use pwntools to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
