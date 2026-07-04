# BUUCTF crackMe 题解___lifanxin的博客-CSDN博客_buuctf crackme

## Case Metadata

- Category: `Reverse`
- Platform: `BUUCTF crackMe 题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-crackMe-题解___lifanxin的博客-CSDN博客_buuctf-crackme.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-crackMe-%E9%A2%98%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf-crackme.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-crackMe-题解___lifanxin的博客-CSDN博客_buuctf-crackme.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: ida
- Techniques: encoding-analysis, php-tricks, reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `13`
- `docs/img/646c961cf691ab18aeae5d1ad52361f5.png`
- `docs/img/3484ff209fd391ecd82626dda6efd728.png`
- `docs/img/4a502b87ca3df60bf8513c377b1f70fc.png`
- `docs/img/c50f3ad5a16138fa3eedd1cad5c1d3d2.png`
- `docs/img/b3e49f66b214f35050efd05a8516f7b9.png`
- `docs/img/5b5e8c400d8202b6187ff4cf896c0037.png`
- `docs/img/7fcccf899413be97404553945556be84.png`
- `docs/img/356f4aab2df3bc2d856ae74775342fba.png`
- `docs/img/5fa1ce28485923b38b6162d7252db079.png`
- `docs/img/f32a1b054331a913aa92164bee69fede.png`
- `docs/img/8fe6520fbee9e5b4a8950ae5c0501bd9.png`
- `docs/img/91b5663fdc6816ef8a1bf6016123d6e5.png`
- ... and `1` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF crackMe 题解___lifanxin的博客-CSDN博客_buuctf crackme

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/118667242](https://blog.csdn.net/A951860555/article/details/118667242)`

### Step 3: 程序信息

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `之所以要写这个wp，是对题目的答案存在一些疑问，网上也有很多wp，我都看了一下，大致都出自于同一个人的手笔O(∩_∩)O。我个人感觉网上的wp分析过程都漏了一步，虽然这样得出的flag可以通过buuoj，但是这是个crack题目，网上wp的答案无法通过程序本身，我个人分析得出的答案是可以通过程序本身的。`

### Step 4: main函数分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `646c961cf691ab18aeae5d1ad52361f5`

### Step 5: sub_401830关键函数分析

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida with the extracted filter/query `先看sub_401470，如下截图所示，只截了一部分，`a2`就是v16-2，让每个if判断中的a2等于对应字母就可得到`v13 == 0xAB94`，这里还有一行反调试，没有截图出来，大家自行判别就好，最后解出来v16-2为`dbappsec`。` and inspect the matching evidence.
- Tools: ida
- Filters or commands:
  - `先看sub_401470，如下截图所示，只截了一部分，`a2`就是v16-2，让每个if判断中的a2等于对应字母就可得到`v13 == 0xAB94`，这里还有一行反调试，没有截图出来，大家自行判别就好，最后解出来v16-2为`dbappsec`。`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida with the extracted filter/query `先看sub_401470，如下截图所示，只截了一部分，`a2`就是v16-2，让每个if判断中的a2等于对应字母就可得到`v13 == 0xAB94`，这里还有一行反调试，没有截图出来，大家自行判别就好，最后解出来v16-2为`dbappsec`。` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5b5e8c400d8202b6187ff4cf896c0037`

### Step 6: 动态调试byte_416050

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f32a1b054331a913aa92164bee69fede`

### Step 7: 求解

- Route type: `ida-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use ida to collect the smallest evidence slice that answers the goal.
- Tools: ida
- Reasoning chain:
  - Recognize the section as ida-driven evidence lookup.
  - Use ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e2d687c262ba6bdb660ed0965d083a37`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
