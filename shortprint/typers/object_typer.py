"""Object Typer."""

import logging
from typing import Any, Callable, List

from shortprint.utils import add_padding, get_type

FUNCTION_TYPES = {"builtin_function_or_method", "function", "method"}


def type_object(
    *,
    element: Any,
    recursive_func: Callable,
    current_padding: str,
    padding_increment: int,
    only_show_public_attributes: bool = True,
    only_show_attributes: bool = True,
    is_depth_reached: bool = False,
) -> str:
    """Type for a list."""
    logging.debug(
        "Object '%s' with type %s", element.__class__.__name__, get_type(element)
    )
    attributes: List[str]

    if is_depth_reached:  # Max depth
        return add_padding(f"{get_type(element)}()", current_padding)

    if hasattr(element, "__dict__"):
        # If we have access to dict, then easy peasy
        attributes = list(
            sorted(
                [
                    f"{key}: {recursive_func(value)[:-1]}"
                    for key, value in element.__dict__.items()
                    if not (key.startswith("_") and only_show_public_attributes)
                    and not (get_type(value) in FUNCTION_TYPES and only_show_attributes)
                ]
            )
        )
    else:
        # We try to use dir instead
        special_keys = [
            key
            for key in dir(element)
            if not (key.startswith("_") and only_show_public_attributes)
            and not (
                get_type(getattr(element, key)) in FUNCTION_TYPES
                and only_show_attributes
            )
        ]

        attributes = []
        for key in special_keys:
            attributes.append(f"{key}: {recursive_func(getattr(element,key))[:-1]}")
        attributes = list(sorted(attributes))

        if len(attributes) == 0:  # Standard for basic types
            return add_padding(get_type(element), current_padding)

    # Handle the case when there are no public attributes
    if len(attributes) == 0:
        return add_padding(f"{get_type(element)}()", current_padding)

    content_text = "\n".join(attributes)
    return (
        add_padding(f"{get_type(element)}(", current_padding)
        + add_padding(
            content_text,
            current_padding + padding_increment * " ",
        )
        + add_padding(")", current_padding)
    )
