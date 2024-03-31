import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

adj_list = [[] for _ in range(n + 1)]
in_degrees = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    in_degrees[b] += 1

q = deque()
for i in range(1, n + 1):
    if in_degrees[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    print(node, end=' ')
    
    for i in adj_list[node]:
        in_degrees[i] -= 1
        if in_degrees[i] == 0:
            q.append(i)