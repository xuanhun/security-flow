# [BUUCTF 2018]Online Tool 题解_偷一个月亮的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF 2018`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[BUUCTF-2018]Online-Tool-题解_偷一个月亮的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BBUUCTF-2018%5DOnline-Tool-%E9%A2%98%E8%A7%A3_%E5%81%B7%E4%B8%80%E4%B8%AA%E6%9C%88%E4%BA%AE%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[BUUCTF-2018]Online-Tool-题解_偷一个月亮的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: netcat, nmap
- Techniques: command-injection, http-analysis, php-tricks, ret2libc, service-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, nmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, nmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: [BUUCTF 2018]Online Tool 题解_偷一个月亮的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat, nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat, nmap
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat, nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `172.17.0.2`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
