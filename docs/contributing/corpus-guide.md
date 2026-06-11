# Corpus Contribution Guide

The Setswana text corpus is a Phase 3 goal, but corpus-eligible material can be identified and documented now. This guide defines what counts as acceptable corpus text and how to contribute it.

**Current status:** `data/corpus/` is empty. Phase 3.

---

## What Counts as Corpus Text

The corpus is a collection of naturally occurring Setswana text that can be used for NLP training, evaluation, and research. To be included:

- **Naturally written Setswana** — written by native/fluent speakers in authentic contexts, not translated from English by machine
- **Open license** — must be legally usable for research and model training (see License Requirements below)
- **Minimum quality** — legible, reasonably grammatical, Botswana-standard Setswana preferred
- **Varied domains** — we want coverage across: news, literature, oral tradition, formal documents, educational text, proverbs

We explicitly do **not** want:
- Machine-translated text (it encodes English syntax in Setswana words)
- Social media text without contributor consent
- Text of unknown provenance

---

## License Requirements

This is the most critical constraint. Including copyrighted text can create serious legal problems for the project and its users.

Only include text that is:

| License type | Acceptable? | Notes |
|--------------|-------------|-------|
| Public domain (pre-1928 or explicitly released) | Yes | Document clearly |
| CC0 | Yes | No restrictions |
| CC BY | Yes | Attribution required |
| CC BY-SA | Yes | Share-alike; downstream must also use CC BY-SA |
| CC BY-NC | **No** | Non-commercial restriction disqualifies NLP research use |
| All Rights Reserved | **No** | Cannot include without explicit written permission |
| Unknown license | **No** | Assume copyright until proven otherwise |

**How to verify license:**
1. Check the source website/publication for explicit license information
2. For government publications: Botswana government works are often public domain — verify on a case-by-case basis
3. When in doubt, open a GitHub Issue and ask before including anything

---

## Acceptable Source Categories

1. **Pre-1928 Setswana publications** — Sol Plaatje's works, early missionary publications
2. **Government documents** (Botswana) — official reports, parliamentary records — verify license
3. **Open-license newspapers or media** — publications that explicitly release under CC licenses
4. **Academic publications** — where authors/institutions have granted CC license
5. **Community contributions** — text written specifically for this project by community members (CC BY 4.0 by default under the project's contribution agreement)
6. **Proverbs and oral tradition** — proverbs themselves are not copyrightable; however, specific written collections may be. Contribute proverbs as community knowledge, not copied from a copyrighted book.

---

## File Format

Each corpus contribution is two files:

**1. Text file** (`data/corpus/<source>_<year>.txt`):
- UTF-8 plain text
- One sentence per line (preferred) or paragraph-separated
- No HTML, no markdown, no annotations
- Filename example: `govt_annual_report_2019.txt`, `proverbs_community_2024.txt`

**2. Metadata sidecar** (`data/corpus/<source>_<year>.meta.json`):
```json
{
  "filename": "govt_annual_report_2019.txt",
  "source": "Botswana Government Annual Report 2019",
  "author": "Government of Botswana",
  "year": 2019,
  "license": "Public Domain",
  "license_url": "https://...",
  "domain": "government",
  "contributor": "GitHub username or name",
  "notes": "Pages 12-45, economic section only"
}
```

The `domain` field should be one of: `government`, `news`, `literature`, `education`, `proverbs`, `community`, `religious`, `other`.

---

## How to Contribute

1. Verify the text source and license (this is the hard part — do it carefully)
2. Fork and create a branch: `data/corpus-<source-description>`
3. Add your `.txt` and `.meta.json` files to `data/corpus/`
4. Open a PR with title: `data(corpus): add <description> (<license>)`
5. In the PR description, include a link to the original source and the license confirmation

For large contributions (>10,000 sentences), open an issue first to discuss format and structure before doing the work.

---

## Alignment with Masakhane

[Masakhane](https://www.masakhane.io/) is building African language datasets using participatory methods. Our corpus format aims to be compatible with Masakhane datasets so contributions can flow between projects. If you are contributing to both, coordinate via GitHub Issues.
