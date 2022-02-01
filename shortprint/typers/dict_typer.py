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
) -> str:
    """Type for a dict."""
    entity_name = "Dict"
    if isinstance(element, defaultdict):
        entity_name = "DefaultDict"

    # Empty dict
    if len(element) == 0:
        return add_padding(f"{entity_name}[]", current_padding)

    # If not, we count the number of elements that differ (in terms of type)
    element_types_dict: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)

    for ele, val in element.items():
        element_types_dict[get_type(ele), get_type(val)].append(
            {
                "key_type": recursive_func(ele),
                "value_type": recursive_func(val),
            }
        )

    # sort by number of elements, key_type string and value_type string
    element_types_dict_sorted = sorted(
        element_types_dict.values(),
        key=lambda x: (len(x), x[0]["key_type"], x[0]["value_type"]),
    )

    context_text = ""

    for flatten_ele in element_types_dict_sorted:
        to_add = (
            f"({len(flatten_ele)}) {flatten_ele[0]['key_type'][:-1]}"
            f": {flatten_ele[0]['value_type'][:-1]}\n"
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
