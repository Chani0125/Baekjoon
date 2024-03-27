import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[1, ] * n for _ in range(n)]

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1-1][n2-1] = 0

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 0 and graph[k][j] == 0:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    ans = 0
    for j in range(n):
        if graph[i][j] == 1 and graph[j][i] == 1:
            ans += 1
    print(ans)
