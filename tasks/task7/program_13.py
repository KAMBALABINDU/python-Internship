#

import math
import os
import random
import re
import sys


def isValid(s):
    d = {}
    for i in s:
        d[i] = s.count(i)

    freq = list(d.values())
    unique = set(freq)

    if len(unique) == 1:
        return 'YES'

    if len(unique) == 2:
        a, b = sorted(unique)

        if freq.count(b) == 1 and b - a == 1:
            return 'YES'

        if freq.count(a) == 1 and a == 1:
            return 'YES'

    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
