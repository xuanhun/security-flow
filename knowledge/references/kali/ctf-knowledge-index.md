# CTF Knowledge Index

Use this index for authorized CTF challenges after reading
[ctf-agent-skill-tree.md](ctf-agent-skill-tree.md). The skill tree is the
Nemo-style base layer: notes first, phased solving, local knowledge routing,
explicit checkpoints, and proof before solve. This file routes category
knowledge once the case state and first-pass evidence exist.

## Universal Triage

1. Restate the challenge goal, flag format, category, and provided artifacts.
2. Initialize or reuse a case directory with `ctf_agent.py init`, then start
   with `ctf_agent.py start` and read notes with `ctf_agent.py note --read-all`.
3. Follow the case phase from `ctf_agent.py phase`; do not skip note replay.
4. Perform first-pass information
   gathering with skill tools before reading cases:
   landing page, login flow when credentials are provided, headers, cookies,
   redirects, forms, links, scripts, visible text, screenshots when useful, and
   attachment inventory.
5. Extract observed evidence terms: technologies, routes, APIs, parameters,
   state objects, roles, artifacts, unusual wording, and trust boundaries.
6. Browse the local casebook by content hierarchy: category, artifact,
   technique, then route/card. Record the chosen path and useful cards in
   challenge notes.
7. Run `ctf_agent.py knowledge` to record local knowledge hits before relying
   on any external source.
8. Check whether a skill tool already covers the needed probe. For Web
   challenges, use `scripts/ctf_web.py` before manual requests. If a repeatable
   probe is missing, add it to the skill first, then run it.
9. Inventory evidence: page text, files, URLs, hints, source, traffic, binary
   metadata, strings, hashes, and screenshots.
10. Identify the first trust boundary: browser/server, parser/file, crypto
   primitive, binary input, mobile app boundary, CDN/cache, or ML pipeline.
11. Form two or three hypotheses, then run the cheapest probe for each.
12. If local evidence, local casebook cards, and skill-backed hypotheses stall,
   use web search for public docs, source, CVEs, framework behavior, and
   writeups. Record queries and useful URLs, then verify ideas locally before
   treating them as part of the route.
13. Preserve every useful command, request, response, hash, script path, and
   useful search query.
14. Stop when a route crosses out of the CTF scope or needs credentials not
   provided by the challenge.
15. If the category is unclear or the first route stalls, read
   [ctf-external-pattern-map.md](ctf-external-pattern-map.md) and then return to
   the most relevant local category file.

## Tool-First Closed Loop

- Read the wisdom workflow `framework/workflows/engagement-lifecycle.md` before using
  the skill in this workspace.
- Use `ctf_agent.py` for local state, notes, phase checkpoints, knowledge hits,
  and handoff summaries.
- Open the target and collect first-pass evidence before using solved cases as
  hypotheses.
- Treat missing repeatable probes as skill gaps, not as reasons to hand-write a
  one-off solve path.
- Use web search only as a stall-recovery gate. Validated external ideas should
  be turned into local notes, tools, or case patterns after the solve.
- After solving, update the case library, category knowledge, and replay
  commands so the next challenge can start from the skill.

## Audit Checklists

- Git history, source leaks, orphan commits, and issue-screenshot evidence:
  [git-audit-checklist.md](git-audit-checklist.md)

## Category Routing

- Web: [ctf-knowledge-web.md](ctf-knowledge-web.md)
- Crypto: [ctf-knowledge-crypto.md](ctf-knowledge-crypto.md)
- MISC and forensics: [ctf-knowledge-misc-forensics.md](ctf-knowledge-misc-forensics.md)
- Reverse and pwn: [ctf-knowledge-reverse-pwn.md](ctf-knowledge-reverse-pwn.md)
- Mobile and Android app: [ctf-knowledge-mobile.md](ctf-knowledge-mobile.md)
- OSINT: [ctf-knowledge-osint.md](ctf-knowledge-osint.md)
- Malware: [ctf-knowledge-malware.md](ctf-knowledge-malware.md)
- AI and digital watermark: [ctf-knowledge-ai-watermark.md](ctf-knowledge-ai-watermark.md)
- CDN, privacy, and client security:
  [ctf-knowledge-cdn-privacy-client.md](ctf-knowledge-cdn-privacy-client.md)
