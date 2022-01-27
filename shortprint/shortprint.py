"""TypePrint."""

from dataclasses import is_dataclass
from typing import Any

from shortprint.config import PADDING
from shortprint.typers import type_dataclass, type_dict, type_list
from shortprint.utils import add_padding, get_type


def shortprint_str(
    element: Any, current_padding: str = "", padding_increment: int = PADDING
) -> str:
    """Typeprint an element to string."""
    type_ = get_type(element)
    if isinstance(element, (str, int, float)):
        return add_padding(type_, current_padding)
    if isinstance(element, list):
        return type_list(
            element=element,
            recursive_func=shortprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )
    if isinstance(element, dict):
        return type_dict(
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

    return f"Unknown Type ({element.__class__.__name__})"


def shortprint(*args, **kwargs) -> None:
    """Typeprint an element."""
    print(shortprint_str(*args, **kwargs))
