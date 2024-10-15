#!/usr/bin/env python3
"""A type-annotated function that returns the floor of a float."""

import math


def floor(n: float) -> int:
    """
    Function that returns the floor of a given float.

    Args:
        n (float): The float number to be floored.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
