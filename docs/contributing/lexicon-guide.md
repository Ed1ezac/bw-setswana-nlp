# Lexicon Contribution Guide

The lexicon is the most fundamental dataset in this project — the structured dictionary that downstream tools (morphological analyzer, POS tagger, spellchecker) will depend on. Getting entries right matters more than adding entries fast.

---

## What the Lexicon Is

The lexicon lives in `data/lexicon/lexicon.json`. Its structure is defined by `data/lexicon/schema.json` (a JSON Schema document you can read directly).

The outer wrapper:
```json
{
  "metadata": { "version": "...", "count": N, "license": "CC BY 4.0" },
  "lexicon": [ ...entries... ]
}
```

Each entry is an object. Required fields: `word`, `pos`, `definition_en`.

---

## Field Reference

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `word` | Yes | string | Setswana word, standard tn-BW orthography, NFC normalized |
| `pos` | Yes | string | Part of speech (see table below) |
| `definition_en` | Yes | string | Definition in English |
| `noun_class` | Nouns only | integer (1–18) | Bantu noun class number |
| `definition_tn` | Encouraged | string | Definition in Setswana |
| `example_sentence` | Encouraged | string | Example sentence in Setswana |
| `example_sentence_en` | If above given | string | English translation of example |
| `synonyms` | Optional | array of strings | Setswana synonyms |
| `source` | Encouraged | string | Source citation |
| `tags` | Optional | array of strings | Labels: `formal`, `colloquial`, `archaic`, `loanword`, `proverb` |

---

## Part-of-Speech Tags

Use exactly these values (lowercase):

| POS tag | Setswana example | Gloss |
|---------|-----------------|-------|
| `noun` | motho | person |
| `verb` | bua | speak/say |
| `adjective` | golo | big/great |
| `adverb` | gape | again/also |
| `pronoun` | ene | he/she/it (class 1) |
| `conjunction` | le | and |
| `interjection` | ee | yes |
| `preposition` | go | to/at (also infinitive marker — context dependent) |
| `particle` | a | subject concord marker (class 1 present) |

When the POS of a word is genuinely ambiguous, prefer the most common usage and add a note in `definition_en`.

---

## Noun Class Annotation

Setswana nouns belong to noun classes (Bantu class system). Include `noun_class` for every noun entry. The class number determines the noun's agreement patterns throughout the grammar.

See [docs/noun-classes.md](../noun-classes.md) for the full class table. Quick reference for the most common classes:

| Class | Singular prefix | Plural class | Example |
|-------|----------------|--------------|---------|
| 1 | mo- | 2 (ba-) | motho (person) |
| 3 | mo- | 4 (me-) | molomo (mouth) |
| 5 | le- | 6 (ma-) | leina (name) |
| 7 | se- | 8 (di-) | selo (thing) |
| 9 | (n-) | 10 (din-) | naga (land/country) |
| 14 | bo- | — | bosula (evil/badness) |

If you are not sure of the noun class, leave `noun_class` out and add `"tags": ["needs-class-annotation"]`.

---

## How to Add Entries

### Path A — Direct JSON edit (for developers)

1. Fork the repository and create a branch: `feat/lexicon-<description>`
2. Open `data/lexicon/lexicon.json`
3. Add your entries to the `"lexicon"` array following the schema
4. Update `"count"` in `"metadata"` to reflect the new total
5. Run a quick validity check:
   ```bash
   python -c "import json; data=json.load(open('data/lexicon/lexicon.json')); print(f'{data[\"metadata\"][\"count\"]} entries, JSON valid')"
   ```
6. Open a PR with the title: `feat(lexicon): add <N> <description> entries`

### Path B — GitHub Issue template (recommended for non-developers)

If you are a native speaker without a development setup, open a GitHub Issue using the **Lexicon Entry Submission** template. Provide:
- The Setswana word
- Its part of speech
- A definition in English (and Setswana if possible)
- An example sentence
- Your source (which dictionary, personal knowledge, etc.)

A project maintainer will format and add the entry.

---

## Quality Checklist

Before submitting a PR, verify each entry:

- [ ] `word` is spelled correctly per [docs/orthography.md](../orthography.md)
- [ ] `pos` uses an exact value from the allowed enum
- [ ] `definition_en` is clear and accurate
- [ ] Nouns have `noun_class` set (or tagged `needs-class-annotation`)
- [ ] `source` field is filled in
- [ ] At least one `example_sentence` is included for new entries

---

## What NOT to Include

- **Disputed spellings** — if the standard spelling is uncertain, open an issue for discussion before adding
- **Copyrighted definitions** — do not copy verbatim from proprietary dictionaries; paraphrase with a source citation
- **Loanwords without adaptation** — loanwords that have not been phonologically adapted to Setswana should be tagged `loanword` and discussed in an issue first
- **Proper nouns** (people's names, place names) — these belong in a separate gazetteer dataset, not the core lexicon
