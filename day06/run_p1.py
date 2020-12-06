#!/usr/bin/env python


import os
import sys
import math
    

if __name__ == "__main__":
    filepath = 'input.txt'
    result = 0
    with open(filepath) as file:
        content = file.read()
        groups = content.split('\n\n')
        for g in groups:
            answers = g.replace('\n', '')
            result += len(set(answers))

    print(result)
