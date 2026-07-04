# There only 10 people use the same phone as you（i春秋CTF题解）_weixin_30618985的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `There only 10 people use the same phone`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/There-only-10-people-use-the-same-phone-as-you（i春秋CTF题解）_weixin_30618985的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/There-only-10-people-use-the-same-phone-as-you%EF%BC%88i%E6%98%A5%E7%A7%8BCTF%E9%A2%98%E8%A7%A3%EF%BC%89_weixin_30618985%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/There-only-10-people-use-the-same-phone-as-you（i春秋CTF题解）_weixin_30618985的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp
- Techniques: sql-injection

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `14`
- `docs/img/cf8ebd6037491fdab4d9863f411bd3eb.png`
- `docs/img/c6e2d13e7c076955a91ba352697ee366.png`
- `docs/img/b0baafe4bef91b297ab262ec37106d39.png`
- `docs/img/8db67deccc104780d8b64ec12253f222.png`
- `docs/img/ed2497a6a52de2ba5c71c10a85ba18f5.png`
- `docs/img/5241f9678de772217d6543a596e033a9.png`
- `docs/img/fe65be64230b978b008224ef2da87401.png`
- `docs/img/00ca4ce4310fc8c34faabcafe7356b81.png`
- `docs/img/8060eb81402386462f13d35130cb1fa4.png`
- `docs/img/f52c71317c166c9d11d37d2d8e3e9d94.png`
- `docs/img/0134c814f6604d81bc5eacfb31a692a1.png`
- `docs/img/c0d5cead4f6b09d6a60115b95d6c0c5e.png`
- ... and `2` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: There only 10 people use the same phone as you（i春秋CTF题解）_weixin_30618985的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_30618985/article/details/98878078](https://blog.csdn.net/weixin_30618985/article/details/98878078)`

### Step 3: （1）访问网址进行CTF测试，仅出现登陆与注册的页面

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cf8ebd6037491fdab4d9863f411bd3eb`

### Step 4: （2）进行注册尝试登陆并进行burp抓取数据包：

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c6e2d13e7c076955a91ba352697ee366`

### Step 5: （3）注册成功，进行登陆尝试查看信息是否具有提示，在登录的页面只有两个点击页面，一个为：Check，一个为logout

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `8db67deccc104780d8b64ec12253f222`

### Step 6: （4）进入到Check的登录页面，查看是否具有提示信息，果然有提示，发现了一句良心提示，找到思路，让我们对注册页面的电话那一栏进行sql注入操作！

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ed2497a6a52de2ba5c71c10a85ba18f5`

### Step 7: （5）首先，进行抓包：为了不做重复型的工作，我们可以使用burp的repeater进行包的重复发送

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fe65be64230b978b008224ef2da87401`

### Step 8: （6）每注册一次，希望能执行一次sql的语句注入，猜想：

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8060eb81402386462f13d35130cb1fa4`

### Step 9: （7）构造sql注入语句：

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> -1 union select table_schema from information_schema.columns`

### Step 10: 进行了整个数据库的数据查询，16进制加密为：

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> ## 0x2d3120756e696f6e2073656c656374207461626c655f736368656d612066726f6d20696e666f726d6174696f6e5f736368656d612e636f6c756d6e73`

### Step 11: 登录显示结果：

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0134c814f6604d81bc5eacfb31a692a1`

### Step 12: （8）三个库，我们猜想，一般admin或是flag都藏在mysql库中，使用这个库进行查询表的操作：

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - The proof is the database-backed response difference, error, or extracted row tied to the injected parameter.
- Evidence rule: The proof is the database-backed response difference, error, or extracted row tied to the injected parameter.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
