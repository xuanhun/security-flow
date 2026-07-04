# CTF Case: KotKit

- Event: ByteCTF challenge 143
- Category: mobile / privacy compliance
- Pattern: Android media object API to MP4 cover EXIF thumbnail coordinate leak.
- Final answer: `-15.164285,-39.807139`

## Prompt Summary

The challenge asks for the home coordinate of a KotKit creator named `viki`.
The only in-scope sources are the challenge web page and the provided KotKit APK
archive.

## Signals

- The web page asks for signed coordinates and has only a small quick-check
  gate before coordinate submission.
- The APK contains `feed_posts.json`, remote profile logic for the exact query
  `viki`, and native bridge code.
- Native strings include `/gateway/object/ping`, `/gateway/object/file`,
  `?vid=`, `&address=`, and `X-KotKit-Bridge-Mode`.

## Route

1. Decompile the APK and map the remote-media flow:
   - `/gateway/media/list` lists `item_id` and preview file names.
   - `/gateway/search/<item_id>` returns a `vid`.
   - the Java bridge validates `v24[a-z0-9]{29}` video IDs.
2. Reverse the native object downloader enough to recover the full request:
   - `/gateway/object/<ping|file>?vid=<vid>&address=<hostPortSuffix>`
   - `X-KotKit-Bridge-Mode: exec`
3. Probe only the three challenge-provided `vid` values. The second item is the
   only available original source.
4. Download the original MP4 and parse MP4 boxes. The `ilst/covr` box contains
   a cover JPEG with EXIF.
5. Parse the JPEG EXIF 1st IFD. The embedded thumbnail has a visible Base64
   string:

   ```text
   LTE1LjE2NDI4NSwtMzkuODA3MTM5
   ```

6. Decode Base64 to get:

   ```text
   -15.164285,-39.807139
   ```

## Evidence

- Solution note:
  `../../../ctf/bytectf-143/challenges/kotkit/notes/solution.md`
- Downloaded original MP4:
  `../../../ctf/bytectf-143/challenges/kotkit/responses/object_exec/viki2_file.body`
- Extracted cover:
  `../../../ctf/bytectf-143/challenges/kotkit/files/viki2_covr_exif.jpg`
- Extracted EXIF thumbnail:
  `../../../ctf/bytectf-143/challenges/kotkit/files/viki2_exif_thumbnail.jpg`
- White-mask crop:
  `../../../ctf/bytectf-143/challenges/kotkit/files/thumbnail_crops/text_band_tophat51_cc_dilate.png`

## Lessons

- Do not pivot to real-world social platforms when a privacy challenge provides
  a closed APK/backend scope.
- For media apps, preview URLs can differ from original-object URLs. Decompile
  both Java and JNI code before assuming all media has been inspected.
- MP4 `ilst/covr` cover art can preserve JPEG EXIF, including a second embedded
  thumbnail. Inspect nested media metadata, not just top-level strings.
