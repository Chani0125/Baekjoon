import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [list() for _ in range(n+1)]

for order in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, order))
    graph[b].append((a, order))

INF = n * m

dist = [INF for _ in range(n+1)]
dist[0] = 0

q = []
heapq.heappush(q, (0, 1, 0))

while q:
    time, node, order = heapq.heappop(q)
    if time > dist[node]:
        continue
    for now_node, now_order in graph[node]:
        if order == m or now_order > order:
            if dist[now_node] > time - time % m + now_order:
                dist[now_node] = time - time % m + now_order
                heapq.heappush(q, (dist[now_node], now_node, now_order))
        elif now_order < order:
            if dist[now_node] > time - time % m + m + now_order:
                dist[now_node] = time - time % m + m + now_order
                heapq.heappush(q, (dist[now_node], now_node, now_order))

print(dist[n])
