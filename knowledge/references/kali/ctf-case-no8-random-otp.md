# NO.8 Random OTP Address

## Metadata

- Event: ByteCTF 143
- Category: Web / Crypto
- Pattern: Go `math/rand` time-seeded OTP prediction
- Knowledge link:
  [ctf-knowledge-crypto.md#prng-and-oracles](ctf-knowledge-crypto.md#prng-and-oracles)
- Local solution:
  [solution.md](../../../ctf/bytectf-143/challenges/no8-random-otp/notes/solution.md)

## Prompt Summary

The challenge provides a URL and the login phone number `18888888888`. The
attacker has the phone number but not the device receiving the realtime
verification code. The goal is to obtain the verification code and recover the
Heracles address/flag.

## Signals

- The page posts JSON to `/generate-code`, receives an `id`, and later posts
  `{phone, code, id}` to `/verify-code`.
- The source archive contains a Gin application using Redis-backed sessions.
- `/generate-code` seeds `math/rand` with `time.Now().UnixMicro()`, generates
  the hidden 6-digit code first, then generates and returns a 32-character id
  from the same PRNG stream.
- `/verify-code` compares both code and id from the session, then returns the
  flag only when the stored phone is `18888888888`.

## Route

1. Capture the login page and identify `/generate-code` and `/verify-code`.
2. Inspect the attached tar with `ctf_artifact.py tar-inspect --extract`.
3. Browse the local casebook through `Pentesting -> web-service`; no direct
   card matched Go `math/rand` OTP recovery, so promote the missing PRNG route
   into the skill.
4. Install/use a local Go runtime, then run `ctf_prng.py go-rand-otp` to make a
   fresh `/generate-code` request.
5. The tool records the local request time window, receives the returned id,
   brute-forces the Unix microsecond seed with Go `rand.NewSource`, regenerates
   the hidden code and id in order, and posts the recovered code with the same
   session.

## Replay Commands

```bash
python scripts/sec.py knowledge browse \
  --category Pentesting \
  --artifact web-service \
  --cards \
  --limit 8

python scripts/sec.py probe artifact tar-inspect \
  --case-dir ctf/bytectf-143/challenges/no8-random-otp \
  --input ctf/bytectf-143/reports/ctf-2023-random.tar \
  --label attachment_random_tar \
  --extract

python scripts/sec.py probe crypto go-rand-otp \
  --case-dir ctf/bytectf-143/challenges/no8-random-otp \
  --base-url 'https://aebc43f36acff87c338c1e0cff04a545.ctf.bytedance.net' \
  --phone '18888888888' \
  --window-ms 1000 \
  --verify \
  --label go_rand_otp_phone_18888888888
```

## External Sources Used

- Official Go download endpoint: `https://go.dev/VERSION?m=text`
- Official Go `math/rand` source and docs for `NewSource`, `Intn`, and
  `Int31n` behavior.

## Final

`flag{68d09a50278ea377420b2edbe8892216b76cf9a86e16c216682b9682}`
