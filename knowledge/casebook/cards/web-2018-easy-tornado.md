# 护网杯 2018-easy_tornado

## Case Metadata

- Category: `Web`
- Platform: `护网杯 2018`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/护网杯 2018-easy_tornado.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%E6%8A%A4%E7%BD%91%E6%9D%AF%202018-easy_tornado.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/护网杯 2018-easy_tornado.md`
- Challenge URL: `https://www.nssctf.cn/problem/175`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: Yakit
- Techniques: http-analysis, php-tricks, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `4`
- `web/images/护网杯 2018-easy_tornado-dir.png`
- `web/images/护网杯 2018-easy_tornado-get-env.png`
- `web/images/护网杯 2018-easy_tornado-hash.png`
- `web/images/护网杯 2018-easy_tornado-flag.png`

## Solve Thinking

### Step 1: 解题思路

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: Yakit
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `我们知道了flag文件的filename，现在需要获得cookie_secret`

### Step 2: 过程和结果记录

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use Yakit to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: Yakit
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use Yakit to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `将获得的hash值填入url中，即可得到flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
