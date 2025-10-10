import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n, k, x, y = map(int, input().split())
per, car = [[] for _ in range(n)], [[] for _ in range(n)]
for _ in range(x):
    s, e, d = map(int, input().split())
    s, e = s - 1, e - 1
    per[s].append((e, d))
    per[e].append((s, d))
for _ in range(y):
    s, e, d = map(int, input().split())
    s, e = s - 1, e - 1
    car[s].append((e, d))
    car[e].append((s, d))

q = [(0, 0)]
dist = [10**20] * n
dist[0] = 0

while q:
    cost, cur = heappop(q)
    if dist[cur] < cost: continue
    for e, d in per[cur]:
        if cost + d < dist[e]:
            dist[e] = cost + d
            heappush(q, (cost + d, e))
    if cost >= k:
        for e, d in car[cur]:
            if cost + d < dist[e]:
                dist[e] = cost + d
                heappush(q, (cost + d, e))
    else:
        for e, d in car[cur]:
            if k + d < dist[e]:
                dist[e] = k + d
                heappush(q, (k + d, e))

print(dist[n-1])