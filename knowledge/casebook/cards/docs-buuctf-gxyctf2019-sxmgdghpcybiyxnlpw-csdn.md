# BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==_末 初的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==_末-初的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF%EF%BC%9A%5BGXYCTF2019%5DSXMgdGhpcyBiYXNlPw%3D%3D_%E6%9C%AB-%E5%88%9D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==_末-初的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, stego-media, web-app challenges.

## Input Signals

- Artifacts: ciphertext, stego-media, web-app
- Tools: netcat, radare2, z3
- Techniques: classical-crypto, encoding-analysis, http-analysis, image-analysis, misc-analysis, qr-analysis, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `1`
- `docs/img/e036d8511fffe090e5f568cba164eb3d.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==_末 初的博客-CSDN博客

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use netcat, radare2, z3 with the extracted filter/query `> 题目地址：https://buuoj.cn/challenges#[GXYCTF2019]SXMgdGhpcyBiYXNlPw==` and inspect the matching evidence.
- Tools: netcat, radare2, z3
- Filters or commands:
  - `> 题目地址：https://buuoj.cn/challenges#[GXYCTF2019]SXMgdGhpcyBiYXNlPw==`
  - `PS C:\Users\Administrator\Desktop> php -r "var_dump(base64_decode('SXMgdGhpcyBiYXNlPw=='));"`
  - `SmUgc3ViaXMsCt==`
  - `RWxsZSBtZSBkaXQsCo==`
  - `SmUgdm91ZSBtZXMgbnVpdHMsCm==`
  - `QSBsJ2Fzc2FzeW1waG9uaWUsCl==`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use netcat, radare2, z3 with the extracted filter/query `> 题目地址：https://buuoj.cn/challenges#[GXYCTF2019]SXMgdGhpcyBiYXNlPw==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e036d8511fffe090e5f568cba164eb3d`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
