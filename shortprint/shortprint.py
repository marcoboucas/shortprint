"""TypePrint."""

from collections import defaultdict
from dataclasses import is_dataclass
from datetime import date, datetime, timedelta
from typing import Any

from shortprint.config import PADDING
from shortprint.typers import type_dataclass, type_dict, type_list, type_tuple
from shortprint.typers.object_typer import type_object
from shortprint.typers.set_typer import type_set
from shortprint.utils import add_padding, get_type


# pylint: disable=too-many-return-statements
def shortprint_str(
    element: Any, current_padding: str = "", padding_increment: int = PADDING
) -> str:
    """Typeprint an element to string."""
    type_ = get_type(element)
    if element is None:
        return add_padding("None", current_padding)
    if isinstance(element, (str, int, float, date, datetime, timedelta, bytes)):
        return add_padding(type_, current_padding)

    if isinstance(element, tuple):
        return type_tuple(
            element=element,
            recursive_func=shortprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )
    if isinstance(element, list):
        return type_list(
            element=element,
            recursive_func=shortprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )
    if isinstance(element, (dict, defaultdict)):
        return type_dict(
            element=element,
            recursive_func=shortprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )
    if isinstance(element, (set, frozenset)):
        return type_set(
            element=element,
            recursive_func=shortprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )
    if is_dataclass(element):
        return type_dataclass(
            element=element,
            recursive_func=shortprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )

    return type_object(
        element=element,
        recursive_func=shortprint_str,
        current_padding=current_padding,
        padding_increment=padding_increment,
    )


def shortprint(*args, **kwargs) -> None:
    """Typeprint an element."""
    print(shortprint_str(*args, **kwargs))
