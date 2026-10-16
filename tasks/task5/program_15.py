#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        c = input().split()
        if c[0] == "insert":
            l.insert(int(c[1]),int(c[2]))
        elif c[0] =="print":
            print(l)
        elif c[0]=="remove":
            l.remove(int(c[1]))
        elif c[0] == "append":
            l.append(int(c[1]))
        elif c[0] == 'pop':
            l.pop()
        elif c[0] == 'reverse':
            l.reverse()
        elif c[0] == 'sort':
            l.sort()
