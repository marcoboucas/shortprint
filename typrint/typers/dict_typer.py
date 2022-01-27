"""List typer."""

from collections import defaultdict
from email.policy import default
from typing import Any, Callable, Dict, List
from typrint.utils import add_padding, get_type


def type_dict(
    *,
    element: Dict[Any, Any],
    recursive_func: Callable,
    current_padding: str,
    padding_increment: int,
) -> str:
    """Type for a dict."""

    # Empty dict
    if len(element) == 0:
        return add_padding("Dict[]", current_padding)

    # If not, we count the number of elements that differ (in terms of type)
    element_types_dict: Dict[str, Dict[str, List[Dict[str, str]]]] = defaultdict(
        lambda: defaultdict(list)
    )

    for ele, val in element.items():
        ele_type = get_type(ele)
        val_type = get_type(val)
        element_types_dict[ele_type][val_type].append(
            {
                "key_type": recursive_func(ele),
                "value_type": recursive_func(val),
            }
        )

    element_types_items = element_types_dict.items()

    flatten_dict = []
    for ele_type, value in element_types_items:
        for value_type in value:
            flatten_dict.append(element_types_dict[ele_type][value_type])

    flatten_dict = sorted(
        flatten_dict, key=lambda x: (len(x), x[0]["key_type"], x[0]["value_type"])
    )

    context_text = ""

    for flatten_ele in flatten_dict:
        context_text += f"({len(flatten_ele)}) {flatten_ele[0]['key_type'][:-1]}: {flatten_ele[0]['value_type'][:-1]}\n"

    return (
        add_padding("Dict[", current_padding)
        + add_padding(
            context_text,
            current_padding + padding_increment * " ",
        )
        + add_padding("]", current_padding)
    )
