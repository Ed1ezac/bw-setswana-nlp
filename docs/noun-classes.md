# Setswana Noun Class System

> **Status: Phase 2 — skeleton document.** Section headers and introductions are in place.
> Tables are partially filled and marked where native speaker verification or additional data is needed.
> Open an issue tagged `Phase-2` and `needs-native-speaker` to contribute to this document.

---

## Introduction

Setswana, like all Bantu languages, organizes nouns into **noun classes** — a grammatical category system in which every noun belongs to a class, and that class controls agreement patterns throughout the sentence. Understanding the noun class system is essential for:

- The morphological analyzer (Phase 2) — prefixes identify class membership
- The POS tagger — noun class determines concord forms on verbs and adjectives
- The lexicon — every noun entry should carry its class number

Setswana has approximately **15 noun classes**, organized in singular/plural pairs. Classes are numbered using the standard Bantu numbering convention.

---

## Class Table

<!-- TODO: Verify all entries with a native Setswana speaker or authoritative linguistic source.
     Cite: specific dictionary or grammar reference for each row. -->

| Class | Role | Prefix | Example noun | Gloss |
|-------|------|--------|--------------|-------|
| 1 | Singular (animate) | mo- / m- | motho | person |
| 2 | Plural of Class 1 | ba- / b- | batho | people |
| 3 | Singular (inanimate) | mo- / m- | molomo | mouth |
| 4 | Plural of Class 3 | me- | melomo | mouths |
| 5 | Singular | le- / l- | leina | name |
| 6 | Plural of Class 5 | ma- | maina | names |
| 7 | Singular | se- | selo | thing |
| 8 | Plural of Class 7 | di- | dilo | things |
| 9 | Singular (often animals, loanwords) | (n-) / — | naga | land/country |
| 10 | Plural of Class 9 | din- / (n-) | dinaga | lands/countries |
| 11 | Singular (long/thin objects) | lo- | lonao | foot/leg |
| 12 | Diminutive singular | go- | <!-- TODO --> | — |
| 14 | Abstract nouns (uncountable) | bo- | bosula | evil/badness |
| 15 | Infinitive / verbal noun | go- | go bua | to speak |
| 16/17/18 | Locative | fa- / go- / mo- | fatshe | on the ground |

> Class 12 and locative classes (16/17/18) need additional verification and examples.

---

## Concord Paradigms

Each noun class controls agreement on:
- **Subject verb prefix** — the morpheme on the verb that agrees with the subject
- **Object prefix** — on the verb, agreeing with the object
- **Adjective/demonstrative prefix** — on modifiers

<!-- TODO: Fill this table with the full concord paradigm for each class.
     Source to use: Standard Setswana grammar reference. -->

| Class | Subject concord | Object concord | Demonstrative (proximal) |
|-------|----------------|----------------|--------------------------|
| 1 | o | mo | yo |
| 2 | ba | ba | bao |
| 3 | o | o | wo |
| 4 | e | e | eo |
| 5 | le | le | leo |
| 6 | a | a | ao |
| 7 | se | se | seo |
| 8 | di | di | dio |
| 9 | e | e | eo |
| 10 | di | di | dio |
| 14 | bo | bo | boo |
| 15 | go | go | — |

---

## Locative Classes

Classes 16, 17, and 18 encode **location** rather than object categories. They are formed by adding locative prefixes to nouns:

| Class | Prefix | Meaning | Example |
|-------|--------|---------|---------|
| 16 | fa- | at/on a surface | fatshe (on the ground/earth) |
| 17 | go- | at/near (general) | — |
| 18 | mo- | inside/within | — |

<!-- TODO: Add full example set for locative classes with example sentences. -->

---

## Data Structure for Noun Classes

The lexicon schema stores `noun_class` as an integer field on noun entries. The full class data (prefix patterns, concord forms) will be stored as a structured reference file once this document is verified.

Planned data file: `data/lexicon/noun-classes.json`

Proposed structure:
```json
{
  "classes": [
    {
      "class_number": 1,
      "role": "singular_animate",
      "prefix_singular": "mo",
      "plural_class": 2,
      "subject_concord": "o",
      "object_concord": "mo",
      "examples": [
        { "word": "motho", "gloss": "person" }
      ]
    }
  ]
}
```

<!-- TODO: Finalize the data structure in an issue before implementing. -->

---

## Relationship to the Tokenizer

Noun class prefixes (`mo-`, `ba-`, `se-`, `di-`, `bo-`, `le-`, `ma-`) are detachable morphemes. In Phase 2, the morphological analyzer will use these prefixes to:
1. Identify a noun's class from its surface form
2. Strip the prefix to find the stem
3. Look up the stem in the lexicon

Phase 1 tokenization does **not** split at morpheme boundaries — `motho` is one token, not `mo` + `tho`. This is a deliberate Phase 1 scope decision.

---

## References

<!-- TODO: Add specific grammar references used to compile this table. -->
- Standard Setswana grammar (source to be cited)
- Bantu noun class numbering: Guthrie classification system
- [docs/orthography.md](orthography.md) — for prefix spelling conventions
