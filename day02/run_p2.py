#!/usr/bin/env python


import os
import sys
import math


def test_is_valid_example1():
    assert is_valid(1,3,'a','abcde') == True

def test_is_valid_example2():
    assert is_valid(1,3,'b','cdefg') == False

def test_is_valid_example3():
    assert is_valid(2,9,'c','ccccccccc') == False

def test_parse_line_example1():
    assert parse_line('1-3 a: abcde') == (1,3,'a','abcde')

def test_parse_line_example2():
    assert parse_line('1-3 b: cdefg') == (1,3,'b','cdefg')

def test_parse_line_example3():
    assert parse_line('2-9 c: ccccccccc') == (2,9,'c','ccccccccc')


def is_valid(first_occ, second_occ, letter, password):
    return bool(password[first_occ-1] == letter) ^ bool(password[second_occ-1] == letter)

def parse_line(line):
    space_splitted = line.strip().split(' ')
    dash_splitted = space_splitted[0].split('-')
    first_occ = int(dash_splitted[0])
    second_occ = int(dash_splitted[1])
    letter = space_splitted[1][0]
    password = space_splitted[2]
    return (first_occ, second_occ, letter, password)
    

if __name__ == "__main__":
    cnt = 0
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            (first_occ, second_occ, letter, password) = parse_line(line)
            if is_valid(first_occ, second_occ, letter, password):
                cnt+=1
    print(cnt)
                    