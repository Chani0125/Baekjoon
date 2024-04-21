# import sys
# from collections import deque
#
#
# d = (1, 0), (0, 1), (-1, 0), (0, -1)
#
# m, n = map(int, sys.stdin.readline().split())
# maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
#
# q = deque([(0, 0)])
# num_break = [[m + n, ] * m for _ in range(n)]
# num_break[0][0] = 0
#
# while len(q) > 0:
#     x, y = q.popleft()
#     for dx, dy in d:
#         a, b = x + dx, y + dy
#         if 0 <= a < n and 0 <= b < m:
#             if num_break[a][b] > num_break[x][y]:
#                 if (a, b) in q:
#                     q.remove((a, b))
#                 q.append((a, b))
#                 num_break[a][b] = num_break[x][y] + maze[a][b]
#
# print(num_break[n-1][m-1])

import heapq

# 미로 정보 입력
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# 방문 여부와 최단거리를 저장할 리스트 초기화
visited = [[False] * m for _ in range(n)]
distance = [[float('inf')] * m for _ in range(n)]

# 시작점 설정
start = (0, 0)
distance[start[0]][start[1]] = 0

# 우선순위 큐 생성
queue = []
heapq.heappush(queue, (0, start))

# 다익스트라 알고리즘 수행
while queue:
    # 우선순위 큐에서 최단거리가 가장 짧은 노드 선택
    current_dist, current = heapq.heappop(queue)

    # 이미 방문한 노드인 경우 skip
    if visited[current[0]][current[1]]:
        continue

    # 현재 노드 방문 처리
    visited[current[0]][current[1]] = True

    # 도착점에 도달한 경우
    if current[0] == n - 1 and current[1] == m - 1:
        break

    # 상하좌우로 이동하는 경우의 수 계산
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = current[0] + dx[i]
        ny = current[1] + dy[i]

        # 미로를 벗어나는 경우 skip
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        # 벽인 경우 부숴서 이동해야 함
        if maze[nx][ny] == 1:
            # 벽을 한 번도 부수지 않은 경우
            if distance[nx][ny] > current_dist + 1:
                distance[nx][ny] = current_dist + 1
                heapq.heappush(queue, (distance[nx][ny], (nx, ny)))
        # 벽이 아닌 경우
        else:
            if distance[nx][ny] > current_dist:
                distance[nx][ny] = current_dist
                heapq.heappush(queue, (distance[nx][ny], (nx, ny)))

# 도착점까지의 최단거리 출력
if distance[n-1][m-1] == float('inf'):
    print(-1)
else:
    print(distance[n-1][m-1])