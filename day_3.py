# Day 3. Binary Diagnostic - Part One and Part Two

import sys
import timeit

from functools import reduce
from collections import defaultdict

from typing import List

DATA_PATH = './data/day_3.txt'

def read_input(path_to_file: str):
    sys.stdin = open(path_to_file, 'r')
    data = list(map(str.strip, sys.stdin.readlines()))
    return data

def solution1(arr: List[str]):
    '''
    >>> solution1(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    198
    >>> solution1(['1'])
    0
    '''
    
    gamma = [1 if x.count('1') >= x.count('0') else 0 for x in zip(*arr)] 
    epsilon = [int(not x) for x in gamma]

    return int(''.join(map(str, gamma)), 2) * int(''.join(map(str, epsilon)), 2)

def solution2(arr: List[str]):
    '''
    >>> solution2(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    230
    '''

    gamma = epsilon = None

    temp = arr[::]

    i = 0
    while True:
        zipped_arr = list(zip(*temp))
        if len(temp) == 1: 
            gamma = int(temp[0], 2)
            break
        if zipped_arr[i].count('1') >= zipped_arr[i].count('0'):
            temp = list(filter(lambda x: x[i] == '1', temp))
        else:
            temp = list(filter(lambda x: x[i] == '0', temp))
        i += 1

    temp = arr[::]
    i = 0
    while True:
        zipped_arr = list(zip(*temp))
        if zipped_arr[i].count('1') >= zipped_arr[i].count('0'):
            temp = list(filter(lambda x: x[i] == '0', temp))
        else:
            temp = list(filter(lambda x: x[i] == '1', temp))
        if len(temp) == 1: 
            epsilon = int(temp[0], 2)
            break
        i += 1

    return epsilon*gamma

def main():
    t0 = timeit.default_timer()
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH))))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution2(read_input(DATA_PATH))))
    print('Finished in %.3f s.' % (timeit.default_timer() - t0))

if __name__ == "__main__":
    main()