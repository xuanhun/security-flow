# 再不学点现代密码，CTF就Hold不住啦！_合天网安实验室的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `再不学点现代密码，CTF就Hold不住啦！`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/再不学点现代密码，CTF就Hold不住啦！_合天网安实验室的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%86%8D%E4%B8%8D%E5%AD%A6%E7%82%B9%E7%8E%B0%E4%BB%A3%E5%AF%86%E7%A0%81%EF%BC%8CCTF%E5%B0%B1Hold%E4%B8%8D%E4%BD%8F%E5%95%A6%EF%BC%81_%E5%90%88%E5%A4%A9%E7%BD%91%E5%AE%89%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/再不学点现代密码，CTF就Hold不住啦！_合天网安实验室的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: ida, netcat, pwntools
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, http-analysis, php-tricks, qr-analysis, reverse-engineering, waf-bypass, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `40`
- `docs/img/8c457013fa66dac62f09ff7e862862fd.png`
- `docs/img/9ee32053d967d6c6aeaccb9eb8576e8e.png`
- `docs/img/1e2fca5c5f6e831e989e337333f8d0da.png`
- `docs/img/0f9fe858f4867230852ed0e83a867fde.png`
- `docs/img/f8348672e0c91123b190fb44c00ef064.png`
- `docs/img/d1d0efa8373f311d93cf0027acc61a51.png`
- `docs/img/d927944cc5193c481b81c4cdedeed24a.png`
- `docs/img/7036a729c7dd77fec68e09c74543ebef.png`
- `docs/img/ab799a1446b14fd5b1064cf8a262ef0b.png`
- `docs/img/6743f319e296c4b28542cfc8998e3d09.png`
- `docs/img/a057a7685f70f56d342f2ba77b312e8b.png`
- `docs/img/19620e5d628e6fb2f8b9b291af6fcfd3.png`
- ... and `28` more

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

### Step 2: 再不学点现代密码，CTF就Hold不住啦！_合天网安实验室的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8c457013fa66dac62f09ff7e862862fd`

### Step 3: coding:utf-8

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use ida, netcat, pwntools with the extracted filter/query `d*e-1|phi_n` and inspect the matching evidence.
- Tools: ida, netcat, pwntools
- Filters or commands:
  - `d*e-1|phi_n`
  - `pow(x,e,n) == pow(t,e,n)`
  - `重金悬赏 | 合天原创投稿奖励来啦`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use ida, netcat, pwntools with the extracted filter/query `d*e-1|phi_n` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{Do_you_think_change_e_d_means_change_the_key?}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
