#!/usr/bin/env python3
""" Sum a list of mixed floats and integers """

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing mixed floats and integers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of mixed floats and int.

    Returns:
        float: The sum of the elements in the list.
    """
    return sum(mxd_lst)
