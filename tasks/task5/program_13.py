#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores = sorted(list(set([score for name, score in records])))
    second_lowest = scores[1]
    
    result = sorted([name for name, score in records if score == second_lowest])
    
    for name in result:
        print(name)
