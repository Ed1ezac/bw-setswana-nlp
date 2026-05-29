"""Tests for bw_setswana_nlp.utils text utilities.

These tests cover real implementations in utils/text.py and should
pass immediately after installation with `pip install -e ".[dev]"`.
"""

import pytest

from bw_setswana_nlp.utils import is_setswana_char, normalize_text, remove_diacritics


class TestNormalizeText:
    def test_strips_leading_whitespace(self):
        assert normalize_text("  motho") == "motho"

    def test_strips_trailing_whitespace(self):
        assert normalize_text("motho  ") == "motho"

    def test_strips_both_sides(self):
        assert normalize_text("  motho  ") == "motho"

    def test_empty_string_returns_empty(self):
        assert normalize_text("") == ""

    def test_whitespace_only_returns_empty(self):
        assert normalize_text("   ") == ""

    def test_nfc_normalization_applied(self):
        # NFD: e + combining acute accent (two code points)
        nfd_form = "é"
        # NFC: precomposed é (one code point)
        nfc_form = "\xe9"
        assert normalize_text(nfd_form) == nfc_form

    def test_does_not_lowercase(self):
        # Case is meaningful in Setswana (proper nouns, sentence-initial words)
        assert normalize_text("Botswana") == "Botswana"
        assert normalize_text("SETSWANA") == "SETSWANA"

    def test_plain_setswana_word_unchanged(self):
        assert normalize_text("motho") == "motho"


class TestIsSetswanaChar:
    def test_lowercase_letter_is_valid(self):
        assert is_setswana_char("a") is True

    def test_uppercase_letter_is_valid(self):
        assert is_setswana_char("A") is True

    def test_apostrophe_is_valid(self):
        # Apostrophe marks morpheme boundaries in Setswana
        assert is_setswana_char("'") is True

    def test_digit_is_not_valid(self):
        assert is_setswana_char("1") is False

    def test_space_is_not_valid(self):
        assert is_setswana_char(" ") is False

    def test_period_is_not_valid(self):
        assert is_setswana_char(".") is False

    def test_question_mark_is_not_valid(self):
        assert is_setswana_char("?") is False

    def test_multi_char_raises_value_error(self):
        with pytest.raises(ValueError):
            is_setswana_char("ab")

    def test_empty_string_raises_value_error(self):
        with pytest.raises(ValueError):
            is_setswana_char("")

    def test_all_setswana_alphabet_letters(self):
        # All 26 letters should be valid
        for letter in "abcdefghijklmnopqrstuvwxyz":
            assert is_setswana_char(letter) is True
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            assert is_setswana_char(letter) is True


class TestRemoveDiacritics:
    def test_removes_acute_accent(self):
        assert remove_diacritics("\xe9") == "e"   # é → e

    def test_removes_grave_accent(self):
        assert remove_diacritics("\xe0") == "a"   # à → a

    def test_removes_circumflex(self):
        assert remove_diacritics("\xea") == "e"   # ê → e

    def test_plain_setswana_word_unchanged(self):
        assert remove_diacritics("motho") == "motho"

    def test_plain_sentence_unchanged(self):
        assert remove_diacritics("Ke a bua Setswana.") == "Ke a bua Setswana."

    def test_empty_string_returns_empty(self):
        assert remove_diacritics("") == ""

    def test_mixed_text_strips_only_diacritics(self):
        # Only combining marks removed, letters kept
        result = remove_diacritics("caf\xe9")  # café
        assert result == "cafe"
