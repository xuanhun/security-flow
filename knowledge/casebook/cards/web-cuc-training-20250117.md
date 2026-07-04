# 17 题解

## Case Metadata

- Category: `Web`
- Platform: `cuc`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/cuc_training_20250117.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/cuc_training_20250117.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/cuc_training_20250117.md`

## Why This Case Matters

Use this case as a Web reference for binary, pe-malware, web-app challenges.

## Input Signals

- Artifacts: binary, pe-malware, web-app
- Tools: capa, sqlmap, yakit
- Techniques: http-analysis, malware-static, sql-injection, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: [MoeCTF 2022]Sqlmap_boy

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 2: conda activate pentest

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use sqlmap with the extracted filter/query `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' -c 'PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a'` and inspect the matching evidence.
- Tools: sqlmap
- Filters or commands:
  - `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' -c 'PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a'`
  - `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' --cookie='PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a'`
  - `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' --cookie='PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a' --dbs`
  - `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' --cookie='PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a' --tables -D moectf`
  - `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' --cookie='PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a' -D moectf -T flag --columns`
  - `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' --cookie='PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a' -D moectf -T flag -C flAg --dump`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use sqlmap with the extracted filter/query `sqlmap -u 'http://node5.anna.nssctf.cn:21540/secrets.php?id=2' -c 'PHPSESSID=43f72e5a89d64eaa9f7e4af07fe6ef1a'` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `43f72e5a89d64eaa9f7e4af07fe6ef1a`

### Step 3: hack:admin123

- Route type: `capa-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use capa, sqlmap, yakit to collect the smallest evidence slice that answers the goal.
- Tools: capa, sqlmap, yakit
- Reasoning chain:
  - Recognize the section as capa-driven evidence lookup.
  - Use capa, sqlmap, yakit to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: [HDCTF 2023]LoginMaster

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use capa, sqlmap, yakit to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: capa, sqlmap, yakit
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use capa, sqlmap, yakit to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[hdctf2023-loginmaster.md](hdctf2023-loginmaster.md)`

### Step 5: [第五空间 2021]yet_another_mysql_injection

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use capa, sqlmap, yakit to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: capa, sqlmap, yakit
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use capa, sqlmap, yakit to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[第五空间2021-yet_another_mysql_injection.md](第五空间2021-yet_another_mysql_injection.md)`

### Step 6: [LitCTF 2024]一个....池子？

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: yakit
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 7: ref: https://github.com/vladko312/SSTImap

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use capa, yakit with the extracted filter/query `python sstimap.py -u http://node4.anna.nssctf.cn:28633/echo -d input=1 --os-shell` and inspect the matching evidence.
- Tools: capa, yakit
- Filters or commands:
  - `python sstimap.py -u http://node4.anna.nssctf.cn:28633/echo -d input=1 --os-shell`
  - `╚════╗ ╠════╗ ║ ║ ║ ║*║ | '_ ` _ \ / _` | '_ \`
  - `╔════╝ ╠════╝ ║ ║ ║ ║}║ | | | | | | (_| | |_) |`
  - `╚══════╩══════╝ ╚═╝ ╚╦╝ |_| |_| |_|\__,_| .__/`
  - `│ | |`
  - `|_|`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use capa, yakit with the extracted filter/query `python sstimap.py -u http://node4.anna.nssctf.cn:28633/echo -d input=1 --os-shell` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 另一个 3.8k 的 SSTI 工具 https://github.com/epinna/tplmap 还没有测试`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
