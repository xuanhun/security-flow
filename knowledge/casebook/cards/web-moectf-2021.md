# [MoeCTF 2021]地狱通讯-改

## Case Metadata

- Category: `Web`
- Platform: `MoeCTF 2021`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[MoeCTF 2021]地狱通讯-改.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BMoeCTF%202021%5D%E5%9C%B0%E7%8B%B1%E9%80%9A%E8%AE%AF-%E6%94%B9.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[MoeCTF 2021]地狱通讯-改.md`
- Challenge URL: `https://www.nssctf.cn/problem/3397`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: python环境
- Techniques: crypto-analysis, format-string, http-analysis, jwt-analysis, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `7`
- `web/images/0528wp_get_jwt.png`
- `web/images/0528wp_jwt_de.png`
- `web/images/0528wp_hello1.png`
- `web/images/0528wp_hello2.png`
- `web/images/0528wp_secret_leak.png`
- `web/images/0528wp_change_jwt.png`
- `web/images/0528wp_flag-1.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use python环境 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: python环境
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use python环境 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `进入靶机后看到flask的源码，发现需要伪造属于admin的jwt才能获得flag`

### Step 2: 想到什么解题思路

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use python环境 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: python环境
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use python环境 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `代码审计后根据代码逻辑获取jwt后修改user为“name”`

### Step 3: 尝试过程和结果记录

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use python环境 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: python环境
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use python环境 to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `然后发送修改后的jwt获得flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
