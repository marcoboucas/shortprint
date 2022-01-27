"""Test utils.py file."""

from typing import Any

import pytest

from typrint.utils import add_padding, get_type


@pytest.mark.parametrize(
    "test_input,current_padding,expected",
    [
        ("1", " " * 2, "  1\n"),
        ("ab\ncd", " " * 2, "  ab\n  cd\n"),
    ],
)
def test_add_padding(test_input: str, current_padding: str, expected: str):
    """Test the add_padding() function."""
    assert add_padding(test_input, current_padding=current_padding) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [(1, "int"), (1.2, "float"), ("d", "str")],
)
def test_get_type(test_input: Any, expected: str):
    """Test the get_type() function."""

    assert get_type(test_input) == expected
