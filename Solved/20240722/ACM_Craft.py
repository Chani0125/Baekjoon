import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    d = [0] + list(map(int, sys.stdin.readline().split()))
    adj_list = [[] for _ in range(n+1)]
    in_degress = [0] * (n+1)
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        adj_list[x].append(y)
        in_degress[y] += 1
    w = int(sys.stdin.readline())
    
    cost = [i for i in d]
    
    q = deque()
    for i in range(1, n+1):
        if in_degress[i] == 0:
            q.append(i)
                 
    while q:
        node = q.popleft()
    
        for i in adj_list[node]:
            in_degress[i] -= 1
            cost[i] = max(cost[i], cost[node]+d[i])
            if in_degress[i] == 0:
                q.append(i)
