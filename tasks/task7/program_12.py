#https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys


def makingAnagrams(s1, s2):
    deletions = 0
    for char in "abcdefghijklmnopqrstuvwxyz":
        deletions += abs(s1.count(char) - s2.count(char))
    return deletions
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
