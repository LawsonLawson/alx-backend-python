#!/usr/bin/env python3
"""
Module for summing elements of a list of floats.

This module provides a function to take a list of floating-point numbers as
input and return their sum.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all elements in the input list.

    Parameters:
    input_list (List[float]): A list of floating-point numbers to be summed.

    Returns:
    float: The sum of all the floating-point numbers in the input list.

    Example Usage:
    --------------
    >>> sum_list([1.1, 2.2, 3.3])
    6.6

    >>> sum_list([-1.0, 0.5, 2.5])
    2.0

    >>> sum_list([0.0, 0.0, 0.0])
    0.0
    """
    return sum(input_list)
