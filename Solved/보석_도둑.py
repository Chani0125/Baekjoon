import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

pq = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(pq, (m, -v))
for _ in range(k):
    c = int(sys.stdin.readline())
    heapq.heappush(pq, (c, 1))    

ans = 0
q = []
while pq:
    m, v = heapq.heappop(pq)
    if v == 1:
        if q:
            ans -= heapq.heappop(q)
    else:
        heapq.heappush(q, v)
            
print(ans)