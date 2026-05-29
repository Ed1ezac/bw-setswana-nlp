# Setswana Orthography Reference

> This document is the canonical writing-system reference for the `bw-setswana-nlp` project.
> All lexicon entries, corpus text, and code must follow the conventions described here.
> If you find an error or omission, please open an issue before submitting a correction.

---

## Overview

Setswana (`tn-BW`) uses the Latin alphabet. The orthography is largely phonemic — one symbol per sound — but it encodes several phonemes using **digraphs** (two letters) and one **trigraph** (three letters). These multi-character sequences represent single sounds and must never be split during tokenization or character-level processing.

The standard reference orthography for this project is the Botswana standard, as reflected in official government publications and the South African school orthography where they agree.

---

## Alphabet

Setswana uses all 26 letters of the Latin alphabet. Letters **c**, **q**, **v**, and **x** appear only in loanwords or proper names.

| Letter | Example word | Gloss | Pronunciation note |
|--------|-------------|-------|--------------------|
| a | **a**tla | hand | open central vowel, like "a" in "father" |
| b | **b**oya | hair/fur | voiced bilabial stop |
| c | — | — | rare; only in loanwords |
| d | **d**ilo | things | voiced alveolar stop |
| e | **e**lo | tongue | mid front vowel |
| f | **f**elo | place | voiceless labiodental fricative |
| g | **g**ape | again/also | voiced velar stop |
| h | **h**ua | speak (variant) | voiceless glottal fricative |
| i | **i**na | name | high front vowel |
| j | **j**a | eat | palatal approximant (like English "y") |
| k | **k**a | by/with | voiceless velar stop |
| l | **l**efatshe | country/earth | lateral approximant |
| m | **m**otho | person | bilabial nasal |
| n | **n**tlo | house | alveolar nasal |
| o | **o**se | do not | mid back vowel |
| p | **p**ele | before/front | voiceless bilabial stop |
| q | — | — | rare; only in loanwords |
| r | **r**e | we/say | alveolar trill or tap |
| s | **s**ala | stay | voiceless alveolar fricative |
| t | **t**samaya | walk/go | voiceless alveolar stop |
| u | **u**la | threaten | high back vowel |
| v | — | — | rare; only in loanwords |
| w | **w**a | fall | labio-velar approximant |
| x | — | — | rare; only in loanwords |
| y | **y**a | go (imperative) | palatal approximant |
| z | **z**ola | be quiet | voiced alveolar fricative |

---

## Digraphs and Trigraphs

These sequences represent **single phonemes**. They are critical for the tokenizer — a tokenizer that splits `tlh` into `t` + `l` + `h` produces linguistically invalid output.

| Sequence | Type | Example word | Gloss | Phonetic description |
|----------|------|-------------|-------|---------------------|
| **kg** | digraph | **kg**osi | chief/king | voiceless velar fricative (IPA: /x/) |
| **ng** | digraph | **ng**wana | child | velar nasal (IPA: /ŋ/) — also word-medial/final |
| **ph** | digraph | **ph**arologano | difference | aspirated bilabial stop (IPA: /pʰ/) |
| **sh** | digraph | **sh**aba | copper | voiceless postalveolar fricative (IPA: /ʃ/) |
| **tl** | digraph | **tl**hogo | head | voiceless lateral affricate (IPA: /tɬ/) |
| **ts** | digraph | **ts**a | of/belonging to | voiceless alveolar affricate (IPA: /ts/) |
| **tlh** | trigraph | **tlh**ogo | head | aspirated lateral affricate (IPA: /tɬʰ/) |
| **tsh** | digraph | **tsh**wara | hold/catch | aspirated affricate (IPA: /tsʰ/) |

> **Note on `tl` vs `tlh`:** Both are valid digraph/trigraph combinations. `tlh` must be matched before `tl` in any left-to-right scan to avoid misidentifying the trigraph. The tokenizer must handle this ordering.

> **Note on `ng`:** This digraph represents a single velar nasal sound, but it is not always a digraph — for example in `n-go` (not standard, shown for illustration). Context matters; word-level tokenization treats word boundaries, not sub-word grapheme sequences.

---

## Vowels

Setswana has **five vowel phonemes**: a, e, i, o, u. Vowels are generally short and pure (no diphthongs in core vocabulary). Vowel length variation exists phonetically but is not consistently marked in standard orthography.

| Vowel | IPA | Example | Gloss |
|-------|-----|---------|-------|
| a | /a/ | naga | country/wilderness |
| e | /ɛ/ or /e/ | re | we; say |
| i | /i/ | bina | dance |
| o | /ɔ/ or /o/ | go | to (infinitive marker) |
| u | /u/ | pula | rain; Botswana Pula (currency) |

---

## Apostrophe Usage

The apostrophe (`'`) appears in Setswana text in specific grammatical contexts. It is **not** a punctuation mark separating sentences — it marks morpheme boundaries or elision within a word or phrase.

Common contexts:

- **Elision of vowels** at morpheme boundaries: `o a` → `o'a` (he/she is + verb stem initial vowel elided in fast speech — representation varies)
- **Subject concord contractions**: some concord forms contract before vowel-initial stems

**Tokenizer implication:** The apostrophe must not trigger word splitting as if it were punctuation. Words containing an apostrophe are single tokens. See [docs/contributing/tokenizer-guide.md](contributing/tokenizer-guide.md) for implementation details.

---

## Capitalization

- **Sentence-initial** words are capitalized (standard).
- **Proper nouns** are capitalized: `Botswana`, `Gaborone`, `Setswana`.
- The language name `Setswana` is always capitalized.
- **Common nouns** are lowercase: `motho` (person), `ntlo` (house).
- Do **not** capitalize common nouns mid-sentence unless they are proper names.

---

## Tonal Marking

Setswana is a **tonal language** (high and low tones are phonemically distinctive), but tones are **not marked** in the standard written orthography. Most published Setswana text — dictionaries, newspapers, government documents, school textbooks — is written without tone marks.

**Implication for this project:**
- The lexicon does not include tone marks unless a contributor explicitly provides them with linguistic justification and source.
- The tokenizer and morphological tools do not assume tonal diacritics in input.
- If/when tonal annotation is added in a future phase, it will be stored as a separate optional field (`tone_pattern`) in the lexicon schema, not embedded in the `word` field.

This gap (unwritten tones) is a known limitation of standard Setswana orthography, documented here honestly.

---

## Diacritics

Standard Setswana orthography uses **no diacritics** on native words. Diacritics may appear in:
- Academic/linguistic transcriptions (IPA notation in sources like SIL)
- Older orthographic traditions (circumflex in some mid-20th century publications)
- Loanword adaptations from languages that use diacritics

All text in this project's datasets is stored in **NFC-normalized Unicode**. Diacritics encountered in source materials are either preserved as-is with a note, or stripped using `utils.text.remove_diacritics()` for search/matching purposes only.

---

## Reference Sources

1. **Setswana Dictionary** — R. S. Setiloane, Longman Botswana (for lexical reference)
2. **Mafeking Setswana** — Sol Plaatje (historical/literary reference)
3. **CLDR Setswana data** (`tn` locale) — Unicode Common Locale Data Repository
4. **SIL International** — Setswana language documentation (https://www.sil.org/)
5. **Botswana Examinations Council** — official orthography as used in school curriculum
6. **Masakhane** community references — https://www.masakhane.io/

---

*Last updated: 2024. Open an issue to propose corrections or additions.*
