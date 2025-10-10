from heapq import heappush, heappop

INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n)]

hq = []
dist = [INF] * n

while hq:
    d, v = heappop(hq)
    if dist[v] < d:
        continue
    for u, w in graph[v]:
        if dist[u] > d + w:
            dist[u] = d + w
            heappush(hq, (dist[u], u))