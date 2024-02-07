#!/usr/bin/env python3
""" Safely Get Value """

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on an array by repeating each element a
    certain number of times.

    Args:
        lst (Tuple): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed-in array.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
