# Decorator that caches function's return values. All function's arguments must be hashable.

from functools import cache

@cache
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)
# Potential problem with cache is that it can grow indefinitely. To clear stored values run '<func>.cache_clear()', 
# or use '@lru_cache(maxsize=<int>)' decorator instead.
# CPython interpreter limits recursion depth to 3000 by default. To increase it run 'sys.setrecursionlimit(<int>)'.