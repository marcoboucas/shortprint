"""Test typeprint.py file."""

from itertools import chain
from typing import Any

import pytest

from typrint.typeprint import typeprint_str

from .data import ALL_TESTS


@pytest.mark.parametrize(
    "test_input,expected",
    list(chain(*ALL_TESTS)),
)
def test_typeprint(test_input: Any, expected: str):
    """Test the typeprint_str() function."""

    assert typeprint_str(test_input) == expected
