#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
