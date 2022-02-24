"""Module Tests."""


from typing import List

import pytest

from shortprint.shortprint import shortprint_str

TEST_INSTANCES: List = []
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LinearRegression

    TEST_INSTANCES = [
        (
            LinearRegression(),
            """sklearn.linear_model._base.LinearRegression(
  copy_X: bool
  fit_intercept: bool
  n_jobs: None
  normalize: str
  positive: bool
)
""",
        ),
        (
            TfidfVectorizer(),
            """sklearn.feature_extraction.text.TfidfVectorizer(
  analyzer: str
  binary: bool
  decode_error: str
  dtype: type(
    as_integer_ratio: method_descriptor
    is_integer: method_descriptor
  )
  encoding: str
  input: str
  lowercase: bool
  max_df: float
  max_features: None
  min_df: int
  ngram_range: Tuple[
    (2) int
  ]
  preprocessor: None
  stop_words: None
  strip_accents: None
  token_pattern: str
  tokenizer: None
  vocabulary: None
)
""",
        ),
        (
            TfidfVectorizer().fit(["hello world", "my name is marco"]),
            """sklearn.feature_extraction.text.TfidfVectorizer(
  analyzer: str
  binary: bool
  decode_error: str
  dtype: type(
    as_integer_ratio: method_descriptor
    is_integer: method_descriptor
  )
  encoding: str
  fixed_vocabulary_: bool
  input: str
  lowercase: bool
  max_df: float
  max_features: None
  min_df: int
  ngram_range: Tuple[
    (2) int
  ]
  preprocessor: None
  stop_words: None
  stop_words_: Set{}
  strip_accents: None
  token_pattern: str
  tokenizer: None
  vocabulary: None
  vocabulary_: Dict[
    (6) str: int
  ]
)
""",
        ),
    ]


except ImportError:
    pass


@pytest.mark.module
@pytest.mark.parametrize(
    "test_input,expected",
    TEST_INSTANCES,  # type: ignore
)
def test_function(test_input, expected):
    """Test shortprint reaction to those objects."""

    assert shortprint_str(test_input) == expected
