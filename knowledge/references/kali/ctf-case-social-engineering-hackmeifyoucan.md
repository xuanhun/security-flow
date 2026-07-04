# Social Engineering HackMeIfYouCan

## Metadata

- Category: Social Engineering / OSINT.
- Source material: user-provided challenge screenshots in this workspace
  conversation.
- Local artifact status: the original JPG and public-platform screenshots were
  not present as files; only the Base64 decoding step was replayed locally.
- Final flag shown by the challenge route: `flag{Heracles_salute_you}`.

## Prompt Summary

The challenge first identifies the POI "Hongshan Ruiting Hotel" from JPG
metadata. A Google result for that hotel has a recent review whose time matches
the JPG modification time. The suspicious reviewer ID is `HackMeIfYouCan`.

Searching that ID on Douyin/TikTok leads to a profile whose visible note says
to decode a value and add WeChat. The decoded value is used as a WeChat search
target, and the public profile signature exposes the flag.

## Pattern

POI review timestamp to cross-platform identity pivot.

The important clue is not only the location. The location becomes a public
source pivot: map/search results provide a time-correlated reviewer identity,
and that identity becomes the next search key across platforms.

## Signal Inventory

- Provided JPG has location metadata and a modification time.
- The recovered POI is "Hongshan Ruiting Hotel" / `红山瑞廷酒店`.
- A latest Google review has a time matching the JPG modification time.
- The reviewer handle `HackMeIfYouCan` is intentionally challenge-like.
- A same-handle Douyin/TikTok profile gives an encoded WeChat hint.
- The final flag is in a public WeChat profile signature.

## Probes And Evidence

Base64 candidate replay:

```bash
python scripts/sec.py probe crypto triage \
  --case-dir engagements/social-engineering-hackmeifyoucan \
  --label wechat-base64 \
  --text 'Vm1IODYx='
```

This literal screenshot/OCR candidate decodes to `VmH861`.

Corrected visual candidate replay:

```bash
python scripts/sec.py probe crypto triage \
  --case-dir engagements/social-engineering-hackmeifyoucan \
  --label wechat-base64-viu861 \
  --text 'Vml1ODYx'
```

This decodes to `Viu861`, matching the challenge screenshot's described WeChat
search value.

Evidence:

- `../../../engagements/social-engineering-hackmeifyoucan/artifacts/wechat-base64-crypto-triage.json`
- `../../../engagements/social-engineering-hackmeifyoucan/artifacts/wechat-base64-viu861-crypto-triage.json`

## Route Decision

1. Extract image metadata and map the coordinates to the POI.
2. Search the exact POI name and inspect recent public reviews.
3. Use timestamp consistency between the JPG modification time and review time
   to select the intended review.
4. Treat the suspicious reviewer ID as the next pivot, not as the answer.
5. Search the exact ID `HackMeIfYouCan` on public social platforms.
6. Decode the profile hint. When OCR makes Base64 ambiguous, test plausible
   `l/1/I/O/0` substitutions and keep the variant that produces a valid next
   account.
7. Search the decoded account ID `Viu861` in WeChat and read the public profile
   signature.
8. Submit the literal flag shown there:
   `flag{Heracles_salute_you}`.

## Reusable Lesson

For social-engineering CTFs, a location or timestamp often serves as an
identity disambiguator. Build a chain where each step has two ties to the
previous step: same place plus matching time, same handle plus avatar/profile
context, encoded hint plus platform account existence, then public profile plus
flag syntax.

Do not contact real users. Public profile search and visible signatures are
enough for this pattern; messaging or adding friends is outside the useful
evidence path unless the challenge explicitly provides a controlled account and
requires that interaction.
