from collections import deque

import numpy as np
from tqdm.notebook import tqdm


def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def solve(thearr, extra_obstacle=None):
    moves = deque([(-1, 0), (0, 1), (1, 0), (0, -1)])
    max_y, max_x = thearr.shape

    travelled = set()

    ys, xs = np.where(thearr == '#')
    start = np.where(thearr == '^')
    start_coord = start[0][0].item(), start[1][0].item()
    obstacles = list(zip(ys.tolist(), xs.tolist()))
    obstacles = set(obstacles)
    if extra_obstacle:
        obstacles.add(extra_obstacle)
    current_space = start_coord
    new_space = current_space
    travelled.add(start_coord)
    max_iteration = 1e5
    i = 0
    while (0 <= new_space[0] < max_y) and (0 <= new_space[1] < max_x):
        i += 1
        if i > max_iteration:
            return 'loop', 'loop'
        movement = moves[0]
        new_space = add_tuples(current_space, movement)
        if new_space not in obstacles:
            travelled.add(new_space)
            #  print(f"moving to {new_space}")
            current_space = new_space
        else:
            moves.rotate(-1)
        # print('rotating')
    return len(travelled) - 1, i


def part2(arr):
    bad_count = 0
    max_y, max_x = arr.shape
    for x in tqdm(range(max_x)):
        for y in range(max_y):
            out = solve(arr, extra_obstacle=(y, x))
            if out[0] == 'loop':
                #   print('loop found')
                bad_count += 1
    return bad_count
