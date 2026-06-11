# Tokenizer Contribution Guide

The tokenizer is the first executable component of `bw-setswana-nlp`. It splits Setswana text into word tokens in a way that respects Setswana's orthographic conventions — conventions that generic tokenizers built for European languages will get wrong.

---

## Tokenization Goals

Phase 1 delivers a **word-level tokenizer** only. It must:

1. Split text on whitespace and punctuation boundaries
2. **Not split digraphs and trigraphs** — `tlh`, `tsh`, `tl`, `ts`, `kg`, `ph`, `sh`, `ng` are single phonemes written as multi-character sequences. Splitting them produces linguistically invalid output.
3. Return punctuation as separate tokens (configurable)
4. Handle the apostrophe correctly — in Setswana, `'` appears inside words as a morpheme boundary marker, not as sentence-level punctuation
5. Handle empty input and whitespace-only input gracefully

Phase 2 will add morpheme-boundary tokenization (splitting `motho` into `mo-` + `tho`). Phase 1 does not attempt sub-word segmentation.

---

## Architecture

The tokenizer is a single pure-Python class in `src/bw_setswana_nlp/tokenizer/tokenizer.py`.

- **Zero runtime dependencies** — uses only `re` and `typing` from the Python standard library
- **No machine learning** — rule-based, fully deterministic, reproducible
- Importable as: `from bw_setswana_nlp.tokenizer import Tokenizer`

---

## The `Tokenizer` Class Interface

```python
class Tokenizer:
    DIGRAPHS: tuple[str, ...]  # ("tlh", "tsh", "tl", "ts", "kg", "ph", "sh", "ng")

    def __init__(self, keep_punctuation: bool = True) -> None: ...

    def tokenize(self, text: str) -> list[str]:
        """Split text into word tokens. Returns [] for empty/whitespace input."""

    def tokenize_sentences(self, text: str) -> list[list[str]]:
        """Split text into sentences, return list of token lists."""

    def detokenize(self, tokens: list[str]) -> str:
        """Reconstruct a string from tokens (best-effort, lossy)."""
```

### Expected behavior examples

```python
t = Tokenizer()

t.tokenize("Ke a bua Setswana.")
# → ['Ke', 'a', 'bua', 'Setswana', '.']

t.tokenize("O tlhoga jang?")
# → ['O', 'tlhoga', 'jang', '?']     ← 'tlh' stays together

t.tokenize("Lefatshe la Botswana le a galalela.")
# → ['Lefatshe', 'la', 'Botswana', 'le', 'a', 'galalela', '.']

t.tokenize("")
# → []

Tokenizer(keep_punctuation=False).tokenize("Ke a bua.")
# → ['Ke', 'a', 'bua']               ← period discarded
```

---

## Edge Cases (Exhaustive List)

Every item in this list needs a corresponding test in `tests/test_tokenizer.py`:

| Case | Expected behavior |
|------|-------------------|
| Empty string `""` | `[]` |
| Whitespace only `"   "` | `[]` |
| Single word | `["word"]` |
| Period at end of sentence | Period as separate token: `[..., '.']` |
| Question mark | `[..., '?']` |
| Comma mid-sentence | `[..., ',', ...]` |
| Digraph `tlh` — word-initial | Not split: `"tlhogo"` → `["tlhogo"]` |
| Digraph `tlh` — word-medial | Not split: word containing `tlh` is one token |
| Digraph `tl` (vs trigraph `tlh`) | `tl` in `"tlhogo"` is part of `tlh`, not `tl` + `h` |
| Digraph `ts` | Not split: `"tsala"` (friend) → `["tsala"]` |
| Digraph `kg` | `"kgosi"` → `["kgosi"]` |
| Digraph `ng` word-initial | `"ngwana"` → `["ngwana"]` |
| Digraph `ph` | `"phiri"` (hyena) → `["phiri"]` |
| Apostrophe within a word | Preserve as single token, do not split at `'` |
| Mixed Setswana + English text | Tokenize by whitespace/punctuation; no language detection needed |
| Multiple spaces | Treated as one delimiter |
| Newlines | Treated as whitespace |
| Numbers in text | Numerals returned as tokens |
| All-caps word | Returned as-is (case is meaningful) |

---

## Digraph Ordering Note

The trigraph `tlh` must be matched **before** the digraph `tl` in any left-to-right scan. Similarly `tsh` before `ts`. Failure to do this will cause `tlh` to be misread as `tl` + `h`.

The `DIGRAPHS` tuple is ordered longest-first to enforce this:
```python
DIGRAPHS = ("tlh", "tsh", "tl", "ts", "kg", "ph", "sh", "ng")
```

Any regex or scanning loop over digraphs must process them in this order.

---

## Implementing `_build_pattern()`

The internal `_build_pattern()` method should compile a `re.Pattern` that:
1. Matches Setswana word characters — letters plus `'` (apostrophe)
2. Treats digraphs/trigraphs as atomic units within words
3. Captures punctuation as separate tokens when `keep_punctuation=True`

A starting approach is to match word tokens (letter sequences including apostrophe) and punctuation separately, then join them. The exact regex design is left to the implementer — open a discussion issue if you want to propose an approach before coding.

---

## Testing Requirements

Every edge case in the table above needs a test. See `tests/test_tokenizer.py` for the structure. Tests that have real Setswana examples:
- Use actual Setswana words (not placeholder "word1", "word2")
- Document the linguistic justification as a docstring

To run tests:
```bash
pip install -e ".[dev]"
pytest tests/test_tokenizer.py -v
```

All tests must pass before a tokenizer PR will be merged.

---

## Future Scope (Not Phase 1)

- **Phase 2:** Morpheme-boundary tokenization — split `motho` → `['mo', 'tho']` using noun class prefix rules from `docs/noun-classes.md`
- **Phase 3:** Sentence boundary detection as a standalone component
- **Phase 4:** Integration with language model tokenizers (SentencePiece, BPE)
