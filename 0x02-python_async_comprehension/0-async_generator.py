#!/usr/bin/env python3

"""
Module: async_generator

This module contains a coroutine that generates random numbers asynchronously.

The coroutine async_generator takes no arguments. It loops 10 times, each time
asynchronously waiting for 1 second before yielding a random number between 0
and 10.

Functions:
    - async_generator() -> Generator[float, None, None]: Asynchronously
    generates random numbers between 0 and 10.
"""

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generate a random number between 0 and 10 every second, for
    a total of 10 numbers.

    Yields:
    float: A random number between 0 and 10.
    """
    for i in range(10):
        await sleep(1)
        yield 10 * random()
