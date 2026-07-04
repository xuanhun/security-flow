# MISC

## Case Metadata

- Category: `Training and Meta`
- Platform: `tools.md`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `tools.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/tools.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/tools.md`

## Why This Case Matters

Use this case as a Training and Meta reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: cyberchef, netcat
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, misc-analysis, osint, sql-injection, ssti, web-exploitation

## First-Principles Route

- Treat the document as study guidance: extract challenge taxonomy, workflow rules, tool references, and reusable habits.
- Record platform names, topic tags, and tool examples so later queries can reach the right note quickly.
- Prefer compact summaries that preserve lookup value over full-text duplication.

## Solve Thinking

### Step 1: 编解码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use cyberchef to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: cyberchef
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use cyberchef to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [misc/tools/base-crack.py](misc/tools/base-crack.py) 无关字符过滤，套娃解码，迭代解码`

### Step 2: 压缩包

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- [X] 本地通过 `cargo` 安装，命令行全局可用`

### Step 3: Web

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use sqlmap, yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: sqlmap, yakit
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use sqlmap, yakit to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [X] 本地图形化界面已安装`

### Step 4: debug

- Route type: `cyberchef-driven evidence lookup`
- Why: For Training and Meta, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use cyberchef, netcat to collect the smallest evidence slice that answers the goal.
- Tools: cyberchef, netcat
- Reasoning chain:
  - Recognize the section as cyberchef-driven evidence lookup.
  - Use cyberchef, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [pgsql + adminer](stats/docker-compose.yml)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
