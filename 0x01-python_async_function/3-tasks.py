#!/usr/bin/env python3

"""
Module: task_wait_random

This module contains a function that creates an asyncio.Task for an
asynchronous routine.

The function task_wait_random takes an integer argument `max_delay` and
returns an asyncio.Task that runs the wait_random coroutine with the
specified `max_delay`.

Functions:
    - task_wait_random(max_delay: int = 10) -> asyncio.Task: Creates and
    returns an asyncio.Task for the wait_random coroutine.
"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Create and return an asyncio.Task for the wait_random coroutine with the
    specified max_delay./

    Parameters:
    max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
    asyncio.Task: An asyncio.Task object running the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
