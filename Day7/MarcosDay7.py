# part 1
import itertools
from tqdm.notebook import tqdm
import re

operators = [' * ', ' + ']


def process_ops(op, s):
    x = list(itertools.chain.from_iterable(itertools.zip_longest(s, op)))
    return x[0] + x[1] + add_parens(x[2:-1]), add_parens(x[2:-1])


def add_parens(_mylist):
    mylist = _mylist.copy()
    l = len(mylist)
    for i in range(2, l, 2):
        mylist[i] = mylist[i] + ')'
    return ''.join(['(' * (l // 2)] + mylist)


def make_equations(s, operators):
    ops = itertools.product(operators, repeat=len(s) - 2)
    ops = [(' == ',) + x for x in ops]
    out = [process_ops(op, s) for op in ops]
    return out


def solve(t):
    out = []
    strings = [re.findall(r'\d+', y) for y in t]
    for s in tqdm(strings):
        eq_strings = make_equations(s, operators=operators)
        # print(eq_strings)
        for eq in eq_strings:
            if eval(eq[0]):
                out.append(eval(eq[1]))
                break
    return sum(out)


operators_part2 = [' * ', ' + ', ' // ']


class MyInt:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __repr__(self):
        return f'MyInt({self.val})'

    def __add__(self, other):
        if isinstance(other, MyInt):
            return MyInt(self.val + other.val)
        elif isinstance(other, int):
            return self.val + other

    def __radd__(self, other):
        if isinstance(other, MyInt):
            return MyInt(self.val + other.val)
        elif isinstance(other, int):
            return self.val + other

    def __mul__(self, other):
        return MyInt(self.val * other.val)

    def __int__(self):
        return self.val

    def __floordiv__(self, other):
        return MyInt(int(str(self.val) + str(other.val)))


def solve_part2(t):
    count = 0
    strings = [re.findall(r'\d+', y) for y in t]
    strings = [[f'{MyInt(x)}' for x in s] for s in strings]
    for s in tqdm(strings):
        eq_strings = make_equations(s, operators_part2)
        # print(eq_strings)
        for eq in eq_strings:
            if eval(eq[0]):
                count += int(eval(eq[1]))
                break
    return count
