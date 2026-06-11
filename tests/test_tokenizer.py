"""Tests for bw_setswana_nlp.tokenizer.Tokenizer.

Tests define the tokenizer's contract. Digraph tests verify that
Setswana multi-character phoneme sequences (tlh, tl, ts, kg, etc.)
are never split across token boundaries.

See docs/orthography.md for the full digraph reference.
See docs/contributing/tokenizer-guide.md for edge case documentation.
"""

from bw_setswana_nlp.tokenizer import Tokenizer


class TestTokenizerBasic:
    def test_simple_sentence(self, tokenizer):
        assert tokenizer.tokenize("Ke a bua") == ["Ke", "a", "bua"]

    def test_empty_string_returns_empty_list(self, tokenizer):
        assert tokenizer.tokenize("") == []

    def test_whitespace_only_returns_empty_list(self, tokenizer):
        assert tokenizer.tokenize("   ") == []

    def test_single_word(self, tokenizer):
        assert tokenizer.tokenize("Setswana") == ["Setswana"]

    def test_multiple_spaces_treated_as_one_delimiter(self, tokenizer):
        result = tokenizer.tokenize("Ke  a   bua")
        assert result == ["Ke", "a", "bua"]

    def test_newline_treated_as_whitespace(self, tokenizer):
        result = tokenizer.tokenize("Ke a\nbua")
        assert result == ["Ke", "a", "bua"]

    def test_real_sentence(self, tokenizer):
        result = tokenizer.tokenize("Lefatshe la Botswana le a galalela.")
        assert result[0] == "Lefatshe"
        assert "Botswana" in result
        assert result[-1] == "."


class TestTokenizerPunctuation:
    def test_period_is_separate_token(self, tokenizer):
        tokens = tokenizer.tokenize("Ke a bua.")
        assert tokens[-1] == "."
        assert "bua." not in tokens

    def test_question_mark_is_separate_token(self, tokenizer):
        tokens = tokenizer.tokenize("O tlhoga jang?")
        assert "?" in tokens
        assert "jang?" not in tokens

    def test_keep_punctuation_false_discards_period(self, tokenizer_no_punct):
        tokens = tokenizer_no_punct.tokenize("Ke a bua.")
        assert "." not in tokens
        assert tokens == ["Ke", "a", "bua"]

    def test_keep_punctuation_false_discards_question_mark(self, tokenizer_no_punct):
        tokens = tokenizer_no_punct.tokenize("O tlhoga jang?")
        assert "?" not in tokens


class TestTokenizerDigraphs:
    """
    Setswana digraphs and trigraphs are single phonemes written as
    multi-character sequences. They must not be split within a word token.

    Full digraph list: tlh, tsh, tl, ts, kg, ph, sh, ng
    See docs/orthography.md — Digraphs and Trigraphs section.
    """

    def test_tlh_trigraph_not_split(self, tokenizer):
        # 'tlhoga' contains the trigraph 'tlh' — must remain as one token
        tokens = tokenizer.tokenize("O tlhoga jang")
        assert "tlhoga" in tokens
        assert "t" not in tokens
        assert "lh" not in tokens

    def test_tlh_word_initial_preserved(self, tokenizer):
        # 'tlhogo' = head; trigraph tlh at start of word
        tokens = tokenizer.tokenize("Tlhogo e e gobogile.")
        assert "Tlhogo" in tokens

    def test_tl_digraph_not_split(self, tokenizer):
        # 'tlala' = hunger; 'tl' digraph at word start
        tokens = tokenizer.tokenize("Tlala e a tshwenyega.")
        assert "Tlala" in tokens

    def test_ts_digraph_not_split(self, tokenizer):
        # 'tsala' = friend; 'ts' digraph at word start
        tokens = tokenizer.tokenize("Ke tsala ya gago.")
        assert "tsala" in tokens

    def test_kg_digraph_not_split(self, tokenizer):
        # 'kgosi' = chief; 'kg' digraph at word start
        tokens = tokenizer.tokenize("Kgosi e e nna kwa gae.")
        assert "Kgosi" in tokens

    def test_ng_digraph_preserved(self, tokenizer):
        # 'ngwana' = child; 'ng' digraph at word start
        tokens = tokenizer.tokenize("Ngwana o a lela.")
        assert "Ngwana" in tokens

    def test_ph_digraph_not_split(self, tokenizer):
        # 'phiri' = hyena; 'ph' at word start
        tokens = tokenizer.tokenize("Phiri o a goroga.")
        assert "Phiri" in tokens

    def test_sh_digraph_not_split(self, tokenizer):
        # 'shaba' = copper; 'sh' digraph
        tokens = tokenizer.tokenize("Shaba e e ntle.")
        assert "Shaba" in tokens

    def test_digraphs_class_attribute_ordered_longest_first(self):
        # tlh must come before tl, tsh before ts, to ensure correct matching
        digraphs = list(Tokenizer.DIGRAPHS)
        assert digraphs.index("tlh") < digraphs.index("tl")
        assert digraphs.index("tsh") < digraphs.index("ts")


class TestTokenizerApostrophe:
    """
    Apostrophes in Setswana mark morpheme boundaries within words.
    They are NOT sentence-level punctuation and must not split a word token.
    See docs/orthography.md — Apostrophe Usage section.
    """

    def test_apostrophe_within_word_preserved_as_single_token(self, tokenizer):
        # Word-internal apostrophe: the whole string including ' is one token
        tokens = tokenizer.tokenize("o'a bua")
        # "o'a" should be a single token, not split into "o", "'", "a"
        assert "o'a" in tokens
        assert tokens.count("'") == 0  # no bare apostrophe token

    def test_sentence_with_apostrophe_word_correct_token_count(self, tokenizer):
        tokens = tokenizer.tokenize("o'a bua Setswana")
        # Expect 3 tokens: "o'a", "bua", "Setswana"
        assert len(tokens) == 3


class TestTokenizerSentences:
    def test_tokenize_sentences_returns_list_of_lists(self, tokenizer):
        result = tokenizer.tokenize_sentences("Ke a bua. O tlhoga jang?")
        assert isinstance(result, list)
        assert all(isinstance(s, list) for s in result)

    def test_tokenize_sentences_two_sentences(self, tokenizer):
        result = tokenizer.tokenize_sentences("Ke a bua. O tlhoga jang?")
        assert len(result) == 2

    def test_tokenize_sentences_empty_input(self, tokenizer):
        assert tokenizer.tokenize_sentences("") == []

    def test_each_sentence_correctly_tokenized(self, tokenizer):
        result = tokenizer.tokenize_sentences("Ke a bua. O tlhoga jang?")
        # First sentence should contain period
        assert "." in result[0]
        # Second should contain question mark
        assert "?" in result[1]


class TestTokenizerDetokenize:
    def test_detokenize_rejoins_words(self, tokenizer):
        tokens = ["Ke", "a", "bua"]
        assert tokenizer.detokenize(tokens) == "Ke a bua"

    def test_detokenize_no_space_before_period(self, tokenizer):
        tokens = ["Ke", "a", "bua", "."]
        assert tokenizer.detokenize(tokens) == "Ke a bua."

    def test_detokenize_empty_list(self, tokenizer):
        assert tokenizer.detokenize([]) == ""

    def test_roundtrip_basic(self, tokenizer):
        original = "Ke a bua Setswana."
        tokens = tokenizer.tokenize(original)
        reconstructed = tokenizer.detokenize(tokens)
        assert reconstructed == original
