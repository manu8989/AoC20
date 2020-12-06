#!/usr/bin/env python


import os
import sys
import math
import re

def test_valid_hcl_example1():
    assert valid_hcl('#12345g') == False

def test_valid_hcl_example2():
    assert valid_hcl('#1235f') == False

def test_valid_hcl_example3():
    assert valid_hcl('1235ff') == False

def test_valid_hcl_example4():
    assert valid_hcl('#1235ff') == True

def test_valid_hcl_example4():
    assert valid_hcl('#1235ff') == True

def test_valid_pid_example1():
    assert valid_pid('000001234') == True

def test_valid_pid_example2():
    assert valid_pid('00001234') == False

def test_valid_pid_example2():
    assert valid_pid('00001234a') == False
    

def valid_hcl(value):
    if len(value) == 7 and re.match("^#[a-f0-9]*$", value):
        return True
    return False

def valid_pid(value):
    if len(value) == 9 and re.match("^[0-9]*$", value):
        return True
    return False

def valid_hgt(value):
    number = int(value.replace('cm','').replace('in',''))
    if value.endswith('cm'):
        if number >= 150 and number <= 193:
            return True
    if value.endswith('in'):
        if number >= 59 and number <= 76:
            return True
    return False
    
if __name__ == "__main__":
    filepath = 'input.txt'
    result = 0
    with open(filepath) as file:
        content = file.read()
        passports = content.split('\n\n')
        for p in passports:
            p_line = p.replace('\n', ' ')
            if p_line.count(':') == 8 or (p_line.count(':') == 7 and not "cid:" in p_line):
                p_data = p_line.split(' ')
                p_dict = {}
                for tmp in p_data:
                    p_dict[tmp.split(':')[0]] = tmp.split(':')[1]
                if int(p_dict['byr']) >= 1920 and int(p_dict['byr']) <= 2002 and \
                    int(p_dict['iyr']) >= 2010 and int(p_dict['iyr']) <= 2020 and \
                    int(p_dict['eyr']) >= 2020 and int(p_dict['eyr']) <= 2030 and \
                    valid_hgt(p_dict['hgt']) and \
                    valid_hcl(p_dict['hcl']) and \
                    any(i == p_dict['ecl'] for i in ('amb','blu','brn','gry','grn','hzl','oth')) and \
                    valid_pid(p_dict['pid']):
                        result +=1 
    print(result)
