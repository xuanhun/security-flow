# php ctf题解,国际赛-N1CTF 2018-Web题解_无敌小羊历险记的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `php ctf题解,国际赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/php-ctf题解,国际赛-N1CTF-2018-Web题解_无敌小羊历险记的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/php-ctf%E9%A2%98%E8%A7%A3%2C%E5%9B%BD%E9%99%85%E8%B5%9B-N1CTF-2018-Web%E9%A2%98%E8%A7%A3_%E6%97%A0%E6%95%8C%E5%B0%8F%E7%BE%8A%E5%8E%86%E9%99%A9%E8%AE%B0%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/php-ctf题解,国际赛-N1CTF-2018-Web题解_无敌小羊历险记的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, ret2libc, sql-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `docs/img/6256d70fdd00460a0ab9d591b1327f69.png`

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

### Step 2: php ctf题解,国际赛-N1CTF 2018-Web题解_无敌小羊历险记的博客-CSDN博客

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if "| 10` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if "| 10`
  - `if "| 11`
  - `if (FLAG_SIG != 1){`
  - `$picdata = system("cat ./upload_b3bb2cfed6371dfeb2db1dbcceb124d3/".$filename." | base64 -w 0");`
  - `jpg || ls 文件名`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `if "| 10` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `47.52.137.90:20000`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
