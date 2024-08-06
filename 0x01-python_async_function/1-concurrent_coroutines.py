#!/usr/bin/env python3

"""
Module: wait_n

This module contains an asynchronous coroutine function that spawns multiple
tasks and returns the list of delays.

The function wait_n imports the wait_random function from a previous script. It
defines an async routine wait_n that takes two integer arguments, `n` and
`max_delay`. The function spawns wait_random `n` times with the specified
`max_delay`. The wait_n function returns a list of all the delays
(float values) in ascending order without using the sort() method.

Functions:
    - wait_n(n: int, max_delay: int = 10) -> List[float]: Spawns wait_random
      n times with the specified max_delay and returns the list of delays in
      ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list
    of delays in ascending order.

    Parameters:
    n (int): The number of times to spawn wait_random.
    max_delay (int): The maximum number of seconds to wait for each call to
    wait_random. Default is 10.

    Returns:
    List[float]: A list of delays in ascending order.
    """
    spawn_ls = []
    delay_ls = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(delayed_task)

    for spawn in spawn_ls:
        await spawn

    return delay_ls
