# Locale Data — tn-BW

Machine-readable locale settings for Setswana as spoken in Botswana (`tn-BW`).

## Files

| File | Description |
|------|-------------|
| `tn-BW.json` | Primary locale data: currency, numbers, dates, text direction |

## Format

This project uses a human-readable JSON format aligned with CLDR semantics. It is **not** CLDR XML — it is designed to be easy to read, edit, and validate without CLDR tooling. The long-term goal is to contribute verified data upstream to CLDR.

See [docs/contributing/locale-guide.md](../../docs/contributing/locale-guide.md) for field reference and CLDR contribution notes.

## License

Language data in this directory is licensed under **CC BY 4.0**.

## What Needs Verification

The following fields are documented as needing native speaker or official source verification:

- `dates.months_short` — abbreviated month names
- `dates.days_short` and `dates.days_min` — abbreviated day names
- Date format conventions (confirm against official Botswana documents)

Open an issue tagged `locale` and `needs-native-speaker` to contribute verification.
