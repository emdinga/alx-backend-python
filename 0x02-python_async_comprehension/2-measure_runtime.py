#!/usr/bin/env python3
""" """


from typing import List
import asyncio
from random import uniform

async def async_generator() -> float:
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]

async def measure_runtime() -> float:
    start_time = asyncio.get_event_loop().time()

    # Run async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime

