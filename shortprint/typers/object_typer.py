"""Object Typer."""

from typing import Any, Callable

from shortprint.utils import add_padding, get_type


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

    if is_depth_reached:
        return add_padding(f"{element.__class__.__name__}()", current_padding)

    if not hasattr(element, "__dict__"):
        return add_padding(get_type(element), current_padding)

    attributes = list(
        sorted(
            [
                f"{key}: {recursive_func(value)[:-1]}"
                for key, value in element.__dict__.items()
                if not (key.startswith("_") and only_show_public_attributes)
                and not (get_type(value) == "function" and only_show_attributes)
            ]
        )
    )

    # Handle the case when there are no public attributes
    if len(attributes) == 0:
        return add_padding(f"{element.__class__.__name__}()", current_padding)

    content_text = "\n".join(attributes)
    return (
        add_padding(f"{element.__class__.__name__}(", current_padding)
        + add_padding(
            content_text,
            current_padding + padding_increment * " ",
        )
        + add_padding(")", current_padding)
    )
