# Corpus

Open-license Setswana text corpus for NLP research and model training.

**Current status: Empty — Phase 3 goal.**

## What Goes Here

Naturally occurring Setswana text from open-license sources. Each contribution is two files:

- `<source>_<year>.txt` — UTF-8 plain text, one sentence per line
- `<source>_<year>.meta.json` — provenance metadata

## Metadata Schema

```json
{
  "filename": "source_year.txt",
  "source": "Name of source publication or dataset",
  "author": "Author or institution",
  "year": 2024,
  "license": "CC BY 4.0",
  "license_url": "https://...",
  "domain": "government | news | literature | education | proverbs | community | religious | other",
  "contributor": "GitHub username",
  "notes": "Optional notes about the text selection"
}
```

## License Requirement

**Only open-license text.** Acceptable licenses: CC0, CC BY, CC BY-SA, or verified public domain.
CC BY-NC, All Rights Reserved, and unknown-license text are **not** acceptable.

When in doubt, open an issue before including any text.

## How to Contribute

See [docs/contributing/corpus-guide.md](../../docs/contributing/corpus-guide.md) for the full guide, including license verification process, source categories, and format requirements.

## License

Text contributed to this corpus is licensed under **CC BY 4.0** (or the original open license, whichever is more permissive), as documented in each `.meta.json` file.
