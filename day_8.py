# Day 8: Seven Segment Search - Part One and Part Two

from collections import defaultdict
import sys
import timeit
import itertools

from typing import List

DATA_PATH = './data/day_8.txt'

segments_to_digit = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

def read_input(path_to_file: str):
    sys.stdin = open(path_to_file, 'r')
    data = list(map(str.strip, sys.stdin.readlines()))
    return data

def decode_output(sample):

    ans = 0
    patterns, output = map(str.strip, sample.split('|'))
    
    for s in output.split():
        x = len(set(list(s)))        
        if x in segments_to_digit.keys():
            ans += 1

    return ans 

def decode_sample(sample):

    ans = 0
    patterns, output = map(str.strip, sample.split('|'))


    #
    #    0000
    #   1    2
    #   1    2
    #    3333
    #   4    5
    #   4    5
    #    6666
    #

    mapping = {idx:None for idx in range(7)}

    using_segments = {
        0: [0,1,2,4,5,6],
        1: [2,5],
        2: [0,2,3,4,6],
        3: [0,2,3,5,6],
        4: [1,3,2,5],
        5: [0,1,3,5,6],
        6: [0,1,3,4,5,6],
        7: [0,2,5],
        8: [0,1,2,3,4,5,6],
        9: [0,1,2,3,5,6]
    }

    patterns_len = defaultdict(list)
    for p in patterns.split():
        patterns_len[len(p)].append(p)

    one = patterns_len.get(2,[0])[0]
    four = patterns_len.get(4,[0])[0]
    seven = patterns_len.get(3,[0])[0]
    eight = patterns_len.get(7, [0])[0]
    nine = None

    if not one or not four or not seven:
        raise ValueError('Cant decode')

    mapping[0] = list(set(seven) - set(one))[0]

    for p in patterns_len.get(6):
        comb = set(four)
        comb.add(mapping[0])
        diff = set(p) - comb
        if len(diff) == 1:
            mapping[6] = list(diff)[0]
            nine = p

    mapping[4] = list(set(eight) - set(nine))[0]

    for p in patterns_len.get(5):
        diff = list(set(nine)-set(p))
        if len(diff) == 1 and diff[0] in set(one):
            mapping[2] = diff[0]

    mapping[5] = list(set(one) - set(mapping[2]))[0]

    for p in patterns_len.get(5):
        comb = set(mapping[6]+mapping[0]+mapping[2]+mapping[5])
        diff = set(p) - comb
        if len(diff) == 1 and list(diff)[0] not in comb:
            mapping[3] = list(diff)[0]

    mapping[1] = list(set(four) - set(mapping[2]+mapping[5]+mapping[3]))[0]

    mapping_inverse = {v:k for k, v in mapping.items()}
    using_segments_inverse = {tuple(sorted(v)):k for k, v in using_segments.items()}

    ans = ''
    for p in output.split():
        code = tuple(sorted([mapping_inverse.get(x) for x in p]))
        if not using_segments_inverse.get(code) and len(p) == 7:
            ans += '0'
            continue
        
        ans += str(using_segments_inverse.get(code, 0))

    return ans

def solution1(data: List[int]):
    ans = 0
    for i in range(len(data)):
        ans += decode_output(data[i])
    return ans

def solution2(data: List[int]):
    ans = 0
    for i in range(len(data)):
        ans += int(decode_sample(data[i]))
    return ans

def main():
    t0 = timeit.default_timer()
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH))))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution2(read_input(DATA_PATH))))
    print('Finished in %.3f s.' % (timeit.default_timer() - t0))

if __name__ == "__main__":
    main()