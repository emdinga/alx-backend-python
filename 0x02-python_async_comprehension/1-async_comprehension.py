#!/usr/bin/env python3
"""coroutine will collect 10 random numbers using an async comprehensing"""



from typing import List
import asyncio
from random import uniform


async def async_generator() -> float:
    """coroutine will collect 10 random numbers using an async comprehensing"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]
