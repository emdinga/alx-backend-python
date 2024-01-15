#!/usr/bin/env python3
"""concurrent coroutines module"""


import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns wait random n 
    times with the specified max_delay."""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
