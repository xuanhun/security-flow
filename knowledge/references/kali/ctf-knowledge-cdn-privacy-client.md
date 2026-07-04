# CTF CDN Privacy And Client Security

## CDN And Cache

- Inspect host, path, query, method, headers, cookies, cache-control, vary, and
  redirect behavior.
- Compare cache keys by changing harmless headers or query order.
- Look for origin leaks, stale cache, cache poisoning, path normalization, and
  host header confusion.
- Compare proxy and origin parsing for multi-slash paths, encoded slashes,
  host header variants, cache busters, query order, `Vary`, and unkeyed
  headers.

## Privacy Security

- Identify what data is sensitive in the challenge model: identity, location,
  token, cookie, fingerprint, image metadata, or logs.
- Check minimization, masking, access control, retention hints, and accidental
  disclosure in client bundles or responses.
- For anonymized data puzzles, test linkage, uniqueness, timestamp joins, and
  metadata correlation.

## Client Security

- Inventory browser storage, service workers, CSP, postMessage, WebView bridge,
  extension APIs, native app links, and client-side crypto.
- Check whether trust is placed in modifiable client state.
- Compare same action across browser, mobile, and API if available.
- For client-only secrets, inspect source maps, bundled constants, WebAssembly,
  React/Vue component state, local/session storage, service worker caches, and
  CSP bypass opportunities.

## Useful Tools

Browser devtools/Playwright, curl, mitmproxy/Burp in lab, dig, openssl, jq,
small Python scripts for cache-key and metadata comparison.
