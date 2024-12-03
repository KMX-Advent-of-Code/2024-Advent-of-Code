from aoc_helper import get_input

input1, input2 = get_input()

import re


def mul(a, b):
    return a * b


res = 0
for s in re.findall(r'mul\(\d+,\d+\)', input1):
    res += eval(s)

# part 1
print(res)

res = 0
active = 1
for s in re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', input1):
    if s == "don't()":
        active = 0
        continue
    elif s == 'do()':
        active = 1
        continue
    if active:
        res += eval(s)
