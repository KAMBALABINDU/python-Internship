#https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        row = s[::-1] + s[1:]
        lines.append(row.center(4 * size - 3, "-"))
        
    print("\n".join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
