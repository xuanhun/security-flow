# CTF-NEFU校赛-题解_「已注销」的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-NEFU校赛-题解_「已注销」的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-NEFU%E6%A0%A1%E8%B5%9B-%E9%A2%98%E8%A7%A3_%E3%80%8C%E5%B7%B2%E6%B3%A8%E9%94%80%E3%80%8D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-NEFU校赛-题解_「已注销」的博客-CSDN博客.md`

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

- Referenced assets: `1`
- `docs/img/37c679031b5c50c32c20839a3b642e0a.png`

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

### Step 2: CTF-NEFU校赛-题解_「已注销」的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, radare2, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 0ERROR`

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
- Result: `even_1f_i_L0Ve_U}`

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
- Result: `import gmpy2`

### Step 12: 由题目可知

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, radare2, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, radare2, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e = 65537`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
