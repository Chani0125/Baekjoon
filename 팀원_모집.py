import sys

n, m = map(int, sys.stdin.readline().split())
v = [[0] * n for _ in range(m)]

for i in range(m):
    o, *p =  map(int, sys.stdin.readline().split())
    for j in p:
        v[i][j-1] = 1

ans = []
u = zip(*v)
p = [0] * n
for i in range(n):
    if p[i]:
        continue
    s = 0
    qu = []
    for j in range(m):
        if v[j][i]:
            s += 1
            qu.append(j)
    if s == 1:
        ans.append(qu[0])
        for j in range(m):
            if v[qu[0]][j]:
                p[j] = 1


        
        
print(p)
print()

for i in v:
    print(i)
print()
for i in u:
    print(i)