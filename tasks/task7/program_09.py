#https://www.hackerrank.com/challenges/beautiful-binary-string/problem
import math
import os
import random
import re
import sys
def beautifulBinaryString(b):
    i = 0
    c = 0
    while i < len(b)-2:
        if b[i:i+3] == '010':
            c += 1
            i+= 3
        else:
            i+=1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)
    fptr.write(str(result) + '\n')
    fptr.close()
