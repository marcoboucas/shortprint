"""Init typers."""

from .dataclasses_typer import type_dataclass
from .dict_typer import type_dict
from .list_typer import type_list
from .object_typer import type_object
from .set_typer import type_set
from .tuple_typer import type_tuple

try:
    from .ndarray_typer import type_ndarray
except ModuleNotFoundError:
    pass

__all__ = [
    "type_list",
    "type_dataclass",
    "type_dict",
    "type_ndarray",
    "type_tuple",
    "type_set",
    "type_object",
    "type_ndarray",
]
