#https://www.hackerrank.com/challenges/nested-list/problem#
if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
        
    scores = sorted(list(set([score for name, score in score_list])))
    second_lowest = scores[1]
    
    result_names = sorted([name for name, score in score_list if score == second_lowest])
    
    for name in result_names:
        print(name)
