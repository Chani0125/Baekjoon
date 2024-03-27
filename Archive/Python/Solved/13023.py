import sys


def dfs(v, d):
    visit[v] = True
    for i in g[v]:
        if not visit[i]:
            if d == 4:
                return True
            ans = dfs(i, d+1)
            if ans:
                return True
            else:
                visit[i] = False
    return False


n, m = map(int, sys.stdin.readline().split())
r = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
g = [set() for _ in range(n)]
for x, y in r:
    g[x].add(y)
    g[y].add(x)
visit = [False for _ in range(n)]
for i in range(n):
    if dfs(i, 1):
        print(1)
        break
else:
    print(0)
