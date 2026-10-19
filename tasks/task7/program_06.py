#https://www.hackerrank.com/challenges/pangrams/problem
import math
import os
import random
import re
import sys

def pangrams(s):
    letters = {char for char in s.lower() if char.isalpha()}
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
