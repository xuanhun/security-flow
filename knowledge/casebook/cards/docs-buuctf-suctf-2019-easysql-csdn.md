# BUUCTF__[SUCTF 2019]EasySQL_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[SUCTF-2019]EasySQL_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5BSUCTF-2019%5DEasySQL_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[SUCTF-2019]EasySQL_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy, netcat
- Techniques: binary-exploitation, dns-analysis, encoding-analysis, file-inclusion, http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `docs/img/be2336ba4856b9c68fd90e4bd5300c3d.png`
- `docs/img/fe5adebd8b30d01933957e82065fc8ce.png`
- `docs/img/b23887d076a4cb6f3179d2946bb38da3.png`
- `docs/img/271d881520e8665fc14ab01837118911.png`
- `docs/img/3af7056b1a18981744b75c8c1dc08250.png`

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

### Step 2: BUUCTF__[SUCTF 2019]EasySQL_题解_风过江南乱的博客-CSDN博客

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `select $_GET['query'] || flag from flag` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `select $_GET['query'] || flag from flag`
  - `这里的 || 是或运算符，也就是说先查询 select $_GET[‘query’] from flag，查询成功，后面的flag不执行查询。`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `select $_GET['query'] || flag from flag` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `be2336ba4856b9c68fd90e4bd5300c3d`

### Step 3: 方法一

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `此时sql语句为 select *,1||flag from flag;` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `此时sql语句为 select *,1||flag from flag;`
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat with the extracted filter/query `此时sql语句为 select *,1||flag from flag;` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `271d881520e8665fc14ab01837118911`

### Step 4: 方法二

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `让这里的 || 实现字符串拼接而不是或运算符。` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `让这里的 || 实现字符串拼接而不是或运算符。`
  - `但mysql缺省（默认）不支持 || 实现字符串拼接。`
  - `通过 sql_mode 中PIPES_AS_CONCAT的来使 || 实现字符串拼接功能。`
  - `我的理解是，相当于通过 sql_mode 中PIPES_AS_CONCAT 来设置mysql 中 || 支持字符串拼接。`
  - `set sql_mode=PIPES_AS_CONCAT 就相当于设置 || 支持字符串拼接。`
  - `再 select 1||flag from flag 得到flag。`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `让这里的 || 实现字符串拼接而不是或运算符。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3af7056b1a18981744b75c8c1dc08250`

### Step 5: 最后

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `$BlackList = "prepare|flag|unhex|xml|drop|create|insert|like|regexp|outfile|readfile|where|from|union|update|delete|if|sleep|extractvalue|updatexml|or|and|&|\"";` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `$BlackList = "prepare|flag|unhex|xml|drop|create|insert|like|regexp|outfile|readfile|where|from|union|update|delete|if|sleep|extractvalue|updatexml|or|and|&|\"";`
  - `$sql = "select ".$post['query']."||flag from Flag";`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `$BlackList = "prepare|flag|unhex|xml|drop|create|insert|like|regexp|outfile|readfile|where|from|union|update|delete|if|sleep|extractvalue|updatexml|or|and|&|\"";` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `config.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
