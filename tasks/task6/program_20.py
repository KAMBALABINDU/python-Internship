#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
n = int(input())
for i in range(n):
    p = input()
    if len(p)==10 and p[0] in '789' and p.isdigit():
        print('YES')
    else:
        print('NO')
