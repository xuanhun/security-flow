# CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛

## Case Metadata

- Category: `Web`
- Platform: `CTF解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E8%A7%A3%E9%A2%98-2020%E5%B9%B4%E5%BC%BA%E7%BD%91%E6%9D%AF%E5%8F%82%E8%B5%9BWriteUp_Tr0e%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E8%A7%A3%E9%A2%98%E8%B5%9B.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, ids, pcap challenges.

## Input Signals

- Artifacts: ciphertext, ids, pcap, stego-media, web-app
- Tools: detect-it-easy, netcat, steghide, wireshark
- Techniques: classical-crypto, command-injection, deserialization, encoding-analysis, file-upload, http-analysis, network-forensics, php-tricks, ret2libc, sql-injection, stego-extraction, traffic-analysis, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `33`
- `docs/img/5838c3dc7a69c1406f997191f92cdf7e.png`
- `docs/img/f44d54883c1ab39d52a5ef291f5891a2.png`
- `docs/img/ed2c96ba148e5d48b3807b9224f534ee.png`
- `docs/img/0df17e029fc4981cefa3dece760c35ae.png`
- `docs/img/edfbfd9925266fc570e5bc44642249db.png`
- `docs/img/72682b1cbde165c8544b1dba6492109b.png`
- `docs/img/d942db98152b697ece0bac0b5161018a.png`
- `docs/img/2014ce6bcd494e3f8f549bdf2c4d11a5.png`
- `docs/img/3e2e27329be176fecea4b0a32f1d9918.png`
- `docs/img/a6a372de298aba96bbff420a561d3778.png`
- `docs/img/472647f03d69350d696e3f5e12497cbc.png`
- `docs/img/58344eb42ed204532a48a599f666921e.png`
- ... and `21` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, steghide, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, steghide, wireshark
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, steghide, wireshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF解题-2020年强网杯参赛WriteUp_Tr0e的博客-CSDN博客_ctf解题赛

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, steghide, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat, steghide, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, steghide, wireshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_39190897/article/details/108287362](https://blog.csdn.net/weixin_39190897/article/details/108287362)`

### Step 3: 前言

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, steghide, wireshark to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, steghide, wireshark
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, steghide, wireshark to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5838c3dc7a69c1406f997191f92cdf7e`

### Step 4: 主动

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy, netcat, steghide, wireshark with the extracted filter/query `?id=1;cat `echo 'Li9mbGFnLnBocAo=' | base64 -d`：` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, steghide, wireshark
- Filters or commands:
  - `?id=1;cat `echo 'Li9mbGFnLnBocAo=' | base64 -d`：`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy, netcat, steghide, wireshark with the extracted filter/query `?id=1;cat `echo 'Li9mbGFnLnBocAo=' | base64 -d`：` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f44d54883c1ab39d52a5ef291f5891a2`

### Step 5: FunHash

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy, netcat, steghide, wireshark with the extracted filter/query `2、先看 **level 1** 的绕过：PHP在处理哈希字符串时，会利用`”!=”`或`”==”`来对哈希值进行比较，**它把每一个以”0E”开头的哈希值都解释为0**，所以如果两个不同的密码经过哈希以后，其哈希值都是以”0E”开头的，那么PHP将会认为他们相同，都是0。故执行以下php脚本：` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, steghide, wireshark
- Filters or commands:
  - `2、先看 **level 1** 的绕过：PHP在处理哈希字符串时，会利用`”!=”`或`”==”`来对哈希值进行比较，**它把每一个以”0E”开头的哈希值都解释为0**，所以如果两个不同的密码经过哈希以后，其哈希值都是以”0E”开头的，那么PHP将会认为他们相同，都是0。故执行以下php脚本：`
  - `3、 再来看看 **level 2** 的绕过：php处理哈希函数时，如果传入的两个参数不是字符串，而是数组，md5()函数无法解出其数值，而且不会报错，就会得到`===`强比较的值相等；`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy, netcat, steghide, wireshark with the extracted filter/query `2、先看 **level 1** 的绕过：PHP在处理哈希字符串时，会利用`”!=”`或`”==”`来对哈希值进行比较，**它把每一个以”0E”开头的哈希值都解释为0**，所以如果两个不同的密码经过哈希以后，其哈希值都是以”0E”开头的，那么PHP将会认为他们相同，都是0。故执行以下php脚本：` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2014ce6bcd494e3f8f549bdf2c4d11a5`

### Step 6: Web辅助

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `| 方法 | 解释 |` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `| 方法 | 解释 |`
  - `| --- | --- |`
  - `| __construct | 构造函数，具有构造函数的类会在每次创建新对象时先调用此方法 |`
  - `| __destruct | 析构函数，析构函数会在到某个对象的所有引用都被删除或者当对象被显式销毁时执行 |`
  - `| wakeup | unserialize() 会检查是否存在一个 wakeup() 方法。如果存在，则会先调用 |`
  - `| invoke | **当尝试以调用函数的方式调用一个对象时**，**invoke() 方法会被自动调用** |`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat with the extracted filter/query `| 方法 | 解释 |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5965722bc84c01be319621667fbf2431`

### Step 7: Upload

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use steghide, wireshark with the extracted filter/query `steghide extract -sf $1 -p $line > /dev/null 2>&1` and inspect the matching evidence.
- Tools: steghide, wireshark
- Filters or commands:
  - `steghide extract -sf $1 -p $line > /dev/null 2>&1`
  - `Steghide 是一个可以将文件隐藏到图片或音频中的工具，其使用如下：`
  - `| 目的 | 命令 |`
  - `| --- | --- |`
  - `| Liunx安装 | apt-get install steghide |`
  - `| 隐藏文件 | steghide embed -cf 1.jpg（图片文件载体） -ef 1.txt（待隐藏文件） |`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use steghide, wireshark with the extracted filter/query `steghide extract -sf $1 -p $line > /dev/null 2>&1` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2bdfd5cc1dd04984853ae157f56dec6f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
