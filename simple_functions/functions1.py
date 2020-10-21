
from functools import lru_cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


# Cache that holds dictionary of previosuly computed factorials
# utilises result to avoid new redundant computations
@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1
