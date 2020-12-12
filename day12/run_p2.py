#!/usr/bin/env python

import os
import sys
import math

def rotate_right(t,n,e):
    for i in range(t):
        tmp = n
        n = -e
        e = tmp
    return (n,e)

if __name__ == "__main__":
    instructions = []
    filepath = 'input.txt'
    with open(filepath) as file:
        instructions = [(l.strip()[0],int(l.strip()[1:])) for l in file.readlines()]
    ship_north = 0
    ship_east = 0
    wp_north = 1
    wp_east = 10
    for i in instructions:
        if i[0] == "N":
            wp_north += i[1]
        if i[0] == "S":
            wp_north -= i[1]
        if i[0] == "E":
            wp_east += i[1]
        if i[0] == "W":
            wp_east -= i[1]
        if i[0] == "R":
            wp_north,wp_east = rotate_right(i[1]/90,wp_north,wp_east)
        if i[0] == "L":
            wp_north,wp_east = rotate_right(abs((i[1]-360)/90),wp_north,wp_east)
        if i[0] == "F":
            ship_north += wp_north*i[1]
            ship_east += wp_east*i[1]
    
    print(abs(ship_north)+abs(ship_east))
