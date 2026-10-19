#https://www.hackerrank.com/challenges/separate-the-numbers/problem
import math
import os
import random
import re
import sys

def separateNumbers(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        first_str = s[:i]
        if first_str.startswith('0'):
            break
            
        current = int(first_str)
        reconstructed = first_str
        
        while len(reconstructed) < n:
            current += 1
            reconstructed += str(current)
            
        if reconstructed == s:
            print(f"YES {first_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
