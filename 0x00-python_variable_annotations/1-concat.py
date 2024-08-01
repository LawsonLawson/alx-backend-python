#!/usr/bin/env python3
"""
Module for concatenating two strings.

This module provides a function to concatenate two strings and return
the result.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Parameters:
    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.

    Returns:
    str: The concatenation of the two input strings.

    Example Usage:
    --------------
    >>> concat("Hello, ", "world!")
    'Hello, world!'

    >>> concat("foo", "bar")
    'foobar'
    """
    return str1 + str2
