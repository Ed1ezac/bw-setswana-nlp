# Lexicon Contributor Guide

This guide explains how to add and edit entries in the `bw-setswana-nlp` lexicon.
The lexicon is the reference standard for the project — accuracy matters more than
volume. **If you are not sure about a word, do not guess.** Flag it (see
[The `flag` field](#the-flag-field)) or open an issue instead.

All lexicon data targets **Setswana as spoken in Botswana** (`tn-BW`). Where dialects
diverge, the Botswana standard is authoritative.

## Files

| File | Purpose |
|---|---|
| `data/lexicon/core.json` | The seed dictionary — a JSON array of entry objects. |
| `data/lexicon/schema.json` | The formal [JSON Schema](https://json-schema.org/) (draft-07) that every entry must validate against. |

Validate your changes before opening a PR:

```bash
pip install jsonschema
python -c "import json,jsonschema; jsonschema.Draft7Validator(json.load(open('data/lexicon/schema.json'))).validate(json.load(open('data/lexicon/core.json')))" && echo OK
```

## Entry format

Each entry is a JSON object. A complete noun entry looks like this:

```json
{
  "word": "motho",
  "pos": "noun",
  "noun_class": 1,
  "definition": "a person; human being",
  "plural": "batho",
  "example": "Motho yo o botlhokwa.",
  "example_translation": "This person is important.",
  "tags": ["common", "human"]
}
```

### Field reference

| Field | Required | Notes |
|---|---|---|
| `word` | always | The headword. See [Citation forms](#citation-forms). |
| `pos` | always | Part of speech. Must be one of the [POS tags](#part-of-speech-pos-tags). |
| `definition` | always | English definition. Separate multiple senses with a semicolon (`;`). |
| `example` | always | A short, natural Setswana sentence using the word. |
| `example_translation` | always | English translation of the example. |
| `tags` | always | Lowercase keyword array (`[a-z0-9-]`) for grouping/filtering. Use `"common"` for everyday vocabulary. |
| `noun_class` | nouns only | The noun class number. **Mandatory for nouns** (see below). |
| `plural` | nouns only | The plural form. **Mandatory for all nouns** (see below). |
| `flag` | optional | Review marker. Currently only `"needs-review"`. |

Definitions and translations are **always in English**. Setswana is only used in the
`word`, `plural`, and `example` fields.

### Citation forms

Setswana is agglutinative, so different parts of speech are cited differently:

- **Nouns, pronouns, numerals, greetings/interjections** — written in their normal
  surface form (`motho`, `wena`, `lesome`, `Dumela`).
- **Verbs** — cited by their **stem**, i.e. the form that follows the infinitive
  prefix *go* (`go bua` → `"bua"`). The example sentence shows it conjugated.
- **Adjectives** — true Setswana adjective stems are bound morphemes that never stand
  alone; they always take a class-agreement prefix. They are therefore cited with a
  **leading hyphen** (`-tona`, `-ntle`). The example shows the inflected form
  (`Ntlo e tona`, `Mosetsana yo montle`).

## Part-of-speech (POS) tags

The `pos` field is a closed vocabulary. This seed batch uses:

| `pos` | Description |
|---|---|
| `noun` | Naming word. Requires `noun_class` and `plural`. |
| `verb` | Action/state word, cited as a stem. |
| `pronoun` | Personal/absolute pronouns (`nna`, `wena`, …). |
| `numeral` | Cardinal numbers. Note that counting forms agree with noun class. |
| `adjective` | True adjective stems (hyphen-prefixed). |
| `interjection` | Greetings, farewells, and fixed expressions (`Dumela`, `Go siame`). |

Need a POS that isn't listed (e.g. `adverb`, `conjunction`, `ideophone`)? Open an issue
first so we extend the `enum` in `schema.json` deliberately and consistently.

## Noun class numbering

Setswana nouns belong to **noun classes** — grammatical genders that govern the noun's
prefix, its plural, and the agreement on verbs and adjectives. The `noun_class` field is
**non-optional for nouns** because almost every downstream tool (pluralization,
agreement, morphology) depends on it.

We use the standard Bantu/Setswana class numbering. Singular and plural sit in paired
classes:

| Class | Typical prefix | Example (sg.) | Plural class | Example (pl.) | Typical meaning |
|---|---|---|---|---|---|
| 1 | *mo-* | motho | 2 | batho | people |
| 1a | (none) | rre | 2a | borre | kinship / proper |
| 3 | *mo-* | molomo | 4 | melomo | body parts, plants, things |
| 5 | *le-* | leitlho | 6 | matlho | paired things, collectives |
| 7 | *se-* | seatla | 8 | diatla | things, instruments |
| 9 | *N-* | kgomo | 10 | dikgomo | animals, many loanwords |
| 11 | *lo-* | — | 10 | — | long/thin things |
| 14 | *bo-* | bogobe | 6 | — | abstracts, mass nouns |
| 15 | *go-* | go bua | — | — | infinitives |

Notes and conventions:

- Record the **singular's** class number in `noun_class`. The plural's class is implied
  by the pairing above and does not get its own field.
- **Class 1a/2a** (kinship terms and names that take no singular prefix and pluralise
  with *bo-*, e.g. `rre`/`borre`) are recorded as class **1** in this seed batch for
  simplicity. If you need the finer distinction, raise it in an issue.
- Some nouns have **irregular** singular/plural pairings (e.g. `ntlo` is class 9 but its
  plural `matlo` patterns with class 6). Record the singular class and give the actual
  plural form — that is exactly what `plural` is for.
- **Mass nouns** (e.g. water, some abstracts) have no countable plural. Repeat the same
  form in `plural` and add a `"mass-noun"` tag.

The class system is documented more fully in `docs/noun-classes.md` (Phase 2).

## Plurals

`plural` is **mandatory for every noun**. Do not infer it mechanically from the prefix —
irregular forms are common. If you genuinely don't know the plural, flag the entry rather
than inventing one.

## The `flag` field

Set `"flag": "needs-review"` on any entry whose spelling, noun class, plural, or meaning
you are not fully confident about. This is the project's explicit alternative to guessing.

A flagged **noun** is **exempt** from the mandatory `noun_class`/`plural` requirement —
omit the field(s) you are unsure of rather than filling them with a guess. In this seed
batch, the days of the week are flagged: their meanings are solid, but the noun-class and
plural assignments for fossilised day names need confirmation by a native speaker, so
those fields are left off pending review.

Reviewers should remove the flag (and complete any missing fields) only after a native
speaker or a citable source confirms the entry.

## No loanwords (this batch)

This seed batch is **root Setswana only** — no borrowings from English, Afrikaans, or
other languages (so no *buka*, *sekolo*, *beke*, *tafole*, etc.). Loanwords are a
legitimate part of the living language and will be added in a later, clearly-tagged batch.

## Word selection priority

When extending the lexicon, prioritise high-frequency, foundational vocabulary:
everyday nouns, common verbs, greetings, pronouns, numbers, days of the week, and basic
adjectives.

## Sources

Cite a dictionary, academic source, or note "native speaker" in your PR description for
linguistic data where possible. Linguistic accuracy over speed — when in doubt, open a
discussion.
