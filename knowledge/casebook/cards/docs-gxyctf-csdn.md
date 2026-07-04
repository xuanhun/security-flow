# GXYCTF部分详细题解_合天网安实验室的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `GXYCTF部分详细题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/GXYCTF部分详细题解_合天网安实验室的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/GXYCTF%E9%83%A8%E5%88%86%E8%AF%A6%E7%BB%86%E9%A2%98%E8%A7%A3_%E5%90%88%E5%A4%A9%E7%BD%91%E5%AE%89%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/GXYCTF部分详细题解_合天网安实验室的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media, web-app, web-service
- Tools: burp, checksec, ida, netcat, pwntools, radare2, z3
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, php-tricks, qr-analysis, ret2libc, reverse-engineering, sql-injection, stack-overflow, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `16`
- `docs/img/998e662aace3a61091ce6cbf9f1d37ce.png`
- `docs/img/858509166e7179ba56e52f6d44105c32.png`
- `docs/img/e7029533d3f22ed4dbd139f9d5fab863.png`
- `docs/img/67f6c0c08721bff882ae2aab5b7cdbe4.png`
- `docs/img/0043dccbbd68ede56e9313d50ce1bb74.png`
- `docs/img/0fde58395524c69e6213a55867e41b53.png`
- `docs/img/cf9abd9a665290ead36f2a1da6ad0d0c.png`
- `docs/img/fa2420c14004bb6a29723682e3931e6a.png`
- `docs/img/a2933b3839e7485a556a5d7618b6f753.png`
- `docs/img/e833c6f27b5fea1311281294ffa8ec10.png`
- `docs/img/0791a03bfab1719995db55f658f4d206.png`
- `docs/img/b6783d13738127d33f1bc45ba3a1813c.png`
- ... and `4` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, checksec, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, checksec, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: GXYCTF部分详细题解_合天网安实验室的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, checksec, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, checksec, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_38154820/article/details/106330179](https://blog.csdn.net/qq_38154820/article/details/106330179)`

### Step 3: 0x00：GXYCTF部分详细题解

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, checksec, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, checksec, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 2019GXYCTF结束，这里我写下较详细的部分题解，希望可以帮到大家！`

### Step 4: 0x01：baby_sqli

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, checksec, ida with the extracted filter/query `c2VsZWN0ICogZnJvbSB1c2VyIHdoZXJlIHVzZXJuYW1lID0gJyRuYW1lJw==` and inspect the matching evidence.
- Tools: burp, checksec, ida
- Filters or commands:
  - `c2VsZWN0ICogZnJvbSB1c2VyIHdoZXJlIHVzZXJuYW1lID0gJyRuYW1lJw==`
  - `if($row['username']=='admin'){`
  - `if($row['password']==md5($pass)){`
  - `passsword字段中的内容要==md5(我们密码栏输入的password)`
  - `0000| buf`
  - `0008|`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, checksec, ida with the extracted filter/query `c2VsZWN0ICogZnJvbSB1c2VyIHdoZXJlIHVzZXJuYW1lID0gJyRuYW1lJw==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 5: 0x06：exp:

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use pwntools with the extracted filter/query `python 跑下便可以拿到flag` and inspect the matching evidence.
- Tools: pwntools
- Filters or commands:
  - `python 跑下便可以拿到flag`
  - `python fantasy.py`
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use pwntools with the extracted filter/query `python 跑下便可以拿到flag` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `183.129.189.60`

### Step 6: 0x07：fu

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use netcat, radare2, z3 with the extracted filter/query `SmUgc3ViaXMsCt==` and inspect the matching evidence.
- Tools: netcat, radare2, z3
- Filters or commands:
  - `SmUgc3ViaXMsCt==`
  - `RWxsZSBtZSBkaXQsCo==`
  - `SmUgdm91ZSBtZXMgbnVpdHMsCm==`
  - `QSBsJ2Fzc2FzeW1waG9uaWUsCl==`
  - `Q2UgcXVlIGplIHNlbWUsCt==`
  - `SmUgdm91ZSBtZXMgbnVpdHMsCp==`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use netcat, radare2, z3 with the extracted filter/query `SmUgc3ViaXMsCt==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a2933b3839e7485a556a5d7618b6f753`

### Step 7: -*- coding: UTF-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, checksec, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, checksec, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `我们对应写出Rot47解题脚本：`

### Step 8: -*- coding: UTF-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, checksec, ida, netcat with the extracted filter/query `dikqTCpfRjA8fUBIMD5GNDkwMjNARkUwI0BFTg==` and inspect the matching evidence.
- Tools: burp, checksec, ida, netcat, pwntools
- Filters or commands:
  - `dikqTCpfRjA8fUBIMD5GNDkwMjNARkUwI0BFTg==`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, checksec, ida, netcat with the extracted filter/query `dikqTCpfRjA8fUBIMD5GNDkwMjNARkUwI0BFTg==` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `带入我们写入的Rot47 解密 Python脚本：`

### Step 9: -*- coding: UTF-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, checksec, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, checksec, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9cba9cac935a369ddff538a4982155e1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
