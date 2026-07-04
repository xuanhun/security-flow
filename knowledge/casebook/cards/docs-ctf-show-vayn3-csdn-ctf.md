# CTF show 萌新区解题报告 （一）_Vayn3的博客-CSDN博客_ctf解题报告

## Case Metadata

- Category: `Crypto`
- Platform: `CTF show 萌新区解题报告 （一）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-show-萌新区解题报告-（一）_Vayn3的博客-CSDN博客_ctf解题报告.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-show-%E8%90%8C%E6%96%B0%E5%8C%BA%E8%A7%A3%E9%A2%98%E6%8A%A5%E5%91%8A-%EF%BC%88%E4%B8%80%EF%BC%89_Vayn3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E8%A7%A3%E9%A2%98%E6%8A%A5%E5%91%8A.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-show-萌新区解题报告-（一）_Vayn3的博客-CSDN博客_ctf解题报告.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, stego-media, web-app challenges.

## Input Signals

- Artifacts: ciphertext, stego-media, web-app, web-service
- Tools: burp
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, image-analysis, misc-analysis, php-tricks, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `31`
- `docs/img/c02f27239a478b0f8bb50bdf44c01a22.png`
- `docs/img/150d5984854158d51a790027bb3563c5.png`
- `docs/img/bd1f6ce75bd01e776b4e39ebf9a06fe2.png`
- `docs/img/6488529480d6546694589faa3827e4f5.png`
- `docs/img/b83bc1677efc3f37abc4657b23c3dfda.png`
- `docs/img/611a3e7fadb17ca1e15b32efa76c39f3.png`
- `docs/img/702ed8dcad75fbc67b50561065967349.png`
- `docs/img/bf3b0a8f069d04989776f6284dda51d2.png`
- `docs/img/ec522e0d235885d367dfd4a3e0ad57fd.png`
- `docs/img/3f3135f624751a6d3f4bf771d633a80c.png`
- `docs/img/a07ed2c52035a2e330d3eb94da79413b.png`
- `docs/img/6b70966f753a4e4e38c6051585295ef4.png`
- ... and `19` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF show 萌新区解题报告 （一）_Vayn3的博客-CSDN博客_ctf解题报告

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_51090016/article/details/113917961](https://blog.csdn.net/qq_51090016/article/details/113917961)`

### Step 3: 萌新认证

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c02f27239a478b0f8bb50bdf44c01a22`

### Step 4: 萌新_密码1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `150d5984854158d51a790027bb3563c5`

### Step 5: 3\. 萌新_密码2

- Route type: `burp-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `也就是说，flag应该就是：KEY{fwy}`

### Step 6: 萌新 密码3

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `611a3e7fadb17ca1e15b32efa76c39f3`

### Step 7: 萌新 隐写2

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6b70966f753a4e4e38c6051585295ef4`

### Step 8: 萌新 隐写4

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use burp to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: burp
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use burp to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7a3dd8125b2ea308162a8e4dff292449`

### Step 9: 萌新 密码#4

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1b32eff390dfe48675964e4f93659fa1`

### Step 10: 萌新 隐写3

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use burp to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: burp
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use burp to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `8351d22a2419021398e961a4766dcbe5`

### Step 11: 杂项1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `81a10297f6780d53fdd5cce97abf2615`

### Step 12: 杂项2

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use burp to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: burp
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use burp to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `603dfd138001071d2c38b507d3783e2b`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
