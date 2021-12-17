# Day 10: Syntax Scoring - Part One and Part Two

import functools
import sys
import timeit
import statistics

from typing import List

DATA_PATH = './data/day_10.txt'

def read_input(path_to_file: str):
    sys.stdin = open(path_to_file, 'r')
    data = list(map(str.strip, sys.stdin.readlines()))
    return data

def is_corrupted(s):

    openinigs = '{(<['

    mapping = {
        '}': '{',
        ')': '(',
        '>': '<',
        ']': '['
    }

    stk = []
    
    for i in range(len(s)):

        if s[i] in openinigs:
            stk.append(s[i])
        elif stk and s[i] not in openinigs and stk[-1] == mapping.get(s[i], None):
            stk.pop()
        else:
            return 1, s[i]

    return 0, stk

def solution1(data: List[List[str]]) -> int:
    
    costs = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    error = 0

    for s in data:
        corrupted, incorrect_char = is_corrupted(s)
        if corrupted:
            error += costs.get(incorrect_char, 0)

    return error

def solution2(data: List[List[str]]) -> int:
    
    costs = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    mapping = {
        '{': '}',
        '(': ')',
        '<': '>',
        '[': ']'
    }

    errors_costs = []

    for s in data:
        
        corrupted, stk = is_corrupted(s)
        
        if corrupted:
            continue
        
        if len(stk) == 0:
            continue

        errors_costs.append(functools.reduce(\
            lambda acc, x: acc*5+costs.get(x),\
            [mapping.get(x) for x in reversed(stk)],\
            0))

    return statistics.median(errors_costs)

def main():
    t0 = timeit.default_timer()
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH))))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution2(read_input(DATA_PATH))))
    print('Finished in %.3f s.' % (timeit.default_timer() - t0))

if __name__ == "__main__":
    main()