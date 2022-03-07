"""Test data for dataclasses."""

from dataclasses import dataclass


@dataclass
class TestDataclass:
    """Test dataclass."""

    attribute_str: str = "hello"
    attribute_int: int = 1


TESTS_FOR_DATACLASSES = [
    (
        TestDataclass(),
        "TestDataclass(\n  attribute_int: int\n  attribute_str: str\n)\n",
    ),
    (
        TestDataclass("bye"),
        "TestDataclass(\n  attribute_int: int\n  attribute_str: str\n)\n",
    ),
    (
        [[[[TestDataclass("bye")]]]],
        """List[
  (1) List[
    (1) List[
      (1) List[
        (1) TestDataclass(...)
      ]
    ]
  ]
]
""",
    ),
]
