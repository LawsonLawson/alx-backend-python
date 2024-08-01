#!/usr/bin/env python3
"""
Module for safely retrieving a value from a mapping.

This module provides a function to safely get a value from a dictionary.
If the key does not exist in the dictionary, it returns a default value.
"""

from typing import Mapping, Any, Union, TypeVar

# Define a type variable for the default value
T = TypeVar('T')


def safely_get_value(dict: Mapping[Any, Any], key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a mapping if the key exists, otherwise
    returns the default value.

    Parameters:
    dct (Mapping[Any, Any]): The mapping (e.g., dictionary) from which to
    retrieve the value.
    key (Any): The key whose associated value is to be retrieved.
    default (Union[T, None], optional): The value to return if the key is not
    found in the mapping. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key if it exists in the
    mapping, otherwise the default value.

    Example Usage:
    --------------
    >>> safely_get_value({'a': 1, 'b': 2}, 'a')
    1

    >>> safely_get_value({'a': 1, 'b': 2}, 'c', default='not found')
    'not found'

    >>> safely_get_value({'a': 1, 'b': 2}, 'c')
    None
    """
    if key in dct:
        return dct[key]
    else:
        return default
