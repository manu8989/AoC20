#!/usr/bin/env python


import os
import sys
import math


can_contain = {}


def test_parse_line_example1():
    assert parse_line('light red bags contain 1 bright white bag, 2 muted yellow bags.') == ('light red',[(1,'bright white'),(2, 'muted yellow')])

def test_parse_line_example2():
    assert parse_line('muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.') == ('muted yellow',[(2, 'shiny gold'),(9,'faded blue')])

def test_parse_line_example3():
    assert parse_line('dark violet bags contain no other bags.') == ('dark violet',[])


def parse_line(line):
    splitted = str.strip(line).split(' bags contain ')
    outer = splitted[0]
    inner = []
    if splitted[1] != 'no other bags.':
        inner_tmp = splitted[1].split(', ')
        inner_tmp = [i.split(' ') for i in inner_tmp]
        inner = [(int(i[0]),' '.join(i[1:-1])) for i in inner_tmp]
    return (outer, inner)

def next_layer_contains(root_color):
    if root_color not in can_contain or not len(can_contain[root_color]):
        return 0
    bag_sum = 0
    for c in can_contain[root_color]:
        bag_sum += c[0]+c[0]*next_layer_contains(c[1])
    return bag_sum


if __name__ == "__main__":
    filepath = 'input.txt'
    result = 0
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            data = parse_line(line)
            can_contain[data[0]] = data[1]
    print(next_layer_contains('shiny gold'))
