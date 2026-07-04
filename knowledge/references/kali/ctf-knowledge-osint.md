# CTF OSINT

## First Pass

- Treat OSINT as evidence collection, not guessing. Record query, source URL,
  timestamp, and why the result is tied to the challenge.
- Identify the target type: person, username, organization, domain, IP,
  location, image, document, repository, or service banner.
- Prefer public, challenge-scoped sources. Avoid private-account access,
  harassment, doxxing, or real-world contact.

## Routes

### DNS, WHOIS, And Web Archives

- Check `A`, `AAAA`, `CNAME`, `MX`, `TXT`, DNSSEC, zone-transfer mistakes,
  historical DNS, WHOIS, ASN, and certificate transparency.
- Use web archives for removed pages, old robots files, exposed directories,
  and historical metadata.

### Username And Social Graphs

- Search exact username, aliases, avatar reuse, profile IDs, old handles,
  public posts, and platform-specific metadata.
- Watch false positives: require at least two independent links before treating
  an account as the same identity.

### Image And Geolocation

- Inspect metadata first, then crop distinctive regions for reverse image
  search. Check signs, architecture, road markings, vegetation, shadows, and
  mirrored/reflected text.
- For JPG/TIFF location clues, run `ctf_image.py exif-gps` before reverse image
  search. Preserve the original hash, raw EXIF GPS DMS values, decimal
  coordinate, and coordinate-system candidates.
- Convert MGRS, plus codes, What3Words, or coordinates when the clue format
  suggests a location encoding.
- For mainland China POIs, do not assume one datum. Try the raw coordinate and
  WGS84/GCJ-02/BD-09 variants against the map provider used by the challenge,
  then trust the POI whose map label and nearby context match the prompt.

### Image Geolocation To Plus Code Crypto Key

- Signal: an image or screenshot gives a real-world location clue, and a crypto
  note says the key format resembles `________+__`, "Google knows", "Maps", or
  another Google Maps hint.
- First probes: hash and metadata-check the image; OCR visible UI/caption text;
  search distinctive mural/sign/place phrases; collect candidate POI
  coordinates from public map pages; convert coordinates to Google Maps Plus
  Codes / Open Location Codes.
- Common route: generate Plus Codes for the exact POI and a small neighborhood
  grid, then test deterministic key derivations against the provided cipher.
  For AES-256-CBC, start with raw code, normalized case variants, and
  `sha256(plus_code)` as the 32-byte key when no explicit KDF is given.
- Location pitfall: the correct Plus Code may be the exact photographed object
  or nearby street/courtyard center, not the broader area label shown by a
  social-media location tag. Try the POI, area center, and nearby map geometry.
- Crypto pitfall: do not submit the location or leaked credential before
  decrypting the challenge note. The proof should be the plaintext recovered by
  the stated cipher with the derived key.
- Evidence to keep: original image hash, metadata result, OCR/search queries,
  candidate coordinates, generated Plus Codes, failed and successful KDF/mode
  attempts, and a minimal replay command.
- Example cases:
  [The Careless Developer](ctf-case-the-careless-developer.md).

### POI Review To Cross-Platform Identity Pivot

- Signal: a prompt gives a known place, a JPG modification time, a suspicious
  public reviewer/profile ID, or asks for "social engineering" rather than pure
  image forensics.
- First probes: extract the artifact timestamp and EXIF GPS; search the exact
  POI name; sort or inspect recent reviews; compare review time with the
  artifact modification time; save the review URL/screenshot and reviewer ID.
- Common route: pivot from the reviewer ID to other public platforms by exact
  handle search, then read only public profile fields such as nickname, bio,
  signature, comments, pinned posts, and visible contact hints. Decode obvious
  encodings like Base64 before treating a contact field as an account ID.
- OCR/visual pitfall: Base64 strings in screenshots often confuse `l`, `1`,
  `I`, `O`, and `0`. Decode multiple plausible candidates and prefer the one
  that produces the platform account or handle confirmed by the next evidence
  step.
- Safety boundary: do not message, harass, or socially manipulate real users.
  In CTFs, prefer public search/profile previews and stop once the public
  challenge-controlled profile exposes the flag.
- False leads: using review sentiment as the answer, trusting a same-name
  profile without time or avatar/context linkage, submitting an encoded contact
  string before decoding, or continuing to reverse image search after metadata
  and review timing already identify a stronger route.
- Useful tools: `ctf_image.py exif-gps`, `ctf_crypto.py triage`, browser/search
  screenshots, platform search, EXIF timestamp viewers, and map POI pages.
- Evidence to keep: original artifact hash, EXIF/timestamp JSON, search query,
  POI page/review screenshot, reviewer ID, cross-platform search result,
  decoded contact hint, final public profile screenshot, and the extracted flag.
- Example cases:
  [Social Engineering HackMeIfYouCan](ctf-case-social-engineering-hackmeifyoucan.md).

### Public Repositories And Documents

- Search commit history, author emails, issue comments, leaked `.DS_Store`,
  public docs/sheets export views, and archived attachments.
- Keep a copy of relevant public artifacts in the case evidence directory when
  allowed by the challenge.

## Useful Tools

whois, dig, curl, nmap service fingerprints, exiftool, ImageMagick,
`scripts/ctf_image.py exif-gps`, `scripts/ctf_crypto.py triage`,
browser/search engines, Wayback CDX, crt.sh, Shodan when authorized, and small
scripts for timestamp or coordinate conversion.
