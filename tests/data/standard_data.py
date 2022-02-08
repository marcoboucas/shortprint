"""Standard types."""

from collections import defaultdict
from typing import DefaultDict, List, Tuple

TESTS_FOR_STANDARD = [
    (1, "int\n"),
    (-1, "int\n"),
    (1.2, "float\n"),
    ("2", "str\n"),
]

TESTS_FOR_LIST = [
    ([1, 2, 3], "List[\n  (3) int\n]\n"),
    ([1, 2, 3, "abc"], "List[\n  (3) int\n  (1) str\n]\n"),
    ([1, 2, 3, "abc", 3.5, 3.1], "List[\n  (2) float\n  (3) int\n  (1) str\n]\n"),
    ([], "List[]\n"),
]


TESTS_FOR_DICT = [
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
TESTS_FOR_DEFAULTDICT: List[Tuple[DefaultDict, str]] = [
    (defaultdict(list, dict(a=[])), "DefaultDict[\n  (1) str: List[]\n]\n")
]


TESTS_FOR_SET = [({1, 2}, "Set{\n  (2) int\n}\n"), (set(), "Set{}\n")]

TESTS_FOR_TUPLE = [
    ((1, 2, 3), "Tuple[\n  (3) int\n]\n"),
    ((1, 2, 3, "abc"), "Tuple[\n  (3) int\n  (1) str\n]\n"),
    ((1, 2, 3, "abc", 3.5, 3.1), "Tuple[\n  (2) float\n  (3) int\n  (1) str\n]\n"),
    ((), "Tuple[]\n"),
]
