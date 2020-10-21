
from functools import lru_cache

__all__ = ['my_sum', 'factorial', 'sin']


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


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def sin(x):
    numerator = [x**n for n in range(1, 100, 2)]
    denominator = [factorial(n) for n in range(1, 100, 2)]
    signs = [(-1)**n for n in range(50)]
    sinx = [(sign*num)/den for num, den, sign in zip(numerator, denominator,
                                                     signs)]
    return my_sum(sinx)
