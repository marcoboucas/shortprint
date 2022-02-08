"""Numpy tests data."""

import numpy as np

TESTS_NDARRAY = [
    (np.array([12.3, 13], dtype=np.float64), "NDArray[(2,), dtype=float64]\n"),
    (np.array([12, 13], dtype=np.int32), "NDArray[(2,), dtype=int32]\n"),
    (np.array([[12, 13]], dtype=np.int32), "NDArray[(1, 2), dtype=int32]\n"),
    (np.array([[12.3, 13.2]], dtype=np.float64), "NDArray[(1, 2), dtype=float64]\n"),
]
