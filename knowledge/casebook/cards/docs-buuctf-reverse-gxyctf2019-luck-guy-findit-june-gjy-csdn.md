# BUUCTF reverse：[GXYCTF2019]luck_guy,findit,简单注册器题解_June_gjy的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `BUUCTF reverse：[GXYCTF2019]luck`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-reverse：[GXYCTF2019]luck_guy,findit,简单注册器题解_June_gjy的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-reverse%EF%BC%9A%5BGXYCTF2019%5Dluck_guy%2Cfindit%2C%E7%AE%80%E5%8D%95%E6%B3%A8%E5%86%8C%E5%99%A8%E9%A2%98%E8%A7%A3_June_gjy%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-reverse：[GXYCTF2019]luck_guy,findit,简单注册器题解_June_gjy的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for apk-mobile, binary, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, binary, ciphertext, web-app
- Tools: ida, netcat, radare2
- Techniques: classical-crypto, crypto-analysis, http-analysis, integer-overflow, mobile-forensics, qr-analysis, reverse-engineering, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `6`
- `docs/img/21fa588be4a1c09ff527dba5815facd1.png`
- `docs/img/88363cd779a52c593521a5aa4d72097b.png`
- `docs/img/4b49883ece9c73724af84eb2dae09fe5.png`
- `docs/img/3fdaf98e3e2f4f34b357f21ff6dc6b23.png`
- `docs/img/c9270acd25f990f0f62bf6b832a8c8fe.png`
- `docs/img/f43480fd5514f6cbb83d829b4dede9d5.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF reverse：[GXYCTF2019]luck_guy,findit,简单注册器题解_June_gjy的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_50549897/article/details/113523762](https://blog.csdn.net/weixin_50549897/article/details/113523762)`

### Step 3: [GXYCTF2019]luck_guy，简单注册器，题解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题目地址[https://buuoj.cn/challenges](https://buuoj.cn/challenges)`

### Step 4: luck_guy

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida with the extracted filter/query `if ( j % 2 == 1 )` and inspect the matching evidence.
- Tools: ida
- Filters or commands:
  - `if ( j % 2 == 1 )`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida with the extracted filter/query `if ( j % 2 == 1 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `21fa588be4a1c09ff527dba5815facd1`

### Step 5: 简单注册器

- Route type: `ida-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, netcat, radare2 with the extracted filter/query `if (j == 1)` and inspect the matching evidence.
- Tools: ida, netcat, radare2
- Filters or commands:
  - `if (j == 1)`
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, netcat, radare2 with the extracted filter/query `if (j == 1)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dd2940c04462b4dd7c450528835cca15`

### Step 6: findit

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c9270acd25f990f0f62bf6b832a8c8fe`

### Step 7: 本人其它文章链接

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `[逆向迷宫题总结（持续更新） 2020华南师大CTF新生赛maze，攻防世界新手区：NJUPT CTF 2017，BUUCTF：不一样的flag](https://blog.csdn.net/weixin_50549897/article/details/110633105)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
