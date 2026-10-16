#https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_customers = int(input())

total_earned = 0

for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        shoe_sizes[size] -= 1
        total_earned += price

print(total_earned)
