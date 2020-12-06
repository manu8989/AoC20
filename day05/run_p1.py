#!/usr/bin/env python

import os
import sys
import math
import re


def test_get_row_example1():
    assert get_row('BFFFBBF') == 70

def test_get_row_example2():
    assert get_row('FFFBBBF') == 14

def test_get_row_example3():
    assert get_row('BBFFBBF') == 102

def test_get_col_example1():
    assert get_col('RRR') == 7

def test_get_col_example2():
    assert get_col('RLL') == 4

def test_get_col_example3():
    assert get_col('RLR') == 5

def test_get_seat_example1():
    assert get_seat('BFFFBBFRRR') == 567

def test_get_seat_example2():
    assert get_seat('FFFBBBFRRR') == 119

def test_get_seat_example3():
    assert get_seat('BBFFBBFRLL') == 820
    

def get_row(value):
    return int(value.replace('B','1').replace('F','0'),2)

def get_col(value):
    return int(value.replace('R','1').replace('L','0'),2)

def get_seat(value):
    return get_row(value[:7]) * 8 + get_col(value[7:10])

    
if __name__ == "__main__":
    filepath = 'input.txt'
    result = 0
    with open(filepath) as file:
        lines = file.readlines()
        print(max(get_seat(line) for line in lines))
