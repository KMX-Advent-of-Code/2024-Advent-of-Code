from collections import defaultdict

from aoc_helper import get_input

input1, input2 = get_input()


def make_rules(test):
    data = [[int(y) for y in x.split('|')] for x in test.split('\n')]
    lt_dict = defaultdict(list)
    for x, y in data:
        lt_dict[x].append(y)
    return lt_dict


rules, bigs = input1.split('\n\n')
lt_dict = make_rules(rules)


class Page:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f'Page {self.n}'

    def __lt__(self, other):
        if other.n in lt_dict[self.n]:
            return True
        return False


def make_lists(s):
    return [[Page(int(y)) for y in x.split(',')] for x in s.split('\n')]


def part1(s):
    mylists = make_lists(s)
    out = []
    for thelist in mylists:
        if thelist == sorted(thelist):
            middleIndex = (len(thelist) - 1) // 2
            out.append(thelist[middleIndex].n)
    return sum(out)


def part2(s):
    mylists = make_lists(s)
    print(len(mylists))
    out = []
    for thelist in mylists:
        if thelist != sorted(thelist):
            thelist.sort()
            middleIndex = (len(thelist) - 1) // 2
            out.append(thelist[middleIndex].n)
    return sum(out)
