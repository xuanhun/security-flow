# NO.12 EzAndro

## Metadata

- Event: ByteCTF challenge 143
- Category: Mobile and Android app
- Pattern: non-exported activity reached through an exported in-app caller
- Knowledge link:
  [ctf-knowledge-mobile.md#non-exported-activity-reached-by-exported-caller](ctf-knowledge-mobile.md#non-exported-activity-reached-by-exported-caller)
- Local solution:
  [solution note](../../../ctf/bytectf-143/challenges/no12-ezandro/notes/solution.md)

## Prompt Summary

The challenge hints that an activity remains protected when it is not exported.
The artifact is an Android APK.

## Signals

- `classes4.dex` contains `The flag is in the protected activity!`.
- Business classes include `MainActivity2.kt` and `Showflag.kt`.
- Manifest has `Showflag` with `android:exported="false"`.
- Manifest has `MainActivity2` with `android:exported="true"`.
- `MainActivity2` calls `startActivityForResult(intent, ...)` where the intent
  targets `Showflag.class`.
- `Showflag` checks `getCallingActivity()` and accepts
  `com.example.myapplication.MainActivity2`.

## Route

1. Inventory the APK and locate business DEX strings.
2. Decompile with skill-local jadx using `ctf_mobile.py jadx-decompile`.
3. Compare Manifest exported state with source call chains.
4. Read the protected activity logic and its live literal constants.
5. Reconstruct the flag from the `StringBuilder` sequence.

## Replay Commands

```bash
python scripts/sec.py probe mobile apk-summary \
  --case-dir ctf/bytectf-143/challenges/no12-ezandro \
  --input ctf/bytectf-143/challenges/no12-ezandro/files/ctf-2024_EzAndro.apk \
  --label ezandro_apk \
  --include-entries

python scripts/sec.py probe mobile jadx-decompile \
  --case-dir ctf/bytectf-143/challenges/no12-ezandro \
  --input ctf/bytectf-143/challenges/no12-ezandro/files/ctf-2024_EzAndro.apk \
  --label ezandro_jadx \
  --output-dir ctf/bytectf-143/challenges/no12-ezandro/files/jadx-tool

python scripts/sec.py probe mobile source-grep \
  --case-dir ctf/bytectf-143/challenges/no12-ezandro \
  --source-dir ctf/bytectf-143/challenges/no12-ezandro/files/jadx-tool \
  --label ezandro_sources \
  --pattern 'Showflag|startActivityForResult|getCallingActivity|flag\\{|exported|MainActivity2|ssAry' \
  --ignore-case \
  --ext java --ext xml
```

## False Leads

- Treating `exported=false` as the end of the route. It blocks direct external
  launch, but not an exported internal component that starts it.
- Ignoring `getCallingActivity()`: direct launches may fail the check, while a
  `startActivityForResult` caller can satisfy it.
- Searching only literal `flag{...}`. This APK builds the flag with live
  literal fragments and numeric constants.

## Final

`flag{D0nt_3xp0rt_Unn4c4ssAry_Act1vit14s}`
