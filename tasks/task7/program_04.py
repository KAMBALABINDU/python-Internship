#https://www.hackerrank.com/challenges/funny-string/problem
import math
import os
import random
import re
import sys
def funnyString(s):
    rev_s = s[::-1]
    s_diffs = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1)]
    rev_diffs = [abs(ord(rev_s[i]) - ord(rev_s[i+1])) for i in range(len(rev_s) - 1)]
    if s_diffs == rev_diffs:
        return "Funny"
    else:
        return "Not Funny"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
