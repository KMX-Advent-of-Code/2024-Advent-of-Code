import numpy as np


def make_diag(arr, coords):
    for y, x in coords:
        if y < 0 or x < 0:
            return ''
    try:
        out = ''.join([arr[z[0], z[1]] for z in coords])
    except:
        out = ''
    return out


def find_xmas(arr, y, x):
    # across
    try:
        across = ''.join(arr[y, x : x + 4])
    except IndexError:
        across = ''
    try:
        down = ''.join(arr[y : y + 4, x])
    except IndexError:
        down = ''

    up = ''
    try:
        up = ''.join(arr[y : y - 4 : -1, x])
    except IndexError as e:
        up = ''

    backwards = ''
    try:
        backwards = ''.join(arr[y, x : x - 4 : -1])
    except IndexError:
        backwards = ''

    coords = [[y + i, x + i] for i in range(4)]
    down_right = make_diag(arr, coords)
    coords = [[y - i, x + i] for i in range(4)]
    up_right = make_diag(arr, coords)
    coords = [[y + i, x - i] for i in range(4)]
    down_left = make_diag(arr, coords)
    coords = [[y - i, x - i] for i in range(4)]
    up_left = make_diag(arr, coords)

    count = 0
    thelist = [across, backwards, up, down, down_right, up_right, down_left, up_left]
    for word in thelist:
        if word == 'XMAS':
            count += 1
    return count


def get_total(_arr):
    total = 0
    myarr = np.pad(_arr, (4, 4), constant_values='Z')

    sy, sx = myarr.shape
    for x in range(sx):
        for y in range(sy):
            total += find_xmas(myarr, y, x)
    return total


def find_x_mas(arr, y, x):
    # across
    if arr[y, x] != 'A':
        return False
    try:
        diag1 = [arr[y - 1, x - 1], arr[y, x], arr[y + 1, x + 1]]
        word1 = ''.join(diag1)
    except IndexError:
        word1 = ''
    try:
        diag2 = [arr[y + 1, x - 1], arr[y, x], arr[y - 1, x + 1]]
        word2 = ''.join(diag2)
    except IndexError:
        word2 = ''
    return all(x in ['SAM', 'MAS'] for x in [word1, word2])
