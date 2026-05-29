"""
Setswana word tokenizer.

Handles Setswana-specific orthographic conventions:
- Digraphs and trigraphs (tlh, tsh, tl, ts, kg, ph, sh, ng) represent
  single phonemes and must not be split across tokens.
- Apostrophe marks morpheme boundaries within words and must not trigger
  word splitting.
- See docs/orthography.md for the full writing system reference.
- See docs/contributing/tokenizer-guide.md for implementation notes.
"""

import re
from typing import Optional

from bw_setswana_nlp.utils.text import normalize_text


class Tokenizer:
    """
    Word-level tokenizer for Setswana (tn-BW).

    Splits text into word tokens using whitespace and punctuation boundaries
    while preserving Setswana digraphs/trigraphs and apostrophe-containing
    words as single tokens.

    Examples:
        >>> t = Tokenizer()
        >>> t.tokenize("Ke a bua Setswana.")
        ['Ke', 'a', 'bua', 'Setswana', '.']
        >>> t.tokenize("O tlhoga jang?")
        ['O', 'tlhoga', 'jang', '?']
        >>> t.tokenize("")
        []
    """

    # Ordered longest-first so the trigraph 'tlh' is matched before 'tl',
    # and 'tsh' before 'ts'. Any regex or scan over these must use this order.
    DIGRAPHS: tuple[str, ...] = ("tlh", "tsh", "tl", "ts", "kg", "ph", "sh", "ng")

    def __init__(self, keep_punctuation: bool = True) -> None:
        """
        Initialize the tokenizer.

        Args:
            keep_punctuation: If True (default), punctuation marks are
                returned as separate tokens. If False, they are discarded.
        """
        self.keep_punctuation = keep_punctuation
        self._word_pattern = self._build_word_pattern()
        self._punct_pattern = re.compile(r"[^\w\s']+")
        self._sentence_boundary = re.compile(r"(?<=[.!?])\s+")

    def _build_word_pattern(self) -> re.Pattern:
        """
        Build a compiled regex that matches Setswana word tokens.

        A word token is a maximal sequence of Unicode word characters plus
        the apostrophe. This pattern handles ASCII and extended Latin letters
        that may appear in loanwords or proper names.
        """
        # Match sequences of word characters (letters, digits) and apostrophes.
        # Apostrophe is included because it marks morpheme boundaries within words.
        return re.compile(r"[\w']+", re.UNICODE)

    def tokenize(self, text: str) -> list[str]:
        """
        Tokenize a Setswana text string into a list of word tokens.

        Splits on whitespace and punctuation. Digraphs (tlh, tl, ts, etc.)
        within a word remain as part of their word token — they are not split
        at the character level by this method, since word-level tokenization
        splits between words, not within them.

        Args:
            text: Input text in Setswana (tn-BW orthography).

        Returns:
            List of string tokens. Punctuation is returned as separate
            tokens if keep_punctuation=True. Returns [] for empty or
            whitespace-only input.

        Examples:
            >>> t = Tokenizer()
            >>> t.tokenize("O tlhoga jang?")
            ['O', 'tlhoga', 'jang', '?']
            >>> t.tokenize("Lefatshe la Botswana.")
            ['Lefatshe', 'la', 'Botswana', '.']
        """
        if not text or not text.strip():
            return []

        normalized = normalize_text(text)
        tokens: list[str] = []
        pos = 0

        while pos < len(normalized):
            char = normalized[pos]

            if char.isspace():
                pos += 1
                continue

            # Try to match a word token (letters + apostrophe)
            word_match = self._word_pattern.match(normalized, pos)
            if word_match:
                tokens.append(word_match.group())
                pos = word_match.end()
                continue

            # Non-word, non-space character — treat as punctuation
            if self.keep_punctuation:
                tokens.append(char)
            pos += 1

        return tokens

    def tokenize_sentences(self, text: str) -> list[list[str]]:
        """
        Split text into sentences, then tokenize each sentence.

        Uses `.`, `!`, and `?` followed by whitespace as sentence boundaries.
        This is a best-effort heuristic for Phase 1 — a dedicated sentence
        boundary detector is planned for Phase 3.

        Args:
            text: Multi-sentence Setswana text.

        Returns:
            List of token lists, one per detected sentence.
            Returns [[]] if text is empty or whitespace-only.

        Examples:
            >>> t = Tokenizer()
            >>> t.tokenize_sentences("Ke a bua. O tlhoga jang?")
            [['Ke', 'a', 'bua', '.'], ['O', 'tlhoga', 'jang', '?']]
        """
        if not text or not text.strip():
            return []

        sentences = self._sentence_boundary.split(text.strip())
        return [self.tokenize(s) for s in sentences if s.strip()]

    def detokenize(self, tokens: list[str]) -> str:
        """
        Reconstruct a string from tokens (best-effort, lossy).

        Joins tokens with spaces, then removes spaces before punctuation.
        This is a lossy operation — original whitespace and formatting
        cannot be fully recovered from tokens alone.

        Args:
            tokens: List of tokens as returned by tokenize().

        Returns:
            Reconstructed string with standard spacing.

        Examples:
            >>> t = Tokenizer()
            >>> t.detokenize(['Ke', 'a', 'bua', '.'])
            'Ke a bua.'
        """
        if not tokens:
            return ""

        result = " ".join(tokens)
        # Remove spaces before punctuation marks
        result = re.sub(r"\s+([.!?,;:'])", r"\1", result)
        return result
