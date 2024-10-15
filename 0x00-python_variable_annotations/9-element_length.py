#!/usr/bin/env python3
from typing import List, Tuple, Sequence


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths.

    Args:
        lst (Sequence): A sequence (like a list or a string) of elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        where each tuple contains
        an element and its length.
    """
    return [(i, len(i)) for i in lst]
