import sys

input = sys.stdin.readline
v, e = map(int, input().split())
g = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

from heapq import heappop, heappush

hq = [(0, 1)]
visited = [False] * (v+1)
ans = 0

while hq:
    cost, node = heappop(hq)
    if visited[node]: continue
    visited[node] = True
    ans += cost
    for n, c in g[node]:
        if not visited[n]:
            heappush(hq, (c, n))

print(ans)
