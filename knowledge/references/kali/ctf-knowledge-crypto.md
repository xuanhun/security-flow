# CTF Crypto

## First Pass

- Preserve exact ciphertext, nonce, IV, key hints, public keys, source code,
  oracle behavior, and output format.
- Classify the primitive before attacking: encoding, hash, classical cipher,
  stream cipher, block mode, RSA, ECC, lattice, RNG, or protocol.
- Check whether the challenge is about misuse rather than breaking the
  primitive.
- Preserve oracle transcripts exactly: query, response, error, timing, and
  whether ciphertexts or messages can be modified.

## Route Map

### Encoding And Obfuscation

- Try hex/base64/base32/base58/url/html, compression, XOR, byte order, and
  repeated layers.
- Signal: printable-looking alphabets, padding, magic bytes after decode.
- For text-only puzzles, start with `ctf_crypto.py triage` to preserve the
  exact value, candidate alphabets, Base64/Base64URL decode attempts, entropy,
  and any inline flag-shaped strings.

### Morse And Two-Symbol Encodings

- Signal: only two visible symbols plus unusual separators, escaped separators,
  slashes, repeated whitespace, or text where one symbol pair may stand for dot
  and dash.
- First probe: use `ctf_crypto.py morse` to preserve the raw text, separator,
  decoded normal mapping, and swapped dot/dash mapping in one artifact.
- CTF pitfall: online decoders may disagree about spaces, slashes, or custom
  separators. Treat decoder output as a hypothesis until the exact split and
  symbol mapping are recorded locally.
- If one mapping produces readable words and the swapped mapping produces
  unknowns or nonsense, promote the readable output as a clue for the next
  layer; do not over-translate source-language text without another signal.

### Book Coordinates And Classical Keys

- Signal: title names a source text and hints look like `paragraph.word.char`
  or `book.line.word` style three-part coordinates.
- First probes: preserve the exact source text, count words per paragraph, and
  use `ctf_crypto.py book-extract` or `ctf_crypto.py line-extract` before
  trying derived keys in downstream ciphers.
- Common route: coordinates produce a short key, then a Vigenere-style,
  Caesar, XOR, or layered encoding step reveals the answer.
- False lead: using a nearby lorem/example text whose paragraph word counts do
  not cover the coordinates; record out-of-range counts instead of forcing a
  key.
- Evidence to keep: source text path or URL, coordinate list, extracted words
  and letters, derived key, and the verification decode command.

### XOR And Stream Ciphers

- Look for reused key/nonce, known plaintext, repeated period, crib dragging,
  or biased RNG.
- Keep scripts parameterized so new cribs can be tried quickly.

### Block Ciphers

- Identify mode. ECB leaks blocks; CBC may expose padding oracle or bit flipping;
  CTR/GCM fail under nonce reuse.
- Keep IV, nonce, tag, and associated data separated in notes.
- Check JSON/cookie structures for block alignment, cut-and-paste, IV forgery,
  Unicode decode side channels, and authenticated-data mistakes.

### RSA

- Check small exponent, shared modulus, common factors, small `d`, close primes,
  broadcast, partial key leaks, and bad padding.
- Start with `n`, `e`, ciphertext inventory and `gcd` across moduli.

### ECC And Lattice

- Look for nonce reuse, biased nonce, invalid curve, small subgroup, or leaked
  nonce bits.
- Do not assume lattice is needed until simpler misuse is ruled out.
- For lattice/HNP/LWE, record sample count, modulus, dimensions, noise bounds,
  leaked-bit positions, and whether the equations are over integers, mod `n`,
  or GF(2).

### Hash And MAC

- Distinguish hash, HMAC, checksum, and password hash.
- Check length extension only for raw Merkle-Damgard hash MACs, not HMAC.
- Check CRC or linear MACs for GF(2) linearity, parameter override after
  lenient decoding, and secret-prefix constructions.

### PRNG And Oracles

- Signal: time-based tokens, shuffled pixels, repeated random output, lottery,
  UUID-like values, or challenge source using `rand`, MT19937, LCG, XorShift,
  or JavaScript `Math.random`.
- First probes: collect consecutive outputs, estimate seed window, recover
  state from enough output, and test forward/backward prediction.
- Go `math/rand` OTP route: if source seeds with `time.Now().UnixMicro()` and
  returns a later random string such as an `id`, brute-force the request-time
  microsecond seed, regenerate the hidden code and returned id in order, then
  verify with the same session. Use `ctf_prng.py go-rand-otp`.
- Fixed shuffle oracle route: if a service returns `shuffle(secret)` and lets
  you submit equal-weight anagrams that are shuffled with the same permutation,
  recover the permutation by sending balanced binary code columns. Map each
  output position back to its encoded input index, invert the target shuffle,
  then decode the recovered bits. Use `ctf_tcp.py shuffle-oracle-solve`.
- Oracle route: if a decrypt/sign/check endpoint leaks parity, padding, length,
  timing, or success/failure, model the leak before brute force.

## Useful Tools

Python, Go, sage, sympy, pycryptodome, openssl, RsaCtfTool, z3, CyberChef.
