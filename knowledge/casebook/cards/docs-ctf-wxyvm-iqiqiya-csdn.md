# 南邮CTF逆向题第四道WxyVM解题思路_iqiqiya的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `南邮CTF逆向题第四道WxyVM解题思路`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/南邮CTF逆向题第四道WxyVM解题思路_iqiqiya的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%8D%97%E9%82%AECTF%E9%80%86%E5%90%91%E9%A2%98%E7%AC%AC%E5%9B%9B%E9%81%93WxyVM%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF_iqiqiya%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/南邮CTF逆向题第四道WxyVM解题思路_iqiqiya的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida, netcat
- Techniques: encoding-analysis, reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `6`
- `docs/img/3d5ec77e98d704a5e1f7e5ca6cafe06b.png`
- `docs/img/c6489d83155121c271eb552fa501745a.png`
- `docs/img/f015d7a91305453afe1fa9d0c41a328c.png`
- `docs/img/b44578a31b5c4627a3fb9b7ea1ce81d5.png`
- `docs/img/b8303db0da97ff045e10bcfccb071ab5.png`
- `docs/img/5c4ece3dd25587ac7889c66fcb8efc87.png`

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

### Step 2: 南邮CTF逆向题第四道WxyVM解题思路_iqiqiya的博客-CSDN博客

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat with the extracted filter/query `if****(** strlen**(&**byte_604B80**)****!=**24**)**//如果获取的字符串长度不等于24` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `if****(** strlen**(&**byte_604B80**)****!=**24**)**//如果获取的字符串长度不等于24`
  - `if****(*****(&**byte_604B80 **+** i**)****!=** dword_601060**[**i**]****)**//比较404B80加上i的地址处保存的值与601060处的值`
  - `if** i **==**1**:**`
  - `elif** i **==**2**:**`
  - `elif** i **==**3**:**`
  - `if** hex**(**flag**[**k**])==**s**[**k**]:**`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat with the extracted filter/query `if****(** strlen**(&**byte_604B80**)****!=**24**)**//如果获取的字符串长度不等于24` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3d5ec77e98d704a5e1f7e5ca6cafe06b`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
