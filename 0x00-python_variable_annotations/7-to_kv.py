#!/usr/bin/env python3
"""A type-annotated function that converts a string
   and a number into a tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is k and
       the second element is the square of v.

    Args:
        k (str): The string key.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return (k, float(v ** 2))
