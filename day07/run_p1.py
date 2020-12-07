#!/usr/bin/env python


import os
import sys
import math


can_contain = {}


def test_parse_line_example1():
    assert parse_line('light red bags contain 1 bright white bag, 2 muted yellow bags.') == ('light red',['bright white','muted yellow'])

def test_parse_line_example2():
    assert parse_line('muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.') == ('muted yellow',['shiny gold','faded blue'])


def parse_line(line):
    split1 = line.split(' bags contain ')
    outer = split1[0]
    inner_tmp = split1[1].split(', ')
    inner = [' '.join(i.split(' ')[1:-1]) for i in inner_tmp]
    return (outer, inner)

def can_it_or_its_children_contain_shiny_gold(root_color):
    if root_color not in can_contain:
        return False
    if 'shiny gold' in can_contain[root_color]:
        return True
    else:
        return any(can_it_or_its_children_contain_shiny_gold(c) for c in can_contain[root_color])


if __name__ == "__main__":
    filepath = 'input.txt'
    result = 0
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            data = parse_line(line)
            can_contain[data[0]] = data[1]
        for key in can_contain.iterkeys():
            if can_it_or_its_children_contain_shiny_gold(key):
                result += 1
    print(result)
