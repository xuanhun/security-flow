# [DASCTF八月挑战赛]easymath题解_mortal15的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `DASCTF八月挑战赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[DASCTF八月挑战赛]easymath题解_mortal15的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BDASCTF%E5%85%AB%E6%9C%88%E6%8C%91%E6%88%98%E8%B5%9B%5Deasymath%E9%A2%98%E8%A7%A3_mortal15%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[DASCTF八月挑战赛]easymath题解_mortal15的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: not detected
- Techniques: crypto-analysis

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `7`
- `docs/img/a7ed206986afa6764cb2280d6b2adb96.png`
- `docs/img/f438d4180557ff5491856e399f2364d0.png`
- `docs/img/b4ad2f6c1830f099853d07d3d6b4a58b.png`
- `docs/img/bacbc9d591c4f2cd942ab4d85718b993.png`
- `docs/img/591e1f44e7d5209f2cc1deac8e4599d4.png`
- `docs/img/32580b24c4eed563c1ca88898f149111.png`
- `docs/img/d2692b310e0feb93578c9e9720f59886.png`

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

### Step 2: [DASCTF八月挑战赛]easymath题解_mortal15的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `DASCTF八月赛的Crypto方向，拿下其他两道题很简单，但是这道最多人解出来的题反而解不出来。打完比赛回来看其他师傅写的wp，说是这是TSGCTF原题，所以直接放弃思考，上大佬的wp，我看看大佬这个wp，感觉这题还是有点东西的，里面涉及的基础的一些数学知识还是值得总结总结。`

### Step 3: 题目

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `题目就两行，意思大概就是有个长度不超过50的flag，让它右移10000个二进制位，然后截下来最后175个十进制位，让我们通过截下来的175个十进制位还原flag。`

### Step 4: 分析

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `题目也有提示，ezmath嘛，跟数学有关，这里最好的解决方案还是用数学式子来表示其中的关系。`

### Step 5: **![(flag*2^{10000})%10^{175} = r %10^{175}](img/a7ed206986afa6764cb2280d6b2adb96.png)**

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `分析到这里其实就很容易想到2**10000的逆元了，通过逆元消掉其他项，剩下一个flag。`

### Step 6: 求解

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f438d4180557ff5491856e399f2364d0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
