import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
a.sort()

pq = []
for s, e in a:
    if pq and pq[0][0] <= s:
        heappop(pq)
    heappush(pq, (e, s))

print(len(pq))