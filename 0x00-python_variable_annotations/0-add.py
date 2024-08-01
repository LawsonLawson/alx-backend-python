#!/usr/bin/env python3
"""
Module for adding two floating-point numbers.

This module provides a function to add two floating-point numbers and return
the result.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers.

    Parameters:
    a (float): The first floating-point number to add.
    b (float): The second floating-point number to add.

    Returns:
    float: The sum of the two floating-point numbers.

    Example Usage:
    --------------
    >>> add(1.5, 2.5)
    4.0

    >>> add(-1.0, 3.0)
    2.0
    """
    return a + b
