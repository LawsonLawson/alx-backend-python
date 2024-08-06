#!/usr/bin/env python3

"""
Module: task_wait_n

This module contains a function that spawns multiple asyncio.Tasks and returns
a list of delays.

The function task_wait_n is similar to wait_n but uses task_wait_random to
create the asyncio.Tasks. It takes two integer arguments, `n` and `max_delay`,
and returns a list of all the delays (float values) in ascending order.

Functions:
    - task_wait_n(n: int, max_delay: int = 10) -> List[float]: Spawns
      task_wait_random n times with the specified max_delay and returns the
      list of delays in ascending order.
"""


from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and return the
    list of delays in ascending order.

    Parameters:
    n (int): The number of times to spawn task_wait_random.
    max_delay (int): The maximum number of seconds to wait for each call to
    task_wait_random. Default is 10.

    Returns:
    List[float]: A list of delays in ascending order.
    """
    spawn_ls = []
    delay_ls = []
    for i in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(delayed_task)

    for spawn in spawn_ls:
        await spawn

    return delay_ls
