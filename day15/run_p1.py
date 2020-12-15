#!/usr/bin/env python

import os
import sys
import math
import numpy as np


if __name__ == "__main__":
    numbers = [6,19,0,5,7,13,1]
    for _ in range(2020-len(numbers)):
        if numbers[-1] in numbers[0:-1]:
            cnt = 0
            for i in reversed(range(0,len(numbers)-1)):
                cnt += 1
                if numbers[i] == numbers[-1]:
                    numbers.append(cnt)
                    break;
        else:
            numbers.append(0)
    print(numbers[-1])