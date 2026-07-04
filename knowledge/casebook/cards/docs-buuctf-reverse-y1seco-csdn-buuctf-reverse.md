# [BUUCTF 刷题] Reverse解题方法总结（一）_Y1seco的博客-CSDN博客_buuctf reverse

## Case Metadata

- Category: `Reverse`
- Platform: `BUUCTF 刷题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[BUUCTF-刷题]-Reverse解题方法总结（一）_Y1seco的博客-CSDN博客_buuctf-reverse.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BBUUCTF-%E5%88%B7%E9%A2%98%5D-Reverse%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%E6%80%BB%E7%BB%93%EF%BC%88%E4%B8%80%EF%BC%89_Y1seco%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf-reverse.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[BUUCTF-刷题]-Reverse解题方法总结（一）_Y1seco的博客-CSDN博客_buuctf-reverse.md`

## Why This Case Matters

Use this case as a Reverse reference for apk-mobile, binary, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, binary, ciphertext, pe-malware, web-app
- Tools: dnspy, gdb, ida, netcat, strings
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, http-analysis, malware-static, mobile-forensics, php-tricks, qr-analysis, reverse-engineering, stego-extraction, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `9`
- `docs/img/dceec73f90cf5e868e2959c01a1bb80b.png`
- `docs/img/3965d76ffc66fd8b0b6fda740899f5b8.png`
- `docs/img/cc793b42134f0588824cccb1642672df.png`
- `docs/img/111526c9b221874a0102c4c4ea8265f6.png`
- `docs/img/25242321dacc602e61a13e68fb73e4b9.png`
- `docs/img/6514a74d707ffd2bce166dc2b2491081.png`
- `docs/img/ff747132afb4ec30aa983eb411113db9.png`
- `docs/img/71b3b5be701eab9204bd5d7f5691bb06.png`
- `docs/img/8cf1669d9e37b85940757088ead94685.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: dnspy, gdb, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 前言：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: dnspy, gdb, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `db 3 dup(0,1,2) 指 db 0,1,2,0,1,2,0,1,2`

### Step 3: gdb

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: dnspy, gdb, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `x 指令表示查看寄存器内容，参数/s 表示用字符串形式显示，/w 表示四字节宽，/sw 表示字符串显示，四字节宽`

### Step 4: BUUCTF [BJDCTF2020]easy

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dceec73f90cf5e868e2959c01a1bb80b`

### Step 5: 二 静态分析IDA

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, strings with the extracted filter/query `strings window: 字符串显示窗口，会列出程序中的所有字符串` and inspect the matching evidence.
- Tools: ida, netcat, strings
- Filters or commands:
  - `strings window: 字符串显示窗口，会列出程序中的所有字符串`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, strings with the extracted filter/query `strings window: 字符串显示窗口，会列出程序中的所有字符串` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cc793b42134f0588824cccb1642672df`

### Step 6: 安卓逆向 apk

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, jadx to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, jadx
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, jadx to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `apkide里查看了一下libcore.so文件（C代码写的库文件，一般放在lib文件下。android是基于java的 但也可以调用c代码，so就是），用ida打开，shift+F12查看字符串，找到一串base64编码的字符，解密得到flag`

### Step 7: 算法分析

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if (j < 'A' || j > 'z' || j > 'Z' && j < 'a')` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (j < 'A' || j > 'z' || j > 'Z' && j < 'a')`
  - `if ((j - 39 - key[v3 % 10] + 97) % 26 + 97 == text[i])`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if (j < 'A' || j > 'z' || j > 'Z' && j < 'a')` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `}`

### Step 8: [BUUCTF8086]

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use dnspy, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: dnspy, gdb, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use dnspy, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 9: [ACTF] rome

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use dnspy, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: dnspy, gdb, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use dnspy, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `原文链接：https://blog.csdn.net/mcmuyanga/article/details/110196934`

### Step 10: BUUCTF [BJDCTF2020]easy

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dceec73f90cf5e868e2959c01a1bb80b`

### Step 11: RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `282164587459512124844245113950593348271`

### Step 12: upx

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: dnspy, gdb, ida, netcat, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use dnspy, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `sample_mal.exe`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
