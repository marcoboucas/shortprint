"""TypePrint."""

from collections import defaultdict
from typing import Any

PADDING = 2


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


def typeprint_str(
    element: Any, current_padding: str = "", padding_increment: int = PADDING
) -> str:
    """Typeprint an element to string."""
    type_ = get_type(element)
    if isinstance(element, (str, int, float)):
        return add_padding(type_, current_padding)
    if isinstance(element, list):

        # Empty list
        if len(element) == 0:
            return add_padding("List[]", current_padding)

        # If not, we count the number of elements that differ (in terms of type)
        counter = defaultdict(list)
        for ele in element:
            counter[get_type(ele)].append(ele)
        # Sort by type value (to get unique order)
        counter_values = list(
            map(lambda x: x[1], sorted(list(counter.items()), key=lambda x: x[0]))
        )
        content_text = "\n".join(
            [f"({len(sons)}){typeprint_str(sons[0])[:-1]}" for sons in counter_values]
        )
        return (
            add_padding("List[", current_padding)
            + add_padding(
                content_text,
                current_padding + padding_increment * " ",
            )
            + add_padding("]", current_padding)
        )
    return "Unknown Type"


def typeprint(*args, **kwargs) -> None:
    """Typeprint an element."""
    print("\n".join(typeprint_str(*args, **kwargs)))
