import sys
import heapq

n = int(sys.stdin.readline())
space = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

start = 0, 0
is_find = False
for x, arr in enumerate(space):
    for y, val in enumerate(arr):
        if val == 9:
            start = x, y
            space[x][y] = 0
            is_find = True
            break
    if is_find:
        break

size = 2
accumulated_food = 0
time = 0

d = (-1, 0), (0, -1), (0, 1), (1, 0)

visited = [[False, ] * n for _ in range(n)]
visited[start[0]][start[1]] = True

queue = []
heapq.heappush(queue, (0, start))

while queue:
    now_cost, (now_x, now_y) = heapq.heappop(queue)
    if 0 < space[now_x][now_y] < size:
        space[now_x][now_y] = 0
        accumulated_food += 1
        if accumulated_food == size:
            accumulated_food = 0
            size += 1
        time += now_cost
        visited = [[False, ] * n for _ in range(n)]
        queue = []
        now_cost = 0
        visited[now_x][now_y] = True
        # print("\n".join(map(str, space)))
        # print(size, accumulated_food, time)
    for dx, dy in d:
        x = now_x + dx
        y = now_y + dy
        if 0 <= x < n and 0 <= y < n:
            if not visited[x][y]:
                if space[x][y] <= size:
                    heapq.heappush(queue, (now_cost + 1, (x, y)))
                    visited[x][y] = True

print(time)


