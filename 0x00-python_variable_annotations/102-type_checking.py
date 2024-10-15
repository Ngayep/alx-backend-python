#!/usr/bin/env python3
from typing import List, Tuple
"""Zoom in on the given array by a specified factor"""


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """Zoom in on the given array by a specified factor.

    Args:
        lst (List[int]): The input array to zoom.
        factor (int): The zoom factor. Default is 2.

    Returns:
        List[int]: The zoomed-in array.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

# Change the factor to an integer
zoom_3x = zoom_array(array, 3)  # Use an integer for the factor
