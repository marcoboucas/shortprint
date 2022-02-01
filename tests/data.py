"""Test data."""
# pylint: disable=missing-class-docstring,too-few-public-methods
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, List, Tuple

import numpy as np
from requests import Request


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

TEST_NDARRAY = [
    (np.array([12.3, 13]), "NDArray[(2,), dtype=float64]\n"),
    (np.array([12, 13]), "NDArray[(2,), dtype=int32]\n"),
    (np.array([[12, 13]]), "NDArray[(1, 2), dtype=int32]\n"),
    (np.array([[12.3, 13.2]]), "NDArray[(1, 2), dtype=float64]\n"),
    (np.array([[12.3, 13.2]]), "NDArray[(1, 2), dtype=float64]\n"),
]


TESTS_FOR_TUPLE = [
    ((1, 2, 3), "Tuple[\n  (3) int\n]\n"),
    ((1, 2, 3, "abc"), "Tuple[\n  (3) int\n  (1) str\n]\n"),
    ((1, 2, 3, "abc", 3.5, 3.1), "Tuple[\n  (2) float\n  (3) int\n  (1) str\n]\n"),
    ((), "Tuple[]\n"),
]

recursive_list: List = [1, 2]
recursive_list.append(recursive_list)

TESTS_FOR_RECURSION = [
    (
        recursive_list,
        """List[
  (2) int
  (1) <Recursion avoided: 'list'>
]
""",
    )
]
TESTS_NDARRAY = [
    (np.array([12.3, 13]), "NDArray[(2,), dtype=float64]\n"),
    (np.array([12, 13]), "NDArray[(2,), dtype=int32]\n"),
    (np.array([[12, 13]]), "NDArray[(1, 2), dtype=int32]\n"),
    (np.array([[12.3, 13.2]]), "NDArray[(1, 2), dtype=float64]\n"),
]


TESTS_DEPTH = [
    (
        [[[[[[[5]]]]]]],
        """List[
  (1) List[
    (1) List[
      (1) List[
        (1) List[...]
      ]
    ]
  ]
]
""",
    )
]


class ObjectWithDict:
    def __init__(self) -> None:
        self.__dict__ = {}


TESTS_FOR_OBJECTS = [
    (
        Request(),
        """Request(
  auth: None
  cookies: None
  data: List[]
  files: List[]
  headers: Dict[]
  hooks: Dict[
    (1) str: List[]
  ]
  json: None
  method: None
  params: Dict[]
  url: None
)
""",
    ),
    (
        Request("hello"),
        """Request(
  auth: None
  cookies: None
  data: List[]
  files: List[]
  headers: Dict[]
  hooks: Dict[
    (1) str: List[]
  ]
  json: None
  method: str
  params: Dict[]
  url: None
)
""",
    ),
    (ObjectWithDict(), "ObjectWithDict()\n"),
]

TESTS_FOR_SET = [({1, 2}, "Set{\n  (2) int\n}\n"), (set(), "Set{}\n")]

ALL_TESTS = [
    TESTS_FOR_LIST,
    TESTS_FOR_STANDARD,
    TESTS_FOR_DICT,
    TESTS_FOR_DATACLASSES,
    TEST_NDARRAY,
    TESTS_FOR_OBJECTS,
    TESTS_FOR_TUPLE,
    TESTS_FOR_DEFAULTDICT,
    TESTS_FOR_SET,
    TESTS_DEPTH,
    TESTS_FOR_RECURSION,
    TESTS_NDARRAY,
]
