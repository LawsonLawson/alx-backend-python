#!/usr/bin/env python3
"""
Module for creating a tuple with a string and the square of a number.

This module provides a function to take a string and a number
(integer or float) as input and returns a tuple where the first element is the
string and the second element is the square of the number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple consisting of a string and the square of a number.

    Parameters:
    k (str): A string to be included as the first element of the tuple.
    v (Union[int, float]): A number (either integer or floating-point) whose
    square will be the second element of the tuple.

    Returns:
    Tuple[str, float]: A tuple where:
        - The first element is the string `k`.
        - The second element is the square of the number `v`, annotated as a
        float.

    Example Usage:
    --------------
    >>> to_kv("hello", 3)
    ('hello', 9.0)

    >>> to_kv("pi", 3.14)
    ('pi', 9.8596)

    >>> to_kv("number", -4)
    ('number', 16.0)
    """
    return k, v * v
