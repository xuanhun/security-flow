# swpuctf2019 p1KkHeap 详细题解_ha1vk的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `swpuctf2019 p1KkHeap 详细题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/swpuctf2019-p1KkHeap-详细题解_ha1vk的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/swpuctf2019-p1KkHeap-%E8%AF%A6%E7%BB%86%E9%A2%98%E8%A7%A3_ha1vk%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/swpuctf2019-p1KkHeap-详细题解_ha1vk的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ida, netcat
- Techniques: binary-exploitation, classical-crypto, encoding-analysis, file-inclusion, reverse-engineering, waf-bypass

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `19`
- `docs/img/fd5afa3f2f18630a5c7cc59700ae4af6.png`
- `docs/img/ae93278f2fe313e5ec8a19b6b89c7403.png`
- `docs/img/454d9ff1dfb5a881b3caa69973f843d0.png`
- `docs/img/af121b27bca9566e95a8812622f40aba.png`
- `docs/img/2b0f42cb95c68f96dabefbfac35eb469.png`
- `docs/img/9fd5cb31fc620fab683002baf32c7648.png`
- `docs/img/3439d113ee331ecae41a947844f10a38.png`
- `docs/img/eef985d2406139260c7c08e4d2103657.png`
- `docs/img/548820e6eac993c9c51e2a828ddfafd9.png`
- `docs/img/7cea2cf80773036b3847c6b7c1131c98.png`
- `docs/img/0ca49d8c9947d1270977b490186f408b.png`
- `docs/img/3cc3fec199265a069f0d40f625d23b95.png`
- ... and `7` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: swpuctf2019 p1KkHeap 详细题解_ha1vk的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/seaaseesa/article/details/103450524](https://blog.csdn.net/seaaseesa/article/details/103450524)`

### Step 3: p1KkHeap

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat with the extracted filter/query `44. #define NARENAS_FROM_NCORES(n) ((n) * (sizeof (long) == 4 ? 2 : 8))` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `44. #define NARENAS_FROM_NCORES(n) ((n) * (sizeof (long) == 4 ? 2 : 8))`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat with the extracted filter/query `44. #define NARENAS_FROM_NCORES(n) ((n) * (sizeof (long) == 4 ? 2 : 8))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `39.98.64.24`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
