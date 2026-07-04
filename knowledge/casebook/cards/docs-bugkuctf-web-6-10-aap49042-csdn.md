# BugkuCTF WEB解题记录 6-10_aap49042的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BugkuCTF WEB解题记录 6`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BugkuCTF-WEB解题记录-6-10_aap49042的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BugkuCTF-WEB%E8%A7%A3%E9%A2%98%E8%AE%B0%E5%BD%95-6-10_aap49042%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BugkuCTF-WEB解题记录-6-10_aap49042的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: binary-exploitation, crypto-analysis, dns-analysis, http-analysis, sql-injection, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `14`
- `docs/img/5db5440450faba62a087fd3e3b152b3a.png`
- `docs/img/a582c8c087189661f534d350b7dcc97d.png`
- `docs/img/3acad41c741e3e659aee87590cfc2b88.png`
- `docs/img/4d55dde64dc58648135f6de169e84b67.png`
- `docs/img/6b5a84d04adf93917d566f198ecadfcc.png`
- `docs/img/724240a18a403314c5e88ad6c8a9ad1e.png`
- `docs/img/32e8b8736190917d5d3882b815e12d67.png`
- `docs/img/247cde0dcad9d0a9b12cd530f04018d4.png`
- `docs/img/737b3289727a127781c7f7ffc5371eba.png`
- `docs/img/73ff3b5bbe038edc6a18b55744e96aae.png`
- `docs/img/33227b7c0049c3d6d6e8936ca403457d.png`
- `docs/img/1dc91197872c5baaee217a2a094c677f.png`
- ... and `2` more

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

### Step 2: BugkuCTF WEB解题记录 6-10_aap49042的博客-CSDN博客

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `{ echo $num; if($num==1) echo 'flag{**********}';` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `{ echo $num; if($num==1) echo 'flag{**********}';`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `{ echo $num; if($num==1) echo 'flag{**********}';` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145:8002`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
