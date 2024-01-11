#!/usr/bin/env python3
""" takes a float and returns a function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as an argument and returns a function
       that multiplies a float by multiplier."""
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
