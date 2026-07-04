# The Careless Developer

## Metadata

- Event: ByteCTF challenge 143
- Category: MISC
- Pattern: public Git repository history credential leak into third-party app
  metadata, then image geolocation to Google Maps Plus Code crypto key
- Knowledge link:
  [ctf-knowledge-misc-forensics.md#git-repository-history-credential-leak](ctf-knowledge-misc-forensics.md#git-repository-history-credential-leak)
  and
  [ctf-knowledge-osint.md#image-geolocation-to-plus-code-crypto-key](ctf-knowledge-osint.md#image-geolocation-to-plus-code-crypto-key)
- Local solution:
  [solution note](../../../ctf/bytectf-143/challenges/the-careless-developer/notes/solution.md)

## Prompt Summary

A colleague published a weather CLI project and claimed it was ready for
production. The task starts from a public GitHub repository and asks the
operator to inspect whether the source is actually clean.

## Signals

- The prompt points to a public repository rather than a live application.
- The commit history contains a suspicious message:
  `Add service credentials and notification config`.
- Current files contain only `.env.example`, so current-tree search alone looks
  clean.
- Repository metadata exposes no useful original releases, actions runs, issues,
  or commit comments in the original project.
- Related public repositories by the same account can preserve the intended
  challenge route even when the first leaked credential is revoked.
- A decoded credential can be an entry point rather than the final flag.
- A clue shaped as `________+__` beside a Google Maps/location hint is an Open
  Location Code / Plus Code candidate, not an arbitrary password format.

## Route

1. Clone the repository locally.
2. Record refs, tags, remotes, and chronological commit history.
3. Search tracked files and full Git history for credential-shaped terms.
4. Inspect commit `5ae7486`, which added `config.json` with concrete service
   values.
5. Decode the base64-wrapped notification token locally.
6. Treat the decoded Discord bot token as an intermediate credential. Use only
   scoped, read-only validation first, such as `/users/@me`.
7. Query application metadata and guild membership while the token is valid.
   In the recorded run, `/oauth2/applications/@me` identified owner
   `upekkha0896`, and `/users/@me/guilds` identified the original guild
   `weather-utils-dev`.
8. Read only channels/messages available to the bot. The recorded run confirmed
   category `Text Channels`, channel `general`, and three setup messages, but
   the token was revoked before full channel/search enumeration completed.
9. Inspect same-owner public repositories, excluding participant/noisy forks
   when requested. Replacement weather bot repositories exposed credentials
   that still had read-only access to the intended developer guild.
10. Read the challenge-controlled `dev-notes` channel. It contained an
    AES-256-CBC note, IV, ciphertext, a Google Maps key hint, and a Kaunas wall
    mural image.
11. Analyze the image as OSINT: verify no useful EXIF/GPS, collect visible
    social/location text, then use public map sources and nearby POIs to narrow
    the location to Kaunas Old Town / Yard Gallery candidates.
12. Generate Google Maps Plus Codes around the candidate coordinates and test
    them as AES-256-CBC keys through deterministic derivations. The successful
    key was `sha256("9G65VVWQ+CW")`, which decrypts the note to the flag.
13. Treat participant-created forks, PR refs, slash commands, and later bot
   installs as noise unless their timestamps and provenance match the original
   challenge setup.

## Replay Commands

```bash
git clone https://github.com/GPA50/Weather-Bot-CLI.git \
  ctf/bytectf-143/challenges/the-careless-developer/repos/Weather-Bot-CLI

git -C ctf/bytectf-143/challenges/the-careless-developer/repos/Weather-Bot-CLI \
  log --oneline --decorate --all

git -C ctf/bytectf-143/challenges/the-careless-developer/repos/Weather-Bot-CLI \
  show --patch 5ae7486

gitleaks detect \
  --source ctf/bytectf-143/challenges/the-careless-developer/repos/Weather-Bot-CLI \
  --report-format json \
  --report-path ctf/bytectf-143/challenges/the-careless-developer/artifacts/scans/gitleaks-weather-bot.json \
  --redact=0 --exit-code 0 --no-color --no-banner

node - <<'NODE'
const crypto = require('crypto');
const key = crypto.createHash('sha256').update('9G65VVWQ+CW').digest();
const iv = Buffer.from('8FF/uvD98djcJTxCTTvYFA==', 'base64');
const ct = Buffer.from(
  'j8RAVbraxsYub/auHaOTzuliBBfIhcePXXPM4K59cLNVCopizNp6iEOIe/gaX52L',
  'base64',
);
const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
console.log(Buffer.concat([decipher.update(ct), decipher.final()]).toString());
NODE
```

## False Leads

- A clean current `config.json` is not proof that credentials were never
  committed.
- Fork names, PR refs, and later slash commands can be noisy. Prefer original
  refs, same-owner repositories, and timestamp-correlated evidence.
- Do not treat leaked third-party tokens as final flags without platform
  confirmation.
- Do not validate leaked third-party tokens against live services unless the
  challenge scope explicitly requires and authorizes that action; when used,
  start with read-only identity checks and stop on revocation/rate limits.
- `git fsck` can rule out local dangling objects, but it does not replace public
  platform checks such as forks, PRs, issues, comments, and tags.

## Evidence To Keep

- Current ref list and chronological commit table.
- Patch for the credential-bearing commit.
- Base64 decode transcript.
- Scanner JSON report.
- Public platform checks.
- Discord read-only API response headers/bodies, guild snowflake timestamps,
  message transcripts, and token revocation status.
- Original image hash and metadata check, relevant public map/POI evidence,
  generated Plus Code candidates, and the minimal decrypt replay.

## Proof Rule

The historical `config.json` patch plus local decoding proves a credential leak,
not the final flag by itself. The decoded-token wrapper was later rejected by
the user, so it must be recorded as negative evidence.

The solved route treats the credential as a pivot to challenge-controlled
developer notes, then treats the image/location clue as the actual key recovery
step. The final proof is:

```text
Plus Code: 9G65VVWQ+CW
Location center: 54.8960625, 23.8898125
KDF: sha256(Plus Code)
Cipher: AES-256-CBC with the provided IV
```

The final flag is recorded in the local solution note. No automatic platform
submission was performed.
