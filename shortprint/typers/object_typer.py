"""Object Typer."""

from typing import Any, Callable

from shortprint.utils import add_padding


def type_object(
    *,
    element: Any,
    recursive_func: Callable,
    current_padding: str,
    padding_increment: int,
) -> str:
    """Type for a list."""

    print(element)
    print(element.__dict__)
    content_text = "\n".join(
        list(
            sorted(
                [
                    f"{key}: {recursive_func(value)[:-1]}"
                    for key, value in element.__dict__.items()
                ]
            )
        )
    )

    content_text = ""
    return (
        add_padding(f"{element.__class__.__name__}(", current_padding)
        + add_padding(
            content_text,
            current_padding + padding_increment * " ",
        )
        + add_padding(")", current_padding)
    )
