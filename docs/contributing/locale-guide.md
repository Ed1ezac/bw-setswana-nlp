# Locale Data Contribution Guide

`tn-BW` (Setswana — Botswana) is a valid IETF language tag and Unicode locale identifier, but it has incomplete or missing data in most locale registries. This guide explains how to contribute locale data to this project and, eventually, how to submit it upstream to CLDR.

---

## What Locale Data Covers

Locale data encodes the conventions a region uses for:

- **Currency** — symbol, name, subunit, decimal digits
- **Number formatting** — decimal separator, thousands grouping
- **Date and time** — short/medium/long date formats, month names, day names, first day of week
- **Text direction** — left-to-right (Setswana uses Latin script: LTR)
- **Calendar** — Gregorian is the primary calendar in Botswana

This data is what allows software to display "P1,234.56" instead of "$1,234.56", or "Laboraro, 29 Sedimonthole 2024" instead of "Wednesday, September 29, 2024" — correctly, in Setswana.

---

## CLDR Background

The [Unicode Common Locale Data Repository (CLDR)](https://cldr.unicode.org/) is the authoritative source of locale data used by operating systems, browsers, and apps worldwide. CLDR already has some Setswana data (under the `tn` locale tag for South Africa), but `tn-BW` (Botswana-specific) is sparse.

This project maintains its own `data/locale/tn-BW.json` as:
1. A working reference that can be contributed to immediately without CLDR tooling
2. A structured staging ground for eventual CLDR submission

Our JSON format is designed to be human-readable and easy to validate, not CLDR XML — but the field semantics align with CLDR's data model.

---

## The `tn-BW.json` File

Located at `data/locale/tn-BW.json`. Top-level structure:

```
{
  "locale": "tn-BW",
  "currency": { ... },
  "numbers": { ... },
  "dates": { ... },
  "text_direction": "ltr",
  "metadata": { ... }
}
```

### Currency fields

| Field | Description | Botswana value |
|-------|-------------|---------------|
| `code` | ISO 4217 currency code | `BWP` |
| `name` | Full name | Botswana Pula |
| `symbol` | Currency symbol | `P` |
| `subunit` | Subunit name | thebe |
| `subunit_symbol` | Subunit symbol | `t` |
| `decimal_digits` | Standard decimal places | `2` |
| `format` | Number format pattern | `P#,##0.00` |

### Number fields

| Field | Description | Botswana value |
|-------|-------------|---------------|
| `decimal_separator` | Decimal point character | `.` |
| `group_separator` | Thousands separator | `,` |
| `group_size` | Digits per group | `3` |
| `percent_symbol` | Percent sign | `%` |

### Date fields

Dates in Botswana follow the **dd/MM/yyyy** format in everyday usage. The `months_long` and `days_long` arrays need native speaker verification — if you can confirm or correct Setswana month and day names, that is one of the highest-value contributions you can make to this file.

---

## How to Contribute

1. Fork and create a branch: `data/locale-<what-you-are-fixing>`
2. Edit `data/locale/tn-BW.json`
3. Where data is uncertain or placeholder, the current file marks fields with a `"TODO"` string or a note in `metadata.notes`
4. **Cite your source** for any change — especially month names, day names, and number format conventions. Government publications, school textbooks, and official Botswana documents are the preferred sources.
5. Open a PR with title: `data(locale): <description of change>`

### Most needed right now

- [ ] Setswana names for all 12 months (confirmed, with source)
- [ ] Setswana names for all 7 days of the week (confirmed, with source)
- [ ] Verification of date format conventions against official Botswana documents
- [ ] Collation order (sort order for Setswana characters)

---

## Contributing Upstream to CLDR

Once our `tn-BW.json` data is verified by native speakers and has source citations, it can be submitted to CLDR via the [CLDR Survey Tool](https://st.unicode.org/cldr-apps/). CLDR requires:
- A CLDR account (free registration)
- Data submitted through the Survey Tool interface
- Community votes from multiple vetters for data to be accepted

This project aims to prepare verified, cited data so that CLDR submission is a straightforward step. Coordination for upstream submission will be tracked in GitHub Issues tagged `cldr-upstream`.

---

## Key References

- [CLDR Project](https://cldr.unicode.org/) — authoritative locale data standard
- [CLDR `tn` data](https://github.com/unicode-org/cldr/tree/main/common/main) — current Setswana (South Africa) data in CLDR
- [ICU User Guide](https://unicode-org.github.io/icu/userguide/) — how locale data is used in software
- Botswana Government publications for official date/currency conventions
