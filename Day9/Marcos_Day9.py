from collections import deque


def make_deque(s):
    d = deque(list(s))
    out = deque()
    i = 0
    while d:
        file_size = d.popleft()
        for x in range(int(file_size)):
            out.append(i)
        i += 1
        if d:
            free_space = d.popleft()
        for x in range(int(free_space)):
            out.append('.')
    return out


def optimize_deque(s):
    last_block = s.pop()
    if last_block != '.':
        try:
            first_empty_index = s.index('.')
        except ValueError:
            s.append(last_block)
            return 0
        s[first_empty_index] = last_block
    return 1


def solve1(s):
    thedeque = make_deque(s)
    res = 1
    while res:
        res = optimize_deque(thedeque)
    result = 0
    for i, x in enumerate(thedeque):
        result += i * x
    return result


## part2


class FileBlock:
    def __init__(self, _id, size):
        self._id = _id
        self.size = size

    def __repr__(self):
        return f'File Id {self._id} Size: {self.size}'


class FreeSpace:
    _id = 0

    def __init__(self, size):
        self.size = size

    def shrink(self, n):
        self.size = self.size - n

    def __repr__(self):
        return f'Free Space {self.size}'

    def __eq__(self, other):
        """I define this such that .index in tnhe deque will find the first free space block equal to or bigger than the size I need"""
        return isinstance(other, FreeSpace) and (other.size <= self.size)


def make_deque2(s):
    d = deque(list(s))
    out = deque()
    i = 0
    while d:
        file_size = d.popleft()
        out.append(FileBlock(i, int(file_size)))
        i += 1
        if d:
            free_space = d.popleft()
            out.append(FreeSpace(int(free_space)))
    return out


def optimize_deque2(s, right_deque):
    if s:
        last_block = s.pop()
    else:
        return 0

    if isinstance(last_block, FileBlock):
        try:
            first_empty_index = s.index(FreeSpace(last_block.size))
            s[first_empty_index].shrink(last_block.size)
            s.insert(
                first_empty_index, last_block
            )  # i think insert is reasonably fast for deque but not sure about .index
            s.append(FreeSpace(last_block.size))
        except ValueError:
            right_deque.appendleft(last_block)
    else:
        right_deque.appendleft(last_block)


def solve2(s):
    thedeque = make_deque2(s)
    right_deque = deque()
    while thedeque:
        optimize_deque2(thedeque, right_deque)
    ans = 0
    i = 0
    for block in right_deque:
        for k in range(block.size):
            ans += i * block._id
            i += 1
    return ans
