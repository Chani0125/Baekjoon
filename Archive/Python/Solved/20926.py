import sys
import heapq


w, h = map(int, sys.stdin.readline().strip().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(h)]

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

INF = w * h * 10
slippery_time = [[INF, ] * w for _ in range(h)]

q = []

is_find = False
for i in range(h):
    for j in range(w):
        if maze[i][j] == 'T':
            maze[i][j] = '0'
            heapq.heappush(q, (0, (i, j)))
            slippery_time[i][j] = 0
            is_find = True
            break
    if is_find:
        break

while q:
    n_time, (nx, ny) = heapq.heappop(q)
    if n_time > slippery_time[nx][ny]:
        continue
    for dx, dy in d:
        x, y = nx + dx, ny + dy
        sum_time = n_time
        if 0 <= x < h and 0 <= y < w:
            if maze[x][y] == 'E':
                if slippery_time[x][y] > sum_time + int(maze[nx][ny]):
                    slippery_time[x][y] = sum_time + int(maze[nx][ny])
                continue
            elif maze[x][y] == 'R':
                continue
            elif maze[x][y] == 'H':
                continue
        while 0 <= x < h and 0 <= y < w:
            if maze[x][y] == 'E':
                if slippery_time[x][y] > sum_time + int(maze[x-dx][y-dy]):
                    slippery_time[x][y] = sum_time + int(maze[x-dx][y-dy])
                break
            elif maze[x][y] == 'R':
                if slippery_time[x-dx][y-dy] > sum_time:
                    slippery_time[x-dx][y-dy] = sum_time
                    heapq.heappush(q, (sum_time, (x-dx, y-dy)))
                break
            elif maze[x][y] == 'H':
                break
            sum_time += int(maze[x-dx][y-dy])
            x += dx
            y += dy

is_find = False
for i in range(h):
    for j in range(w):
        if maze[i][j] == 'E':
            ans = slippery_time[i][j]
            if ans == INF:
                ans = -1
            is_find = True
            break
    if is_find:
        break

print(ans)