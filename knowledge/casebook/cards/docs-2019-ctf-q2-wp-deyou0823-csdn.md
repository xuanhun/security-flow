# 2019看雪CTF 晋级赛Q2第四题wp_deyou0823的博客-CSDN博客

## Case Metadata

- Category: `Training and Meta`
- Platform: `2019看雪CTF 晋级赛Q2第四题wp`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2019看雪CTF-晋级赛Q2第四题wp_deyou0823的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2019%E7%9C%8B%E9%9B%AACTF-%E6%99%8B%E7%BA%A7%E8%B5%9BQ2%E7%AC%AC%E5%9B%9B%E9%A2%98wp_deyou0823%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2019看雪CTF-晋级赛Q2第四题wp_deyou0823的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Training and Meta reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: radare2
- Techniques: classical-crypto, encoding-analysis, http-analysis, integer-overflow, qr-analysis, web-exploitation

## First-Principles Route

- Treat the document as study guidance: extract challenge taxonomy, workflow rules, tool references, and reusable habits.
- Record platform names, topic tags, and tool examples so later queries can reach the right note quickly.
- Prefer compact summaries that preserve lookup value over full-text duplication.

## Solve Thinking

### Step 1: Document

- Route type: `radare2-driven evidence lookup`
- Why: For Training and Meta, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use radare2 to collect the smallest evidence slice that answers the goal.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as radare2-driven evidence lookup.
  - Use radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2019看雪CTF 晋级赛Q2第四题wp_deyou0823的博客-CSDN博客

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use radare2 with the extracted filter/query `106 { 107 if ( x[v4] ) // x[7]!=0` and inspect the matching evidence.
- Tools: radare2
- Filters or commands:
  - `106 { 107 if ( x[v4] ) // x[7]!=0`
  - `108 break; 109 --v3; 110 --v4; 111 } 112 while ( v4 >= 0 ); 113 if ( v3 == 8 ) 114 { 115 low_index = 7; 116 do`
  - `117 { 118 if ( y[low_index] ) // y[7]!=0`
  - `124 if ( v3 == 8 && !(x[7] & 0xF0) ) // 第8位<0x10`
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use radare2 with the extracted filter/query `106 { 107 if ( x[v4] ) // x[7]!=0` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `复制这段内容后打开百度网盘手机App，操作更方便哦`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
