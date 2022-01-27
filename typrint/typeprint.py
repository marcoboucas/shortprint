"""TypePrint."""

from reprlib import recursive_repr
from typing import Any

from typrint.config import PADDING
from typrint.typers import type_list, type_dict
from typrint.utils import add_padding, get_type


def typeprint_str(
    element: Any, current_padding: str = "", padding_increment: int = PADDING
) -> str:
    """Typeprint an element to string."""
    type_ = get_type(element)
    if isinstance(element, (str, int, float)):
        return add_padding(type_, current_padding)
    if isinstance(element, list):
        return type_list(
            element=element,
            recursive_func=typeprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )
    if isinstance(element, dict):
        return type_dict(
            element=element,
            recursive_func=typeprint_str,
            current_padding=current_padding,
            padding_increment=padding_increment,
        )

    return "Unknown Type"


def typeprint(*args, **kwargs) -> None:
    """Typeprint an element."""
    print("\n".join(typeprint_str(*args, **kwargs)))
