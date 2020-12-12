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

def update_seat(m, origin_row, origin_col):
    surrounding_seats = []
    row = origin_row
    col = origin_col
    while row > 0 and col > 0:
        seat = m[row-1][col-1]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        row -= 1
        col -= 1
    row = origin_row
    col = origin_col
    while row > 0 and col < col_size-1:
        seat = m[row-1][col+1]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        row -= 1
        col += 1
    row = origin_row
    col = origin_col
    while col > 0 and row < row_size-1:
        seat = m[row+1][col-1]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        row += 1
        col -= 1
    row = origin_row
    col = origin_col
    while row < row_size-1 and col < col_size-1:
        seat = m[row+1][col+1]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        row += 1
        col += 1
    row = origin_row
    col = origin_col
    while row > 0:
        seat = m[row-1][col]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        row -= 1
    row = origin_row
    col = origin_col
    while col > 0:
        seat = m[row][col-1]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        col -= 1
    row = origin_row
    col = origin_col
    while col < col_size-1:
        seat = m[row][col+1]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        col += 1
    row = origin_row
    col = origin_col
    while row < row_size-1:
        seat = m[row+1][col]
        if seat in ['#','L']:
            surrounding_seats.append(seat)
            break;
        row += 1
    if m[origin_row][origin_col] == 'L' and not '#' in surrounding_seats:
        return '#'
    elif m[origin_row][origin_col] == '#' and surrounding_seats.count('#') >= 5:
        return 'L'
    else:
        return m[origin_row][origin_col]
    
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
