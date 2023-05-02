#!/usr/bin/env python3
""" Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n, return a float."""

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of a function
    Args:
        n: the number of coroutines to launch
        max_delay: the maximum amount of time to wait for each coroutine
    Returns: elapsed time in seconds
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start_time
    return total_time / n
