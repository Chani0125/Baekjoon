import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    q = []
    for _ in range(k):
        o, n = sys.stdin.readline().strip().split()
        n = int(n)
        if o == "I":
            heapq.heappush(q, n)
        elif len(q) > 0:
            if n == -1:
                heapq.heappop(q)
            else:
                q = heapq.nsmallest(len(q) - 1, q)
                heapq.heapify(q)
    if len(q) == 0:
        print("EMPTY")
    else:
        print(heapq.nlargest(1, q).pop(), heapq[0])
