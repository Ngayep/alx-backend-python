#!/usr/bin/env python3
"""A type-annotated function that sums a mixed list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list containing integers and floats.

    Returns:
        float: The sum of the numbers in the mxd_lst.
    """
    return float(sum(mxd_lst))
