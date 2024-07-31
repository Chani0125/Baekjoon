import sys

input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g[b].append((c, a))

p, q = map(int, input().split())
homes = list(map(int, input().split()))
convs = list(map(int, input().split()))

from heapq import heappush, heappop

INF = 10000 * n
min_dist = INF
ans = 0

pq = []
dist = [(INF, n+1), ] * (n+1)

for h in homes:
    heappush(pq, (0, h, h))
    dist[h] = (0, h)

while pq:
    cost, node, home = heappop(pq)
    if cost > dist[node][0]: continue
    
    for n_cost, n_node in g[node]:
        if cost + n_cost < dist[n_node][0]:
            dist[n_node] = (cost + n_cost, home)
            heappush(pq, (cost + n_cost, n_node, home))

for conv in convs:
    if dist[conv][0] < min_dist:
        min_dist = dist[conv][0]
        ans = dist[conv][1]
    elif dist[conv][0] == min_dist and dist[conv][1] < ans:
        min_dist = dist[conv][0]
        ans = dist[conv][1]
        
print(ans)