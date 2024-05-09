import sys
import heapq as hq

n, m = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a-1].append((b-1, c))
    edges[b-1].append((a-1, c))

pq, roads = [], []
visited = [False] * n
for i in edges[0]:
    hq.heappush(pq, (i[1], i[0]))
visited[0] = True

while pq:
    c, b = hq.heappop(pq)
    if visited[b]: continue
    visited[b] = True
    hq.heappush(roads, -c)
    for i in edges[b]:
        if not visited[i[0]]:
            hq.heappush(pq, (i[1], i[0]))

hq.heappop(roads)
res = 0
while roads:
    res -= hq.heappop(roads)
print(res)