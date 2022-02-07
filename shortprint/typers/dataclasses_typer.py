"""Dataclass typer."""

from typing import Any, Callable

from shortprint.utils import add_padding


def type_dataclass(
    *,
    element: Any,
    recursive_func: Callable,
    current_padding: str,
    padding_increment: int,
    is_depth_reached: bool = False,
) -> str:
    """Type for a dataclass."""

    if is_depth_reached:
        return add_padding(f"{element.__class__.__name__}(...)", current_padding)

    content_text = "\n".join(
        list(
            sorted(
                [
                    f"{attribute}: {recursive_func(getattr(element, attribute))[:-1]}"
                    for attribute in element.__dataclass_fields__.keys()
                ]
            )
        )
    )
    return (
        add_padding(f"{element.__class__.__name__}(", current_padding)
        + add_padding(
            content_text,
            current_padding + padding_increment * " ",
        )
        + add_padding(")", current_padding)
    )
