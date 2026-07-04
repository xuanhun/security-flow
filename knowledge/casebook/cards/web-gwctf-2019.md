# GWCTF 2019-你的名字

## Case Metadata

- Category: `Web`
- Platform: `GWCTF 2019`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/GWCTF 2019-你的名字.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/GWCTF%202019-%E4%BD%A0%E7%9A%84%E5%90%8D%E5%AD%97.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/GWCTF 2019-你的名字.md`
- Challenge URL: `https://www.nssctf.cn/problem/259`

## Why This Case Matters

Use this case as a Web reference for ids, web-app challenges.

## Input Signals

- Artifacts: ids, web-app
- Tools: Yakit
- Techniques: http-analysis, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `6`
- `web/images/GWCTF 2019-你的名字-regression.png`
- `web/images/GWCTF 2019-你的名字-error.png`
- `web/images/GWCTF 2019-你的名字-fingerprint.png`
- `web/images/GWCTF 2019-你的名字-fuzz.png`
- `web/images/GWCTF 2019-你的名字-ls.png`
- `web/images/GWCTF 2019-你的名字-flag.png`

## Solve Thinking

### Step 1: 解题思路

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit to collect the smallest evidence slice that answers the goal.
- Tools: Yakit
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `test.php`

### Step 2: 过程和结果记录

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use Yakit to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: Yakit
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use Yakit to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `最终，通过该命令，我们成功列出了环境变量：`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
