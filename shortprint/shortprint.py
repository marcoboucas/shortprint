"""TypePrint."""

from dataclasses import is_dataclass
from datetime import date, datetime, timedelta
from functools import partial
from typing import Any, Optional

from shortprint.config import MAX_DEPTH, PADDING
from shortprint.typers import type_dataclass, type_dict, type_list, type_tuple
from shortprint.typers.object_typer import type_object
from shortprint.typers.set_typer import type_set
from shortprint.utils import add_padding, get_type, print_output


# pylint: disable=too-many-return-statements
@print_output
def shortprint(
    element: Any,
    *,
    current_padding: str = "",
    padding_increment: int = PADDING,
    depth: Optional[int] = MAX_DEPTH,
) -> str:
    """Typeprint an element to string.

    :param depth: The maximum depth, set to -1 or None to disable the max depth.
    """
    if depth is None:
        depth = -1
    type_ = get_type(element)

    if element is None:
        return add_padding("None", current_padding)
    if isinstance(element, (str, int, float, date, datetime, timedelta, bytes)):
        return add_padding(type_, current_padding)

    kwargs = dict(current_padding=current_padding, padding_increment=padding_increment)
    # Special objects
    recursive_func = partial(shortprint, depth=depth - 1)
    if isinstance(element, tuple):
        return type_tuple(
            element=element,
            recursive_func=recursive_func,
            is_depth_reached=depth == 0,
            **kwargs,  # type: ignore
        )
    if isinstance(element, list):
        return type_list(
            element=element,
            recursive_func=recursive_func,
            is_depth_reached=depth == 0,
            **kwargs,  # type: ignore
        )
    if isinstance(element, dict):
        return type_dict(
            element=element,
            recursive_func=recursive_func,
            is_depth_reached=depth == 0,
            **kwargs,  # type: ignore
        )
    if isinstance(element, (set, frozenset)):
        return type_set(
            element=element,
            recursive_func=recursive_func,
            is_depth_reached=depth == 0,
            **kwargs,  # type: ignore
        )
    if is_dataclass(element):
        return type_dataclass(
            element=element,
            recursive_func=shortprint,
            is_depth_reached=depth == 0,
            **kwargs,  # type: ignore
        )

    return type_object(
        element=element,
        recursive_func=shortprint,
        is_depth_reached=depth == 0,
        **kwargs,  # type: ignore
    )
