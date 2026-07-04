# BUUCTF RSA题目全解3_宁嘉的博客-CSDN博客_buuctf rsa3

## Case Metadata

- Category: `Crypto`
- Platform: `BUUCTF RSA题目全解3`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-RSA题目全解3_宁嘉的博客-CSDN博客_buuctf-rsa3.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-RSA%E9%A2%98%E7%9B%AE%E5%85%A8%E8%A7%A33_%E5%AE%81%E5%98%89%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf-rsa3.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-RSA题目全解3_宁嘉的博客-CSDN博客_buuctf-rsa3.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, stego-media, web-app challenges.

## Input Signals

- Artifacts: ciphertext, stego-media, web-app
- Tools: netcat, z3
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `8`
- `docs/img/5e94c4975da43d164cea205e4059306c.png`
- `docs/img/0870fdf094bc0ed4dc89d6b56bf35b6c.png`
- `docs/img/baa3724ac2be40f02025ec828c5d7a52.png`
- `docs/img/54a8971b70ca83f28796738f94bb3ab1.png`
- `docs/img/49d58e4c0c2b630ee07710fee5ac6baa.png`
- `docs/img/0dcd2e96440dab1daaafc8ae3d392625.png`
- `docs/img/0e19ad7f1fd4071f27e07d893740f2e9.png`
- `docs/img/995486df03755d16d7e48a7852b85536.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF RSA题目全解3_宁嘉的博客-CSDN博客_buuctf rsa3

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/MikeCoke/article/details/107973068](https://blog.csdn.net/MikeCoke/article/details/107973068)`

### Step 3: [WUSTCTF2020]babyrsa

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `189239861511125143212536989589123569301`

### Step 4: RSA4

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `**flag{D4mn_y0u_h4s74d_wh47_4_b100dy_b4s74rd!}**`

### Step 5: [AFCTF2018]你能看出这是什么加密么

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 with the extracted filter/query `flag{R54_|5_$0_$imp13}` and inspect the matching evidence.
- Tools: netcat, z3
- Filters or commands:
  - `flag{R54_|5_$0_$imp13}`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 with the extracted filter/query `flag{R54_|5_$0_$imp13}` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{R54_|5_$0_$imp13}`

### Step 6: [HDCTF2019]together（共模攻击）

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `if b==0: return 1, 0` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `if b==0: return 1, 0`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `if b==0: return 1, 0` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5e94c4975da43d164cea205e4059306c`

### Step 7: [RoarCTF2019]babyRSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `49d58e4c0c2b630ee07710fee5ac6baa`

### Step 8: [ACTF新生赛2020]crypto-rsa3

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0dcd2e96440dab1daaafc8ae3d392625`

### Step 9: [RoarCTF2019]RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0e19ad7f1fd4071f27e07d893740f2e9`

### Step 10: [AFCTF2018]可怜的RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(flag)`

### Step 11: RSA & what

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `995486df03755d16d7e48a7852b85536`

### Step 12: 关键代码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(bytes_to_string(flag))`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
