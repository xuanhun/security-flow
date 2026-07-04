# BUUCTF-MISC刷题记录-1_L.o.W的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-MISC刷题记录-1_L.o.W的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-MISC%E5%88%B7%E9%A2%98%E8%AE%B0%E5%BD%95-1_L.o.W%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-MISC刷题记录-1_L.o.W的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, stego-media challenges.

## Input Signals

- Artifacts: ciphertext, stego-media
- Tools: binwalk, foremost, stegsolve, z3
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, image-analysis, misc-analysis, qr-analysis, stego-extraction, symbolic-execution

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `20`
- `docs/img/616ead91eb5136b62c9c55b9104fae8b.png`
- `docs/img/1e12e93d7214777db2db9ef3c812b71a.png`
- `docs/img/a56b21a2e126aa1ca4903bc2993d38a7.png`
- `docs/img/ccfc5f7f6750e6147bd29ee3044c00df.png`
- `docs/img/8b9bfb12e0eb31cdfdaad28ad2cd7178.png`
- `docs/img/dc71342dcbf1fc3745c301006a4d96ff.png`
- `docs/img/41e746ab90eea0f45a99da01c35b3416.png`
- `docs/img/bf46f09dcaae83ccb3eeb3ab0bb6f72d.png`
- `docs/img/3f6d41750331a9a7e4b89fb77f50f245.png`
- `docs/img/e6cb142cb13fe35b50607f95c1b07292.png`
- `docs/img/c465e31391075ec1e6ebc339da5f41ba.png`
- `docs/img/bf9d8bbb118cd89ea639dda47b25977f.png`
- ... and `8` more

## Solve Thinking

### Step 1: Document

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF-MISC刷题记录-1_L.o.W的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, foremost, stegsolve, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, foremost, stegsolve, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_44145820/article/details/104701824](https://blog.csdn.net/weixin_44145820/article/details/104701824)`

### Step 3: 二维码

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, foremost to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, foremost
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, foremost to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `616ead91eb5136b62c9c55b9104fae8b`

### Step 4: N种方法解决

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, foremost, stegsolve, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, foremost, stegsolve, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8b9bfb12e0eb31cdfdaad28ad2cd7178`

### Step 5: 大白

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `41e746ab90eea0f45a99da01c35b3416`

### Step 6: 基础破解

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e6cb142cb13fe35b50607f95c1b07292`

### Step 7: 你竟然赶我走

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c465e31391075ec1e6ebc339da5f41ba`

### Step 8: LSB

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: stegsolve
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `bf9d8bbb118cd89ea639dda47b25977f`

### Step 9: 乌镇峰会种图

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `64033233ebc575ee2f0e844a64a1131f`

### Step 10: rar

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, stegsolve, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2b07849b5da2aa5808c14651311cfa30`

### Step 11: ningen

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, foremost, stegsolve, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, foremost, stegsolve, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `50b4feac770a675f202d10be6689190a`

### Step 12: qr

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, foremost, stegsolve, z3 to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, foremost, stegsolve, z3
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, foremost, stegsolve, z3 to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `bcdc8d2eb29818ae99058dd58b718868`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
