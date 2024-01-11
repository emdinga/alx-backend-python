#!/usr/bin/env python3
"""100-safe_first_element module"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the sequence 
    if it exists, otherwise returns None."""
    if lst:
        return lst[0]
    else:
        return None
