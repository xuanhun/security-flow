# 看雪CTF 2017 第六题设计思路和解题思路_Ericky_的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `看雪CTF 2017 第六题设计思路和解题思路`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/看雪CTF-2017-第六题设计思路和解题思路_Ericky_的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%9C%8B%E9%9B%AACTF-2017-%E7%AC%AC%E5%85%AD%E9%A2%98%E8%AE%BE%E8%AE%A1%E6%80%9D%E8%B7%AF%E5%92%8C%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF_Ericky_%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/看雪CTF-2017-第六题设计思路和解题思路_Ericky_的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: not detected
- Techniques: classical-crypto, encoding-analysis, stream-cipher

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `3`
- `docs/img/96ab9689a32ab092f542cfbf25bc9a01.png`
- `docs/img/fb42d66bc2065a08b6e9da5b9f8b9091.png`
- `docs/img/eec439522517abb2c8d73c35cba4e97a.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 看雪CTF 2017 第六题设计思路和解题思路_Ericky_的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这道题主要需要花时间搞清楚套路，就迎刃而解了。^_^`

### Step 3: java层稍作字符串加密和类名方法名混淆处理(本来是打算java层也做点文章的@_@)

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `96ab9689a32ab092f542cfbf25bc9a01`

### Step 4: so层用花指令对程序指令进行混淆，在一定程度上防止分析。

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fb42d66bc2065a08b6e9da5b9f8b9091`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
