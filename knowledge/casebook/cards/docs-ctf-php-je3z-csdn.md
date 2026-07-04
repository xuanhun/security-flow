# 从一道CTF的非预期解看PHP反斜杠匹配问题_Je3Z的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `从一道CTF的非预期解看PHP反斜杠匹配问题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/从一道CTF的非预期解看PHP反斜杠匹配问题_Je3Z的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E4%BB%8E%E4%B8%80%E9%81%93CTF%E7%9A%84%E9%9D%9E%E9%A2%84%E6%9C%9F%E8%A7%A3%E7%9C%8BPHP%E5%8F%8D%E6%96%9C%E6%9D%A0%E5%8C%B9%E9%85%8D%E9%97%AE%E9%A2%98_Je3Z%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/从一道CTF的非预期解看PHP反斜杠匹配问题_Je3Z的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy, netcat
- Techniques: command-injection, file-inclusion, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/fbfd485bae52098d0e058110b90c1b0f.png`
- `docs/img/85a1c3191b3ca9c8a8796335b8e195a4.png`
- `docs/img/54cd71fb46b7dbf3c1472c0a5c3ce919.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 从一道CTF的非预期解看PHP反斜杠匹配问题_Je3Z的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if ($out === "Wa4nn") {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if ($out === "Wa4nn") {`
  - `预期解应该是：`?yell="W".("!"|"@")."4".("."|"@").("."|"@")``
  - `而像`'\\'`不注意的话，很容易偏离最初的用意，像 安洵杯2019easy_web那题就是因为过滤反斜杠 `|\\|\\\\|` 这里的时候正则没有写好，这个正则就变成了匹配`|\``
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `if ($out === "Wa4nn") {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fbfd485bae52098d0e058110b90c1b0f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
