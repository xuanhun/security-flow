# buuctf XCTF October 2019 Twice SQL Injection 二次注入原理+题解_AAAAAAAAAAAA66的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `buuctf XCTF October 2019 Twice SQL Injec`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/buuctf-XCTF-October-2019-Twice-SQL-Injection-二次注入原理+题解_AAAAAAAAAAAA66的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/buuctf-XCTF-October-2019-Twice-SQL-Injection-%E4%BA%8C%E6%AC%A1%E6%B3%A8%E5%85%A5%E5%8E%9F%E7%90%86%2B%E9%A2%98%E8%A7%A3_AAAAAAAAAAAA66%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/buuctf-XCTF-October-2019-Twice-SQL-Injection-二次注入原理+题解_AAAAAAAAAAAA66的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: sql-injection

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `11`
- `docs/img/7d9e3d7188cac3358f1ddff2e70b623a.png`
- `docs/img/be4fb0974c2b996dec8fcf7d5188c1cc.png`
- `docs/img/902f47ba5eb99df32e06aab44ad09544.png`
- `docs/img/3122230776efe92dd21b561b3c9a61fe.png`
- `docs/img/3016e6f2ebe3e4573edee1bf60c081a6.png`
- `docs/img/a5d4dfe0812ed14a41e9117465abf2c3.png`
- `docs/img/d9f8d39bd60fe9238ef3e31c74a08247.png`
- `docs/img/6dec89054597c00d4adf978671a83546.png`
- `docs/img/f921da6e4b7f261f64c84a78bd3a2819.png`
- `docs/img/35226d97fe6f57964cca1b286c3272cc.png`
- `docs/img/4c686ea02523bf9097e684440165d231.png`

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

### Step 2: buuctf XCTF October 2019 Twice SQL Injection 二次注入原理+题解_AAAAAAAAAAAA66的博客-CSDN博客

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7d9e3d7188cac3358f1ddff2e70b623a`

### Step 3: 二次注入的成因

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**所以要说明的是，二次注入的产生是需要以上一些特定的条件的。所以二次注入一般比较难发现**。`

### Step 4: 思路

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3016e6f2ebe3e4573edee1bf60c081a6`

### Step 5: 步骤

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a5d4dfe0812ed14a41e9117465abf2c3`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
