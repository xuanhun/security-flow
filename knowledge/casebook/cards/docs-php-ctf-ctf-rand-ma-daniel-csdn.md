# php伪随机数 ctf,从一道ctf题目理解rand()随机函数_Ma Daniel的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `php伪随机数 ctf,从一道ctf题目理解rand()随机函数`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/php伪随机数-ctf,从一道ctf题目理解rand()随机函数_Ma-Daniel的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/php%E4%BC%AA%E9%9A%8F%E6%9C%BA%E6%95%B0-ctf%2C%E4%BB%8E%E4%B8%80%E9%81%93ctf%E9%A2%98%E7%9B%AE%E7%90%86%E8%A7%A3rand%28%29%E9%9A%8F%E6%9C%BA%E5%87%BD%E6%95%B0_Ma-Daniel%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/php伪随机数-ctf,从一道ctf题目理解rand()随机函数_Ma-Daniel的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: ida
- Techniques: classical-crypto, crypto-analysis, http-analysis, reverse-engineering, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `docs/img/12261cfa459b61e9de1a1ce96d0db462.png`
- `docs/img/3246218cdc0a1060a37ca03f50080532.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: php伪随机数 ctf,从一道ctf题目理解rand()随机函数_Ma Daniel的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida with the extracted filter/query `if ( 4 * (i >> 2) != i || 4 * (i >> 4) == i >> 2 || !(i >> 3) || (result = (i >> 4), result) )` and inspect the matching evidence.
- Tools: ida
- Filters or commands:
  - `if ( 4 * (i >> 2) != i || 4 * (i >> 4) == i >> 2 || !(i >> 3) || (result = (i >> 4), result) )`
  - `if (4 * (i >> 2) != i || 4 * (i >> 4) == i >> 2 || !(i >> 3) || (result = i >> 4, result))`
  - `if ( v2 - v3 + v4 != 0x70667A78`
  - `|| v3 + 2 * (v4 + v2) != 0x22F241C1FLL`
  - `|| (result = 0x31CD156AC3A69DC4LL, v3 * v4 != 0x31CD156AC3A69DC4LL) )`
  - `if ( (*(i + username) <= 96 || *(i + username) > 122) && *(i + username) != 95 )`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida with the extracted filter/query `if ( 4 * (i >> 2) != i || 4 * (i >> 4) == i >> 2 || !(i >> 3) || (result = (i >> 4), result) )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c557529e2ea4bb8d5cb558b7b5575102`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
