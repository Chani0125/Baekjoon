import sys
from collections import deque


d = (1, 0), (0, 1), (-1, 0), (0, -1)

m, n = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

q = deque([(0, 0)])
num_break = [[m + n, ] * m for _ in range(n)]
num_break[0][0] = 0

while len(q) > 0:
    x, y = q.popleft()
    for dx, dy in d:
        a, b = x + dx, y + dy
        if 0 <= a < n and 0 <= b < m:
            if num_break[a][b] > num_break[x][y]:
                if (a, b) in q:
                    q.remove((a, b))
                q.append((a, b))
                num_break[a][b] = num_break[x][y] + maze[a][b]

print(num_break[n-1][m-1])
