import sys
from itertools import combinations

input = sys.stdin.readline

a = input().strip()
n = int(input())

p = sorted([input().strip() for _ in range(n)])
q = [[a.count(i) + s.count(i) for i in 'LOVE'] for s in p]
r = []

for idx, v in enumerate(q):
    res = 1
    for i, j in combinations(v, 2):
        res *= i + j
    r.append((res % 100, idx))

r.sort(reverse=True, key=lambda x: (x[0]))

print(p[r[0][1]])