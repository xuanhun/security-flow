# mysql_char ctf_buuctf_sql注入_随便注1_折柳为信的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `mysql`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/mysql_char-ctf_buuctf_sql注入_随便注1_折柳为信的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/mysql_char-ctf_buuctf_sql%E6%B3%A8%E5%85%A5_%E9%9A%8F%E4%BE%BF%E6%B3%A81_%E6%8A%98%E6%9F%B3%E4%B8%BA%E4%BF%A1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/mysql_char-ctf_buuctf_sql注入_随便注1_折柳为信的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `10`
- `docs/img/666e464532415ff9504ceedb34a9c925.png`
- `docs/img/73efa81fdb165c5ce2dd0a6647ea03b4.png`
- `docs/img/fe162cfbae73bb3e56b1e3fe2aa71465.png`
- `docs/img/585758548ba70de09bd6450357994238.png`
- `docs/img/682428048416ece5bcef883362171101.png`
- `docs/img/da3e0593378c4d7be3e09018aad673d6.png`
- `docs/img/dce69cae63a051ae377d025cc8811193.png`
- `docs/img/fecfa8773a32257de030b78b29d20786.png`
- `docs/img/e796e2e4b9010202e9c671c94e33a17e.png`
- `docs/img/61105905447ffee1a78323a725fd396b.png`

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

### Step 2: mysql_char ctf_buuctf_sql注入_随便注1_折柳为信的博客-CSDN博客

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d5a80f89ba86b723ef777de0d929c22b`

### Step 3: 打开一张表，无返回结果，实际上声明了一个名为tb1_name的句柄。

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `HANDLER tbl_name READ index_name { = | <= | >= | < | > } (value1,value2,...)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `HANDLER tbl_name READ index_name { = | <= | >= | < | > } (value1,value2,...)`
  - `HANDLER tbl_name READ index_name { FIRST | NEXT | PREV | LAST }`
  - `HANDLER tbl_name READ { FIRST | NEXT }`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `HANDLER tbl_name READ index_name { = | <= | >= | < | > } (value1,value2,...)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[ WHERE where_condition ] [LIMIT ... ]`

### Step 4: 获取句柄的第一行，通过READ NEXT依次获取其它行。最后一行执行之后再执行NEXT会返回一个空的结果。

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `HANDLER tbl_name CLOSE`

### Step 5: 关闭打开的句柄。

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `总结：在监工短短的督促下，这道题的总结终于东拼西凑写完了。我还很菜，文章中内容很多都是摘自大佬们，其中有些知识点我的理解也许不对，不确定的这部分我写的比较繁琐详细，希望能与大家交流。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
