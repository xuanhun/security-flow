# get_started_3dsctf_2016 1_一路开花●-●的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `get`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/get_started_3dsctf_2016-1_一路开花●-●的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/get_started_3dsctf_2016-1_%E4%B8%80%E8%B7%AF%E5%BC%80%E8%8A%B1%E2%97%8F-%E2%97%8F%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/get_started_3dsctf_2016-1_一路开花●-●的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, ida, netcat, pwntools
- Techniques: binary-exploitation, classical-crypto, file-inclusion, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `20`
- `docs/img/c66c86d165a5817ef29e7c0aa9aef048.png`
- `docs/img/1d427b48495a11685cf651cd57a917a3.png`
- `docs/img/d71ee650a72602d3fe37ea387a2403f1.png`
- `docs/img/281e9767ac40222da2e3726898c0b00a.png`
- `docs/img/1ac7ce58fa11de61fad57ecf980d6b4d.png`
- `docs/img/cddaece7bd36fd0dd2915f768163fd24.png`
- `docs/img/dafe8ecd27c29f61d4315bf223557b38.png`
- `docs/img/c43a0fc1c4b3a1dc603e15ddb5fbe2da.png`
- `docs/img/7663792c8b8dc4930172030b56abf81a.png`
- `docs/img/d173d61ab8ca6486f580dc831fcf52de.png`
- `docs/img/59c2c2a4f2fa26a1163dd4a3e7403f1d.png`
- `docs/img/cd37fb1d3a8c13fe4f4551618da0b5b9.png`
- ... and `8` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: get_started_3dsctf_2016 1_一路开花●-●的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c66c86d165a5817ef29e7c0aa9aef048`

### Step 3: 查看文件权限

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use gdb, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use gdb, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1d427b48495a11685cf651cd57a917a3`

### Step 4: 查看源程序

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d71ee650a72602d3fe37ea387a2403f1`

### Step 5: 分析

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `281e9767ac40222da2e3726898c0b00a`

### Step 6: 题解代码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `shellcraft.sh`

### Step 7: 大功告成

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cd37fb1d3a8c13fe4f4551618da0b5b9`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
