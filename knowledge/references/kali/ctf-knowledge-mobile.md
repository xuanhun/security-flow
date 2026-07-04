# CTF Mobile And Android

## First Pass

- Preserve the APK/IPA hash and package metadata.
- Extract manifest, permissions, activities, deep links, exported components,
  strings, assets, native libraries, and network config.
- Identify whether the goal is static secret recovery, runtime bypass, traffic
  inspection, native reverse, or client-server logic.

## Android Routes

- Static: apktool, jadx, strings, assets, resources, hardcoded endpoints,
  crypto keys, and feature flags.
- Activity exposure: compare `AndroidManifest.xml` exported state with call
  chains in source. A non-exported activity can still be reached indirectly
  when an exported in-app component calls it with `startActivityForResult`,
  and `getCallingActivity()` checks may accept that exported caller.
- Dynamic: emulator/device logs, Frida hooks, root/debug checks, SSL pinning
  only in a lab device, and local storage.
- Native: inspect `.so` with strings, symbols, Ghidra/radare2, JNI bridges,
  and anti-debug behavior.
- WebView: JavaScript bridge exposure, file access, deep links, and origin
  checks.
- Frameworks: check Flutter/Dart AOT, Unity IL2CPP/Mono, React Native bundles,
  Cordova/Ionic WebViews, and asset-packaged scripts separately from native
  code.
- Runtime: hook only in a lab device or emulator; record the method/class,
  arguments, return value, and reason the hook is in scope.

### Non-Exported Activity Reached By Exported Caller

- Signal: the prompt mentions non-exported/protected activities, Manifest has a
  flag-bearing activity with `android:exported="false"`, and DEX/source strings
  mention `getCallingActivity`, `startActivityForResult`, or a second exported
  activity.
- First probes: run `ctf_mobile.py apk-summary`, then
  `ctf_mobile.py jadx-decompile`; compare Manifest components against source
  call chains.
- Common route: an exported in-app activity can launch a non-exported activity.
  If the protected activity checks `getCallingActivity()`, find the accepted
  caller and reconstruct the flag from that protected activity's UI/log logic.
- False leads: assuming `exported=false` makes the code unreachable, launching
  the protected activity directly and missing the caller check, or searching
  only for a complete literal `flag{...}`.
- Evidence to keep: APK hash, decoded Manifest component table, caller source,
  protected activity source, literal/constants source, and reconstructed flag.
- Example cases: [NO.12 EzAndro](ctf-case-no12-ezandro.md).

### WebView Tool Browsing With Userinfo Allowlist Confusion

- Signal: an Android app exposes a deeplink that can reach an AI/chat workflow,
  the chat workflow has a browser or URL-opening tool, and the app stores a
  target-domain secret in `CookieManager`.
- First probes: decompile the APK, map exported deeplink handlers to activity
  launches, grep for `addJavascriptInterface`, `loadUrl`, `CookieManager`,
  regex URL checks, and tool names such as `browse_url`.
- Common route: use the exported deeplink to inject a chat prompt or intent
  extra, ask the in-app tool to browse a URL that passes the app's allowlist
  but resolves to a controlled host, then use the exposed JS bridge from the
  controlled page. A URL like `https://m.toutiao.com@callback.example/p` can
  pass a prefix regex for `m.toutiao.com` while WebView actually requests
  `callback.example`.
- Cookie relay variant: if the JS bridge posts a delayed native check based on
  `webView.getUrl()`, call the bridge from the controlled page and navigate the
  WebView to the cookie domain before the delayed check runs. The callback URL
  receives the cookie in the bridge's outbound request.
- False leads: trusting regex URL validation as hostname validation, checking
  only Manifest deeplinks and missing `Intent.parseUri`, or calling the bridge
  after navigation when the controlled JavaScript context is gone.
- Evidence to keep: manifest exported component, deeplink parser source,
  AI/tool prompt path, allowlist regex, JS bridge source, controlled callback
  log, and final submitted deeplink.
- Example cases: [DouXiaoBao](ctf-case-douxiaobao.md).

### Media Object API With Nested Cover Metadata

- Signal: a mobile short-video or media app exposes only sanitized preview media
  in normal UI, while decompiled code mentions `item_id`, `vid`, original
  object downloads, native bridges, or separate media lookup endpoints.
- First probes: decompile Java/Kotlin and native libraries. Map the preview
  flow separately from original-object flow. Grep native strings for URL paths,
  query keys, request headers, and bridge mode values. Preserve each candidate
  `item_id`, `vid`, and response.
- Common route: list challenge-scoped media, resolve each item to the backend
  video/object id, reconstruct the native object request, then inspect the
  original media file. For MP4, parse boxes such as `moov/udta/meta/ilst/covr`;
  cover JPEGs can contain EXIF and an embedded EXIF thumbnail with overlaid
  text or encoded coordinates.
