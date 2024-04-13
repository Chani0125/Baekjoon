import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y, k, n, m):
    u[x][y] = True
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not u[nx][ny]:
                if abs(v[x][y] - v[nx][ny]) <= k:
                    dfs(nx, ny, k, n, m)
                    

n, m, k = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]
u = [[False] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if not u[i][j]:
            ans += 1
            dfs(i, j, k, n, m)

print(ans)