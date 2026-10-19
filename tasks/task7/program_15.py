#https://www.hackerrank.com/challenges/game-of-thrones/problem
import math
import os
import random
import re
import sys
def gameOfThrones(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
            
    if len(s) % 2 == 0:
        return "YES" if odd_count == 0 else "NO"
    else:
        return "YES" if odd_count == 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
