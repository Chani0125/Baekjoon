import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(q, (abs(x), x))
    else:
        print(heapq.heappop(q)[1] if q else 0)
