# 【moeCTF题解-0x05】Misc_框架主义者的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `【moeCTF题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【moeCTF题解-0x05】Misc_框架主义者的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90moeCTF%E9%A2%98%E8%A7%A3-0x05%E3%80%91Misc_%E6%A1%86%E6%9E%B6%E4%B8%BB%E4%B9%89%E8%80%85%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【moeCTF题解-0x05】Misc_框架主义者的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, stego-media, web-app challenges.

## Input Signals

- Artifacts: ciphertext, stego-media, web-app
- Tools: binwalk, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, osint, php-tricks, qr-analysis, stego-extraction, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `5`
- `docs/img/7f4b8a6d00f95d3ff6530a585fd26535.png`
- `docs/img/11e2417c0bb0a5ee59bf21525ebd6ceb.png`
- `docs/img/29909ce660948fd9be4aeee7d2960608.png`
- `docs/img/d50deb20a0c86ae5131376496a0e029d.png`
- `docs/img/ea4d97a2537e0a8799afa44da8a6b669.png`

## Solve Thinking

### Step 1: Document

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【moeCTF题解-0x05】Misc_框架主义者的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, netcat with the extracted filter/query `Python` and inspect the matching evidence.
- Tools: binwalk, netcat
- Filters or commands:
  - `Python`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, netcat with the extracted filter/query `Python` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 【moeCTF题解-0x05】Misc

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> **【moeCTF题解】总目录如下：**（若本文图片看不见请访问以下相应的地址）`

### Step 4: Misc

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `13/17`

### Step 5: Welcome

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `> ——XDSEC@EndCat`

### Step 6: MD5

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c4d038b4bed09fdb1471ef51ec3a32cd`

### Step 7: base64

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ``moectf{ez_b64!}``

### Step 8: hey fxck you!

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use binwalk with the extracted filter/query `> | 字符 | 含义 |` and inspect the matching evidence.
- Tools: binwalk
- Filters or commands:
  - `> | 字符 | 含义 |`
  - `> | :-: | :-: |`
  - `> | `>` | 指针加一 |`
  - `> | `<` | 指针减一 |`
  - `> | `+` | 指针指向的字节的值加一 |`
  - `> | `-` | 指针指向的字节的值减一 |`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use binwalk with the extracted filter/query `> | 字符 | 含义 |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `brainfuck.evaluate(sourcecode)`

### Step 9: base64？¿

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `<mark>TODO</mark>`

### Step 10: Pseudo Encryption

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ``moectf{Jus7_c6an9e_@_b1t!}``

### Step 11: 不 会 吧 ？ 就 这 ¿

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk to collect the smallest evidence slice that answers the goal.
- Tools: binwalk
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7f4b8a6d00f95d3ff6530a585fd26535`

### Step 12: Cor1e的支票

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> [Ook!](http://www.dangermouse.net/esoteric/ook.html) 与Brainfuck类似, 但用单词`Ook！`，`Ook.` 和`Ook?`代替。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
