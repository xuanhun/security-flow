# 【CTF WriteUp】网鼎杯 青龙组 Misc题解复现（整理，WP非原创）_零食商人的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `【CTF WriteUp】网鼎杯 青龙组 Misc题解复现（整理，WP非原创）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF-WriteUp】网鼎杯-青龙组-Misc题解复现（整理，WP非原创）_零食商人的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF-WriteUp%E3%80%91%E7%BD%91%E9%BC%8E%E6%9D%AF-%E9%9D%92%E9%BE%99%E7%BB%84-Misc%E9%A2%98%E8%A7%A3%E5%A4%8D%E7%8E%B0%EF%BC%88%E6%95%B4%E7%90%86%EF%BC%8CWP%E9%9D%9E%E5%8E%9F%E5%88%9B%EF%BC%89_%E9%9B%B6%E9%A3%9F%E5%95%86%E4%BA%BA%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF-WriteUp】网鼎杯-青龙组-Misc题解复现（整理，WP非原创）_零食商人的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, ida, netcat, z3
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, misc-analysis, qr-analysis, reverse-engineering, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `32`
- `docs/img/9789d25b0c0ea84aced8dfceaf7e586b.png`
- `docs/img/1d8ec60a8666ca0cb54ab5877537c6eb.png`
- `docs/img/ff6a4729632c814ee39ebec6a8035094.png`
- `docs/img/7fb93ee1f8784607eb674b2332a66dd0.png`
- `docs/img/576dbaabbab96d8c67884009f3053594.png`
- `docs/img/0bbeb04506bbccb4a773213408b38808.png`
- `docs/img/627d4bfad30679fc59bee70e9d407245.png`
- `docs/img/a4b2bad80756388435f3f3a7126461fb.png`
- `docs/img/16679dae21acae7b63d52bcced4e638d.png`
- `docs/img/4a28945be059acc6d8e657c36843b9fc.png`
- `docs/img/bc1335410be564964acea0d5e7ac3a6c.png`
- `docs/img/35259e534927bfbd22d7693ef9245025.png`
- ... and `20` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF WriteUp】网鼎杯 青龙组 Misc题解复现（整理，WP非原创）_零食商人的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, ida, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, ida, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `（另：求白虎组 Misc-boot 的 WP）`

### Step 3: 虚幻2

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, ida, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, ida, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9789d25b0c0ea84aced8dfceaf7e586b`

### Step 4: Teslaaaaa

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, ida, netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, ida, netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0bbeb04506bbccb4a773213408b38808`

### Step 5: -*- coding: utf-8 -*-

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `tmpdata = []`

### Step 6: Step 1: Remove Rx

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `88fe5a993b8e37e14bad5da30b2b51b7`

### Step 7: 未完成的书

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use burp, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: burp, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use burp, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#!/usr/bin/env python`

### Step 8: -*- coding: utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8ea1efd2c59a9301799651babf1278d6`

### Step 9: 当前已知文字，当前层数，当前剩余矩阵

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `if(level == len(cipher)): # 已全部替换成功` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(level == len(cipher)): # 已全部替换成功`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `if(level == len(cipher)): # 已全部替换成功` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `if(mysha(tmpbase64.encode())==sha265base64):`

### Step 10: LxnWBAlyiXc62kCBHfyEo8woR6oMuk7cKQQN8T75gbbQtZlLBx2AwL4CZ3M/JT5lOg4Fp6y70mle0ZTTgzKr8EUCW8R1D+E7x4AuBI/CsOKm5PWnhpJaUoPDpk9PscMXLQJUGkBsO80/SjggzjvDwxSiTqFjdKPKylKc6F4fKes=

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use burp, ida, netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: burp, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use burp, ida, netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print(hex(tmpm)[2:])`

### Step 11: 222021b2311dfdddbdfdf1df31dc3dddfdbddc3dfdf1df3c3f21df321c3ddf31f1df221f3dfdfdddb2213

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use burp, netcat with the extracted filter/query `if(base64format[level]!='*'): # 触发base64残片限制` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `if(base64format[level]!='*'): # 触发base64残片限制`
  - `if(level == len(flagcheckmode)): # 所有位置已知`
  - `if(flagcheckmode[level:level+2] != '**'): # 确定位`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use burp, netcat with the extracted filter/query `if(base64format[level]!='*'): # 触发base64残片限制` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c8dc548c7f3fc6c3204d78400c3e419a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
