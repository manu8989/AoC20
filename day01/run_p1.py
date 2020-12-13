#!/usr/bin/env python


import os
import sys
import math


def test_sums_to_2020_example1():
    assert sums_to_2020(1989,31) == True

def test_sums_to_2020_example2():
    assert sums_to_2020(1337,42) == False


def sums_to_2020(a, b):
    return a+b == 2020


if __name__ == "__main__":
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = file.readlines()
        for line_a in lines:
            for line_b in lines:
                a = int(line_a.strip())
                b = int(line_b.strip())
                if sums_to_2020(a, b):
                    print(a*b)
                    print(a)
                    print(b)
                    exit()
                    