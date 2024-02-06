#!/usr/bin/env python3
""" Convert a string and an int OR float to a tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Given a string k and an int OR float v, return a tuple.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int OR float value.

    Returns:
        Tuple[str, float]: The tuple containing k and v*v.
    """
    return (k, v*v)
