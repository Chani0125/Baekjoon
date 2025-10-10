import sys

input = sys.stdin.readline
n, m = map(int, input().split())
v = [list(map(int, list(input().strip()))) for _ in range(n)]

from collections import deque

INF = 100 * 100 + 1
dist = [[INF] * m for _ in range(n)]

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = deque()
q.append((1, (0, 0)))
while q:
    d, (x, y) = q.popleft()
    if d >= dist[x][y]: continue
    dist[x][y] = d
    if x == n-1 and y == m-1: break
    
    for dx, dy in direct:
        if x+dx < 0 or x+dx >= n: continue
        if y+dy < 0 or y+dy >= m: continue
        if v[x+dx][y+dy] and d+1 < dist[x+dx][y+dy]:
            q.append((d+1, (x+dx, y+dy)))
    
print(dist[n-1][m-1])
    