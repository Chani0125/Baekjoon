import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().strip().split())
tomatoes = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] for _ in range(h)]

d = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0)]

queue = deque()
day = 0

for i in range(len(tomatoes)):
    for j in range(len(tomatoes[i])):
        for k in range(len(tomatoes[i][j])):
            if tomatoes[i][j][k] == 1:
                queue.append((0, (i, j, k)))

while queue:
    day, (nx, ny, nz) = queue.popleft()
    for dx, dy, dz in d:
        x = nx + dx
        y = ny + dy
        z = nz + dz
        if 0 <= x < h and 0 <= y < n and 0 <= z < m:
            if tomatoes[x][y][z] == 0:
                tomatoes[x][y][z] = 1
                queue.append((day + 1, (x, y, z)))

for i in range(len(tomatoes)):
    for j in range(len(tomatoes[i])):
        for k in range(len(tomatoes[i][j])):
            if tomatoes[i][j][k] == 0:
                day = -1
                break
    if day == -1:
        break

print(day)
