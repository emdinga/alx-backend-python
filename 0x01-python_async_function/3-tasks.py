#!/usr/bin/env python3
"""tasks module"""


import asyncio
from typing import Callable


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task that runs the wait_random
    coroutine with the specified max_delay."""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
