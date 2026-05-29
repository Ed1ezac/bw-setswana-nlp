"""Tests for bw_setswana_nlp.morphology.MorphologicalAnalyzer.

Phase 2 — these tests define the planned interface and are skipped until
the morphological analyzer is implemented. See docs/noun-classes.md and
open issues tagged 'Phase-2' to contribute.
"""

import pytest

from bw_setswana_nlp.morphology import MorphemeAnalysis, MorphologicalAnalyzer


class TestMorphologicalAnalyzerPhase2Interface:
    def test_analyze_raises_not_implemented_in_phase1(self):
        """Phase 1 safety check: calling analyze() raises NotImplementedError."""
        analyzer = MorphologicalAnalyzer()
        with pytest.raises(NotImplementedError):
            analyzer.analyze("motho")

    def test_lemmatize_raises_not_implemented_in_phase1(self):
        """Phase 1 safety check: calling lemmatize() raises NotImplementedError."""
        analyzer = MorphologicalAnalyzer()
        with pytest.raises(NotImplementedError):
            analyzer.lemmatize("batho")


class TestMorphemeAnalysisDataclass:
    def test_morpheme_analysis_created_with_surface_form(self):
        result = MorphemeAnalysis(surface_form="motho")
        assert result.surface_form == "motho"

    def test_morpheme_analysis_optional_fields_default_none(self):
        result = MorphemeAnalysis(surface_form="motho")
        assert result.stem is None
        assert result.prefix is None
        assert result.noun_class is None
        assert result.pos is None

    def test_morpheme_analysis_features_defaults_to_empty_dict(self):
        result = MorphemeAnalysis(surface_form="motho")
        assert result.features == {}


class TestMorphologicalAnalyzerPlannedBehavior:
    """
    These tests describe the planned Phase 2 behavior. They are all skipped.
    When implementing Phase 2, remove the pytest.skip() calls and implement
    the analyzer to make them pass.
    """

    def test_analyze_class1_noun_returns_correct_class(self):
        """motho (person) is a Class 1 noun with prefix mo-."""
        pytest.skip("Phase 2 — not yet implemented")
        analyzer = MorphologicalAnalyzer()
        result = analyzer.analyze("motho")
        assert result.noun_class == 1
        assert result.prefix == "mo"
        assert result.stem == "tho"

    def test_analyze_class2_noun_plural(self):
        """batho (people) is Class 2, plural of motho."""
        pytest.skip("Phase 2 — not yet implemented")
        analyzer = MorphologicalAnalyzer()
        result = analyzer.analyze("batho")
        assert result.noun_class == 2
        assert result.prefix == "ba"

    def test_analyze_class9_noun(self):
        """naga (country/land) is a Class 9 noun."""
        pytest.skip("Phase 2 — not yet implemented")
        analyzer = MorphologicalAnalyzer()
        result = analyzer.analyze("naga")
        assert result.noun_class == 9

    def test_lemmatize_verb_returns_stem(self):
        """Verb lemmatization should return the base stem."""
        pytest.skip("Phase 2 — not yet implemented")
        analyzer = MorphologicalAnalyzer()
        assert analyzer.lemmatize("bua") == "bua"

    def test_analyze_returns_morpheme_analysis_instance(self):
        """analyze() should return a MorphemeAnalysis object."""
        pytest.skip("Phase 2 — not yet implemented")
        analyzer = MorphologicalAnalyzer()
        result = analyzer.analyze("motho")
        assert isinstance(result, MorphemeAnalysis)
