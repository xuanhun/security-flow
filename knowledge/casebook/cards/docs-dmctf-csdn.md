# DMCTF校赛思路总结_烦躁的程序员的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `DMCTF校赛思路总结`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/DMCTF校赛思路总结_烦躁的程序员的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/DMCTF%E6%A0%A1%E8%B5%9B%E6%80%9D%E8%B7%AF%E6%80%BB%E7%BB%93_%E7%83%A6%E8%BA%81%E7%9A%84%E7%A8%8B%E5%BA%8F%E5%91%98%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/DMCTF校赛思路总结_烦躁的程序员的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, disk-image challenges.

## Input Signals

- Artifacts: binary, ciphertext, disk-image, stego-media, web-app
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, image-analysis, misc-analysis, php-tricks, qr-analysis, reverse-engineering, stego-extraction, timeline-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `24`
- `docs/img/30b79e64aa89a9875ca3ff7c5bc2f92c.png`
- `docs/img/78ef07e2a4cbb12d03b2e0b061538d59.png`
- `docs/img/2c2cb24880bbbb082df0817233bf803d.png`
- `docs/img/5418be69043df8b8091812ffdea658ac.png`
- `docs/img/4f243e7136e1f9c3ef710a51a9841cd0.png`
- `docs/img/79a20076573a20901392ad4e4b24309a.png`
- `docs/img/5220fa17e7a7a8380ac6bed3c9dfe916.png`
- `docs/img/2dfb9266c5dfc38ce83a640197132b99.png`
- `docs/img/8c8f2dfe4ff0cf382d89c13607f18cd0.png`
- `docs/img/5cd252cdaf6849d1fdcd819aeab79c79.png`
- `docs/img/1f2420968b38bc32448e7322ff305b93.png`
- `docs/img/4e381ef7f1e9aaa089bd70c6fcd3aa55.png`
- ... and `12` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: Weak_type：

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use cyberchef, detect-it-easy, ida, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.
- Evidence rule: The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.

### Step 3: THINKPHP：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: SimpleQrcode：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use cyberchef, detect-it-easy, ida, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `​ 把 GIF 上传到一个在线分解 GIF 的网站，然后一个一个扫二维码`

### Step 5: 签到题：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `​ 直接复制粘贴`

### Step 6: Fazezip：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `​ 百度了一下 faze 的意思发现是伪装，然后按照一个杂项笔记，找到了 一个伪加密攻击软件，然后取得 flag。`

### Step 7: Base family：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `​ 就是根据密文特征然后在 base 的在线解码网站不断破解，最后取得 flag。`

### Step 8: 编码之王：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `​ 就是根据编码特点不断在在线网站解密。`

### Step 9: ARCHPR：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use cyberchef, detect-it-easy, ida, netcat to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 10: Outguess：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 11: Steghide：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef, detect-it-easy, ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 12: SSTV：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: cyberchef, detect-it-easy, ida, netcat, steghide
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use cyberchef, detect-it-easy, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `以上则为校赛做出的题的一些思路。(第一次写思路总结，当时没有及时记录，导致写的过于简单。)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
