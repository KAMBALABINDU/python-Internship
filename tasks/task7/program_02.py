#https://www.hackerrank.com/challenges/py-the-captains-room/problem
n = int(input())
l = list(map(int,input().split()))
captains_room = (sum(set(l)) * n - sum(l)) // (n - 1)
print(captains_room)
    
