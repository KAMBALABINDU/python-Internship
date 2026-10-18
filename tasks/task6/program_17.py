#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
s = set(map(int,input().split()))
n = int(input())
s1 = set()
for i in range(n):
    s2 = list(map(int,input().split()))
    s1.update(s2)
print(s1.issubset(s))
