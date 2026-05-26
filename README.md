# bw-setswana-nlp

> A developer-facing NLP toolkit and language resource for **Setswana as spoken in Botswana** — building the digital foundation for a language that belongs online.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-early%20development-orange.svg)
![Language](https://img.shields.io/badge/language-Setswana%20(tn--BW)-green.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

---

## Why This Exists

Setswana is spoken by millions of people in Botswana as a first language and serves as the national language of the country. Yet in digital spaces — operating systems, translation engines, NLP pipelines, keyboards, and developer tooling — it remains largely invisible.

This project exists to change that.

`bw-setswana-nlp` is an open-source effort to build the foundational language resources that allow Setswana to exist as a first-class language in software: locale support, dictionary datasets, morphological tooling, corpora, and eventually NLP/AI-ready resources — all rooted in **Setswana as natively spoken in Botswana** (`tn-BW`).

This is not a translation app. It is the **infrastructure layer** that makes Setswana viable for developers building apps, researchers training models, and platform teams adding locale support.

---

## Project Scope

This repository targets **Setswana as spoken in Botswana** (`tn-BW` locale). While Setswana/Tswana is also spoken in South Africa and Zimbabwe, this project's primary reference is the Botswana standard. Contributions that introduce dialect conflicts will be discussed in issues before merging.

---

## Roadmap

Development is phased to build a solid foundation before higher-level tooling.

### Phase 1 — Foundation *(current focus)*
- [ ] Structured lexicon / dictionary dataset (words, definitions, POS tags)
- [ ] ISO locale data (`tn-BW`) — date formats, number formats, currency (BWP)
- [ ] Basic tokenizer (whitespace + punctuation aware)
- [ ] Character and diacritic reference for Setswana orthography

### Phase 2 — Morphology & Grammar
- [ ] Noun class system documentation and data structures
- [ ] Verb conjugation tables
- [ ] Agglutination rules and morphological analyzer
- [ ] Part-of-speech tagger

### Phase 3 — Corpus & Translation
- [ ] Setswana text corpus (open license only)
- [ ] Setswana ↔ English translation pairs dataset
- [ ] Sentence boundary detection

### Phase 4 — NLP/AI Ready
- [ ] Pre-trained embeddings or fine-tuning datasets
- [ ] Language model integration guides
- [ ] Speech data collection guidelines (TTS/STT groundwork)

> Phases are not strictly sequential — parallel contributions across phases are welcome.

---

## Repository Structure

```
bw-setswana-nlp/
├── data/
│   ├── lexicon/          # Dictionary and word list datasets
│   ├── corpus/           # Text corpus files
│   ├── locale/           # tn-BW locale data files
│   └── translations/     # Parallel translation datasets
├── src/
│   ├── tokenizer/        # Tokenization logic
│   ├── morphology/       # Morphological analysis tools
│   └── utils/            # Shared utilities
├── docs/
│   ├── orthography.md    # Setswana writing system reference
│   ├── noun-classes.md   # Noun class system
│   └── contributing/     # Extended contribution guides
├── tests/
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## Contributing

All contributions are welcome — from native speakers helping with linguistic accuracy, to developers building tooling, to researchers contributing datasets.

### Getting Started

1. **Fork** the repository
2. **Browse open issues** — issues tagged `good first issue` are a great entry point
3. **Read the relevant doc** in `/docs` before contributing to a linguistic area
4. **Open an issue first** for anything non-trivial before submitting a PR — alignment matters especially for language data

### What We Need Most Right Now

| Need | Skills Required |
|---|---|
| Lexicon entries (words + definitions + POS) | Native Setswana speaker |
| Orthography documentation | Linguistics knowledge |
| Locale data (`tn-BW`) | Developer familiar with CLDR/ICU formats |
| Tokenizer implementation | Developer (any language) |
| Corpus text collection | Native speaker + copyright diligence |
| Test cases | Developer |

### Contribution Guidelines

- **Linguistic accuracy over speed.** If unsure about a word, translation, or rule — open a discussion rather than guessing.
- **Cite your sources** for linguistic data where possible (dictionaries, academic papers, official publications).
- **No copyrighted text** in the corpus without explicit open license confirmation.
- **One concern per PR.** Keep pull requests focused and reviewable.
- **Write in English** for code, comments, and documentation. Setswana is used for language data only.
- All data files should be in open formats (JSON, CSV, or plain text).

### Commit Message Convention

```
type(scope): short description

Examples:
feat(lexicon): add 200 common verb entries
fix(tokenizer): handle apostrophe in contractions
docs(orthography): document tonal marking rules
data(corpus): add public domain Setswana proverbs
```

---

## Community

This project is in its earliest stage. The goal is to build a small, focused core team of:
- Native Setswana speakers (Botswana-based preferred)
- African language NLP researchers
- Developers interested in underrepresented language tooling

**To join or get involved:**
- Open an issue introducing yourself and your area of interest
- Reach out via GitHub Discussions (will be enabled shortly)

We are also monitoring related efforts like [Masakhane](https://www.masakhane.io/) and aim to align with and contribute back to the broader African NLP ecosystem.

---

## Related Projects & Resources

- [Masakhane](https://www.masakhane.io/) — African NLP research community
- [NLLB (Meta)](https://ai.meta.com/research/no-language-left-behind/) — includes some Setswana data
- [CLDR Project](https://cldr.unicode.org/) — Unicode locale data standard (target for `tn-BW` contributions)
- [SIL International](https://www.sil.org/) — language documentation resources

---

## License

MIT License — see [LICENSE](./LICENSE) for details.

Language data (lexicon, corpus, translations) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless otherwise noted.

---

*Ke ya rona rotlhe.* — It is for all of us.
