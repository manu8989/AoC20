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
        depart_at = int(lines[0].strip())
    for b in lines[1].strip().split(','):
        if(b != 'x'):
            bus = int(b)
            busses.append((bus, bus*(depart_at/bus)+bus))
    next_bus = np.argmin([b[1] for b in busses])
    print(busses[next_bus][0]*(busses[next_bus][1]-depart_at))
