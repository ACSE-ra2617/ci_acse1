# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:23:15 2020

@author: raula
"""

from numpy import sqrt
from simple_functions.functions1 import factorial
from functools import lru_cache

__all__ = ['pi']


def pi(terms=1):
    return 1./(2.*sqrt(2.)/9801.*rsum(terms))


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def rsum(n):
    t = factorial(4*n)*(1103+26390*n)/(factorial(n)**4*396**(4*n))
    return t + rsum(n-1) if n else t
