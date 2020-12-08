#!/usr/bin/env python


import os
import sys
import math


def parse_line(line):
    splitted = str.strip(line).split(' ')
    return (splitted[0], int(splitted[1]))


if __name__ == "__main__":
    filepath = 'input.txt'
    program = []
    executed_steps = []
    exec_index = 0
    result = 0
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            program.append(parse_line(line))
    while True:
        if exec_index not in executed_steps:
            executed_steps.append(exec_index)
            if program[exec_index][0] == "nop":
                exec_index += 1
            elif program[exec_index][0] == "acc":
                result += program[exec_index][1]
                exec_index += 1
            elif program[exec_index][0] == "jmp":
                exec_index += program[exec_index][1]
        else:
            break;

    print(result)
