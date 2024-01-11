#!/usr/bin/env python3
"""101-safely_get_value module"""


from typing import Mapping, Any, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the value associated with the key in the mapping if it exists,
    otherwise returns the default value."""
    if key in dct:
        return dct[key]
    else:
        return default
