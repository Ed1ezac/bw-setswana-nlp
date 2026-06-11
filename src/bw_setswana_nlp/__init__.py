"""
bw-setswana-nlp: NLP toolkit and language resources for Setswana (tn-BW).

Building digital infrastructure for Setswana as spoken in Botswana —
locale support, lexicon data, tokenization, and morphological tooling.
"""

__version__ = "0.1.0-dev"
__author__ = "Edgar Kealeboga and contributors"
__license__ = "MIT"

from bw_setswana_nlp.tokenizer import Tokenizer

__all__ = ["Tokenizer", "__version__"]
