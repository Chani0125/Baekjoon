import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().split())

    INF = n * 1000

    graph = [list() for i in range(n + 1)]
    distance = [INF, ] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            now_dist, now_node = heapq.heappop(q)
            if distance[now_node] < now_dist:
                continue
            for node, cost in graph[now_node]:
                sum_cost = now_dist + cost
                if sum_cost < distance[node]:
                    distance[node] = sum_cost
                    heapq.heappush(q, (sum_cost, node))

    dijkstra(c)

    time = max([d for d in distance if d != INF])
    num_infected = n + 1 - distance.count(INF)

    print(num_infected, time)

# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n, d, c = map(int, sys.stdin.readline().split())
#
#     INF = n * 1000
#
#     graph = [list() for i in range(n + 1)]
#     visited = [False, ] * (n + 1)
#     distance = [INF, ] * (n + 1)
#
#     for _ in range(d):
#         a, b, s = map(int, sys.stdin.readline().split())
#         graph[b].append((a, s))
#
#     def get_smallest_node():
#         min_value = INF
#         index = 0
#         for i in range(1, n + 1):
#             if distance[i] < min_value and not visited[i]:
#                 min_value = distance[i]
#                 index = i
#         return index
#
#     def dijkstra(start):
#         distance[start] = 0
#         visited[start] = True
#         for node, cost in graph[start]:
#             distance[node] = cost
#         for _ in range(n - 1):
#             now_node = get_smallest_node()
#             visited[now_node] = True
#             for node, cost in graph[now_node]:
#                 sum_cost = distance[node] + cost
#                 if sum_cost < distance[node]:
#                     distance[node] = sum_cost
#
#     dijkstra(c)
#
#     time = max([distance[i] for i in range(1, n + 1) if visited[i]])
#     num_infected = visited[1:].count(True)
#
#     print(num_infected, time)
