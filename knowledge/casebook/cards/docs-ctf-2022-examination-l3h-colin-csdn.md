# *CTF-2022 examination 题解_L3H_CoLin的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `*CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/＊CTF-2022-examination-题解_L3H_CoLin的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%EF%BC%8ACTF-2022-examination-%E9%A2%98%E8%A7%A3_L3H_CoLin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/＊CTF-2022-examination-题解_L3H_CoLin的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: netcat, pwntools
- Techniques: binary-exploitation, ret2libc, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `9`
- `docs/img/2c4297ae478b5abd6810cfc4dc6d9020.png`
- `docs/img/f8433a4892091856913334b4789c3134.png`
- `docs/img/6ba10977c222a1c4e36cefa9e7b8d6d3.png`
- `docs/img/cebbe7937f127fda8ea0e95aee55ec8e.png`
- `docs/img/88074613542b921c703251b18780f731.png`
- `docs/img/cf5134091c8e1cb0b3c51ca1725e40b9.png`
- `docs/img/b39e68cbe1d0823c72f58897450fa72c.png`
- `docs/img/d6885ead741ec3a3af2222c6cac498da.png`
- `docs/img/bce9adc19afcc5e89d0161b68e920977.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: *CTF-2022 examination 题解_L3H_CoLin的博客-CSDN博客

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat, pwntools with the extracted filter/query `|| __builtin_expect (nextsize >= av->system_mem, 0))` and inspect the matching evidence.
- Tools: netcat, pwntools
- Filters or commands:
  - `|| __builtin_expect (nextsize >= av->system_mem, 0))`
  - `assert(current_role == 0)`
  - `assert(current_role == 0 and students[sid] == 1)`
  - `assert(current_role == 1)`
  - `assert(current_role == 1 and students[sid] != 0)`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat, pwntools with the extracted filter/query `|| __builtin_expect (nextsize >= av->system_mem, 0))` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2c4297ae478b5abd6810cfc4dc6d9020`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