- False leads: searching real public social platforms for the person, trusting
  preview MP4 metadata as complete, grepping only Java source and missing JNI
  request parameters, or stopping at the top-level JPEG EXIF without checking
  the 1st IFD thumbnail.
- Evidence to keep: APK hash, decompiled source paths, native strings or
  disassembly showing request shape, object response headers, original MP4
  hash, MP4 box tree, extracted cover/thumbnail files, OCR or decode transcript,
  and a note if coordinate submission was intentionally skipped.
- Example cases: [KotKit](ctf-case-kotkit.md).

## iOS Routes

- Inspect plist, entitlements, URL schemes, strings, binary symbols, and local
  storage.
- When `Assets.car` contains the only promising resource, treat it as a
  CoreUI compiled asset catalog rather than a normal archive. Linux-side
  `strings`, LZFSE, BGRA rendering, stride guesses, and bitplane scans can
  prove that a `dmp2`/`bvx2` rendition exists, but they may not faithfully
  reproduce CoreUI's export semantics. If the decompressed image is black,
  noisy, or only partially legible after local probes, move to a macOS
  extractor gate instead of spending cycles hand-reconstructing the PNG.
- Dynamic testing needs a properly authorized lab device.

### iOS Assets.car CoreUI Extraction Gate

- Signal: an IPA has no useful Mach-O check logic, `Assets.car` strings show
  `CoreUI`, `ISTC`, `BGRA`, `dmp2`, `bvx2`, or a named PNG/JPG resource, and
  local LZFSE/BGRA rendering produces black, noisy, or stride-dependent images.
- First probes: run `ctf_mobile.py ipa-summary --extract`, preserve the
  extracted `Payload/*.app/Assets.car`, and record resource names plus
  `dmp2`/`bvx2` offsets. Use local rendering only to confirm the resource
  exists, not as final proof when CoreUI metadata is unresolved.
- Common route: export the `.car` on macOS with the native CoreUI toolchain,
  then continue normal image inspection on the exported PNG/PDF/JPG. Prefer
  built-in `assetutil` first when available:

  ```bash
  mkdir -p out
  assetutil --info Assets.car
  assetutil --extract out Assets.car
  ```

  If `assetutil --extract` is unavailable or incomplete on that macOS version,
  use a CoreUI-backed extractor such as Asset Catalog Tinkerer, `acextract`, or
  `cartool` on macOS:

  ```bash
  acextract -i Assets.car -o out
  cartool Assets.car out
  ```

- False leads: treating LZFSE output as final contiguous PNG/RGBA pixels,
  trusting one guessed stride as the exported image, or assuming a Linux build
  of an Xcode/CoreUI project can run without macOS private frameworks.
- Evidence to keep: IPA hash, `Assets.car` path and hash, resource names,
  `dmp2`/`bvx2` offsets, local failed render evidence, macOS extractor command,
  exported image path, and the final readable crop or decoded text.
- Example cases: [Local iOS CTF03 Assets.car](ctf-case-local-ios-ctf03-assets-car.md).

### iOS Format Gate With Visual Algorithm Hint

- Signal: the binary validates only a broad flag-shaped format such as
  `flag{[a-z0-9]{32}}`, then reveals an image or asset rather than checking a
  unique secret. The prompt asks for an algorithm, password, or magic code.
- First probes: reverse the input gate enough to prove whether it enforces a
  real secret or only unlocks a resource. If it is only a format gate, export
  the hidden resource and solve the visual clue instead of brute forcing the
  input field.
- Common route: identify the visual clue or CoreUI metadata as an algorithm or
  concept, normalize the answer to lowercase, and test the common CTF
  convention `flag{md5(answer)}` when the app or prompt requires a
  32-character lowercase alphanumeric value. Keep each candidate separate until
  a judge, user, or stronger local evidence verifies it.
- False leads: assuming any accepted `flag{32}` is the final password,
  continuing binary patching after proving the app accepts a broad regex, or
  promoting a visual guess such as `knapsack` before verification.
- Evidence to keep: disassembled input checks, exported resource, metadata
  scans proving no direct hidden text, candidate answer normalization, and the
  exact digest command.
- Example cases: [Local Magic Code Challenge](ctf-case-local-magic-code-challenge.md).

## Useful Tools

apktool, jadx, aapt, adb, frida, objection, mitmproxy/Burp in lab, Ghidra,
radare2/rizin, Il2CppDumper, Blutter when Flutter artifacts are present.

Skill-local commands:

- `ctf_artifact.py inventory` and `zip-inspect` for first-pass APK hashes,
  ZIP entries, DEX files, strings, and safe extraction.
- `ctf_mobile.py apk-summary` for APK entry and DEX inventory.
- `ctf_mobile.py ipa-summary` for IPA app bundle, plist, Mach-O, strings,
  `Assets.car`, and safe extraction.
- `ctf_mobile.py jadx-decompile` for skill-local jadx decompilation and
  Manifest component summaries.
- `ctf_mobile.py source-grep` for replayable source evidence lookup.
