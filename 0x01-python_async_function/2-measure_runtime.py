#!/usr/bin/env python3

"""
Module: measure_time

This module contains a function to measure the average execution time of an
asynchronous routine.

The function measure_time takes two integer arguments, `n` and `max_delay`, and
measures the total execution time for wait_n(n, max_delay). It returns the
average time per task by dividing the total execution time by `n`.

Functions:
    - measure_time(n: int, max_delay: int) -> float: Measures the total
    execution time for wait_n(n, max_delay) and returns the average time per
    task.
"""


from time import time
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return the
    average time per task.

    Parameters:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum number of seconds to wait for each call to
    wait_random.

    Returns:
    float: The average execution time per task.
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
