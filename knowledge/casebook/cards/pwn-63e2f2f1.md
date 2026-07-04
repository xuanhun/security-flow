# [SWPUCTF 2024 秋季新生赛]又是签到！？

## Case Metadata

- Category: `Pwn`
- Platform: `SWPUCTF 2024 秋季新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `pwn/又是签到！？.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/pwn/%E5%8F%88%E6%98%AF%E7%AD%BE%E5%88%B0%EF%BC%81%EF%BC%9F.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/pwn/又是签到！？.md`
- Challenge URL: `https://www.nssctf.cn/problem/5934`

## Why This Case Matters

Use this case as a Pwn reference for apk-mobile, binary, web-app challenges.

## Input Signals

- Artifacts: apk-mobile, binary, web-app
- Tools: jadx
- Techniques: binary-exploitation, http-analysis, mobile-forensics, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `6`
- `pwn/images/SWPUCTF_2024_秋季新生赛又是签到！？-apk.png`
- `pwn/images/SWPUCTF_2024_秋季新生赛又是签到！？-jadx_1.png`
- `pwn/images/SWPUCTF_2024_秋季新生赛又是签到！？-jadx_2.png`
- `pwn/images/SWPUCTF_2024_秋季新生赛又是签到！？-jadx_3.png`
- `pwn/images/SWPUCTF_2024_秋季新生赛又是签到！？-jadx_4.png`
- `pwn/images/SWPUCTF_2024_秋季新生赛又是签到！？-flag.png`

## Solve Thinking

### Step 1: 第一轮

- Route type: `jadx-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use jadx to collect the smallest evidence slice that answers the goal.
- Tools: jadx
- Reasoning chain:
  - Recognize the section as jadx-driven evidence lookup.
  - Use jadx to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 2: 第一轮

- Route type: `jadx-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use jadx to collect the smallest evidence slice that answers the goal.
- Tools: jadx
- Reasoning chain:
  - Recognize the section as jadx-driven evidence lookup.
  - Use jadx to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 第二轮

- Route type: `jadx-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use jadx to collect the smallest evidence slice that answers the goal.
- Tools: jadx
- Reasoning chain:
  - Recognize the section as jadx-driven evidence lookup.
  - Use jadx to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 4: 第一轮

- Route type: `jadx-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use jadx to collect the smallest evidence slice that answers the goal.
- Tools: jadx
- Reasoning chain:
  - Recognize the section as jadx-driven evidence lookup.
  - Use jadx to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: 第二轮

- Route type: `jadx-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use jadx to collect the smallest evidence slice that answers the goal.
- Tools: jadx
- Reasoning chain:
  - Recognize the section as jadx-driven evidence lookup.
  - Use jadx to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 6: 第三轮

- Route type: `jadx-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use jadx to collect the smallest evidence slice that answers the goal.
- Tools: jadx
- Reasoning chain:
  - Recognize the section as jadx-driven evidence lookup.
  - Use jadx to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `成功找到flag信息`

### Step 7: jadx

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: jadx
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use jadx to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://github.com/skylot/jadx/releases/tag/v1.5.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
