"""Utils."""

from typing import Any


def add_padding(text: str, current_padding: str) -> str:
    """Add padding and merge."""
    return (
        "\n".join(
            list(
                map(
                    lambda x: current_padding + x.strip("\n"),
                    text.strip("\n").split("\n"),
                )
            )
        )
        + "\n"
    )


def get_type(ele: Any) -> str:
    """Get the type of an element."""
    return str(type(ele)).split("'")[1]
