#!/usr/bin/env python3
"""
Module for summing elements of a list containing both integers and floats.

This module provides a function to take a list of mixed integers and
floating-point numbers as input and return their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of all elements in the mixed list.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing both integers and
    floating-point numbers to be summed.

    Returns:
    float: The sum of all the integers and floating-point numbers in the
    input list.

    Example Usage:
    --------------
    >>> sum_mixed_list([1, 2.5, 3, 4.0])
    10.5

    >>> sum_mixed_list([0, -1.5, 2, 3.5])
    4.0

    >>> sum_mixed_list([7, 8.5, -3])
    12.5
    """
    return sum(mxd_lst)
