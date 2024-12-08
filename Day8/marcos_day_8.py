import re
import numpy as np
from collections import Counter
import itertools
from fractions import Fraction


def string_to_lists(s):
    return [list(x) for x in s.split('\n')]


def get_antenna(x):
    return [x for x in list(Counter(x).keys()) if re.match(r'\d|[a-zA-Z]', x)]


def undumb(l):
    return [tuple([int(y) for y in x]) for x in l]


def get_coords(theinput):
    ant_list = get_antenna(theinput)
    arr = np.array(string_to_lists(theinput))

    return [undumb(zip(*np.where(arr == ant))) for ant in ant_list], arr.shape


def find_antinodes(coord1, coord2):
    y_dist = coord1[0] - coord2[0]
    x_dist = coord1[1] - coord2[1]
    # return y_dist,x_dist
    return [(coord1[0] + y_dist, coord1[1] + x_dist), (coord2[0] - y_dist, coord2[1] - x_dist)]


def check_coords(coord_pair, theshape):
    y, x = coord_pair
    max_y, max_x = theshape
    return (0 <= y < max_y) and (0 <= x < max_x)


def find_all_antinodes(coord_list):
    out = []
    for coord1, coord2 in itertools.permutations(coord_list, 2):
        out.extend(find_antinodes(coord1, coord2))
    return out


def solve(theinput):
    coord_list, theshape = get_coords(theinput)
    print(theshape)
    out = []
    for thelist in coord_list:
        out.extend(find_all_antinodes(thelist))
    answer_set = set([x for x in out if check_coords(x, theshape)])
    return len(answer_set), answer_set


def find_antinodes2(coord1, coord2):
    y_dist = coord1[0] - coord2[0]
    x_dist = coord1[1] - coord2[1]
    f = Fraction(
        y_dist, x_dist
    )  # apparentyl it worsk without this. I thought i needed to this if the antenna distance was some reducabel fraciton like 3,9
    y_dist, x_dist = f.numerator, f.denominator
    return [(coord1[0] + i * y_dist, coord1[1] + i * x_dist) for i in range(-50, 50)]


def find_all_antinodes2(coord_list):
    out = []
    for coord1, coord2 in itertools.permutations(coord_list, 2):
        out.extend(find_antinodes2(coord1, coord2))
    return out


def solve2(theinput):
    coord_list, theshape = get_coords(theinput)
    print(theshape)
    out = []
    for thelist in coord_list:
        out.extend(find_all_antinodes2(thelist))
    answer_set = set([x for x in out if check_coords(x, theshape)])
    return len(answer_set), answer_set
