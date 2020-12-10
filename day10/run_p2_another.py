#!/usr/bin/env python


import os
import sys
import math
import time


def copy_list(inp):
    out = []
    for i in inp:
        out.append(i)
    return out

def is_valid(inp):
    for i in range(1,len(inp)):
        if inp[i] - inp[i-1] > 3:
            return False
    return True

def rem(inp):
    removed = []
    i = 1
    while i < len(inp)-1:
        if inp[i+1] - inp[i-1] <= 3:
            removed.append(inp[i])
            del inp[i]
        else:
            i += 1
    return (inp, removed)

if __name__ == "__main__":
    result = 0
    data = []
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            data.append(int(line))
    data.sort()
    data, removed = rem(data)
    for i in range(0,2**len(removed)):
        result += 1
        map = format(i, "0" + str(len(removed)) + "b")
        new_data = copy_list(data)
        idxs = []
        for i in range(len(map)):
            if map[i] == '1':
                new_data.append(removed[i])
                idxs.append(i)
        new_data.sort()
        for i in idxs:
            new_new_data1 = copy_list(new_data)
            new_new_data2 = copy_list(new_data)
            idx = new_new_data1.index(removed[i])
            del new_new_data1[idx-1]
            del new_new_data2[idx+1]
            if is_valid(new_new_data1):
                result+=1
            if is_valid(new_new_data2):
                result+=1

    print(result)