"""Utils."""

import inspect
import re
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
    try:
        return str(type(ele)).split("'")[1]
    except IndexError:
        return str(type(ele))


def display_caller(func_name: str = "shortprint"):
    """Display the caller."""
    frames = inspect.getouterframes(inspect.currentframe(), 2)
    if frames is None:
        return
    cal_frame = frames[-1]

    # Search the variable name
    var_name = "Unknown Variable"
    if cal_frame.code_context is not None:
        var_name = cal_frame.code_context[-1].strip("\n ")
        search = re.search(
            func_name + r"\((.+)\)", cal_frame.code_context[-1].strip("\n ")
        )
        if search is not None:
            var_name = str(search.group(1))

    # Generate the message
    msg = (
        f"{'='*5} Shortprinting {'='*5}\n"
        "Shortprinting the variable located at the following location:\n"
        f"File: {cal_frame.filename}, at line {cal_frame.lineno}\n"
        f"Variable Name: '{var_name}'\n"
        f'{"=" * 25}'
    )
    print(msg)
