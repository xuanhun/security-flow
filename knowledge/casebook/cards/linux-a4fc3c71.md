# 第一章 应急响应-Linux日志分析 · 玄机 - EDISEC https://xj.edisec.net/challenges/24

## Case Metadata

- Category: `Incident Response`
- Platform: `第一章 应急响应`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `应急响应/应急响应-Linux日志分析.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94-Linux%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/应急响应/应急响应-Linux日志分析.md`

## Why This Case Matters

Use this case as a Incident Response reference for linux-logs, web-app challenges.

## Input Signals

- Artifacts: linux-logs, web-app
- Tools: not detected
- Techniques: http-analysis, service-enumeration, web-exploitation

## First-Principles Route

- Anchor the case in the supplied host, log, or traffic artifact and build a time-bounded incident narrative.
- Correlate users, processes, files, timestamps, and network indicators before trusting any single log line.
- Preserve the exact log field or recovered artifact that proves each conclusion.

## Linked Assets

- Referenced assets: `6`
- `应急响应/images/3-26wp_logs.png`
- `应急响应/images/3-26wp_authlog.png`
- `应急响应/images/3-26wp_get_failed_ip.png`
- `应急响应/images/3-26wp_get_success_flag.png`
- `应急响应/images/3-26wp_get_user.png`
- `应急响应/images/3-26wp_add_user.png`

## Solve Thinking

### Step 1: 第一章 应急响应-Linux日志分析 · 玄机 - EDISEC https://xj.edisec.net/challenges/24

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use the artifact-specific tool to anchor the event in time, user, host, and file/process context before answering.
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use the artifact-specific tool to anchor the event in time, user, host, and file/process context before answering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `>5.黑客登陆主机后新建了一个后门用户，用户名是多少**`

### Step 2: 有多少IP在爆破主机ssh的root帐号，如果有多个使用","分割

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use the artifact-specific tool with the extracted filter/query `| 日志文件 | 说明 |` and inspect the matching evidence.
- Filters or commands:
  - `| 日志文件 | 说明 |`
  - `|:-------------:|:--------------------------------------:|`
  - `| auth.log | 记录系统认证相关信息，如用户登录、sudo使用等 |`
  - `| auth.log.1 | auth.log的历史归档日志 |`
  - `| btmp | 记录失败的登录尝试，二进制文件，用`lastb`命令查看 |`
  - `| lastlog | 记录所有用户最近一次登录时间，二进制文件 |`
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use the artifact-specific tool with the extracted filter/query `| 日志文件 | 说明 |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ````bash`

### Step 3: ssh爆破成功登陆的IP是多少，如果有多个使用","分割

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep -a "Accepted " auth.log.1 | awk '{print $11}' | uniq -c` and inspect the matching evidence.
- Filters or commands:
  - `grep -a "Accepted " auth.log.1 | awk '{print $11}' | uniq -c`
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use the artifact-specific tool with the extracted filter/query `grep -a "Accepted " auth.log.1 | awk '{print $11}' | uniq -c` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ````bash`

### Step 4: 爆破用户名字典是什么？如果有多个使用","分割

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep --binary-files=text -Eo 'Invalid user [^ ]+|user=[^ ]+' auth.log.1 | sed -E 's/Invalid user //;s/user=//' | sort -u` and inspect the matching evidence.
- Filters or commands:
  - `grep --binary-files=text -Eo 'Invalid user [^ ]+|user=[^ ]+' auth.log.1 | sed -E 's/Invalid user //;s/user=//' | sort -u`
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use the artifact-specific tool with the extracted filter/query `grep --binary-files=text -Eo 'Invalid user [^ ]+|user=[^ ]+' auth.log.1 | sed -E 's/Invalid user //;s/user=//' | sort -u` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 5: 登陆成功的IP共爆破了多少次

- Route type: `evidence lookup`
- Why: For Incident Response, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `从1里我们也可以看出来是4次，所以flag是4（虽然其实我用别的命令得出总的尝试登陆次数比4次多，但是答案是4次，我也很疑惑，可能是因为这里要得的是爆破root登陆次数且失败的？）`

### Step 6: 黑客登陆主机后新建了一个后门用户，用户名是多少

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use the artifact-specific tool with the extracted filter/query `grep --binary-files=text -oP 'new user: name=\K[^,]+' auth.log.1 | head -n1` and inspect the matching evidence.
- Filters or commands:
  - `grep --binary-files=text -oP 'new user: name=\K[^,]+' auth.log.1 | head -n1`
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use the artifact-specific tool with the extracted filter/query `grep --binary-files=text -oP 'new user: name=\K[^,]+' auth.log.1 | head -n1` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
