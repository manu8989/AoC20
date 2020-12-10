#!/usr/bin/env python


import os
import sys
import math
import time

counter = 1
exist = []

def copy_list(inp):
    out = []
    for i in inp:
        out.append(i)
    return out

def next_step(inp, first_index):
    global counter
    global exist
    for i in range(first_index,len(inp)-1):
        if inp[i+1] - inp[i-1] <= 3:
            new_inp = copy_list(inp)
            del new_inp[i]
            if new_inp not in exist:
                counter += 1
                exist.append(new_inp)
                next_step(new_inp,i)

if __name__ == "__main__":
    data = [0]
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            data.append(int(line))
    data.sort()
    start = time.time()
    next_step(data, 1)
    end = time.time()
    print(counter)
    print(end-start)