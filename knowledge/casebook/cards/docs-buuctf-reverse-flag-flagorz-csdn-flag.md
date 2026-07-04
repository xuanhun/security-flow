# [BUUCTF] [Reverse]不一样的flag_flagorz的博客-CSDN博客_不一样的flag

## Case Metadata

- Category: `Reverse`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[BUUCTF]-[Reverse]不一样的flag_flagorz的博客-CSDN博客_不一样的flag.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BBUUCTF%5D-%5BReverse%5D%E4%B8%8D%E4%B8%80%E6%A0%B7%E7%9A%84flag_flagorz%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E4%B8%8D%E4%B8%80%E6%A0%B7%E7%9A%84flag.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[BUUCTF]-[Reverse]不一样的flag_flagorz的博客-CSDN博客_不一样的flag.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: not detected
- Techniques: osint

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: [BUUCTF] [Reverse]不一样的flag_flagorz的博客-CSDN博客_不一样的flag

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/inuseonline/article/details/120618298](https://blog.csdn.net/inuseonline/article/details/120618298)`

### Step 3: 前言

- Route type: `evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `下面说一下我的思路吧。`

### Step 4: 题目

- Route type: `evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `是不是做习惯了常规的逆向题目？试试这道题，看你在能不能在程序中找到真正的flag！注意：flag并非是flag{XXX}形式，就是一个’字符串‘，考验眼力的时候到了！ 注意：得到的 flag 请包上 flag{} 提交`

### Step 5: 思路

- Route type: `evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool with the extracted filter/query `if ( input == 2 ) // 下` and inspect the matching evidence.
- Filters or commands:
  - `if ( input == 2 ) // 下`
  - `if ( input == 3 ) // 左`
  - `if ( input != 4 )`
  - `if ( input != 1 )`
  - `if ( *(int *)&v_5x5_4[4 * i + 25] < 0 || *(int *)&v_5x5_4[4 * i + 25] > 4 )// 超出边界退出。25是上下位置，29超出数组了，指针指向到v4的位置，为左右位置`
  - `if ( v7[5 * *(_DWORD *)&v_5x5_4[25] - 41 + v4] == '1' )`
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool with the extracted filter/query `if ( input == 2 ) // 下` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `所以，最后的答案才是迷宫的路径，“下下下右右上上右右下下下”，即flag{222441144222}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
