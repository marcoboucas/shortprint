"""TypePrint."""

from typing import Any


def typeprint_str(element: Any) -> str:
    """Typeprint an element to string."""
    type_ = str(type(element)).split("'")[1]
    if isinstance(element, (str, int, float)):
        return type_
    return "Unknown Type"


def typeprint(element: Any) -> None:
    """Typeprint an element."""
    print(typeprint_str(element))
