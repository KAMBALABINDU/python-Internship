#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        subs = string[i:i+k]
        seen = set()
        p = ""

        for ch in subs:
            if ch not in seen:
                seen.add(ch)
                p += ch

        print(p)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
