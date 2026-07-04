# NEFUCTF校赛-题解_Do1phln的博客-CSDN博客_这个id不能分配为此对象的所有者

## Case Metadata

- Category: `Misc`
- Platform: `NEFUCTF校赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/NEFUCTF校赛-题解_Do1phln的博客-CSDN博客_这个id不能分配为此对象的所有者.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/NEFUCTF%E6%A0%A1%E8%B5%9B-%E9%A2%98%E8%A7%A3_Do1phln%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E8%BF%99%E4%B8%AAid%E4%B8%8D%E8%83%BD%E5%88%86%E9%85%8D%E4%B8%BA%E6%AD%A4%E5%AF%B9%E8%B1%A1%E7%9A%84%E6%89%80%E6%9C%89%E8%80%85.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/NEFUCTF校赛-题解_Do1phln的博客-CSDN博客_这个id不能分配为此对象的所有者.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media, web-app
- Tools: ida, radare2, z3
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, image-analysis, misc-analysis, qr-analysis, reverse-engineering, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `17`
- `docs/img/87a608b8c287c0f64fa6872dd3808dc0.png`
- `docs/img/0aa540f390695fb9a5baca77ab12edfa.png`
- `docs/img/b1e31dec2c5f10e377dd590a1c279b81.png`
- `docs/img/bffa25ebdc221b5b839766fad8ada106.png`
- `docs/img/636c1eba0a25e2e58b86446e2c43193f.png`
- `docs/img/5680f16eb45467d478f83e3eae70a1e3.png`
- `docs/img/e6bc2457d8fbfd6909ec19b09c7c60c9.png`
- `docs/img/902a9cb2f22ed626e71faee1f02b4343.png`
- `docs/img/9aaa82dcc1c399bf2b1f77fb9ddcaf4d.png`
- `docs/img/6d931232f98dc59f67d9cf78a4b7de0a.png`
- `docs/img/0df9dea917ebcf91511681cd15ab2f94.png`
- `docs/img/566e04721e9ca54977e68e5113785b12.png`
- ... and `5` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: NEFUCTF校赛-题解_Do1phln的博客-CSDN博客_这个id不能分配为此对象的所有者

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> Do1phln`

### Step 3: 签到

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 4: signin

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 5: Re_SignUp

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use cyberchef, ida to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: cyberchef, ida
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use cyberchef, ida to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - The proof is the returned command output or filesystem effect from the injected command.
- Evidence rule: The proof is the returned command output or filesystem effect from the injected command.

### Step 6: untitle

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use radare2 to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use radare2 to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 7: 蛇图攻击

- Route type: `ida-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 8: 别人家的孩子

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 9: 谁还没受过伤呢

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `87a608b8c287c0f64fa6872dd3808dc0`

### Step 10: CRYPTO

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 11: RSA1.0

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 12: are you file?

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `zhalanmima.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
