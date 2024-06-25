import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    a_min = min(a)
    a = [*map(lambda x: x - a_min, a)]
    
    a_max, last = 0, 0
    a_max_list = []
    for idx, val in enumerate(a):
        if val >= a_max: last, a_max = idx, val
        a_max_list.append(a_max)

    a_max = 0
    for idx, val in enumerate(a[last:][::-1]):
        a_max = max(a_max, val)
        a_max_list[-idx-1] = a_max

    print(sum(a_max_list) - sum(a))
