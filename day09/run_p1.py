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
    for i in range(25, len(data)):
        if not any([x!=y and x+y==data[i] for y in data[i-25:i] for x in data[i-25:i]]):
            print(data[i])
            exit()
