# CTF题解三 逆向 where is your flag（ISCC2017）_目标是技术宅的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `CTF题解三 逆向 where is your flag（ISCC2017）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF题解三-逆向-where-is-your-flag（ISCC2017）_目标是技术宅的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E9%A2%98%E8%A7%A3%E4%B8%89-%E9%80%86%E5%90%91-where-is-your-flag%EF%BC%88ISCC2017%EF%BC%89_%E7%9B%AE%E6%A0%87%E6%98%AF%E6%8A%80%E6%9C%AF%E5%AE%85%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF题解三-逆向-where-is-your-flag（ISCC2017）_目标是技术宅的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: not detected
- Techniques: reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `2`
- `docs/img/7eaaee1384ffc68f3fe7e4d458a81e10.png`
- `docs/img/5e8ccb3e923ef936a9af629a00bd1727.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use the artifact-specific tool to locate strings, comparisons, and control-flow decisions relevant to the input.
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use the artifact-specific tool to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF题解三 逆向 where is your flag（ISCC2017）_目标是技术宅的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/LJFYYJ/article/details/81006047](https://blog.csdn.net/LJFYYJ/article/details/81006047)`

### Step 3: 直接进入test函数：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use the artifact-specific tool to locate strings, comparisons, and control-flow decisions relevant to the input.
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use the artifact-specific tool to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7eaaee1384ffc68f3fe7e4d458a81e10`

### Step 4: 反思：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use the artifact-specific tool to locate strings, comparisons, and control-flow decisions relevant to the input.
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use the artifact-specific tool to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `本题主要对于s2的异或理解上出现了问题，忘记考虑了与s2地址相连的其它变量。对于16进制的表示以及小端的特性还是不够熟悉。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
