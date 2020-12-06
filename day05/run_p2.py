#!/usr/bin/env python

import os
import sys
import math
import re
import numpy as np
    

def get_row(value):
    return int(value.replace('B','1').replace('F','0'),2)

def get_col(value):
    return int(value.replace('R','1').replace('L','0'),2)

def get_seat(value):
    return get_row(value[:7]) * 8 + get_col(value[7:10])

    
if __name__ == "__main__":
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = file.readlines()
        seats = np.zeros(max(get_seat(line) for line in lines) + 1)
        for line in lines:
            seats[get_seat(line)] = 1
        for i in range(1,len(seats)):
            if seats[i-1] and not seats[i] and seats[i+1]:
                print(i)

