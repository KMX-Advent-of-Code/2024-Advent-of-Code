"""Day 2"""


# pylint: disable=unused-import, invalid-name, redefined-outer-name

from abc import ABC, abstractmethod
from functools import lru_cache

import re
from collections import deque
import numpy as np
import pandas as pd

from utils.inputs import (
    get_input,
    split,
    split_newline,
    split_lax,
    list_map,
    list_reshape,
    get_int,
    get_float,
)

DAY = 2


def solution_part1(s: str):
    """Part 1 solution from the plaintext input"""
    p = list_map(get_int, list_map(split_lax, split_newline(s)), level=2)
    soln = sum(list_map(is_safe, p))
    return soln


def solution_part2(s: str):
    """Part 2 solution from the plaintext input"""
    p = list_map(get_int, list_map(split_lax, split_newline(s)), level=2)
    soln = sum(list_map(is_safe_dampened, p))
    return soln


def is_safe(row):
    diffs = np.diff(np.array(row))
    return (
        (all(diffs >= 0) or all(diffs <= 0))
        and all(abs(diffs) >= 1)
        and all(abs(diffs) <= 3)
    )


def is_safe_dampened(row):
    return any([is_safe(row[:i] + row[i + 1 :]) for i in range(len(row))])


if __name__ == "__main__":
    s = get_input(DAY)
    print()
    soln1 = solution_part1(s)
    print("Part 1 solution:")
    print(soln1)
    print()
    soln2 = solution_part2(s)
    print("Part 2 solution:")
    print(soln2)
    print()
    print("Done")