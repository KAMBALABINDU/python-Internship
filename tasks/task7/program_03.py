#https://www.hackerrank.com/challenges/mars-exploration/problem
import math
import os
import random
import re
import sys


def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    return sum(1 for c1, c2 in zip(s, expected) if c1 != c2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
