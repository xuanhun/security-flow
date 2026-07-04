# [NSSRound#30 Duo]你也是迷宫高手吗

## Case Metadata

- Category: `Web`
- Platform: `NSSRound#30 Duo`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[NSSRound#30 Duo]你也是迷宫高手吗 .md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BNSSRound%2330%20Duo%5D%E4%BD%A0%E4%B9%9F%E6%98%AF%E8%BF%B7%E5%AE%AB%E9%AB%98%E6%89%8B%E5%90%97%20.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[NSSRound#30 Duo]你也是迷宫高手吗 .md`
- Challenge URL: `https://www.nssctf.cn/problem/6675`

## Why This Case Matters

Use this case as a Web reference for ids, web-app challenges.

## Input Signals

- Artifacts: ids, web-app
- Tools: python环境, flask-unsign, netcat
- Techniques: binary-exploitation, command-injection, crypto-analysis, http-analysis, jwt-analysis, password-cracking, ret2libc, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `4`
- `web/images/0528wp_flask.png`
- `web/images/0528wp_cookie.png`
- `web/images/0528wp_jwt1.png`
- `web/images/0528wp_flag.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `python环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
- Tools: python环境, flask-unsign, netcat
- Reasoning chain:
  - Recognize the section as python环境-driven evidence lookup.
  - Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `进入看到一个迷宫游戏界面，同时可以看到服务是由flask起的`

### Step 2: 想到什么解题思路

- Route type: `python环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
- Tools: python环境, flask-unsign, netcat
- Reasoning chain:
  - Recognize the section as python环境-driven evidence lookup.
  - Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `想到编写脚本过关或者前端找到过关条件`

### Step 3: 尝试过程和结果记录

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `import time`

### Step 4: 目标网址

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use python环境, flask-unsign, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: python环境, flask-unsign, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use python环境, flask-unsign, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `url = "http://node7.anna.nssctf.cn:29809/"`

### Step 5: 已知密钥

- Route type: `python环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
- Tools: python环境, flask-unsign, netcat
- Reasoning chain:
  - Recognize the section as python环境-driven evidence lookup.
  - Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `secret = "supersecretkey"`

### Step 6: 构造 payload

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use python环境, flask-unsign, netcat to align timestamps and identify the event that satisfies the question.
- Tools: python环境, flask-unsign, netcat
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use python环境, flask-unsign, netcat to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `}`

### Step 7: 签名生成新的 session cookie

- Route type: `python环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
- Tools: python环境, flask-unsign, netcat
- Reasoning chain:
  - Recognize the section as python环境-driven evidence lookup.
  - Use python环境, flask-unsign, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cookie = flask_unsign.sign(payload, secret=secret)`

### Step 8: 设置 cookie 并访问目标页面

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use python环境, flask-unsign, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: python环境, flask-unsign, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use python环境, flask-unsign, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `os.system('flask-unsign --sign --cookie "{}" --secret "{}"'.format(e_cookie, secret))`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
