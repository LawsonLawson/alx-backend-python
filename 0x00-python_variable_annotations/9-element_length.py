#!/usr/bin/env python3
"""
Module for annotating and processing sequences.

This module provides a function that takes an iterable of sequences and returns
a list of tuples. Each tuple contains a sequence from the input and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains a sequence and its
    length.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences
    (e.g., strings, lists).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where:
        - The first element of each tuple is a sequence from the input
        iterable.
        - The second element of each tuple is the length of that sequence.

    Example Usage:
    --------------
    >>> element_length(["hello", "Lawson"])
    [("hello", 5), ("Lawson", 5)]

    >>> element_length([[1, 2], [3, 4, 5], [6]])
    [([1, 2], 2), ([3, 4, 5], 3), ([6], 1)]

    >>> element_length(("Israel", "Pascal", "Lawson"))
    [("Israel", 5), ("Pascal", 6), ("Lawson", 6)]
    """
    return [(i, len(i)) for i in lst]
