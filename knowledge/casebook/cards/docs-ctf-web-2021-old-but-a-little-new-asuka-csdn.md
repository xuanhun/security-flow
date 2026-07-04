# CTF_Web：长安杯-2021 Old But A Little New & asuka题解_星辰照耀你我的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF_Web：长安杯-2021-Old-But-A-Little-New-&-asuka题解_星辰照耀你我的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF_Web%EF%BC%9A%E9%95%BF%E5%AE%89%E6%9D%AF-2021-Old-But-A-Little-New-%26-asuka%E9%A2%98%E8%A7%A3_%E6%98%9F%E8%BE%B0%E7%85%A7%E8%80%80%E4%BD%A0%E6%88%91%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF_Web：长安杯-2021-Old-But-A-Little-New-&-asuka题解_星辰照耀你我的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: not detected
- Techniques: command-injection, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `6`
- `docs/img/eda7dc6c6485446721d8347a690f5caf.png`
- `docs/img/b7ab186cca0a32f35cf063e45ba91643.png`
- `docs/img/db1043b9079de767f25c77258a86232c.png`
- `docs/img/200dd67aec4ce380c789758d89fa78b7.png`
- `docs/img/9a27499eb76e0e913d840cf006b1c4ed.png`
- `docs/img/6460d9e8da3a20437f2f0f7ec2972cce.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF_Web：长安杯-2021 Old But A Little New & asuka题解_星辰照耀你我的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_35493457/article/details/120470858](https://blog.csdn.net/qq_35493457/article/details/120470858)`

### Step 3: 0x00 Old But A Little New

- Route type: `evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `eda7dc6c6485446721d8347a690f5caf`

### Step 4: 0x01 弱口令登录

- Route type: `evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b7ab186cca0a32f35cf063e45ba91643`

### Step 5: 0x02 上传war包getshell

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `while((a=in.read(b))!=-1){` and inspect the matching evidence.
- Filters or commands:
  - `while((a=in.read(b))!=-1){`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `while((a=in.read(b))!=-1){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `200dd67aec4ce380c789758d89fa78b7`

### Step 6: 0x03 asuka

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6460d9e8da3a20437f2f0f7ec2972cce`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
