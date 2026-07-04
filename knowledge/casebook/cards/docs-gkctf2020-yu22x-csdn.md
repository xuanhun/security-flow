# GKCTF2020部分题解_yu22x的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `GKCTF2020部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/GKCTF2020部分题解_yu22x的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/GKCTF2020%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_yu22x%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/GKCTF2020部分题解_yu22x的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media, web-app
- Tools: binwalk, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, image-analysis, misc-analysis, osint, qr-analysis, stego-extraction, waf-bypass, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `18`
- `docs/img/34657caa30c836fba7d3d6ffe88b6d71.png`
- `docs/img/0973ae24eedc98460ac696052d386b0c.png`
- `docs/img/6af6ef1fbd0cad309261d2ab927ac151.png`
- `docs/img/1a69e31ff0d0f9b0c86682af4c5a3ef0.png`
- `docs/img/72c5c9546678a1b7dd366b2086cebbdc.png`
- `docs/img/2f011f7e9b94df148caaace7270e5d91.png`
- `docs/img/06be2bb41c835d7704a5b50f52e9167f.png`
- `docs/img/83b5aaaa7a8c0b8a7f1c52e3851f35c4.png`
- `docs/img/9ac288e46e531396c8fabeef00e8a4be.png`
- `docs/img/8643212bf60f333a472e57da031a24e7.png`
- `docs/img/c36832f3a0c655e85a7478d64287a27e.png`
- `docs/img/0abb8d91c87adf27246dfd5c466ce34a.png`
- ... and `6` more

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

### Step 2: GKCTF2020部分题解_yu22x的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/miuzzx/article/details/106317592](https://blog.csdn.net/miuzzx/article/details/106317592)`

### Step 3: [GKCTF2020]CheckIN

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `那我们直接传 `eval($_POST[1]);`的base64然后蚁剑连接即可(`Ginkgo=ZXZhbCgkX1BPU1RbMV0pOw==`)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `那我们直接传 `eval($_POST[1]);`的base64然后蚁剑连接即可(`Ginkgo=ZXZhbCgkX1BPU1RbMV0pOw==`)`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `那我们直接传 `eval($_POST[1]);`的base64然后蚁剑连接即可(`Ginkgo=ZXZhbCgkX1BPU1RbMV0pOw==`)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `34657caa30c836fba7d3d6ffe88b6d71`

### Step 4: [GKCTF2020]老八小超市儿

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use binwalk, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `72c5c9546678a1b7dd366b2086cebbdc`

### Step 5: [GKCTF2020]cve版签到

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 6: [GKCTF2020]签到

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `访问给的网站就有flag`

### Step 7: [GKCTF2020]问卷调查

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `填完问卷就有flag`

### Step 8: [GKCTF2020]Pokémon

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0abb8d91c87adf27246dfd5c466ce34a`

### Step 9: [GKCTF2020]code obfuscation

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `678670193d3504627162f9033738344e`

### Step 10: [GKCTF2020]小学生的密码学

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use binwalk, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use binwalk, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `13fc200821006f85822aa499884e2334`

### Step 11: [GKCTF2020]汉字的秘密

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `运行得到FLAG{YOU_ARE_GOOD}`

### Step 12: [GKCTF2020]babycrypto

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `转换成16进制再转字符串得到`flag{3d0914a1-1e97-4822-a745-c7e20c5179b9}``

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
