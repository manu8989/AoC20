#!/usr/bin/env python

import os
import sys
import math
import numpy as np
    
if __name__ == "__main__":
    depart_at = 0
    busses = []
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = file.readlines()
    t = 0
    max_bus = 0
    for b in lines[1].strip().split(','):
        if(b != 'x'):
            bus = int(b)
            if bus > max_bus:
                max_bus = bus
            busses.append((bus, t))
        t += 1
    t = busses[0][0]*(100000000000000/busses[0][0])
    step_size = busses[0][0]*(max_bus/busses[0][0])
    while True:
        if all([(t+b[1]) % b[0] == 0 for b in busses]):
            print(t)
            exit()
        t += step_size
