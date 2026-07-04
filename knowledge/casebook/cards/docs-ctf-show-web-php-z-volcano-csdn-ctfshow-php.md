# ctf show-web入门 php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性

## Case Metadata

- Category: `Web`
- Platform: `ctf show`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf-show-web入门-php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf-show-web%E5%85%A5%E9%97%A8-php%E7%89%B9%E6%80%A7%E7%AF%87%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_z.volcano%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctfshow%E7%9A%84php%E7%89%B9%E6%80%A7.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf-show-web入门-php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, detect-it-easy, netcat, radare2
- Techniques: classical-crypto, command-injection, crypto-analysis, dns-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, ret2libc, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `docs/img/2a53d086f78657fd968788e5f5074285.png`
- `docs/img/134981bbfb919996218fc77e72958bff.png`
- `docs/img/21fd3a89121f68dceca89ce0ffc7e93e.png`
- `docs/img/fed81ca0dae2f2c520d360fc16af50ef.png`
- `docs/img/fef5bfb1eb8bbd82456624ba3d3e5603.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf show-web入门 php特性篇部分题解_z.volcano的博客-CSDN博客_ctfshow的php特性

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_45696568/article/details/113631173](https://blog.csdn.net/weixin_45696568/article/details/113631173)`

### Step 3: php特性

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `89-95基本都是考察一些php函数的作用及其绕过姿势，所以不记录具体题目做法，只把姿势记下来。`

### Step 4: preg_match()

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, detect-it-easy, netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `如果不按规定传一个字符串，通常是传一个数组进去，这样就会报错，从而返回false，达到我们的目的。`

### Step 5: intval()

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy with the extracted filter/query `if($num==="4476"){` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if($num==="4476"){`
  - `if(intval($num,0)===4476){`
  - `intval('4476.0')===4476 小数点`
  - `intval('+4476.0')===4476 正负号`
  - `intval('4476e0')===4476 科学计数法`
  - `intval('0x117c')===4476 16进制`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy with the extracted filter/query `if($num==="4476"){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `intval('0b1000101111100')===4476 2进制`

### Step 6: web96(路径问题)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy with the extracted filter/query `if($_GET['u']=='flag.php'){` and inspect the matching evidence.
- Tools: detect-it-easy
- Filters or commands:
  - `if($_GET['u']=='flag.php'){`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy with the extracted filter/query `if($_GET['u']=='flag.php'){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 7: web98

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `$_GET['flag']=='flag'?$_GET=&$_COOKIE:'flag';` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `$_GET['flag']=='flag'?$_GET=&$_COOKIE:'flag';`
  - `$_GET['flag']=='flag'?$_GET=&$_SERVER:'flag';`
  - `highlight_file($_GET['HTTP_FLAG']=='flag'?$flag:__FILE__);`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `$_GET['flag']=='flag'?$_GET=&$_COOKIE:'flag';` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 8: web99(in_array弱类型比较)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这题突破点在in_array()函数`

### Step 9: in_array()

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `很明显，这题再使用in_array()函数时并没有设置第三个参数为TRUE,所以此时是==的弱类型比较。` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat, radare2
- Filters or commands:
  - `很明显，这题再使用in_array()函数时并没有设置第三个参数为TRUE,所以此时是==的弱类型比较。`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use burp, detect-it-easy, netcat, radare2 with the extracted filter/query `很明显，这题再使用in_array()函数时并没有设置第三个参数为TRUE,所以此时是==的弱类型比较。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2a53d086f78657fd968788e5f5074285`

### Step 10: web100

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ctfshow.php`

### Step 11: var_dump()函数

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `两种方法均可，原理是直接打印ctfshow类的信息。`

### Step 12: web101

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `但是直接:`?v1=1&v2=echo new ReflectionClass&v3=;`可以得到flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
