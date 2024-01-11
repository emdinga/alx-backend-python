#!/usr/bin/env python3
"""102-type_checking module"""

from typing import List, Tuple

def zoom_array(lst: List, factor: int = 2) -> Tuple:
    """Zooms in the elements of the list by repeating
    them according to the given factor."""
    zoomed_in: Tuple = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in
