#!/usr/bin/env python


import os
import sys
import math


def is_tree(map, row, column):
    col_size = len(map[0]) - 1
    return map[row][column % col_size] == '#'
    
if __name__ == "__main__":
    filepath = 'input.txt'
    with open(filepath) as file:
        my_map = file.readlines()
        row_size = len(my_map)
        row_cnt = 0
        col_cnt = 0
        result_cnt = 0
        while row_cnt < row_size:
            if is_tree(my_map, row_cnt, col_cnt):
                result_cnt +=1
            row_cnt += 1
            col_cnt += 3
    print(result_cnt)
