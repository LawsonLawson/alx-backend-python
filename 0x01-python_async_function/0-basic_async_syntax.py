#!/usr/bin/env python3

"""
Module: wait_random

This module contains an asynchronous coroutine function that waits for a random
delay and returns the actual delay.

The function wait_random takes an integer argument `max_delay` with a default
value of 10. It waits for a random amount of time between 0 and `max_delay`
seconds and then returns the duration of the delay.

Functions:
    - wait_random(max_delay: int = 10) -> float: Waits for a random delay
    between 0 and max_delay seconds and returns the actual delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return the
    actual delay.

    Parameters:
    max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
    float: The actual number of seconds waited.
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
