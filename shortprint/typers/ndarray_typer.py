"""NDArray typer."""
# pylint: disable=E0401
import numpy as np

from shortprint.utils import add_padding


def type_ndarray(
    *,
    element: np.ndarray,
    current_padding: str,
) -> str:
    """Type for a dataclass."""
    return add_padding(
        f"NDArray[{element.shape}, dtype={element.dtype}]", current_padding
    )
