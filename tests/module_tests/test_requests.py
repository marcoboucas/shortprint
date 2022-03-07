"""Module Tests."""


from typing import List

import pytest

from shortprint.shortprint import shortprint_str

TEST_INSTANCES: List = []
try:
    from requests import Request

    TEST_INSTANCES = [
        (
            Request(),
            """requests.models.Request(
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
            """requests.models.Request(
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
