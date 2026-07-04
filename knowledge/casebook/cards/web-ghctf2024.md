# [GHCTF 2024 新生赛]理想国

## Case Metadata

- Category: `Web`
- Platform: `GHCTF 2024 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/GHCTF2024新生赛-理想国.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/GHCTF2024%E6%96%B0%E7%94%9F%E8%B5%9B-%E7%90%86%E6%83%B3%E5%9B%BD.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/GHCTF2024新生赛-理想国.md`
- Challenge URL: `https://www.nssctf.cn/problem/5145`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: Yakit, 在线 JWT, cyberchef, netcat
- Techniques: command-injection, crypto-analysis, http-analysis, jwt-analysis, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `web/images/GHCTF2024新生赛-理想国-yakit-register.png`
- `web/images/GHCTF2024新生赛-理想国-yakit-login.png`
- `web/images/GHCTF2024新生赛-理想国-yakit-search-passwd.png`
- `web/images/GHCTF2024新生赛-理想国-Fake-JWT.png`
- `web/images/GHCTF2024新生赛-理想国-backdoor.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, 在线 JWT, cyberchef, netcat to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, 在线 JWT, cyberchef, netcat
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, 在线 JWT, cyberchef, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, 在线 JWT, cyberchef, netcat to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, 在线 JWT, cyberchef, netcat
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, 在线 JWT, cyberchef, netcat to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 尝试过程和结果记录

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use yakit with the extracted filter/query `python app.py` and inspect the matching evidence.
- Tools: yakit
- Filters or commands:
  - `python app.py`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use yakit with the extracted filter/query `python app.py` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `A035C8C19219BA821ECEA86B64E628F8D684696D`

### Step 4: coding=gbk

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use cyberchef, netcat with the extracted filter/query `payload['username'] == "Plato" and payload['password'] == "ideal_state"` and inspect the matching evidence.
- Tools: cyberchef, netcat
- Filters or commands:
  - `payload['username'] == "Plato" and payload['password'] == "ideal_state"`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use cyberchef, netcat with the extracted filter/query `payload['username'] == "Plato" and payload['password'] == "ideal_state"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0`

### Step 5: CyberChef

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use cyberchef to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `在本地备份一份源码，直接点击即可在浏览器打开。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
