import sys

input = sys.stdin.readline
n, m = map(int, input().split())
v = [[*map(int, input().split())] for _ in range(n)]
virus = []
for x in range(n):
    for y in range(m):
        if v[x][y] == 2:
            virus.append((x, y))

from itertools import combinations

res = 0
for w in combinations(range(n*m), 3):
    w = [divmod(i, m) for i in w]
    flag = False
    for x, y in w:
        if v[x][y]:
            flag = True
            break
    if flag: continue

    parent = [[(i, j) for j in range(m)] for i in range(n)]
    rank = [[0] * m for _ in range(n)] 
    
    def find(x):
        if parent[x[0]][x[1]] == x: return x
        parent[x[0]][x[1]] = find(parent[x[0]][x[1]])
        return parent[x[0]][x[1]]

    def union(x, y):
        x, y = find(x), find(y)
        if x == y: return
        if rank[x[0]][x[1]] > rank[y[0]][y[1]]:
            x, y = y, x
        parent[x[0]][x[1]] = parent[y[0]][y[1]]
        if rank[x[0]][x[1]] == rank[y[0]][y[1]]:
            rank[y[0]][y[1]] += 1
    
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for x in range(n):
        for y in range(m):
            if v[x][y] == 1 or (x, y) in w: continue
            for dx, dy in d:
                if x+dx < 0 or x+dx >= n: continue
                if y+dy < 0 or y+dy >= m: continue
                if (x+dx, y+dy) in w: continue
                if v[x+dx][y+dy] == 1: continue
                union((x, y), (x+dx, y+dy))
    
    virus_parent = set()
    for x, y in virus:
        virus_parent.add(find((x, y)))
    
    ans = 0
    for x in range(n):
        for y in range(m):
            if v[x][y] == 0 and ((x, y) not in w) and (find((x, y)) not in virus_parent):
                ans += 1
    
    res = max(res, ans)

print(res)