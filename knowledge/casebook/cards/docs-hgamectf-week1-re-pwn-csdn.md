# HgameCTF(week1)-RE,PWN题解析_合天网安实验室的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `HgameCTF(week1)`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/HgameCTF(week1)-RE,PWN题解析_合天网安实验室的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/HgameCTF%28week1%29-RE%2CPWN%E9%A2%98%E8%A7%A3%E6%9E%90_%E5%90%88%E5%A4%A9%E7%BD%91%E5%AE%89%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/HgameCTF(week1)-RE,PWN题解析_合天网安实验室的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: ida, netcat, pwntools, z3
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, osint, ret2libc, reverse-engineering, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `4`
- `docs/img/a36916f7004de0a0653211c700381e8b.png`
- `docs/img/1f4d2bcd016e34f15585e72d9ada4a63.png`
- `docs/img/11cf5b91394d35c134358aff666723bf.png`
- `docs/img/d9870527d545ded9194582008312fa8f.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, pwntools, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, pwntools, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, pwntools, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: HgameCTF(week1)-RE,PWN题解析_合天网安实验室的博客-CSDN博客

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida with the extracted filter/query `if ( v3 == 'd' )` and inspect the matching evidence.
- Tools: ida
- Filters or commands:
  - `if ( v3 == 'd' )`
  - `if ( v3 == 's' )`
  - `if ( v3 != 'w' )`
  - `if ( v3 != 'a' )`
  - `if ( local < (char *)&unk_602080 || local > (char *)&unk_60247C || *(_DWORD *)local & 1 )`
  - `01|00|01 01 01 01 01 01 01 01 01 01 01 01 01 01`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida with the extracted filter/query `if ( v3 == 'd' )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `key = [0x4C,0x3C,0xD6,0x36,0x50,0x88,0x20,0xCC]`

### Step 3: right =[0xEB ,0x82 ,0xD6 ,0xB1 ,0xAF ,0xC1 ,0x2C,0x0F]

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat, pwntools, z3 with the extracted filter/query `left_temp = left_q_5|left_q_a` and inspect the matching evidence.
- Tools: netcat, pwntools, z3
- Filters or commands:
  - `left_temp = left_q_5|left_q_a`
  - `right_temp = right_q_5|right_q_a`
  - `left_temp_2 = left_q_5_2|left_q_a_2`
  - `if ( v11 == -1 )`
  - `if ( *(&v31 + 3 * j + k) != v12 )`
  - `a+b+2*c==0x0065`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat, pwntools, z3 with the extracted filter/query `left_temp = left_q_5|left_q_a` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `47.103.214.163`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
