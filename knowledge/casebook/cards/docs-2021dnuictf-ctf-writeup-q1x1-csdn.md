# 2021DNUICTF（东软杯CTF）的几个签到题writeup_Q1X1的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `2021DNUICTF（东软杯CTF）的几个签到题writeup`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2021DNUICTF（东软杯CTF）的几个签到题writeup_Q1X1的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2021DNUICTF%EF%BC%88%E4%B8%9C%E8%BD%AF%E6%9D%AFCTF%EF%BC%89%E7%9A%84%E5%87%A0%E4%B8%AA%E7%AD%BE%E5%88%B0%E9%A2%98writeup_Q1X1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2021DNUICTF（东软杯CTF）的几个签到题writeup_Q1X1的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: not detected
- Techniques: binary-exploitation, crypto-analysis, encoding-analysis, misc-analysis, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `5`
- `docs/img/f325c2d9b106b1a90e0eb2e47a21ff5a.png`
- `docs/img/61d42727208040e56ff18bc7d0f47fc5.png`
- `docs/img/1e55b90a67f40f2a1e993ad156f02f30.png`
- `docs/img/e02cc6831287cc4309a89347dbe0b05a.png`
- `docs/img/674764b900d8e39fdaa48ba86df53a17.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2021DNUICTF（东软杯CTF）的几个签到题writeup_Q1X1的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_54430466/article/details/121771286](https://blog.csdn.net/weixin_54430466/article/details/121771286)`

### Step 3: WEB

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f325c2d9b106b1a90e0eb2e47a21ff5a`

### Step 4: MISC

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `61d42727208040e56ff18bc7d0f47fc5`

### Step 5: REVERSE

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1e55b90a67f40f2a1e993ad156f02f30`

### Step 6: CRYPTO

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e02cc6831287cc4309a89347dbe0b05a`

### Step 7: PWN

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `674764b900d8e39fdaa48ba86df53a17`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
