# Local Pigskin Insider

## Metadata

- Category: MISC and forensics
- Artifact: ZIP with PNG, WAV, JPEG, and RAR5 archive
- Local evidence:
  `engagements/local-demo-pigskin-insider/`
- Local reproducible outputs:
  `flag{evil*Doggy_Liu}`, `flag{mOnkeySong}`, `PIGGY_SU`, `WICKEDX`
- Live full-chain result:
  password `DoggySUmOnkeySong`, final flag `flag{devil*Pumbaa}`

## Prompt Summary

The challenge asks for the code name of a kung-fu insider. The provided ZIP
contains a folder named `同伙4人众` with one visible suspect photo and three
normal-looking companion files.

## Signal Inventory

- ZIP filenames were UTF-8 Chinese names interpreted as CP437; decoding yields
  `同伙4人众`, `古斯塔沃的照片.jpg`, `猴立松图.png`, `释放PPG.rar`,
  and `flag.wav`.
- `古斯塔沃的照片.jpg` ends with valid JPEG trailer `FF D9`, then a long
  binary ASCII tail.
- `猴立松图.png` is a PDPO logo image with a second PNG appended after the first
  `IEND`.
- The appended PNG has declared dimensions `1064x1270`, but IDAT data aligns
  exactly as `1048x1270` RGB scanlines.
- The RAR5 archive contains a normal text file and an NTFS alternate data
  stream target named `:circle.mp4`.
- The recovered MP4 contains changing stylized QR codes and a kung-fu clip.
- The WAV spectrogram contains clear text, and a late left-channel pulse train
  decodes cleanly as Morse.
- A standalone document QR decodes to a live password page on `qr61.cn`.

## Route

1. Run `ctf_artifact.py zip-inspect --extract` to inventory the ZIP and decode
   mojibake filenames with CP437-to-UTF-8.
2. Inspect the tail of `古斯塔沃的照片.jpg`. After `FF D9`, a binary string
   remains. Group it into bytes and decode as ASCII to recover
   `flag{evil*Doggy_Liu}`. The useful reusable token for the later password is
   `Doggy`.
3. Run `ctf_image.py inspect` on `猴立松图.png`; note
   `appended_magic: png`.
4. Run `ctf_image.py extract-appended --ext png`, then infer the true width
   from IDAT length and valid scanline filter bytes.
5. Run `ctf_image.py render-partial --width 1048 --channels 3 --height 1270`
   to recover the appended monkey image. It shows `flag{mOnkeySong}`, used as
   the RAR password and later contributes `mOnkeySong` to the final web-page
   password.
6. Use local `unrar`/`7z` to inspect the RAR. `vta` shows an `STM` service item
   targeting `:circle.mp4`.
7. Copy the RAR, change the `STM` header type from service header `3` to file
   header `2`, recompute the RAR5 header CRC over the header-size byte plus
   header data, and extract the stream as a normal file.
8. Use ffmpeg `showspectrumpic` on `flag.wav`; the spectrogram text reads
   `WICKEDX`.
9. Isolate the left-channel pulse segment near `12.35s..13.55s`. Using dot
   length about `0.011s`, dash length about `0.029s`, intra-symbol gap about
   `0.008s`, and inter-letter gap about `0.035s`, the Morse groups decode to
   `PIGGY_SU`.
10. Extract and scan frames from `circle.mp4`. The reproducible QR payloads are
    `4QXhocjZ2bFA2TnZnOGY` with center marker `8`, and
    `aHR0cHM6Ly9ieXRlZGFuY2` with center marker `U`.
11. The standalone document QR image decodes to
    `https://qr61.cn/onnK3y/qt05jS0`.
12. That short-link page is live and displays password hint
    `Gustavo's animal code name Piggy's Famliy name 3rd ’s Full codename`.
13. The final page password is `DoggySUmOnkeySong`, assembled from file 1
    `Doggy`, file 3 surname `SU`, and file 2 `mOnkeySong`.
14. Unlocking the page reveals the final image. Downloading the underlying JPEG
    and cropping the vertical banner confirms final flag
    `flag{devil*Pumbaa}`.

## Reusable Lesson

When a RAR5 archive stores a challenge payload as an NTFS alternate data stream,
Linux extraction tools may list the stream but refuse to restore it. If the
stream data is otherwise supported by the extractor, changing only the header
type in a copy can convert the stream into a normal file while preserving the
compressed data area.

When a misc challenge depends on public external content, preserve the exact
URL, password hints, API responses, screenshots, and any intermediate
identifiers while the route is live. Stylized QR codes may need preprocessing
before decoding, and the shortest confirmed route may use a standalone document
QR rather than a guessed intermediate URL path.
