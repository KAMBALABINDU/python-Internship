#https://www.hackerrank.com/challenges/camelcase/problem
import math
import os
import random
import re
import sys

def camelcase(s):
    a = 1
    for i in s:
        if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            a += 1
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
