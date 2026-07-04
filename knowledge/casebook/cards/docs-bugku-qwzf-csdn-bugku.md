# BUGKU做题总结(一)_Qwzf的博客-CSDN博客_bugku解题

## Case Metadata

- Category: `Misc`
- Platform: `BUGKU做题总结(一)`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUGKU做题总结(一)_Qwzf的博客-CSDN博客_bugku解题.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUGKU%E5%81%9A%E9%A2%98%E6%80%BB%E7%BB%93%28%E4%B8%80%29_Qwzf%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_bugku%E8%A7%A3%E9%A2%98.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUGKU做题总结(一)_Qwzf的博客-CSDN博客_bugku解题.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: not detected
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, misc-analysis

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `24`
- `docs/img/83379775a445bf844545d0e764bb1be1.png`
- `docs/img/351cf40521ffec785130fa29fdfcb3b4.png`
- `docs/img/2677c5f8423176c67a25c8370ea3e4c4.png`
- `docs/img/3ba58ca92bf6192e4ba189c36ed89c19.png`
- `docs/img/2e5dae805dfc7621d1c922c64add30eb.png`
- `docs/img/d6d18e792c627a904845991205fea916.png`
- `docs/img/dfef3e572f254ae4cc7391eca64c870d.png`
- `docs/img/122ca8cc0ff950ab15bb77c41489c399.png`
- `docs/img/3c5de41d7fe994e56f6e6ed53a3203a2.png`
- `docs/img/48c3e74765af4abe88a5ba4676a4d2dd.png`
- `docs/img/eb5676226dfd5a9070a37d7060219ae9.png`
- `docs/img/972701b2ed9cd7d9bcf6e420997c0b30.png`
- ... and `12` more

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: MISC1(啊哒)

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `83379775a445bf844545d0e764bb1be1`

### Step 3: MISC2(宽带信息泄露)

- Route type: `evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `dfef3e572f254ae4cc7391eca64c870d`

### Step 4: MISC3(come_game)

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use the artifact-specific tool to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `48c3e74765af4abe88a5ba4676a4d2dd`

### Step 5: MISC4(linux)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b1af3b55c53a883c5f1bf60277fd6c5c`

### Step 6: MISC5(做个游戏(08067CTF))

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5a3317e2caf2bc1e06855da4c22a4ec7`

### Step 7: MISC6(想蹭网先解开密码)

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1b329fc8fa9081885bb099a6d40dff41`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
