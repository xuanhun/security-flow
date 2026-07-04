# BUUCTF[SCTF2019]Who is he题解_mortal15的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `BUUCTF[SCTF2019]Who is he题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF[SCTF2019]Who-is-he题解_mortal15的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF%5BSCTF2019%5DWho-is-he%E9%A2%98%E8%A7%A3_mortal15%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF[SCTF2019]Who-is-he题解_mortal15的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: not detected
- Techniques: crypto-analysis

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `15`
- `docs/img/09bfd0005edb2ee8c3cd5ac4116f8b89.png`
- `docs/img/8348749e44e3e5af304a677fac455962.png`
- `docs/img/19f9c911097df61fd8f65ab010350fc2.png`
- `docs/img/b9eb4aeb6218943c552c076418e6debc.png`
- `docs/img/e534a0ad73d496de66c3cbb1edbfe803.png`
- `docs/img/431760de21346d4d6777b497e9476b89.png`
- `docs/img/7fca6a5e958c879d809e772d50772107.png`
- `docs/img/fa19006241dd1e0ba306924e6599efba.png`
- `docs/img/d36adf98f3fd47654583388090171985.png`
- `docs/img/376b482b55a6ad85e5367e83c6fa3caf.png`
- `docs/img/b2cd050b8a82432f288def8b5822ede5.png`
- `docs/img/c7b6034186e7c73976d5eb7f59945b37.png`
- ... and `3` more

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

### Step 2: BUUCTF[SCTF2019]Who is he题解_mortal15的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/a5555678744/article/details/118371570](https://blog.csdn.net/a5555678744/article/details/118371570)`

### Step 3: 简介

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `话说回来，虽然是unity逆向，但是这道题有点特例独行，一般unity的关键信息都会放在assembly-Csharp.dll里面，这道题看似也不例外，但是得到的却是假答案。真正的答案需要依靠动态调试来慢慢找。`

### Step 4: 题解

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `09bfd0005edb2ee8c3cd5ac4116f8b89`

### Step 5: 定位关键判断

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b9eb4aeb6218943c552c076418e6debc`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
