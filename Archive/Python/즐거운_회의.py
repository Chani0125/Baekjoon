import sys

n, m, t = map(int, input().split())
v = [(tuple(map(int, input().split())), i+1) for i in range(n)]
u = [tuple(map(int, input().split())) for _ in range(m)]

v.sort(key=lambda x: (x[0][0], x[0][1]))

now = [[] for _ in range(t+1)]
for (a, b), idx in v:
    for i in range(a, b):
        now[i].append(idx)

c = [[False] * (n+1) for _ in range(n+1)]
for a, b in u:
    c[a][b] = True
    c[b][a] = True

from itertools import combinations

for i in range(t):
    ans = 0
    
    for a, b in combinations(now[i], 2):
        if c[a][b] == True: ans += 1

    print(ans)

print(*v, sep='\n')
