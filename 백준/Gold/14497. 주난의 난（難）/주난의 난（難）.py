import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y, n, m):
    u[x][y] = True
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not u[nx][ny]:
                if v[nx][ny] == '0':
                    dfs(nx, ny, n, m)
                else:
                    u[nx][ny] = True

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
v = [list(input().strip()) for _ in range(n)]
u = [[False] * m for _ in range(n)]

jump = 0
while u[x2-1][y2-1] == False:
    u = [[False] * m for _ in range(n)]
    dfs(x1-1, y1-1, n, m)
    jump += 1
    for i in range(n):
        for j in range(m):
            if u[i][j]:
                v[i][j] = '0'
        
print(jump)