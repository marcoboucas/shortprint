"""TypePrint."""
# pylint: disable=C0415

from collections import defaultdict
from dataclasses import is_dataclass
from datetime import date, datetime, timedelta
from functools import partial
from typing import Any, Callable, Dict, Optional, Set, Tuple

from shortprint.config import MAX_DEPTH, PADDING
from shortprint.typers import type_dataclass, type_dict, type_list, type_tuple
from shortprint.typers.object_typer import type_object
from shortprint.typers.set_typer import type_set
from shortprint.utils import add_padding, display_caller, get_type

SPECIAL_OBJECTS: Dict[Tuple, Callable[..., str]] = {
    (tuple,): type_tuple,
    (list,): type_list,
    (dict, defaultdict): type_dict,
    (set, frozenset): type_set,
}


# TODO: Reduce the complexity of the function for modules types (numpy, ...)
# pylint: disable=too-many-return-statements
def shortprint_str(  # noqa: C901
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
    kwargs = dict(current_padding=current_padding, padding_increment=padding_increment)

    # Base types
    if element is None:
        return add_padding("None", current_padding)
    if isinstance(element, (str, int, float, date, datetime, timedelta, bytes)):
        return add_padding(type_, current_padding)

    # Special objects
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

    # Special objects
    for types, type_func in SPECIAL_OBJECTS.items():
        if isinstance(element, types):
            return type_func(
                element=element,
                recursive_func=recursive_func,
                is_depth_reached=depth == 0,
                **kwargs,  # type: ignore
            )

    # Not classic types
    if is_dataclass(element):
        return type_dataclass(
            element=element,
            recursive_func=recursive_func,
            is_depth_reached=depth == 0,
            **kwargs,  # type: ignore
        )

    # Module types
    try:
        import numpy as np
    except ImportError:
        pass
    else:
        if isinstance(element, np.ndarray):
            from shortprint.typers import type_ndarray

            return type_ndarray(
                element=element,
                current_padding=current_padding,
            )

    return type_object(
        element=element,
        recursive_func=recursive_func,
        is_depth_reached=depth == 0,
        **kwargs,  # type: ignore
    )


def shortprint_print(
    *args,
    display_info: bool = True,
    **kwargs,
) -> str:
    """Typeprint an element."""
    if display_info:
        display_caller()
    result = shortprint_str(*args, **kwargs)
    print(result)
    return result
