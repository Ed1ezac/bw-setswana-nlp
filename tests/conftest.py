"""Shared pytest fixtures for bw-setswana-nlp tests."""

import pytest

from bw_setswana_nlp.tokenizer import Tokenizer


@pytest.fixture
def tokenizer() -> Tokenizer:
    """Return a default Tokenizer instance (keep_punctuation=True)."""
    return Tokenizer()


@pytest.fixture
def tokenizer_no_punct() -> Tokenizer:
    """Return a Tokenizer configured to discard punctuation tokens."""
    return Tokenizer(keep_punctuation=False)


# Real Setswana sentences used across multiple test modules
SAMPLE_SENTENCES = [
    "Ke a bua Setswana.",
    "O tlhoga jang?",
    "Lefatshe la Botswana le a galalela.",
    "Ntlo e e kwa moseja.",
    "Batho ba a bua.",
]
