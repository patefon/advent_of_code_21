# Day 2. Dive! - Part One and Part Two

# Now, you need to figure out how to pilot this thing.
# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:
# * forward X increases the horizontal position by X units.
# * down X increases the depth by X units.
# * up X decreases the depth by X units.

################
# Part Two    ##
################

# Based on your calculations, the planned course doesn't seem to make any sense. You find the 
# submarine manual and discover that the process is actually slightly more complicated.

# In addition to horizontal position and depth, you'll also need to track a third value, aim, 
# which also starts at 0. The commands also mean something entirely different than you first thought:
# * down X increases your aim by X units.
# * up X decreases your aim by X units.
# * forward X does two things:
# * It increases your horizontal position by X units.
# * It increases your depth by your aim multiplied by X.

import sys
import timeit

from functools import reduce
from collections import defaultdict

from typing import List

DATA_PATH = './data/day_2.txt'

def read_input(path_to_file: str):
    sys.stdin = open(path_to_file, 'r')
    data = map(lambda x: x.split(), sys.stdin.readlines())
    data = list(map(lambda x: (x[0], int(x[1])), data))
    return data

def solution1(arr: List[str]):
    '''
    >>> solution1([('forward',5),('down',5),('forward',8),('up',3),('down',8),('forward',2)])
    150
    >>> solution1([('forward',5)])
    0
    >>> solution1([('forward',5),('down',10)])
    50
    >>> solution1([('forward',5),('down',10),('up',11)])
    0
    '''
    pos_x = 0 # horizontal position
    pos_y = 0 # vertical position

    def calc_ops_helper(acc, el):
        acc[el[0]] += el[1]
        return acc
    ops = reduce(calc_ops_helper, arr, defaultdict(int))
    pos_x = ops.get('forward', 0) # forward X increases the horizontal position.
    pos_y = ops.get('down', 0) - ops.get('up', 0) # down X increases/up X decreases the depth
    return pos_x*pos_y if pos_y > 0 else 0

def solution2(arr: List[str]):
    '''
    >>> solution1([('forward',5),('down',5),('forward',8),('up',3),('down',8),('forward',2)])
    150
    >>> solution1([('forward',5)])
    0
    >>> solution1([('forward',5),('down',10)])
    50
    >>> solution1([('forward',5),('down',10),('up',11)])
    0
    '''
    pos_x = 0 # horizontal position
    pos_y = 0 # vertical position
    aim = 0

    def calc_ops_helper(acc, el):
        pos_x, pos_y, aim = acc
        if el[0] == 'down':
            aim += el[1]
        elif el[0] == 'up':
            aim -= el[1]
        elif el[0] == 'forward':
            pos_x += el[1]
            pos_y += aim * el[1]
        return pos_x, pos_y, aim
    
    ops = reduce(calc_ops_helper, arr, (pos_x, pos_y, aim))

    return ops[0]*ops[1]

def main():
    t0 = timeit.default_timer()
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH))))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution2(read_input(DATA_PATH))))
    print('Finished in %.3f s.' % (timeit.default_timer() - t0))

if __name__ == "__main__":
    main()