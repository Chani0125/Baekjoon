import sys

input = sys.stdin.readline
n, m = map(int, input().split())

p = [*range(n+1)]
r = [0] * (n+1)

def find(x):
    if p[x] == x: return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    if r[x] > r[y]: x, y = y, x
    p[x] = p[y]
    if r[x] == r[y]: r[y] += 1

for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')