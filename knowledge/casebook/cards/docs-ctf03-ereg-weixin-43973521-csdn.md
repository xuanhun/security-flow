# 四叶草云演-CTF03# ereg_weixin_43973521的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `四叶草云演`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/四叶草云演-CTF03#-ereg_weixin_43973521的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%9B%9B%E5%8F%B6%E8%8D%89%E4%BA%91%E6%BC%94-CTF03%23-ereg_weixin_43973521%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/四叶草云演-CTF03#-ereg_weixin_43973521的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy
- Techniques: waf-bypass

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `docs/img/8d3976e4e3f152f0ffcbf52054ec1025.png`

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

### Step 2: 四叶草云演-CTF03# ereg_weixin_43973521的博客-CSDN博客

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `> * ereg函数存在NULL截断漏洞，导致了正则过滤被绕过,所以可以使用%00截断正则匹配`

### Step 3: 题解：

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use detect-it-easy with the extracted filter/query `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)`
  - `if (strpos ($_GET['password'], '*-*') !== FALSE)`
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use detect-it-easy with the extracted filter/query `if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `**得到**Flag: flag{this_is_flag}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
