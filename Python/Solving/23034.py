import sys

n, m = map(int, sys.stdin.readline().strip().split())

INF = n * (10 ** 5)
graph = [[INF, ] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = c
    graph[b][a] = c

q = int(sys.stdin.readline())

for _ in range(q):
    x, y = map(int, sys.stdin.readline().strip().split())