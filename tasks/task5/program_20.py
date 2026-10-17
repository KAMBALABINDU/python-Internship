#https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    d = deque(map(int, input().split()))
    
    lb = float('inf')
    possible = True
    
    while d:
        if d[0] >= d[-1]:
            c = d[0]
            d.popleft()
        else:
            c = d[-1]
            d.pop()
            
        if c <= lb:
            lb = c
        else:
            possible = False
            break
            
    if possible:
        print("Yes")
    else:
        print("No")
