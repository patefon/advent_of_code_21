# Day 6: Lanternfish - Part One and Part Two

import sys
import timeit
from typing import List

DATA_PATH = './data/day_6.txt'

def read_input(path_to_file: str):
    sys.stdin = open(path_to_file, 'r')
    data = list(map(int, sys.stdin.readline().split(',')))
    return data

def solution1(data: List[int], num_days: int):
    '''

    Simulate lanternfish for days

    >>> solution1([3,4,3,1,2], 18)
    26
    >>> solution1([3,4,3,1,2], 80)
    5934
    >>> solution1([3], 80)
    1154
    >>> solution1([], 80)
    0
    '''

    if not data or len(data) == 0:
        return 0

    template = {k:0 for k in range(8+1)}
    fish_freqs = template.copy()

    for i in range(len(data)):
        fish_freqs[data[i]] += 1

    for i in range(1, num_days+1):
        next_fish_freqs = template.copy()
        for j in range(8, -1, -1):
            current = fish_freqs.get(j, 0)
            if current == 0:
                continue
            if j == 0:
                next_fish_freqs[6] += current
                next_fish_freqs[8] += current
            else:
                next_fish_freqs[j-1] += current
        fish_freqs = next_fish_freqs

    return sum(fish_freqs.values())

def main():
    t0 = timeit.default_timer()
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH), num_days=80)))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH), num_days=256)))
    print('Finished in %.3f s.' % (timeit.default_timer() - t0))

if __name__ == "__main__":
    main()