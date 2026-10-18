#https://www.hackerrank.com/challenges/py-set-mutations/problem
n = int(input())
s = set(map(int, input().split()))
num_operations = int(input())

for _ in range(num_operations):
    op_name, length = input().split()
    other_set = set(map(int, input().split()))
    
    getattr(s, op_name)(other_set)

print(sum(s))
