import sys
from math import factorial
from collections import deque

n, r, g, b = map(int, sys.stdin.readline().strip().split())

level_case = []

for i in range(1, n+1):
    now = [0, 0, 0]
    now[0] += 1
    if i % 2 == 0:
        now[1] += (factorial(i) // pow(factorial(i//2), 2))
    if i % 3 == 0:
        now[2] += factorial(i) // pow(factorial(i//3), 3)
    level_case.append(now)
    
graph = []
for i in range(n):
    now = []
    for j in range(3):
        if level_case[i][j] != 0:
            now.append(j)
    graph.append(now)

q = deque([(n, r, g, b, 1)])
num_case = 0

while q:
    nfloor, nr, ng, nb, ncase = q.pop()
    if nr < 0 or ng < 0 or nb < 0:
        continue
    if nfloor == 0:
        num_case += ncase
        continue
    for i in graph[nfloor - 1]:
        if i == 0:
            q.append((nfloor - 1, nr - nfloor, ng, nb, ncase * level_case[nfloor -1][i]))
            q.append((nfloor - 1, nr, ng - nfloor, nb, ncase * level_case[nfloor -1][i]))
            q.append((nfloor - 1, nr, ng, nb - nfloor, ncase * level_case[nfloor -1][i]))
        if i == 1:
            q.append((nfloor - 1, nr - nfloor // 2, ng - nfloor // 2, nb, ncase * level_case[nfloor -1][i]))
            q.append((nfloor - 1, nr, ng - nfloor // 2, nb - nfloor // 2, ncase * level_case[nfloor -1][i]))
            q.append((nfloor - 1, nr - nfloor // 2, ng, nb - nfloor // 2, ncase * level_case[nfloor -1][i]))
        if i == 2:
            q.append((nfloor - 1, nr - nfloor // 3, ng - nfloor // 3, nb - nfloor // 3, ncase * level_case[nfloor -1][i]))

print(num_case)