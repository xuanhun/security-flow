# ctf xor题_详解两道CTF逆向题_weixin_34324618的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `ctf xor题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf-xor题_详解两道CTF逆向题_weixin_34324618的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf-xor%E9%A2%98_%E8%AF%A6%E8%A7%A3%E4%B8%A4%E9%81%93CTF%E9%80%86%E5%90%91%E9%A2%98_weixin_34324618%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf-xor题_详解两道CTF逆向题_weixin_34324618的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: ida, netcat, radare2
- Techniques: classical-crypto, encoding-analysis, integer-overflow, misc-analysis, reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf xor题_详解两道CTF逆向题_weixin_34324618的博客-CSDN博客

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use ida, netcat, radare2 with the extracted filter/query `if ( *v1 != v1[208] )` and inspect the matching evidence.
- Tools: ida, netcat, radare2
- Filters or commands:
  - `if ( *v1 != v1[208] )`
  - `v3 = -(v2 < v1[208]) | 1;`
  - `if ( i % 3 == 1 )`
  - `sub_411302(&v3 == &v3, v1, a1);`
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use ida, netcat, radare2 with the extracted filter/query `if ( *v1 != v1[208] )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `str1 += chr(ord(str2[i])^i)`

### Step 3: print str1

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `总结：当没有头绪的时候，可以查看变量或字符串的引用`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
