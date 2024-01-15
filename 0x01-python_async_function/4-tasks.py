#!/usr/bin/env python3
"""tasks module"""


import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns task_wait_random
    n times with the specified max_delay."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
