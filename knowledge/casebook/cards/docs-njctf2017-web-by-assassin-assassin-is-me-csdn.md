# NJCTF2017 线上赛 web 题解 By Assassin_Assassin__is__me的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `NJCTF2017 线上赛 web 题解 By Assassin`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/NJCTF2017-线上赛-web-题解-By-Assassin_Assassin__is__me的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/NJCTF2017-%E7%BA%BF%E4%B8%8A%E8%B5%9B-web-%E9%A2%98%E8%A7%A3-By-Assassin_Assassin__is__me%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/NJCTF2017-线上赛-web-题解-By-Assassin_Assassin__is__me的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, dns-analysis, encoding-analysis, http-analysis, misc-analysis, php-tricks, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `27`
- `docs/img/724009814381e7650cf93a805db9acc1.png`
- `docs/img/11484091cfc7702293c9ed493736169e.png`
- `docs/img/058f8ee514126c5a6247b88af537a331.png`
- `docs/img/ad6ce8b03af275e63eb342f96fe75377.png`
- `docs/img/15d06d2085e476844ada613131be3677.png`
- `docs/img/3293fff246f4a95596511bb2263ee05d.png`
- `docs/img/f80d87574e9caec414da169add687ce8.png`
- `docs/img/ee8c74704a21bcd78d89b4fe3098aad9.png`
- `docs/img/8211f70d1d22d2f25a251d468a327b81.png`
- `docs/img/d93bb2d73647f7c1c2b74fda7f83c56c.png`
- `docs/img/a7e9605d8397c89345731225201215a1.png`
- `docs/img/a7dd6263bfba6e413fd22a03abef0e85.png`
- ... and `15` more

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

### Step 2: NJCTF2017 线上赛 web 题解 By Assassin_Assassin__is__me的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_35078631/article/details/62980648](https://blog.csdn.net/qq_35078631/article/details/62980648)`

### Step 3: **Login**

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `724009814381e7650cf93a805db9acc1`

### Step 4: **Get Flag**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `15d06d2085e476844ada613131be3677`

### Step 5: **Chall I**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `$http.post('/login', {password: $scope.password}).then(function(response) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `$http.post('/login', {password: $scope.password}).then(function(response) {`
  - `if(response.data.status === 'ok') {`
  - `$http.get('/logout').then(function(response) {`
  - `if(req.body.password !== undefined) {`
  - `if(password.toString('base64') == config.secret_password) {`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `$http.post('/login', {password: $scope.password}).then(function(response) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `218.2.197.235:23729`

### Step 6: **chall II**

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a7dd6263bfba6e413fd22a03abef0e85`

### Step 7: **blog**

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e2d0ebf06af3e7ac518a71f4302ea994`

### Step 8: **come on**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `首先输入1查询一下，发现很多股票就出来了。然后构造各种乱七八糟的发现根本没什么回显，那么就是盲注了，然后我们看一下宽字节的构造`http://218.2.197.235:23733/index.php?key=1%df%27||1=1%23` 然后发现有回显，那么我们就可以构造或后面的1=1盲注爆出他字段。` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `首先输入1查询一下，发现很多股票就出来了。然后构造各种乱七八糟的发现根本没什么回显，那么就是盲注了，然后我们看一下宽字节的构造`http://218.2.197.235:23733/index.php?key=1%df%27||1=1%23` 然后发现有回显，那么我们就可以构造或后面的1=1盲注爆出他字段。`
  - `url='http://218.2.197.235:23733/index.php?key=123%df%27||'`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `首先输入1查询一下，发现很多股票就出来了。然后构造各种乱七八糟的发现根本没什么回显，那么就是盲注了，然后我们看一下宽字节的构造`http://218.2.197.235:23733/index.php?key=1%df%27||1=1%23` 然后发现有回显，那么我们就可以构造或后面的1=1盲注爆出他字段。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `218.2.197.235:23733`

### Step 9: **Wallet**

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `if ($auth == $hsh) {` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if ($auth == $hsh) {`
  - `} else if (sha1((string)$hsh) == md5((string)$auth)) {`
  - `if (!$result === NULL) {`
  - `echo "Wallet contains: $result";`
  - `首先需要利用(sha1((string)$hsh) == md5((string)$auth))中==的漏洞，构造0exxxx的数字(x必须是10进制数字)，达到绕过的目的（实际上是科学计数法）。实验`
  - `MD5值==0小结`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `if ($auth == $hsh) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `13fe42bb09370c47d0bde22904878179`

### Step 10: **Text wall**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `218.2.197.235:23721`

### Step 11: **Be admin**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `return $password == $pass;` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `return $password == $pass;`
  - `发现返回值来自==弱匹配！其中$pass来自用户输入的password，$encrypted_pass就是上面主函数中查询的语句。`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `return $password == $pass;` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9aaa969dba1fa048aa4239628192a656`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
