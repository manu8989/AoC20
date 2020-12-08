#!/usr/bin/env python


import os
import sys
import math


def parse_line(line):
    splitted = str.strip(line).split(' ')
    return [splitted[0], int(splitted[1])]

def get_program(lines):
    program = []
    for line in lines:
        program.append(parse_line(line))
    return program

def exec_program(program):
    executed_steps = []
    exec_index = 0
    result = 0
    while True:
        if exec_index >= len(program):
            break;
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
            return (False, result)
    return (True, result)


if __name__ == "__main__":
    filepath = 'input.txt'
    with open(filepath) as file:
        lines = file.readlines()
        program = get_program(lines)
        for i in range(len(program)):
            result = (False, 0)
            if program[i][0] == "nop":
                program = get_program(lines)
                program[i][0] = "jmp"
                result = exec_program(program)
            elif program[i][0] == "jmp":
                program = get_program(lines)
                program[i][0] = "nop"
                result = exec_program(program)
            if result[0]:
                print(result[1])

    print("DONE")
