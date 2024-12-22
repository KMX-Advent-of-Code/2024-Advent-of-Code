import math
import numpy as np
from tqdm.autonotebook import tqdm
from collections import defaultdict, deque


def prune(x):
    return x % 16777216


def mix(secret, other):
    return secret ^ other


def sequence(secret):
    step1 = secret * 64
    step1 = prune(mix(step1, secret))
    step2 = math.floor(step1 / 32)
    step2 = prune(mix(step2, step1))
    return prune(mix(step2, step2 * 2048))


def more_sequences(seed, n):
    new_num = seed
    for n in range(n):
        new_num = sequence(new_num)
    return new_num


myints = [int(x) for x in input2]
# part 1
sum([more_sequences(x, 2000) for x in myints])


def last_digit(x):
    return x % 10  # less dumb


def solve_part2(ints):
    bananas = defaultdict(int)

    def more_sequences2(seed, n):
        out = [last_digit(seed)]
        new_num = seed
        used_tuples = set()
        old_digit = last_digit(seed)
        changes = deque(maxlen=4)
        for n in range(n):
            new_num = sequence(new_num)
            new_last_digit = last_digit(new_num)
            delta = new_last_digit - old_digit
            # keep a running list of the last 4 deltas using a deque with maxlen = 4
            changes.append(delta)
            out.append(new_last_digit)
            old_digit = new_last_digit
            tchange = tuple(changes)

            if tchange not in used_tuples:
                bananas[tchange] += new_last_digit
                used_tuples.add(tchange)

    for x in tqdm(ints):
        _ = more_sequences2(x, 2000)
    return max(bananas.values())


solve_part2(myints)
