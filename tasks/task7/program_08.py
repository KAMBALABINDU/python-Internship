#https://www.hackerrank.com/challenges/gem-stones/problem
common_chars = set(arr[0])
    for rock in arr[1:]:
        common_chars.intersection_update(set(rock))
    return len(common_chars)
