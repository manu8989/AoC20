#!/usr/bin/env python

import os
import sys
import math
import numpy as np

def apply_mask(val, mask):
    val = list(val)
    for pos in range(len(mask)):
        if mask[pos] == '0' or mask[pos] == '1':
            val[pos] = mask[pos]
    return int(''.join(val),2)

def get_mask(line):
    return line.split('=')[1].strip()

def work_on_memory(memory, line, mask):
    line = line.replace('mem[','').replace(']','').split('=')
    adr = int(line[0])
    val_bin = format(int(line[1]),'036b')
    val_dec = apply_mask(val_bin, mask)
    memory[adr] = val_dec

if __name__ == "__main__":
    program = []
    memory = {}
    mask = ""
    filepath = 'input.txt'
    with open(filepath) as file:
        program = file.readlines()
    for s in program:
        if s.startswith('mask'):
            mask = get_mask(s)
        if s.startswith('mem'):
            work_on_memory(memory, s, mask)
    print(sum([memory[i] for i in memory]))
