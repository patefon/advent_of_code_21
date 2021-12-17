# Day 11: Dumbo Octopus - Part One and Part Two

import sys
import timeit

from typing import List

DATA_PATH = './data/day_11.txt'

def raw_data_preprocess(x):
    return list(map(int, x.strip()))

def read_input(path_to_file: str):
    sys.stdin = open(path_to_file, 'r')
    data = list(map(raw_data_preprocess, sys.stdin.readlines()))
    return data

def flash(grid, i, j, flashed, num_flashes):
    
    n = len(grid) if grid else 0
    m = len(grid[0]) if n else 0
    
    directions = ((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1))

    for d in directions:
        
        next_y, next_x = i+d[0], j+d[1]
        
        if (next_x < 0 or next_x >= m) or (next_y < 0 or next_y >= n):
            continue
        
        new_val = grid[next_y][next_x]+1
        
        if new_val <= 9 and (next_y, next_x) not in flashed:
            grid[next_y][next_x] = new_val
            continue
        elif (next_y, next_x) not in flashed:
            grid[next_y][next_x] = 0
            flashed.add((next_y, next_x))
            num_flashes[0]+=1
            flash(grid, next_y, next_x, flashed, num_flashes)

def solution1(grid: List[List[int]]) -> int:
            
    n = len(grid) if grid else 0
    m = len(grid[0]) if n else 0

    steps = 100
    num_flashes = [0]

    for s in range(steps):
        flashed = set()
        for i in range(n):
            for j in range(m):
                new_val = grid[i][j]+1
                if new_val <= 9 and (i, j) not in flashed:
                    grid[i][j] = new_val
                    continue
                elif (i,j) in flashed:
                    continue
                grid[i][j] = 0
                flashed.add((i, j))
                num_flashes[0] += 1
                flash(grid, i, j, flashed, num_flashes)

    return num_flashes

def solution2(grid: List[List[int]]) -> int:
            
    n = len(grid) if grid else 0
    m = len(grid[0]) if n else 0
    s = 1

    num_flashes = [0]

    while True:
        
        flashed = set()
        
        for i in range(n):
            for j in range(m):
                new_val = grid[i][j]+1
                if new_val <= 9 and (i, j) not in flashed:
                    grid[i][j] = new_val
                    continue
                elif (i,j) in flashed:
                    continue
                grid[i][j] = 0
                flashed.add((i, j))
                num_flashes[0] += 1
                flash(grid, i, j, flashed, num_flashes)
        
        if len(flashed) == (n*m):
            return s

        s += 1

def main():
    t0 = timeit.default_timer()
    print('Part I Answer for %s is [%s]' % (DATA_PATH, solution1(read_input(DATA_PATH))))
    print('Part II Answer for %s is [%s]' % (DATA_PATH, solution2(read_input(DATA_PATH))))
    print('Finished in %.3f s.' % (timeit.default_timer() - t0))

if __name__ == "__main__":
    main()