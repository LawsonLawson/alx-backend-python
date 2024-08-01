#!/usr/bin/env python3
"""
Module for safely accessing the first element of a sequence.

This module provides a function to safely retrieve the first element of a
sequence. If the sequence is empty, it returns `None`.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it exists, otherwise returns
    None.

    Parameters:
    lst (Sequence[Any]): A sequence of elements where the type of elements is
    not known.

    Returns:
    Union[Any, None]: The first element of the sequence if it is not empty,
    otherwise None.

    Example Usage:
    --------------
    >>> safe_first_element([1, 2, 3])
    1

    >>> safe_first_element(["lawson", "israel", "pascal"])
    'lawson'

    >>> safe_first_element([])
    None
    """
    if lst:
        return lst[0]
    else:
        return None
