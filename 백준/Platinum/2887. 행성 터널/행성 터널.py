import sys
import heapq as hq

input = sys.stdin.readline
n = int(input())
a = [(i, tuple(map(int, input().split()))) for i in range(n)]

x = sorted(a, key=lambda x: x[1][0])
y = sorted(a, key=lambda x: x[1][1])
z = sorted(a, key=lambda x: x[1][2])

def cost(a, b):
    return min(abs(a[1][0] - b[1][0]), abs(a[1][1] - b[1][1]), abs(a[1][2] - b[1][2]))

graph = [[] for _ in range(n)]

for i in range(n-1):
    graph[x[i][0]].append((x[i+1][0], cost(x[i], x[i+1])))
    graph[x[i+1][0]].append((x[i][0], cost(x[i], x[i+1])))
    graph[y[i][0]].append((y[i+1][0], cost(y[i], y[i+1])))
    graph[y[i+1][0]].append((y[i][0], cost(y[i], y[i+1])))
    graph[z[i][0]].append((z[i+1][0], cost(z[i], z[i+1])))
    graph[z[i+1][0]].append((z[i][0], cost(z[i], z[i+1])))

# print(*graph, sep='\n')
pq = []
hq.heappush(pq, (0, 0))
visited = [False] * n
res = []
while pq and len(res) < n:
    # print(pq)
    c, d = hq.heappop(pq)
    if visited[d]: continue
    visited[d] = True
    res.append(c)
    for dd, cc in graph[d]:
        if not visited[dd]:
            hq.heappush(pq, (cc, dd))
            
# print(res)
print(sum(res))