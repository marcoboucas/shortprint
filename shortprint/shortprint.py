"""TypePrint."""

from dataclasses import is_dataclass
from datetime import date, datetime, timedelta
from functools import partial
from typing import Any, Optional, Set

from shortprint.config import MAX_DEPTH, PADDING
from shortprint.typers import type_dataclass, type_dict, type_list, type_tuple
from shortprint.typers.object_typer import type_object
from shortprint.typers.set_typer import type_set
from shortprint.utils import add_padding, get_type


# pylint: disable=too-many-return-statements
def shortprint_str(
    element: Any,
    *,
    current_padding: str = "",
    padding_increment: int = PADDING,
    depth: Optional[int] = MAX_DEPTH,
    already_visited: Optional[Set[str]] = None,
) -> str:
    """Typeprint an element to string."""
    if depth is None:
        depth = -1
    if already_visited is None:
        already_visited = set()
    type_ = get_type(element)

    # Base types
    if element is None:
        return add_padding("None", current_padding)
    if isinstance(element, (str, int, float, date, datetime, timedelta, bytes)):
        return add_padding(type_, current_padding)

    # Special objects
    recursive_func = partial(shortprint_str, depth=depth - 1)
    element_identifier = str(id(element))
    if element_identifier in already_visited:
        return add_padding(
            f"<Recursion avoided: '{element.__class__.__name__}'>", current_padding
        )
    already_visited.add(element_identifier)

    kwargs = dict(
        current_padding=current_padding,
        padding_increment=padding_increment,
    )
    recursive_func = partial(
        shortprint_str,
        depth=depth - 1,
        already_visited=already_visited,
        padding_increment=padding_increment,
    )
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
            recursive_func=shortprint_str,
            is_depth_reached=depth == 0,
            **kwargs,  # type: ignore
        )

    return type_object(
        element=element,
        recursive_func=shortprint_str,
        is_depth_reached=depth == 0,
        **kwargs,  # type: ignore
    )


def shortprint_print(*args, **kwargs) -> str:
    """Print the results."""
    result = shortprint_str(*args, **kwargs)
    print(result)
    return result
