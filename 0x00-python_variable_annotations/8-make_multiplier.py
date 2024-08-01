#!/usr/bin/env python3
"""
Module for creating a multiplier function.

This module provides a function to take a floating-point multiplier as input
and return a new function that multiplies any given float by this multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float as input and
    returns the product of that float and the multiplier.

    Example Usage:
    --------------
    >>> multiply_by_2 = make_multiplier(2.0)
    >>> multiply_by_2(5.0)
    10.0

    >>> multiply_by_0.5 = make_multiplier(0.5)
    >>> multiply_by_0.5(10.0)
    5.0

    >>> multiply_by_neg3 = make_multiplier(-3.0)
    >>> multiply_by_neg3(4.0)
    -12.0
    """
    return lambda x: x * multiplier
