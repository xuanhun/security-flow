# SUCTF_2019部分题解复现_FFM-G的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `SUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/SUCTF_2019部分题解复现_FFM-G的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/SUCTF_2019%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3%E5%A4%8D%E7%8E%B0_FFM-G%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/SUCTF_2019部分题解复现_FFM-G的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: browser-forensics, classical-crypto, command-injection, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `13`
- `docs/img/a05e9a68899dbf0b96af103e0a99ee4a.png`
- `docs/img/2e1c107b74a842254e19ba30a198eca6.png`
- `docs/img/37d3d125c32fec47a3ed1f3ff9388a64.png`
- `docs/img/15f5fd05321030599f5a6dda447b0402.png`
- `docs/img/edeb115a4e9babb78a0a1ca71a745a32.png`
- `docs/img/6cbaedf10d07d80af090fa70eda3608a.png`
- `docs/img/bfb0139feb14afec1ff6a84ad9289fd0.png`
- `docs/img/03189e484725cee18b2b1b4df4027e5d.png`
- `docs/img/4e1f63e19ee82c120900364b384abb56.png`
- `docs/img/8158bd0454db63f0524d57135c9166f9.png`
- `docs/img/8fff9d37e2a36f6e23fceca3470e2d98.png`
- `docs/img/3c290da2d0049420a68c5b046f4705d2.png`
- ... and `1` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: SUCTF_2019部分题解复现_FFM-G的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `本次比赛还是太菜了，只写出了两道题。但是学习到了很多东西。`

### Step 3: check

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a05e9a68899dbf0b96af103e0a99ee4a`

### Step 4: easyphp

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if(mb_strpos(file_get_contents($tmp_name), '<?')!==False) die("^_^");` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if(mb_strpos(file_get_contents($tmp_name), '<?')!==False) die("^_^");`
  - `if ( preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $hhh) )`
  - `发现这个正则太变态了`if ( preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i’, $hhh) )`过滤了字母，数字，下划线以及其他的符号。`
  - `if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {`
  - `if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $t) == 0) {`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `if(mb_strpos(file_get_contents($tmp_name), '<?')!==False) die("^_^");` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `47.111.59.243:9001`

### Step 5: pythonginx

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8158bd0454db63f0524d57135c9166f9`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
