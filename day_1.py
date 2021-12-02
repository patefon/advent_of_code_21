# Day 1. Sonar Sweep - Part One and Part Two

# running: python -m doctest -v day_1.py

# As the submarine drops below the surface of the ocean, it automatically performs 
# a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report 
# (your puzzle input) appears: each line is a measurement of the sea floor depth as 
# the sweep looks further and further away from the submarine.
# For example, suppose you had the following report:
# [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# This report indicates that, scanning outward from the submarine, the sonar sweep 
# found depths of 199, 200, 208, 210, and so on.

# The first order of business is to figure out how quickly the depth increases, 
# just so you know what you're dealing with - you never know if the keys will get 
# carried into deeper water by an ocean current or a fish or something.
# To do this, count the number of times a depth measurement increases from the 
# previous measurement.

################
# Part Two    ##
################

# Considering every single measurement isn't as useful as you expected: there's 
# just too much noise in the data.

# Your goal now is to count the number of times the sum of measurements in this 
# sliding window increases from the previous sum. So, compare A with B, then 
# compare B with C, then C with D, and so on. Stop when there aren't enough measurements 
# left to create a new three-measurement sum.

from typing import List

DATA_PATH = './data/day_1.txt'

def read_input(path: str):
    res = []
    with open(path, 'r') as f:
        while True:
            data = f.readline()
            if not data: break
            res.append(int(data.strip()))
    return res

def solution1(arr: List[str]):
    '''
    Compare elements -> sum

    >>> solution1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    7
    
    >>> solution1([199, 200])
    1
    
    >>> solution1([200, 199])
    0

    >>> solution1([200])
    0

    '''
    return sum([arr[i] > arr[i-1] for i in range(1, len(arr))]) if arr and len(arr) > 1 else 0

def solution2(arr: List[str]):
    '''
    Compare elements -> sum

    >>> solution2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    5

    >>> solution2([1, 1, 1, 2, 2])
    2

    >>> solution2([1, 1, 1, 1, 1])
    0
    
    >>> solution2([199, 200])
    0
    
    >>> solution2([200, 199])
    0

    >>> solution2([200])
    0

    '''

    if not arr or len(arr) <= 3:
        return 0

    ans = 0
    window = []

    for i in range(len(arr)):
        if len(window) < 3:
            window.append(arr[i])
        else:
            current_sum = sum(window)
            window.pop(0)
            window.append(arr[i])
            ans += current_sum < sum(window)
    
    return ans

if __name__ == "__main__":
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH))))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution2(read_input(DATA_PATH))))