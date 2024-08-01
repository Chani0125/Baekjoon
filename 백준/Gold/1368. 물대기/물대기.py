import sys

input = sys.stdin.readline
n = int(input())
w = [int(input()) for _ in range(n)]

adj_m = [list(map(int, input().split())) for _ in range(n)]

from heapq import heappush, heappop

pq = []
for i in range(n):
    heappush(pq, (w[i], i))

visited = [False] * n
total = 0

while pq:
    cost, node = heappop(pq)
    if visited[node]: continue
    visited[node] = True
    total += cost
    
    for next in range(n):
        if not visited[next]:
            heappush(pq, (adj_m[node][next], next))

print(total)