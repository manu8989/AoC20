#!/usr/bin/env python


import os
import sys
import math


if __name__ == "__main__":
    filepath = 'input.txt'
    search_for = 0
    data = []
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            data.append(int(line))
    for i in range(25, len(data)):
        if not any([x!=y and x+y==data[i] for y in data[i-25:i] for x in data[i-25:i]]):
            search_for = data[i]
            break;
    
    for i in range(1,len(data)):
        for j in range(i+1,len(data)):
            if sum(data[i:j+1]) == search_for:
                print(min(data[i:j+1])+max(data[i:j+1]))
                exit()