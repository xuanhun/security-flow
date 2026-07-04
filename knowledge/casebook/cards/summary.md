# + 未分类

## Case Metadata

- Category: `Web`
- Platform: `SUMMARY.md`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `SUMMARY.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/SUMMARY.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/SUMMARY.md`

## Why This Case Matters

Use this case as a Web reference for apk-mobile, binary, ciphertext challenges.

## Input Signals

- Artifacts: apk-mobile, binary, ciphertext, stego-media, web-app, web-service
- Tools: angr, binwalk, burp, foremost, gdb, ida, netcat, radare2, sqlmap, z3
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, image-analysis, jwt-analysis, misc-analysis, mobile-forensics, php-tricks, reverse-engineering, sql-injection, ssti, stack-overflow, stego-extraction, symbolic-execution, traffic-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use angr, binwalk, burp, foremost with the extracted filter/query `+ [BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==_末 初的博客-CSDN博客](docs/BUUCTF%EF%BC%9A%5BGXYCTF2019%5DSXMgdGhpcyBiYXNlPw%3D%3D_%E6%9C%AB-%E5%88%9D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md)` and inspect the matching evidence.
- Tools: angr, binwalk, burp, foremost, gdb, ida, netcat, radare2, sqlmap, z3
- Filters or commands:
  - `+ [BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==_末 初的博客-CSDN博客](docs/BUUCTF%EF%BC%9A%5BGXYCTF2019%5DSXMgdGhpcyBiYXNlPw%3D%3D_%E6%9C%AB-%E5%88%9D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md)`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use angr, binwalk, burp, foremost with the extracted filter/query `+ [BUUCTF：[GXYCTF2019]SXMgdGhpcyBiYXNlPw==_末 初的博客-CSDN博客](docs/BUUCTF%EF%BC%9A%5BGXYCTF2019%5DSXMgdGhpcyBiYXNlPw%3D%3D_%E6%9C%AB-%E5%88%9D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `98secret.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
