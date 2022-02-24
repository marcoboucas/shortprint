"""Tests for numpy."""


from typing import List

import pytest

from shortprint.shortprint import shortprint_str

CAN_RUN_TEST = True
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
    CAN_RUN_TEST = False


@pytest.mark.module
@pytest.mark.parametrize(
    "test_input,expected",
    TEST_INSTANCES,  # type: ignore
)
def test_numpy(test_input, expected):
    """Test numpy objects."""

    assert shortprint_str(test_input) == expected
