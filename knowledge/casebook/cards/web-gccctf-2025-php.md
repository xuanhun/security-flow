# PHP签到

## Case Metadata

- Category: `Web`
- Platform: `GCCCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[GCCCTF 2025]PHP签到.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BGCCCTF%202025%5DPHP%E7%AD%BE%E5%88%B0.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[GCCCTF 2025]PHP签到.md`
- Challenge URL: `[[GCCCTF 2025]PHP签到 | NSSCTF](https://www.nssctf.cn/problem/7167)`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: 解题思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `if (strpos($xff, '127.0.0.1') === false && strpos($xff, '::1') === false) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (strpos($xff, '127.0.0.1') === false && strpos($xff, '::1') === false) {`
  - `if (base64_decode($nonce) === false || !preg_match('/^[A-Za-z0-9+\/=]+$/', $nonce)) {`
  - `if (strpos($user, 'admin') == false) {`
  - `if (substr($mac, 0, 6) == substr($sig, 0, 6)) {`
  - `if (md5($token) == $stored_hash) {`
  - `如果 `user` **不包含**字符串 `"admin"`（注意是 `strpos(...) == false`，即找不到），则进入验证流程：`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `if (strpos($xff, '127.0.0.1') === false && strpos($xff, '::1') === false) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1:8080`

### Step 2: 计算 HMAC-MD5(user + token + ts, key)，取前6位

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `127.0.0.1`

### Step 3: 不发送 authkey cookie，让服务端使用默认 'NULL'

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `main()`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
