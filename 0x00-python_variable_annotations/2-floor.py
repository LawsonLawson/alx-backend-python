#!/usr/bin/env python3
"""
Module for calculating the floor of a floating-point number.

This module provides a function that takes a float as an argument and
returns the floor of the float.
"""


def floor(n: float) -> int:
    """
    Returns the largest integer value less than or equal to n.

    Parameters:
    n (float): The floating-point number to floor.

    Returns:
    int: The largest integer value less than or equal to n.

    Example Usage:
    --------------
    >>> floor(3.7)
    3

    >>> floor(-2.3)
    -3

    >>> floor(0.0)
    0
    """
    return int(n)
