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
            answers = g.split('\n')
            for c in set(g.replace('\n','')):
                if all(c in a for a in answers):
                    result += 1

    print(result)
