import re
import numpy as np


def proc_machine(s, part2=False):
    out = [[int(x) for x in re.findall(r'\d+', x)] for x in s.split('\n')]
    offset = 0
    if part2:
        offset = 10000000000000
    a = np.array([[out[0][0], out[1][0]], [out[0][1], out[1][1]]])
    b = np.array([out[2][0] + offset, out[2][1] + offset])
    return np.linalg.solve(a, b)


def solve_one(s):
    out = proc_machine(s).tolist()
    assert len(out) == 2
    # print(out)
    if all(round(x, 4).is_integer() for x in out):
        a, b = out

        # print(a,int(a),b,int(b))
        return 3 * int(round(a, 4)) + int(round(b, 4))
    return 0


def solve(s):
    thelist = s.split('\n\n')
    ans = 0
    for one_list in thelist:
        ans += solve_one(one_list)
    return ans
