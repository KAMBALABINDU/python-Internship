#https://www.hackerrank.com/challenges/no-idea/problem
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    array = input_data[2:2+n]
    
    set_a = set(input_data[2+n : 2+n+m])
    set_b = set(input_data[2+n+m : 2+n+2*m])
    
    happiness = 0
    for x in array:
        if x in set_a:
            happiness += 1
        elif x in set_b:
            happiness -= 1
            
    print(happiness)

if __name__ == '__main__':
    solve()
