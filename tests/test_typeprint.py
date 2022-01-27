"""Test typeprint.py file."""

from typing import Any

import pytest

from typrint.typeprint import add_padding, get_type, typeprint_str


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


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (1, "int\n"),
        (-1, "int\n"),
        (1.2, "float\n"),
        ("2", "str\n"),
        ([1, 2, 3], "List[\n  (3)int\n]\n"),
        ([1, 2, 3, "abc"], "List[\n  (3)int\n  (1)str\n]\n"),
        ([1, 2, 3, "abc", 3.5, 3.1], "List[\n  (2)float\n  (3)int\n  (1)str\n]\n"),
        ([], "List[]\n"),
    ],
)
def test_typeprint(test_input: Any, expected: str):
    """Test the typeprint_str() function."""

    assert typeprint_str(test_input) == expected
