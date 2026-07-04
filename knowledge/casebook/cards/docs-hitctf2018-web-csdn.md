# HITCTF2018-web全题解_合天网安实验室的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `HITCTF2018`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/HITCTF2018-web全题解_合天网安实验室的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/HITCTF2018-web%E5%85%A8%E9%A2%98%E8%A7%A3_%E5%90%88%E5%A4%A9%E7%BD%91%E5%AE%89%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/HITCTF2018-web全题解_合天网安实验室的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, stego-media, web-app challenges.

## Input Signals

- Artifacts: ciphertext, stego-media, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, misc-analysis, php-tricks, ret2libc, sql-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `17`
- `docs/img/192dae5473a284d1e249faad880bd027.png`
- `docs/img/b88000911d7ecc2b6a59ecf741b697a1.png`
- `docs/img/bbed2c35e59694eb730254d01872ccc5.png`
- `docs/img/24d46d6a4ae3a8984fcfec97f47a11af.png`
- `docs/img/1d9db487fd8a297aab8f6afcbfff1e01.png`
- `docs/img/6c5dec959755797caf2f00bdf0dee694.png`
- `docs/img/9f7c4dc76a2df195ae6ff9058cd8ac1c.png`
- `docs/img/f473f5875148b0f52f46e8ae4c37b826.png`
- `docs/img/ad9db51bd003db730357b915fe6ee22f.png`
- `docs/img/2da5076c0f9bd766fc025e3f458b162d.png`
- `docs/img/26cbba803d03378758843080716007be.png`
- `docs/img/f3bd1c5015ef9a2a8d96e4757dbc1b46.png`
- ... and `5` more

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

### Step 2: HITCTF2018-web全题解_合天网安实验室的博客-CSDN博客

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `eval(base64_decode('JGZsYWc9JF9HRVRbJ2FzZGZnanh6a2FsbGdqODg1MiddO2lmKCRmbGFnPT0nSDFUY3RGMjAxOEV6Q1RGJyl7ZGllKCRmbGFnKTt9ZGllKCdlbW1tbScpOw=='))` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `eval(base64_decode('JGZsYWc9JF9HRVRbJ2FzZGZnanh6a2FsbGdqODg1MiddO2lmKCRmbGFnPT0nSDFUY3RGMjAxOEV6Q1RGJyl7ZGllKCRmbGFnKTt9ZGllKCdlbW1tbScpOw=='))`
  - `$flag=$_GET['asdfgjxzkallgj8852'];if($flag=='H1TctF2018EzCTF'){die($flag);}die('emmmm');`
  - `另外,{}有时候也可以当[]使用,文档中有说明："Note: string 也可用花括号访问，比如 str42",这里str{42}==$str[42]`
  - `$filter = "and|select|from|where|union|join|sleep|benchmark|,|\(|\)|like|rlike|regexp|limit|or";`
  - `if (preg_match("/".$filter."/is",$username)==1){`
  - `if (preg_match("/".$filter."/is",$passwd)==1){`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `eval(base64_decode('JGZsYWc9JF9HRVRbJ2FzZGZnanh6a2FsbGdqODg1MiddO2lmKCRmbGFnPT0nSDFUY3RGMjAxOEV6Q1RGJyl7ZGllKCRmbGFnKTt9ZGllKCdlbW1tbScpOw=='))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `string(39) "flag{162920976d9c04ac69e2f4392a8cffbf} "`

### Step 3: visit http://tool.lu/pyc/ for more information

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if ($username === "admin" && sha1(md5($password)) === $admin_hash){` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if ($username === "admin" && sha1(md5($password)) === $admin_hash){`
  - `if($_GET['debug'] === 'hitctf'){`
  - `query={ getscorebyid(id: "GE======"){ id name score } }`
  - `query={ getscorebyid(id: "11======"){ id name score } }`
  - `GE======`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `if ($username === "admin" && sha1(md5($password)) === $admin_hash){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `HITCTF{O0o0o0oOracle_Attttttack_1s_yinQu3S17ing}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
