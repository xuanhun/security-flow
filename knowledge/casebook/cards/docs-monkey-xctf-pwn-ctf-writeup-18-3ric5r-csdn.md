# monkey [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列18_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `monkey [XCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/monkey-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列18_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/monkey-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9718_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/monkey-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列18_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, netcat, pwntools
- Techniques: binary-exploitation, command-injection, crypto-analysis, ret2libc, reverse-engineering

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `1`
- `docs/img/526303b45b17ac42ef2f47ddf460fd68.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: monkey [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列18_3riC5r的博客-CSDN博客

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `526303b45b17ac42ef2f47ddf460fd68`

### Step 3: elf = ELF(process_name)

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `05fb160732b5493dae565b8c3f35474f`

### Step 4: p = process([process_name], env={'LD_LIBRARY_PATH':'./'})

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `111.198.29.45`

### Step 5: elf = ELF(process_name)

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `111.198.29.45`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
