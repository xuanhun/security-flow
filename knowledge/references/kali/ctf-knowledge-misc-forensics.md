# CTF MISC And Forensics

## First Pass

- Identify file type with magic bytes, extension, metadata, strings, entropy,
  dimensions, and embedded files.
- Keep original artifacts read-only. Work on copies.
- Hash every original file before modification.
- Use `scripts/ctf_artifact.py inventory` on unknown local files before
  tool-specific extraction.

## Routes

### Git Repository History Credential Leak

- Signal: a prompt points to a public source repository, an exposed `.git`
  directory, or a source archive, and current files contain `.env.example`,
  cleaned configuration, suspicious commit messages, or claims that production
  code is clean.
- First probes: record refs, remotes, tags, timeline, and current tree; run
  full-history grep for `key`, `secret`, `token`, `pass`, `api`, and challenge
  flag terms; inspect suspicious commits with `git show --patch`; run a local
  scanner such as `gitleaks` as supporting evidence.
- Common route: a credential is committed briefly, then removed or moved to
  environment variables. Recover the historical value, decode any obvious
  wrapper such as Base64 locally, and verify the exact file, commit, and line.
  Treat the credential as an entry point unless the challenge explicitly says
  the credential itself is the flag; inspect challenge-scoped metadata and
  notes for the next clue.
- Public platform checks: inspect forks, PRs, issues, commit comments, tags,
  releases, actions runs, and wiki/page metadata when the source is hosted on a
  public platform. A fork or issue can preserve evidence missing from current
  refs.
- False leads: stopping at the current tree, treating a clean `git fsck` as a
  complete public-platform audit, validating leaked third-party tokens against
  live services without explicit scope, copying another user's fork name as
  proof, or wrapping an intermediate token as `flag{...}` before testing the
  downstream clue chain.
- Evidence to keep: `git show-ref --head`, chronological `git log`, suspicious
  patch, decode transcript, scanner report, fork/platform query results, and
  a note saying whether live token validation was intentionally skipped.
- Example cases:
  [The Careless Developer](ctf-case-the-careless-developer.md).

### Archive And Container

- Check nested archives, wrong extension, password hints, comments, alternate
  data streams, and corrupted headers.
- For zip: comments, extra fields, weak encryption, known plaintext, CRC hints.
- Use `scripts/ctf_artifact.py zip-inspect --extract` before ad hoc unzip when
  a challenge provides a ZIP, source bundle, or nested attachment. Keep the
  generated entry list, hashes, text samples, and extracted root as evidence.
- For damaged containers, compare magic bytes, central directory/xref tables,
  chunk CRCs, duplicate entries, symlinks, and hidden resource forks.

### Image Stego

- Check metadata, dimensions, palette, alpha channel, LSB planes, appended data,
  QR fragments, and color channel differences.
- Compare visually and by pixel/channel statistics.

### Appended PNG With Corrupted IHDR Dimensions

- Signal: `ctf_image.py inspect` reports large `appended_bytes` with
  `appended_magic: png`, but the extracted tail PNG fails normal parsing with
  decompressed data shorter than the declared width/height requires.
- First probes: run `ctf_image.py extract-appended`, then compare the IDAT
  decompressed byte length against candidate row sizes. Valid PNG scanlines
  begin with filter bytes `0..4`; a width whose row boundaries keep those
  filter bytes valid is a strong repair candidate.
- Common route: run `ctf_image.py render-partial --width <candidate>
  --channels <count>` to render complete scanlines without changing the
  original artifact. Continue visual and string extraction from the repaired
  image.
- False leads: assuming the appended PNG is unrecoverable because viewers
  reject it, or trusting a corrupted IHDR dimension after the IDAT length points
  to a cleaner row geometry.
- Evidence to keep: original and appended hashes, inspect JSON, width/row-size
  calculation, `render-partial` JSON, and the repaired image.
- Example cases:
  [Local Pigskin Insider](ctf-case-local-pigskin-insider.md).

### PNG-Appended HLS Segment Polyglots

- Signal: the prompt mentions strange images or image hosting abuse, a PNG is
  visually trivial such as 1x1, but its file size is much larger than expected.
  A related m3u8 may reference `.png` names as media segments.
- First probes: run `ctf_image.py inspect` and check `appended_bytes`,
  `iend_end_offset`, strings, and `appended_magic`. Confirm the byte after PNG
  `IEND`; MPEG-TS segments commonly begin with sync byte `0x47`.
- Common route: use `ctf_image.py extract-appended --ext ts` on each PNG, then
  rebuild a local m3u8 referencing the extracted TS chunks. Use browser video
  frame capture and a contact sheet to read short-lived visual flags.
- False leads: running only LSB or channel-difference checks on the visible
  1x1 image, or assuming an HLS segment cannot have a misleading extension.
- Evidence to keep: original PNG hashes, inspect summaries, extracted tail
  summaries, local m3u8, browser frame captures, and the flag-bearing frame.
- Example cases:
  [NO.13 Image Hosting Abuse Evidence](ctf-case-no13-image-hosting-abuse.md).

### Audio And Video

- Inspect spectrogram, waveform, metadata, frame differences, subtitles, and
  hidden streams.
- Try speed, phase, DTMF, Morse, SSTV only when signals suggest it.
- When video is encrypted, DRM-like, or tied to a web player/license flow,
  preserve the original browser context and capture rendered frames with
  `scripts/ctf_browser.sh video-captures` before spending time on offline
  decoding. Build a contact sheet when short-lived text fragments appear across
  multiple frames.

### PCAP And Network

- Reconstruct streams, extract files, follow DNS/HTTP/TLS metadata, inspect
  unusual ports, credentials in lab traffic, and encoded payloads.
- Keep packet numbers and stream ids in notes.
- Check covert channels in DNS labels, ICMP payloads, TCP flags, packet lengths,
  inter-packet timing, and protocol fields that look constant or unnecessary.
- If tshark is unavailable, use `scripts/ctf_artifact.py pcapng-http` to extract
  Ethernet/IPv4/TCP HTTP streams and response bodies.

### Logs And Timelines

- Normalize timestamps, identify actor actions, correlate IP/user/session, and
  separate noise from challenge-intended events.

### Memory And Disk

- For memory dumps, start with process list, network sockets, command lines,
  clipboard, environment, file handles, injected regions, and credential stores.
- For disk images, inspect partition tables, deleted files, journal/reflog,
  snapshots, alternate data streams, and unallocated space.

### Jails, Encodings, And Esoteric Puzzles

- For pyjails/bashjails, inventory available characters, builtins, globals,
  imports, file descriptors, environment variables, and error side channels.
- For encoding puzzles, try layered base encodings, Unicode homoglyphs,
  base65536/CJK-like alphabets, QR/barcode variants, esolangs, and audio/visual
  encodings only when the artifact suggests them.

## Useful Tools

`scripts/ctf_artifact.py` for hashing, ZIP inspection/extraction, binary
download, pcapng HTTP extraction, and MP4 box/string inspection;
`scripts/ctf_image.py extract-appended` and `render-partial` for PNG polyglots,
appended payloads, and dimension-corrupted appended PNGs;
`scripts/ctf_browser.sh video-captures` and
`contact-sheet` for web-player video evidence; `scripts/ctf_pdf.py` for PDF
report or artifact text extraction and flag screening; file, xxd, strings,
binwalk, foremost, exiftool, zsteg, stegsolve, wireshark, tshark, volatility3,
sleuthkit, pcapfix, audacity, sonic-visualiser, ffmpeg, ImageMagick, zbarimg.
