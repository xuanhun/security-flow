# [DASCTF 2020 四月春季赛] not_RSA 题解_随缘懂点密码学的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `DASCTF 2020 四月春季赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[DASCTF-2020-四月春季赛]-not_RSA-题解_随缘懂点密码学的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BDASCTF-2020-%E5%9B%9B%E6%9C%88%E6%98%A5%E5%AD%A3%E8%B5%9B%5D-not_RSA-%E9%A2%98%E8%A7%A3_%E9%9A%8F%E7%BC%98%E6%87%82%E7%82%B9%E5%AF%86%E7%A0%81%E5%AD%A6%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[DASCTF-2020-四月春季赛]-not_RSA-题解_随缘懂点密码学的博客-CSDN博客.md`

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

### Step 2: [DASCTF 2020 四月春季赛] not_RSA 题解_随缘懂点密码学的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_42667481/article/details/105757426](https://blog.csdn.net/qq_42667481/article/details/105757426)`

### Step 3: 题目内容

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `加 密 过 程 为 ： 加密过程为： 加密过程为：`

### Step 4: 解题思路

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool with the extracted filter/query `记 a = c ⋅ r − n − 1 。 n ∣ a ， 故 可 对 上 式 左 右 和 模 同 除 以 n ， 得 记\ a=c \cdot r^{-n}-1。n \ |\ a ，\\ 故可对上式左右和模同除以n，得 记 a=c⋅r−n−1。n ∣ a，故可对上式左右和模同除以n，得 m ≡ a n ( m o d n ) \\ m \equiv \dfrac{a}{n}\ (mod\ n) m≡na​ (mod n)` and inspect the matching evidence.
- Filters or commands:
  - `记 a = c ⋅ r − n − 1 。 n ∣ a ， 故 可 对 上 式 左 右 和 模 同 除 以 n ， 得 记\ a=c \cdot r^{-n}-1。n \ |\ a ，\\ 故可对上式左右和模同除以n，得 记 a=c⋅r−n−1。n ∣ a，故可对上式左右和模同除以n，得 m ≡ a n ( m o d n ) \\ m \equiv \dfrac{a}{n}\ (mod\ n) m≡na​ (mod n)`
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool with the extracted filter/query `记 a = c ⋅ r − n − 1 。 n ∣ a ， 故 可 对 上 式 左 右 和 模 同 除 以 n ， 得 记\ a=c \cdot r^{-n}-1。n \ |\ a ，\\ 故可对上式左右和模同除以n，得 记 a=c⋅r−n−1。n ∣ a，故可对上式左右和模同除以n，得 m ≡ a n ( m o d n ) \\ m \equiv \dfrac{a}{n}\ (mod\ n) m≡na​ (mod n)` and inspect the matching evidence.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: exploit.py (solve.py)

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(flag)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
