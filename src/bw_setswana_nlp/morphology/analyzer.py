"""
Setswana morphological analyzer.

Phase 2 component. Analyzes Setswana word forms into their morphemic components
using noun class prefixes, verb stem patterns, and agglutination rules
documented in docs/noun-classes.md.

This module defines the interface — implementation follows in Phase 2.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MorphemeAnalysis:
    """Result of morphological analysis for a single word form."""

    surface_form: str
    stem: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    noun_class: Optional[int] = None
    pos: Optional[str] = None
    features: dict = field(default_factory=dict)


class MorphologicalAnalyzer:
    """
    Rule-based morphological analyzer for Setswana (tn-BW).

    Phase 2 — not yet implemented. See docs/noun-classes.md for the grammatical
    foundation and open issues tagged 'Phase-2' to contribute.

    Analyzes surface word forms into stem + affixes using Setswana noun class
    prefixes and verb conjugation rules.

    Examples (planned interface):
        >>> analyzer = MorphologicalAnalyzer()
        >>> result = analyzer.analyze("batho")
        >>> result.stem
        'tho'
        >>> result.prefix
        'ba'
        >>> result.noun_class
        2
    """

    def analyze(self, word: str) -> MorphemeAnalysis:
        """
        Analyze a single word form into its morphemic components.

        Args:
            word: A single Setswana word token (as returned by Tokenizer).

        Returns:
            MorphemeAnalysis with stem, prefix, suffix, noun class, and features.

        Raises:
            NotImplementedError: Phase 2 — not yet implemented.
        """
        raise NotImplementedError(
            "MorphologicalAnalyzer is a Phase 2 component. "
            "See docs/noun-classes.md and open issues tagged 'Phase-2'."
        )

    def lemmatize(self, word: str) -> str:
        """
        Return the base/dictionary form (lemma) of a word.

        Strips inflectional affixes to return the stem in its canonical form
        as it would appear in the lexicon.

        Args:
            word: A single Setswana word token.

        Returns:
            The lemma form (stem without inflectional affixes).

        Raises:
            NotImplementedError: Phase 2 — not yet implemented.
        """
        raise NotImplementedError(
            "lemmatize() is a Phase 2 component. "
            "See docs/noun-classes.md and open issues tagged 'Phase-2'."
        )
