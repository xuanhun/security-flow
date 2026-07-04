# GHCTF 2025-upload SSTI!

## Case Metadata

- Category: `Web`
- Platform: `GHCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/GHCTF 2025-upload SSTI!.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/GHCTF%202025-upload%20SSTI%21.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/GHCTF 2025-upload SSTI!.md`
- Challenge URL: `https://www.nssctf.cn/problem/6529`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: Yakit
- Techniques: file-upload, http-analysis, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `web/images/GHCTF 2025-upload SSTI!-filepath.png`
- `web/images/GHCTF 2025-upload SSTI!-code.png`
- `web/images/GHCTF 2025-upload SSTI!-test.png`
- `web/images/GHCTF 2025-upload SSTI!-ls.png`
- `web/images/GHCTF 2025-upload SSTI!-flag.png`

## Solve Thinking

### Step 1: 解题思路

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use Yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: Yakit
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use Yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `成功验证SSTI的存在`

### Step 2: 过程和结果记录

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use Yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: Yakit
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use Yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `{{""[request.args.class][request.args.mro][1][request.args.subclass]()[137][request.args.init][request.args.globals]['popen']('cat /fla\g').read()}}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
