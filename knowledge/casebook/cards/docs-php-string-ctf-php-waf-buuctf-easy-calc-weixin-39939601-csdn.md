# php string ctf,PHP字符解析特性绕WAF【buuctf题 easy calc】_weixin_39939601的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `php string ctf`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/php-string-ctf,PHP字符解析特性绕WAF【buuctf题-easy-calc】_weixin_39939601的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/php-string-ctf%2CPHP%E5%AD%97%E7%AC%A6%E8%A7%A3%E6%9E%90%E7%89%B9%E6%80%A7%E7%BB%95WAF%E3%80%90buuctf%E9%A2%98-easy-calc%E3%80%91_weixin_39939601%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/php-string-ctf,PHP字符解析特性绕WAF【buuctf题-easy-calc】_weixin_39939601的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: not detected
- Techniques: encoding-analysis, http-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `8`
- `docs/img/9ce08465322fea3000beafd453f45764.png`
- `docs/img/2b2457508f99b8b0ad1a5f0e0e67873b.png`
- `docs/img/65818d11e1a5a05511aad8aa0aab8d5e.png`
- `docs/img/8ee93595e689c95eaf1e74e4e4d9846f.png`
- `docs/img/000e744415fa03528f49854bc2d73bbc.png`
- `docs/img/434e8f03863c257d2f4aebd75dda00a7.png`
- `docs/img/7a09313e7fd6efa09b0a23b6bfcc41ef.png`
- `docs/img/79306ffcda69edfcc9b16932211d48e2.png`

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

### Step 2: php string ctf,PHP字符解析特性绕WAF【buuctf题 easy calc】_weixin_39939601的博客-CSDN博客

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use the artifact-specific tool to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use the artifact-specific tool to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d94dbddc0a45a49bb399c0615192112f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
