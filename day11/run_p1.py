#!/usr/bin/env python


import os
import sys
import math

row_size = 0
col_size = 0

def copy_list(inp):
    out = []
    for x in inp:
        line = []
        for y in x:
            line.append(y)
        out.append(line)
    return out

def update_seat(m, row, col):
    surrounding_seats = []
    if row > 0 and col > 0:
        surrounding_seats.append(m[row-1][col-1])
    if row > 0 and col < col_size-1:
        surrounding_seats.append(m[row-1][col+1])
    if col > 0 and row < row_size-1:
        surrounding_seats.append(m[row+1][col-1])
    if row < row_size-1 and col < col_size-1:
        surrounding_seats.append(m[row+1][col+1])
    if row > 0:
        surrounding_seats.append(m[row-1][col])
    if col > 0:
        surrounding_seats.append(m[row][col-1])
    if col < col_size-1:
        surrounding_seats.append(m[row][col+1])
    if row < row_size-1:
        surrounding_seats.append(m[row+1][col])
    if m[row][col] == 'L' and not '#' in surrounding_seats:
        return '#'
    elif m[row][col] == '#' and surrounding_seats.count('#') >= 4:
        return 'L'
    else:
        return m[row][col]
    
if __name__ == "__main__":
    my_map = []
    last_my_map = []
    filepath = 'input.txt'
    with open(filepath) as file:
        my_map = [list(l.strip()) for l in file.readlines()]
        row_size = len(my_map)
        col_size = len(my_map[0])
    last_my_map = copy_list(my_map)
    while True:
        for x in range(row_size):
            for y in range(col_size):
                my_map[x][y] = update_seat(last_my_map,x,y)
        if my_map == last_my_map:
            break;
        else:
            last_my_map = copy_list(my_map)

    print(sum([l.count('#') for l in my_map]))
