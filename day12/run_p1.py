#!/usr/bin/env python

import os
import sys
import math
    
if __name__ == "__main__":
    instructions = []
    filepath = 'input.txt'
    with open(filepath) as file:
        instructions = [(l.strip()[0],int(l.strip()[1:])) for l in file.readlines()]
    north = 0
    east = 0
    direction = 0
    for i in instructions:
        if i[0] == "N":
            north += i[1]
        if i[0] == "S":
            north -= i[1]
        if i[0] == "E":
            east += i[1]
        if i[0] == "W":
            east -= i[1]
        if i[0] == "L":
            direction -= i[1]
        if i[0] == "R":
            direction += i[1]
        if i[0] == "F":
            if direction % 360 == 0:
                east += i[1]
            if direction % 360 == 90:
                north -= i[1]
            if direction % 360 == 180:
                east -= i[1]
            if direction % 360 == 270:
                north += i[1]
    
    print(abs(north)+abs(east))
