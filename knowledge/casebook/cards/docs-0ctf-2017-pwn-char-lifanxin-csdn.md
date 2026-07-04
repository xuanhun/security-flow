# 0ctf-2017-pwn-char 题解___lifanxin的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `0ctf`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/0ctf-2017-pwn-char-题解___lifanxin的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/0ctf-2017-pwn-char-%E9%A2%98%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/0ctf-2017-pwn-char-题解___lifanxin的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, netcat, pwntools
- Techniques: binary-exploitation, ret2libc, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/f6bbb5abe6e3e084d78458730b223d8f.png`
- `docs/img/c86e0b57456c700c89fec0919d272fcd.png`
- `docs/img/897b119af647be2e364b0c37f044787b.png`
- `docs/img/0073c11ac063862a872bce22762d7bde.png`
- `docs/img/8413da72d7b6e12fe3fd1bf666f0228d.png`

## Solve Thinking

### Step 1: Document

- Route type: `checksec-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use checksec, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: checksec, netcat, pwntools
- Reasoning chain:
  - Recognize the section as checksec-driven evidence lookup.
  - Use checksec, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 0ctf-2017-pwn-char 题解___lifanxin的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/113666423](https://blog.csdn.net/A951860555/article/details/113666423)`

### Step 3: 文件信息

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f6bbb5abe6e3e084d78458730b223d8f`

### Step 4: 漏洞定位

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c86e0b57456c700c89fec0919d272fcd`

### Step 5: 利用分析

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `8413da72d7b6e12fe3fd1bf666f0228d`

### Step 6: wp

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `p.interactive()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
