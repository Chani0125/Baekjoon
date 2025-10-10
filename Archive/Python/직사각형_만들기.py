import sys

n = int(input())
l = sorted([*map(int, input().split())])

p = [[0] * n for _ in range(n)]
s = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        a = l[i] + l[j]
        b = l[i] * l[j]
        
        p[i][j] = a
        if p[i][j-1] == a or (i > 0 and p[i-1][j] == a and s[i-1][j]):
            s[i][j] = 0
        else:
            s[i][j] = b

d = dict()
for i in range(n):
    for j in range(len(p[i])):
        if p[i][j] not in d:
            d[p[i][j]] = 0
        d[p[i][j]] += s[i][j]

print(max(d.values()))
