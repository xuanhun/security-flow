# NO.13 Image Hosting Abuse Evidence

## Metadata

- Event: ByteCTF challenge 143
- Category: MISC and forensics with Web enumeration
- Pattern: directory listing plus signed download, PNG-appended HLS segments
- Knowledge links:
  [ctf-knowledge-web.md#directory-listing-and-signed-download-urls](ctf-knowledge-web.md#directory-listing-and-signed-download-urls),
  [ctf-knowledge-misc-forensics.md#png-appended-hls-segment-polyglots](ctf-knowledge-misc-forensics.md#png-appended-hls-segment-polyglots)
- Local solution:
  [solution note](../../../ctf/bytectf-143/challenges/no13-image-hosting-abuse/notes/solution.md)

## Prompt Summary

The challenge asks for evidence of image hosting abuse hidden in two strange
images. The target initially shows a public video player.

## Signals

- `/static/play.html` fetches `/sign?filename=./static/public_video.mp4`.
- `/static/` has directory listing enabled.
- The listing exposes `private_0.png`, `private_1.png`, and a private m3u8.
- The m3u8 references the two PNGs as media segments.
- Each PNG is only 1x1 by header, but megabytes on disk.
- After the PNG `IEND` chunk, the appended data starts with byte `0x47`,
  consistent with MPEG-TS sync.

## Route

1. Capture the public page and identify the signing/download flow.
2. Use `ctf_web.py signed-download-probe` for listed static files.
3. Inspect the private PNGs with `ctf_image.py inspect`.
4. Extract bytes appended after `IEND` with `ctf_image.py extract-appended`.
5. Build a local m3u8 that references the extracted TS chunks.
6. Use browser video frame capture and contact sheet review to read the flag.

## Replay Commands

```bash
python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no13-image-hosting-abuse \
  --url /static/ \
  --label static_dir \
  --no-redirect

python scripts/sec.py probe web signed-download-probe \
  --case-dir ctf/bytectf-143/challenges/no13-image-hosting-abuse \
  --filename-file ctf/bytectf-143/challenges/no13-image-hosting-abuse/notes/static-listed-files.txt \
  --label static_listed

python scripts/sec.py probe image extract-appended \
  --case-dir ctf/bytectf-143/challenges/no13-image-hosting-abuse \
  --input ctf/bytectf-143/challenges/no13-image-hosting-abuse/files/static_listed-005-private_0.png \
  --label private0_tail \
  --ext ts \
  --min-bytes 100

python scripts/sec.py probe image extract-appended \
  --case-dir ctf/bytectf-143/challenges/no13-image-hosting-abuse \
  --input ctf/bytectf-143/challenges/no13-image-hosting-abuse/files/static_listed-006-private_1.png \
  --label private1_tail \
  --ext ts \
  --min-bytes 100
```

## False Leads

- Brute-forcing static filenames before checking the directory listing.
- Inspecting only visible PNG pixels. The visible image is a 1x1 placeholder.
- Assuming the `.png` extension means the m3u8 cannot be real media.

## Final

`flag{NoSystemIsSafe_dd287692}`
