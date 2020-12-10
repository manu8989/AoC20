#!/usr/bin/env python


import os
import sys
import math


if __name__ == "__main__":
    filepath = 'input.txt'
    data = []
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            data.append(int(line))
    data.sort()
    sum_1jolt_diff = 1
    sum_3jolt_diff = 1
    for i in range(len(data)-1):
        if data[i] + 1 == data[i+1]:
            sum_1jolt_diff += 1
        elif data[i] + 3 == data[i+1]:
            sum_3jolt_diff += 1
    print(sum_1jolt_diff*sum_3jolt_diff)