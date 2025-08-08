from functools import lru_cache

@lru_cache(maxsize=128)
def cached_fib(n: int) -> int:
    if n <= 1:
        return n
    return cached_fib(n - 1) + cached_fib(n - 2)