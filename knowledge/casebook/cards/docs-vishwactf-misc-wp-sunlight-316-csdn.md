# 【vishwaCTF】misc题解wp_Sunlight_316的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `【vishwaCTF】misc题解wp`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【vishwaCTF】misc题解wp_Sunlight_316的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90vishwaCTF%E3%80%91misc%E9%A2%98%E8%A7%A3wp_Sunlight_316%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【vishwaCTF】misc题解wp_Sunlight_316的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media, web-app
- Tools: binwalk, ida, strings
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, malware-static, misc-analysis, network-forensics, qr-analysis, reverse-engineering, stego-extraction, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `15`
- `docs/img/f956bf0e7ce59e2fe358f77a4617e261.png`
- `docs/img/ce3e28befe972e521cbf57c020aa8eef.png`
- `docs/img/e32b28ad89c74f87e4a981f53480baf4.png`
- `docs/img/78a112ddafda046848eaeeab53757c48.png`
- `docs/img/5466b3ab337e654d8fb5da658a718846.png`
- `docs/img/b0fae81725ee2556c1fb8f3217dd5c41.png`
- `docs/img/0e83262053a7a02841fb424a62cb6fd2.png`
- `docs/img/9e80a44b1de0a1796922e0b2d97911b5.png`
- `docs/img/9d1cd37e0171bec9c839b3b45c12b599.png`
- `docs/img/ac627d0e80c05357a9f3a7a900d27e5b.png`
- `docs/img/8f1484656f42c1ec913e2a201a7a9eeb.png`
- `docs/img/f6a5e567291cfd35d02697583fedd40e.png`
- ... and `3` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, ida, strings
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, ida, strings to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【vishwaCTF】misc题解wp_Sunlight_316的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, ida, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, ida, strings
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, ida, strings to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_51614272/article/details/124131315](https://blog.csdn.net/weixin_51614272/article/details/124131315)`

### Step 3: Epistemus（信息检索、Twitter 隐写和cat命令）

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, ida, strings with the extracted filter/query `cat something_in_the_way/* | grep {` and inspect the matching evidence.
- Tools: binwalk, ida, strings
- Filters or commands:
  - `cat something_in_the_way/* | grep {`
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, ida, strings with the extracted filter/query `cat something_in_the_way/* | grep {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `{th1ng$_a43_n0t_wh4t_th3y_4lw4y$_$33m}`

### Step 4: So Forgetful!（流量包）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, ida, strings to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, ida, strings
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, ida, strings to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5466b3ab337e654d8fb5da658a718846`

### Step 5: The Last Jedi（binwalk和信息检索）

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, ida, strings to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, ida, strings
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, ida, strings to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b0fae81725ee2556c1fb8f3217dd5c41`

### Step 6: Keep the flag high（文件头和rot47）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, strings to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, strings
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, strings to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9e80a44b1de0a1796922e0b2d97911b5`

### Step 7: Garfeld?（Audacity和维吉尼亚加密）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, ida, strings to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, ida, strings
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, ida, strings to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f6a5e567291cfd35d02697583fedd40e`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
