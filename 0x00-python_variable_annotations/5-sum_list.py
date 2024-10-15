#!/usr/bin/env python3
"""A type-annotated function that sums a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the input_list.
    """
    return sum(input_list)
