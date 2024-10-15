#!/usr/bin/env python3
from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """Return a list of tuples containing elements and their lengths.

    Args:
        lst (List[Any]): A list of elements (can be of any type).

    Returns:
        List[Tuple[Any, int]]: A list of tuples, where each tuple contains
        an element and its length (if applicable).
    """
    return [(i, len(i)) for i in lst if isinstance(i, (str, bytes))]
