"""Set typer."""

from collections import defaultdict
from typing import Callable, FrozenSet, Set, Union

from shortprint.utils import add_padding, get_type


def type_set(
    *,
    element: Union[Set, FrozenSet],
    recursive_func: Callable,
    current_padding: str,
    padding_increment: int,
    is_depth_reached: bool = False,
) -> str:
    """Type for a set."""

    # Empty set
    if len(element) == 0:
        return add_padding("Set{}", current_padding)

    if is_depth_reached:
        return add_padding("Set{...}", current_padding)

    # If not, we count the number of elements that differ (in terms of type)
    counter = defaultdict(list)
    for ele in element:
        counter[get_type(ele)].append(ele)
    # Sort by type value (to get unique order)
    counter_values = list(
        map(lambda x: x[1], sorted(list(counter.items()), key=lambda x: x[0]))
    )
    content_text = "\n".join(
        [f"({len(sons)}) {recursive_func(sons[0])[:-1]}" for sons in counter_values]
    )
    return (
        add_padding("Set{", current_padding)
        + add_padding(
            content_text,
            current_padding + padding_increment * " ",
        )
        + add_padding("}", current_padding)
    )
