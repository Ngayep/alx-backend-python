#!/usr/bin/env python3
"""A type-annotated function that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns its product with multiplier.
    """

    def multiply(n: float) -> float:
        """Multiply the input float by the multiplier."""
        return n * multiplier

    return multiply
