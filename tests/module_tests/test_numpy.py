"""Module tests."""


from typing import List

import pytest

from shortprint.shortprint import shortprint_str

TEST_INSTANCES: List = []
try:
    import numpy as np

    TEST_INSTANCES = [
        (np.array([12.3, 13], dtype=np.float64), "NDArray[(2,), dtype=float64]\n"),
        (np.array([12, 13], dtype=np.int32), "NDArray[(2,), dtype=int32]\n"),
        (np.array([[12, 13]], dtype=np.int32), "NDArray[(1, 2), dtype=int32]\n"),
        (
            np.array([[12.3, 13.2]], dtype=np.float64),
            "NDArray[(1, 2), dtype=float64]\n",
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
