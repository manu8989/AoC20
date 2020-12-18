#!/usr/bin/env python

import os
import sys
import math
import numpy as np


ranges = {}


def parse_ranges(inp):
    for line in inp.split('\n'):
        l = line.split(': ')
        n = l[1].split(' or ')
        r = [(int(t.split('-')[0]),int(t.split('-')[1])) for t in n]
        ranges[l[0]] = r


def is_nmbr_valid(nmbr):
    for key,value in ranges.items():
        if (nmbr >= value[0][0] and nmbr <= value[0][1]) or (nmbr >= value[1][0] and nmbr <= value[1][1]):
            return True
    return False


if __name__ == "__main__":
    result = 0
    filepath = 'input.txt'
    with open(filepath) as file:
        content = file.read()
    parts = content.split('\n\n')
    parse_ranges(parts[0])
    for ticket in parts[2].split('\n')[1:-1]:
        for n in ticket.split(','):
            if not is_nmbr_valid(int(n)):
                result += int(n)
    print(result)
