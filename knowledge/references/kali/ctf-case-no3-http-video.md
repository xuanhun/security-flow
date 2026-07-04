# NO.3 Achilles Video

## Metadata

- Event: ByteCTF 143
- Category: Web plus misc-forensics
- Pattern: HTTP session replay and client-side media time gate
- Knowledge link:
  [ctf-knowledge-web.md#http-session-replay-and-client-side-media-gates](ctf-knowledge-web.md#http-session-replay-and-client-side-media-gates)
- Local solution:
  [solution.md](../../../ctf/bytectf-143/challenges/no3-achilles-video/notes/solution.md)

## Prompt Summary

The challenge provides a video that only senior members can watch after an
initial black screen and a smile. A pcapng attachment is also provided, with a
hint that the displayed domain and port in the pcap are unrelated to the target.

## Signals

- The attachment contains clear HTTP traffic, not TLS-only traffic.
- Several `/get-user` requests carry different `sessionId` cookies.
- The web page calls `/ctf/http-risk` and receives media metadata plus
  `start_time` / `end_time`.
- Front-end JavaScript destroys the player when playback passes `end_time`.
- The media URL is encrypted and does not play correctly as a standalone raw
  download.

## Route

1. Use `ctf_pdf.py extract-text` on the provided solution report when available
   to capture intended reasoning and false leads.
2. Use `ctf_artifact.py pcapng-http` to reconstruct HTTP flows and enumerate
   leaked sessions.
3. Compare `/get-user` and `/ctf/http-risk` responses for each candidate
   session.
4. Reject the `is_vip:999` session when evidence shows it returns an Easter
   video rather than the target media.
5. Inject the real `is_vip:1` session into the browser context and let the
   original player load the encrypted video.
6. Use `ctf_browser.sh video-captures` and `contact-sheet` to reconstruct the
   short-lived flag fragments from rendered frames.

## Replay Commands

```bash
python scripts/sec.py probe artifact pcapng-http \
  --case-dir ctf/bytectf-143/challenges/no3-achilles-video \
  --input ctf/bytectf-143/reports/ctf-2023-http.pcapng \
  --label pcap-http \
  --save-streams \
  --strings

python scripts/sec.py probe browser video-captures \
  --case-dir ctf/bytectf-143/challenges/no3-achilles-video \
  --url https://a37f6d774d8298ae95c08e6366ee53aa.ctf.bytedance.net \
  --label vip1-dense \
  --cookie sessionId=d3ccbf4d918906692117c981e275baec \
  --times 14,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,19.5,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27,27.5,28,28.5,29,29.5,30,30.5,31 \
  --wait-ms 5000 \
  --timeout-ms 90000 \
  --width 1365 \
  --height 900

python scripts/sec.py probe browser contact-sheet \
  --case-dir ctf/bytectf-143/challenges/no3-achilles-video \
  --match '^vip1_dense-t.*-video\.png$' \
  --label vip1-dense-videos \
  --columns 5 \
  --width 1800
```

## False Leads

- Treating the numerically highest role (`is_vip:999`) as the target VIP
  without checking the returned media.
- Downloading the encrypted MP4 directly instead of using the page player.
- Sampling only one late frame; the flag appears as moving fragments across
  multiple frames.

## Final

`flag{Victorybelongstous}`
