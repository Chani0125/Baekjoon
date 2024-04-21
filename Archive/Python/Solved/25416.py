import sys
from collections import deque

grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
r, c = map(int, sys.stdin.readline().strip().split())

INF = 5 * 5
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
distance = [[INF, ] * 5 for _ in range(5)]

queue = deque([(r, c)])
distance[r][c] = 0
ans = INF

while queue:
    x, y = queue.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            if distance[nx][ny] > distance[x][y] + 1 and grid[nx][ny] != -1:
                distance[nx][ny] = distance[x][y] + 1
                if grid[nx][ny] == 1:
                    if ans > distance[nx][ny]:
                        ans = distance[nx][ny]
                else:
                    queue.append((nx, ny))

print(-1 if ans == INF else ans)
