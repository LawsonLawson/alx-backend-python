#!/usr/bin/env python3

"""
Module: async_comprehension

This module contains a coroutine that collects random numbers generated
asynchronously.

The coroutine async_comprehension imports async_generator from a previous task
and uses it to collect 10 random numbers using an asynchronous comprehension,
then returns these 10 random numbers.

Functions:
    - async_comprehension() -> List[float]: Collects 10 random numbers
    from async_generator and returns them as a list.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator using asynchronous
    comprehension and return them as a list.

    Returns:
    List[float]: A list of 10 random numbers.
    """
    return [value async for value in async_generator()]
