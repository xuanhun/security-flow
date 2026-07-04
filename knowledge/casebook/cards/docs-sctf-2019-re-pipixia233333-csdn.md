# SCTF 2019 re部分题解(持续更新中)_pipixia233333的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `SCTF 2019 re部分题解(持续更新中)`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/SCTF-2019-re部分题解(持续更新中)_pipixia233333的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/SCTF-2019-re%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3%28%E6%8C%81%E7%BB%AD%E6%9B%B4%E6%96%B0%E4%B8%AD%29_pipixia233333%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/SCTF-2019-re部分题解(持续更新中)_pipixia233333的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for apk-mobile, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, ciphertext
- Tools: netcat, radare2
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, mobile-forensics

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `13`
- `docs/img/296969eeb4b0e7e3c6559b745065d12d.png`
- `docs/img/eeb460203f9780dbb50f955fa78d0896.png`
- `docs/img/8e1cb6fe109887d2523f08a38c360440.png`
- `docs/img/373ea4e2ed14e7caa0fc58969263b430.png`
- `docs/img/099e39028f98a2f0525b02d86d080b71.png`
- `docs/img/51054fe2bfcd95ae881bd24431d27f32.png`
- `docs/img/b8778b68317efaca3bf749be9fe00797.png`
- `docs/img/692ad4d0fb43a22afb12fcd7886b1d7d.png`
- `docs/img/458b66b35e4c94fce3efb8c825f4798b.png`
- `docs/img/ce470822e4e5fe99339cf89fcc6777d5.png`
- `docs/img/5059169015f8a9104801f18945031269.png`
- `docs/img/71403beac6d8e0232452c8226e11b33b.png`
- ... and `1` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: SCTF 2019 re部分题解(持续更新中)_pipixia233333的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `296969eeb4b0e7e3c6559b745065d12d`

### Step 3: -*- coding:utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `eeb460203f9780dbb50f955fa78d0896`

### Step 4: -*- coding:utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `51054fe2bfcd95ae881bd24431d27f32`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
