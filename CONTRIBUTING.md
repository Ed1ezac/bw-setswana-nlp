# Contributing to bw-setswana-nlp

Thank you for your interest in contributing to this project. `bw-setswana-nlp` is building foundational language infrastructure for Setswana (`tn-BW`) — work that requires both linguistic expertise and technical skills. Contributions from native speakers, linguists, and developers are all essential.

---

## Core Principle

**Linguistic accuracy over speed.** If you are unsure about a word, translation, spelling, or grammatical rule — open a discussion rather than guessing. Incorrect linguistic data is harder to fix than slow progress.

---

## Two-License Model

This project uses a dual-license structure:

| Component | License |
|-----------|---------|
| Source code (`src/`, `tests/`) | MIT License |
| Language data (`data/lexicon/`, `data/corpus/`, `data/locale/`, `data/translations/`) | CC BY 4.0 |
| Documentation (`docs/`, `*.md`) | MIT License |

When contributing language data, you agree that your contribution is licensed under CC BY 4.0. Attribution format: `bw-setswana-nlp contributors, ed1ezac/bw-setswana-nlp`.

---

## Development Setup

Requirements: Python 3.9+, git.

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone https://github.com/<your-username>/bw-setswana-nlp.git
cd bw-setswana-nlp

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install in editable mode with dev dependencies
pip install -e ".[dev]"

# 4. Verify everything works
pytest -v
```

---

## Contribution Types

| What you want to contribute | Start here |
|-----------------------------|------------|
| Lexicon entries (words + definitions + POS) | [docs/contributing/lexicon-guide.md](docs/contributing/lexicon-guide.md) |
| Orthography or linguistic documentation | [docs/orthography.md](docs/orthography.md), open an issue first |
| Locale data (`tn-BW` formats) | [docs/contributing/locale-guide.md](docs/contributing/locale-guide.md) |
| Tokenizer implementation | [docs/contributing/tokenizer-guide.md](docs/contributing/tokenizer-guide.md) |
| Corpus text (open-license Setswana text) | [docs/contributing/corpus-guide.md](docs/contributing/corpus-guide.md) |
| Test cases | `tests/` directory — see existing test files for patterns |
| Bug reports | Open a GitHub issue with the `bug` label |

---

## Workflow

1. **Open an issue first** for anything non-trivial. Alignment on linguistic data especially matters before implementation begins.
2. **Fork** the repository and create a branch:
   ```
   feat/lexicon-common-verbs
   docs/orthography-digraphs
   fix/tokenizer-apostrophe
   data/corpus-public-domain-proverbs
   ```
3. **Make your changes.** Read the relevant guide in `docs/contributing/` before modifying a linguistic area.
4. **Run tests** before opening a PR: `pytest -v`
5. **Submit a pull request** with a clear title and description of what changed and why.
6. **Cite sources** for any linguistic data you add.

---

## Commit Message Convention

```
type(scope): short description

Types:   feat | fix | docs | data | test | chore | refactor
Scopes:  lexicon | tokenizer | orthography | corpus | locale | morphology | utils | tests

Examples:
feat(lexicon): add 50 common noun entries with noun class annotations
fix(tokenizer): handle apostrophe as morpheme boundary marker
docs(orthography): document digraph tokenization rules
data(corpus): add public domain Setswana proverbs (CC0)
test(tokenizer): add edge cases for tlh/tl/ts digraphs
```

---

## Code Standards

- **Language:** Python 3.9+
- **Linting:** `ruff check src/ tests/` must pass with zero errors
- **Type hints:** Required for all public function signatures
- **Docstrings:** Required for all public classes and methods; include a Setswana example where relevant
- **No runtime dependencies** in Phase 1 — use Python stdlib only (`re`, `unicodedata`, `json`)

---

## Data Standards

- **Encoding:** UTF-8, NFC normalized
- **Formats:** JSON or plain text (UTF-8). No binary formats.
- **No copyrighted text** in corpus or translations without explicit open-license confirmation. When in doubt, do not include it — open an issue instead.
- **Cite your sources.** For lexicon entries, note the source dictionary or reference. For corpus text, provide full provenance in the metadata sidecar file.
- **One concern per PR.** Keep pull requests focused and reviewable.

---

## Review Process

- **Linguistic PRs** (lexicon entries, orthography changes, noun class data): require review from at least one person with native Setswana speaker competence before merge.
- **Code PRs** (tokenizer, utils, morphology): require review from at least one project maintainer.
- **Documentation PRs**: lighter review, but still checked for accuracy against existing linguistic references.

---

## Getting Help

- **GitHub Issues:** For bugs, questions, or proposing contributions
- **GitHub Discussions:** For open-ended questions, introductions, and research discussion (will be enabled shortly)
- **Issue labels:** `good first issue` for beginner-friendly tasks, `needs-native-speaker` for linguistic review, `Phase-1` / `Phase-2` etc. for roadmap alignment

---

*Ke ya rona rotlhe.* — It is for all of us.
