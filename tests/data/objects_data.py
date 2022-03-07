"""Objects tests data."""


# pylint: disable=missing-class-docstring,too-few-public-methods
class ObjectWithDict:
    def __init__(self) -> None:
        self.__dict__ = {}


TESTS_FOR_OBJECTS = [
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
