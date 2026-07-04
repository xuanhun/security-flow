# SWPU 2024 新生引导-ez_SSTI

## Case Metadata

- Category: `Web`
- Platform: `SWPU 2024 新生引导`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/SWPU 2024 新生引导-ez_SSTI.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/SWPU%202024%20%E6%96%B0%E7%94%9F%E5%BC%95%E5%AF%BC-ez_SSTI.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/SWPU 2024 新生引导-ez_SSTI.md`
- Challenge URL: `https://www.nssctf.cn/problem/5808`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: Fenjing
- Techniques: http-analysis, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `web/images/SWPU 2024 新生引导-ez_SSTI-test.png`
- `web/images/SWPU 2024 新生引导-ez_SSTI-fenjing.png`

## Solve Thinking

### Step 1: 解题思路

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use Fenjing to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: Fenjing
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use Fenjing to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `此外，题目中特别提到了 `fenjing` 这个工具，这表明我们可以借助 `fenjing` 来分析和利用 SSTI 漏洞。`

### Step 2: 过程和结果记录

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use Fenjing to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: Fenjing
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use Fenjing to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `通过 `fenjing` 的自动化分析，我们成功识别了 SSTI 漏洞，并利用该工具执行了相应的 payload，最终成功获取 flag。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
