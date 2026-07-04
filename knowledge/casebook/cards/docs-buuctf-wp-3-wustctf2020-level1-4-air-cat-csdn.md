# BUUCTF逆向题练习记录（wp） --（3）WUSTCTF2020&&level1-4已完成_Air_cat的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `BUUCTF逆向题练习记录（wp）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF逆向题练习记录（wp）---（3）WUSTCTF2020&&level1-4已完成_Air_cat的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF%E9%80%86%E5%90%91%E9%A2%98%E7%BB%83%E4%B9%A0%E8%AE%B0%E5%BD%95%EF%BC%88wp%EF%BC%89---%EF%BC%883%EF%BC%89WUSTCTF2020%26%26level1-4%E5%B7%B2%E5%AE%8C%E6%88%90_Air_cat%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF逆向题练习记录（wp）---（3）WUSTCTF2020&&level1-4已完成_Air_cat的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: angr, netcat
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, qr-analysis, symbolic-execution

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: Document

- Route type: `angr-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, netcat
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF逆向题练习记录（wp） --（3）WUSTCTF2020&&level1-4已完成_Air_cat的博客-CSDN博客

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use angr to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: angr
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use angr to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `注：funnyre待我搞懂angr后来解`

### Step 3: WUSTCTF2020-level1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use angr, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: angr, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use angr, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `别忘了前缀改成flag`

### Step 4: level2

- Route type: `angr-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, netcat
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `脱upx壳应该不用人教了吧？在被加upx壳的文件的对应目录下，放upx执行文件，然后upx -d 文件名。`

### Step 5: level3

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `wctf2020{Base64_is_the_start_of_reverse}`

### Step 6: level4

- Route type: `angr-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, netcat
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `wctf2020{This_IS_A_7reE}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
