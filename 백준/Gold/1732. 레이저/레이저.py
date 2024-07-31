import sys

input = sys.stdin.readline
n = int(input())
v = [list(map(int, input().split())) for _ in range(n)]

from functools import cmp_to_key

def ccw(a, b):
    return a[0]*b[1] - a[1]*b[0]

def ccw_cmp(a, b):
    c = ccw(a, b)
    if c: return c
    if a[0] * b[0] < 0:
        return a[0] - b[0]
    if a[0] == b[0]:
        return a[1] - b[1]
    return abs(a[0]) - abs(b[0])

v.sort(key=cmp_to_key(ccw_cmp))

prev = -1
ans = []
for i in range(1, n):
    if ccw(v[i-1], v[i]) == 0:
        prev = max(prev, v[i-1][2])
        if prev >= v[i][2]:
            ans.append(v[i])
    else:
        prev = -1

ans.sort(key=lambda x: (x[0], x[1]))
for x, y, z in ans:
    print(x, y)