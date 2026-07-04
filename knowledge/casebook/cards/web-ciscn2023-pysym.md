# [CISCN 2023 华北]pysym

## Case Metadata

- Category: `Web`
- Platform: `CISCN 2023 华北`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/CISCN2023华北-pysym.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/CISCN2023%E5%8D%8E%E5%8C%97-pysym.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/CISCN2023华北-pysym.md`
- Challenge URL: `https://www.nssctf.cn/problem/4098`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: Yakit, netcat
- Techniques: classical-crypto, command-injection, encoding-analysis, http-analysis, php-tricks, ret2libc, sql-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `4`
- `web/images/CISCN2019华北-pysym-sleep-5.png`
- `web/images/CISCN2019华北-pysym-base64-sleep.png`
- `web/images/CISCN2019华北-pysym-guess.png`
- `web/images/CISCN2019华北-pysym-burp.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, netcat to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, netcat
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use Yakit, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: Yakit, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use Yakit, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - The proof is the returned command output or filesystem effect from the injected command.
- Evidence rule: The proof is the returned command output or filesystem effect from the injected command.

### Step 3: 尝试过程和结果记录

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, netcat with the extracted filter/query `Content-Disposition: form-data; name="file"; filename="1.txt || echo {{base64enc(bash -i -c '[ "$(head -c 1 /flag)" == "{{rangechar(20,7E)}}" ] && sleep 5')}} | base64 -d | bash ||"` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `Content-Disposition: form-data; name="file"; filename="1.txt || echo {{base64enc(bash -i -c '[ "$(head -c 1 /flag)" == "{{rangechar(20,7E)}}" ] && sleep 5')}} | base64 -d | bash ||"`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, netcat with the extracted filter/query `Content-Disposition: form-data; name="file"; filename="1.txt || echo {{base64enc(bash -i -c '[ "$(head -c 1 /flag)" == "{{rangechar(20,7E)}}" ] && sleep 5')}} | base64 -d | bash ||"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `把延迟超过5000ms的响应包按照发包顺序组装payload即可获得最终flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
