from collections import deque

# DFS 방식을 BFS로 바꿔볼 것
def bfs_passenger(location, distance):
    if location in locate:
        return distance, location
    distance_to = []
    d = (-1, 0), (0, -1), (0, 1), (1, 0)
    taxi_map[location[0]][location[1]] = 2
    exist = False
    for dx, dy in d:
        if 0 <= location[0] + dx < len(taxi_map) and 0 <= location[1] + dy < len(taxi_map):
            if taxi_map[location[0] + dx][location[1] + dy] == 0:
                search = bfs_passenger((location[0] + dx, location[1] + dy), distance + 1)
                if search is not None:
                    distance_to.append(search)
                    exist = True
    taxi_map[location[0]][location[1]] = 0
    if exist:
        ret = distance_to[0]
        for i in distance_to:
            if i[0] < ret[0]:
                ret = i
            if i[0] == ret[0]:
                if i[1][0] < ret[1][0]:
                    ret = i
                elif i[1][0] == ret[1][0] and i[1][1] < ret[1][1]:
                    ret = i
        return ret


def bfs_destination(destination, location, distance):
    if location == destination:
        return distance
    distance_to = []
    d = (0, 1), (1, 0), (0, -1), (-1, 0)
    taxi_map[location[0]][location[1]] = 2
    exist = False
    for dx, dy in d:
        if 0 <= location[0] + dx < len(taxi_map) and 0 <= location[1] + dy < len(taxi_map):
            if taxi_map[location[0] + dx][location[1] + dy] == 0:
                search = bfs_destination(destination, (location[0] + dx, location[1] + dy), distance + 1)
                if search is not None:
                    distance_to.append(search)
                    exist = True
    taxi_map[location[0]][location[1]] = 0
    if exist:
        return min(distance_to)


# ========== 입력 부분 ==========

# N: 지도 크기, M: 승객 수, fuel: 연료
N, M, fuel = map(int, input().split())

# taxi_map: 활동할 영역의 지도 (0: 빈칸, 1: 벽)
taxi_map = [list(map(int, input().split())) for _ in range(N)]

# locate_taxi: 택시의 칸의 행 번호와 열 번호
locate_taxi = tuple(map(int, input().split()))
locate_taxi = locate_taxi[0] - 1, locate_taxi[1] - 1

locate = {}

for _ in range(M):
    x_passenger, y_passenger, x_destination, y_destination = map(int, input().split())
    locate[(x_passenger - 1, y_passenger - 1)] = (x_destination - 1, y_destination - 1)

# ========== 연산 부분 ==========
while len(locate) > 0:
    passenger = bfs_passenger(locate_taxi, 0)
    if passenger is None:
        print(-1)
        break
    fuel -= passenger[0]
    if fuel < 0:
        print(-1)
        break
    distance_to_destination = bfs_destination(locate[passenger[1]], passenger[1], 0)
    if distance_to_destination is None:
        print(-1)
        break
    fuel -= distance_to_destination
    if fuel < 0:
        print(-1)
        break
    fuel += distance_to_destination * 2
    locate_taxi = locate[passenger[1]]
    del locate[passenger[1]]
else:
    print(fuel)