# External CTF Pattern Map

Source distilled from `ljagiello/ctf-skills`
(`https://github.com/ljagiello/ctf-skills`, commit
`1af14f9030fee9da46014a8a3ed61a555b81ab98`). Use this as a routing checklist,
not as a replacement for local evidence or the category knowledge files.

## How To Use

- Start with the local closed loop: initialize a case, run the closest skill
  tool, read evidence, then choose a category.
- Use this map when the challenge category is blurry or when the first route
  stalls.
- Load only the matching local category reference after choosing a route.
- Promote any repeated probe into `scripts/` before relying on it in a solve.

## Category Signals

### Web

- Signals: HTTP app, API, browser bot, JWT/cookie/session, upload form,
  template, webhook, OAuth/OIDC/SAML, GraphQL, Node.js, Web3, or exposed source.
- First checks: page snapshot, JS bundle API extraction, route inventory,
  unauthenticated/authenticated diff, alternate methods, alternate content
  types, headers, redirects, and hidden metadata paths.
- Pattern families: SQL/NoSQL/LDAP/XPath injection, SSTI, SSRF parser mismatch,
  XXE/XML upload, JWT/JWK/KID confusion, OAuth/SAML validation gaps, CORS,
  XSS/admin bot, CSP/XS-Leak/CSS exfil, file upload polyglot, deserialization,
  prototype pollution, Node VM escape, cache poisoning, and business logic.

### Crypto

- Signals: ciphertext/key material, public keys, signatures, nonce/IV/tag,
  oracle endpoint, custom RNG, math source, ZKP, lattice/LWE, or stream output.
- First checks: classify primitive, preserve exact bytes, inventory repeated
  nonce/key/modulus, test known plaintext, inspect padding/errors, and separate
  encoding from cryptography.
- Pattern families: RSA small exponent/shared factor/close primes/partial key,
  raw hash MAC length extension, ECB/CBC/CTR/GCM misuse, padding and parity
  oracles, XOR/stream key reuse, MT/LCG/LFSR PRNG recovery, ECDSA/DSA nonce
  reuse, invalid-curve/small-subgroup ECC, and lattice from partial bits.

### Forensics And Misc

- Signals: pcap, memory/disk image, archive, image/audio/video, USB capture,
  PDF/Office file, logs, QR/barcode, esolang, jail, sandbox, or puzzle service.
- First checks: hash originals, identify file types, inspect metadata and magic
  bytes, extract strings, entropy, embedded files, streams, frames, and timing.
- Pattern families: archive repair, weak zip crypto, disk deleted file recovery,
  memory process/network artifacts, DNS/ICMP/TCP covert channels, USB HID key
  reconstruction, image LSB/palette/alpha/slack stego, audio spectrogram/DTMF,
  video frame diff/averaging, Unicode/base-N encodings, pyjails/bashjails, and
  constraint solving.

### Reverse And Pwn

- Signals: ELF/PE/Mach-O/APK/WASM/firmware, stripped binary, custom VM,
  anti-debug, remote service crash, heap/stack terms, shellcode, ROP, seccomp.
- First checks: file type, architecture, strings/imports, checksec, run only in
  a controlled local setup, collect crash offset/registers, and identify input
  parsing before exploit work.
- Pattern families: static and dynamic tracing, anti-analysis bypass, bytecode
  lifting/tracing, symbolic execution, format string, stack/heap primitives,
  tcache/fastbin/FSOP, ret2libc/ret2dlresolve/SROP, sandbox/seccomp bypass, and
  kernel challenges only in lab scope.

### Mobile

- Signals: APK/IPA, deep links, WebView, exported components, native `.so`,
  certificate pinning, Flutter/Unity/React Native, or app-local secrets.
- First checks: manifest/plist, permissions, strings/assets/resources,
  endpoints, storage, native libraries, network config, and anti-debug/root
  behavior.
- Pattern families: hardcoded keys, weak local crypto, exported activity or
  intent abuse, WebView bridge exposure, native JNI logic, smali patching,
  pinning bypass in lab, and runtime hooks.

### OSINT

- Signals: identify a person/place/service, username, domain, social profile,
  image location, DNS clue, archive clue, public repo, or open web source.
- First checks: DNS/WHOIS, web archives, search targeted phrases, reverse image
  search on cropped distinctive regions, metadata, username reuse, public
  commits, and service/banner fingerprints.
- Pattern families: social account history, geolocation, reflected text,
  plus codes/MGRS/What3Words, Google dorks, GitHub/email mining, Telegram bots,
  Shodan fingerprints, `.DS_Store`, and cross-challenge infrastructure reuse.

### Malware

- Signals: suspicious executable/script, C2 traffic, beaconing, packed PE/.NET,
  obfuscated JS/PowerShell, YARA, process injection, or sandbox evasion.
- First checks: static strings/imports/resources, config blobs, PE/.NET
  metadata, script deobfuscation by replacing execution with printing, PCAP
  reconstruction, and sandbox-safe dynamic traces.
- Pattern families: API hashing, VM/debug checks, PyInstaller/.NET unpacking,
  RAT config extraction, RC4/AES C2 protocols, DNS/HTTP/WebSocket C2, injected
  memory regions, and custom alphabet or key derivation.

### AI And ML

- Signals: model weights, classifier, prompt transcript, embedding, watermark,
  adversarial examples, membership/model extraction, or neural-network cipher.
- First checks: input preprocessing, label mapping, thresholds, seeds, model
  architecture, confidence deltas, and benign perturbation behavior.
- Pattern families: prompt injection, retrieval leakage, adversarial examples,
  gradient/weight inversion, model extraction, data poisoning/backdoors, LoRA
  adapter abuse, and watermark residual analysis.

## Tooling Notes

- Prefer the skill wrappers first: `ctf_web.py`, `ctf_browser.sh`, `ctf_pdf.py`.
- Use `kali.py install-tools --profile <profile>` for an install plan before
  installing external tools.
- Useful optional profiles include `ctf-web`, `ctf-crypto`, `ctf-forensics`,
  `ctf-reverse`, `ctf-pwn`, `ctf-mobile`, `ctf-osint`, and `ctf-malware`.
