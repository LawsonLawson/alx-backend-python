#!/usr/bin/env python3
"""
Module for zooming in on an array by repeating its elements.
This module contains a function that takes a tuple of items and returns a list
where each item is repeated a specified number of times. The default repetition
factor is 2.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on a tuple by repeating each element `factor` times.
    Parameters:
    lst (Tuple[int, ...]): A tuple containing elements to be repeated.
    factor (int, optional): The number of times each element should be
    repeated. Defaults to 2.
    Returns:
    List[int]: A list where each element from the tuple is repeated `factor`
    times.
    """
    zoomed_in: List = [item for item in lst for _ in range(factor)]
    return zoomed_in


# Example usage
array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
