import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split())
tomatoes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

queue = deque()
day = 0

for i in range(len(tomatoes)):
    for j in range(len(tomatoes[i])):
        if tomatoes[i][j] == 1:
            queue.append((0, (i, j)))

while queue:
    day, (nx, ny) = queue.popleft()
    for dx, dy in d:
        x = nx + dx
        y = ny + dy
        if 0 <= x < n and 0 <= y < m:
            if tomatoes[x][y] == 0:
                tomatoes[x][y] = 1
                queue.append((day + 1, (x, y)))

for i in range(len(tomatoes)):
    for j in range(len(tomatoes[i])):
        if tomatoes[i][j] == 0:
            day = -1
            break
    if day == -1:
        break

print(day)
