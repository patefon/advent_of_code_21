# Day 8: Seven Segment Search - Part One and Part Two

from collections import defaultdict
import functools
import operator
import sys
import timeit
import heapq

from typing import List

DATA_PATH = './data/day_9.txt'

def raw_data_preprocess(x):
    return list(map(int, x.strip()))

def read_input(path_to_file: str):
    sys.stdin = open(path_to_file, 'r')
    data = list(map(raw_data_preprocess, sys.stdin.readlines()))
    return data

def find_lower_points(grid):

    results = []

    n = len(grid) if grid else 0
    m = len(grid[0]) if n else 0

    if n == 0 or m == 0:
        return []

    directions = ((0,1),(0,-1),(1,0),(-1,0))

    for i in range(n):
        for j in range(m):
            is_lower = 1
            for d in directions:
                adj_x, adj_y = j+d[1], i+d[0]
                if (adj_x < 0 or adj_x >= m) or (adj_y < 0 or adj_y >= n):
                    continue
                if grid[adj_y][adj_x] <= grid[i][j]:
                    is_lower = 0
            if is_lower: 
                results.append((i,j))

    return results

def dfs(grid, i, j, basin, seen):

    n = len(grid) if grid else 0
    m = len(grid[0]) if n else 0

    directions = ((0,1),(0,-1),(1,0),(-1,0))

    for d in directions:
        
        adj_x, adj_y = j+d[1], i+d[0]

        if (adj_x < 0 or adj_x >= m) or \
            (adj_y < 0 or adj_y >= n):
            continue
        elif grid[adj_y][adj_x] == 9:
            continue

        if grid[i][j] < grid[adj_y][adj_x]:
            if (adj_y, adj_x) not in seen:
                basin.append(grid[adj_y][adj_x])
                seen.add((adj_y, adj_x))
            dfs(grid, adj_y, adj_x, basin, seen)

    return basin

def solution1(data: List[List[int]]) -> int:
    '''
    >>> solution1([[2,1,9,9,9,4,3,2,1,0],[3,9,8,7,8,9,4,9,2,1],[9,8,5,6,7,8,9,8,9,2],[8,7,6,7,8,9,6,7,8,9],[9,8,9,9,9,6,5,6,7,8]])
    15
    '''
    lower_points_locs = find_lower_points(data)
    return sum([data[x[0]][x[1]] for x in lower_points_locs]) + len(lower_points_locs)

def solution2(data: List[List[int]]) -> int:
    '''
    >>> solution2([[2,1,9,9,9,4,3,2,1,0],[3,9,8,7,8,9,4,9,2,1],[9,8,5,6,7,8,9,8,9,2],[8,7,6,7,8,9,6,7,8,9],[9,8,9,9,9,6,5,6,7,8]])
    1134
    '''

    lower_points_locs = find_lower_points(data)

    # find basin size for each lower point
    # return K-largest multiplication

    basins = []
    k = 3

    for loc in lower_points_locs:
        seen = set()
        seen.add((loc[0], loc[1]))
        basin = dfs(data, loc[0], loc[1], [data[loc[0]][loc[1]]], seen)
        heapq.heappush(basins, len(basin))
    
    return functools.reduce(lambda x, y: x*y, heapq.nlargest(k, basins))

def main():
    t0 = timeit.default_timer()
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH))))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution2(read_input(DATA_PATH))))
    print('Finished in %.3f s.' % (timeit.default_timer() - t0))

if __name__ == "__main__":
    main()