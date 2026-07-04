# [GXYCTF2019]BabyUpload 题解_偷一个月亮的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `GXYCTF2019`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[GXYCTF2019]BabyUpload-题解_偷一个月亮的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BGXYCTF2019%5DBabyUpload-%E9%A2%98%E8%A7%A3_%E5%81%B7%E4%B8%80%E4%B8%AA%E6%9C%88%E4%BA%AE%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[GXYCTF2019]BabyUpload-题解_偷一个月亮的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: not detected
- Techniques: file-upload, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `7`
- `docs/img/f1abfb722b96c3116ada5e96582dcc5a.png`
- `docs/img/539e4d98de98ba4dd3593cca53d1a3d2.png`
- `docs/img/4e52c4772bbaa12e34fbf309021ceae2.png`
- `docs/img/7f2ff790c10515289952c2f6a976d378.png`
- `docs/img/d51827ef4a3e8388b2d7c5853d9543e1.png`
- `docs/img/6f9280f7d1c1095dc6261c18a2721041.png`
- `docs/img/f5283667b089b361fc419e54cb2955e5.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: [GXYCTF2019]BabyUpload 题解_偷一个月亮的博客-CSDN博客

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use the artifact-specific tool to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f1abfb722b96c3116ada5e96582dcc5a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
