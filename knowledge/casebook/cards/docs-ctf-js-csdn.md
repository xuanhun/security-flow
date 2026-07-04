# CTF习题解答--查找正确的密码 [JS题型]_乌恩大侠的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `CTF习题解答`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF习题解答--查找正确的密码-[JS题型]_乌恩大侠的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E4%B9%A0%E9%A2%98%E8%A7%A3%E7%AD%94--%E6%9F%A5%E6%89%BE%E6%AD%A3%E7%A1%AE%E7%9A%84%E5%AF%86%E7%A0%81-%5BJS%E9%A2%98%E5%9E%8B%5D_%E4%B9%8C%E6%81%A9%E5%A4%A7%E4%BE%A0%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF习题解答--查找正确的密码-[JS题型]_乌恩大侠的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, ids challenges.

## Input Signals

- Artifacts: ciphertext, ids
- Tools: netcat, radare2
- Techniques: crypto-analysis, qr-analysis

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `2`
- `docs/img/e98b0451c6468d3d8a4b3b4386283e46.png`
- `docs/img/92cd9c81ad5d62d80417aea13df6a437.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF习题解答--查找正确的密码 [JS题型]_乌恩大侠的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_36666115/article/details/80137538](https://blog.csdn.net/qq_36666115/article/details/80137538)`

### Step 3: 小黑客们，坐好了，老司机要开车了！

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e98b0451c6468d3d8a4b3b4386283e46`

### Step 4: 首页的代码

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use netcat, radare2 with the extracted filter/query `var b = s === "FAKE-TOKEN"` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `var b = s === "FAKE-TOKEN"`
  - `for (var i = 0; i < ip.length; i++) {`
  - `x = ip.charCodeAt(i);`
  - `var len = ip.length;`
  - `var t = (ip.charCodeAt(i) << 16) | (i + 1 < len ? ip.charCodeAt(i + 1) << 8 : 0) | (i + 2 < len ? ip.charCodeAt(i + 2) : 0);`
  - `if (i * 8 + j * 6 > ip.length * 8)`
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use netcat, radare2 with the extracted filter/query `var b = s === "FAKE-TOKEN"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `}`

### Step 5: 正式 开始了

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `return s === "FAKE-TOKEN";` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `return s === "FAKE-TOKEN";`
  - `if (s.length == a.length) {`
  - `if (a[i] - s.charCodeAt(i) != 3)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `return s === "FAKE-TOKEN";` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `s就是最后要得出的密码；`

### Step 6: 解决脚本

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `consolo.log(s)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
