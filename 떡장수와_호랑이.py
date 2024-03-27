import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, s):
    if x == 0:
        return s
    for i in range(9):
        if i != y and graph[x-1][i]:
            return dfs(x-1, i, [i] + s)
    return []

n = int(input())
graph = [[False] * 9 for _ in range(n)]
visited = [[False] * 9 for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in a[1:]:
        graph[i][j-1] = True

ans = []
for i in range(9):
    if graph[n-1][i]:
        tmp = dfs(n-1, i, [i])
        if len(tmp) == n:
            ans = tmp
            break
if ans:
    for i in ans:
        print(i+1)
else:
    print(-1)