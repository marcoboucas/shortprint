"""Object Typer."""


from typing import Any, Callable, List

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
    attributes: List[str]

    if is_depth_reached:  # Max depth
        return add_padding(f"{element.__class__.__name__}()", current_padding)

    if hasattr(element, "__dict__"):
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
    else:
        # We try to use dir instead
        print("HAS NO DICT", element, dir(element))

        attributes = list(
            sorted(
                [
                    f"{key}: {recursive_func(getattr(element,key))[:-1]}"
                    for key in dir(element)
                    if not (key.startswith("_") and only_show_public_attributes)
                    and not (
                        get_type(getattr(element, key)) == "function"
                        and only_show_attributes
                    )
                ]
            )
        )

        if len(attributes) == 0:  # Standard for basic types (str, ...)
            return add_padding(get_type(element), current_padding)

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
