"""
Text utility functions for Setswana (tn-BW) processing.

Character-level normalization and validation following the conventions in
docs/orthography.md. Used by the tokenizer and (in Phase 2) the morphological
analyzer.
"""

import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize Unicode text for Setswana processing.

    Applies NFC normalization and strips leading/trailing whitespace.
    Does NOT lowercase — case is meaningful in Setswana (proper nouns,
    sentence-initial words).

    Args:
        text: Raw input text string.

    Returns:
        NFC-normalized, stripped string.
    """
    return unicodedata.normalize("NFC", text).strip()


def is_setswana_char(char: str) -> bool:
    """
    Return True if the character is a valid Setswana orthographic character.

    Valid characters are Latin letters (a-z, A-Z) and the apostrophe ('),
    which marks morpheme boundaries in Setswana text. Digits, punctuation
    (other than apostrophe), and whitespace return False.

    Args:
        char: A single character string.

    Returns:
        True if char is a valid Setswana orthographic character.

    Raises:
        ValueError: If char is not a single character.
    """
    if len(char) != 1:
        raise ValueError(f"Expected a single character, got string of length {len(char)!r}")
    return char.isalpha() or char == "'"


def remove_diacritics(text: str) -> str:
    """
    Strip diacritical marks from text (lossy normalization).

    Standard Setswana orthography uses no diacritics on native words, but
    source materials may contain them (older orthographies, IPA transcriptions,
    loanwords). This function is intended for fuzzy search and matching only.

    Do NOT use this for data storage — always store NFC-normalized forms
    with diacritics intact.

    Args:
        text: Input text possibly containing diacritical marks.

    Returns:
        Text with all combining diacritical marks (Unicode category Mn) removed.

    Examples:
        >>> remove_diacritics("é")
        'e'
        >>> remove_diacritics("motho")
        'motho'
    """
    return "".join(
        c
        for c in unicodedata.normalize("NFD", text)
        if unicodedata.category(c) != "Mn"
    )
