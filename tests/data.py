"""Test data."""

from dataclasses import dataclass

import numpy as np


@dataclass
class TestDataclass:
    """Test dataclass."""

    attribute_str: str = "hello"
    attribute_int: int = 1


TESTS_FOR_LIST = [
    ([1, 2, 3], "List[\n  (3) int\n]\n"),
    ([1, 2, 3, "abc"], "List[\n  (3) int\n  (1) str\n]\n"),
    ([1, 2, 3, "abc", 3.5, 3.1], "List[\n  (2) float\n  (3) int\n  (1) str\n]\n"),
    ([], "List[]\n"),
]

TESTS_FOR_DATACLASSES = [
    (
        TestDataclass(),
        "TestDataclass(\n  attribute_int: int\n  attribute_str: str\n)\n",
    ),
    (
        TestDataclass("bye"),
        "TestDataclass(\n  attribute_int: int\n  attribute_str: str\n)\n",
    ),
]


TESTS_FOR_STANDARD = [
    (1, "int\n"),
    (-1, "int\n"),
    (1.2, "float\n"),
    ("2", "str\n"),
]


TEST_FOR_DICT = [
    ({"hello": "world"}, "Dict[\n  (1) str: str\n]\n"),
    ({"hello": "world", "bonjour": "monde"}, "Dict[\n  (2) str: str\n]\n"),
    ({1: "world"}, "Dict[\n  (1) int: str\n]\n"),
    ({1: "world", 0: "hello"}, "Dict[\n  (2) int: str\n]\n"),
    (
        {1: ["world"], 0: "h"},
        "Dict[\n  (1) int: List[\n    (1) str\n  ]\n  (1) int: str\n]\n",
    ),
    ({}, "Dict[]\n"),
]

TEST_NDARRAY = [
    (np.array([12.3, 13]), "NDArray[(2,), dtype=float64]\n"),
    (np.array([12, 13]), "NDArray[(2,), dtype=int32]\n"),
    (np.array([[12, 13]]), "NDArray[(1, 2), dtype=int32]\n"),
    (np.array([[12.3, 13.2]]), "NDArray[(1, 2), dtype=float64]\n"),
    (np.array([[12.3, 13.2]]), "NDArray[(1, 2), dtype=float64]\n"),
]


ALL_TESTS = [
    TESTS_FOR_LIST,
    TESTS_FOR_STANDARD,
    TEST_FOR_DICT,
    TESTS_FOR_DATACLASSES,
    TEST_NDARRAY,
]
