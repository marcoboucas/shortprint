"""Test typeprint.py file."""

from typing import Any

import pytest

from dprint.typeprint import typeprint_str


@pytest.mark.parametrize(
    "test_input,expected", [(1, "int"), (-1, "int"), (1.2, "float"), ("2", "str")]
)
def test_typeprint(test_input: Any, expected: str):
    """Test the typeprint_str() function."""

    assert typeprint_str(test_input) == expected
