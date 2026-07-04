# BUUCTF__[RoarCTF 2019]Easy Calc_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[RoarCTF-2019]Easy-Calc_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5BRoarCTF-2019%5DEasy-Calc_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[RoarCTF-2019]Easy-Calc_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy
- Techniques: command-injection, http-analysis, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/403fa56e50615e0dcd0c88f201dae220.png`
- `docs/img/9b48c041b099cb812009ac8ce202973d.png`
- `docs/img/956bd456fd042ef8d7457fe58edef1f1.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF__[RoarCTF 2019]Easy Calc_题解_风过江南乱的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/TM_1024/article/details/106061191](https://blog.csdn.net/TM_1024/article/details/106061191)`

### Step 3: 看题

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use detect-it-easy to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use detect-it-easy to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `403fa56e50615e0dcd0c88f201dae220`

### Step 4: 研究

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f1agg.php`

### Step 5: 解题

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `956bd456fd042ef8d7457fe58edef1f1`

### Step 6: 最后

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 欢迎来访个人博客 http://ctf-web.zm996.cloud/`

### Step 7: 扩展

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 这里就不说了，可自行了解。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
