#!/usr/bin/env python3

"""
Module: measure_runtime

This module contains a coroutine that measures the total runtime of executing
another coroutine multiple times in parallel.

The coroutine measure_runtime imports async_comprehension from a previous task
and executes it four times in parallel using asyncio.gather. It measures the
total runtime and returns it.

Functions:
    - measure_runtime() -> float: Measures the total runtime of
    executing async_comprehension four times in parallel.
"""

import asyncio
import time
from importlib import import_module as import_using


async_comprehension = import_using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times in
    parallel.

    Returns:
    float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
