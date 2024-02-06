#!/usr/bin/env python3
""" Create a multiplier function """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Given a float multiplier, return a function that multiplies a float by the multiplier.

    Args:
        multiplier (float): The float multiplier.

    Returns:
        Callable[[float], float]: The function that multiplies a float by the multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
