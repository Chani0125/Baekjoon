import sys, bisect

input = sys.stdin.readline

n = int(input())
a = sorted([tuple(map(int, input().split())) for _ in range(n)])
b = [a[i][1] for i in range(n)]

lis, pos = [b[0]], [0] * n
for i in range(1, n):
    if b[i] > lis[-1]:
        pos[i] = len(lis)
        lis.append(b[i])
    else:
        idx = bisect.bisect_left(lis, b[i])
        pos[i] = idx
        lis[idx] = b[i]

res = []
idx = len(lis) - 1
for i in range(n-1, -1, -1):
    if pos[i] == idx:
        idx -= 1
    else:
        res.append(a[i][0])
        
print(len(res))
print(*sorted(res), sep='\n')
