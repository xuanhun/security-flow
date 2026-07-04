# 【moeCTF题解-0x04】Crypto_框架主义者的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `【moeCTF题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【moeCTF题解-0x04】Crypto_框架主义者的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90moeCTF%E9%A2%98%E8%A7%A3-0x04%E3%80%91Crypto_%E6%A1%86%E6%9E%B6%E4%B8%BB%E4%B9%89%E8%80%85%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【moeCTF题解-0x04】Crypto_框架主义者的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, siem challenges.

## Input Signals

- Artifacts: binary, ciphertext, siem, web-app
- Tools: elk, ida, netcat, radare2, z3
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, osint, qr-analysis, reverse-engineering, service-enumeration, siem-query, symbolic-execution, web-exploitation, xss

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use elk, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: elk, ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use elk, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【moeCTF题解-0x04】Crypto_框架主义者的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, ida, netcat, radare2 with the extracted filter/query `Python` and inspect the matching evidence.
- Tools: elk, ida, netcat, radare2, z3
- Filters or commands:
  - `Python`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use elk, ida, netcat, radare2 with the extracted filter/query `Python` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 【moeCTF题解-0x04】Crypto

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use elk, ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> **【moeCTF题解】总目录如下：** （若本文图片看不见请访问以下相应的地址）`

### Step 4: Classic Crypto

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use elk, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: elk, ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use elk, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6/6`

### Step 5: 大帝的征程#1

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `*Ps. 可检测字符是否含有字符串来抑制输出*`

### Step 6: 大帝的征程#2

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `输出第一行就是flag：`moectf{c0nquer_th3_un1v3rs3}``

### Step 7: 外面的世界

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `> 因此flag为 `moectf{Rai1F3nc3_3nc2ypT_1s-FunNy~}``

### Step 8: 大帝的征程#3

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use elk, ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: elk, ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use elk, ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `> `>@64E7L4_?BF6C0E9b0)s$trN` 前6位与 `moectf` 做比较，发现差为 `47` 于是编写代码`

### Step 9: 大帝的征程#维吉尼亚

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use elk, netcat with the extracted filter/query `print(chr(j+ord(a))+'|',''.join(str_list))` and inspect the matching evidence.
- Tools: elk, netcat
- Filters or commands:
  - `print(chr(j+ord(a))+'|',''.join(str_list))`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use elk, netcat with the extracted filter/query `print(chr(j+ord(a))+'|',''.join(str_list))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `> 因此flag为 `moectf{s0_whaT_s-N3xt?}``

### Step 10: 大帝的征程#维吉尼亚Ex

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use ida, netcat with the extracted filter/query `print(chr(j+ord(a))+'|',''.join(str_list))` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `print(chr(j+ord(a))+'|',''.join(str_list))`
- Reasoning chain:
  - Recognize the section as xss route.
  - Use ida, netcat with the extracted filter/query `print(chr(j+ord(a))+'|',''.join(str_list))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `vigenerecipher.aspx`

### Step 11: Crypto

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use elk, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: elk, ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use elk, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6/10`

### Step 12: crypto入门指北

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use elk, ida, netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: elk, ida, netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use elk, ida, netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
