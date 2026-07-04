# [GKCTF 2020]老八小超市儿

## Case Metadata

- Category: `Web`
- Platform: `GKCTF 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[GKCTF 2020]老八小超市儿.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BGKCTF%202020%5D%E8%80%81%E5%85%AB%E5%B0%8F%E8%B6%85%E5%B8%82%E5%84%BF.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[GKCTF 2020]老八小超市儿.md`
- Challenge URL: `https://www.nssctf.cn/problem/1302`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: 无
- Techniques: command-injection, http-analysis, misc-analysis, ret2libc, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `7`
- `web/images/[GKCTF 2020]老八小超市儿-主题管理.png`
- `web/images/[GKCTF 2020]老八小超市儿-免费主题.png`
- `web/images/[GKCTF 2020]老八小超市儿-目录结构.png`
- `web/images/[GKCTF 2020]老八小超市儿-主题路径.png`
- `web/images/[GKCTF 2020]老八小超市儿-访问php文件.png`
- `web/images/[GKCTF 2020]老八小超市儿-假flag.png`
- `web/images/[GKCTF 2020]老八小超市儿-flag.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `无-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无 to collect the smallest evidence slice that answers the goal.
- Tools: 无
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `无-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 无 to collect the smallest evidence slice that answers the goal.
- Tools: 无
- Reasoning chain:
  - Recognize the section as 无-driven evidence lookup.
  - Use 无 to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 尝试过程和结果记录

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use 无 to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: 无
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use 无 to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `admin.php`

### Step 4: os.system("cat /root/flag>/1.txt")

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use 无 to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: 无
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use 无 to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
