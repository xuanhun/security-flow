# 2018 SCUCTF web题：cat？非常规题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `2018 SCUCTF web题：cat？非常规题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2018-SCUCTF-web题：cat？非常规题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2018-SCUCTF-web%E9%A2%98%EF%BC%9Acat%EF%BC%9F%E9%9D%9E%E5%B8%B8%E8%A7%84%E9%A2%98%E8%A7%A3_%E4%B8%9C%E5%9D%A1%E4%BD%95%E7%BD%AA%E5%8F%91%E6%96%87%E7%AB%A0%E6%80%BB%E6%98%AF%E5%AE%A1%E6%A0%B8%E4%B8%8D%E9%80%9A%E8%BF%87%EF%BC%8C%E5%8E%BB%E5%8D%9A%E5%AE%A2%E5%9B%AD%E4%BA%86%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2018-SCUCTF-web题：cat？非常规题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2018 SCUCTF web题：cat？非常规题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/perfect0066/article/details/85108416](https://blog.csdn.net/perfect0066/article/details/85108416)`

### Step 3: 主要思路

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4.在服务器使用 **"nc -lnvp 相应端口"**`

### Step 4: python脚本如下

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `'>\|\\']` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `'>\|\\']`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `'>\|\\']` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `120.78.66.77:87`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
