import sys
from collections import deque

n, q = map(int, sys.stdin.readline().strip().split())

graph = [list() for _ in range(n+1)]
for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

query = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(q)]

visited = [True] + [False, ] * n
for i in range(n):
    if len(graph[i]) == 1:
        visited[i] = True

loop_edge = False
for idx, val in enumerate(visited):
    if val == False:
        for i in graph[idx+1]:
            if visited[i] == False:
                loop_edge = (idx+1, i)
                break
    if loop_edge:
        break

while query:
    start, end = query.pop()
    visited = [True] + [False, ] * n
    stack = deque([start])
    while stack:
        pass
