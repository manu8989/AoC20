#!/usr/bin/env python

import os
import sys
import math
import numpy as np
import time

if __name__ == "__main__":
    numbers = {6:0,19:1,0:2,5:3,7:4,13:5}
    keys = {6,19,0,5,7,13} # set makes search faster
    limit = 30000000
    last_value = 1
    start_time = time.time()
    for i in range(len(numbers),limit-1):
        tmp = last_value
        if last_value in keys:
            last_value = i - numbers[last_value]
        else:
            keys.add(last_value)
            last_value = 0
        numbers[tmp] = i
        if i % (limit/100) == 0:
            print(str(100*i/limit) + '%')
    end_time = time.time()
    print('Duration: ' + str(end_time - start_time) + 's')
    print(last_value)
    