"""Dict typer."""
# pylint: disable=R0914

from collections import defaultdict
from typing import Any, Callable, Dict, List, Tuple

from shortprint.utils import add_padding, get_type


def type_dict(
    *,
    element: Dict[Any, Any],
    recursive_func: Callable,
    current_padding: str,
    padding_increment: int,
    is_depth_reached: bool = False,
) -> str:
    """Type for a dict."""
    entity_name = "Dict"
    if isinstance(element, defaultdict):
        entity_name = "DefaultDict"

    # Empty dict
    if len(element) == 0:
        return add_padding(f"{entity_name}[]", current_padding)

    if is_depth_reached:
        return add_padding("Dict[...]", current_padding)

    # If not, we count the number of elements that differ (in terms of type)
    element_types_dict: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)

    for ele, val in element.items():
        element_types_dict[get_type(ele), get_type(val)].append(
            {
                "key": ele,
                "value": val,
            }
        )

    # sort by number of elements, key_type string and value_type string
    element_types_dict_sorted = sorted(
        element_types_dict.items(),
        key=lambda x: (len(x[1]), x[0][0], x[0][1]),
    )

    context_text = ""

    for _, value in element_types_dict_sorted:
        to_add = (
            f"({len(value)}) {recursive_func(value[0]['key'])[:-1]}"
            f": {recursive_func(value[0]['value'])[:-1]}\n"
        )
        context_text += to_add

    return (
        add_padding(f"{entity_name}[", current_padding)
        + add_padding(
            context_text,
            current_padding + padding_increment * " ",
        )
        + add_padding("]", current_padding)
    )
