# Interest Circle

## Metadata

- Event: ByteDance CTF
- Category: Web
- Pattern: encrypted mobile API envelope plus cross-object approval mismatch
- Knowledge link:
  [ctf-knowledge-web.md#encrypted-mobile-api-envelopes-with-cross-object-approval-checks](ctf-knowledge-web.md#encrypted-mobile-api-envelopes-with-cross-object-approval-checks)
- Local solution:
  [solution note](../../../ctf/bytedance/interest-circle/notes/solution.md)

## Prompt Summary

The challenge asks the player to join an interesting circle. The landing page
only exposes an APK, so the real route starts from the mobile client and ends
in a server-side circle approval flaw.

## Signals

- The website is mostly static and advertises `chall.apk`.
- Decompiled sources expose concrete `/users/*` and `/circle/*` endpoints.
- The mobile app wraps each API body in an AES-CBC JSON envelope instead of
  sending plain JSON.
- Nearby-circle enumeration reveals private circles but detail access is gated
  on membership.
- Joining a private circle returns a request id and keeps detail access denied.
- Approval is a separate API that takes both `circle_id` and `request_id`.
- Creating a controlled private circle yields a normal admin context for one
  circle id.

## Route

1. Capture the landing page and download the APK.
2. Use `ctf_mobile.py` to summarize and decompile the APK.
3. Recover the AES envelope format and key derivation, then replay it with
   `ctf_web.py aes-envelope-request`.
4. Register and log in with a controlled account.
5. Enumerate circles through `/circle/nearby`; identify private target circle
   `id=7`.
6. Infer the circle's coordinates by probing `/circle/nearby` radius behavior
   from several points, then join from near Reykjavik.
7. Save the returned join `request_id`.
8. Create a private controlled circle to become admin of that new circle.
9. Call `/circle/approval` with the controlled `circle_id` but the target
   circle's `request_id`.
10. Read `/circle/detail` for `circle_id=7` and recover the flag from the
    returned member signature.

## Replay Commands

```bash
python scripts/sec.py probe mobile apk-summary \
  --apk ctf/bytedance/interest-circle/files/chall-apk.apk \
  --output ctf/bytedance/interest-circle/artifacts/chall_apk-summary.json

python scripts/sec.py probe mobile jadx-decompile \
  --apk ctf/bytedance/interest-circle/files/chall-apk.apk \
  --output-dir ctf/bytedance/interest-circle/files/chall-apk-jadx \
  --output ctf/bytedance/interest-circle/artifacts/chall-apk-jadx-jadx.json

python scripts/sec.py probe web aes-envelope-request \
  --case-dir ctf/bytedance/interest-circle \
  --url /circle/nearby \
  --method POST \
  --auth-token '<bearer_token>' \
  --json '{"latitude":0,"longitude":0,"radius":20000}' \
  --label nearby_global

python scripts/sec.py probe web aes-envelope-request \
  --case-dir ctf/bytedance/interest-circle \
  --url /circle/approval \
  --method POST \
  --auth-token '<bearer_token>' \
  --json '{"circle_id":13,"request_id":"4991b936-2beb-4e01-a384-4137ff069fc3"}' \
  --label approve_join7_via_own_circle
```

## False Leads

- Treating the AES envelope itself as the challenge end state instead of a
  transport wrapper to remove first.
- Spending time on JWT signature forgery after a normal login already works.
- Assuming the 2 km radius check is the only meaningful access-control
  boundary.
- Trying to approve the target request with `circle_id=7` before creating a
  controlled admin circle.

## Final

`flag{ae5b4fe788c53cee3375324b27c851e934bf73642a2b0b39df5723d9}`
