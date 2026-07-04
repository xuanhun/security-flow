# 百度杯”CTF比赛（十二月场)_Root__Liu的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `百度杯”CTF比赛（十二月场)`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/百度杯”CTF比赛（十二月场)_Root__Liu的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%99%BE%E5%BA%A6%E6%9D%AF%E2%80%9DCTF%E6%AF%94%E8%B5%9B%EF%BC%88%E5%8D%81%E4%BA%8C%E6%9C%88%E5%9C%BA%29_Root__Liu%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/百度杯”CTF比赛（十二月场)_Root__Liu的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, ids, stego-media challenges.

## Input Signals

- Artifacts: ciphertext, ids, stego-media, web-app
- Tools: z3
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `24`
- `docs/img/2f565c031c5e6a63b5de0a5e4539ceb7.png`
- `docs/img/5f3002ea2c26b87efe6194cc94a8ece1.png`
- `docs/img/b716defe71a2febd0a86b91f361ebb2f.png`
- `docs/img/7d50b2fb589ab6e608c167761667cbdd.png`
- `docs/img/e10bc14d62524cea7501d9114ab288bb.png`
- `docs/img/a6ab3f3a14ecd1cbdd9a6a6fe7cfe8d2.png`
- `docs/img/6141f12d98340323a1c32a737008dd42.png`
- `docs/img/7f835e5cdf3f8f20b588ee0e65dab80d.png`
- `docs/img/0980aa4c25267c1a27f89e8d4f9450db.png`
- `docs/img/16e1ab6c1ee8f8dc7242db93f5dc825f.png`
- `docs/img/4924cdcfdf57527dc3ae988bdf9a8741.png`
- `docs/img/d77afe874bda09cbbb8a2c657331873f.png`
- ... and `12` more

## Solve Thinking

### Step 1: Document

- Route type: `z3-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use z3 to collect the smallest evidence slice that answers the goal.
- Tools: z3
- Reasoning chain:
  - Recognize the section as z3-driven evidence lookup.
  - Use z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 百度杯”CTF比赛（十二月场)_Root__Liu的博客-CSDN博客

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2f565c031c5e6a63b5de0a5e4539ceb7`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
