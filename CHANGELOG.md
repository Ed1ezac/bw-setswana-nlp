# Changelog

All notable changes to this project will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Repository scaffolding: complete project directory structure
- `pyproject.toml`: Python package definition with `src/` layout, zero runtime deps, dev extras (pytest, ruff)
- `LICENSE`: MIT for code, CC BY 4.0 notation for language data
- `CONTRIBUTING.md`: full contributor guide covering dev setup, workflow, commit convention, code and data standards
- `CODE_OF_CONDUCT.md`: Contributor Covenant 2.1 with project-specific preamble
- `data/lexicon/schema.json`: JSON Schema (draft-07) defining lexicon entry structure
- `data/lexicon/lexicon.json`: Seed entries establishing format baseline
- `data/locale/tn-BW.json`: Phase 1 locale data stub (date, number, currency for Botswana)
- `docs/orthography.md`: Setswana writing system reference with real linguistic content
- `docs/noun-classes.md`: Phase 2 skeleton for Setswana noun class system
- `docs/contributing/`: Per-area contribution guides (lexicon, corpus, locale, tokenizer)
- `src/bw_setswana_nlp/tokenizer/tokenizer.py`: `Tokenizer` class interface with Setswana-aware design
- `src/bw_setswana_nlp/utils/text.py`: Text normalization and character utilities (real implementations)
- `src/bw_setswana_nlp/morphology/analyzer.py`: Phase 2 interface stub
- `tests/`: Test suite covering utils (passing), tokenizer (contract), morphology (skipped/Phase 2)
