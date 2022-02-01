"""Test typeprint.py file."""

from itertools import chain
from typing import Any

import pytest

from shortprint.shortprint import shortprint

from .data import ALL_TESTS


@pytest.mark.parametrize(
    "test_input,expected",
    list(chain(*ALL_TESTS)),  # type: ignore
)
def test_typeprint(test_input: Any, expected: str):
    """Test the typeprint_str() function."""

    assert shortprint(test_input) == expected
