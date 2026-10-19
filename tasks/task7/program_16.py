#https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    encrypted = []
    k = k % 26
    
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted.append(new_char)
        else:
            encrypted.append(char)
            
    return "".join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
