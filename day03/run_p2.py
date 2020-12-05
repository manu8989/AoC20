#!/usr/bin/env python


import os
import sys
import math


def is_tree(map, row, column):
    col_size = len(map[0]) - 1
    return map[row][column % col_size] == '#'

def get_trees_on_slope(map, slope_row, slope_column):
    row_size = len(my_map)
    row_cnt = 0
    col_cnt = 0
    result_cnt = 0
    while row_cnt < row_size:
        if is_tree(my_map, row_cnt, col_cnt):
            result_cnt +=1
        row_cnt += slope_row
        col_cnt += slope_column
    return result_cnt

if __name__ == "__main__":
    filepath = 'input.txt'
    with open(filepath) as file:
        my_map = file.readlines()
        a = get_trees_on_slope(my_map, 1, 1)
        b = get_trees_on_slope(my_map, 1, 3)
        c = get_trees_on_slope(my_map, 1, 5)
        d = get_trees_on_slope(my_map, 1, 7)
        e = get_trees_on_slope(my_map, 2, 1)
    print(a*b*c*d*e)
