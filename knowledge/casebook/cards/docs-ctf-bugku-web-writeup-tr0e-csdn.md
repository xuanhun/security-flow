# CTF解题-Bugku_Web_WriteUp (下）_Tr0e的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF解题-Bugku_Web_WriteUp-(下）_Tr0e的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E8%A7%A3%E9%A2%98-Bugku_Web_WriteUp-%28%E4%B8%8B%EF%BC%89_Tr0e%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF解题-Bugku_Web_WriteUp-(下）_Tr0e的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: detect-it-easy, ida, netcat, radare2, sqlmap
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, http-analysis, php-tricks, qr-analysis, reverse-engineering, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `65`
- `docs/img/f50cc276c38e5d9aad3bf0dcf4d4b391.png`
- `docs/img/d10a0d9011a4831fa7e9491057a4a018.png`
- `docs/img/be2f2142c84b7f7f718fabf5acf79572.png`
- `docs/img/7ba170d3e815ae77952dc64fd7157dc1.png`
- `docs/img/a941c6ee3b2099cdde33e148917f88a9.png`
- `docs/img/c184fe8aea5ae7291cc7b53666bac80d.png`
- `docs/img/8bd3c5148cfda168785b849f21db4982.png`
- `docs/img/cbb37f3d6985c1c0db8e5d6e4072ce04.png`
- `docs/img/759dcd4bd3b3a3aa8000b444044fc7b0.png`
- `docs/img/d628df7a83a6a1b91159f6d20c7a5c5a.png`
- `docs/img/4041975aaa1e9d6054c20f9106ebf45e.png`
- `docs/img/0439760271b88055cfba3dfa0959cfb3.png`
- ... and `53` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, ida, netcat, radare2, sqlmap
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use detect-it-easy, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF解题-Bugku_Web_WriteUp (下）_Tr0e的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, ida, netcat, radare2, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, ida, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f50cc276c38e5d9aad3bf0dcf4d4b391`

### Step 3: No.1 Python脚本算数

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 4: No.2 Python提交数据

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 5: No.3 Python爬取数据

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, ida, netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, ida, netcat, radare2, sqlmap
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, ida, netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 6: No.4 Python逆向解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `if ($x == $klen)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if ($x == $klen)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `if ($x == $klen)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c493217bb9477226336e154827a36cf4`

### Step 7: No.5 JS 加密代码审计

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, radare2 with the extracted filter/query `if (c.indexOf(name) == 0) return c.substring(name.length, c.length)` and inspect the matching evidence.
- Tools: ida, netcat, radare2
- Filters or commands:
  - `if (c.indexOf(name) == 0) return c.substring(name.length, c.length)`
  - `enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);`
  - `enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, radare2 with the extracted filter/query `if (c.indexOf(name) == 0) return c.substring(name.length, c.length)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `728a4900c6037def25fd556599b0d2f0`

### Step 8: No.6 sql 注入手工绕过

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:9004`

### Step 9: No.7 Python 时间盲注

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 10: No.8 Python 布尔盲注

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use sqlmap with the extracted filter/query `print "=================================>"` and inspect the matching evidence.
- Tools: sqlmap
- Filters or commands:
  - `print "=================================>"`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use sqlmap with the extracted filter/query `print "=================================>"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8007`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
