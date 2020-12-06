#!/usr/bin/env python


import os
import sys
import math


def is_tree(map, row, column):
    col_size = len(map[0]) - 1
    return map[row][column % col_size] == '#'
    
if __name__ == "__main__":
    filepath = 'input.txt'
    result = 0
    with open(filepath) as file:
        content = file.read()
        passports = content.split('\n\n')
        for p in passports:
            p = p.replace('\n', ' ')
            if p.count(':') == 8 or (p.count(':') == 7 and not "cid:" in p):
                result += 1
    print(result)
