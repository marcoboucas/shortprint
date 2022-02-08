"""Depth data."""

from typing import List

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
