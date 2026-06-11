# Translation Pairs Dataset

Parallel Setswana ↔ English sentence pairs for machine translation research.

**Current status: Empty — Phase 3 goal.**

## Format

Each entry is a JSON Lines (`.jsonl`) file, one sentence pair per line:

```json
{"tn": "Ke a bua Setswana.", "en": "I speak Setswana.", "source": "...", "license": "CC BY 4.0"}
```

Accompanying each `.jsonl` file: a `.meta.json` sidecar with source, author, year, license, and domain.

## License Requirement

Same strict requirement as the corpus: only CC0, CC BY, CC BY-SA, or verified public domain text.

## Alignment with Masakhane

Translation pair format is designed to be compatible with [Masakhane](https://www.masakhane.io/) datasets to allow cross-project contributions.

## How to Contribute

See [docs/contributing/corpus-guide.md](../../docs/contributing/corpus-guide.md) — the same provenance and license verification requirements apply. Open an issue tagged `translations` before contributing a large dataset.

## License

Data contributed here is licensed under **CC BY 4.0** unless the source material carries a more permissive license, as documented per file.
