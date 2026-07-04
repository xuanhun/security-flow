# Local iOS CTF03 Assets.car

## Metadata

- Category: mobile, iOS, local CTF artifact.
- Pattern: CoreUI `Assets.car` image extraction requires the macOS CoreUI
  export path when Linux reconstruction stalls.
- Knowledge: [ctf-knowledge-mobile.md#ios-assetscar-coreui-extraction-gate](ctf-knowledge-mobile.md#ios-assetscar-coreui-extraction-gate).
- Evidence: [local-demo-ios-ctf03](../../../engagements/local-demo-ios-ctf03).

## Signal Inventory

- The IPA contained `Payload/ctf03.app/Assets.car`, storyboard/nib files, an
  arm64 Mach-O, and provisioning metadata.
- Static disassembly showed the app-side `ViewController` had no useful custom
  password or flag check beyond normal lifecycle code.
- `Assets.car` strings and parsed structure exposed a named image resource,
  CoreUI metadata, `dmp2`, `bvx2`, `BGRA`, and LZFSE-compressed bitmap data.

## Route Decision

The local Linux route could inventory the IPA, extract the `.car`, locate the
compressed rendition, decompress LZFSE data, and render BGRA-like candidates.
Those candidates remained black, noisy, or stride-dependent after dimension,
alpha, bitplane, channel, and byte-level checks.

The durable lesson is the stop condition: do not treat the LZFSE output as the
final exported image. For modern CoreUI renditions, reproduce CoreUI's export
semantics with a macOS toolchain before continuing image forensics.

## macOS Replay Commands

Copy the extracted `Assets.car` to macOS and try the native tool first:

```bash
mkdir -p out
assetutil --info Assets.car
assetutil --extract out Assets.car
```

If that macOS build does not support extraction or omits the target rendition,
use a CoreUI-backed extractor on macOS:

```bash
acextract -i Assets.car -o out
cartool Assets.car out
```

Asset Catalog Tinkerer is also useful for manual inspection when a GUI is more
convenient.

## Evidence To Preserve

- Original IPA hash and extracted `Assets.car` hash.
- `ctf_mobile.py ipa-summary --extract` output.
- Resource names and offsets for `ISTC`, `dmp2`, `bvx2`, and named PNG/JPG
  strings.
- Failed local render candidates that justified the macOS extractor gate.
- macOS extractor command, exported files, and final readable crop.

## False Leads

- Assuming `.car` is a normal ZIP or ordinary PNG container.
- Stopping after raw LZFSE decompression because the output has BGRA-looking
  bytes.
- Spending unbounded time on Linux stride guesses after CoreUI-specific
  metadata is confirmed.
- Trying to run macOS Mach-O extractor releases or CoreUI-linked Xcode projects
  directly on Linux.
