import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
v = [*map(int, input().split())]

u = [bisect_left(v, -v[i]) for i in range(n)]
m = 2000000001

a, b = -1, n
for i in range(n):
    if u[i] > 0 and u[i]-1 != i:
        p = abs(v[i] + v[u[i]-1])
        if p < m:
            m = p
            a, b = v[i], v[u[i]-1]
    
    if u[i] < n and u[i] != i:
        p = abs(v[i] + v[u[i]])
        if p < m:
            m = p
            a, b = v[i], v[u[i]]

print(*sorted([a, b]))