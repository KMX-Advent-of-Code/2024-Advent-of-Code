    from collections import defaultdict
    from functools import cache


    @cache  # not needed at all but does improve speed
    def process_int(i):
        length = len(str(i))
        if i == 0:
            return 1, None
        elif length % 2 == 0:
            return int(str(i)[: length // 2]), int(str(i)[length // 2 :])
        else:
            return i * 2024, None


    def iterate_once(count_dict):
        out_dict = defaultdict(int)
        for key, val in count_dict.items():
            for res in process_int(key):
                if res is not None:
                    out_dict[res] += val
        return out_dict


    def solve(s, n=25):
        count_dict = defaultdict(int)
        for x in [int(x) for x in s.split()]:
            count_dict[x] += 1
        for _ in range(n):
            count_dict = iterate_once(count_dict)
        return sum(count_dict.values())



