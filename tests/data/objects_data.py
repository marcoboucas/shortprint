"""Objects tests data."""

from requests import Request


# pylint: disable=missing-class-docstring,too-few-public-methods
class ObjectWithDict:
    def __init__(self) -> None:
        self.__dict__ = {}


TESTS_FOR_OBJECTS = [
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
    (ObjectWithDict(), "tests.data.objects_data.ObjectWithDict()\n"),
    (
        [[[[ObjectWithDict()]]]],
        """List[
  (1) List[
    (1) List[
      (1) List[
        (1) tests.data.objects_data.ObjectWithDict(...)
      ]
    ]
  ]
]\n""",
    ),
]