- Coding specification: [ctf-knowledge-coding-spec.md](ctf-knowledge-coding-spec.md)

## Solved Case Library

Use solved cases as examples after reading the category knowledge. A case should
not replace reasoning; it should show how a pattern was recognized, probed, and
verified.

- Local parsed casebook:
  [ctf-casebook.md](ctf-casebook.md)
- Case index: [ctf-case-index.md](ctf-case-index.md)
- NO.1 Cookie: [ctf-case-no1-cookie.md](ctf-case-no1-cookie.md)
- Bytedance Lobster Hole:
  [ctf-case-bytedance-lobster-hole.md](ctf-case-bytedance-lobster-hole.md)
- NO.2 Member Gift: [ctf-case-no2-member-gift.md](ctf-case-no2-member-gift.md)
- NO.3 Achilles Video: [ctf-case-no3-http-video.md](ctf-case-no3-http-video.md)
- NO.4 Easy Hertz: [ctf-case-no4-easy-hertz.md](ctf-case-no4-easy-hertz.md)
- NO.5 Blind Ads Cross:
  [ctf-case-no5-blind-ads-cross.md](ctf-case-no5-blind-ads-cross.md)
- NO.6 BitDancing Guest:
  [ctf-case-no6-bitdancing-guest.md](ctf-case-no6-bitdancing-guest.md)
- NO.7 SQL Differential Privacy Salary:
  [ctf-case-no7-sql-dp-salary.md](ctf-case-no7-sql-dp-salary.md)
- NO.8 Random OTP Address:
  [ctf-case-no8-random-otp.md](ctf-case-no8-random-otp.md)
- NO.9 Tonight Party:
  [ctf-case-no9-tonight-party.md](ctf-case-no9-tonight-party.md)
- NO.10 Multimodal Identity:
  [ctf-case-no10-multimodal-identity.md](ctf-case-no10-multimodal-identity.md)
- AI Security Multimodal Prompt Injection:
  [ctf-case-ai-security-multimodal-prompt-injection.md](ctf-case-ai-security-multimodal-prompt-injection.md)
- NO.11 Admin Dev Public:
  [ctf-case-no11-admin-dev-public.md](ctf-case-no11-admin-dev-public.md)
- NO.12 EzAndro:
  [ctf-case-no12-ezandro.md](ctf-case-no12-ezandro.md)
- KotKit:
  [ctf-case-kotkit.md](ctf-case-kotkit.md)
- Local iOS CTF03 Assets.car:
  [ctf-case-local-ios-ctf03-assets-car.md](ctf-case-local-ios-ctf03-assets-car.md)
- NO.13 Image Hosting Abuse Evidence:
  [ctf-case-no13-image-hosting-abuse.md](ctf-case-no13-image-hosting-abuse.md)
- NO.14 Private Messenger:
  [ctf-case-no14-private-messenger.md](ctf-case-no14-private-messenger.md)
- BytePaste:
  [ctf-case-bytepaste.md](ctf-case-bytepaste.md)
- Byte Secret:
  [ctf-case-byte-secret.md](ctf-case-byte-secret.md)
- Interest Circle:
  [ctf-case-interest-circle.md](ctf-case-interest-circle.md)
- Social Engineering HackMeIfYouCan:
  [ctf-case-social-engineering-hackmeifyoucan.md](ctf-case-social-engineering-hackmeifyoucan.md)
- The Careless Developer:
  [ctf-case-the-careless-developer.md](ctf-case-the-careless-developer.md)

## External Pattern Cross-Check

- Distilled source map:
  [ctf-external-pattern-map.md](ctf-external-pattern-map.md)
- Upstream source:
  `https://github.com/ljagiello/ctf-skills` at commit
  `1af14f9030fee9da46014a8a3ed61a555b81ab98`

## Note Format For New Lessons

```text
### <short pattern name>

- Signal:
- First probes:
- Common route:
- False leads:
- Useful tools:
- Evidence to keep:
- Example cases:
```
