#!/usr/bin/env python3
"""
Module for converting a floating-point number to a string.

This module provides a function to cast a floating-point number into a string.
"""


def to_str(n: float) -> str:
    """
    Converts a floating-point number to a string.

    Parameters:
    n (float): The floating-point number to convert.

    Returns:
    str: The string representation of the floating-point number.

    Example Usage:
    --------------
    >>> to_str(3.14)
    '3.14'

    >>> to_str(-0.001)
    '-0.001'

    >>> to_str(0.0)
    '0.0'
    """
    return str(n)
