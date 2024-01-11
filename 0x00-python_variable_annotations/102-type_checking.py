#!/usr/bin/env python3
"""102-type_checking module"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> list:
    """Zooms in the elements of the tuple by 
    repeating them according to the given factor."""
    zoomed_in: list = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
