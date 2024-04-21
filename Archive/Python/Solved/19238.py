import sys
from collections import deque
import heapq

# N: 지도 크기, M: 승객 수, fuel: 연료
N, M, fuel = map(int, sys.stdin.readline().strip().split())

# taxi_map: 활동할 영역의 지도 (0: 빈칸, 1: 벽)
taxi_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# locate_taxi: 택시의 칸의 행 번호와 열 번호
locate_taxi = tuple(map(int, sys.stdin.readline().strip().split()))
locate_taxi = locate_taxi[0] - 1, locate_taxi[1] - 1

locate_dest = []
num_pass = 0

# 승객 정보 입력
for _ in range(M):
    x_pass, y_pass, x_dest, y_dest = map(int, sys.stdin.readline().strip().split())
    taxi_map[x_pass - 1][y_pass - 1] = 2 + len(locate_dest)
    locate_dest.append((x_dest - 1, y_dest - 1))
    num_pass += 1

d = (-1, 0), (0, -1), (0, 1), (1, 0)

while num_pass != 0:
    # 가장 가까운 승객 BFS 탐색
    visited = [[False, ] * N for _ in range(N)]
    visited[locate_taxi[0]][locate_taxi[1]] = True
    # queue = deque([(0, locate_taxi)])
    queue = []
    heapq.heappush(queue, (0, locate_taxi))
    while queue:
        # dist_pass, (now_x, now_y) = queue.popleft()
        dist_pass, (now_x, now_y) = heapq.heappop(queue)
        if taxi_map[now_x][now_y] > 1:
            idx_pass = taxi_map[now_x][now_y] - 2
            taxi_map[now_x][now_y] = 0
            break
        for dx, dy in d:
            x = now_x + dx
            y = now_y + dy
            if 0 <= x < N and 0 <= y < N:
                if taxi_map[x][y] != 1 and not visited[x][y]:
                    # queue.append((dist_pass + 1, (x, y)))
                    heapq.heappush(queue, (dist_pass + 1, (x, y)))
                    visited[x][y] = True
    else:
        print(-1)
        break
    # 승객까지 이동
    fuel -= dist_pass
    if fuel < 0:
        print(-1)
        break

    # 목적지까지 BFS 탐색
    visited = [[False, ] * N for _ in range(N)]
    visited[now_x][now_y] = True
    # queue = deque([(0, (now_x, now_y))])
    queue = []
    heapq.heappush(queue, (0, (now_x, now_y)))
    while queue:
        # dist_dest, (now_x, now_y) = queue.popleft()
        dist_dest, (now_x, now_y) = heapq.heappop(queue)
        if (now_x, now_y) == locate_dest[idx_pass]:
            num_pass -= 1
            break
        for dx, dy in d:
            x = now_x + dx
            y = now_y + dy
            if 0 <= x < N and 0 <= y < N:
                if taxi_map[x][y] != 1 and not visited[x][y]:
                    # queue.append((dist_dest + 1, (x, y)))
                    heapq.heappush(queue, (dist_dest + 1, (x, y)))
                    visited[x][y] = True
    else:
        print(-1)
        break
    # 목적지까지 이동
    fuel -= dist_dest
    if fuel < 0:
        print(-1)
        break

    fuel += dist_dest * 2
    locate_taxi = locate_dest[idx_pass]
    # print("Debug:", idx_pass, dist_dest, dist_pass, fuel, locate_taxi)
else:
    print(fuel)
# print("Debug:", idx_pass, dist_pass, dist_dest, fuel, (now_x, now_y))