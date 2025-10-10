import sys

input = sys.stdin.readline
n = int(input())

v = [[*map(int, input().split())] for _ in range(n)]

dir = ((1, 0), (-1, 0), (0, 1), (0, -1))

p = [i*n+j for i in range(n) for j in range(n)]
r = [0] * (n**2)

def find(x):
    if p[x] == x: return x
    return find(p[x])

def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    if r[x] < r[y]: x, y = y, x
    p[y] = p[x]
    if r[x] == r[y]:
        r[x] += 1

for x in range(n):
    for y in range(n):
        if v[x][y] == 0:
            p[x*n+y] = -1
            continue
        
        for dx, dy in dir:
            if 0 <= x+dx < n and 0 <= y+dy < n and v[x+dx][y+dy]:
                union(x*n+y, (x+dx)*n+y+dy)

lands = set()
for x in range(n):
    for y in range(n):
        if p[x*n+y] >= 0:
            lands.add(find(x*n+y))

from collections import deque

ans = []
for i in lands:
    dist = [[n**2+1] * n for _ in range(n)]
    s = deque()
    s.append((0, (i//n, i%n)))
    flag = False
    
    while s:
        d, (x, y) = s.popleft()
        if d >= dist[x][y]: continue
        dist[x][y] = d
        
        for dx, dy in dir:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if v[x+dx][y+dy] and find((x+dx)*n+(y+dy)) == i:
                    if d < dist[x+dx][y+dy]:
                        s.append((d, (x+dx, y+dy)))
                elif v[x+dx][y+dy]:
                    ans.append(d)
                    break
                else:
                    if d+1 < dist[x+dx][y+dy]:
                        s.append((d+1, (x+dx, y+dy)))
        if flag:
            break

print(min(ans))
    