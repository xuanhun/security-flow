# UNCTF2020 writeup部分题解_YE.SS的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `UNCTF2020 writeup部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/UNCTF2020-writeup部分题解_YE.SS的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/UNCTF2020-writeup%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_YE.SS%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/UNCTF2020-writeup部分题解_YE.SS的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media, web-app
- Tools: ida, netcat, pwntools, radare2
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, image-analysis, misc-analysis, osint, php-tricks, qr-analysis, ret2libc, reverse-engineering, stack-overflow, traffic-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `26`
- `docs/img/265d9c6856e010a806dc4473d4190e17.png`
- `docs/img/44fe57aa1716c47509d53b91f151048e.png`
- `docs/img/1a51d3beacb8b4104ed4ebdcba65c705.png`
- `docs/img/c39caa01bf506b6fc754b462f6256a92.png`
- `docs/img/1f2ee063466eea3449ab7b37d5807831.png`
- `docs/img/06a12997e8b4d3c0438a8ce3add8a202.png`
- `docs/img/ae031d114f353ab20bebdb800c463787.png`
- `docs/img/c55a7ce5496dfcc413e5d274082f4221.png`
- `docs/img/a2e8fbd8821f94db92846d19a972e2f0.png`
- `docs/img/01264ce2911741347b9430f993d1c6bc.png`
- `docs/img/a23c544d0bde7deca08087b26f43a0db.png`
- `docs/img/9a4f5ceeb169c8103c00f701469e0b2a.png`
- ... and `14` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, pwntools, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, pwntools, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: UNCTF2020 writeup部分题解_YE.SS的博客-CSDN博客

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use ida, netcat, pwntools, radare2 with the extracted filter/query `?a=echo%20`cat%20flag.php|base64`;` and inspect the matching evidence.
- Tools: ida, netcat, pwntools, radare2
- Filters or commands:
  - `?a=echo%20`cat%20flag.php|base64`;`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use ida, netcat, pwntools, radare2 with the extracted filter/query `?a=echo%20`cat%20flag.php|base64`;` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `265d9c6856e010a806dc4473d4190e17`

### Step 3: 操作内容：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c55a7ce5496dfcc413e5d274082f4221`

### Step 4: 操作内容：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a23c544d0bde7deca08087b26f43a0db`

### Step 5: 操作内容：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat, pwntools, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat, pwntools, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat, pwntools, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `45.158.33.12:8000`

### Step 6: 操作内容：

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cd826e148ea6ef140bcd50b94a42a900`

### Step 7: 操作内容：

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ae12c28506d8b3b8ecfe7160919d54d0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
