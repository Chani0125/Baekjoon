import sys

input = sys.stdin.readline
r, c = map(int, input().split())
m = [[*(input().strip())] for _ in range(r)]
a, b = (-1, -1), (-1, -1)
for i in range(r):
    for j in range(c):
        if m[i][j] == 'L':
            if a == (-1, -1):
                a = (i, j)
            else:
                b = (i, j)
                break

v = [[(1 if m[i][j] == 'X' else 0) for j in range(c)] for i in range(r)]


 
# import heapq as hq

# INF = 1500 ** 2
# direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# dist = [[INF] * c for _ in range(r)]

# pq = [(0, a)]
# dist[a[0]][a[1]] = 0
# while pq: 
#     d, (x, y) = hq.heappop(pq)
#     if d > dist[x][y]: continue
    
#     for dx, dy in direct:
#         if x+dx < 0 or x+dx >= r: continue
#         if y+dy < 0 or y+dy >= c: continue
#         if d + v[x+dx][y+dy] < dist[x+dx][y+dy]:
#             dist[x+dx][y+dy] = d + v[x+dx][y+dy]
#             hq.heappush(pq, (dist[x+dx][y+dy], (x+dx, y+dy)))

# ice = dist[b[0]][b[1]]
# print((ice+1)//2)

