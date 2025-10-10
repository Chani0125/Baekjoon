import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    f = int(input())
    v = dict()

    p = []
    r = []

    def find(x):
        if p[x] == x: return x
        p[x] = find(p[x])
        return p[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x == y: return
        if r[x] > r[y]: x, y = y, x
        p[x] = p[y]
        r[y] += r[x]

    for _ in range(f):
        a, b = input().split()
        if a not in v:
            v[a] = len(v)
            p.append(v[a])
            r.append(1)
        if b not in v:
            v[b] = len(v)
            p.append(v[b])
            r.append(1)
        a, b = v[a], v[b]
        
        union(a, b)
        x = find(a)
        
        print(r[x])