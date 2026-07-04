# 南邮ctf非正式题解 -- 逆向maze （方向的判断函数解析）_Air_cat的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `南邮ctf非正式题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/南邮ctf非正式题解----逆向maze-（方向的判断函数解析）_Air_cat的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%8D%97%E9%82%AEctf%E9%9D%9E%E6%AD%A3%E5%BC%8F%E9%A2%98%E8%A7%A3----%E9%80%86%E5%90%91maze-%EF%BC%88%E6%96%B9%E5%90%91%E7%9A%84%E5%88%A4%E6%96%AD%E5%87%BD%E6%95%B0%E8%A7%A3%E6%9E%90%EF%BC%89_Air_cat%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/南邮ctf非正式题解----逆向maze-（方向的判断函数解析）_Air_cat的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: not detected
- Techniques: encoding-analysis

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `2`
- `docs/img/ffcad7885b16595382bdaa5ad674e788.png`
- `docs/img/e8eef34c435cfd28c10f6e7535cb6705.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 南邮ctf非正式题解 -- 逆向maze （方向的判断函数解析）_Air_cat的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ffcad7885b16595382bdaa5ad674e788`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
